while True:
    print("\n===INTRAMURALS SPORTS EVENT TRACKER===")
    section = input("\nClass section: ").upper()
    coordinator = input("Coordinator name: ").title()

    sports = [
        ["Basketball", "  [Team]"],
        ["Volleyball", "  [Team]"],
        ["Badminton", "  [Individual]"],
        ["Chess", "  [Individual]"],
        ["Table Tennis", "[Individual]"]
    ]

    selected_games = []
    total_points = 0
    game_count = 1

    print("\n==========================================")
    print(f"      {"INTRAMURALS -- SPORTS EVENTS"}")
    print("==========================================")

    i = 0
    while i < len(sports):
        print(f"{i+1:>3}. {sports[i][0]:<10} {sports[i][1]}")
        i += 1

    while game_count <= 4:
        print(f"\n--- GAME {game_count} ---")
        choice_raw = input("Sport number (0 to skip): ")
        
        if not choice_raw.isdigit():
            print("Invalid input!")
        else:
            choice = int(choice_raw)
            
            if choice == 0:
                print("Game skipped.")
                selected_games.append([
                    "No Game",
                    "",
                    "-",
                    "SKIPPED",
                    0
                ])
                game_count += 1
                continue

            elif 1 <= choice <= 5:
                opp_name = input("Opposing section: ")
                res = input("Result (W/L): ").upper()

                if res == "W":
                    pts = 3
                    res_text = "WIN"
                elif res == "L":
                    pts = 0
                    res_text = "LOSS"
                else:
                    print("Invalid result! Please enter W or L.")
                    continue
                
                selected_games.append([
                    sports[choice-1][0],
                    sports[choice-1][1],
                    opp_name,
                    res_text,
                    pts
                ])
                
                total_points += pts
                game_count += 1
            else:
                print("Please choose 1-5 or 0 to skip.")

    if total_points >= 9:
        standing = "GOLD CONTENDER"
    elif total_points >= 6:
        standing = "SILVER PUSH"
    else:
        standing = "KEEP FIGHTING!"

    print("\n=============================================")
    print(section, "-- GAME RESULTS BOARD")
    print("=============================================")
    print("Coordinator :", coordinator)
    print("=============================================\n")


    i = 0
    while i < len(selected_games):
        game = selected_games[i]
        print(f"[{i+1}] {game[0]} {game[1]}")
        print(f"vs {game[2]}  |  Result: {game[3]}  |  Points: {game[4]}")
        i += 1

    print(f"\nTotal Points   : {total_points}")
    print(f"Standing       : {standing}")
    
    question = input("Would you like to try the tracker again? [Yes/No]: ").title()
    if question == "Yes":
        print("Continuing...")
        continue
    elif question == "No":
        print("Exiting...")
        break
    else:
        print("Invalid result! Please enter W or L.")
        break
