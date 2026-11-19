from unittest.mock import Mock, call

from kauppa import Kauppa
from tuote import Tuote


def luo_kauppa():
    pankki = Mock()
    viitteet = Mock()
    viitteet.uusi.side_effect = [11, 12, 13, 14]

    maito = Tuote(1, "maito", 5)
    leipa = Tuote(2, "leipa", 7)
    tuotteet = {1: maito, 2: leipa}

    varasto = Mock()
    varasto.saldo.return_value = 10
    varasto.hae_tuote.side_effect = lambda id: tuotteet[id]

    kauppa = Kauppa(varasto, pankki, viitteet)
    return kauppa, varasto, pankki, viitteet, maito, leipa


def test_uusi_asiointi_nollaa_edellisen_ostoksen():
    kauppa, varasto, pankki, viitteet, maito, leipa = luo_kauppa()

    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.tilimaksu("pekka", "111")

    kauppa.aloita_asiointi()
    kauppa.tilimaksu("liisa", "222")

    assert pankki.tilisiirto.call_args_list == [
        call("pekka", 11, "111", "33333-44455", 5),
        call("liisa", 12, "222", "33333-44455", 0),
    ]


def test_uusi_viitenumero_jokaiselle_maksulle():
    kauppa, varasto, pankki, viitteet, maito, leipa = luo_kauppa()

    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.tilimaksu("pekka", "111")

    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(2)
    kauppa.tilimaksu("liisa", "222")

    assert viitteet.uusi.call_count == 2
    assert pankki.tilisiirto.call_args_list == [
        call("pekka", 11, "111", "33333-44455", 5),
        call("liisa", 12, "222", "33333-44455", 7),
    ]


def test_tuotteen_poistaminen_korista():
    kauppa, varasto, pankki, viitteet, maito, leipa = luo_kauppa()

    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(2)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("pekka", "111")

    varasto.palauta_varastoon.assert_called_once_with(maito)
    pankki.tilisiirto.assert_called_once_with(
        "pekka", 11, "111", "33333-44455", 7
    )


def test_loppunutta_tuotetta_ei_lisata():
    kauppa, varasto, pankki, viitteet, maito, leipa = luo_kauppa()
    varasto.saldo.return_value = 0

    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.tilimaksu("pekka", "111")

    varasto.hae_tuote.assert_not_called()
    varasto.ota_varastosta.assert_not_called()
    pankki.tilisiirto.assert_called_once_with(
        "pekka", 11, "111", "33333-44455", 0
    )