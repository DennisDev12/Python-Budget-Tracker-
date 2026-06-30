import json
import os

bestand = "budget.json"

# Kijken of het bestand al bestaat
if os.path.exists(bestand):
    with open(bestand, "r") as f:
        gegevens = json.load(f)
else:
    gegevens = {
        "inkomsten": [],
        "uitgaven": []
    }

while True:
    print("\n===== Budget Tracker =====")
    print("1. Inkomst toevoegen")
    print("2. Uitgave toevoegen")
    print("3. Saldo bekijken")
    print("4. Alles bekijken")
    print("5. Stoppen")

    keuze = input("Maak een keuze: ")

    if keuze == "1":
        omschrijving = input("Waar komt het geld vandaan? ")
        bedrag = float(input("Bedrag: €"))

        nieuwe_inkomst = {
            "omschrijving": omschrijving,
            "bedrag": bedrag
        }

        gegevens["inkomsten"].append(nieuwe_inkomst)

        with open(bestand, "w") as f:
            json.dump(gegevens, f, indent=4)

        print("Inkomst opgeslagen!")

    elif keuze == "2":
        omschrijving = input("Waar heb je geld aan uitgegeven? ")
        bedrag = float(input("Bedrag: €"))

        nieuwe_uitgave = {
            "omschrijving": omschrijving,
            "bedrag": bedrag
        }

        gegevens["uitgaven"].append(nieuwe_uitgave)

        with open(bestand, "w") as f:
            json.dump(gegevens, f, indent=4)

        print("Uitgave opgeslagen!")

    elif keuze == "3":
        totaal_inkomsten = 0
        totaal_uitgaven = 0

        for inkomen in gegevens["inkomsten"]:
            totaal_inkomsten += inkomen["bedrag"]

        for uitgave in gegevens["uitgaven"]:
            totaal_uitgaven += uitgave["bedrag"]

        saldo = totaal_inkomsten - totaal_uitgaven

        print("\n----- Saldo -----")
        print("Totaal inkomsten: €", round(totaal_inkomsten, 2))
        print("Totaal uitgaven: €", round(totaal_uitgaven, 2))
        print("Saldo: €", round(saldo, 2))

    elif keuze == "4":
        print("\n=== Inkomsten ===")

        if len(gegevens["inkomsten"]) == 0:
            print("Nog geen inkomsten toegevoegd.")
        else:
            for inkomen in gegevens["inkomsten"]:
                print(
                    inkomen["omschrijving"],
                    "- €",
                    round(inkomen["bedrag"], 2)
                )

        print("\n=== Uitgaven ===")

        if len(gegevens["uitgaven"]) == 0:
            print("Nog geen uitgaven toegevoegd.")
        else:
            for uitgave in gegevens["uitgaven"]:
                print(
                    uitgave["omschrijving"],
                    "- €",
                    round(uitgave["bedrag"], 2)
                )

    elif keuze == "5":
        print("Programma afgesloten.")
        break

    else:
        print("Deze keuze bestaat niet.")