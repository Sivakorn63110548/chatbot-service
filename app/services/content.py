from sqlalchemy import text, bindparam
from app.core.database import engine

VALID_LANGS = {"en", "th"}


def _set_nested(d: dict, path: list[str], value: str) -> None:
    for part in path[:-1]:
        d = d.setdefault(part, {})
    d[path[-1]] = value


def get_locale(lang: str) -> dict:
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT section, key, value FROM locale_strings WHERE lang = :lang ORDER BY section, key"),
            {"lang": lang},
        ).fetchall()
    result: dict = {}
    for row in rows:
        _set_nested(result, row.section.split(".") + [row.key], row.value)
    return result


def get_experience(lang: str) -> list[dict]:
    with engine.connect() as conn:
        entries = conn.execute(text("""
            SELECT e.id, e.slug, e.logo, e.period, e.is_current,
                   t.company, t.role, t.description
            FROM experience_entries e
            JOIN experience_translations t ON t.experience_id = e.id AND t.lang = :lang
            ORDER BY e.is_current DESC, e.id
        """), {"lang": lang}).fetchall()

        if not entries:
            return []

        exp_ids = [r.id for r in entries]
        resp_rows = conn.execute(
            text("""
                SELECT experience_id, text
                FROM experience_responsibilities
                WHERE experience_id IN :ids AND lang = :lang
                ORDER BY experience_id, position
            """).bindparams(bindparam("ids", expanding=True)),
            {"ids": exp_ids, "lang": lang},
        ).fetchall()

    resp_map: dict[int, list[str]] = {}
    for r in resp_rows:
        resp_map.setdefault(r.experience_id, []).append(r.text)

    return [
        {
            "id": e.slug,
            "company": e.company,
            "logo": e.logo,
            "role": e.role,
            "period": e.period,
            "is_current": e.is_current,
            "description": e.description,
            "responsibilities": resp_map.get(e.id, []),
        }
        for e in entries
    ]


def get_projects(lang: str) -> list[dict]:
    with engine.connect() as conn:
        items = conn.execute(text("""
            SELECT p.id, p.slug, p.lang_code, p.stars, p.is_private, p.url,
                   t.name, t.description
            FROM projects p
            JOIN project_translations t ON t.project_id = p.id AND t.lang = :lang
            ORDER BY p.id
        """), {"lang": lang}).fetchall()

        if not items:
            return []

        proj_ids = [r.id for r in items]
        tag_rows = conn.execute(
            text("""
                SELECT project_id, tag FROM project_tags
                WHERE project_id IN :ids ORDER BY project_id, id
            """).bindparams(bindparam("ids", expanding=True)),
            {"ids": proj_ids},
        ).fetchall()

    tags_map: dict[int, list[str]] = {}
    for t in tag_rows:
        tags_map.setdefault(t.project_id, []).append(t.tag)

    return [
        {
            "id": p.slug,
            "name": p.name,
            "description": p.description,
            "lang_code": p.lang_code,
            "stars": p.stars,
            "is_private": p.is_private,
            "url": p.url,
            "tags": tags_map.get(p.id, []),
        }
        for p in items
    ]


def get_education(lang: str) -> list[dict]:
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT label, value FROM education_subjects WHERE lang = :lang ORDER BY position"),
            {"lang": lang},
        ).fetchall()
    return [{"label": r.label, "value": r.value} for r in rows]


def get_skill_categories(lang: str) -> list[dict]:
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT title, description FROM skill_categories WHERE lang = :lang ORDER BY position"),
            {"lang": lang},
        ).fetchall()
    return [{"title": r.title, "description": r.description} for r in rows]
