
#Responsabilidades separadas y usando el Patrón Strategy

class Producto:
    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = float(precio)


class PagoStrategy:
    """Interfaz simple: cada estrategia calcula el total final desde el total bruto."""
    def calcular_total(self, total_bruto):
        return total_bruto


class PagoTransferencia(PagoStrategy):
    def calcular_total(self, total_bruto):
        return round(total_bruto * 0.95, 2)  # 5% desc.


class PagoEfectivo(PagoStrategy):
    def calcular_total(self, total_bruto):
        return round(total_bruto * 0.90, 2)  # 10% desc.


class PagoTarjeta(PagoStrategy):
    def calcular_total(self, total_bruto):
        return round(total_bruto, 2)  # sin descuento


class PagoFactory:
    
    @staticmethod
    def crear(nombre_metodo):
        nombre = (nombre_metodo or "").strip().lower()
        if nombre == "transferencia":
            return PagoTransferencia()
        if nombre == "efectivo":
            return PagoEfectivo()
        if nombre == "tarjeta":
            return PagoTarjeta()
        raise ValueError("Método de pago inválido: %r" % nombre_metodo)


class Pedido:

    def __init__(self, nombre_cliente, productos, metodo_pago):
        self.nombre_cliente = nombre_cliente
        self.productos = list(productos or [])
        self.pago = metodo_pago  

    def total_bruto(self):
        return round(sum(p.precio for p in self.productos), 2)

    def total_final(self):
        return self.pago.calcular_total(self.total_bruto())

    def items(self):
        
        return [(p.descripcion, p.precio) for p in self.productos]

    def registro(self):
      
        return "%s;%s;%s" % (
            self.nombre_cliente,
            self.items(),
            self.total_final()
        )


# --- Presentación (I/O de salida) ---

class PedidoPresenter:
    @staticmethod
    def imprimir(pedido, nombre_metodo_pago=None):
        print("Cliente:", pedido.nombre_cliente)
        print("Productos:")
        for desc, precio in pedido.items():
            print("  - %s - %.2f" % (desc, precio))
        if nombre_metodo_pago:
            print("Método de pago:", nombre_metodo_pago)
        print("Total bruto: %.2f" % pedido.total_bruto())
        print("Total final: %.2f" % pedido.total_final())


# --- Persistencia (I/O a archivo) ---

class PedidoArchivo:
    @staticmethod
    def guardar(pedido, ruta="pedidos.txt"):
        with open(ruta, "a", encoding="utf-8") as f:
            f.write(pedido.registro() + "\n")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    productos = [
        Producto("Teclado", 25000),
        Producto("Mouse", 15000),
        Producto("Pad", 8000),
    ]

    # elegir estrategia desde un nombre
    metodo = "efectivo"  # "transferencia" | "efectivo" | "tarjeta"
    estrategia = PagoFactory.crear(metodo)

    pedido = Pedido("Juan Pérez", productos, estrategia)

    PedidoPresenter.imprimir(pedido, nombre_metodo_pago=metodo)
    PedidoArchivo.guardar(pedido)  # guarda en pedidos.txt
