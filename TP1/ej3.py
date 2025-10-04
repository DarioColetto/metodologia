FACTOR = 9 / 5
OFFSET_F = 32

def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte °C a °F."""
    return celsius * FACTOR + OFFSET_F