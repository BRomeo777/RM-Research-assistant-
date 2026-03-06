from pydantic import BaseModel, Field
from typing import List, Optional
from .paper import PaperResponse

class SearchQuery(BaseModel):
    q: str = Field(..., min_length=2, description="The search keywords or natural language query")
    limit: int = Field(default=20, ge=1, le=100)
    offset: int = 0
    year_start: Optional[int] = None
    year_end: Optional[int] = None

class SearchResponse(BaseModel):
    total_results: int
    took_ms: int
    results: List[PaperResponse]
