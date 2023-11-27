from dataclasses import dataclass, field
from typing import Generic, TypeVar, Optional, Any

T = TypeVar('T')


@dataclass
class QueryResult(Generic[T]):
    payload: Optional[T]
    errors: list[Any] = field(default_factory=list)



