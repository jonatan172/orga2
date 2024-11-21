import time

# Interfaz Command: Define una interfaz general para todos los comandos.
# Esta clase es abstracta y debe ser implementada por las subclases concretas.
class Command:
    def execute(self):
        pass  # El metodo execute debe ser implementado por las subclases

# ConcreteCommand para encender el televisor: Implementa la interfaz Command
# y especifica la accion de encender el televisor.
class EncenderTelevisionCommand(Command):
    def __init__(self, television):
        # El comando necesita una referencia al receptor (television)
        self.television = television

    # Implementacion del metodo execute que llama al metodo encender del receptor
    def execute(self):
        self.television.encender()

# ConcreteCommand para apagar el televisor: Implementa la interfaz Command
# y especifica la accion de apagar el televisor.
class ApagarTelevisionCommand(Command):
    def __init__(self, television):
        # El comando necesita una referencia al receptor (television)
        self.television = television

    # Implementacion del metodo execute que llama al metodo apagar del receptor
    def execute(self):
        self.television.apagar()

# Receiver (Receptor): La clase Television contiene la logica para encender
# y apagar la television. Estos son los metodos que se invocan desde los comandos.
class Television:
    def encender(self):
        # Metodo que se ejecuta cuando se desea encender la television
        print("La television esta encendida")

    def apagar(self):
        # Metodo que se ejecuta cuando se desea apagar la television
        print("La television esta apagada")

# Invoker (Invocador): La clase ControlRemoto es responsable de almacenar
# el comando y de ejecutarlo cuando se presiona el boton.
class ControlRemoto:
    def __init__(self):
        # El invocador puede almacenar un comando
        self.command = None

    # Este metodo se utiliza para establecer el comando que el invocador debe ejecutar
    def set_command(self, command):
        self.command = command

    # Metodo que ejecuta el comando almacenado
    def presionar_boton(self):
        if self.command:  # Comprueba si hay un comando asignado
            self.command.execute()  # Llama al metodo execute del comando

# Cliente: Crea los objetos necesarios y organiza su interaccion
if __name__ == "__main__":
    # Crear el receptor (la television)
    television = Television()

    # Crear los comandos concretos para encender y apagar la television
    comando_encender = EncenderTelevisionCommand(television)
    comando_apagar = ApagarTelevisionCommand(television)

    # Crear el invocador (el control remoto)
    control_remoto = ControlRemoto()

    # Asignar el comando de encender la television al control remoto y ejecutarlo
    print("Ejecutando comando para encender la television...")
    time.sleep(2)
    control_remoto.set_command(comando_encender)
    control_remoto.presionar_boton()  # Salida: La television esta encendida
    print("Ejecutando comando para apagar la television...")
    time.sleep(2)

    # Asignar el comando de apagar la television al control remoto y ejecutarlo
    control_remoto.set_command(comando_apagar)
    control_remoto.presionar_boton()  # Salida: La television esta apagada
