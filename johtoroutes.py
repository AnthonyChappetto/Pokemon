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
        current_route = "Route 34"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Drowzee": (50, ["morning", "day", "night"]),
                        "Rattata": (35, ["morning", "day", "night"]),
                        "Abra": (10, ["morning", "day", "night"]),
                        "Ditto": (5, ["morning", "day", "night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Snubbull": (30, ["morning", "day"]),
                        "Rattata": (30, ["morning", "day"]),
                        "Pidgey": (20, ["morning", "day"]),
                        "Abra": (10, ["morning", "day"]),
                        "Jigglypuff": (5, ["morning", "day"]),
                        "Ditto": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Drowzee": (30, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Hoothoot": (20, ["night"]),
                        "Abra": (10, ["night"]),
                        "Jigglypuff": (5, ["night"]),
                        "Ditto": (5, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)

    @staticmethod
    def route35():
        current_route = "Route 35"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Nidoran_F": (30, ["morning", "day"]),
                        "Nidoran_M": (30, ["morning", "day"]),
                        "Drowzee": (20, ["morning", "day"]),
                        "Abra": (10, ["morning", "day"]),
                        "Pidgey": (5, ["morning", "day"]),
                        "Ditto": (4, ["morning", "day"]),
                        "Yanma": (1, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Nidoran_F": (30, ["night"]),
                        "Nidoran_M": (30, ["night"]),
                        "Drowzee": (20, ["night"]),
                        "Abra": (10, ["night"]),
                        "Hoothoot": (5, ["night"]),
                        "Ditto": (4, ["night"]),
                        "Yanma": (1, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Pidgey": (30, ["morning", "day"]),
                        "Snubbull": (30, ["morning", "day"]),
                        "Growlithe": (20, ["morning", "day"]),
                        "Abra": (10, ["morning", "day"]),
                        "Jigglypuff": (5, ["morning", "day"]),
                        "Ditto": (4, ["morning", "day"]),
                        "Yanma": (1, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Drowzee": (30, ["night"]),
                        "Hoothoot": (30, ["night"]),
                        "Psyduck": (20, ["night"]),
                        "Abra": (10, ["night"]),
                        "Jigglypuff": (5, ["night"]),
                        "Ditto": (4, ["night"]),
                        "Yanma": (1, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route36():
        current_route = "Route 36"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Nidoran_F": (30, ["morning", "day"]),
                        "Nidoran_M": (30, ["morning", "day"]),
                        "Pidgey": (25, ["morning", "day"]),
                        "Growlithe": (10, ["morning", "day"]),
                        "Stantler": (5, ["morning", "day"]),
                    }
                else: #night
                    route_pokemon = {
                        "Nidoran_F": (30, ["night"]),
                        "Nidoran_M": (30, ["night"]),
                        "Hoothoot": (25, ["night"]),
                        "Growlithe": (10, ["night"]),
                        "Stantler": (5, ["night"])
                    }
            case "soulsilver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Nidoran_F": (30, ["morning", "day"]),
                        "Nidoran_M": (30, ["morning", "day"]),
                        "Pidgey": (25, ["morning", "day"]),
                        "Vulpix": (10, ["morning", "day"]),
                        "Stantler": (5, ["morning", "day"]),
                    }
                else: #night
                    route_pokemon = {
                        "Nidoran_F": (30, ["night"]),
                        "Nidoran_M": (30, ["night"]),
                        "Hoothoot": (25, ["night"]),
                        "Vulpix": (10, ["night"]),
                        "Stantler": (5, ["night"])
                    }
            case "gold":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Nidoran_F": (30, ["morning"]),
                        "Nidoran_M": (30, ["morning"]),
                        "Pidgey": (25, ["morning"]),
                        "Growlithe": (10, ["morning"]),
                        "Stantler": (5, ["morning"]),
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Nidoran_F": (30, ["day"]),
                        "Nidoran_M": (30, ["day"]),
                        "Pidgey": (20, ["day"]),
                        "Growlithe": (15, ["day"]),
                        "Stantler": (5, ["day"]),
                    }
                else: #night
                    route_pokemon = {
                        "Nidoran_F": (30, ["night"]),
                        "Nidoran_M": (30, ["night"]),
                        "Hoothoot": (25, ["night"]),
                        "Growlithe": (10, ["night"])
                    }
            case "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Nidoran_F": (30, ["morning"]),
                        "Nidoran_M": (30, ["morning"]),
                        "Pidgey": (25, ["morning"]),
                        "Vulpix": (10, ["morning"]),
                        "Stantler": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Nidoran_F": (30, ["day"]),
                        "Nidoran_M": (30, ["day"]),
                        "Pidgey": (20, ["day"]),
                        "Vulpix": (15, ["day"]),
                        "Stantler": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Nidoran_F": (30, ["night"]),
                        "Nidoran_M": (30, ["night"]),
                        "Hoothoot": (25, ["night"]),
                        "Vulpix": (10, ["night"]),
                        "Stantler": (5, ["night"])
                    }
            case "crystal":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Pidgey": (40, ["morning"]),
                        "Ledyba": (30, ["morning"]),
                        "Bellsprout": (20, ["morning"]),
                        "Growlithe": (10, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Pidgey": (70, ["day"]),
                        "Bellsprout": (20, ["day"]),
                        "Growlithe": (10, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (45, ["night"]),
                        "Spinarak": (30, ["night"]),
                        "Bellsprout": (20, ["night"]),
                        "Gastly": (5, ["night"])
                    }
        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route37():
        current_route = "Route 37"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Pidgey": (60, ["morning"]),
                        "Stantler": (30, ["morning"]),
                        "Growlithe": (10, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Pidgey": (50, ["day"]),
                        "Stantler": (30, ["day"]),
                        "Growlithe": (15, ["day"]),
                        "Pidgeotto": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Spinarak": (40, ["night"]),
                        "Stantler": (30, ["night"]),
                        "Hoothoot": (20, ["night"]),
                        "Growlithe": (10, ["night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Ledyba": (40, ["morning"]),
                        "Stantler": (30, ["morning"]),
                        "Pidgey": (20, ["morning"]),
                        "Vulpix": (10, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Pidgey": (50, ["day"]),
                        "Stantler": (30, ["day"]),
                        "Vulpix": (15, ["day"]),
                        "Pidgeotto": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Hoothoot": (60, ["night"]),
                        "Stantler": (30, ["night"]),
                        "Vulpix": (10, ["night"])
                    }
            case "crystal":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Ledyba": (30, ["morning"]),
                        "Pidgey": (20, ["morning"]),
                        "Growlithe": (10, ["morning"]),
                        "Pidgeotto": (5, ["morning"]),
                        "Ledian": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Pidgey": (55, ["day"]),
                        "Growlithe": (40, ["day"]),
                        "Pidgeotto": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Stantler": (40, ["night"]),
                        "Spinarak": (30, ["night"]),
                        "Hoothoot": (20, ["night"]),
                        "Noctowl": (5, ["night"]),
                        "Ariados": (5, ["night"])
                    }
        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route38():
        current_route = "Route 38"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Raticate": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Farfetch'd": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (4, ["morning", "day"]),
                        "Snubull": (1, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Miltank": (5, ["night"]),
                        "Tauros": (4, ["night"]),
                        "Snubull": (1, ["night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Raticate": (30, ["morning", "day"]),
                        "Meowth": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Farfetch'd": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (4, ["morning", "day"]),
                        "Snubull": (1, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Meowth": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Miltank": (5, ["night"]),
                        "Tauros": (4, ["night"]),
                        "Snubull": (1, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Raticate": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Pidgeotto": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Meowth": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Noctowl": (10, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)

    @staticmethod
    def route39():
        current_route = "Route 39"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Raticate": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Farfetch'd": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Miltank": (5, ["night"]),
                        "Tauros": (5, ["night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Raticate": (30, ["morning", "day"]),
                        "Meowth": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Farfetch'd": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Meowth": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Miltank": (5, ["night"]),
                        "Tauros": (5, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Rattata": (30, ["morning", "day"]),
                        "Raticate": (30, ["morning", "day"]),
                        "Magnemite": (20, ["morning", "day"]),
                        "Pidgeotto": (10, ["morning", "day"]),
                        "Miltank": (5, ["morning", "day"]),
                        "Tauros": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Meowth": (40, ["night"]),
                        "Raticate": (30, ["night"]),
                        "Magnemite": (20, ["night"]),
                        "Noctowl": (10, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route40():
        current_route = "Route 40"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver" | "crystal":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Tentacool": (90, ["morning", "day", "night"]),
                        "Tentacruel": (10, ["morning", "day", "night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route41():
        current_route = "Route 41"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold" | "crystal":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Tentacool": (60, ["morning", "day", "night"]),
                        "Tentacruel": (30, ["morning", "day", "night"]),
                        "Mantine": (10, ["morning", "day", "night"])
                    }
            case "soulsilver":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Tentacool": (60, ["morning", "day", "night"]),
                        "Tentacruel": (40, ["morning", "day", "night"])
                    }
            case "silver":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Tentacool": (70, ["morning", "day", "night"]),
                        "Tentacruel": (30, ["morning", "day", "night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route42():
        current_route = "Route 42"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Spearow": (30, ["morning", "day"]),
                        "Mankey": (30, ["morning", "day"]),
                        "Mareep": (30, ["morning", "day"]),
                        "Flaaffy": (10, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Zubat": (30, ["night"]),
                        "Mankey": (30, ["night"]),
                        "Mareep": (30, ["night"]),
                        "Flaaffy": (10, ["night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Mareep": (50, ["morning", "day"]),
                        "Spearow": (40, ["morning", "day"]),
                        "Flaaffy": (10, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Mareep": (50, ["night"]),
                        "Zubat": (40, ["night"]),
                        "Flaaffy": (10, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Spearow": (30, ["morning", "day"]),
                        "Ekans": (30, ["morning", "day"]),
                        "Rattata": (20, ["morning", "day"]),
                        "Raticate": (10, ["morning", "day"]),
                        "Arbok": (5, ["morning", "day"]),
                        "Fearow": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Zubat": (30, ["night"]),
                        "Rattata": (30, ["night"]),
                        "Raticate": (20, ["night"]),
                        "Golbat": (15, ["night"]),
                        "Marill": (5, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route43():
        current_route = "Route 43"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Flaaffy": (30, ["morning"]),
                        "Girafarig": (30, ["morning"]),
                        "Pidgeotto": (25, ["morning"]),
                        "Mareep": (10, ["morning"]),
                        "Venonat": (5, ["morning"])
                    }
                if time_of_day == "day":
                    route_pokemon = {
                        "Flaaffy": (40, ["day"]),
                        "Girafarig": (30, ["day"]),
                        "Pidgeotto": (20, ["day"]),
                        "Mareep": (10, ["day"])
                    }
                if time_of_day == "night":
                    route_pokemon = {
                        "Flaaffy": (30, ["night"]),
                        "Girafarig": (30, ["night"]),
                        "Noctowl": (20, ["night"]),
                        "Venonat": (15, ["night"]),
                        "Mareep": (5, ["night"])
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Pidgeotto": (30, ["morning", "day"]),
                        "Sentret": (30, ["morning", "day"]),
                        "Farfetch'd": (20, ["morning", "day"]),
                        "Furret": (15, ["morning", "day"]),
                        "Raticate": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Venonat": (40, ["night"]),
                        "Noctowl": (30, ["night"]),
                        "Raticate": (25, ["night"]),
                        "Venomoth": (5, ["night"])
                    }
        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route44():
        current_route = "Route 44"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver" | "gold" | "silver":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Weepinbell": (35, ["morning", "day", "night"]),
                        "Tangela": (30, ["morning", "day", "night"]),
                        "Bellspout": (20, ["morning", "day", "night"]),
                        "Lickitung": (15, ["morning", "day", "night"]),
                    }
            case "crystal":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Lickitung": (40, ["morning", "day"]),
                        "Tangela": (30, ["morning", "day"]),
                        "Bellspout": (20, ["morning", "day"]),
                        "Weepinbell": (10, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Tangela": (30, ["night"]),
                        "Poliwag": (30, ["night"]),
                        "Bellspout": (20, ["night"]),
                        "Weepinbell": (10, ["night"]),
                        "Poliwhirl": (10, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route45():
        current_route = "Route 45"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "gold":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Graveler": (40, ["morning", "day", "night"]),
                        "Geodude": (30, ["morning", "day", "night"]),
                        "Gligar": (20, ["morning", "day", "night"]),
                        "Phanpy": (10, ["morning", "day", "night"])
                    }
            case "soulsilver" | "silver":
                if time_of_day in ["morning", "day", "night"]:
                    route_pokemon = {
                        "Graveler": (55, ["morning", "day", "night"]),
                        "Geodude": (30, ["morning", "day", "night"]),
                        "Teddiursa": (10, ["morning", "day", "night"]),
                        "Skarmory": (5, ["morning", "day", "night"])
                    }
            case "crystal":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Geodude": (30, ["morning"]),
                        "Graveler": (30, ["morning"]),
                        "Gligar": (20, ["morning"]),
                        "Donphan": (10, ["morning"]),
                        "Phanpy": (5, ["morning"]),
                        "Skarmory": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Geodude": (30, ["day"]),
                        "Graveler": (30, ["day"]),
                        "Gligar": (20, ["day"]),
                        "Donphan": (15, ["day"]),
                        "Skarmory": (5, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Graveler": (50, ["night"]),
                        "Geodude": (30, ["night"]),
                        "Gligar": (20, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route46():
        current_route = "Route 46"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Geodude": (40, ["morning", "day"]),
                        "Spearow": (35, ["morning", "day"]),
                        "Rattata": (25, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (55, ["night"]),
                        "Geodude": (45, ["night"])
                    }
            case "gold" | "silver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Geodude": (40, ["morning", "day"]),
                        "Spearow": (35, ["morning", "day"]),
                        "Rattata": (20, ["morning", "day"]),
                        "Jigglypuff": (5, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Rattata": (50, ["night"]),
                        "Geodude": (45, ["night"]),
                        "Jigglypuff": (5, ["night"])
                    }
            case "crystal":
                if time_of_day == "morning":
                    route_pokemon = {
                        "Geodude": (50, ["morning"]),
                        "Spearow": (30, ["morning"]),
                        "Rattata": (15, ["morning"]),
                        "Phanpy": (5, ["morning"])
                    }
                elif time_of_day == "day":
                    route_pokemon = {
                        "Geodude": (50, ["day"]),
                        "Spearow": (30, ["day"]),
                        "Rattata": (20, ["day"])
                    }
                else: #night
                    route_pokemon = {
                        "Geodude": (50, ["night"]),
                        "Rattata": (50, ["night"])
                    }
        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route47():
        current_route = "Route 47"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold" | "soulsilver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Ditto": (41, ["morning", "day"]),
                        "Farfetch'd": (20, ["morning", "day"]),
                        "Miltank": (20, ["morning", "day"]),
                        "Raticate": (5, ["morning", "day"]),
                        "Spearow": (5, ["morning", "day"]),
                        "Gloom": (5, ["morning", "day"]),
                        "Fearow": (4, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Ditto": (41, ["night"]),
                        "Noctowl": (20, ["night"]),
                        "Miltank": (20, ["night"]),
                        "Raticate": (5, ["night"]),
                        "Spearow": (5, ["night"]),
                        "Gloom": (5, ["night"]),
                        "Fearow": (4, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)
    @staticmethod
    def route48():
        current_route = "Route 48"
        version = get_version()
        time_of_day = grab_user_time()

        match version:
            case "heartgold":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Tauros": (21, ["morning", "day"]),
                        "Gloom": (20, ["morning", "day"]),
                        "Farfetch'd": (20, ["morning", "day"]),
                        "Hoppip": (11, ["morning", "day"]),
                        "Fearow": (10, ["morning", "day"]),
                        "Growlithe": (9, ["morning", "day"]),
                        "Girafarig": (5, ["morning", "day"]),
                        "Diglett": (4, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Growlithe": (29, ["night"]),
                        "Tauros": (21, ["night"]),
                        "Gloom": (20, ["night"]),
                        "Hoppip": (11, ["night"]),
                        "Fearow": (10, ["night"]),
                        "Girafarig": (5, ["night"]),
                        "Diglett": (4, ["night"])
                    }
            case "soulsilver":
                if time_of_day in ["morning", "day"]:
                    route_pokemon = {
                        "Tauros": (21, ["morning", "day"]),
                        "Gloom": (20, ["morning", "day"]),
                        "Farfetch'd": (20, ["morning", "day"]),
                        "Hoppip": (11, ["morning", "day"]),
                        "Fearow": (10, ["morning", "day"]),
                        "Vulpix": (9, ["morning", "day"]),
                        "Girafarig": (5, ["morning", "day"]),
                        "Diglett": (4, ["morning", "day"])
                    }
                else: #night
                    route_pokemon = {
                        "Vulpix": (29, ["night"]),
                        "Tauros": (21, ["night"]),
                        "Gloom": (20, ["night"]),
                        "Hoppip": (11, ["night"]),
                        "Fearow": (10, ["night"]),
                        "Girafarig": (5, ["night"]),
                        "Diglett": (4, ["night"])
                    }

        from johtomain import Johto
        return Johto.encounter_pokemon(route_pokemon)