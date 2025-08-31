from __future__ import annotations
import random
import time
from typing import List, Dict
from models.pokemon import Pokemon
from models.move import Move
from battle import Battle
from data.pokedex import pokedex_data
from data.types import type_effectiveness, TYPE_CHART_GEN2

def get_random_pokemon() -> Pokemon:
    """Get a completely random Pokémon using from_dict factory"""
    pokemon_name = random.choice(list(pokedex_data.keys()))
    return Pokemon.from_dict(pokedex_data[pokemon_name])

def get_user_pokemon_choice() -> Pokemon:
    """Let user choose a Pokémon from the pokedex"""
    print("\n" + "="*50)
    print("CHOOSE YOUR POKÉMON")
    print("="*50)
    
    pokemon_names = list(pokedex_data.keys())
    
    for i, name in enumerate(pokemon_names, 1):
        types = pokedex_data[name]["types"]
        stats = pokedex_data[name]["stats"]
        total_stats = sum(stats.values())
        print(f"{i:2d}. {name:12} ({'/'.join(types):15}) Total: {total_stats:3d} HP: {stats['hp']:3d}")
    
    while True:
        try:
            choice = input(f"\nChoose your Pokémon (1-{len(pokemon_names)}): ").strip()
            if not choice:
                continue
                
            index = int(choice) - 1
            if 0 <= index < len(pokemon_names):
                selected_name = pokemon_names[index]
                pokemon = Pokemon.from_dict(pokedex_data[selected_name])
                print(f"You chose {pokemon.name}!")
                return pokemon
            else:
                print(f"Please choose a number between 1 and {len(pokemon_names)}!")
                
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nSelection interrupted!")
            exit()

def get_smart_npc_pokemon(player_pokemon: Pokemon) -> Pokemon:
    """NPC chooses a Pokémon that has type advantage against player's Pokémon"""
    player_types = player_pokemon.types
    advantageous_pokemon = []
    
    for pokemon_name, pokemon_data in pokedex_data.items():
        npc_types = pokemon_data["types"]
        for npc_type in npc_types:
            for player_type in player_types:
                effectiveness = TYPE_CHART_GEN2.get(npc_type, {}).get(player_type, 1.0)
                if effectiveness > 1.0:
                    advantageous_pokemon.append(pokemon_name)
                    break
            else:
                continue
            break
    
    if not advantageous_pokemon:
        return get_random_pokemon()
    
    pokemon_name = random.choice(advantageous_pokemon)
    return Pokemon.from_dict(pokedex_data[pokemon_name])

def choose_npc_move(attacker: Pokemon, defender: Pokemon, difficulty: int) -> int:
    """
    NPC move choosing algorithm
    Simply selects for damage by factoring in type effectiveness and STAB
    """
    best_score = -1
    best_moves = []
    
    for i, move in enumerate(attacker.moves):
        effectiveness = type_effectiveness(move.mov_type, defender.types)
        score = move.base * effectiveness
        
        if move.mov_type in attacker.types:
            score *= 1.2
        
        if score > best_score:
            best_score = score
            best_moves = [i]
        elif score == best_score:
            best_moves.append(i)
    
    # If no best moves are found
    if not best_moves:
        return random.randint(0, len(attacker.moves) - 1)
    
    # If hard difficulty, choose among best moves
    if difficulty == 3:
        return random.choice(best_moves)
    
    # If medium difficulty, choose among best moves 50% of the time
    if difficulty == 2:
        if random.random() < 0.5:
            return random.choice(best_moves)
        else:
            return random.randint(0, len(attacker.moves) - 1)
    
    # If easy difficulty, choose random move
    if difficulty == 1:
        return random.randint(0, len(attacker.moves) - 1)

def print_battle_intro(p1: Pokemon, p2: Pokemon):
    """Print classic Pokémon battle introduction"""
    print(f"\n{'='*50}")
    print(f"Wild {p2.name} appeared!")
    print(f"Go! {p1.name}!")
    print(f"{'='*50}")
    # time.sleep(1)

def print_hp_bars(p1: Pokemon, p2: Pokemon):
    """Print HP bars close to Pokémon style"""
    def create_hp_bar(current, max_hp, width=20):
        filled = int((current / max_hp) * width)
        return f"[{'='*filled}{' '*(width-filled)}] {current}/{max_hp}"
    
    print(f"\n{p1.name}: {create_hp_bar(p1.hp, p1.max_hp)}")
    print(f"{p2.name}: {create_hp_bar(p2.hp, p2.max_hp)}")
    print()

def print_move_list(pokemon: Pokemon):
    """Print available moves with indices"""
    print(f"\n{pokemon.name}'s moves:")
    for i, move in enumerate(pokemon.moves):
        print(f"{i+1}. {move.name} ({move.mov_type}, Power: {move.base}, Acc: {move.accuracy*100}%)")

