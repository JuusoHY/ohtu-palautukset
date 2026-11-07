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

Pyysin GitHub Copilotin Agent-tilaa toteuttamaan NHL-sovellukseen
joukkuekohtaisen pelaajahaun ja siihen yksikkötestit.

Agentti tutki projektin tiedostoja, ehdotti koodimuutoksia,
loi stub-pohjaiset pytest-testit ja yritti ajaa tarkistukset.
Agentin työssä tuli myös ongelmia: sama metodi näkyi
kahteen kertaan ja VS Coden tallennusristiriita esti
muutetun koodin tallentumisen levylle.

Lopullinen player_stats.py korjattiin erikseen.
Tämän jälkeen kaikki neljä yksikkötestiä menivät läpi
ja Pylint antoi 10/10. Joukkuehakua kokeiltiin myös
oikeilla NHL-pelaajatiedoilla: DAL-joukkueen pelaajat
löytyivät oikeassa pistejärjestyksessä.

Testit käyttävät StubPlayerReader-luokkaa eivätkä tee
HTTP-pyyntöjä. Stub-periaate oli tuttu jo edellisen
viikon harjoituksista. Nyt sillä testattiin myös
pilkuilla eroteltuja joukkuekoodeja ja pistejärjestystä.

Pylint löysi agentin testien työversiosta
dokumentointi- ja muotoiluvirheitä.
Tallennusristiriidan aikana Pylint ilmoitti myös
no-member-virheistä, koska se luki vanhaa lähdekoodia.
Lopuksi ongelmat korjattiin ja Pylint antoi 10/10.
Agentti oli hyödyllinen mutta ei tehnyt täysin valmista
ratkaisua itsenäisesti. Opin, että agentin tekemät
muutokset on aina tarkistettava ja testattava itse.

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
- joukkueen perusteella hakeminen
- joukkueen pelaajien pistejärjestys
- useassa joukkueessa pelanneen pelaajan löytyminen

Stubin käyttäminen tekee testeistä nopeita ja riippumattomia
ulkoisen verkkopalvelun saatavuudesta.

Kaikki neljä yksikkötestiä menivät läpi.
Pylint antoi lähdekoodille tuloksen 10/10.

## Yhteenveto

Copilotin automaattinen koodintäydennys oli hyödyllinen,
ja Ask-tila auttoi ymmärtämään olemassa olevaa koodia.

Agentin ensimmäinen yritys eteni hitaasti.
Uudella yrityksellä agentti muokkasi koodia ja testejä,
mutta lopputulos tarvitsi vielä korjauksia.

Opin, että tekoälyn ehdottama koodi kannattaa aina
tarkistaa. Yksikkötestit ja Pylint ovat hyödyllisiä
työkaluja toimivuuden ja koodin laadun varmistamisessa.

## Pylint-selityksen tarkistus

Rikoin kokeilutiedostossa tarkoituksella projektin
80 merkin rivipituussääntöä. Pylint ilmoitti C0301-virheestä.

Pyysin Copilotin Ask-tilaa selittämään varoituksen.
Copilot kertoi, että pitkät rivit heikentävät luettavuutta
ja että koodirivin voi jakaa useammalle riville.

Tarkistin selityksen Pylintin dokumentaatiosta.
Selitys piti paikkansa.

Kokeilutiedosto poistettiin tarkistuksen jälkeen.

Dokumentaatio:
https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/line-too-long.html
