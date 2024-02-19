
from unittest.mock import Mock
from kalkulacka import LogWrapper


def test_log() -> None:
    k = Mock()
    lw = LogWrapper(k)
    k.plus.return_value = 3
    # test
    r = lw.plus(1,1)
    print(f"returned: {r}")