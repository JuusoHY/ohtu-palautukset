# Viikko 5 – Tehtävä 6: Ohtuvaraston verkkokäyttöliittymä

## Toteutus

VS Coden Copilot Agent toteutti Ohtuvarastolle Flask-pohjaisen
verkkokäyttöliittymän GitHub-issuen #1 perusteella.

Sovelluksella voi luoda useita varastoja, tarkastella niiden
tilavuuksia ja saldoja sekä lisätä ja ottaa tavaraa.

Toteutus käyttää projektin alkuperäistä Varasto-luokkaa.
Varastot säilytetään sovelluksen muistissa.

Ratkaisu vaikuttaa tehtävän laajuuteen nähden toimivalta.
Käyttöliittymässä on tarvittavat perustoiminnot ilman
ylimääräisiä ominaisuuksia.

## Toiminnan varmistaminen

Agentti ajoi automatisoidut testit ja tarkisti sovelluksen
toiminnan HTTP-pyynnöllä, joka palautti tilakoodin 200.

Alkuperäisen toteutuksen kaikki 31 testiä menivät läpi.
Katselmoinnin jälkeisessä versiossa testejä oli 33.

Pylint antoi arvosanan 10/10.

GitHub Actionsin Pylint-tarkistus epäonnistui ensin,
koska vanhojen Python-tiedostojen käyttämä varasto-moduuli
ei löytynyt CI-ympäristön hakupolusta. Ongelma ratkaistiin
asettamalla työnkulussa PYTHONPATH=src.

## Testien arviointi

Agentti kirjoitti testit varastojen luomiselle, listaamiselle,
tavaran lisäämiselle ja virheellisille syötteille.

Testit kattoivat keskeiset käyttötapaukset. Katselmoinnissa
huomattiin kuitenkin, että tavaran poistamisen rajatapauksia
piti testata tarkemmin.

Korjauskierroksella lisättiin testit liian suurelle
poistomäärälle sekä virheelliselle poistomäärälle.
Testeissä varmistetaan, ettei saldo muutu negatiiviseksi.

## Koodin selkeys

Flask-sovelluksen reitit ja apufunktiot ovat omassa
tiedostossaan. HTML-rakenne on erillisessä pohjassa.

Koodi hyödyntää olemassa olevaa Varasto-luokkaa eikä
toteuta samaa varastologiikkaa uudelleen.

Ratkaisun rakenne on suhteellisen yksinkertainen ja
vastaa pienen verkkosovelluksen tarpeita.

## Katselmointi

Pull requestissa #2 kirjattiin kaksi muutospyyntöä:

1. Varastolistauksessa pitää näyttää myös vapaa tila.
2. Tavaran poistamisen poikkeustilanteita pitää testata.

Koska katselmoinnin kohteena oli oma pull request,
GitHub ei sallinut Request changes -valintaa.
Muutospyyntö annettiin katselmointikommenttina ja
välitettiin VS Coden Copilot Agentille.

Agentti toteutti molemmat parannukset.
Vapaa tila näkyy käyttöliittymässä, ja testit
tarkistavat tavaran poistamisen rajatapaukset.

## Havainnot ja oppiminen

Tehtävässä tuli esiin Flaskin reittien, HTML-pohjien
ja testiasiakkaan yhteistoiminta.

Agentti sai nopeasti aikaan toimivan kokonaisuuden,
mutta katselmointi oli silti tarpeellinen.
Puuttuvat rajatapaustestit löytyivät vasta toteutusta
tarkasteltaessa.

Myös GitHub Actionsin epäonnistuminen osoitti,
että paikallisesti onnistuneet testit eivät yksin
takaa toimivuutta toisessa ympäristössä.

## Linkit

- Issue: https://github.com/JuusoHY/ohtuvarasto/issues/1
- Pull request: https://github.com/JuusoHY/ohtuvarasto/pull/2
## Lopullinen CI-tilanne

Main-haaran CI- ja Pylint-ajot onnistuivat.
