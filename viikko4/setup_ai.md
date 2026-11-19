# Viikko 4, tehtävä 4: Testikoodin siistiminen tekoälyagentilla

Käytin GitHub Copilotin Agent-tilaa verkkokaupan testikoodin siistimiseen. Pyysin agenttia poistamaan toistuvat alustukset siirtämällä yhteiset Mock-oliot ja Kauppa-olion alustuksen setUp-metodiin. Ohjeistin sitä säilyttämään kaikkien viiden testin toiminnallisuuden ja tarkistukset.

Copilot teki muutokset mielestäni järkevästi. Testien rakenne on nyt selkeämpi, koska jokaisessa testissä näkyy paremmin juuri kyseisen tilanteen valmistelu ja varsinainen testaus. Yhteisiä Mock-olioita ei tarvitse alustaa uudelleen jokaisessa testissä.

Tarkistin agentin tekemät muutokset git diff -komennolla. Agentti säilytti alkuperäiset tarkistukset, mukaan lukien assert_called_once_with-kutsut ja niiden odotetut argumentit. Testien toiminnallisuutta ei siis havaintojeni mukaan heikennetty. Kaikki viisi testiä menivät muutoksen jälkeen läpi.

Minun ei tarvinnut korjata Copilotin tekemiä muutoksia tai pyytää uutta toteutusta. Kokemuksen perusteella agentti soveltuu hyvin mekaanisen toisteisuuden poistamiseen, mutta muutokset ja testien tarkistukset kannattaa silti käydä itse läpi.