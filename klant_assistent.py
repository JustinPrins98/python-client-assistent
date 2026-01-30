"""
CODE KICKSTART — KlantAssistent (WerkZeker Nederland)
-----------------------------------------------------

Context:
Dit project is onderdeel van de training Code Kickstart.
Je bouwt een eenvoudige Python applicatie die gegevens van burgers/aanvragers verwerkt
en op basis daarvan één advieslabel genereert.

De tool is beslisondersteunend: het advies is een intern signaal voor de medewerker.
De tool voert geen acties uit, kent geen rechten toe en neemt geen echte besluiten.

Doel:
- Oefenen met Python fundamentals (variables, types, if/elif/else, loops)
- Denken in iteraties
- Vertalen van pseudocode naar Python
- Structureren met dicts/lists en functies (parameters + return)

Spelregels:
- Werk stap voor stap
- Test elke iteratie
- Houd de code leesbaar
- Werk toe naar een werkende terminal-applicatie
"""

print("OUTPUT HELLO")


def verzamel_klant():
    """
    Vraagt gegevens van één klant/aanvrager en retourneert een dictionary.

    Verwachte keys in de dictionary:
    - naam (str)
    - leeftijd (int)
    - besteding (float)  -> bestedingsniveau per maand in euro's
    - klanttype (str)    -> 'nieuw', 'bestaand', 'premium'

    Denkstappen (pseudocode):
    1. Vraag de naam
    2. Vraag de leeftijd (moet int worden)
    3. Vraag het bestedingsniveau (moet float worden)
    4. Vraag het klanttype (alleen nieuw/bestaand/premium)
    5. Stop alles in een dictionary
    6. Return de dictionary

    Let op (iteratie 4):
    - Leeftijd en besteding moeten getallen zijn (anders opnieuw vragen)
    - Klanttype mag alleen geldige waarden hebben (anders opnieuw vragen)
    """
    # Dictionary
    customer_info_dic = {
        "name" : None,
        "age" : None,
        "budget" : None,
        "type" : None}

    # flag
    customer_age_set = False
    budget_customer_set = False

    name_customer = str(input("Wat is uw naam? "))
    customer_info_dic["name"] = name_customer

    while customer_age_set == False:
        try:
            age_customer = int(input("Wat is uw leeftijd? "))
        except:
            print("Age has to be a digit")
        else:
            customer_info_dic["age"] = age_customer
            customer_age_set = True
    
    while budget_customer_set == False:
        try:
            budget_customer = float(input("Wat is uw bestedingsniveau? "))
        except:
            print("Budget has to be a digit")
        else:
            customer_info_dic["budget"] = budget_customer
            budget_customer_set = True

    # customer types
    customer_type = None
    customer_type_list = ["nieuw", "bestaand", "premium"]
            
    while customer_type not in customer_type_list:
        customer_type = str(input("Wat is uw klanttype? (Keuze tussen nieuw, bestaand, premium) ")).strip().lower()
    
    customer_info_dic["type"] = customer_type

    
    return customer_info_dic





def genereer_advies(customer):
    """
    Ontvangt één klant (dictionary) en retourneert één advieslabel (string).

    Advieslabels (exact deze strings gebruiken):
    - 'AOW-check en extra begeleiding'
    - 'Check aanvullende regelingen / samenloop'
    - 'Intensievere begeleiding (complex dossier)'
    - 'Standaard dienstverlening'

    Regels + prioriteit (hoog -> laag):
    1) Klanttype == 'premium' -> 'Intensievere begeleiding (complex dossier)'
    2) Leeftijd >= 67         -> 'AOW-check en extra begeleiding'
    3) Besteding > 100        -> 'Check aanvullende regelingen / samenloop'
    4) Anders                 -> 'Standaard dienstverlening'

    Denkstappen:
    1. Lees waarden uit de dictionary
    2. Gebruik if / elif / else in de juiste volgorde (prioriteit)
    3. Return één advieslabel
    """
    
    print(customer)

    advice_label = [
        'AOW-check en extra begeleiding', 
        'Check aanvullende regelingen / samenloop', 
        'Intensievere begeleiding (complex dossier)', 
        'Standaard dienstverlening'
        ]

    if customer["type"] == "premium":
        return advice_label[2]
    
    elif customer["age"] >= 67:
        return advice_label[0]
    
    elif customer["budget"] > 100:
        return advice_label[1]
    
    else:
        return advice_label[3]






def samenvatting(customers):
    """
    Print een samenvatting van alle klanten en adviezen.

    Verwachting (minimaal):
    - Print het aantal klanten
    - Print per advieslabel hoe vaak deze voorkomt

    Denkstappen:
    1. Loop over de lijst met klanten
    2. Bepaal per klant het advies (gebruik genereer_advies)
    3. Tel de adviezen (bijv. met een dict)
    4. Print het overzicht netjes
    """
    advice_dictionary = {
        "AOW-check en extra begeleiding": 0,
        "Check aanvullende regelingen / samenloop": 0,
        "Intensievere begeleiding (complex dossier)": 0,
        "Standaard dienstverlening": 0
    }
    
    # customer_list = []

    for customer in customers:
        given_advice = genereer_advies(customer)
        advice_dictionary[given_advice] += 1

    print("\n--- SAMENVATTING ---")
    print(f"Aantal klanten: {len(customers)}\n")

    for advice, count in advice_dictionary.items():
        print(f"{advice}: {count}")


def main():

    
    """
    Hoofdprogramma van de applicatie.

    Programmaflow (pseudocode):
    1. Print startbericht
    2. Vraag hoeveel klanten worden ingevoerd (moet int zijn)
    3. Maak een lege lijst voor klanten
    4. Gebruik een loop om klanten te verzamelen (verzamel_klant)
    5. Print per klant het advieslabel (genereer_advies)
    6. Toon een samenvatting (samenvatting)
    """
    print("KlantAssistent gestart (WerkZeker Nederland)")
    print("Welkom bij de KlantAssistent")

    customer_list = []

    while True:
        try:
            amount_of_customers = int(input("Hoeveel klanten wil je invoeren? "))
            break
        except:
            print("Aantal moet een getal zijn")

    for _ in range(amount_of_customers):
        customer = verzamel_klant()
        customer_list.append(customer)

        advies = genereer_advies(customer)
        print(f"Advies: {advies}\n")

    samenvatting(customer_list)


if __name__ == "__main__":
    main()

