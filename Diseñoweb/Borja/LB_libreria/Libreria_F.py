
class BorjaLB:
    def __init__(self, nombre="Borja", nivel=1):
        self.nombre = nombre
        self.nivel = nivel
        self.activo = True

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f"ID: {self.nombre} | Nivel: {self.nivel} | Estado: {estado}")

    def ingreso_correcto(self, clave):
        if clave == "secreto123":
            print("Ingreso correcto. Bienvenido, Borja.")
            self.activo = True
        else:
            print("Clave incorrecta. Acceso denegado.")
            self.activo = False
