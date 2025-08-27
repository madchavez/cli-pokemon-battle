from __future__ import annotations   # must be the first import!
import random as rand
from typing import List, Dict
from dataclasses import dataclass, field
from models.move import Move

@dataclass
class Pokemon:
    name: str
    hp: int
    n_atk: int
    n_def: int
    sp_atk: int
    sp_def: int
    spd: int
    types: List[str]
    moves: List[Move]
    max_hp: int = field(init=False)
    rng: rand.Random = field(default_factory=rand.Random, repr=False)

    def __post_init__(self):
        self.max_hp = self.hp

    def is_fainted(self) -> bool:
        """Check if Pokemon has fainted"""
        return self.hp <= 0

    def is_accurate(self, move: Move) -> bool:
        """Check if a move hits based on its accuracy."""
        return self.rng.random() <= move.accuracy

    def initiative(self, move: Move):
        """Return tuple for sorting turn order: (priority, speed)."""
        return move.priority, self.spd

    def is_stab(self, move: Move) -> float:
        """Same-Type Attack Bonus (STAB)."""
        return 1.5 if move.mov_type in self.types else 1.0

    def crit_check(self, move: Move):
        """Determine if the move is a critical hit."""
        is_crit = self.rng.random() <= move.crit_chance
        return is_crit, (1.5 if is_crit else 1.0)

    def calc_r(self) -> float:
        """Damage variance (0.85–1.00)."""
        return self.rng.uniform(0.85, 1.0)

    def n_or_sp(self, move: Move, defender: Pokemon):
        """Return (attacker_stat, defender_stat) depending on move category."""
        if move.category.lower() == "sp":
            return self.sp_atk, defender.sp_def
        return self.n_atk, defender.n_def
    
    @classmethod
    def from_dict(cls, data: Dict) -> Pokemon:
        """Build a Pokemon directly from dict"""
        stats = data["stats"]
        moves = [
            Move(
                name=m["name"],
                power=int(m.get("power", 0)),
                mov_type=m.get("mov_type", "Normal"),
                accuracy=float(m.get("accuracy", 1.0)),
                category=m.get("category", "n"),
                priority=int(m.get("priority", 0)),
                crit_chance=float(m.get("crit_chance", 1/24)),
            )
            for m in data.get("moves", [])[:4]
        ]

        return cls(
            name=data["name"],
            hp=stats["hp"],
            n_atk=stats["n_atk"],
            n_def=stats["n_def"],
            sp_atk=stats["sp_atk"],
            sp_def=stats["sp_def"],
            spd=stats["spd"],
            types=data.get("types", ["Normal"]),
            moves=moves,
        )