def get_player_move(pokemon: Pokemon) -> int:
    """Get validated player move input"""
    while True:
        try:
            print_move_list(pokemon)
            choice = input("\nChoose a move (1-4): ").strip()
            
            if not choice:
                print("Please enter a number!")
                continue
                
            move_index = int(choice) - 1
            
            if 0 <= move_index < len(pokemon.moves):
                return move_index
            else:
                print(f"Please choose a number between 1 and {len(pokemon.moves)}!")
                
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\nBattle interrupted!")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")

def print_effectiveness_message(effectiveness: float):
    """Print effectiveness messages, simplified"""
    if effectiveness == 0:
        print("It doesn't affect the opponent...")
    elif effectiveness < 1:
        print("It's not very effective...")
    elif effectiveness > 1:
        print("It's super effective!")
    # time.sleep(0.5)

def print_critical_hit_message():
    """Print critical hit message"""
    print("A critical hit!")
    # time.sleep(0.3)

def print_faint_message(pokemon: Pokemon):
    """Print faint message"""
    print(f"{pokemon.name} fainted!")
    # time.sleep(1)

def print_battle_message(actor: str, target: str, move: str):
    """Print basic battle message"""
    print(f"{actor} used {move}!")
    # time.sleep(0.3)

def print_miss_message():
    """Print miss message"""
    print("The attack missed!")
    # time.sleep(0.3)

def animate_damage(damage: int):
    """Simple damage animation"""
    print(f"It did {damage} damage!")
    # time.sleep(0.5)

# ===== MAIN GAMEPLAY LOOP =====
def play_battle():
    """Main battle gameplay function"""

    print("Choose Difficulty!")
    print(
        """
        1. Easy
        2. Normal
        3. Hard
        """
    )
    # Get difficulty input with validation
    while True:
        try:
            difficulty = int(input("Enter difficulty (1-3): ").strip())
            if 1 <= difficulty <= 3:
                break
            else:
                print("Please enter 1, 2, or 3!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Player chooses Pokémon
    player_pokemon = get_user_pokemon_choice()
    
    # Choose random pokemon by default
    npc_pokemon = get_random_pokemon()
    
    if difficulty == 2:
        # If Medium, choose counter 30% of the time
        if random.random() < 0.3:
            npc_pokemon = get_random_pokemon()
        else:
            npc_pokemon = get_smart_npc_pokemon(player_pokemon)
    elif difficulty == 3:
        # If Hard, choose counter
        npc_pokemon = get_smart_npc_pokemon(player_pokemon)
    
    # Initialize battle
    battle = Battle(player_pokemon, npc_pokemon)
    print_battle_intro(player_pokemon, npc_pokemon)
    
    # Show type advantage info
    # time.sleep(2)
    
    # Gameplay loop
    turn_count = 1
    while not battle.p1.is_fainted() and not battle.p2.is_fainted():
        print_hp_bars(battle.p1, battle.p2)
        
        # Player's turn
        player_move_index = get_player_move(battle.p1)
        
        # NPC's turn
        npc_move_index = choose_npc_move(battle.p2, battle.p1, difficulty)
        
        # Execute turn
        result = battle.take_turn(player_move_index, npc_move_index)
        
        # Print battle results with classic messages
        print(f"\n{'='*30} TURN {result['turn']} {'='*30}")
        
        for action in result['log']:
            if action['result'] == 'miss':
                print_battle_message(action['actor'], action['target'], action['move'])
                print_miss_message()
                
            elif action['result'] == 'hit':
                print_battle_message(action['actor'], action['target'], action['move'])
                
                if action['critical']:
                    print_critical_hit_message()
                
                animate_damage(action['damage'])
                print_effectiveness_message(action['effectiveness'])
                
            elif action['result'] == 'target_fainted':
                print_faint_message(battle.p2 if action['target'] == battle.p2.name else battle.p1)
        
        print(f"{'='*70}")
        # time.sleep(1)
    
    # Battle conclusion
    print_hp_bars(battle.p1, battle.p2)
    
    if battle.p1.is_fainted():
        print(f"\n💔 {player_pokemon.name} was defeated!")
        print(f"🏆 Wild {npc_pokemon.name} wins!")
    else:
        print(f"\n💔 Wild {npc_pokemon.name} was defeated!")
        print(f"🏆 {player_pokemon.name} wins the battle!")
    
    print(f"\nBattle finished in {result['turn']} turns!")

def main():
    """Main game loop with replay option"""
    print("🎮 POKÉMON BATTLE SIMULATOR")
    print("="*50)
    
    while True:
        play_battle()
        
        # Ask if player wants to play again
        while True:
            replay = input("\nWould you like to play again? (y/n): ").strip().lower()
            if replay in ['y', 'yes']:
                print("\n" + "="*50)
                print("NEW BATTLE")
                print("="*50)
                break
            elif replay in ['n', 'no']:
                print("\nThanks for playing! Goodbye! 👋")
                return
            else:
                print("Please enter 'y' or 'n'.")

# Run the game
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted! Thanks for playing! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")