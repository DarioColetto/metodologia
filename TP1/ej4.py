class Calculadora:
    """Calculadora básica."""

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def sumar(self) -> float:
        return self.a + self.b

    def restar(self) -> float:
        return self.a - self.b

    def multiplicar(self) -> float:
        return self.a * self.b

    def dividir(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return self.a / self.b

if __name__ == "__main__":

    calc = Calculadora(10, 5)
    print("Suma:", calc.sumar())
    print("Resta:", calc.restar())
    print("Multiplicación:", calc.multiplicar())
    print("División:", calc.dividir())