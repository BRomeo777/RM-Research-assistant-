from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from ..enums.paper import OpenAccessStatus

class PaperBase(BaseModel):
    title: str
    doi: Optional[str] = None
    authors: List[str]
    journal: Optional[str] = None
    publication_date: Optional[datetime] = None

class PaperCreate(PaperBase):
    abstract: Optional[str] = None

class PaperResponse(PaperBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    citations_count: int = 0
    open_access_status: OpenAccessStatus = OpenAccessStatus.CLOSED
    created_at: datetime
