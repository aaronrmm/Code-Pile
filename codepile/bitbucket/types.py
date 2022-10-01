from typing import Dict, Any, Optional

from pydantic import BaseModel


class BitbucketRepo(BaseModel):
    hash: str
    details: Dict[str, Any] = {}


class BitbucketQueryResult(BaseModel):
    repos: Dict[str, BitbucketRepo] = {}
    is_complete: bool = False
    starting_query: str
    next_query: Optional[str] = None
