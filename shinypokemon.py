from sinnohmain import Sinnoh
from shared import set_version
import random

def select_region():
    """
    Asks user which region they want to hunt in and returns the region method selected.

    Returns:
        function: The method associated with the region the user selected.
    """
    while True:
        print('\nWhich region would you like to explore?')
        print('Options: Sinnoh')
        print('Type 0 to quit')
        #converts input to string to match region_method
        region = input().lower()

        if region == '0':
            print('Exiting program, goodbye!')
            exit(0)

        region_method = select_region_version(region)
        if region_method:
            return region_method
        else:
            print("Invalid region selected. Please try again.")

def select_region_version(region):
    """
    Asks user which version of the given region they want to explore, sets the version, and returns the region method associated with the selected version.

    Parameters:
        region (str): The region the user wants to explore.

    Returns:
        function: The method associated with the region the user selected.
    """
    print(f'\nWhich version of the {region} region would you like to explore?')
    match region:
        case 'kanto':
            print('Options: Red, Blue, Yellow, Fire Red, Leaf Green, Heart Hold, Soul Silver, Lets Go Pikachu, Lets Go Eevee')
        case 'johto':
            print('Options: Gold, Silver, Crystal, Heart Gold, Soul Silver')
        case 'hoenn':
            print('Options: Ruby, Sapphire, Emerald, Omega Ruby, Alpha Sapphire')
        case 'sinnoh':
            print("Options: Diamond, Pearl, Platinum, Brilliant Diamond, Shining Pearl")
        case 'unova':
            print('Options: Black, White, Black2, White2')
        case 'kalos':
            print('Options: X, Y')
        case 'alola':
            print('Options: Sun, Moon, Ultra Sun, Ultra Moon')
        case 'galar':
            print('Options: Sword, Shield')
    version = input().lower()
    set_version(version)

    match region:
        case 'kanto':  
            match version:
                case "red" | "blue" | "yellow" | "fire red" | "leaf green" | "heart gold" | "soul silver" | "lets go pikachu" | "lets go eevee":
                    return #red()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'johto':
            match version:
                case "gold" | "silver" | "crystal" | "heart gold" | "soul silver":
                    return#gold()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'hoenn':
            match version:
                case "ruby" | "sapphire" | "emerald" | "omega ruby" | "alpha sapphire":
                    return#ruby()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'sinnoh':
            match version:
                case "diamond" | "pearl" | "platinum" | "brilliant diamond" | "shining pearl":
                    return Sinnoh.sinnohMain
                case _:
                    print("Invalid version selected. Please try again.")
        case 'unova':
            match version:
                case "black" | "white" | "black2" | "white2":
                    return#black()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'kalos':
            match version:
                case "x" | "y":
                    return#x()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'alola':
            match version:
                case "sun" | "moon" | "ultra sun" | "ultra moon":
                    return#sun()
                case _:
                    print("Invalid version selected. Please try again.")
        case 'galar':
            match version:
                case "sword" | "shield":
                    return#sword()
                case _:
                    print("Invalid version selected. Please try again.")    

def hunt_shinies(route_function):
    """
    Hunts for shiny Pokémon in the wild based on the given route function.

    Parameters:
        route_function (function): A function that takes no arguments and returns a string representing a Pokémon.

    Returns:
        tuple: A tuple containing the number of shinies hunted, the total number of encounters it took to find them all, and a list of all the shinies found.
    """
    shiny_num = get_shiny_hunt_number()
    #holds total encounters during hunt and list to hold the shinies caught
    total_encounters, shinies_found = 0, []

    # Loops through shiny_num, amount of shinies that are going to be hunted
    for i in range(shiny_num): 
        # Shiny value represents the value of the shiny Pokémon, i.e., the number that needs to be hit to guarantee a shiny            
        shiny_value = random.randint(1, 8192)
        count = 0
        # Loops until shiny is found, i.e., encounter value being equal to shiny value
        while True:
            encounter_value = random.randint(1, 8192)  # Generates shiny values, simulating encounters in the wild
            count += 1  # Increments number of encounters
            if shiny_value == encounter_value:
                # Calls route to determine which Pokémon was found when shiny value is hit
                shiny = route_function()
                shinies_found.append(shiny)  # Appends shiny to the list
                break
        
        print(f"Shiny {shiny} found! It took {count} encounters to find.")
        total_encounters += count  # Tallies up total encounters

    return shiny_num, total_encounters, shinies_found

def get_shiny_hunt_number():
    """
    Asks user how many shiny Pokémon they want to hunt and returns the answer as an integer.

    Returns:
        int: The number of shiny Pokémon the user wants to hunt.
    """
    while True:
        print("How many shiny Pokémon do you want to hunt?")
        try:
            return int(input())
        except ValueError:
            print("Not a valid number")                

def print_hunt_summary(shiny_num, total_encounters, shinies_found):
    """
    Prints out a summary of the hunt, including the total number of shinies, how many encounters it took to find them all, and the average number of encounters per shiny.

    Parameters:
        shiny_num (int): The number of shinies the user wanted to hunt.
        total_encounters (int): The total number of encounters it took to find all the shinies.
        shinies_found (list): A list of all the shinies that were found.
    """
    avg = total_encounters / shiny_num  # Calculates average per phase
    print(f"\nTotal shinies: {shiny_num} and it took {total_encounters} encounters to find them all!")
    print(f"\nAverage Phase: {avg}")
    print(f"The shinies found were: {', '.join(shinies_found)}")

def main():
    """
    Main loop of program. Allows user to select a region, route, and hunt for shiny Pokémon. 
    After each hunt, asks user if they want to continue hunting and if not, allows them to select another region.
    """
    while True:
        region_method = select_region()
        if not region_method:
            continue

        while True:
            route_function = region_method()
            if not route_function:
                break
            
            #simulates hunting and prints a summary
            shiny_num, total_encounters, shinies_found = hunt_shinies(route_function)
            print_hunt_summary(shiny_num, total_encounters, shinies_found)
            
            #hunting ends through y keystroke
            print(f"\nKeep hunting in this region? y/n")
            continueHunting = input().lower()
            if continueHunting != 'y':
                break

        print(f"\nWould you like to explore another region? y/n")
        explore_another_region = input().lower()
        if explore_another_region != 'y':
            print("Exiting program, goodbye!")
            break

if __name__ == "__main__":
    main()

# To do list:

# fix readme

# add in all versions of each region
# add in all towns and caves/buildings from sinnoh
# Add in shiny charm probability
# Add in other region compatibility
# Add in individual randomly generated stats for each shiny
# Organize these shinies by most appeal in their stats
# return stats about how many of certain pokemon you found