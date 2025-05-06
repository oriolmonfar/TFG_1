from flask import Flask, Response, jsonify, send_from_directory
import requests
from xml.etree import ElementTree as ET
import time
import threading
import os
import re
from config_manager import *
from app_modules import * 

IP_VMIX = load_ip_vmix()

app = Flask(__name__, static_folder='.', static_url_path='')

UIFunctions.send_request("api/?Function=BrowserNavigate&Input=8&Value=https://localhost:5000/")

# Configuración
CONFIG = {
    'BACKGROUND_IMAGE': 'preset_replay4+2.png',
    'VMIX_API_URL': f'http://{IP_VMIX}/api',
    'UPDATE_INTERVAL_MS': 50,
    'VUMETER': {
        'INPUT': {'HEIGHT': 50, 'WIDTH': 6},
        'REPLAY': {'HEIGHT': 75, 'WIDTH': 8}
    }
}

# Datos compartidos
vu_data = {
    'channelmode': None,
    'input_1': {'meterF1': 0, 'meterF2': 0},
    'input_2': {'meterF1': 0, 'meterF2': 0},
    'input_3': {'meterF1': 0, 'meterF2': 0},
    'input_4': {'meterF1': 0, 'meterF2': 0},
    'replay': {
        'meterF1': 0, 
        'meterF2': 0,
        'timecode': '00:00:00.000',  # Mostrará timecodeA
        'cameraA': None,
        'speedA': None,
        'cam_angleA': None, 
        'inpoint_clipA': None,
        'countdownA':None, 
        'ID_A': None

    },
    'replay_preview': {
        'meterF1': 0, 
        'meterF2': 0,
        'timecode': '00:00:00.000',  # Mostrará timecodeB
        'cameraB': None,
        'speedB': None,
        'cam_angleB': None, 
        'inpoint_clipB': None,
        'countdownB':None, 
        'ID_B': None
    }
}

from datetime import datetime, timedelta

from datetime import datetime, timedelta

from datetime import datetime

def calculate_clip_duration_mw(clip_tc_in, clip_tc_out):
    """
    Calcula la duración entre clip_tc_in y clip_tc_out.

    clip_tc_in tiene formato "HH:MM:SS.sss"
    clip_tc_out tiene formato "YYYY-MM-DDTHH:MM:SS.sss"

    Retorna:
        str: Duración del clip en formato "HH:MM:SS.sss"
    """
    try:
        # Formatos esperados
        format_in = "%H:%M:%S.%f"
        format_out = "%Y-%m-%dT%H:%M:%S.%f"

        # Parsear clip_tc_in con fecha base ficticia
        base_date = "1900-01-01"
        time_in = datetime.strptime(f"{base_date}T{clip_tc_in}", f"%Y-%m-%dT{format_in}")

        # Parsear clip_tc_out directamente
        time_out = datetime.strptime(clip_tc_out, format_out)

        # Restar los datetime
        duration = time_out - time_in

        if duration.total_seconds() < 0:
            raise ValueError("clip_tc_out es anterior a clip_tc_in")

        # Convertir la duración en componentes
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds % 1) * 1000)

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

    except Exception as e:
        raise ValueError(f"Error procesando los timecodes: {e}")




def get_channelmode():
    """Obtiene el modo de canal ('channelMode') de la sección de Replay en vMix."""
    
    # Paso 1: Obtener el XML desde la API de vMix
    response = UIFunctions.send_request("api/")  # Usamos send_request con el endpoint de la API
    
    if not response:
        print("No se pudo obtener el XML debido a la falta de conexión con vMix.")
        return None  # Salimos de la función si no hay conexión

    # Paso 2: Parsear el XML
    try:
        root = ET.fromstring(response)  # Convertimos el texto XML en una estructura de árbol
    except ET.ParseError as e:
        print(f"Error al parsear el XML: {e}")
        return None  # Salimos si hay un error en el XML

    # Paso 3: Iterar sobre todos los inputs y buscar el 'channelMode' en la sección de Replay
    result = None  # Inicializamos result como None por si no encontramos nada
    
    for input_element in root.findall(".//input"):
        replay_element = input_element.find('replay')
        
        if replay_element is not None:
            channel_mode = replay_element.get('channelMode')
            if channel_mode:
                result = channel_mode  # Guardamos el modo de canal encontrado

    return result  # Devolvemos el modo de canal o None si no se encontró

