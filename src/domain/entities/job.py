from datetime import datetime
from typing import List
from typing import Optional, Callable
from pydantic import BaseModel, Field


class Job(BaseModel):
    func: Callable = Field(default=None)
    trigger: str | None = Field(default=None)
    run_date: datetime | None = Field(default=None)
    hour: int | None = Field(default=None)
    minute: int | None = Field(default=None)
    args: list | None = Field(default=None)
    job_id: Optional[str] = Field(default=None)
    job_type: Optional[str] = Field(default=None)

