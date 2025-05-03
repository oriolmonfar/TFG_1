#Clip dictionary:
#"000": [ID, Name, *, PLST, inPoint, outPoint, Dur]

import json
import os

CONFIG_FILE = "config.json"
CLIP_MANAGEMENT_FILE = "clip_management.json"
CLIP_DICTIONARY_FILE = "clip_dictionary.json"

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

def load_clip_management():
    """Carga el archivo clip_manager.json y devuelve su contenido como un diccionario."""
    if os.path.exists(CLIP_MANAGEMENT_FILE):
        try:
            with open(CLIP_MANAGEMENT_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error leyendo clip_manager.json. Creando una nueva estructura.")
    # Si hay error o no existe, devolver estructura vacía
    return {f"{i:03d}": "void" for i in range(1000)}

def save_clip_management(data):
    """Guarda el diccionario en clip_manager.json."""
    with open(CLIP_MANAGEMENT_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_default_config():
    """Devuelve la configuración predeterminada."""
    return {
        "FAST_JOG": 50,
        "SEC_FAST_JOG": 100,
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
        "current_camangle": "A",
        "clip_id": 0,
        "last_date": "2025-03-22",
        "last_time": "12:45:33.00",
        "timecodes": [],
        "mark_in_tc": "00:00:00:00",
        "estrella1": [],
        "estrella2": [],
        "estrella3": []
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

def load_sec_fast_jog():
    """Carga el valor de FAST_JOG desde el archivo config.json."""
    global sec_fast_jog
    sec_fast_jog = load_config().get("SEC_FAST_JOG", 100)  # Actualiza la variable global
    return sec_fast_jog

def save_sec_fast_jog(value):
    """Guarda el valor de FAST_JOG en el archivo config.json y actualiza la variable global."""
    save_config("SEC_FAST_JOG", value)  # Llama a la función genérica save_config para actualizar FAST_JOG

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

def load_current_clip_pgm():
    """Carga el número de clip actual desde el archivo JSON."""
    global current_clip_pgm
    current_clip_pgm = load_config().get("CURRENT_CLIP_PGM", 1)
    return current_clip_pgm

def load_current_clip_prv():
    """Carga el número de clip actual desde el archivo JSON."""
    global current_clip_prv
    current_clip_prv = load_config().get("CURRENT_CLIP_PRV", 1)
    return current_clip_prv

def save_current_clip(value):
    """Guarda el número de clip actual en el archivo JSON."""
    save_config("CURRENT_CLIP", value)

def save_current_clip_pgm(value):
    """Guarda el número de clip actual en el archivo JSON."""
    save_config("CURRENT_CLIP_PGM", value)

def save_current_clip_prv(value):
    """Guarda el número de clip actual en el archivo JSON."""
    save_config("CURRENT_CLIP_PRV", value)

def load_current_camangle():
    """Carga el cam angle actual desde el archivo JSON."""
    global current_camangle
    current_camangle = load_config().get("current_camangle", "A")
    return current_camangle

def save_current_camangle(value):
    """Guarda el número de camanlge actual en el archivo JSON."""
    save_config("current_camangle", value)

def load_current_clip_id():
    """Carga el clip id actual desde el archivo JSON."""
    global clip_id 
    clip_id = load_config().get("clip_id", "0")
    return clip_id

def save_current_clip_id(value):
    """Guarda el clip id actual en el archivo JSON."""
    save_config("clip_id", value)

def load_last_date():
    """Carga el clip id actual desde el archivo JSON."""
    global last_date 
    last_date = load_config().get("last_date", "2025-03-22")
    return last_date

def save_last_date(value):
    """Guarda el clip id actual en el archivo JSON."""
    save_config("last_date", value)

def load_last_time():
    """Carga el clip id actual desde el archivo JSON."""
    global last_time 
    last_time = load_config().get("last_time", "12:45:33.00")
    return last_time

def save_last_time(value):
    """Guarda el clip id actual en el archivo JSON."""
    save_config("last_time", value)


# Funciones relacionadas con clip_mode

def load_clip_mode():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global clip_mode
    clip_mode = load_config().get("clip_mode", False)  # Establece el valor por defecto como False
    return clip_mode

def save_clip_mode(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("clip_mode", value)

def load_page_mode():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global modo_page
    modo_page = load_config().get("modo_page", False)  # Establece el valor por defecto como False
    return modo_page

def save_page_mode(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("modo_page", value)

def load_shift():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global SHIFT
    SHIFT = load_config().get("SHIFT", False)  # Establece el valor por defecto como False
    return SHIFT

def save_shift(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("SHIFT", value)


def load_mark_in_tc():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global mark_in_tc
    mark_in_tc = load_config().get("mark_in_tc", "00:00:00:00")  # Establece el valor por defecto como False
    return mark_in_tc

def save_mark_in_tc(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("mark_in_tc", value)

def load_active_playlist():
    """Carga el estado de clip_mode desde el archivo config.json."""
    global active_playlist
    active_playlist = load_config().get("active_playlist", "PL1")  # Establece el valor por defecto como False
    return active_playlist

def save_active_playlist(value):
    """Guarda el estado de clip_mode en el archivo config.json y actualiza la variable global."""
    save_config("active_playlist", value)


def load_timecodes_list():
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get("timecodes", [])

def save_timecodes_list(timecodes):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config["timecodes"] = timecodes  # Actualizar la lista de VMIX
    save_config("timecodes", timecodes)  # Guardar la lista actualizada

def load_estrella1_list():
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get("estrella1", [])

def save_estrella1_list(element):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config["estrella1"] = element  # Actualizar la lista de VMIX
    save_config("estrella1", element)  # Guardar la lista actualizada

def load_estrella2_list():
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get("estrella2", [])

def save_estrella2_list(element):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config["estrella2"] = element  # Actualizar la lista de VMIX
    save_config("estrella2", element)  # Guardar la lista actualizada

def load_estrella3_list():
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get("estrella3", [])

def save_estrella3_list(element):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config["estrella3"] = element  # Actualizar la lista de VMIX
    save_config("estrella3", element)  # Guardar la lista actualizada


#functiones relacionada clip_management
def load_clip_dictionary():
    try:
        with open(CLIP_DICTIONARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {str(i).zfill(3): ["void"] * 7 for i in range(1000)}

def save_clip_dictionary(data):
    with open(CLIP_DICTIONARY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def update_clip_dictionary(index, new_value):
    if not (0 <= index < 7):  # Verifica que el índice esté en el rango válido
        print("Índice fuera de rango. Debe estar entre 0 y 6.")
        return

    data = load_clip_dictionary()  # Cargar el diccionario desde el archivo

    # Modificar el elemento en la posición especificada en todas las listas
    for key in data:
        data[key][index] = new_value  

    save_clip_dictionary(data)  # Guardar los cambios en el archivo
    print(f"Se actualizó el índice {index} en todas las listas con '{new_value}'")


#cargar playlists

def load_plst(num):
    """Carga la lista de VMIX desde el archivo config.json."""
    config = load_config()
    return config.get(f"playlist{num}", [])

def save_plst(num, element):
    """Guarda la lista de VMIX en el archivo config.json."""
    config = load_config()
    config[f"playlist{num}"] = element  # Actualizar la lista de VMIX
    save_config(f"playlist{num}", element)  # Guardar la lista actualizada




