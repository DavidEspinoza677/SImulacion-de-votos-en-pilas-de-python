#Durante una simulación de elecciones estudiantiles en una universidad privada en Nicaragua, 
#cada mesa (junta receptora de votos) registra los votos depositados en una urna. Por motivos
#de seguridad y control, se lleva un registro digital temporal donde se apila cada voto emitido.
#En caso de error (como voto mal asignado), el último voto debe poder eliminarse rápidamente, 
#sin afectar los anteriores.


from collections import deque

class EleccionesEstudiantiles:
    def __init__(self):
        self.mesas = {i: [] for i in range(1, 6)}  # Pilas por mesa
        self.cola_global = deque()  # Cola global

    def es_mesa_valida(self, numero_mesa):
        if numero_mesa not in self.mesas:
            print(f"❌ Error: La mesa {numero_mesa} no existe. Solo hay mesas del 1 al 5.")
            return False
        return True

    def votar(self, numero_mesa, nombre_estudiante):
        if self.es_mesa_valida(numero_mesa):
            self.mesas[numero_mesa].append(nombre_estudiante)
            self.cola_global.append((numero_mesa, nombre_estudiante))
            print(f"✅ Voto registrado en mesa {numero_mesa}: {nombre_estudiante}")

    def eliminar_ultimo_voto(self, numero_mesa):
        if self.es_mesa_valida(numero_mesa):
            if self.mesas[numero_mesa]:
                voto_eliminado = self.mesas[numero_mesa].pop()
                for i in range(len(self.cola_global) - 1, -1, -1):
                    if self.cola_global[i][0] == numero_mesa and self.cola_global[i][1] == voto_eliminado:
                        del self.cola_global[i]
                        break
                print(f"🗑️ Último voto eliminado de mesa {numero_mesa}: {voto_eliminado}")
            else:
                print(f"⚠️ La mesa {numero_mesa} no tiene votos.")

    def mostrar_votos_mesa(self, numero_mesa):
        if self.es_mesa_valida(numero_mesa):
            print(f"\n📋 Votos en la mesa {numero_mesa}:")
            if not self.mesas[numero_mesa]:
                print("  (Sin votos)")
            else:
                for i, voto in enumerate(reversed(self.mesas[numero_mesa]), 1):
                    print(f"  {i}. {voto}")

    def mostrar_votos_globales(self):
        print("\n🌐 Votos globales en orden de llegada:")
        if not self.cola_global:
            print("  (Sin votos registrados)")
        else:
            for i, (mesa, voto) in enumerate(self.cola_global, 1):
                print(f"  {i}. Mesa {mesa}: {voto}")


def menu():
    elecciones = EleccionesEstudiantiles()

    while True:
        print("\n📊 MENÚ DE ELECCIONES ESTUDIANTILES")
        print("1. Votar")
        print("2. Eliminar último voto de una mesa")
        print("3. Mostrar votos por mesa")
        print("4. Mostrar todos los votos (global)")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            try:
                mesa = int(input("Número de mesa (1-5): "))
                nombre = input("Nombre del estudiante: ")
                elecciones.votar(mesa, nombre)
            except ValueError:
                print("⚠️ Entrada inválida. Debe ser un número de mesa.")

        elif opcion == "2":
            try:
                mesa = int(input("Número de mesa para eliminar el último voto: "))
                elecciones.eliminar_ultimo_voto(mesa)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "3":
            try:
                mesa = int(input("Número de mesa a mostrar: "))
                elecciones.mostrar_votos_mesa(mesa)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "4":
            elecciones.mostrar_votos_globales()

        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
