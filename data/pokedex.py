# data/pokedex.py
pokedex_data = {
    # --- Tier 2 (kept & cleaned to fit your constraints) ---
    "Croconaw": {
        "name": "Croconaw",
        "stats": {"hp": 65, "n_atk": 80, "n_def": 80, "sp_atk": 59, "sp_def": 63, "spd": 58},
        "types": ["Water"],
        "moves": [
            {"name": "Scratch",   "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Water Gun", "base": 40, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Rage",      "base": 20, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Absorb",    "base": 20, "mov_type": "Grass",  "accuracy": 1.0,  "category": "sp",
             "move_eff": "drain"},
        ],
    },

    "Quagsire": {
        "name": "Quagsire",
        "stats": {"hp": 95, "n_atk": 85, "n_def": 85, "sp_atk": 65, "sp_def": 65, "spd": 35},
        "types": ["Water", "Ground"],
        "moves": [
            {"name": "Tackle",    "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Mud-Slap",  "base": 20, "mov_type": "Ground", "accuracy": 1.0,  "category": "n"},
            {"name": "Water Gun", "base": 40, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Defense Curl","base":0, "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": +1},
        ],
    },

    "Scizor": {
        "name": "Scizor",
        "stats": {"hp": 70, "n_atk": 130, "n_def": 100, "sp_atk": 55, "sp_def": 80, "spd": 65},
        "types": ["Bug", "Steel"],
        "moves": [
            {"name": "Quick Attack", "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n", "priority": 1},
            {"name": "Metal Claw",   "base": 50, "mov_type": "Steel",  "accuracy": 0.95, "category": "n"},
            {"name": "Pursuit",      "base": 40, "mov_type": "Dark",   "accuracy": 1.0,  "category": "sp"},
            {"name": "Agility",      "base": 0,  "mov_type": "Psychic","accuracy": 1.0,  "category": "n",
             "attr_ch": "spd", "attr_delta": +2},
        ],
    },

    "Donphan": {
        "name": "Donphan",
        "stats": {"hp": 90, "n_atk": 120, "n_def": 120, "sp_atk": 60, "sp_def": 60, "spd": 50},
        "types": ["Ground"],
        "moves": [
            {"name": "Tackle",   "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Mud-Slap", "base": 20, "mov_type": "Ground", "accuracy": 1.0,  "category": "n"},
            {"name": "Rollout",  "base": 30, "mov_type": "Rock",   "accuracy": 0.9,  "category": "n"},
            {"name": "Take Down","base": 90, "mov_type": "Normal", "accuracy": 0.85, "category": "n"},
        ],
    },

    "Steelix": {
        "name": "Steelix",
        "stats": {"hp": 75, "n_atk": 85, "n_def": 200, "sp_atk": 55, "sp_def": 65, "spd": 30},
        "types": ["Steel", "Ground"],
        "moves": [
            {"name": "Tackle",     "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Rock Throw", "base": 50, "mov_type": "Rock",   "accuracy": 0.9,  "category": "n"},
            {"name": "Rage",       "base": 20, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Harden",     "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": +1},
        ],
    },

    "Furret": {
        "name": "Furret",
        "stats": {"hp": 85, "n_atk": 76, "n_def": 64, "sp_atk": 45, "sp_def": 55, "spd": 90},
        "types": ["Normal"],
        "moves": [
            {"name": "Tackle",       "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Quick Attack", "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n", "priority": 1},
            {"name": "Fury Swipes",  "base": 18, "mov_type": "Normal", "accuracy": 0.8,  "category": "n"},
            {"name": "Slam",         "base": 80, "mov_type": "Normal", "accuracy": 0.75, "category": "n"},
        ],
    },

    "Azumarill": {
        "name": "Azumarill",
        "stats": {"hp": 100, "n_atk": 50, "n_def": 80, "sp_atk": 50, "sp_def": 80, "spd": 50},
        "types": ["Water"],
        "moves": [
            {"name": "Tackle",    "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Water Gun", "base": 40, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Rollout",   "base": 30, "mov_type": "Rock",   "accuracy": 0.9,  "category": "n"},
            {"name": "Defense Curl","base":0, "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": +1},
        ],
    },

    "Umbreon": {
        "name": "Umbreon",
        "stats": {"hp": 95, "n_atk": 65, "n_def": 110, "sp_atk": 60, "sp_def": 130, "spd": 65},
        "types": ["Dark"],
        "moves": [
            {"name": "Tackle",       "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Pursuit",      "base": 40, "mov_type": "Dark",   "accuracy": 1.0,  "category": "sp"},
            {"name": "Quick Attack", "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n", "priority": 1},
            {"name": "Moonlight",    "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "move_eff": "heal"},
        ],
    },

    "Octillery": {
        "name": "Octillery",
        "stats": {"hp": 75, "n_atk": 105, "n_def": 75, "sp_atk": 105, "sp_def": 75, "spd": 45},
        "types": ["Water"],
        "moves": [
            {"name": "Constrict",   "base": 10, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Water Gun",   "base": 40, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "BubbleBeam",  "base": 65, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Aurora Beam", "base": 65, "mov_type": "Ice",    "accuracy": 1.0,  "category": "sp"},
        ],
    },

    # --- Tier 3 additions (selected 4 moves <= Lv30 that fit your rules) ---
    "Feraligatr": {
        "name": "Feraligatr",
        "stats": {"hp": 85, "n_atk": 105, "n_def": 100, "sp_atk": 79, "sp_def": 83, "spd": 78},
        "types": ["Water"],
        "moves": [
            {"name": "Scratch",   "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Water Gun", "base": 40, "mov_type": "Water",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Rage",      "base": 20, "mov_type": "Normal", "accuracy": 1.0,  "category": "n"},
            {"name": "Leer",      "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": -1},
        ],
    },

    "Typhlosion": {
        "name": "Typhlosion",
        "stats": {"hp": 78, "n_atk": 84, "n_def": 78, "sp_atk": 109, "sp_def": 85, "spd": 100},
        "types": ["Fire"],
        "moves": [
            {"name": "Tackle",       "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Quick Attack", "base": 40, "mov_type": "Normal", "accuracy": 1.0,  "category": "n", "priority": 1},
            {"name": "Swift",        "base": 60, "mov_type": "Normal", "accuracy": 1.0,  "category": "sp"},
            {"name": "Defense Curl", "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": +1},
        ],
    },

    "Meganium": {
        "name": "Meganium",
        "stats": {"hp": 80, "n_atk": 82, "n_def": 100, "sp_atk": 83, "sp_def": 100, "spd": 80},
        "types": ["Grass"],
        "moves": [
            {"name": "Tackle",     "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Vine Whip",  "base": 35, "mov_type": "Grass",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Razor Leaf", "base": 55, "mov_type": "Grass",  "accuracy": 0.95, "category": "sp"},
            {"name": "Growl",      "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_atk", "attr_delta": -1},
        ],
    },

    "Tyranitar": {
        "name": "Tyranitar",
        "stats": {"hp": 100, "n_atk": 134, "n_def": 110, "sp_atk": 95, "sp_def": 100, "spd": 61},
        "types": ["Rock", "Dark"],
        "moves": [
            {"name": "Tackle",     "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Rock Throw", "base": 50, "mov_type": "Rock",   "accuracy": 0.9,  "category": "n"},
            {"name": "Screech",    "base": 0,  "mov_type": "Normal", "accuracy": 0.85, "category": "n",
             "attr_ch": "n_def", "attr_delta": -2},
            {"name": "Leer",       "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": -1},
        ],
    },

    "Dragonite": {
        "name": "Dragonite",
        "stats": {"hp": 91, "n_atk": 134, "n_def": 95, "sp_atk": 100, "sp_def": 100, "spd": 80},
        "types": ["Dragon", "Flying"],
        "moves": [
            {"name": "Slam",        "base": 80, "mov_type": "Normal", "accuracy": 0.75, "category": "n"},
            {"name": "Dragon Rage", "base": 40, "mov_type": "Dragon", "accuracy": 1.0,  "category": "sp"},
            {"name": "Agility",     "base": 0,  "mov_type": "Psychic","accuracy": 1.0,  "category": "n",
             "attr_ch": "spd", "attr_delta": +2},
            {"name": "Leer",        "base": 0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": -1},
        ],
    },

    "Golem": {
        "name": "Golem",
        "stats": {"hp": 80, "n_atk": 110, "n_def": 130, "sp_atk": 55, "sp_def": 65, "spd": 45},
        "types": ["Rock", "Ground"],
        "moves": [
            {"name": "Tackle",     "base": 35, "mov_type": "Normal", "accuracy": 0.95, "category": "n"},
            {"name": "Defense Curl","base":0,  "mov_type": "Normal", "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": +1},
            {"name": "Rock Throw", "base": 50, "mov_type": "Rock",   "accuracy": 0.9,  "category": "n"},
            {"name": "Magnitude",  "base": 70, "mov_type": "Ground", "accuracy": 1.0,  "category": "n"},
        ],
    },

    "Espeon": {
        "name": "Espeon",
        "stats": {"hp": 65, "n_atk": 65, "n_def": 60, "sp_atk": 130, "sp_def": 95, "spd": 110},
        "types": ["Psychic"],
        "moves": [
            {"name": "Tackle",      "base": 35, "mov_type": "Normal",  "accuracy": 0.95, "category": "n"},
            {"name": "Swift",       "base": 60, "mov_type": "Normal",  "accuracy": 1.0,  "category": "sp"},
            {"name": "Confusion",   "base": 50, "mov_type": "Psychic", "accuracy": 1.0,  "category": "sp"},  # treat as pure damage here
            {"name": "Tail Whip",   "base": 0,  "mov_type": "Normal",  "accuracy": 1.0,  "category": "n",
             "attr_ch": "n_def", "attr_delta": -1},
        ],
    },
}
