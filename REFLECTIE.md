# Reflectie

Tijdens het ontwikkelen van de KlantAssistent ben ik stap voor stap te werk gegaan. In plaats van duidelijke iteraties met aparte versies, ben ik van boven naar beneden door het Python-document gegaan en heb ik per onderdeel getest of de code werkte voordat ik verder ging. Op deze manier hield ik overzicht en kon ik fouten direct oplossen.

Ten opzichte van mijn eerste aanpak heb ik vooral verbeteringen aangebracht in de manier waarop ik input valideer en logica structureer. Een concreet voorbeeld hiervan is het controleren van het klanttype. In mijn eerste versie gebruikte ik een lange `if`-statement waarin ik meerdere voorwaarden combineerde, zoals:

`if customer_type == "nieuw" or customer_type == "bestaand" or customer_type == "premium"`

Tijdens het werken merkte ik dat dit geen nette en schaalbare oplossing was. Daarom ben ik met Lars gaan sparren om te kijken hoe hij dit probleem had aangepakt. Zijn oplossing werkte met een lijst van toegestane klanttypes en een `while`-loop die blijft vragen totdat de invoer geldig is. Deze aanpak bleek veel robuuster en overzichtelijker. Ik heb deze oplossing overgenomen en hiervan geleerd hoe je invoervalidatie op een betere manier kunt oplossen.

Daarnaast liep ik vast bij de logica in de `main()`-functie, vooral bij de volgorde van stappen en het verzamelen van meerdere klanten. Dit heb ik opgelost door eerst pseudocode te schrijven. Door het probleem eerst in woorden en stappen uit te werken, werd het makkelijker om de juiste Python-code te schrijven en de flow van het programma goed te begrijpen.


