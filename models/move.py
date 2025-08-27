from __future__ import annotations
import random as rand
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Move:
    """Simple data model for pokemon moves."""
    name: str
    base: int
    mov_type: str
    accuracy: float
    category: str
    crit_chance: float = 1/24
    priority: int = 0
