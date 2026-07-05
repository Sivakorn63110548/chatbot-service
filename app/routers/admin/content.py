import logging
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.admin_content import (
    LocaleSectionsUpdate,
    EducationUpdate,
    SkillCategoriesUpdate,
    ExperienceUpdate,
    ProjectsUpdate,
)
from app.services.content import VALID_LANGS
from app.services import admin_content as service
from app.dependencies import get_current_admin

logger = logging.getLogger("admin.content")
router = APIRouter(prefix="/admin/content", tags=["admin"])


def _validate_lang(lang: str) -> str:
    if lang not in VALID_LANGS:
        raise HTTPException(status_code=400, detail=f"lang must be one of {sorted(VALID_LANGS)}")
    return lang


@router.put("/locale/{lang}")
def put_locale(lang: str, body: LocaleSectionsUpdate, admin: dict = Depends(get_current_admin)):
    _validate_lang(lang)
    service.upsert_locale_sections(lang, [s.model_dump() for s in body.sections])
    logger.info(f"[ADMIN] {admin['username']} updated locale sections {[s.section for s in body.sections]} ({lang})")
    return {"status": "ok"}


@router.put("/education/{lang}")
def put_education(lang: str, body: EducationUpdate, admin: dict = Depends(get_current_admin)):
    _validate_lang(lang)
    service.replace_education(lang, [s.model_dump() for s in body.subjects])
    logger.info(f"[ADMIN] {admin['username']} updated education ({lang})")
    return {"status": "ok"}


@router.put("/skill-categories/{lang}")
def put_skill_categories(lang: str, body: SkillCategoriesUpdate, admin: dict = Depends(get_current_admin)):
    _validate_lang(lang)
    service.replace_skill_categories(lang, [c.model_dump() for c in body.categories])
    logger.info(f"[ADMIN] {admin['username']} updated skill categories ({lang})")
    return {"status": "ok"}


@router.put("/experience/{lang}")
def put_experience(lang: str, body: ExperienceUpdate, admin: dict = Depends(get_current_admin)):
    _validate_lang(lang)
    service.upsert_experience(lang, [e.model_dump() for e in body.entries])
    logger.info(f"[ADMIN] {admin['username']} updated experience ({lang})")
    return {"status": "ok"}


@router.put("/projects/{lang}")
def put_projects(lang: str, body: ProjectsUpdate, admin: dict = Depends(get_current_admin)):
    _validate_lang(lang)
    service.upsert_projects(lang, [i.model_dump() for i in body.items])
    logger.info(f"[ADMIN] {admin['username']} updated projects ({lang})")
    return {"status": "ok"}
