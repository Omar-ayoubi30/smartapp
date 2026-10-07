# 1. Functie voor het omrekenen van Celsius naar Fahrenheit
def fahrenheit(temp_celsius):
    f = 32 + 1.8 * temp_celsius
    return f


# 2. Functie voor het berekenen van de gevoelstemperatuur
def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel_temp = temp_celsius - (luchtvochtigheid / 100) * windsnelheid
    return gevoel_temp


# 3. Functie voor het genereren van het weerrapport
def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):

    gevoel = gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid)


    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return (
            "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
        )

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


# 4. De hoofdfunctie van het weerstation
def weerstation():
    totale_temperatuur = 0.0
    aantal_dagen = 0

    # Maximaal 7 dagen doorlopen (dag 1 t/m 7)
    for dag in range(1, 8):
        # --- TEMPERATUUR INVOER ---
        invoer_temp = input(f"Wat is op dag {dag} de temperatuur[C]: ")
        if invoer_temp == "":
            print("bye")
            break

        try:
            temp_celsius = float(invoer_temp)
        except ValueError:
            print("Ongeldige invoer voor temperatuur. Probeer het opnieuw.")
            break


        invoer_wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")
        if invoer_wind == "":
            print("bye")
            break

        try:
            windsnelheid = float(invoer_wind)
        except ValueError:
            print("Ongeldige invoer voor windsnelheid. Probeer het opnieuw.")
            break


        invoer_vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
        if invoer_vocht == "":
            print("bye")
            break

        try:
            luchtvochtigheid = float(invoer_vocht)
        except ValueError:
            print(
                "Ongeldige invoer voor luchtvochtigheid. Probeer het opnieuw."
            )
            break


        temp_fahrenheit = fahrenheit(temp_celsius)
        rapport = weerrapport(temp_celsius, windsnelheid, luchtvochtigheid)


        totale_temperatuur += temp_celsius
        aantal_dagen += 1
        gemiddelde = totale_temperatuur / aantal_dagen

        print("======================================")
        print(f"Het is {temp_celsius:.1f}C ({temp_fahrenheit:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("======================================")


# Start het weerstation
if __name__ == "__main__":
    weerstation()