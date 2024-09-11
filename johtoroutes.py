from shared import get_version, grab_user_time

class GoldSilver:

    @staticmethod
    def route29():
        current_route = "Route 29"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Pidgey": (55, ["morning", "day"]),
                        "Sentret": (40, ["morning", "day"]),
                        "Rattata": (5, ["morning", "day"]),
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (85, ["night"]),
                        "Rattata": (15, ["night"]),
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Pidgey": (50, ["morning", "day"]),
                        "Sentret": (40, ["morning", "day"]),
                        "Rattata": (5, ["morning", "day"]),
                        "Hoppip": (5, ["morning", "day"]),
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (55, ["night"]),
                        "Rattata": (45, ["night"]),
                    }
            case _:
                print("Invalid version selected. Please try again.")

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)

    @staticmethod
    def route30():
        return
    @staticmethod
    def route31():
        return
    @staticmethod
    def route32():
        return
    @staticmethod
    def route33():
        return
    @staticmethod
    def route34():
        return
    @staticmethod
    def route35():
        return
    @staticmethod
    def route36():
        return
    @staticmethod
    def route37():
        return
    @staticmethod
    def route38():
        return
    @staticmethod
    def route39():
        return
    @staticmethod
    def route40():
        return
    @staticmethod
    def route41():
        return
    @staticmethod
    def route42():
        return
    @staticmethod
    def route43():
        return
    @staticmethod
    def route44():
        return
    @staticmethod
    def route45():
        return
    @staticmethod
    def route46():
        return
    @staticmethod
    def route47():
        return
    @staticmethod
    def route48():
        return