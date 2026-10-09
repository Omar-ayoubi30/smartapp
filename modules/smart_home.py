import os

def tel_dagen(input_file):
    """Telt het aantal dataregels in het inputbestand."""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            regels = f.readlines()
        return max(0, len(regels) - 1) if regels else 0
    except FileNotFoundError:
        print(f"\n[FOUT] Het bestand '{input_file}' is niet gevonden.")
        return None
    except Exception as e:
        print(f"\n[FOUT] Fout bij het lezen van het bestand: {e}")
        return None


def bereken_alles(input_file, output_file):
    """Leest data uit input.txt, berekent actuatoren en schrijft naar output.txt."""
    try:
        with open(input_file, "r", encoding="utf-8") as f_in:
            regels = f_in.readlines()

        if len(regels) <= 1:
            print("\n[WAARSCHUWING] Het inputbestand bevat geen dataregels.")
            return

        uitvoer = []
        for idx, regel in enumerate(regels[1:], start=2):
            regel = regel.strip()
            if not regel:
                continue

            delen = regel.split()
            if len(delen) < 5:
                print(f"[WAARSCHUWING] Regel {idx} overgeslagen: onvolledige data.")
                continue

            try:
                datum = delen[0]
                mensen = int(delen[1])
                setpoint = float(delen[2])
                temp_buiten = float(delen[3])
                neerslag = float(delen[4])
            except ValueError:
                print(f"[WAARSCHUWING] Regel {idx} overgeslagen: ongeldige getalindeling.")
                continue

            # A. CV-ketel
            verschil = setpoint - temp_buiten
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            # B. Ventilatie
            vent = min(mensen + 1, 4)

            # C. Bewatering
            water = "True" if neerslag < 3 else "False"

            uitvoer.append(f"{datum};{cv};{vent};{water}\n")

        # Map aanmaken indien niet aanwezig
        map_naam = os.path.dirname(output_file)
        if map_naam:
            os.makedirs(map_naam, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.writelines(uitvoer)

        print(f"\n[SUCCES] De actuatoren zijn berekend en opgeslagen in '{output_file}'.")

    except FileNotFoundError:
        print(f"\n[FOUT] Het bestand '{input_file}' is niet gevonden.")
    except Exception as e:
        print(f"\n[FOUT] Er ging iets mis tijdens de verwerking: {e}")


def pas_aan(output_file):
    """Overschrijft handmatig een waarde in het outputbestand."""
    datum = input("Voer de datum in (bijv. 08-10-2024): ").strip()

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            regels = f.readlines()
    except FileNotFoundError:
        print(f"\n[FOUT] '{output_file}' bestaat nog niet! Voer eerst optie 4 uit.")
        return

    match_idx = -1
    for i, regel in enumerate(regels):
        if regel.strip().startswith(datum):
            match_idx = i
            break

    if match_idx == -1:
        print(f"\n[FOUT] Datum '{datum}' niet gevonden in het bestand.")
        return

    print("\nKies het systeem om te overschrijven:")
    print("1: CV-ketel (0 t/m 100)")
    print("2: Ventilatie (0 t/m 4)")
    print("3: Bewatering (0 of 1)")

    keuze = input("Maak een keuze (1-3): ").strip()
    if keuze not in ["1", "2", "3"]:
        print("\n[FOUT] Ongeldige keuze ingevoerd.")
        return

    waarde = input("Voer de nieuwe waarde in: ").strip()

    # Invoercontrole
    if keuze == "1":
        if not waarde.isdigit() or not (0 <= int(waarde) <= 100):
            print("\n[FOUT] Ongeldige CV-waarde! Kies een getal tussen 0 en 100.")
            return
    elif keuze == "2":
        if not waarde.isdigit() or not (0 <= int(waarde) <= 4):
            print("\n[FOUT] Ongeldige ventilatiewaarde! Kies een getal tussen 0 en 4.")
            return
    elif keuze == "3":
        if waarde == "0":
            waarde = "False"
        elif waarde == "1":
            waarde = "True"
        else:
            print("\n[FOUT] Ongeldige bewateringswaarde! Kies 0 of 1.")
            return

    delen = regels[match_idx].strip().split(";")
    delen[int(keuze)] = waarde
    regels[match_idx] = ";".join(delen) + "\n"

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.writelines(regels)
        print("\n[SUCCES] De waarde is succesvol aangepast!")
    except Exception as e:
        print(f"\n[FOUT] Kon bestand niet opslaan: {e}")