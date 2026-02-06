from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class IssueStatus(str, Enum):
    open = "open"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100, description="Title of the issue")
    description: str = Field(min_length=5, max_length=1000, description="Description of the issue")
    priority: IssuePriority = Field(default=IssuePriority.medium)
    status: IssueStatus = Field(default=IssueStatus.open)


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, min_length=5, max_length=1000)
    priority: Optional[IssuePriority] = Field(default=None)
    status: Optional[IssueStatus] = Field(default=None)

class IssueOut(BaseModel):
    id:str
    title:str
    description:str
    priority:IssuePriority
    status:IssueStatus
