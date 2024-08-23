import random
from datetime import datetime # importing py functions

#Represents Sinnoh region and all its routes
class Sinnoh:
    
    @staticmethod
    def grab_user_time():
        now = datetime.now()    #grabs user datetime from built in py function
        current_hour = now.hour #grabs exact hour and places in current hour

        if 20 <= current_hour or current_hour < 4: #8:00pm to 3:59am
            return "night"
        elif 4 <= current_hour < 10: #4am to 9:59am
            return "morning"
        else:   #10AM to 7:59pm
            return "day"

    @staticmethod
    def encounter_pokemon(route_pokemon):
        time_of_day = Sinnoh.grab_user_time()   #grabs user time and stores in time_of_day
        pokemon_found = random.randint(1, 100)  #grabs random percentage and stores in pokemon_found

        for pokemon, (chance, times) in route_pokemon.items(): #goes through list of pokemon based on time of day and chance
            if time_of_day in times and pokemon_found <= chance: #checks if user time of day is equal to pokemon allowed to be out during that time based on the roll of the dice
                return pokemon
            pokemon_found -= chance
        return "No Pokemon found"

    @staticmethod
    def route201():
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "night"]: #morning and night have same odds so they're combined
            route_pokemon = {
                "Starly": (50, ["morning", "night"]), #pokemon starly is the key paired with the values chance (50%) and time (morning and night)
                "Bidoof": (40, ["morning", "night"]),
                "Kricketot": (10, ["morning", "night"])
            }
        elif time_of_day == "day": #if time is day
            route_pokemon = {
                "Starly": (50, ["day"]),
                "Bidoof": (50, ["day"]),
            }
        return Sinnoh.encounter_pokemon(route_pokemon) #returns the pokemon to put into the list

#currently broken
    @staticmethod
    def route202():
        pokemonFound = random.randint(1,100)
        if pokemonFound <= 20:  #20% chance
            shiny = "Starly"
        elif pokemonFound <= 70:    #50% chance (from 21 to 70)
            shiny = "Bidoof"
        else:
            shiny = "Shinx" # 30% chance (from 71 to 100)
        return shiny
    #currently broken
    def route203():
        pokemonFound = random.randint(1,100)
        if pokemonFound <= 35:  
            shiny = "Starly"
        elif pokemonFound <= 60:    
            shiny = "Bidoof"
        elif pokemonFound <= 85:
            shiny = "Shinx"
        else:
            shiny = "Abra"
        return shiny
    def route204():
        return
    def route205():
        return
    def route206():
        return
    def route207():
        return
    def route208():
        return
    def route209():
        return
    def route210():
        return
    def route211():
        return
    def route212():
        return
    def route213():
        return

def main():
    #Prompts user to choose a route
    print("Choose a route: \n201\n202\n203")
    try:
        #Takes user input as an int
        route_choice = int(input())   
    except ValueError:
        #Error handling if char is entered as input instead of number
        print("Not a valid number")
        exit(0)

    #Assigns corresponding method based on user choice
    route_methods = {
        201: Sinnoh.route201,
        202: Sinnoh.route202,
        203: Sinnoh.route203
    }

    route = route_methods.get(route_choice) #error checking for incorrect value
    if route is None:
        print("Invalid route selected")
        exit(1)
    
    #Askes how many should be hunted
    print("How many shiny pokemon do you want to hunt?")
    try:
        shiny_num = int(input())
    except ValueError:
        print("Not a valid number")
        exit(0)

    #Holds total encounters during the hunts
    total_encounters = 0
    #List to hold the shinys caught
    shinies_found = []

    #Loops through shiny num, amount of shinys that are going to be hunted
    for i in range(shiny_num): 
        #Shiny value represents the value of the shiny pokemon, ie the number that needs to be hit to gaureentee a shiny
        shiny_value = random.randint(1, 8192)
        count = 0
        #Loops until shiny is found, ie encounter value being equal to shiny value
        while True:
            encounter_value = random.randint(1,8192) #generates shiny values, simulating encounteres in the wild
            count += 1  #increments number of shinies
            if shiny_value == encounter_value:
                #Calls route to determine which pokemon was found when shiny value is hit
                shiny = route()
                shinies_found.append(shiny) #Apends shiny to the list
                break
        print("Shiny " + shiny + " found! It took " + str(count) + " encounters to find")
        total_encounters += count #Tallies up total encounters
    avg = total_encounters / shiny_num #Calculates average per phase
    print("\nTotal shinies: " + str(shiny_num) + " and it took " + str(total_encounters) + " encounters to find them all!")
    print("\nAverage Phase: " + str(avg))
    print(f"The shinies found were: {', '.join(shinies_found)}")

#Entry point
if __name__ == "__main__":
    main()

# To do list:

# make different files to condense the code
# add in more routes from sinnoh
# Add in shiny charm probability
# Add in other region compatibility
# Add in individual randomly generated stats for each shiny
# Organize these shinies by most appeal in their stats
# return stats about how many of certain pokemon you found