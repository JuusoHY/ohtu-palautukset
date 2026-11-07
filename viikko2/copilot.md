# Viikko 2: Kokemuksia GitHub Copilotista

## Koodin automaattinen täydentäminen

Kokeilin Copilotin automaattista koodintäydennystä
NHL-projektin PlayerStats-luokassa.

Kirjoitin top_goal_scorers-metodin alun, minkä jälkeen
Copilot ehdotti metodille toteutusta. Ehdotus haki pelaajat
PlayerReaderin avulla ja järjesti heidät maalimäärän mukaan
laskevaan järjestykseen.

Ehdotus vaikutti järkevältä ja sopi ohjelman rakenteeseen.
Poistin kokeilumetodin tämän jälkeen, koska sen tarkoituksena
oli vain testata automaattista koodintäydennystä.

## Ask-tilan kokeileminen

Pyysin Copilotia selittämään PlayerReader-luokan toimintaa.

Copilot kuvasi, miten ohjelma hakee pelaajatiedot HTTP-pyynnöllä,
käsittelee vastauksen JSON-muodossa ja muodostaa tiedoista
Player-olioita. Se selitti myös aikakatkaisun ja HTTP-virheiden
käsittelyn.

Kysyin lisäksi top_scorers_by_nationality-metodin toiminnasta.
Copilot selitti kansallisuuden perusteella tehtävän suodatuksen
ja pelaajien järjestämisen pisteiden mukaan.

Molemmat selitykset olivat selkeitä ja vastasivat
ohjelman lähdekoodia.

## Pylint-varoitusten selittäminen

Kokeilin Pylint-varoitusten selittämistä Copilotilla.

Copilot havaitsi player_stats.py-tiedostossa C0305-varoituksen,
joka tarkoitti ylimääräisiä tyhjiä rivejä tiedoston lopussa.
Se selitti, että kyseessä oli koodin muotoiluun liittyvä
huomautus eikä ohjelman toiminnallinen virhe.

Kokeilin myös itse tarkoituksellista käyttämätöntä import os
-riviä. Pylint ilmoitti siitä W0611-varoituksen eli
unused-import.

Kokeilu osoitti, että Pylint auttaa tunnistamaan myös
sellaisia koodin laatuongelmia, jotka eivät suoraan estä
ohjelman suorittamista.

## Agent-tilan kokeileminen

Kokeilin GitHub Copilotin Agent-tilaa.

Annoin agentille tehtäväksi lisätä PlayerStats-luokkaan
top_scorers_by_team-metodin, jonka avulla voidaan hakea
tietyn NHL-joukkueen pelaajat pistejärjestyksessä.

Agentin toiminta oli kuitenkin odottamaani hitaampaa.
En käyttänyt agentin tuottamaa koodia lopullisessa
toteutuksessa.

Kokeilu auttoi ymmärtämään Agent-tilan ideaa: agentti voi
tutkia projektia ja tehdä siihen muutoksia itsenäisesti,
mutta sen etenemistä ja ehdotuksia pitää seurata.

## Joukkuekohtainen pelaajahaku

Lopulliseen ohjelmaan lisättiin top_scorers_by_team-metodi.

Metodi hakee pelaajat PlayerReaderin kautta, suodattaa
annetussa joukkueessa pelanneet pelaajat ja järjestää heidät
pisteiden mukaan laskevaan järjestykseen.

Toteutuksessa huomioidaan myös tilanteet, joissa pelaajan
team-kentässä on useita joukkueita.

## Yksikkötestit

Uudelle toiminnallisuudelle tehtiin neljä pytest-yksikkötestiä.

Testeissä käytetään StubPlayerReader-luokkaa, joka palauttaa
ennalta määritellyt pelaajat ilman verkkoyhteyttä.

Testeillä tarkistetaan:
- kansallisuuden perusteella hakeminen
- joukkueen perusteella hakeminen ja pistejärjestys
- pienillä kirjaimilla tehtävä joukkuehaku
- tuntemattoman joukkueen palauttama tyhjä lista

Stubin käyttäminen tekee testeistä nopeita ja riippumattomia
ulkoisen verkkopalvelun saatavuudesta.

Kaikki neljä yksikkötestiä menivät läpi.
Pylint antoi lähdekoodille tuloksen 10/10.

## Yhteenveto

Copilotin automaattinen koodintäydennys oli hyödyllinen,
ja Ask-tila auttoi ymmärtämään olemassa olevaa koodia.

Agent-tila vaikutti kiinnostavalta, mutta sen käyttö
oli tällä kertaa liian hidasta omaan työskentelyyni.

Opin, että tekoälyn ehdottama koodi kannattaa aina
tarkistaa. Yksikkötestit ja Pylint ovat hyödyllisiä
työkaluja toimivuuden ja koodin laadun varmistamisessa.
