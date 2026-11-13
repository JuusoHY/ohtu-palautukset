# Viikko 3 - Tehtava 8: Agentti ja hyvaksymistestit

## Agentin generoima ohjetiedosto

Kaytin VS Coden GitHub Copilotia Agent-tilassa. Komento /init loi
tiedoston login/.github/copilot-instructions.md.

Ohjetiedostossa kuvattiin Flask-sovelluksen rakenne, uv-komennot,
Robot Framework -testien suorittaminen ja validoinnin sijainti
UserService.validate()-metodissa.

Ohjeita taydennettiin Windows ARM64 -ympariston rajoituksilla.
Robot Frameworkin selainriippuvuutta ei saatu asennettua paikallisesti,
joten selaintestit suoritettiin GitHub Actionsissa Linuxilla.

## Testit ennen toteutusta

Agenttia pyydettiin kasittelemaan kaksi user storya yksitellen.
Molemmissa tapauksissa agentti kirjoitti ensin Robot Framework
-hyvaksymistestit ja pysahtyi ennen toteutuksen muuttamista.

Ensimmainen story koski pelkista kirjaimista koostuvien salasanojen
hylkaamista. Uudet testit paljastivat kaksi virheellisesti hyvaksyttya
salasanaa. Toteutuksen korjaamisen jalkeen kaikki testit menivat lapi.

Toisessa storyssa tarkistettiin salasanan ja sen vahvistuksen vastaavuus.
Uusi testi epaonnistui ensin odotetusti. Validoinnin toteuttamisen
jalkeen kaikki 15 Robot-testia menivat lapi.

## Agentin ohjaaminen

Agentille annettiin tarkat hyvaksymiskriteerit ja rajattiin muutokset
ensin testitiedostoon ja vasta sen jalkeen validointimetodiin.
Agenttia ohjeistettiin myos olemaan asentamatta selainriippuvuuksia
paikallisesti. Testitulokset tarkistettiin GitHub Actionsista jokaisen
vaiheen jalkeen.

## Toteutuksen tarkoituksellinen rikkominen

Testien toimivuus tarkistettiin kahdella eri rikkomiskokeella.

1. Pelkista kirjaimista koostuvien salasanojen tarkistus poistettiin
   kaytosta. Kaksi Robot-testia epaonnistui odotetusti.
2. Salasanan ja vahvistuksen vertailu poistettiin kaytosta.
   Yksi Robot-testi epaonnistui odotetusti.

Lopuksi alkuperainen toimiva toteutus palautettiin ja kaikki
15 Robot-testia menivat jalleen lapi.

## Mitä opin

Harjoitus havainnollisti, miksi hyvaksymistestit kannattaa kirjoittaa
ennen toteutusta. Ensin epaonnistuva testi osoitti konkreettisesti
puuttuvan toiminnallisuuden. Tarkoitukselliset rikkomiskokeet puolestaan
osoittivat, etta testit todella tunnistavat kyseiset virheet.

Opin myos, etta agentille kannattaa antaa tarkat, rajatut tehtavat
ja tarkistaa sen muutokset seka testitulokset itse.