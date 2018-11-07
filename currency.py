def convert(rates,value,current,to):
    rates = [("USD", "EUR", 0.74), (“USD”, “MXN”, 19.95), (“USD”, “CAD”, 1.31)]
    if current == to:
        return value
    for conversion in rates:
        if current == conversion[0] and to == conversion[1]:
            return value * conversion[2]
    raise ValueError(f"can't convert from {current} to {to}")

def reverse_conversion:
    for conversion in rates:
        if current == conversion[1] and to == conversion[0]:
            return value / conversion[2]
    raise ValueError(f"can't convert from {current} to {to}")