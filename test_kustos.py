from kustos import Karta, Kustos


def test_init() -> None:
    kustos = Kustos([])
    for k in range(10):
        assert not kustos.muze_vstoupit(str(k))

def test_init_2() -> None:
    kustos = Kustos([
        Karta("1", "Jan", "Novak"),
        Karta("2", "Lojza", "Kolibrik")
    ])

    assert kustos.muze_vstoupit("1")
    assert kustos.muze_vstoupit("2")
    assert not kustos.muze_vstoupit("Jan")

def test_pridej_kartu() -> None:
    kustos = Kustos([
        Karta("1", "Jan", "Novak"),
        Karta("2", "Lojza", "Kolibrik")
    ])

    assert not kustos.muze_vstoupit("3")
    kustos.pridej_kartu("3", "Pavel", "Benes")
    assert kustos.muze_vstoupit("3")
