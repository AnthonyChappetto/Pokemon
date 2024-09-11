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
                case _:
                    print("Should be impossible to reach here.")
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
                case _:
                    print("Should be impossible to reach here.")

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
                case _:
                    print("Should be impossible to reach here.")
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
                case _:
                    print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route8():
        current_route = "Route 8"
        version = get_version()
        season = grab_users_month()

        if season in ["spring", "summer", "fall"]:
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Palpitoad": 40, "Shelmet": 40, "Stunfisk": 20
                    }
                case "black2":
                    route_pokemon = {
                        "Palpitoad": 40, "Shelmet": 20, "Stunfisk": 20,
                        "Croagunk": 15, "Karrablast": 5
                    }
                case "white2":
                    route_pokemon = {
                        "Palpitoad": 40, "Karrablast": 20, "Stunfisk": 20,
                        "Croagunk": 15, "Shelmet": 5
                    }
                case _:
                    print("Should be impossible to reach here.")
        else:
            match version:
                case "black" | "white":
                    route_pokemon = {
                        "Stunfisk": 70, "Palpitoad": 30
                    }
                case "black2" | "white2":
                    route_pokemon = {
                        "Stunfisk": 65, "Palpitoad": 30, "Seismitoad": 5,
                    }
                case _:
                    print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route9():
        current_route = "Route 9"
        version = get_version()

        match version:
            case "black":
                route_pokemon = {
                    "Gothorita": 30, "Minccino": 20, "Garbodor": 20,
                    "Pawniard": 20, "Liepard": 10
                }
            case "white":
                route_pokemon = {
                    "Duosion": 30, "Minccino": 20, "Garbodor": 20,
                    "Pawniard": 20, "Liepard": 10
                }
            case "black2":
                route_pokemon = {
                    "Minccino": 30, "Gothorita": 25, "Garbodor": 15,
                    "Pawniard": 15, "Liepard": 10, "Muk": 5
                }
            case "white2":
                route_pokemon = {
                    "Minccino": 30, "Duosion": 25, "Garbodor": 15,
                    "Pawniard": 15, "Liepard": 10, "Muk": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)

    @staticmethod
    def route10():
        current_route = "Route 10"
        version = get_version()

        match version:
            case "black":
                route_pokemon = {
                    "Herdier": 30, "Vullaby": 30, "Bouffalant": 20, 
                    "Foongus": 10, "Sawk": 10
                }
            case "white":
                route_pokemon = {
                    "Herdier": 30, "Rufflet": 30, "Bouffalant": 20, 
                    "Foongus": 10, "Sawk": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    
    @staticmethod
    def route11():
        current_route = "Route 11"
        version = get_version()

        match version:
            case "black":
                route_pokemon = {
                    "Vullaby": 25, "Golduck": 20, "Gligar": 15,
                    "Amoonguss": 10, "Zangoose": 10, "Seviper": 10,
                    "Karrablast": 5, "Pawniard": 5
                }
            case "white":
                route_pokemon = {
                    "Rufflet": 25, "Golduck": 20, "Gligar": 15,
                    "Amoonguss": 10, "Zangoose": 10, "Seviper": 10,
                    "Karrablast": 5, "Pawniard": 5
                }
            case "black2":
                route_pokemon = {
                    "Shelmet": 25, "Golduck": 20, "Gligar": 15,
                    "Marill": 10, "Zangoose": 10, "Seviper": 10,
                    "Amoonguss": 5, "Karrablast": 5
                }
            case "white2":
                route_pokemon = {
                    "Karrablast": 25, "Golduck": 20, "Gligar": 15,
                    "Marill": 10, "Zangoose": 10, "Seviper": 10,
                    "Amoonguss": 5, "Shelmet": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    
    @staticmethod
    def route12():
        current_route = "Route 12"
        version = get_version()

        match version:
            case "black": 
                route_pokemon = {
                    "Combee": 20, "Sunkern": 20, "Tranquill": 15,
                    "Kakuna": 10, "Rapidash": 10, "Cherrim": 10,
                    "Heracross": 5, "Pinsir": 5, "Dunsparce": 5
                } 
            case "white":
                route_pokemon = {
                    "Combee": 20, "Sunkern": 20, "Tranquill": 15,
                    "Metapod": 10, "Rapidash": 10, "Cherrim": 10,
                    "Heracross": 5, "Pinsir": 5, "Dunsparce": 5
                }
            case "black2":
                route_pokemon = {
                    "Roselia": 25, "Tranquill": 25, "Combee": 20,
                    "Sewaddle": 15, "Herracross": 15
                }
            case "white2":
                route_pokemon = {
                    "Roselia": 25, "Tranquill": 25, "Combee": 20,
                    "Sewaddle": 15, "Pinsir": 15
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route13():
        current_route = "Route 13"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Tangela": 25, "Swellow": 20, "Golbat": 15,
                    "Lunatone": 10, "Solrock": 10, "Drifblim": 10,
                    "Absol": 10
                }
            case "black2" | "white2":
                route_pokemon = {
                    "Tangela": 25, "Pelipper": 25, "Drifblim": 15,
                    "Absol": 15, "Lunatone": 10, "Solrock": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route14():
        current_route = "Route 14"
        version = get_version()

        match version:
            case "black" | "white":
                route_pokemon = {
                    "Golduck": 20, "Jigglypuff": 20, "Tropius": 15,
                    "Mienfoo": 10, "Altaria": 10, "Drifblim": 10,
                    "Beheeyem": 10, "Shuckle": 5
                }
            case "black2" | "white2":
                route_pokemon = {
                    "Golduck:": 25, "Swablu": 20, "Mienfoo": 20,
                    "Drifblim": 15, "Absol": 15, "Altaria": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route15():
        current_route = "Route 15"
        version = get_version()

        match version:
            case "black":
                route_pokemon = {
                    "Fearow": 30, "Marowak": 20, "Gligar": 15,
                    "Sawk": 15, "Kangaskhan": 10, "Pupitar": 10
                }
            case "white":
                route_pokemon = {
                    "Fearow": 30, "Marowak": 20, "Gligar": 15,
                    "Throh": 15, "Kangaskhan": 10, "Pupitar": 10
                }
            case "black2":
                route_pokemon = {
                    "Sandslash": 30, "Gligar": 25, "Sawk": 20,
                    "Pupitar": 15, "Scrafty": 10
                }
            case "white2":
                route_pokemon = {
                    "Sandslash": 30, "Gligar": 25, "Throh": 20,
                    "Pupitar": 15, "Scrafty": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route16():
        current_route = "Route 16"
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
    def route17():
        current_route = "Route 17"
        version = get_version()

        match version:
            case "black" | "black2" | "white" | "white2":
                route_pokemon = {
                    "Frillish": 100
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route18():
        current_route = "Route 18"
        version = get_version()

        match version:
            case "black":
                route_pokemon = {
                    "Scraggy": 40, "Dwebble": 30, "Watchog": 20, "Sawk": 10
                }
            case "white":
                route_pokemon = {
                    "Scraggy": 40, "Dwebble": 30, "Watchog": 20, "Throh": 10
                }
            case "black2":
                route_pokemon = {
                    "Scrafty": 30, "Crustle": 20, "Sawk": 20, "Watchog": 10,
                    "Tropius": 10, "Carnivine": 10
                }
            case "white2":
                route_pokemon = {
                    "Scrafty": 30, "Crustle": 20, "Throh": 20, "Watchog": 10,
                    "Tropius": 10, "Carnivine": 10
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route19():
        current_route = "Route 19"
        version = get_version()

        match version:
            case "black2" | "white2":
                route_pokemon = {
                    "Patrat": 50, "Purrloin": 50
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route20():
        current_route = "Route 20"
        version = get_version()
        season = grab_users_month()

        if season in ["spring", "winter", "fall"]:
            match version:
                case "black2" | "white2":
                    route_pokemon = {
                        "Sewaddle": 35, "Pidove": 25, "Patrat": 20,
                        "Purrloin": 15, "Sunkern": 5
                    }
                case _:
                    print("Should be impossible to reach here.")
        else: # summer
            match version:
                case "black2" | "white2":
                    route_pokemon = {
                        "Sewaddle": 35, "Sunkern": 26, "Patrat": 20,
                        "Purrloin": 14, "Pidove": 5
                    }
                case _:
                    print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route21():
        current_route = "Route 19"
        version = get_version()

        match version:
            case "black2" | "white2":
                route_pokemon = {
                    "Frillish": 70, "Mantyke": 30, "Remoraid": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route22():
        current_route = "Route 22"
        version = get_version()

        match version:
            case "black2" | "white2":
                route_pokemon = {
                    "Mienfoo": 25, "Amoonguss": 20, "Pelipper": 10,
                    "Golduck": 10, "Lunatone": 10, "Solrock": 10,
                    "Marill": 10, "Delibird": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)
    @staticmethod
    def route23():
        current_route = "Route 23"
        version = get_version()

        match version:
            case "black2":
                route_pokemon = {
                    "Bouffalant": 25, "Sawk": 25, "Mienfoo": 15, "Gligar": 10,
                    "Amoonguss": 10, "Golduck": 10, "Vullaby": 5
                }
            case "white2":
                route_pokemon = {
                    "Bouffalant": 25, "Throh": 25, "Mienfoo": 15, "Gligar": 10,
                    "Amoonguss": 10, "Golduck": 10, "Vullaby": 5
                }
            case _:
                print("Should be impossible to reach here.")

        from unovamain import Unova
        return Unova.encounter_pokemon(route_pokemon)