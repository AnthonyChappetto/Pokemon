#Represents Sinnoh region and all its routes for diamond
class Diamond:
    @staticmethod
    def route201():
        from sinnohmain import Sinnoh
        """
        Simulates an encounter with a wild pokemon on Route 201 in the Sinnoh region.

        Returns:
            str: The name of the pokemon that was encountered, or "No Pokemon found" if none were found.
        """
        current_route = "Route 201"
        time_of_day = Sinnoh.grab_user_time()

        route_pokemon = {
            "Starly": (50, ["morning", "day", "night"]), #pokemon starly is the key paired with the values chance (50%) and time (morning, day, night)
            "Bidoof": (50, ["morning", "day", "night"]),
            }

        return Sinnoh.encounter_pokemon(route_pokemon) #returns the pokemon to put into the list
    
    @staticmethod
    def route202():
        return
    @staticmethod
    def route203():
        return
    @staticmethod
    def route204():
        return
    @staticmethod
    def route205():
        return
    @staticmethod
    def route206():
        return
    @staticmethod
    def route207():
        return
    @staticmethod
    def route208():
        return
    @staticmethod
    def route209():
        return
    @staticmethod
    def route210():
        return
    @staticmethod
    def route211():
        return
    @staticmethod
    def route212():
        return
    @staticmethod
    def route213():
        return
    @staticmethod
    def route214():
        return
    @staticmethod
    def route215():
        return
    @staticmethod
    def route216():
        return
    @staticmethod
    def route217():
        return
    @staticmethod
    def route218():
        return
    @staticmethod
    def route219():
        return
    @staticmethod
    def route220():
        return
    @staticmethod
    def route221():
        return
    @staticmethod
    def route222():
        return
    @staticmethod
    def route223():
        return
    @staticmethod
    def route224():
        return
    @staticmethod
    def route225():
        return
    @staticmethod
    def route226():
        return
    @staticmethod
    def route227():
        return
    @staticmethod
    def route228():
        return
    @staticmethod
    def route229():
        return
    @staticmethod
    def route230():
        return