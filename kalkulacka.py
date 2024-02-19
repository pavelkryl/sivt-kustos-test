# kontrakt kalkulacky
from abc import ABC, abstractmethod
import logging


class AbstractKalkulator(ABC):

    @abstractmethod
    def plus(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def minus(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def multi(self, op1: int, op2: int) -> int:
        ...

    @abstractmethod
    def divide(self, op1: int, op2: int) -> float:
        ...



logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(name)s %(message)s', level=logging.DEBUG)

class LogWrapper(AbstractKalkulator):

    def __init__(self, kalkulator: AbstractKalkulator) -> None:
        self._kalkulator = kalkulator
        

    def plus(self, op1: int, op2: int) -> int:
        logger.debug(f'Sčítám {op1} a {op2}')
        result = self._kalkulator.plus(op1, op2)
        logger.debug(f'Výsledek: {result}')
        return result

    def minus(self, op1: int, op2: int) -> int:
        logger.debug(f'Odčítám {op1} od {op2}')
        result = self._kalkulator.minus(op1, op2)
        logger.debug(f'Výsledek: {result}')
        return result

    def multi(self, op1: int, op2: int) -> int:
        logger.debug(f'Násobím {op1} a {op2}')
        result = self._kalkulator.multi(op1, op2)
        logger.debug(f'Výsledek: {result}')
        return result

    def divide(self, op1: int, op2: int) -> float:
        logger.debug(f'Dělím {op1} číslem {op2}')
        result = self._kalkulator.divide(op1, op2)
        logger.debug(f'Výsledek: {result}')
        return result
