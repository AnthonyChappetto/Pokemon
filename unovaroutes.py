from shared import get_version, grab_users_month

class Black:

    @staticmethod
    def route1():
        current_route = "Route 1"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Patrat": 50, "Lillipup": 50
                }
            case "black2" | "white2":
                route_pokemon = {
                    "Herdier": 50, "Watchog": 40, "Jigglypuff": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route2():
        current_route = "Route 2"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Patrat": 40, "Lillipup": 40, "Purrloin": 20
                }
            case "black2" | "white2":
                route_pokemon = {
                    "Watchog": 30, "Herdier": 30, "Liepard": 20,
                    "Jigglypuff": 10, "Lickitung": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route3():
        current_route = "Route 3"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Pidove": 40, "Patrat": 20, "Blitzle": 20,
                    "Lillipup": 10, "Purrloin": 10
                }
            case "black2" | "white2":
                route_pokemon = {
                    "Tranquill": 30, "Watchog": 20, "Zebstrika": 20,
                    "Yanma": 10, "Herdier": 10, "Purrloin": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    
    @staticmethod
    def route4():
        current_route = "Route 4"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Sandile": 40, "Darumaka": 40, "Scraggy": 20
                }
            case "black2":
                route_pokemon = {
                    "Sandile": 35, "Darumaka": 35, "Trubbish": 25, "Scraggy": 5     
                }
            case "white2":
                route_pokemon = {
                    "Sandile": 35, "Darumaka": 35, "Minccino": 25, "Scraggy": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route5():
        current_route = "Route 5"
        version = get_version()

        match version:
            case "black" | "black2":
                route_pokemon = {
                    "Gothita": 30, "Minccino": 30, "Trubbish": 20, "Liepard": 20
                }
            case "white" | "white2":
                route_pokemon = {
                    "Solosis": 30, "Minccino": 30, "Trubbish": 20, "Liepard": 20
                }
            case _:
                print("Should be impossible to reach here.")
                
        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route6():
        current_route = "Route 6"
        version = get_version()
        season = grab_users_month()

        if season in ["spring", "summer", "fall"]:
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Deerling": 35, "Karrablast": 25, "Tranquill": 15,
                        "Foongus": 15, "Swadloon": 10
                    }
                case "black2":
                    route_pokemon = {
                        "Deerling": 30, "Shelmet": 25, "Tranquill": 15,
                        "Foongus": 10, "Swadloon": 10, "Marill": 5, "Karrablast": 5
                    }
                case "white2":
                    route_pokemon = {
                        "Deerling": 30, "Karrablast": 25, "Tranquill": 15,
                        "Foongus": 10, "Swadloon": 10, "Marill": 5, "Shelmet": 5
                    }
        else: #Winter
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Deeling": 35, "Karrablast": 25, "Vanillite": 15,
                        "Foongus": 15, "Swadloon": 10
                    }
                case "black2":
                    route_pokemon = {
                        "Deering": 30, "Shelmet": 25, "Tranquill": 15,
                        "Foongus": 10, "Swadloon": 10, "Marill": 5, "Karrablast": 5
                    }
                case "white2":
                    route_pokemon = {
                        "Deering": 30, "Shelmet": 25, "Tranquill": 15,
                        "Foongus": 10, "Swadloon": 10, "Marill": 5, "Karrablast": 5
                    }

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)    
    @staticmethod
    def route7():
        current_route = "Route 7"
        version = get_version()
        season = grab_users_month()

        if season in ["spring", "summer", "fall"]:
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Tranquill": 30, "Deerling": 20, "Watchog": 20,
                        "Zebstrika": 20, "Foongus": 10
                    }
                case "black2" | "white2":
                    route_pokemon = {
                        "Tranquill": 30, "Deerling": 20, "Zebstrika": 20,
                        "Watchog": 15, "Zangoose": 5, "Seviper": 5,
                        "Foongus": 5
                    }
        else: #Winter 
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Cubchoo": 30, "Deerling": 20, "Watchog": 20,
                        "Zebstrika": 20, "Foongus": 10
                    }
                case "black2" | "white2":
                    route_pokemon = {
                        "Cubchoo": 25, "Deerling": 20, "Zebstrika": 20,
                        "Watchog": 10, "Tranquill": 10, "Zangoose": 5, 
                        "Seviper": 5, "Foongus": 5
                    }
                    
        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route8():
        return
    
    @staticmethod
    def route9():
        return
    
    @staticmethod
    def route10():
        return
    
    @staticmethod
    def route11():
        return
    
    @staticmethod
    def route12():
        return
    
    @staticmethod
    def route13():
        return
    
    @staticmethod
    def route14():
        return
    
    @staticmethod
    def route15():
        return
    
    @staticmethod
    def route16():
        return
    
    @staticmethod
    def route17():
        return
    
    @staticmethod
    def route18():
        return
    
    @staticmethod
    def route19():
        return

    @staticmethod
    def route20():
        return

    @staticmethod
    def route21():
        return

    @staticmethod
    def route22():
        return

    @staticmethod
    def route23():
        return