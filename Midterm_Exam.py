 #INITIAL INPUTS
section = input("Class section: ")
coordinator = input("Coordinator name: ")

# DATA STORAGE
sports_names = ["Basketball", "Volleyball", "Badminton", "Chess", "Table Tennis"]
sports_types = ["[Team]", "[Team]", "[Individual]", "[Individual]", "[Individual]"]

# TRACKING VARIABLES
selected_names = []
opponents = []
results = []
points_list = []
total_points = 0
game_count = 1

print("==========================================")
print("INTRAMURALS -- SPORTS EVENTS")
print("1 Basketball    [Team]")
print("2 Volleyball    [Team]")
print("3 Badminton     [Individual]")
print("4 Chess         [Individual]")
print("5 Table Tennis  [Individual]")

# INPUT LOOP (MAX 5 GAMES FOR BREVITY)
while game_count <= 5:
    print(f"--- GAME {game_count} ---")
    choice_raw = input("Sport number (0 to skip): ")
    
    # VALIDATION: CHECK FOR SIGNS, EXTRA SPACES, OR NON-DIGITS
    is_valid = True
    if not choice_raw.isdigit():
        is_valid = False
    
    if is_valid == False:
        print("Invalid input! Use numbers only without signs or spaces.")
    else:
        choice = int(choice_raw)
        
        if choice == 0:
            game_count = 6 # BREAK LOOP
        elif choice >= 1 and choice <= 5:
            opp_name = input("Opposing section: ")
            res = input("Result (W/L): ").upper()
            
            # CALCULATE POINTS
            if res == "W":
                pts = 3
                res_text = "WIN"
            else:
                pts = 0
                res_text = "LOSS"
            
            # SAVE DATA
            selected_names.append(sports_names[choice-1])
            opponents.append(opp_name)
            results.append(res_text)
            points_list.append(pts)
            total_points = total_points + pts
            
            game_count = game_count + 1
        else:
            print("Please choose 1-5 or 0 to skip.")

# CALCULATE STANDING
if total_points >= 9:
    standing = "GOLD CONTENDER"
elif total_points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"

# FINAL DISPLAY
print("=============================================")
print(section, "-- GAME RESULTS BOARD")
print("Coordinator :", coordinator)

# PRINT LISTED RESULTS
index = 0
while index < len(selected_names):
    print(f"[{index + 1}] {selected_names[index]}")
    print(f"vs {opponents[index]}  |  Result: {results[index]}  |  Points: {points_list[index]}")
    index = index + 1

print(f"Total Points   : {total_points}")
print(f"Standing       : {standing}")
