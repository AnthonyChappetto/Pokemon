from sinnohroutes import sinnohMain
import random

def main():
    while True:
        print('Which region would you like to explore?')
        print('Options: Sinnoh')
        region = input().lower()

        region_methods = {
            'sinnoh': sinnohMain
        }

        region_method = region_methods.get(region)

        if region_method is None:
            print("Invalid region selected. Please try again.")
        else:
            while True:
                route_function = region_method()
                if route_function is None:
                    continue

                # Asks how many should be hunted
                while True:
                    print("How many shiny Pokémon do you want to hunt?")
                    try:
                        shiny_num = int(input())
                        break
                    except ValueError:
                        print("Not a valid number")
        
                # Holds total encounters during the hunts
                total_encounters = 0
                # List to hold the shinies caught
                shinies_found = []

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
                    print("Shiny " + shiny + " found! It took " + str(count) + " encounters to find.")
                    total_encounters += count  # Tallies up total encounters
                
                avg = total_encounters / shiny_num  # Calculates average per phase
                print("\nTotal shinies: " + str(shiny_num) + " and it took " + str(total_encounters) + " encounters to find them all!")
                print("\nAverage Phase: " + str(avg))
                print(f"The shinies found were: {', '.join(shinies_found)}")

                print("Keep hunting??? y/n")
                continueHunting = input().lower()
                if continueHunting != 'y':
                    print("Ending program")
                    exit(0)

if __name__ == "__main__":
    main()

# To do list:

# implement extraction and inversion for excessive indentation
# fix readme
# add in more routes from sinnoh
# Add in shiny charm probability
# Add in other region compatibility
# Add in individual randomly generated stats for each shiny
# Organize these shinies by most appeal in their stats
# return stats about how many of certain pokemon you found