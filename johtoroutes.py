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
        current_route = "Route 31"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Caterpie": (35, ["morning", "day"]),
                        "Pidgey": (30, ["morning", "day"]),
                        "Bellsprout": (20, ["morning", "day"]),
                        "Metapod": (15, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (40, ["night"]),
                        "Spinarak": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Hoothoot": (10, ["night"])
                    }
            case "soulsilver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Weedle": (30, ["morning"]),
                        "Ledyba": (30, ["morning"]),
                        "Bellsprout": (20, ["morning"]),
                        "Kakuna": (10, ["morning"]),
                        "Pidgey": (10, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Weedle": (35, ["day"]),
                        "Pidgey": (30, ["day"]),
                        "Bellsprout": (20, ["day"]),
                        "Kakuna": (15, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (40, ["night"]),
                        "Rattata": (40, ["night"]),
                        "Bellsprout": (20, ["night"]),
                    }
            case "crystal":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Ledyba": (30, ["morning"]),
                        "Caterpie": (30, ["morning"]),
                        "Bellsprout": (20, ["morning"]),
                        "Pidgey": (10, ["morning"]),
                        "Weedle": (5, ["morning"]),
                        "Hoppip": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Pidgey": (40, ["day"]),
                        "Caterpie": (30, ["day"]),
                        "Bellsprout": (20, ["day"]),
                        "Weedle": (5, ["day"]),
                        "Hoppip": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Spinarak": (30, ["night"]),
                        "Poliwag": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Hooothoot": (10, ["night"]),
                        "Zubat": (5, ["night"]),
                        "Gastly": (5, ["night"])
                    }
            case "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Weedle": (35, ["morning"]),
                        "Ledyba": (30, ["morning"]),
                        "Bellsprout": (20, ["morning"]),
                        "Pidgey": (15, ["morning"]),
                        "Kakuna": (10, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Weedle": (35, ["day"]),
                        "Pidgey": (30, ["day"]),
                        "Bellsprout": (20, ["day"]),
                        "Kakuna": (15, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (40, ["night"]),
                        "Rattata": (40, ["night"]),
                        "Bellsprout": (20, ["night"]),
                    }
            case _:
                print("Invalid version selected. Please try again.")

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route32():
        current_route = "Route 32"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Rattata": (35, ["morning"]),
                        "Bellsprout": (30, ["morning"]),
                        "Mareep": (20, ["morning"]),
                        "Hoppip": (10, ["morning"]),
                        "Zubat": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Rattata": (40, ["day"]),
                        "Bellsprout": (30, ["day"]),
                        "Mareep": (20, ["day"]),
                        "Hoppip": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (35, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Mareep": (10, ["night"]),
                        "Zubat": (5, ["night"])
                    }
            case "soulsilver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Ekans": (30, ["morning"]),
                        "Bellsprout": (30, ["morning"]),
                        "Mareep": (20, ["morning"]),
                        "Hoppip": (10, ["morning"]),
                        "Rattata": (5, ["morning"]),
                        "Zubat": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Ekans": (30, ["day"]),
                        "Bellsprout": (30, ["day"]),
                        "Mareep": (20, ["day"]),
                        "Hoppip": (10, ["day"]),
                        "Rattata": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (35, ["night"]),
                        "Ekans": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Mareep": (10, ["night"]),
                        "Zubat": (5, ["night"])
                    }
            case "gold":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Rattata": (35, ["morning"]),
                        "Bellsprout": (30, ["morning"]),
                        "Mareep": (20, ["morning"]),
                        "Hoppip": (10, ["morning"]),
                        "Wooper": (4, ["morning"]),
                        "Zubat": (1, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Rattata": (40, ["day"]),
                        "Bellsprout": (30, ["day"]),
                        "Mareep": (20, ["day"]),
                        "Hoppip": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (35, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Mareep": (10, ["night"]),
                        "Zubat": (5, ["night"])
                    }
            case "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Bellsprout": (30, ["morning"]),
                        "Ekans": (30, ["morning"]),
                        "Mareep": (20, ["morning"]),
                        "Hoppip": (10, ["morning"]),
                        "Rattata": (5, ["morning"]),
                        "Wooper": (4, ["morning"]),
                        "Zubat": (1, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Bellsprout": (30, ["day"]),
                        "Ekans": (30, ["day"]),
                        "Mareep": (20, ["day"]),
                        "Hoppip": (10, ["day"]),
                        "Rattata": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (35, ["night"]),
                        "Ekans": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Mareep": (10, ["night"]),
                        "Zubat": (5, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Ekans": (30, ["morning", "day"]),
                        "Bellsprout": (20, ["morning", "day"]),
                        "Hoppip": (15, ["morning", "day"]),
                        "Pidgey": (5, ["morning", "day"])  
                    }
                else: #night
                    route_pokemon = {
                        "Wooper": (30, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Zubat": (10, ["night"]),
                        "Hoothoot": (5, ["night"]),
                        "Gastly": (5, ["night"])
                    }
            case _:
                print("It should be impossibl to reach here.")

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route33():
        current_route = "Route 33"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Rattata": (40, ["morning"]),
                        "Hoppip": (35, ["morning"]),
                        "Spearow": (20, ["mornkng"]),
                        "Zubat": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Rattata": (45, ["day"]),
                        "Hoppip": (35, ["day"]),
                        "Spearow": (20, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (60, ["night"]),
                        "Zubat": (40, ["night"])
                    }
            case "soulsilver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Hoppip": (35, ["morning"]),
                        "Ekans": (30, ["morning"]),
                        "Spearow": (20, ["morning"]),
                        "Rattata": (10, ["morning"]),
                        "Zubat": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Hoppip": (35, ["day"]),
                        "Ekans": (30, ["day"]),
                        "Spearow": (20, ["day"]),
                        "Rattata": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (60, ["night"]),
                        "Zubat": (40, ["night"])
                    }
            case "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Hoppip": (35, ["morning"]),
                        "Ekans": (30, ["morning"]),
                        "Spearow": (20, ["morning"]),
                        "Rattata": (10, ["morning"]),
                        "Zubat": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Hoppip": (35, ["day"]),
                        "Ekans": (30, ["day"]),
                        "Spearow": (20, ["day"]),
                        "Rattata": (15, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Zubat": (40, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Ekans": (30, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Spearow": (30, ["morning", "day"]),
                        "Geodude": (20, ["morning", "day"]),
                        "Hoppip": (15, ["morning", "day"]),
                        "Ekans": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Zubat": (40, ["night"]),
                        "Rattata": (40, ["night"]),
                        "Geodude": (20, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
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