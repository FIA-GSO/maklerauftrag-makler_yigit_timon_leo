komplex = False
Sub_Rechtecke = 0
Gesamtfläche  = 0
dictionary = {}

while True:
    raumname = input("Name des Raumes: ")

    # Raum komplex (hat er Sub_Rechtecke oder nicht)?
    komplex = input("Ist der Raum komplex? (True/False): ")
    if komplex == 'True':
        Sub_Rechtecke = int(input("Wie viele Rechtecke hat der Raum?:"))
    else: #bei einem einfachen Raum gibt es nur ein Rechteck das berechnet werden muss
        Sub_Rechtecke = 1

    # Itteriert ueber die Sub_Rechtecke für den Raum und berechnet die Fläche
    while Sub_Rechtecke > 0:
        a = float(input("Länge des Sub_Raumes in Meter: "))
        b = float(input("Breite des Sub_Raumes in Meter: "))
        Fläche = a * b
        dictionary[raumname] = Fläche #Raumname + Fläche werden in Dictionary gespeichert
        Gesamtfläche = Gesamtfläche + Fläche # Hinzufügen von Fläche zur Gesamtfläche
        Sub_Rechtecke = Sub_Rechtecke - 1 

    Raum = input("Gibt es noch weiter Räume im Gebäude? (True/False):") 
    if Raum == "False": 
        print(f"Gesamtfläche: {Gesamtfläche}")
        for key in dictionary: #Ausgabe der Flächen der einzelnen Räume
            print(f"Raum: {key}| Fläche: {dictionary[key]}m²")
        break

