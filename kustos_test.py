from kustos import Karta, Kustos

kustos = Kustos([
    Karta("1", "Jan", "Novak"),
    Karta("2", "Lojza", "Kolibrik")
])

if kustos.muze_vstoupit("1"):
    kustos.pridej_kartu("1", "Jana", "Chloupková")
if kustos.muze_vstoupit("3"):
    kustos.pridej_kartu("3", "Pavel", "Beneš")
kustos.odeber_kartu("1")
if kustos.muze_vstoupit("2"):
    kustos.pridej_kartu("2", "Ondřej", "Mrzílek")