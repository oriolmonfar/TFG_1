"""""
import json
import os

CONFIG_FILE = "config.json"  # Nombre del archivo JSON

def save_config(key, value):
    config = load_config()  # Cargar la configuración actual
    config[key] = value  # Actualizar o añadir el valor
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def load_config():

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error leyendo config.json. Se usará la configuración por defecto.")
            return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088"}
    return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088"}  # Valores por defecto si el archivo no existe

def load_fast_jog():
    return load_config().get("FAST_JOG", 25)

def save_fast_jog(value):

    save_config("FAST_JOG", value)

def load_ip_vmix():

    return load_config().get("IP_VMIX", "127.0.0.1:8088")

def save_ip_vmix(value):

    save_config("IP_VMIX", value)"
 "
 ""
 """
import json
import os

CONFIG_FILE = "config.json"  # Nombre del archivo JSON

# Variables globales
fast_jog = 10  # Valor inicial
ip_vmix = "127.0.0.1:8088"  # Valor inicial

def save_config(key, value):
    """Guarda una clave-valor en el archivo JSON sin borrar las otras."""
    config = load_config()  # Cargar la configuración actual
    config[key] = value  # Actualizar o añadir el valor
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)  # Guardar el archivo actualizado

    # Actualizar la variable global después de guardar
    global fast_jog, ip_vmix
    if key == "FAST_JOG":
        fast_jog = value
    elif key == "IP_VMIX":
        ip_vmix = value

def load_config():
    """Carga el archivo JSON y devuelve un diccionario con los valores."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error leyendo config.json. Se usará la configuración por defecto.")
            return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088", "VMIX_LIST": []}  # Valores predeterminados si el archivo es inválido
    return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088", "VMIX_LIST": []}  # Valores por defecto si el archivo no existe

# Funciones de carga y guardado de FAST_JOG

def load_fast_jog():
    """Carga el valor de FAST_JOG desde el archivo config.json."""
    global fast_jog
    fast_jog = load_config().get("FAST_JOG", 25)  # Actualiza la variable global
    return fast_jog

def save_fast_jog(value):
    """Guarda el valor de FAST_JOG en el archivo config.json y actualiza la variable global."""
    save_config("FAST_JOG", value)  # Llama a la función genérica save_config para actualizar FAST_JOG

# Funciones de carga y guardado de IP_VMIX

def load_ip_vmix():
    """Carga el valor de IP_VMIX desde el archivo config.json."""
    global ip_vmix
    ip_vmix = load_config().get("IP_VMIX", "127.0.0.1:8088")  # Actualiza la variable global
    return ip_vmix

def save_ip_vmix(value):
    """Guarda el valor de IP_VMIX en el archivo config.json y actualiza la variable global."""
    save_config("IP_VMIX", value)  # Llama a la función genérica save_config para actualizar IP_VMIX

def load_vm_list():
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get("VMIX_LIST", [])

def save_vm_list(vmix_list):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config["VMIX_LIST"] = vmix_list  # Actualizar la lista de VMIX
    save_config("VMIX_LIST", vmix_list)  # Guardar la lista actualizada

def update_vmix_list(selected_value):
    """Mueve el vmix seleccionado al inicio de VMIX_LIST en config.json."""
    config = load_config()

    vmix_list = config.get("VMIX_LIST", [])

    # Si ya existe en la lista, lo eliminamos para evitar duplicados
    if selected_value in vmix_list:
        vmix_list.remove(selected_value)

    # Insertamos el seleccionado al inicio de la lista
    vmix_list.insert(0, selected_value)

    # Guardamos la lista actualizada en config.json
    save_config("VMIX_LIST", vmix_list)