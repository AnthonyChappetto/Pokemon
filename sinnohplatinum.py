from sinnohmain import Sinnoh

#Represents Sinnoh region and all its routes
class SinnohPlatinum:
    @staticmethod
    def route201():
        """
        Simulates an encounter with a wild pokemon on Route 201 in the Sinnoh region.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        current_route = "Route 201"
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

    @staticmethod
    def route202():
        current_route = "Route 202"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "night"]: 
            route_pokemon = {
                "Starly": (30, ["morning", "night"]), 
                "Bidoof": (30, ["morning", "night"]),
                "Shinx": (30, ["morning", "night"]),
                "Kricketot": (10, ["morning", "night"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Starly": (30, ["day"]),
                "Bidoof": (50, ["day"]),
                "Shinx": (20, ["day"])
            }
        return Sinnoh.encounter_pokemon(route_pokemon) 

    @staticmethod
    def route203():
        current_route = "Route 203"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning": 
            route_pokemon = {
                "Starly": (35, ["morning"]), 
                "Shinx": (25, ["morning"]),
                "Abra": (15, ["morning"]),
                "Bidoof": (15, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Starly": (35, ["day"]),
                "Bidoof": (25, ["day"]),
                "Shinx": (25, ["day"]),
                "Abra": (15, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Starly": (25, ["night"]),
                "Shinx": (25, ["night"]),
                "Abra": (15, ["night"]),
                "Bidoof": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Kricketot": (10, ["night"])
            }
        return Sinnoh.encounter_pokemon(route_pokemon) 
    
    #doesn't work properly handing north and south rn
    @staticmethod
    def route204():
        current_route = "Route 204"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
            if time_of_day == "morning": 
                route_pokemon = {
                    "Starly": (25, ["morning"]), 
                    "Bidoof": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Budew": (15, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (25, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"]),
                    "Wurmple": (10, ["day"])
                }
            else: #time of day = night
                route_pokemon = {  
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Budew": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Kricketot": (10, ["night"])
                }
        else: #north
            if time_of_day == "morning": 
                route_pokemon = {
                    "Starly": (25, ["morning"]), 
                    "Bidoof": (25, ["morning"]),
                    "Shinx": (15, ["morning"]),
                    "Budew": (15, ["morning"]),
                    "Wurmple": (10, ["morning"]),
                    "Kricketot": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Starly": (25, ["day"]),
                    "Bidoof": (25, ["day"]),
                    "Budew": (25, ["day"]),
                    "Shinx": (15, ["day"]),
                    "Wurmple": (10, ["day"])
                }
            else: #time of day = night
                route_pokemon = {  
                    "Starly": (25, ["night"]),
                    "Bidoof": (25, ["night"]),
                    "Shinx": (15, ["night"]),
                    "Budew": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Kricketot": (10, ["night"])
                }
        return Sinnoh.encounter_pokemon(route_pokemon)       

    @staticmethod
    def route205():
        current_route = "Route 205"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
            route_pokemon = {
                "Shellos": (45, ["morning", "day", "night"]), 
                "Buizel": (35, ["morning", "day", "night"]),
                "Bidoof": (10, ["morning", "day", "night"]),
                "Pachirisu": (10, ["morning", "day", "night"]),
            }
        else: #north
            if time_of_day in ["morning", "night"]:
                route_pokemon = {
                    "Bidoof": (30, ["morning", "night"]),
                    "Budew": (28, ["morning", "night"]),
                    "Wurmple": (10, ["morning", "night"]),
                    "Silcoon": (10, ["morning", "night"]),
                    "Cascoon": (10, ["morning", "night"]),
                    "Kricketot": (10, ["morning", "night"]),
                    "Beautifly": (1, ["morning", "night"]),
                    "Dustox": (1, ["morning", "night"])
                }
            else: #daytime
                route_pokemon = {
                    "Budew": (38, ["day"]),
                    "Bidoof": (30, ["day"]),
                    "Wurmple": (10, ["day"]),
                    "Silcoon": (10, ["day"]),
                    "Cascoon": (10, ["day"]),
                    "Beautifly": (1, ["day"]),
                    "Dustox": (1, ["day"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route206():
        current_route = "Route 206"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Geodude": (30, ["morning"]),
                "Machop": (20, ["morning"]),
                "Ponyta": (20, ["morning"]),
                "Gligar": (20, ["morning"]),
                "Kricketune": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Geodude": (30, ["day"]),
                "Ponyta": (30, ["day"]),
                "Machop": (20, ["day"]),
                "Gligar": (20, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Geodude": (30, ["night"]),
                "Machop": (20, ["night"]),
                "Ponyta": (20, ["night"]),
                "Zubat": (10, ["night"]),
                "Gligar": (10, ["night"]),
                "Kricketune": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route207():
        current_route = "Route 207"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Machop": (35, ["morning"]),
                "Geodude": (30, ["morning"]),
                "Ponyta": (25, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Machop": (45, ["day"]),
                "Geodude": (30, ["day"]),
                "Ponyta": (25, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Machop": (35, ["night"]),
                "Geodude": (30, ["night"]),
                "Ponyta": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Kricketot": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route208():
        current_route = "Route 208"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Budew": (30, ["morning", "day"]),
                "Bidoof": (20, ["morning", "day"]),
                "Bibarel": (20, ["morning", "day"]),
                "Ralts": (15, ["morning", "day"]),
                "Roselia": (15, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Bidoof": (20, ["night"]),
                "Bibarel": (20, ["night"]),
                "Budew": (20, ["night"]),
                "Ralts": (15, ["night"]),
                "Roselia": (15, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route209():
        current_route = "Route 209"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Bibarel": (30, ["morning", "day"]),
                "Roselia": (25, ["morning", "day"]),
                "Ralts": (20, ["morning", "day"]),
                "Staravia": (20, ["morning", "day"]),
                "Chansey": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Bibarel": (30, ["night"]),
                "Roselia": (25, ["night"]),
                "Zubat": (10, ["night"]),
                "Ralts": (10, ["night"]),
                "Duskull": (10, ["night"]),
                "Staravia": (10, ["night"]),
                "Chansey": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route210():
        current_route = "Route 210"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
            if time_of_day == "morning":
                route_pokemon = {
                    "Ponyta": (25, ["morning"]),
                    "Geodude": (20, ["morning"]),
                    "Staravia": (20, ["morning"]),
                    "Scyther": (15, ["morning"]),
                    "Roselia": (15, ["morning"]),
                    "Chansey": (5, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Ponyta": (35, ["day"]),
                    "Geodude": (20, ["day"]),
                    "Roselia": (15, ["day"]),
                    "Staravia": (10, ["day"]),
                    "Chansey": (5, ["day"]),
                    "Scyther": (5, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Geodude": (20, ["night"]),
                    "Staravia": (20, ["night"]),
                    "Ponyta": (15, ["night"]),
                    "Roselia": (15, ["night"]),
                    "Scyther": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Chansey": (5, ["night"])
                }
        #North section of the routes encounters
        else:
            if time_of_day == "morning":
                route_pokemon = {
                    "Meditite": (20, ["morning"]),
                    "Swablu": (20, ["morning"]),
                    "Bibarel": (20, ["morning"]),
                    "Machop": (15, ["morning"]),
                    "Scyther": (15, ["morning"]),
                    "Machoke": (10, ["morning"])
                }
            elif time_of_day == "day":
                route_pokemon = {
                    "Swablu": (30, ["day"]),
                    "Meditite": (20, ["day"]),
                    "Bibarel": (20, ["day"]),
                    "Machop": (15, ["day"]),
                    "Machoke": (10, ["day"]),
                    "Scyther": (5, ["day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Swablu": (20, ["night"]),
                    "Bibarel": (20, ["night"]),
                    "Machop": (15, ["night"]),
                    "Machoke": (10, ["night"]),
                    "Meditite": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Scyther": (5, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route211():
        current_route = "Route 211"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_eastwest(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "east":
            if time_of_day in ["morning", "day"]: 
                route_pokemon = {
                    "Meditite": (40, ["morning", "day"]),
                    "Graveler": (20, ["morning", "day"]),
                    "Machoke": (15, ["morning", "day"]),
                    "Chingling": (15, ["morning", "day"]),
                    "Bronzor": (10, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Graveler": (20, ["night"]),
                    "Meditite": (20, ["night"]),
                    "Machoke": (15, ["night"]),
                    "Chingling": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Noctowl": (10, ["night"]),
                    "Bronzor": (5, ["night"])
                }
        else: #west section of the routes encounters
            if time_of_day in ["morning", "day"]:
                route_pokemon = {   
                    "Meditite": (40, ["morning", "day"]),
                    "Bidoof": (20, ["morning", "day"]),
                    "Machop": (15, ["morning", "day"]),
                    "Chingling": (15, ["morning", "day"]),
                    "Bronzor": (10, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Meditite": (20, ["night"]),
                    "Bidoof": (20, ["night"]),
                    "Machop": (15, ["night"]),
                    "Chingling": (15, ["night"]),
                    "Zubat": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Bronzor": (10, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route212():
        current_route = "Route 212"
        time_of_day = Sinnoh.grab_user_time()

        #Grabs the user's current cardinal direction from their input
        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "north":
            if time_of_day in ["morning", "day"]: 
                route_pokemon = {
                    "Roselia": (35, ["morning", "day"]),
                    "Marill": (25, ["morning", "day"]),
                    "Kirlia": (20, ["morning", "day"]),
                    "Staravia": (20, ["morning", "day"])
                }
            else: #time of day = night
                route_pokemon = {
                    "Marill": (45, ["night"]),
                    "Roselia": (35, ["night"]),
                    "Kirlia": (10, ["night"]),
                    "Staravia": (10, ["night"])
                }
        else: #south section of the routes encounters
                route_pokemon = {
                    "Shellos": (45, ["morning", "day", "night"]),
                    "Quagsire": (30, ["morning", "day", "night"]),
                    "Buizel": (15, ["morning", "day", "night"]),
                    "Croagunk": (10, ["morning", "day", "night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route213():
        current_route = "Route 213"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Shellos": (35, ["morning", "day"]),
                "Buizel": (25, ["morning", "day"]),
                "Wingull": (20, ["morning", "day"]),
                "Chatot": (20, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Shellos": (45, ["night"]),
                "Buizel": (35, ["night"]),
                "Wingull": (20, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route214():
        current_route = "Route 214"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Graveler": (35, ["morning"]),
                "Rhyhorn": (30, ["morning"]),
                "Geodude": (20, ["morning"]),
                "Houndoor": (15, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
               "Graveler": (35, ["day"]),
               "Houndoor": (25, ["day"]),
               "Geodude": (20, ["day"]),
               "Rhyhorn": (20, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Rhyhorn": (30, ["night"]),
                "Graveler": (25, ["night"]),
                "Geodude": (20, ["night"]),
                "Houndoor": (15, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route215():
        current_route = "Route 215"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {   
                "Staravia": (30, ["morning"]),
                "Marill": (25, ["morning"]),
                "Scyther": (15, ["morning"]),
                "Abra": (10, ["morning"]),
                "Kadabra": (10, ["morning"]),
                "Lickitung": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Staravia": (40, ["day"]),
                "Marill": (25, ["day"]),
                "Abra": (10, ["day"]),
                "Kadabra": (10, ["day"]),
                "Lickitung": (10, ["day"]),
                "Scyther": (5, ["day"])    
            }
        else: #time of day = night
            route_pokemon = {
                "Marill": (45, ["night"]),
                "Staravia": (20, ["night"]),
                "Abra": (10, ["night"]),
                "Kadabra": (10, ["night"]),
                "Lickitung": (10, ["night"]),
                "Scyther": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route216():
        current_route = "Route 216"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Snover": (40, ["morning", "day"]),
                "Sneasel": (35, ["morning", "day"]),
                "Meditite": (20, ["morning", "day"]),
                "Graveler": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Sneasel": (35, ["night"]),
                "Snover": (30, ["night"]),
                "Zubat": (10, ["night"]),
                "Meditite": (10, ["night"]),
                "Snorunt": (10, ["night"]),
                "Graveler": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route217():
        current_route = "Route 217"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Snover": (40, ["morning", "day"]),
                "Swinub": (35, ["morning", "day"]),
                "Sneasel": (25, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Swinub": (35, ["night"]),
                "Snover": (30, ["night"]),
                "Snorunt": (20, ["night"]),
                "Sneasel": (15, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)

    def route218():
        current_route = "Route 218"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Floatzel": (30, ["morning", "day"]),
                "Mr. Mime": (25, ["morning", "day"]),
                "Gastrodon": (25, ["morning", "day"]),
                "Chatot": (20, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Floatzel": (40, ["night"]),
                "Gastrodon": (35, ["night"]),
                "Mr. Mime": (25, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route219():
        current_route = "Route 219"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Tentacool": (60, ["morning", "day", "night"]),
            "Wingull": (30, ["morning", "day", "night"]),
            "Tentacruel": (9, ["morning", "day", "night"]),
            "Pelipper": (1, ["morning", "day", "night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route220():
        current_route = "Route 220"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Tentacool": (60, ["morning", "day", "night"]),
            "Wingull": (30, ["morning", "day", "night"]),
            "Tentacruel": (9, ["morning", "day", "night"]),
            "Pelipper": (1, ["morning", "day", "night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route221():
        current_route = "Route 221"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Sudowoodo": (25, ["morning", "day", "night"]),
            "Girafarig": (25, ["morning", "day", "night"]),
            "Roselia": (25, ["morning", "day", "night"]),
            "Flotzel": (25, ["morning", "day", "night"])
            }
        
        return Sinnoh.encounter_pokemon(route_pokemon)
    def route222():
        current_route = "Route 222"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Electabuzz": (30, ["morning", "day"]),
                "Floatzel": (20, ["morning", "day"]),
                "Magnemite": (10, ["morning", "day"]),
                "Wingull": (10, ["morning", "day"]),
                "Luxio": (10, ["morning", "day"]),
                "Chatot": (10, ["morning", "day"]),
                "Magneton": (5, ["morning", "day"]),
                "Pelipper": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Floatzel": (40, ["night"]),
                "Electabuzz": (20, ["night"]),
                "Magnemite": (10, ["night"]),
                "Wingull": (10, ["night"]),
                "Luxio": (10, ["night"]),
                "Magenton": (5, ["night"]),
                "Pelipper": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route223():
        current_route = "Route 223"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Tentacruel": (60, ["morning", "day", "night"]),
            "Pelipper": (30, ["morning", "day", "night"]),
            "Mantyke": (10, ["morning", "day", "night"])
        }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route224():
        current_route = "Route 224"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Bellsprout": (20, ["morning", "day"]),
                "Roselia": (20, ["morning", "day"]),
                "Floatzel": (20, ["morning", "day"]),
                "Pelipper": (10, ["morning", "day"]),
                "Gastrodon": (10, ["morning", "day"]),
                "Gloom": (5, ["morning", "day"]),
                "Weepinbell": (5, ["morning", "day"]),
                "Beautifly": (5, ["morning", "day"]),
                "Dustox": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Oddish": (20, ["night"]),
                "Roselia": (20, ["night"]),
                "Floatzel": (20, ["night"]),
                "Pelipper": (10, ["night"]),
                "Gastrodon": (10, ["night"]),
                "Gloom": (5, ["night"]),
                "Weepinbell": (5, ["night"]),
                "Beautifly": (5, ["night"]),
                "Dustox": (5, ["night"])                
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route225():
        current_route = "Route 225"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Fearow": (30, ["morning", "day"]),
                "Machoke": (25, ["morning", "day"]),
                "Graveler": (20, ["morning", "day"]),
                "Raticate": (15, ["morning", "day"]),
                "Rattata": (5, ["morning", "day"]),
                "Spearow": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Machoke": (25, ["night"]),
                "Graveler": (20, ["night"]),
                "Banette": (20, ["night"]),
                "Raticate": (15, ["night"]),
                "Fearow": (10, ["night"]),
                "Rattata": (5, ["night"]),
                "Spearow": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route226():
        current_route = "Route 226"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Machoke": (25, ["morning", "day"]),
                "Fearow": (20, ["morning", "day"]),
                "Graveler": (20, ["morning", "day"]),
                "Raticate": (15, ["morning", "day"]),
                "Wingull": (15, ["morning", "day"]),
                "Rattata": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Machoke": (25, ["night"]),
                "Graveler": (20, ["night"]),
                "Banette": (20, ["night"]),
                "Raticate": (15, ["night"]),
                "Wingull": (15, ["night"]),
                "Rattata": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route227():
        current_route = "Route 227"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Fearow": (20, ["morning", "day"]),
                "Rhydon": (20, ["morning", "day"]),
                "Camerupt": (20, ["morning", "day"]),
                "Graveler": (15, ["morning", "day"]),
                "Weezing": (10, ["morning", "day"]),
                "Rhyhorn": (5, ["morning", "day"]),
                "Skarmory": (5, ["morning", "day"]),
                "Numel": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Rhydon": (20, ["night"]),
                "Camerupt": (20, ["night"]),
                "Graveler": (15, ["night"]),
                "Fearow": (10, ["night"]),
                "Golbat": (10, ["night"]),
                "Weezing": (10, ["night"]),
                "Rhyhorn": (5, ["night"]),
                "Skarmory": (5, ["night"]),
                "Numel": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route228():
        current_route = "Route 228"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Dugtrio": (30, ["morning", "day"]),
                "Rhydon": (20, ["morning", "day"]),
                "Cacturne": (20, ["morning", "day"]),
                "Hippowdon": (20, ["morning", "day"]),
                "Diglett": (5, ["morning", "day"]),
                "Cacnea": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Cacturne": (40, ["night"]),
                "Dugtrio": (30, ["night"]),
                "Rhydon": (10, ["night"]),
                "Hippowdon": (10, ["night"]),
                "Diglett": (5, ["night"]),
                "Cacnea": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    def route229():
        current_route = "Route 229"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Roselia": (45, ["morning"]),
                "Ledian": (20, ["morning"]),
                "Volbeat": (10, ["morning"]),
                "Illumise": (10, ["morning"]),
                "Pidgey": (5, ["morning"]),
                "Beautifly": (5, ["morning"]),
                "Dustox": (5, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Roselia": (45, ["day"]),
                "Pidgey": (25, ["day"]),
                "Volbeat": (10, ["day"]),
                "Illumise": (10, ["day"]),
                "Beautifly": (5, ["day"]),
                "Dustox": (5, ["day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Roselia": (45, ["night"]),
                "Ariados": (20, ["night"]),
                "Volbeat": (10, ["night"]),
                "Illumise": (10, ["night"]),
                "Pidgey": (5, ["night"]),
                "Beautifly": (5, ["night"]),
                "Dustox": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)  
    def route230():
        current_route = "Route 230"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Pelipper": (30, ["morning", "day"]),
                "Floatzel": (25, ["morning", "day"]),
                "Bellsprout": (20, ["morning", "day"]),
                "Roselia": (10, ["morning", "day"]),
                "Gloom": (5, ["morning", "day"]),
                "Weepinbell": (5, ["morning", "day"]),
                "Wingull": (5, ["morning", "day"])
            }
        else: #time of day = night
            route_pokemon = {
                "Pelipper": (30, ["night"]),
                "Floatzel": (25, ["night"]),
                "Oddish": (20, ["night"]),
                "Roselia": (10, ["night"]),
                "Gloom": (5, ["night"]),
                "Weepinbell": (5, ["night"]),
                "Wingull": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)