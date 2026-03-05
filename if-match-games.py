answer = '0'

while answer != '42':
    answer = input('What is the answer to the ultimate question of life, the universe and everything? ')

print('Congratulations - you are right!!')


import random

random_integer = random.randint(1, 10)
#print(random_integer) # Output: A random integer between 1 and 10

while answer!=random_integer:
    answer = input('What is the correct no (1 to 10)?  ')
    if int(answer) >random_integer:
        print('Lower')
    elif int(answer)< random_integer:
        print('Higher')
    else:
        print('You guess the correct no!')
        break;
        


import random
import json
import os

SAVE_FILE = "rpg_save_bosses.json"

# -----------------------------
# SAVE / LOAD
# -----------------------------
def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player, f)
    print("💾 Game Saved!")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            print("📂 Save Loaded!")
            return json.load(f)
    return None

# -----------------------------
# DIFFICULTY SETTINGS
# -----------------------------
def choose_difficulty():
    print("Choose Difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    choice = input("> ")
    match choice:
        case "1":
            return {"hp_multiplier":1.2, "potion_heal":50, "enemy_damage":0.8, "xp_multiplier":1.2, "gold_multiplier":1.2}
        case "2":
            return {"hp_multiplier":1.0, "potion_heal":35, "enemy_damage":1.0, "xp_multiplier":1.0, "gold_multiplier":1.0}
        case "3":
            return {"hp_multiplier":0.8, "potion_heal":25, "enemy_damage":1.2, "xp_multiplier":0.8, "gold_multiplier":0.8}
        case _:
            print("Invalid choice, defaulting to Medium.")
            return {"hp_multiplier":1.0, "potion_heal":35, "enemy_damage":1.0, "xp_multiplier":1.0, "gold_multiplier":1.0}

# -----------------------------
# ENEMY GENERATOR
# -----------------------------
def generate_enemy(player_level, diff):
    enemy_type = random.choice(["goblin", "orc", "troll", "assassin"])
    match enemy_type:
        case "goblin":
            return {"name":"Goblin","health":int((40+player_level*5)*diff["hp_multiplier"]),
                    "type":"normal","gold":int(30*diff["gold_multiplier"]),"xp":int(50*diff["xp_multiplier"])}
        case "orc":
            return {"name":"Orc","health":int((70+player_level*8)*diff["hp_multiplier"]),
                    "type":"strong","gold":int(60*diff["gold_multiplier"]),"xp":int(80*diff["xp_multiplier"])}
        case "troll":
            return {"name":"Troll","health":int((100+player_level*10)*diff["hp_multiplier"]),
                    "type":"tank","gold":int(80*diff["gold_multiplier"]),"xp":int(120*diff["xp_multiplier"])}
        case "assassin":
            return {"name":"Shadow Assassin","health":int((60+player_level*6)*diff["hp_multiplier"]),
                    "type":"fast","gold":int(70*diff["gold_multiplier"]),"xp":int(100*diff["xp_multiplier"])}

# -----------------------------
# COMBAT SYSTEM
# -----------------------------
def combat(player, enemy, diff):
    print(f"\n⚔️ A {enemy['name']} appears!")

    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n❤️ {player['health']}/{player['max_health']} HP | {enemy['name']} {enemy['health']} HP")
        print("1 - Attack")
        print("2 - Use Potion")
        print("3 - Run")
        action = input("> ")

        match action:
            case "1":
                damage = random.randint(player["attack"] - 3, player["attack"] + 3)
                enemy["health"] -= damage
                print(f"You deal {damage} damage!")
            case "2":
                match "Potion" in player["inventory"]:
                    case True:
                        player["health"] = min(player["health"] + diff["potion_heal"], player["max_health"])
                        player["inventory"].remove("Potion")
                        print(f"🧪 +{diff['potion_heal']} HP")
                    case False:
                        print("No potion!")
            case "3":
                print("🏃 You escaped!")
                return player
            case _:
                print("Invalid action.")
                continue

        # Enemy attack
        if enemy["health"] > 0:
            match enemy["type"]:
                case "normal":
                    damage = int(random.randint(3,8)*diff["enemy_damage"])
                case "strong":
                    print("💪 Orc swings heavily!")
                    damage = int(random.randint(6,12)*diff["enemy_damage"])
                case "tank":
                    print("🪨 Troll SMASHES!")
                    damage = int(random.randint(8,14)*diff["enemy_damage"])
                case "fast":
                    print("⚡ Assassin strikes swiftly!")
                    damage = int(random.randint(5,16)*diff["enemy_damage"])
                case "boss":
                    damage = int(random.randint(enemy["attack_min"], enemy["attack_max"])*diff["enemy_damage"])
                    print(f"🐉 {enemy['name']} attacks for {damage}!")

            player["health"] -= damage
            print(f"{enemy['name']} hits you for {damage}!")

    # Rewards
    match player["health"] > 0:
        case True:
            print(f"🎉 You defeated {enemy['name']}!")
            player["gold"] += enemy.get("gold",0)
            player["xp"] += enemy.get("xp",0)
            print(f"+{enemy.get('gold',0)} Gold | +{enemy.get('xp',0)} XP")
        case False:
            print("💀 You were defeated!")

    return player

# -----------------------------
# SHOP SYSTEM
# -----------------------------
def shop(player):
    print("\n🏪 Welcome to the Shop")
    print(f"💰 Gold: {player['gold']}")
    print("1 - Potion (20g)")
    print("2 - Sword Upgrade (+7 atk) (50g)")
    print("3 - Armor Upgrade (+50 Max HP) (50g)")
    print("4 - Exit")
    choice = input("> ")

    match choice:
        case "1":
            match player["gold"] >= 20:
                case True:
                    player["gold"] -= 20
                    player["inventory"].append("Potion")
                    print("Potion bought!")
                case False:
                    print("Not enough gold!")
        case "2":
            match player["gold"] >= 50:
                case True:
                    player["gold"] -= 50
                    player["attack"] += 7
                    print("⚔️ Attack increased!")
                case False:
                    print("Not enough gold!")
        case "3":
            match player["gold"] >= 50:
                case True:
                    player["gold"] -= 50
                    player["max_health"] += 50
                    player["health"] = player["max_health"]
                    print("🛡️ Max HP increased!")
                case False:
                    print("Not enough gold!")
        case _:
            print("Leaving shop.")

    return player

# -----------------------------
# 10 Bosses List
# -----------------------------
BOSSES = [
    {"name":"Fire Dragon","health":200,"attack_min":15,"attack_max":25,"gold":100,"xp":150},
    {"name":"Ice Golem","health":250,"attack_min":18,"attack_max":28,"gold":120,"xp":180},
    {"name":"Shadow King","health":300,"attack_min":20,"attack_max":30,"gold":150,"xp":200},
    {"name":"Storm Giant","health":350,"attack_min":22,"attack_max":35,"gold":180,"xp":220},
    {"name":"Vampire Lord","health":400,"attack_min":25,"attack_max":40,"gold":200,"xp":250},
    {"name":"Demon Warlord","health":450,"attack_min":28,"attack_max":45,"gold":220,"xp":280},
    {"name":"Ancient Titan","health":500,"attack_min":30,"attack_max":50,"gold":250,"xp":300},
    {"name":"Sea Serpent","health":550,"attack_min":32,"attack_max":55,"gold":280,"xp":350},
    {"name":"Dark Phoenix","health":600,"attack_min":35,"attack_max":60,"gold":300,"xp":400},
    {"name":"Ultimate Dragon","health":700,"attack_min":40,"attack_max":70,"gold":500,"xp":500},
]

# -----------------------------
# MAIN GAME
# -----------------------------
def adventure_game():
    print("🌍 RPG ADVENTURE WITH 10 BOSSES AND DIFFICULTY MODES")
    diff = choose_difficulty()

    player = load_game()
    if not player:
        print("Choose Class:")
        print("1 - Warrior")
        print("2 - Mage")
        print("3 - Archer")
        choice = input("> ")

        match choice:
            case "1":
                base_hp = int(180*diff["hp_multiplier"])
                attack = 15
            case "2":
                base_hp = int(120*diff["hp_multiplier"])
                attack = 25
            case "3":
                base_hp = int(150*diff["hp_multiplier"])
                attack = 18
            case _:
                base_hp = int(150*diff["hp_multiplier"])
                attack = 15

        player = {
            "health": base_hp,
            "max_health": base_hp,
            "attack": attack,
            "xp": 0,
            "level": 1,
            "gold": 50,
            "inventory": [],
            "position": [0,0],
            "boss_index":0
        }

    while player["health"] > 0:
        print("\n====================")
        print(f"📍 Position: {player['position']}")
        print(f"❤️ HP: {player['health']}/{player['max_health']}")
        print(f"⭐ Level: {player['level']} XP: {player['xp']}/100")
        print(f"💰 Gold: {player['gold']}")
        print("====================")
        print("Move: N / S / E / W")
        print("Other: SHOP / SAVE / QUIT")
        choice = input("> ").upper()

        match choice:
            case "N":
                player["position"][1] += 1
            case "S":
                player["position"][1] -= 1
            case "E":
                player["position"][0] += 1
            case "W":
                player["position"][0] -= 1
            case "SHOP":
                player = shop(player)
            case "SAVE":
                save_game(player)
            case "QUIT":
                print("Goodbye!")
                break
            case _:
                print("Invalid move.")
                continue

        # Random encounter or boss
        encounter = random.choice(["enemy","nothing","boss"])
        match encounter:
            case "enemy":
                enemy = generate_enemy(player["level"], diff)
                player = combat(player, enemy, diff)
            case "boss":
                if player["boss_index"] < len(BOSSES):
                    current_boss = BOSSES[player["boss_index"]]
                    print(f"\n🚨 Boss Encounter! {current_boss['name']} appears!")
                    boss_data = current_boss.copy()
                    boss_data["type"] = "boss"
                    player = combat(player, boss_data, diff)
                    if player["health"] > 0:
                        print(f"🏆 You defeated {current_boss['name']}!")
                        player["boss_index"] += 1
                        player["gold"] += int(current_boss["gold"]*diff["gold_multiplier"])
                        player["xp"] += int(current_boss["xp"]*diff["xp_multiplier"])
                        print(f"+{int(current_boss['gold']*diff['gold_multiplier'])} Gold | +{int(current_boss['xp']*diff['xp_multiplier'])} XP")
                        # Fully heal after boss
                        player["health"] = player["max_health"]
                        print("❤️ You are fully healed after the boss!")
                    else:
                        break
                else:
                    print("All bosses defeated! You have won the game! 🏆")
                    break
            case _:
                print("The area is quiet...")

        # Level Up
        match player["xp"] >= 100:
            case True:
                player["level"] += 1
                player["xp"] = 0
                player["max_health"] += int(50*diff["hp_multiplier"])
                player["attack"] += 7
                player["health"] = player["max_health"]
                print(f"\n🎉 LEVEL UP! Now Level {player['level']}")

    if player["health"] <= 0:
        print("\n💀 GAME OVER")

# Start Game
adventure_game()