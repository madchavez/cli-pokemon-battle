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
    move_eff: str = None  #  Move Effect: heal, drain or None
    attr_ch: str = None  # Attribute changed: atk_s, def_s, sp_atk_s, sp_def_s, spd_s
    attr_delta: int = 0  # Attribute delta