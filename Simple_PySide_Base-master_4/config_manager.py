
"""""
import json
import os

CONFIG_FILE = "config.json"  # Nombre del archivo JSON

# Variables globales
fast_jog = 10  # Valor inicial
ip_vmix = "127.0.0.1:8088"  # Valor inicial

def save_config(key, value):
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
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error leyendo config.json. Se usará la configuración por defecto.")
            return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088", "VMIX_LIST": []}  # Valores predeterminados si el archivo es inválido
    return {"FAST_JOG": 25, "IP_VMIX": "127.0.0.1:8088", "VMIX_LIST": []}  # Valores por defecto si el archivo no existe

"""

import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Carga el archivo JSON y devuelve un diccionario con los valores."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error leyendo config.json. Se usará la configuración por defecto.")
            return get_default_config()  # Valores predeterminados si el archivo es inválido
    return get_default_config()  # Valores por defecto si el archivo no existe

def save_config(key, value):
    """Guarda una clave-valor en el archivo JSON sin borrar las otras."""
    config = load_config()  # Cargar la configuración actual
    config[key] = value  # Actualizar o añadir el valor
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)  # Guardar el archivo actualizado

def get_default_config():
    """Devuelve la configuración predeterminada."""
    return {
        "FAST_JOG": 50,
        "IP_VMIX": "127.0.0.1:8088",
        "VMIX_LIST": [
            "VMIX_URI (127.0.0.1:8088)"
        ],
        "CURRENT_PAGE": 1,
        "CURRENT_BANK": 1,
        "CURRENT_CLIP": 1,
        "last_page": 1,
        "last_bank_per_page": {
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 1,
            "8": 1,
            "9": 1,
            "10": 1
        },
        "last_clip": 1,
        "clip_mode": False,
        "current_camangle": "A"
    }

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

# Funciones relacionadas con la página, banco y clip

def load_current_page():
    """Carga el valor de la página actual desde el archivo config.json."""
    config = load_config()
    return config.get("CURRENT_PAGE", 1)

def load_current_bank():
    """Carga el valor del banco actual desde el archivo config.json, dependiendo de la página actual."""
    config = load_config()
    page = config.get("CURRENT_PAGE", 1)
    return config.get("last_bank_per_page", {}).get(str(page), 1)

def save_current_page(value):
    """Guarda el número de página actual en el archivo JSON."""
    save_config("CURRENT_PAGE", value)

def save_current_bank(value):
    """Guarda el número de banco actual en el archivo config.json y lo actualiza por página."""
    config = load_config()
    current_page = config.get("CURRENT_PAGE", 1)
    if "last_bank_per_page" not in config:
        config["last_bank_per_page"] = {}
    config["last_bank_per_page"][str(current_page)] = value  # Guardamos el banco por la página actual
    save_config("last_bank_per_page", config["last_bank_per_page"])  # Actualizar el archivo config.json

def load_current_clip():
    """Carga el número de clip actual desde el archivo JSON."""
    global current_clip
    current_clip = load_config().get("CURRENT_CLIP", 1)
    return current_clip

def save_current_clip(value):
    """Guarda el número de clip actual en el archivo JSON."""
    save_config("CURRENT_CLIP", value)

def load_current_camangle():
    """Carga el cam angle actual desde el archivo JSON."""
    global current_camangle
    current_camangle = load_config().get("current_camangle", "A")
    return current_camangle

def save_current_camangle(value):
    """Guarda el número de camanlge actual en el archivo JSON."""
    save_config("current_camangle", value)


# Funciones relacionadas con clip_mode

def load_clip_mode():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global clip_mode
    clip_mode = load_config().get("clip_mode", False)  # Establece el valor por defecto como False
    return clip_mode

def save_clip_mode(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("clip_mode", value)
