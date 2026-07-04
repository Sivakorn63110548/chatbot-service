-- Simple key-value strings per language (nav, topbar, home, about, skill, contact, footer)
CREATE TABLE IF NOT EXISTS locale_strings (
    id      BIGSERIAL PRIMARY KEY,
    lang    CHAR(2)  NOT NULL,
    section TEXT     NOT NULL,
    key     TEXT     NOT NULL,
    value   TEXT     NOT NULL,
    UNIQUE (lang, section, key)
);

-- Experience entries — language-agnostic core data
CREATE TABLE IF NOT EXISTS experience_entries (
    id         BIGSERIAL PRIMARY KEY,
    slug       TEXT    NOT NULL UNIQUE,
    logo       TEXT,
    period     TEXT    NOT NULL,
    is_current BOOLEAN NOT NULL DEFAULT false
);

CREATE TABLE IF NOT EXISTS experience_translations (
    id            BIGSERIAL PRIMARY KEY,
    experience_id BIGINT   NOT NULL REFERENCES experience_entries(id) ON DELETE CASCADE,
    lang          CHAR(2)  NOT NULL,
    company       TEXT     NOT NULL,
    role          TEXT     NOT NULL,
    description   TEXT     NOT NULL,
    UNIQUE (experience_id, lang)
);

CREATE TABLE IF NOT EXISTS experience_responsibilities (
    id            BIGSERIAL PRIMARY KEY,
    experience_id BIGINT   NOT NULL REFERENCES experience_entries(id) ON DELETE CASCADE,
    lang          CHAR(2)  NOT NULL,
    position      SMALLINT NOT NULL,
    text          TEXT     NOT NULL,
    UNIQUE (experience_id, lang, position)
);

-- Projects — language-agnostic core data
CREATE TABLE IF NOT EXISTS projects (
    id         BIGSERIAL PRIMARY KEY,
    slug       TEXT    NOT NULL UNIQUE,
    lang_code  TEXT,
    stars      INT     NOT NULL DEFAULT 0,
    is_private BOOLEAN NOT NULL DEFAULT false,
    url        TEXT
);

CREATE TABLE IF NOT EXISTS project_translations (
    id          BIGSERIAL PRIMARY KEY,
    project_id  BIGINT  NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    lang        CHAR(2) NOT NULL,
    name        TEXT    NOT NULL,
    description TEXT    NOT NULL,
    UNIQUE (project_id, lang)
);

CREATE TABLE IF NOT EXISTS project_tags (
    id         BIGSERIAL PRIMARY KEY,
    project_id BIGINT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    tag        TEXT   NOT NULL,
    UNIQUE (project_id, tag)
);

-- Education subjects per language
CREATE TABLE IF NOT EXISTS education_subjects (
    id       BIGSERIAL PRIMARY KEY,
    lang     CHAR(2)  NOT NULL,
    position SMALLINT NOT NULL,
    label    TEXT     NOT NULL,
    value    TEXT     NOT NULL,
    UNIQUE (lang, position)
);

-- Skill categories per language
CREATE TABLE IF NOT EXISTS skill_categories (
    id          BIGSERIAL PRIMARY KEY,
    lang        CHAR(2)  NOT NULL,
    position    SMALLINT NOT NULL,
    title       TEXT     NOT NULL,
    description TEXT     NOT NULL,
    UNIQUE (lang, position)
);

CREATE INDEX IF NOT EXISTS idx_locale_strings_lang    ON locale_strings(lang);
CREATE INDEX IF NOT EXISTS idx_exp_translations_lang  ON experience_translations(lang);
CREATE INDEX IF NOT EXISTS idx_proj_translations_lang ON project_translations(lang);
