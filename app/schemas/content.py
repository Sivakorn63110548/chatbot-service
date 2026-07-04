from pydantic import BaseModel
from typing import Any


class ExperienceEntry(BaseModel):
    id: str
    company: str
    logo: str | None
    role: str
    period: str
    is_current: bool
    description: str
    responsibilities: list[str]


class ProjectItem(BaseModel):
    id: str
    name: str
    description: str
    lang_code: str | None
    stars: int
    is_private: bool
    url: str | None
    tags: list[str]


class EducationSubject(BaseModel):
    label: str
    value: str


class SkillCategory(BaseModel):
    title: str
    description: str


class ContentResponse(BaseModel):
    locale: dict[str, Any]
    experience: list[ExperienceEntry]
    projects: list[ProjectItem]
    education: list[EducationSubject]
    skill_categories: list[SkillCategory]
