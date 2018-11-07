import pytest

from currency import convert

def test_convert_same():
    assert convert([], 1, current="USD", to="USD") == 1
    assert convert([], 3, current="MXN", to="MXN") == 3


def test_convert_usd_to_euros():
    assert convert(rates = ["USD","EUR",0.74)], value=1, current="USD", to= "EUR") == 0.74
    assert convert(rates = [(“USD”, “MXN”, 19.95)], value = 1, current="USD", to ="MXN") == 19.95

def test_convert_reverse():
    assert convert(rates = ["USD","EUR",0.74)], value=3, current="USD", to= "EUR") == 1.35
        
        def test_convert_multiple_rates():
            rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]
                assert convert(rates, value=10, current="USD", to="EUR") == 7.4

def test_convert_with_no_matching_rates():
    rates = [("EUR", "JPY", 145.949)]]
    with pytest.raises(ValueError):
        convert(rates, value=10, current = "EUR", to = "MXN")