def extract_vmix_timecode(full_timecode):
    """
    Extrae el timecode en formato 'HH:MM:SS.mmm' desde un string tipo '2025-04-29T19:20:32.988'
    Devuelve '00:00:00.000' si el formato no es válido
    """
    if not full_timecode or full_timecode == '0001-01-01T00:00:00.000':
        return '00:00:00.000'

    # Formato vMix: "2025-04-29T19:20:32.988"
    match = re.match(r".*T(\d{2}:\d{2}:\d{2}\.\d{3})", full_timecode)
    if match:
        return match.group(1)
    
    return '00:00:00.000'

def fetch_vmix_audio_data():
    """Función que obtiene los datos de audio y timecodes de vMix"""
    global vu_data
    
    while True:
        try:
            response = requests.get(CONFIG['VMIX_API_URL'], timeout=1)
            if response.status_code != 200:
                raise Exception(f"Error HTTP {response.status_code}")
                
            xml_data = response.text
            root = ET.fromstring(xml_data)
            
            # Inicializar estructura temporal para nuevos datos
            new_data = {
                'channelmode': None,
                'input_1': {'meterF1': 0, 'meterF2': 0},
                'input_2': {'meterF1': 0, 'meterF2': 0},
                'input_3': {'meterF1': 0, 'meterF2': 0},
                'input_4': {'meterF1': 0, 'meterF2': 0},
                'replay': {
                    'meterF1': 0, 
                    'meterF2': 0,
                    'timecode': '00:00:00.000',
                    'cameraA': None,
                    'speedA': None,
                    'cam_angleA': None,
                    'countodownA':None, 
                    'ID_A': None
                },
                'replay_preview': {
                    'meterF1': 0, 
                    'meterF2': 0,
                    'timecode': '00:00:00.000',
                    'cameraB': None,
                    'speedB': None,
                    'cam_angleB': None, 
                    'countodwnB':None, 
                    'ID_B': None

                }
            }
            
            # Primero encontrar el elemento replay para obtener timecodeA y timecodeB
            replay_timecodeA = '00:00:00.000'
            replay_timecodeB = '00:00:00.000'
            replay_found = False

            current_clip_pgm = load_current_clip_pgm()
            current_clip_prv = load_current_clip_prv()
            numeric_codeA = current_clip_pgm[:-1]
            numeric_codeB = current_clip_prv[:-1]

            try:
                with open(CLIP_DICTIONARY_FILE, "r") as file:
                    clip_data = json.load(file)
            except FileNotFoundError:
                print(f"Error: El archivo {CLIP_DICTIONARY_FILE} no existe.")
                return None

            clip_listA = clip_data.get(numeric_codeA, ["void"] * 7)
            clip_listB = clip_data.get(numeric_codeB, ["void"] * 7)

            outpoint_clipA = clip_listA[5]
            outpoint_clipB = clip_listB[5]
            ID_A = current_clip_pgm
            ID_B = current_clip_prv

            
            replay = root.find(".//replay")
            if replay is not None:
                # Obtener atributos
                replay_attrs = replay.attrib
                # Obtener los timecodes
                replay_timecodeA = extract_vmix_timecode(replay.findtext("timecodeA"))
                replay_timecodeB = extract_vmix_timecode(replay.findtext("timecodeB"))
                speedA = replay.get("speedA")
                speedB = replay.get("speedB")
                cameraA = replay.get("cameraA")
                cameraB = replay.get("cameraB")
                replay_found = True

                #print(f"[REPLAY] speedA: {speedA}, speedB: {speedB}, cameraA: {cameraA}, cameraB: {cameraB}")
                label_speedA = str(round(float(speedA)* 100))
                label_speedB = str(round(float(speedB)* 100))
                channelmode = get_channelmode()

                countdownA = calculate_clip_duration_mw(replay_timecodeA, outpoint_clipA )
                countdownB = calculate_clip_duration_mw(replay_timecodeB, outpoint_clipB )

                print(countdownA)
                print(countdownB)



                if cameraA == "1": 
                    label_rec_A = "REC 1"
                    label_cam_angleA = "CamA"
                elif cameraA == "2": 
                    label_rec_A = "REC 2"
                    label_cam_angleA = "CamB"
                elif cameraA == "3": 
                    label_rec_A = "REC 3"
                    label_cam_angleA = "CamC"
                elif cameraA == "4": 
                    label_rec_A = "REC 4"
                    label_cam_angleA = "CamD"
                else: 
                    label_rec_A = "REC"
                    label_cam_angleA = "Cam"

                if cameraB == "1": 
                    label_rec_B = "REC 1"
                    label_cam_angleB = "CamA"
                elif cameraB == "2": 
                    label_rec_B = "REC 2"
                    label_cam_angleB = "CamB"
                elif cameraB == "3": 
                    label_rec_B = "REC 3"
                    label_cam_angleB = "CamC"
                elif cameraB == "4": 
                    label_rec_B = "REC 4"
                    label_cam_angleB = "CamD"
                else: 
                    label_rec_B = "REC"
                    label_cam_angleB = "Cam"

            #print(f"[LABELS] speedA: {label_speedA}, speedB: {label_speedB}, REC A: {label_rec_A}, REC B: {label_rec_B}")
            
            # Asignar timecodes A y B a sus respectivos lugares
            new_data['replay']['timecode'] = replay_timecodeA
            new_data['replay_preview']['timecode'] = replay_timecodeB
            new_data['replay']['speedA'] = label_speedA
            new_data['replay']['cameraA'] = label_rec_A
            new_data['replay']['cam_angleA'] = label_cam_angleA
            new_data['replay']['countdownA'] = countdownA
            new_data['replay']['ID_A'] = ID_A
            new_data['replay_preview']['speedB'] = label_speedB
            new_data['replay_preview']['cameraB'] = label_rec_B
            new_data['replay_preview']['cam_angleB'] = label_cam_angleB
            new_data['replay_preview']['countdownB'] = countdownB
            new_data['replay_preview']['ID_B'] = ID_B
            new_data['channelmode'] = channelmode

            print(new_data)
            
            # Procesar todos los inputs para obtener medidores y timecodes individuales
            for input_elem in root.findall('inputs/input'):
                number = input_elem.get('number', '').strip()
                input_type = input_elem.get('type', '').strip()
                
                if number in ['1', '2', '3', '4']:
                    key = f'input_{number}'
                    try:
                        # Obtener valores de los medidores
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        
                        # Obtener timecode del input
                        timecode = extract_vmix_timecode(input_elem.get('timecode', ''))
                        
                        # Actualizar datos
                        new_data[key].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2,
                            'timecode': timecode
                        })
                    except Exception as e:
                        print(f"Error procesando input {number}: {str(e)}")
                
                elif input_type == 'Replay':
                    try:
                        # Solo actualizar medidores (timecode ya lo tenemos)
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        new_data['replay'].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2
                        })
                    except Exception as e:
                        print(f"Error procesando Replay: {str(e)}")
                
                elif input_type == 'ReplayPreview':
                    try:
                        # Solo actualizar medidores (timecode ya lo tenemos)
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        new_data['replay_preview'].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2
                        })
                    except Exception as e:
                        print(f"Error procesando ReplayPreview: {str(e)}")
            
            # Actualizar datos globales solo si hay cambios
            if new_data != vu_data:
                vu_data.update(new_data)
                print("Datos actualizados:", {k: v['timecode'] for k, v in vu_data.items() if 'timecode' in v})
            
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con vMix: {str(e)}")
            time.sleep(1)
        except ET.ParseError as e:
            print(f"Error parseando XML: {str(e)}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            time.sleep(0.1)
        else:
            time.sleep(CONFIG['UPDATE_INTERVAL_MS'] / 1000)


@app.route('/')
def index():
    """Endpoint principal con timecodes"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>vMix Multiview</title>
        <style>
            body, html {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                font-family: 'Arial', sans-serif;
                background-color: transparent !important;
            }}
            .background {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0)
                background-size: cover;
                background-position: center;
                z-index: -1;
                opacity: 0.9;
            }}
            .container {{
                position: relative;
                width: 100%;
                height: 100%;
            }}
            .vu-pair {{
                position: absolute;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 4px;
            }}
            .input-vu-meter {{
                width: {CONFIG['VUMETER']['INPUT']['WIDTH']}px;
                height: {CONFIG['VUMETER']['INPUT']['HEIGHT']}px;
                border: 1px solid rgba(255, 255, 255, 0.5);
                background-color: rgba(0, 0, 0, 0.3);
                display: flex;
                flex-direction: column-reverse;
                border-radius: 2px;
                overflow: hidden;
            }}
            .replay-vu-meter {{
                width: {CONFIG['VUMETER']['REPLAY']['WIDTH']}px;
                height: {CONFIG['VUMETER']['REPLAY']['HEIGHT']}px;
                border: 1px solid rgba(255, 255, 255, 0.5);
                background-color: rgba(0, 0, 0, 0.3);
                display: flex;
                flex-direction: column-reverse;
                border-radius: 2px;
                overflow: hidden;
            }}
            .timecode {{
                color: white;
                font-size: 22px;
                font-weight: bold;
                text-shadow: 1px 1px 2px black;
                background-color: rgba(0, 0, 0, 0);
                padding: 2px 5px;
                border-radius: 3px;
                margin-top: 5px;
                text-align: center;
                min-width: 120px;
                font-family: 'Courier New', monospace;
                position: absolute;
            }}
            .timecode_trans {{
                color: rgba(0,0,0,0);
                font-size: 14px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0);
                padding: 2px 5px;
                margin-top: 5px;
                text-align: center;
                min-width: 120px;
                font-family: 'Courier New', monospace;
            }}
            .timecode-label {{
                position: absolute;
                color: white;
                font-size: 30px;
                text-shadow: 1px 1px 1px black;
                margin-bottom: 2px;
            }}
            .label-rec {{
                color: white;
                font-size: 12px;
                text-shadow: 1px 1px 1px black;
                margin-bottom: 2px;
                position: absolute;
            }}
            .label-replay {{
                color: white;
                font-size: 22px;
                text-shadow: 1px 1px 1px black;
                margin-bottom: 2px;
                position: absolute;
            }}
        </style>
    </head>
    <body>
    

        <div class="background"></div>
        <div class="container">
            <div class="timecode" id="label_cam_pgm" style="top: 870px; left: 250px;">{vu_data['replay']['cameraA']}</div>
            <div class="timecode" id="label_speed_pgm" style="top: 825px; left: 355px;">{vu_data['replay']['speedA']}</div>
            <div class="timecode" id="label_cam_prv" style="top: 870px; left: 1210px;">{vu_data['replay_preview']['cameraB']}</div>
            <div class="timecode" id="label_speed_prv" style="top: 825px; left: 1315px;">{vu_data['replay_preview']['speedB']}</div>
            <div class="timecode" id="cam_angleA" style="top: 870px; left: 150px;">{vu_data['replay']['cam_angleA']}</div>
            <div class="timecode" id="cam_angleB" style="top: 870px; left: 1110px;">{vu_data['replay_preview']['cam_angleB']}</div>

            <div class="label-replay" id="label_pgm" style="top: 450px; left: 455px;">PGM</div>
            <div class="label-replay" id="label_prv" style="top: 450px; left: 1415px;">PRV</div>
            <div class="label-rec" style="top: 60px; left: 395px;">REC 1</div>
            <div class="label-rec" style="top: 60px; left: 875px;">REC 2</div>
            <div class="label-rec" style="top: 60px; left: 1355px;">REC 3</div>
            <div class="label-rec" style="top: 60px; left: 1835px;">REC 4</div>
            <!-- Inputs 1-4 -->
            <div class="vu-pair" style="top: 150px; left: 355px;">
                <div class="timecode_trans" id="input_1_timecode">{vu_data['input_1']}</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_1_meterF1"></div>
                    <div class="input-vu-meter" id="input_1_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 150px; left: 835px;">
                <div class="timecode_trans" id="input_2_timecode">{vu_data['input_2']}</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_2_meterF1"></div>
                    <div class="input-vu-meter" id="input_2_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 150px; left: 1315px;">
                <div class="timecode_trans" id="input_3_timecode">{vu_data['input_3']}</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_3_meterF1"></div>
                    <div class="input-vu-meter" id="input_3_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 150px; left: 1795px;">
                <div class="timecode_trans" id="input_4_timecode">{vu_data['input_4']}</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_4_meterF1"></div>
                    <div class="input-vu-meter" id="input_4_meterF2"></div>
                </div>
            </div>
            
            <!-- Replays -->
            <div class="timecode" id="replay_timecode" style="position: absolute; top: 825px; left: 180px;">{vu_data['replay']['timecode']}</div>
            <div class="vu-pair" style="top: 750px; left: 720px;">
                <div style="display: flex; gap: 4px;">
                    <div class="replay-vu-meter" id="replay_meterF1"></div>
                    <div class="replay-vu-meter" id="replay_meterF2"></div>
                </div>
            </div>
            <div class="timecode" id="replay_preview_timecode" style="position: absolute; top: 825px; left: 1140px;">{vu_data['replay_preview']['timecode']}</div>
            <div class="vu-pair" style="top: 750px; left: 1680px;">
                <div style="display: flex; gap: 4px;">
                    <div class="replay-vu-meter" id="replay_preview_meterF1"></div>
                    <div class="replay-vu-meter" id="replay_preview_meterF2"></div>
                </div>
            </div>
        </div>

        <script>
            // Configuración de colores
            const colors = {{
                green: 'rgba(0, 255, 0, 0.7)',
                yellow: 'rgba(255, 255, 0, 0.7)',
                red: 'rgba(255, 0, 0, 0.7)'
            }};

            function updateMeter(elementId, value) {{
                const meter = document.getElementById(elementId);
                if (!meter) return;
                
                meter.innerHTML = '';
                
                const sections = calculateMeterSections(value);
                sections.forEach(section => {{
                    if (section.height > 0) {{
                        const bar = document.createElement('div');
                        bar.style.width = '100%';
                        bar.style.height = `${{section.height}}%`;
                        bar.style.backgroundColor = colors[section.color];
                        meter.appendChild(bar);
                    }}
                }});
            }}

            function calculateMeterSections(value) {{
                const val = Math.min(Math.max(value, 0), 1);
                const threshold1 = 0.6;
                const threshold2 = 0.95;
                
                return [
                    {{ // Zona verde (0-60%)
                        color: 'green',
                        height: val <= threshold1 ? (val / threshold1) * 60 : 60
                    }},
                    {{ // Zona amarilla (60-95%)
                        color: 'yellow',
                        height: val <= threshold1 ? 0 : 
                               val <= threshold2 ? ((val - threshold1) / (threshold2 - threshold1)) * 35 : 35
                    }},
                    {{ // Zona roja (95-100%)
                        color: 'red',
                        height: val <= threshold2 ? 0 : ((val - threshold2) / (1 - threshold2)) * 5
                    }}
                ];
            }}

            function updateAllMeters() {{
                fetch('/vu_data')
                    .then(response => response.json())
                    .then(data => {{
                        // Actualizar VU meters
                        updateMeter('input_1_meterF1', data.input_1.meterF1);
                        updateMeter('input_1_meterF2', data.input_1.meterF2);
                        updateMeter('input_2_meterF1', data.input_2.meterF1);
                        updateMeter('input_2_meterF2', data.input_2.meterF2);
                        updateMeter('input_3_meterF1', data.input_3.meterF1);
                        updateMeter('input_3_meterF2', data.input_3.meterF2);
                        updateMeter('input_4_meterF1', data.input_4.meterF1);
                        updateMeter('input_4_meterF2', data.input_4.meterF2);
                        updateMeter('replay_meterF1', data.replay.meterF1);
                        updateMeter('replay_meterF2', data.replay.meterF2);
                        updateMeter('replay_preview_meterF1', data.replay_preview.meterF1);
                        updateMeter('replay_preview_meterF2', data.replay_preview.meterF2);
                        
                        // Actualizar timecodes
                        document.getElementById('input_1_timecode').textContent = data.input_1.timecode;
                        document.getElementById('input_2_timecode').textContent = data.input_2.timecode;
                        document.getElementById('input_3_timecode').textContent = data.input_3.timecode;
                        document.getElementById('input_4_timecode').textContent = data.input_4.timecode;
                        document.getElementById('replay_timecode').textContent = data.replay.timecode;
                        document.getElementById('replay_preview_timecode').textContent = data.replay_preview.timecode;
                        document.getElementById('label_cam_pgm').textContent = data.replay.cameraA;
                        document.getElementById('label_speed_pgm').textContent = data.replay.speedA;
                        document.getElementById('label_cam_prv').textContent = data.replay_preview.cameraB;
                        document.getElementById('label_speed_prv').textContent = data.replay_preview.speedB;
                        document.getElementById('cam_angleA').textContent = data.replay.cam_angleA;
                        document.getElementById('cam_angleB').textContent = data.replay_preview.cam_angleB;

                        // Seleccionar PGM o PRV

                        if (data.channelmode === 'A') {{
                            document.getElementById('label_pgm').textContent = '*PGM*';
                            document.getElementById('label_prv').textContent = 'PRV';
                        }} else if (data.channelmode === 'B') {{
                            document.getElementById('label_pgm').textContent = 'PGM';
                            document.getElementById('label_prv').textContent = '*PRV*';
                        }}


                    }})
                    .catch(error => console.error('Error:', error));
                
                requestAnimationFrame(updateAllMeters);
            }}

            document.addEventListener('DOMContentLoaded', updateAllMeters);
        </script>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

@app.route('/vu_data')
def get_vu_data():
    """Endpoint que devuelve los datos de los VU meters en JSON"""
    response = jsonify(vu_data)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/preset_replay4+2.png')
def serve_background():
    return send_from_directory('.', 'preset_replay4+2.png')

def check_requirements():
    if not os.path.exists(CONFIG['BACKGROUND_IMAGE']):
        print(f"\nERROR: No se encuentra la imagen de fondo '{CONFIG['BACKGROUND_IMAGE']}'")
        print(f"Por favor, coloca la imagen en la misma carpeta que este script:")
        print(f"Ubicación actual: {os.getcwd()}\n")
        return False
    return True

if __name__ == '__main__':
    if check_requirements():
        threading.Thread(target=fetch_vmix_audio_data, daemon=True).start()
        print("\nServidor iniciado: http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
