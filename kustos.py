from dataclasses import dataclass
from typing import Optional

@dataclass
class Karta:
    id: str
    jmeno: str
    prijmeni: str


class Kustos():
    """
    Třída vrátného, rozhoduje, zda určitá karta může vstoupit do budovy.
    """
    def __init__(self, opravnene_karty: list[Karta]) -> None:
        self.opravnene_karty = {}
        for karta in opravnene_karty:
            self.opravnene_karty[karta.id] = karta
    
    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        """Přidává kartu do evidence Pokud přidání proběhne úspěšně, vrací objekt karty, jinak vrací None."""
        if id_karty not in self.opravnene_karty:
            return None
        # else:
        karta: Karta = Karta(id_karty, jmeno, prijmeni)
        self.opravnene_karty[id_karty] = karta
        return karta
   
    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        """Odebírá kartu z evidence Pokud odebrání proběhne úspěšně, vrací objekt karty, jinak vrací None."""
        if id_karty not in self.opravnene_karty:
            return None
        # else:
        return self.opravnene_karty.pop(id_karty)

    def muze_vstoupit(self, id_karty: str) -> bool:
        """Vrací True, nebo False podle toho, zda karta s určitým id může vstoupit."""
        return id_karty in self.opravnene_karty