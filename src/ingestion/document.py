from pydantic import BaseModel


class Document(BaseModel):
    text: str
    source: str
    page: int
    chunk_id: str | None = None
    section: str | None = None