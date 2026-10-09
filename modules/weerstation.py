def c_naar_f(celsius):
    """Converteert Celsius naar Fahrenheit."""
    return 32 + 1.8 * celsius


def gevoels_temp(celsius, wind, vocht):
    """Berekent de gevoelstemperatuur."""
    return celsius - (vocht / 100) * wind


def advies_bericht(gevoel, wind):
    """Bepaalt het advies op basis van gevoelstemperatuur en windsnelheid."""
    if gevoel < 0 and wind > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and wind <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and wind > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and wind <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def start_weerstation():
    """Interactieve invoer voor maximaal 7 dagen met robuuste invoercontrole."""
    print("\n--- WEERSTATION HANDMATIGE INVOER ---")
    totaal_temp = 0.0
    dagen = 0

    for dag in range(1, 8):
        # 1. TEMPERATUUR INVOER
        invoer_temp = input(f"Dag {dag} - Temperatuur [°C] (Enter om te stoppen): ").strip()
        if invoer_temp == "":
            print("Invoer gestopt.")
            break

        try:
            temp = float(invoer_temp)
        except ValueError:
            print("[FOUT] Ongeldige invoer! Voer een getal in.")
            break

        # 2. WINDSNELHEID INVOER
        try:
            wind = float(input(f"Dag {dag} - Windsnelheid [m/s]: "))
        except ValueError:
            print("[FOUT] Ongeldige windsnelheid ingevoerd. Invoer afgebroken.")
            break

        # 3. LUCHTVOCHTIGHEID INVOER
        try:
            vocht = float(input(f"Dag {dag} - Luchtvochtigheid [%]: "))
        except ValueError:
            print("[FOUT] Ongeldige luchtvochtigheid ingevoerd. Invoer afgebroken.")
            break

        # Berekeningen & Uitvoer
        f_temp = c_naar_f(temp)
        gevoel = gevoels_temp(temp, wind, vocht)
        advies = advies_bericht(gevoel, wind)

        totaal_temp += temp
        dagen += 1
        gemiddelde = totaal_temp / dagen

        print(f"\nResultaat dag {dag}:")
        print(f"Temperatuur: {temp:.1f}°C ({f_temp:.1f}°F)")
        print(f"Advies     : {advies}")
        print(f"Gemiddelde : {gemiddelde:.1f}°C")
        print("======================================\n")