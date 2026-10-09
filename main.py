import os
from api.weather_api import live_weer
from modules.weerstation import start_weerstation
from modules.smart_home import tel_dagen, bereken_alles, pas_aan

def toon_live_weer():
    """Toont het actuele weer in Utrecht via de Open-Meteo API."""
    print("\n--- LIVE WEER UTRECHT (Open-Meteo API) ---")
    data = live_weer()
    if data["succes"]:
        print(f"Temperatuur : {data['temp']} °C")
        print(f"Windsnelheid: {data['wind']} km/h")
    else:
        print(f"[FOUT] {data['fout']}")


def main_menu():
    """Centraal hoofdmenu (CLI)."""
    base_dir = os.path.dirname(__file__)
    in_file = os.path.join(base_dir, "data", "input.txt")
    out_file = os.path.join(base_dir, "data", "output.txt")

    while True:
        print("\n================ SMART APP MENU ================")
        print("1. Live weer Utrecht bekijken (API)")
        print("2. Handmatig weerstation starten")
        print("3. Hoeveel dagen aanwezig in input.txt?")
        print("4. Autobereken actuatoren (naar output.txt)")
        print("5. Waarde overschrijven in output.txt")
        print("6. Stoppen")
        print("================================================")

        keuze = input("Maak een keuze (1-6): ").strip()

        if keuze == "1":
            toon_live_weer()

        elif keuze == "2":
            start_weerstation()

        elif keuze == "3":
            dagen = tel_dagen(in_file)
            if dagen is not None:
                print(f"\n[INFO] Er zijn {dagen} dagen aanwezig in de dataset.")

        elif keuze == "4":
            bereken_alles(in_file, out_file)

        elif keuze == "5":
            pas_aan(out_file)

        elif keuze == "6":
            print("\nBedankt voor het gebruiken van de Smart App!")
            break

        else:
            print("\n[FOUT] Ongeldige keuze, kies een getal van 1 tot en met 6.")


if __name__ == "__main__":
    main_menu()