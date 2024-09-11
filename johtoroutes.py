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
                        "Rattata": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (85, ["night"]),
                        "Rattata": (15, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Pidgey": (50, ["morning", "day"]),
                        "Sentret": (40, ["morning", "day"]),
                        "Rattata": (5, ["morning", "day"]),
                        "Hoppip": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (55, ["night"]),
                        "Rattata": (45, ["night"])
                    }
            case _:
                print("Invalid version selected. Please try again.")

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)

    @staticmethod
    def route30():
        current_route = "Route 30"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning"]:
                    route_pokemon = {
                        "Caterpie": (50, ["morning"]),
                        "Pidgey": (40, ["morning"]),
                        "Metapod": (10, ["morning"])
                    }
                elif time_of_day in ["day"]:
                    route_pokemon = {
                        "Pidgey": (50, ["day"]),
                        "Caterpie": (35, ["day"]),
                        "Metapod": (15, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (40, ["night"]),
                        "Hoothoot": (30, ["night"]),
                        "Spinarak": (30, ["night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day in ["morning"]:
                    route_pokemon = {
                        "Weedle": (50, ["morning"]),
                        "Ledyba": (30, ["morning"]),
                        "Kakuna": (10, ["morning"]),
                        "Pidgey": (10, ["morning"])
                    }
                elif time_of_day in ["day"]:
                    route_pokemon = {
                        "Pidgey": (50, ["day"]),
                        "Weedle": (35, ["day"]),
                        "Kakuna": (15, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hooothoot": (60, ["night"]),
                        "Rattata": (40, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning"]:
                    route_pokemon = {
                        "Caterpie": (50, ["morning"]),
                        "Ledyba": (30, ["morning"]),
                        "Pidgey": (10, ["morning"]),
                        "Weedle": (5, ["morning"]),
                        "Hoppip": (5, ["morning"])
                    }
                elif time_of_day in ["day"]:
                    route_pokemon = {
                        "Caterpie": (50, ["day"]),
                        "Pidgey": (40, ["day"]),
                        "Weedle": (5, ["day"]),
                        "Hoppip": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (45, ["night"]),
                        "Spinarak": (30, ["night"]),
                        "Poliwag": (20, ["night"]),
                        "Zubat": (5, ["night"])
                    }
            case _:
                print("Invalid version selected. Please try again.")

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
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