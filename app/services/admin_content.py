from sqlalchemy import text, bindparam
from app.core.database import engine


def upsert_locale_sections(lang: str, sections: list[dict]) -> None:
    rows = [
        {"lang": lang, "section": s["section"], "key": k, "value": v}
        for s in sections
        for k, v in s["values"].items()
    ]
    if not rows:
        return
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO locale_strings (lang, section, key, value)
            VALUES (:lang, :section, :key, :value)
            ON CONFLICT (lang, section, key) DO UPDATE SET value = EXCLUDED.value
        """), rows)


def replace_education(lang: str, subjects: list[dict]) -> None:
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM education_subjects WHERE lang = :lang"), {"lang": lang})
        if subjects:
            conn.execute(text("""
                INSERT INTO education_subjects (lang, position, label, value)
                VALUES (:lang, :position, :label, :value)
            """), [
                {"lang": lang, "position": i, "label": s["label"], "value": s["value"]}
                for i, s in enumerate(subjects)
            ])


def replace_skill_categories(lang: str, categories: list[dict]) -> None:
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM skill_categories WHERE lang = :lang"), {"lang": lang})
        if categories:
            conn.execute(text("""
                INSERT INTO skill_categories (lang, position, title, description)
                VALUES (:lang, :position, :title, :description)
            """), [
                {"lang": lang, "position": i, "title": c["title"], "description": c["description"]}
                for i, c in enumerate(categories)
            ])


def upsert_experience(lang: str, entries: list[dict]) -> None:
    slugs = [e["id"] for e in entries]

    with engine.begin() as conn:
        if entries:
            conn.execute(text("""
                INSERT INTO experience_entries (slug, logo, period, is_current)
                VALUES (:slug, :logo, :period, :is_current)
                ON CONFLICT (slug) DO UPDATE SET
                    logo = EXCLUDED.logo,
                    period = EXCLUDED.period,
                    is_current = EXCLUDED.is_current
            """), [
                {"slug": e["id"], "logo": e["logo"], "period": e["period"], "is_current": e["is_current"]}
                for e in entries
            ])

        exp_id: dict[str, int] = {}
        if slugs:
            rows = conn.execute(
                text("SELECT id, slug FROM experience_entries WHERE slug IN :slugs")
                .bindparams(bindparam("slugs", expanding=True)),
                {"slugs": slugs},
            ).fetchall()
            exp_id = {r.slug: r.id for r in rows}

        if entries:
            conn.execute(text("""
                INSERT INTO experience_translations (experience_id, lang, company, role, description)
                VALUES (:experience_id, :lang, :company, :role, :description)
                ON CONFLICT (experience_id, lang) DO UPDATE SET
                    company = EXCLUDED.company, role = EXCLUDED.role, description = EXCLUDED.description
            """), [
                {
                    "experience_id": exp_id[e["id"]],
                    "lang": lang,
                    "company": e["company"],
                    "role": e["role"],
                    "description": e["description"],
                }
                for e in entries
            ])

        for e in entries:
            conn.execute(
                text("DELETE FROM experience_responsibilities WHERE experience_id = :id AND lang = :lang"),
                {"id": exp_id[e["id"]], "lang": lang},
            )

        resp_rows = [
            {"experience_id": exp_id[e["id"]], "lang": lang, "position": i, "text": r}
            for e in entries
            for i, r in enumerate(e["responsibilities"])
        ]
        if resp_rows:
            conn.execute(text("""
                INSERT INTO experience_responsibilities (experience_id, lang, position, text)
                VALUES (:experience_id, :lang, :position, :text)
            """), resp_rows)

        if slugs:
            conn.execute(
                text("DELETE FROM experience_entries WHERE slug NOT IN :slugs")
                .bindparams(bindparam("slugs", expanding=True)),
                {"slugs": slugs},
            )
        else:
            conn.execute(text("DELETE FROM experience_entries"))


def upsert_projects(lang: str, items: list[dict]) -> None:
    slugs = [i["id"] for i in items]

    with engine.begin() as conn:
        if items:
            conn.execute(text("""
                INSERT INTO projects (slug, lang_code, stars, is_private, url)
                VALUES (:slug, :lang_code, :stars, :is_private, :url)
                ON CONFLICT (slug) DO UPDATE SET
                    lang_code = EXCLUDED.lang_code,
                    stars = EXCLUDED.stars,
                    is_private = EXCLUDED.is_private,
                    url = EXCLUDED.url
            """), [
                {
                    "slug": i["id"],
                    "lang_code": i["lang_code"],
                    "stars": i["stars"],
                    "is_private": i["is_private"],
                    "url": i["url"],
                }
                for i in items
            ])

        proj_id: dict[str, int] = {}
        if slugs:
            rows = conn.execute(
                text("SELECT id, slug FROM projects WHERE slug IN :slugs")
                .bindparams(bindparam("slugs", expanding=True)),
                {"slugs": slugs},
            ).fetchall()
            proj_id = {r.slug: r.id for r in rows}

        if items:
            conn.execute(text("""
                INSERT INTO project_translations (project_id, lang, name, description)
                VALUES (:project_id, :lang, :name, :description)
                ON CONFLICT (project_id, lang) DO UPDATE SET
                    name = EXCLUDED.name, description = EXCLUDED.description
            """), [
                {"project_id": proj_id[i["id"]], "lang": lang, "name": i["name"], "description": i["description"]}
                for i in items
            ])

        for i in items:
            conn.execute(text("DELETE FROM project_tags WHERE project_id = :id"), {"id": proj_id[i["id"]]})

        tag_rows = [
            {"project_id": proj_id[i["id"]], "tag": t}
            for i in items
            for t in i["tags"]
        ]
        if tag_rows:
            conn.execute(text("""
                INSERT INTO project_tags (project_id, tag)
                VALUES (:project_id, :tag)
                ON CONFLICT (project_id, tag) DO NOTHING
            """), tag_rows)

        if slugs:
            conn.execute(
                text("DELETE FROM projects WHERE slug NOT IN :slugs")
                .bindparams(bindparam("slugs", expanding=True)),
                {"slugs": slugs},
            )
        else:
            conn.execute(text("DELETE FROM projects"))
