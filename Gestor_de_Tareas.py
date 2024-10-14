class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo        # Almacena el título de la tarea.
        self.completada = False     # Inicializa el estado como no completada.

    def marcar_completada(self):
        self.completada = True  # Cambia el estado a completada.

    def __str__(self):
        estado = "✔️" if self.completada else "❌"  # Define el estado.
        return f"{estado} {self.titulo}"  # Devuelve la representación de la tarea.

class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo):
        tarea = Tarea(titulo)  # Crear una instancia de Tarea
        self.tareas.append(tarea)

    def listar_tareas(self):
        for idx, tarea in enumerate(self.tareas):
            print(f"{idx + 1}. {tarea}")  # Llama a __str__ automáticamente

    def marcar_tarea_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
        else:
            print("Índice inválido.")

def main():
    gestor = GestorDeTareas()

    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            titulo = input("Introduce el título de la tarea: ")
            gestor.agregar_tarea(titulo)
        elif opcion == '2':
            gestor.listar_tareas()
        elif opcion == '3':
            indice = int(input("Introduce el índice de la tarea a marcar como completada: ")) - 1
            gestor.marcar_tarea_completada(indice)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
