from unittest.mock import Mock

from kassapaate import Kassapaate


def test_positiivinen_lataus():
    kortti = Mock()
    kassa = Kassapaate()

    kassa.lataa(kortti, 10)

    kortti.lataa.assert_called_once_with(10)


def test_negatiivista_summaa_ei_ladata():
    kortti = Mock()
    kassa = Kassapaate()

    kassa.lataa(kortti, -5)

    kortti.lataa.assert_not_called()