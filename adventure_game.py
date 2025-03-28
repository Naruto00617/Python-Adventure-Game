import time

player = {
    "has_key": False,
    "has_map": False,
    "has_torch": False
}

def start_game():
    print("Welcome to 'The Quest for the Ancient Treasure'!\n")
    time.sleep(1)
    print("You wake up in a dense, mysterious forest. The trees loom overhead, and the air is thick with fog.")
    time.sleep(1)
    print("You remember your quest: find the legendary treasure hidden in an ancient castle deep within the forest.\n")
    time.sleep(1)
    forest_scene()

def forest_scene():
    print("You stand at a crossroads with three paths:")
    print("Left - Winding path between twisted trees")
    print("Right - Trail leading downhill")
    print("Straight - Overgrown route through thick bushes\n")
    choice = input("Which path do you take? (left/right/straight) ").lower().strip()
    
    if choice == "left":
        wizard_scene()
    elif choice == "right":
        river_scene()
    elif choice == "straight":
        trapdoor_scene()
    else:
        print("\nInvalid choice. Please try again.")
        forest_scene()

def wizard_scene():
    global player
    print("\nYou follow the left path and find a glowing campfire.")
    time.sleep(1)
    print("An ancient wizard materializes from the smoke!\n")
    time.sleep(1)
    print("Wizard: 'Answer my riddle to prove your worth!'")
    print("'What has keys but opens no locks? Has space but no room? You can enter but never go in?'\n")
    
    answer = input("Your answer: ").lower().strip()
    if answer == "keyboard" or answer == "piano":
        print("\nWizard: 'Correct! Take this golden key to the castle.'")
        player["has_key"] = True
        time.sleep(1)
        castle_scene()
    else:
        print("\nWizard: 'Foolish mortal! Your journey ends here.'")
        time.sleep(1)
        game_over()

def river_scene():
    global player
    print("\nYou descend the right path to a raging river.")
    time.sleep(1)
    print("The stone bridge has collapsed. You see:\n1) Dangerous rapids\n2) Materials for a raft\n")
    choice = input("Swim across or build a raft? (swim/build) ").lower().strip()
    
    if choice == "build":
        print("\nIt takes hours, but you construct a sturdy raft.")
        time.sleep(1)
        print("While crossing, you spot a waterlogged map in the reeds!")
        player["has_map"] = True
        castle_scene()
    elif choice == "swim":
        print("\nThe current drags you under! You manage to...")
        time.sleep(2)
        print("...wash up miles downstream, lost and exhausted.")
        game_over()
    else:
        print("\nInvalid choice.")
        river_scene()

def trapdoor_scene():
    global player
    print("\nPushing through bushes reveals a rusted trapdoor!")
    time.sleep(1)
    print("It creaks open to show a ladder descending into darkness.\n")
    choice = input("Take a nearby torch or descend blindly? (torch/dark) ").lower().strip()
    
    if choice == "torch":
        print("\nThe flickering torch reveals pit traps and secret symbols!")
        time.sleep(1)
        print("You follow the symbols to a hidden exit near the castle.")
        player["has_torch"] = True
        castle_scene()
    elif choice == "dark":
        print("\nYour foot hits a tripwire! Arrows shoot from the walls...")
        time.sleep(2)
        game_over()
    else:
        print("\nInvalid choice.")
        trapdoor_scene()

def castle_scene():
    global player
    print("\nYou arrive at the crumbling castle under stormy skies!")
    time.sleep(1)
    
    if player["has_key"]:
        print("The golden key unlocks the massive front gates!")
        treasure_room()
    elif player["has_map"]:
        print("Following the map's secret route through the sewers...")
        time.sleep(1)
        treasure_room()
    elif player["has_torch"]:
        print("Torchlight reveals a hidden door in the courtyard wall!")
        time.sleep(1)
        treasure_room()
    else:
        print("Without guidance, you wander until castle guards capture you!")
        game_over()

def treasure_room():
    print("\nYou enter the treasure chamber! Gold and jewels glitter everywhere!")
    time.sleep(1)
    print("Ancient carvings warn: 'Take only what you can carry wisely.'\n")
    time.sleep(1)
    
    choice = input("Grab a handful of gems or inspect a strange artifact? (gems/artifact) ").lower().strip()
    if choice == "artifact":
        print("\nThe artifact glows! It transports you home, rich beyond dreams!")
        happy_ending()
    else:
        print("\nThe ceiling collapses as you grab gems! But you escape with...")
        time.sleep(1)
        print("...enough wealth to live comfortably ever after!")
        happy_ending()

def happy_ending():
    print("\n\n*** CONGRATULATIONS! You completed your quest! ***")
    play_again()

def game_over():
    print("\n\n*** YOUR QUEST ENDS HERE ***")
    play_again()

def play_again():
    choice = input("\nPlay again? (yes/no): ").lower().strip()
    if choice == "yes":
        global player
        player = {"has_key": False, "has_map": False, "has_torch": False}
        start_game()
    else:
        print("\nThanks for playing!")

if __name__ == "__main__":
    start_game()
