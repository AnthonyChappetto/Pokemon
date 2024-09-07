class Pearl:

    @staticmethod
    def route206():
        from sinnohmain import Sinnoh

        current_route = "Route 206"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Geodude": (35, ["morning"]),
                "Ponyta": (35, ["morning"]),
                "Kricketune": (10, ["morning"]),
                "Bronzor": (10, ["morning"]),
                "Kricketot": (10, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Ponyta": (45, ["day"]),
                "Geodude": (35, ["day"]),
                "Kricketune": (10, ["day"]),
                "Bronzor": (10, ["day"])
            }
        else: #night
            route_pokemon = {
                "Geodude": (35, ["night"]),
                "Ponyta": (35, ["night"]),
                "Kricketune": (10, ["night"]),
                "Bronzor": (10, ["night"]),
                "Zubat": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route209():
        from sinnohmain import Sinnoh

        current_route = "Route 209"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Bibarel": (35, ["morning"]),
                "Bonsly": (25, ["morning"]),
                "Starly": (20, ["morning"]),
                "Staravia": (15, ["morning"]),
                "Chansey": (5, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Bibarel": (45, ["day"]),
                "Staravia": (25, ["day"]),
                "Starly": (20, ["day"]),
                "Chansey": (5, ["day"]),
                "Bonsly": (5, ["day"])
            }
        else: #night
            route_pokemon = {
                "Bibarel": (35, ["night"]),
                "Starly": (20, ["night"]),
                "Staravia": (15, ["night"]),
                "Zubat": (10, ["night"]),
                "Gastly": (10, ["night"]),
                "Chansey": (5, ["night"]),
                "Bonsly": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route210():
        from sinnohmain import Sinnoh
        current_route = "Route 210"
        time_of_day = Sinnoh.grab_user_time()

        if not Sinnoh.user_stored_location:
            Sinnoh.set_route_cardinal_direction_northsouth(current_route)

        cardinality = Sinnoh.user_stored_location

        #South section of the routes encounters
        if cardinality == "south":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Geodude": (30, ["morning"]),
                        "Ponyta": (30, ["morning"]),
                        "Bonsly": (25, ["morning"]),
                        "Kricketune": (10, ["morning"]),
                        "Chansey": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Ponyta": (50, ["day"]),
                        "Geodude": (30, ["day"]),
                        "Kricketune": (10, ["day"]),
                        "Chansey": (5, ["day"]),
                        "Bonsly": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Ponyta": (30, ["night"]),
                        "Kricketune": (30, ["night"]),
                        "Bonsly": (25, ["night"]),
                        "Geodude": (10, ["night"]),
                        "Chansey": (5, ["night"])
                    }
        #North section of the routes encounters
        elif cardinality == "north":
            if time_of_day in ["morning", "day"]:
                route_pokemon = {
                    "Meditite": (30, ["morning", "day"]),
                    "Psyduck": (20, ["morning", "day"]),
                    "Machop": (20, ["morning", "day"]),
                    "Bibarel": (20, ["morning", "day"]),
                    "Machoke": (10, ["morning", "day"])
                }
            else: #night
                route_pokemon = {
                    "Psyduck": (20, ["night"]),
                    "Machop": (20, ["night"]),
                    "Meditite": (20, ["night"]),
                    "Bibarel": (20, ["night"]),
                    "Machoke": (10, ["night"]),
                    "Hoothoot": (10, ["night"]),
                    "Noctowl": (10, ["night"])
                }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route214():
        from sinnohmain import Sinnoh

        current_route = "Route 214"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Ponyta": (35, ["morning", "day"]),
                "Geodude": (20, ["morning", "day"]),
                "Graveler": (15, ["morning", "day"]),
                "Sudowoodo": (15, ["morning", "day"]),
                "Girafarig": (10, ["morning", "day"]),
                "Kricketune": (5, ["morning", "day"])
            }
        else:
            route_pokemon = {
                "Ponyta": (25, ["night"]),
                "Kricketune": (25, ["night"]),
                "Geodude": (20, ["night"]),
                "Sudowoodo": (15, ["night"]),
                "Girafarig": (10, ["night"]),
                "Graveler": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route218():
        from sinnohmain import Sinnoh

        current_route = "Route 218"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Floatzel": (35, ["morning", "day", "night"]),
            "Shellos": (20, ["morning", "day", "night"]),
            "Gastrodon": (20, ["morning", "day", "night"]),
            "Glameow": (15, ["morning", "day", "night"]),
            "Wingull": (10, ["morning", "day", "night"]),
        }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route221():
        from sinnohmain import Sinnoh

        current_route = "Route 221"
        time_of_day = Sinnoh.grab_user_time()
        
        route_pokemon = {
            "Gastrodon": (30, ["morning", "day", "night"]),
            "Floatzel": (25, ["morning", "day", "night"]),
            "Sudowoodo": (15, ["morning", "day", "night"]),
            "Wingull": (10, ["morning", "day", "night"]),
            "Roselia": (10, ["morning", "day", "night"]),
            "Shellos": (10, ["morning", "day", "night"])
        }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route222():
        from sinnohmain import Sinnoh

        current_route = "Route 222"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Floatzel": (25, ["morning", "day"]),
                "Glameow": (20, ["morning", "day"]),
                "Chatot": (20, ["morning", "day"]),
                "Purugly": (15, ["morning", "day"]),
                "Wingull": (10, ["morning", "day"]),
                "Gastrodon": (10, ["morning", "day"])
            }
        else:
            route_pokemon = {
                "Floatzel": (35, ["night"]),
                "Gastrodon": (20, ["night"]),
                "Glameow": (20, ["night"]),
                "Purugly": (15, ["night"]),
                "Wingull": (10, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route225():
        from sinnohmain import Sinnoh

        current_route = "Route 225"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day in ["morning", "day"]:
            route_pokemon = {
                "Fearow": (40, ["morning", "day"]),
                "Raticate": (30, ["morning", "day"]),
                "Roselia": (15, ["morning", "day"]),
                "Rattata": (5, ["morning", "day"]),
                "Spearow": (5, ["morning", "day"]),
                "Machoke": (5, ["morning", "day"]),
            }
        else:
            route_pokemon = {
                "Fearow": (20, ["night"]),
                "Raticate": (30, ["night"]),
                "Banette": (20, ["night"]),
                "Roselia": (15, ["night"]),
                "Rattata": (5, ["night"]),
                "Spearow": (5, ["night"]),
                "Machoke": (5, ["night"]),
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route229():
        from sinnohmain import Sinnoh

        current_route = "Route 229"
        time_of_day = Sinnoh.grab_user_time()

        if time_of_day == "morning":
            route_pokemon = {
                "Gloom": (20, ["morning"]),
                "Weepinbell": (20, ["morning"]),
                "Ledian": (20, ["morning"]),
                "Volbeat": (10, ["morning"]),
                "Purugly": (10, ["morning"]),
                "Oddish": (5, ["morning"]),
                "Bellsprout": (5, ["morning"]),
                "Pinsir": (5, ["morning"]),
                "Illumise": (5, ["morning"])
            }
        elif time_of_day == "day":
            route_pokemon = {
                "Gloom": (30, ["day"]),
                "Weepinbell": (30, ["day"]),
                "Volbeat": (10, ["day"]),
                "Purugly": (10, ["day"]),
                "Oddish": (5, ["day"]),
                "Bellsprout": (5, ["day"]),
                "Pinsir": (5, ["day"]),
                "Illumise": (5, ["day"])
            }
        else:
            route_pokemon = {
                "Gloom": (20, ["night"]),
                "Weepinbell": (20, ["night"]),
                "Ariados": (20, ["night"]),
                "Volbeat": (10, ["night"]),
                "Purugly": (10, ["night"]),
                "Oddish": (5, ["night"]),
                "Bellsprout": (5, ["night"]),
                "Pinsir": (5, ["night"]),
                "Illumise": (5, ["night"])
            }

        return Sinnoh.encounter_pokemon(route_pokemon)
    @staticmethod
    def route230():
        from sinnohmain import Sinnoh

        current_route = "Route 230"
        time_of_day = Sinnoh.grab_user_time()
            
        route_pokemon = {
            "Gloom": (20, ["morning", "day", "night"]),
            "Weepinbell": (20, ["morning", "day", "night"]),
            "Floatzel": (13, ["morning", "day", "night"]),
            "Oddish": (11, ["morning", "day", "night"]),
            "Bellsprout": (11, ["morning", "day", "night"]),
            "Golduck": (10, ["morning", "day", "night"]),
            "Dustox": (10, ["morning", "day", "night"]),
            "Gastrodon": (5, ["morning", "day", "night"])
        }

        return Sinnoh.encounter_pokemon(route_pokemon)     