class AlumnoNotas:
    """
    Manejo de notas de un alumno (cálculo y regla de aprobación).
    """

    def __init__(self, notas=None, nota_aprobacion=6):
        self._notas = list(notas or [])
        self.nota_aprobacion = nota_aprobacion

    def agregar_nota(self, nota):
        self._notas.append(nota)

    def promedio(self):
        if not self._notas:
            raise ValueError("La lista de notas no puede estar vacía")
        return sum(self._notas) / len(self._notas)

    def estado(self):
        return "aprobado" if self.promedio() >= self.nota_aprobacion else "desaprobado"

    def notas(self):
        # Se devuelve una copia para no exponer la lista interna
        return list(self._notas)



class NotasImpresora:
    """
    Muestra las notas por pantalla.
    """

    @staticmethod
    def imprimir(notas):
        for i, nota in enumerate(notas, start=1):
            print(f"nota {i}: {nota}")

    @staticmethod
    def imprimir_resumen(alumno: AlumnoNotas):
        print("Notas:")
        NotasImpresora.imprimir(alumno.notas())
        print(f"Promedio: {alumno.promedio():.2f}")
        print(f"Estado: {alumno.estado()}")



class NotasArchivo:
    """
    Responsabilidad: guardar/cargar notas en archivo.
    """

    @staticmethod
    def guardar(notas, ruta="notas.txt"):
        linea = ",".join(str(n) for n in notas)
        with open(ruta, "a", encoding="utf-8") as f:
            f.write(linea + "\n")

    @staticmethod
    def cargar(ruta="notas.txt"):
        """
        Devuelve una lista de listas de notas (cada línea = un conjunto).
        Si querés solo la última línea, tomá el último elemento del resultado.
        """
        conjuntos = []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    conjuntos.append([float(x) for x in linea.split(",") if x != ""])
        except FileNotFoundError:
            pass  # si no existe el archivo, devolvemos lista vacía
        return conjuntos


#Ejemplo de uso
if __name__ == "__main__":
    alumno = AlumnoNotas([7, 8, 5])
    NotasImpresora.imprimir_resumen(alumno) 

    #Guardar las notas actuales
    NotasArchivo.guardar(alumno.notas(), ruta="notas.txt")

    #Cargar todas las líneas guardadas
    historial = NotasArchivo.cargar("notas.txt")
    print("Historial de conjuntos de notas:", historial)
