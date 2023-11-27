from dataclasses import dataclass, field
from typing import Generic, TypeVar, Optional, Any

T = TypeVar('T')


@dataclass
class CommandResult(Generic[T]):
    ...



