import requests
import xml.etree.ElementTree as ET

# URL de la API de vMix
url = "http://127.0.0.1:8088/api"

# Realiza la petición HTTP a la API de vMix
response = requests.get(url)
root = ET.fromstring(response.content)

def extraer_hora_completa(timecode):
    """Extrae HH:MM:SS.mmm de un timecode con formato ISO."""
    if timecode and "T" in timecode:
        return timecode.split("T")[1]
    return None

# Lista para almacenar los timecodes formateados
timecodes = []

# Buscar inputs de tipo Replay y extraer timecodes
for input_element in root.find("inputs"):
    if input_element.get("type") == "Replay":
        replay = input_element.find("replay")
        if replay is not None:
            timecodes.append({
                "timecode": extraer_hora_completa(replay.findtext("timecode")),
                "timecodeA": extraer_hora_completa(replay.findtext("timecodeA")),
                "timecodeB": extraer_hora_completa(replay.findtext("timecodeB"))
            })

# Mostrar resultados
for tc in timecodes:
    print(tc)

