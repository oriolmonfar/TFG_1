import requests
import xml.etree.ElementTree as ET

def get_replay_info_from_vmix():
    try:
        # Hacer la solicitud HTTP a la API de vMix
        response = requests.get("http://127.0.0.1:8088/api/")
        response.raise_for_status()  # Lanza error si el status code no es 200

        # Parsear el contenido XML
        root = ET.fromstring(response.content)

        # Buscar el input con type="Replay"
        replay_input = None
        for input_elem in root.findall('./inputs/input'):
            if input_elem.attrib.get('type') == 'Replay':
                replay_input = input_elem
                break

        if replay_input is None:
            raise ValueError("No se encontró ningún input de tipo Replay.")

        # Buscar el subelemento <replay>
        replay_elem = replay_input.find('replay')
        if replay_elem is None:
            raise ValueError("El input Replay no contiene un elemento <replay>.")

        # Extraer los valores necesarios
        speedA = replay_elem.attrib.get('speedA')
        speedB = replay_elem.attrib.get('speedB')
        cameraA = replay_elem.attrib.get('cameraA')
        cameraB = replay_elem.attrib.get('cameraB')

        return speedA, speedB, cameraA, cameraB

    except requests.RequestException as e:
        print(f"Error en la solicitud a vMix: {e}")
        return None, None, None, None
    except ET.ParseError as e:
        print(f"Error al parsear XML: {e}")
        return None, None, None, None
    except ValueError as e:
        print(f"Error en los datos del replay: {e}")
        return None, None, None, None

a, b, c, d = get_replay_info_from_vmix()

print(a)
print(b)
print(c)
print(d)

