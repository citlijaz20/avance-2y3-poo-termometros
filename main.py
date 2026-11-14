# Importamos las clases y componentes desde nuestro módulo modelos.py
from modelos import Bateria, TermometroDigital, TermometroInfrarrojo

print("=== HOSPITAL CUGDL: CONTROL DE EQUIPOS BIOMÉDICOS ==_\n")

# 1. Creación de baterías independientes (Composición)
bateria_omron = Bateria("Ion-Litio", 1500)
bateria_braun = Bateria("Alcalina AA", 2500)

# 2. Instanciación de objetos usando la clase base y la subclase
termometro1 = TermometroDigital("Omron", "Piso 1 - Sala A", bateria_omron)
termometro2 = TermometroInfrarrojo("Braun", "Urgencias", bateria_braun, 15)

# 3. Pruebas de métodos, encapsulamiento y polimorfismo
print(termometro1.encender())
print(termometro1.tomar_temperatura(37.1))

print("\n--------------------------------------------------\n")

print(termometro2.encender())
print(termometro2.tomar_temperatura(39.0)) # Aquí actúa el polimorfismo del termómetro infrarrojo

print("\n--- ESTADO FINAL DE CADA DISPOSITIVO ---")
print(termometro1.mostrar_info())
print(termometro2.mostrar_info())

# Demostración del acceso seguro a atributos privados (Encapsulamiento)
print("\n--- CONSULTA DE DATOS ENCAPSULADOS ---")
print(f"Temperatura privada consultada de forma segura: {termometro1.get_temperatura()} °C")
print(f"Nivel exacto de batería de Urgencias: {bateria_braun.get_nivel_carga()}%")
