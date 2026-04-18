print("\n===INTRAMURALS SPORTS EVENT TRACKER===\n")
sports_list = [
    ["Basketball", "  [Team]"],
    ["Volleyball", "  [Team]"],
    ["Badminton", "  [Individual]"],
    ["Chess", "  [Individual]"],
    ["Table Tennis", "[Individual]"],
]
section_name, coordinator_name = input("Class Section: ").upper(), input("Coordinator Name: ").title()
print("\n")
print("="*35)
print(f"  {"INTRAMURALS -- SPORTS EVENTS"}")
print("="*35)
for i in range(len(sports_list)):
        print(f"{i+1:>3}. {sports_list[i][0]:<10} {sports_list[i][1]}")
print("="*35)

logged_games = []
total_points = 0
for i in range(1, 5):
    print(f"\n--- GAME {i} ---")
    sport_num = int(input("Sport number (0 to skip): "))
    
    while True:
        sport_num_input = input("Sport number (0 to skip): ").strip()
        
        # Manually check if the input is one of the allowed numbers
        if sport_num_input in ["0", "1", "2", "3", "4", "5"]:
            sport_num = int(sport_num_input)
            break
        
        print("Invalid Input.")

    if sport_num == 0:
        continue
    
    selected_sport = sports_list[sport_num - 1]
    opponent = input("Opposing section: ").strip()
    
    # Validation for Result using membership check
    while True:
        result = input("Result (W/L): ").upper().strip()
        if result in ["W", "L"]:
            break
        print("Invalid Input.")

    if result == 'W':
        points = 3
        result_text = "WIN"
    else:
        points = 0
        result_text = "LOSS"

    # Using index 0 and 1 specifically from the sport list
    game_data = [selected_sport[0], selected_sport[1], opponent, result_text, points]
    logged_games.append(game_data)
    total_points += points
        
standing = ""
if total_points >= 9:
    standing = "GOLD CONTENDER"
elif total_points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"
    
print("\n=============================================")
print(f"     {section_name} -- GAME RESULTS BOARD")
print("=============================================")
print(f"Coordinator: {coordinator_name}")
print("---------------------------------------------")
for idx, game in enumerate(logged_games, start=1):
    print(f"[{idx}] {game[0]:<9} {game[1]}")
    print(f"    vs {game[2]:<8} |  Result: {game[3]:<4} |  Points: {game[4]}")
    print(" ")

print("---------------------------------------------")
print(f"Total Points   : {total_points}")
print(f"Standing       : {standing}")
print("=============================================")
