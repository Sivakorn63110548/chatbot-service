from pydantic import BaseModel


class LocaleSectionUpdate(BaseModel):
    section: str
    values: dict[str, str]


class LocaleSectionsUpdate(BaseModel):
    sections: list[LocaleSectionUpdate]


class EducationSubjectIn(BaseModel):
    label: str
    value: str


class EducationUpdate(BaseModel):
    subjects: list[EducationSubjectIn]


class SkillCategoryIn(BaseModel):
    title: str
    description: str


class SkillCategoriesUpdate(BaseModel):
    categories: list[SkillCategoryIn]


class ExperienceEntryIn(BaseModel):
    id: str
    logo: str | None
    period: str
    is_current: bool
    company: str
    role: str
    description: str
    responsibilities: list[str]


class ExperienceUpdate(BaseModel):
    entries: list[ExperienceEntryIn]


class ProjectItemIn(BaseModel):
    id: str
    lang_code: str | None
    stars: int
    is_private: bool
    url: str | None
    name: str
    description: str
    tags: list[str]


class ProjectsUpdate(BaseModel):
    items: list[ProjectItemIn]
