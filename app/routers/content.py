import logging
from fastapi import APIRouter, HTTPException, Query
from app.schemas.content import ContentResponse, ExperienceEntry, ProjectItem, EducationSubject, SkillCategory
from app.services.content import (
    VALID_LANGS,
    get_locale,
    get_experience,
    get_projects,
    get_education,
    get_skill_categories,
)

logger = logging.getLogger("content")
router = APIRouter(prefix="/api", tags=["content"])


def _validate_lang(lang: str) -> str:
    if lang not in VALID_LANGS:
        raise HTTPException(status_code=400, detail=f"lang must be one of {sorted(VALID_LANGS)}")
    return lang


@router.get("/content/{lang}", response_model=ContentResponse)
def get_content(lang: str):
    """Full content payload for a given language — single call for the frontend."""
    lang = _validate_lang(lang)
    return ContentResponse(
        locale=get_locale(lang),
        experience=[ExperienceEntry(**e) for e in get_experience(lang)],
        projects=[ProjectItem(**p) for p in get_projects(lang)],
        education=[EducationSubject(**s) for s in get_education(lang)],
        skill_categories=[SkillCategory(**c) for c in get_skill_categories(lang)],
    )


@router.get("/locale/{lang}")
def get_locale_endpoint(lang: str):
    """Locale strings only (nav, topbar, home, about, skill, contact, footer)."""
    return get_locale(_validate_lang(lang))


@router.get("/experience")
def get_experience_endpoint(lang: str = Query(default="en")):
    """Experience entries with responsibilities."""
    return get_experience(_validate_lang(lang))


@router.get("/projects")
def get_projects_endpoint(lang: str = Query(default="en")):
    """Projects with tags and translations."""
    return get_projects(_validate_lang(lang))


@router.get("/education")
def get_education_endpoint(lang: str = Query(default="en")):
    """Education subjects."""
    return get_education(_validate_lang(lang))


@router.get("/skill-categories")
def get_skill_categories_endpoint(lang: str = Query(default="en")):
    """Skill category labels."""
    return get_skill_categories(_validate_lang(lang))
