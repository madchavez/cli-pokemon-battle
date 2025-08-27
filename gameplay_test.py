from models.pokemon import Pokemon
from models.move import Move
from battle import Battle

# --- Define some sample moves ---
tackle = Move(name="Tackle", base=40, mov_type="Normal", accuracy=1.0, category="n", priority=0)
ember  = Move(name="Ember",  base=40, mov_type="Fire",   accuracy=1.0, category="sp", priority=0)
thunderbolt = Move(name="Thunderbolt", base=90, mov_type="Electric", accuracy=1.0, category="sp", priority=0)

# --- Define Pokémon (with minimal stats) ---
charmander = Pokemon(
    name="Charmander",
    hp=39, n_atk=52, n_def=43, sp_atk=60, sp_def=50, spd=65,
    types=["Fire"],
    moves=[tackle, ember]
)

pikachu = Pokemon(
    name="Pikachu",
    hp=35, n_atk=55, n_def=40, sp_atk=50, sp_def=50, spd=90,
    types=["Electric"],
    moves=[tackle, thunderbolt]
)

# --- Create a battle instance ---
battle = Battle(charmander, pikachu)

# --- Take a turn ---
# Charmander uses Ember (index 1), Pikachu uses Thunderbolt (index 1)
result = battle.take_turn(p1_move_index=1, p2_move_index=1)

# --- Inspect the log ---
print(result["log"])

print("HP after turn:")
print(f"{charmander.name}: {charmander.hp}/{charmander.max_hp}")
print(f"{pikachu.name}: {pikachu.hp}/{pikachu.max_hp}")
if result["finished"]:
    print(f"Winner: {result['winner']}")
