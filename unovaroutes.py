from shared import get_version

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
        return
    
    @staticmethod
    def route5():
        return
    
    @staticmethod
    def route6():
        return
    
    @staticmethod
    def route7():
        return
    
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