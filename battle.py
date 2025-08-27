from __future__ import annotations
import random as rand
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from models.move import Move
from models.pokemon import Pokemon
from data.types import type_effectiveness

@dataclass
class Battle:
    p1: Pokemon
    p2: Pokemon
    rng: rand.Random = field(default_factory=rand.Random, repr=False)
    turn: int = field(default=1, init=False)
    # weather: Optional[str] = None

    def calculate_damage(self, attacker: Pokemon, defender: Pokemon, move: Move) -> int:
        A, D = attacker.n_or_sp(move, defender)

        # formula taken from: https://web.archive.org/web/20140712063943/http://www.upokecenter.com/content/pokemon-gold-version-silver-version-and-crystal-version-timing-notes
        base = (((2 * 30) / 5 + 2) * A * move.base / max(1, D)) / 50 # 30 in (2 * 30) is the default level for all pokemon in this project
        
        # modifiers 
        stab = attacker.is_stab(move) # Same-type attack bonus
        crit_bool, crit_mult = attacker.crit_check(move)
        r_factor = attacker.calc_r()
        type_mult = type_effectiveness(move.mov_type, defender.types)

        # final calculation
        dmg = int(base * stab * crit_mult * r_factor * type_mult)
        return max(1, dmg), crit_bool, type_mult
    
    def apply_damage(self, attacker: Pokemon, defender: Pokemon, move: Move) -> tuple[int, bool, float]:
        dmg, crit_bool, type_mult = self.calculate_damage(attacker, defender, move)
        defender.hp = max(0, defender.hp - dmg)
        return dmg, crit_bool, type_mult
    
    def choose_action(self, pokemon: Pokemon, move_index):
        move = pokemon.moves[move_index]
        prio, speed = pokemon.initiative(move)
        return (pokemon, move, prio, speed)
    
    def initiative_order(self, actions):
        return sorted(actions, key=lambda x: (-x[2], -x[3], self.rng.random()))

    def take_turn(self, p1_move_index: int, p2_move_index: int) -> dict:
        actions_log = []

        try:
            a1 = self.choose_action(self.p1, p1_move_index)
        except Exception as e:
            return {"error": f"p1 invalid move index: {e}"}
        try:
            a2 = self.choose_action(self.p2, p2_move_index)
        except Exception as e:
            return {"error": f"p2 invalid move index: {e}"}
        
        ordered = self.initiative_order([a1, a2])
        
        # for debug
        # print(f"actions = {ordered}")

        for (attacker, move, prio, spd) in ordered:
            defender = self.p2 if attacker is self.p1 else self.p1

            if attacker.is_fainted():
                break

            if defender.is_fainted():
                break

            if not attacker.is_accurate(move):
                actions_log.append({
                "actor": attacker.name, "target": defender.name,
                "move": move.name, "result": "miss"
                })
                continue

            # for debug
            # print(f"move = {move}")

            dmg, crit_flag, type_mult = self.apply_damage(attacker, defender, move)
        
            actions_log.append({
                "actor": attacker.name, "target": defender.name,
                "move": move.name, "result": "hit",
                "damage": dmg, "critical": crit_flag,
                "effectiveness": type_mult,
                "target_hp_after": defender.hp
            })

            # KO check
            if defender.is_fainted():
                actions_log.append({
                    "actor": attacker.name, "target": defender.name,
                    "move": move.name, "result": "target_fainted"
                })
                break


        finished = self.p1.is_fainted() or self.p2.is_fainted()
        winner = (
            self.p2.name if self.p1.is_fainted() and not self.p2.is_fainted()
            else self.p1.name if self.p2.is_fainted() and not self.p1.is_fainted()
            else None
        )

        summary = {
            "ok": True,
            "turn": self.turn,
            "actions": ordered,
            "log": actions_log,
            "p1_hp": f"{self.p1.hp}",
            "p2_hp": f"{self.p2.hp}",
            "finished": finished,
            "winner": winner,
        }

        self.turn += 1
        return summary

