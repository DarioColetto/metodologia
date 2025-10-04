# Usa el patron Factory 
import random

class Arma:
    def nombre(self):
        return "arma"
    def bono(self):
        return 0

class Espada(Arma):
    def nombre(self):
        return "espada"
    def bono(self):
        return 5

class Arco(Arma):
    def nombre(self):
        return "arco"
    def bono(self):
        return 3

class ArmaFactory:
    @staticmethod
    def crear(nombre):
        n = (nombre or "").strip().lower()
        if n == "espada":
            return Espada()
        if n == "arco":
            return Arco()
        return Arma()

class Jugador:
    def __init__(self, nombre, hp, arma):
        self.nombre = nombre
        self.hp = int(hp)
        self.arma = arma 

class Combate:
    def __init__(self, jugador1, jugador2, seed=None):
        self.j1 = jugador1
        self.j2 = jugador2
        if seed is not None:
            random.seed(seed)

    def _tirada(self, arma):
        return random.randint(1, 10) + arma.bono()

    def run(self):
        log = []
        while self.j1.hp > 0 and self.j2.hp > 0:
            d1 = self._tirada(self.j1.arma)
            d2 = self._tirada(self.j2.arma)

            self.j2.hp -= d1
            self.j1.hp -= d2

            log.append(f"{self.j1.nombre} ataca con {self.j1.arma.nombre()} daño: {d1} HP enemigo: {self.j2.hp}")
            log.append(f"{self.j2.nombre} ataca con {self.j2.arma.nombre()} daño: {d2} HP enemigo: {self.j1.hp}")

        if self.j1.hp <= 0 and self.j2.hp <= 0:
            resultado = "Empate"
        elif self.j1.hp <= 0:
            resultado = f"{self.j2.nombre} gana"
        else:
            resultado = f"{self.j1.nombre} gana"

        log.append(resultado)
        return resultado, log
    
    def imprimir(log):
        for linea in log:
            print(linea)





#  Ejemplo de uso 
if __name__ == "__main__":
    arma1 = ArmaFactory.crear("espada")
    arma2 = ArmaFactory.crear("arco")

    j1 = Jugador("Alice", 40, arma1)
    j2 = Jugador("Bob", 40, arma2)

    combate = Combate(j1, j2, seed=123)  # seed opcional para reproducibilidad
    resultado, log = combate.run()

    combate.imprimir(log)
