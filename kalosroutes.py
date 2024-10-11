from shared import get_version

class XY:

    @staticmethod
    def route1():
        pass
        #No pokemon on this route

    @staticmethod
    def route2():
        current_route = "Route 2"
        version = get_version()

        match version:
            case "x":
                route_pokemon = {
                    "Bunnelby": 20, "Fletchling": 20, "Scatterbug": 20,
                    "Zigzagoon": 15, "Pidgey": 14, "Weedle": 11
                }
            case "y":
                route_pokemon = {
                    "Bunnelby": 20, "Fletchling": 20, "Scatterbug": 20,
                    "Zigzagoon": 15, "Pidgey": 14, "Caterpie": 11
                }    
        from kalosmain import Kalos
        return Kalos.encounter_pokemon(route_pokemon)
    @staticmethod
    def route3():
        current_route = "Route 3"
        version = get_version()

        match version:
            case "x" | "y":
                route_pokemon = {
                    "Bidoof": 20, "Bunnelby": 20, "Fletchling": 20, "Pidgey": 10,
                    "Azurill": 10, "Burmy": 10, "Pikachu": 5, "Dunsparce": 5
                }

        from kalosmain import Kalos
        return Kalos.encounter_pokemon(route_pokemon)
    @staticmethod
    def route4():
        pass

    @staticmethod
    def route5():
        pass

    @staticmethod
    def route6():
        pass

    @staticmethod
    def route7():
        pass

    @staticmethod
    def route8():
        pass

    @staticmethod
    def route9():
        pass

    @staticmethod
    def route10():
        pass

    @staticmethod
    def route11():
        pass

    @staticmethod
    def route12():
        pass

    @staticmethod
    def route13():
        pass

    @staticmethod
    def route14():
        pass

    @staticmethod
    def route15():
        pass

    @staticmethod
    def route16():
        pass

    @staticmethod
    def route17():
        pass

    @staticmethod
    def route18():
        pass

    @staticmethod
    def route19():
        pass

    @staticmethod
    def route20():
        pass

    @staticmethod
    def route21():
        pass

    @staticmethod
    def route22():
        pass