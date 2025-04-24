from flask import Flask, Response, jsonify, send_from_directory
import requests
from xml.etree import ElementTree as ET
import time
import threading
import os
import re

app = Flask(__name__, static_folder='.', static_url_path='')

# Configuración
BACKGROUND_IMAGE = 'preset_replay4+2.png'
INPUT_VUMETER_HEIGHT = 110
INPUT_VUMETER_WIDTH = 10
REPLAY_VUMETER_HEIGHT = 150
REPLAY_VUMETER_WIDTH = 12

# Datos compartidos
vu_data = {
    'input_1': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
    'input_2': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
    'input_3': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
    'input_4': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
    'replay': {
        'meterF1': 0, 
        'meterF2': 0,
        'timecodeA': '00:00:00.00',
        'timecodeB': '00:00:00.00',
        'timecode': '00:00:00.00'
    },
    'replay_preview': {
        'meterF1': 0, 
        'meterF2': 0,
        'timecode': '00:00:00.00'
    }
}

def format_timecode(full_timecode):
    """Formatea el timecode de vMix a HH:MM:SS.ms"""
    if not full_timecode:
        return '00:00:00.00'
    print(full_timecode)
    
    # Extraer solo la parte del tiempo (formato 0001-01-01T00:00:00.000)
    match = re.search(r'T(\d{2}:\d{2}:\d{2}\.\d{2})\d*', full_timecode)
    if match:
        return match.group(1)
    return '00:00:00.00'

def fetch_vmix_audio_data():
    """Función que obtiene los datos de audio y timecodes de vMix"""
    global vu_data
    
    while True:
        try:
            response = requests.get('http://127.0.0.1:8088/api', timeout=1)
            xml_data = response.text
            root = ET.fromstring(xml_data)
            inputs = root.findall('inputs/input')
            replay = root.find('replay')
            
            new_data = {
                'input_1': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
                'input_2': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
                'input_3': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
                'input_4': {'meterF1': 0, 'meterF2': 0, 'timecode': '00:00:00.00'},
                'replay': {
                    'meterF1': 0, 
                    'meterF2': 0,
                    'timecodeA': '00:00:00.00',
                    'timecodeB': '00:00:00.00',
                    'timecode': '00:00:00.00'
                },
                'replay_preview': {
                    'meterF1': 0, 
                    'meterF2': 0,
                    'timecode': '00:00:00.00'
                }
            }
            
            # Procesar inputs normales
            for input_elem in inputs:
                number = input_elem.get('number', '').strip()
                input_type = input_elem.get('type', '').strip()
                
                if number in ['1', '2', '3', '4']:
                    key = f'input_{number}'
                    try:
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        # Obtener timecode del input
                        timecode = format_timecode(input_elem.get('timecode', ''))
                        new_data[key].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2,
                            'timecode': timecode
                        })
                    except (ValueError, TypeError) as e:
                        print(f"Error procesando {key}: {e}")
                
                elif input_type == 'Replay':
                    try:
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        timecode = format_timecode(input_elem.get('timecode', ''))
                        new_data['replay'].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2,
                            'timecode': timecode
                        })
                    except (ValueError, TypeError) as e:
                        print(f"Error procesando Replay: {e}")
                
                elif input_type == 'ReplayPreview':
                    try:
                        meterF1 = float(input_elem.get('meterF1', 0))
                        meterF2 = float(input_elem.get('meterF2', 0))
                        timecode = format_timecode(input_elem.get('timecode', ''))
                        new_data['replay_preview'].update({
                            'meterF1': meterF1,
                            'meterF2': meterF2,
                            'timecode': timecode
                        })
                    except (ValueError, TypeError) as e:
                        print(f"Error procesando ReplayPreview: {e}")
            
            # Procesar timecodes A/B del nodo replay principal
            if replay is not None:
                try:
                    timecodeA = format_timecode(replay.get('timecodeA', ''))
                    timecodeB = format_timecode(replay.get('timecodeB', ''))
                    new_data['replay'].update({
                        'timecodeA': timecodeA,
                        'timecodeB': timecodeB
                    })
                except Exception as e:
                    print(f"Error procesando timecodes A/B: {e}")
            
            if new_data != vu_data:
                vu_data = new_data
            
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con vMix: {e}")
            time.sleep(1)
        except ET.ParseError as e:
            print(f"Error parseando XML: {e}")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error inesperado: {e}")
            time.sleep(0.1)
        else:
            time.sleep(0.01)

@app.route('/')
def index():
    """Endpoint principal con timecodes"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>vMix VU Meters</title>
        <style>
            body, html {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                font-family: 'Courier New', monospace;
            }}
            .background {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: url('{BACKGROUND_IMAGE}');
                background-size: cover;
                background-position: center;
                z-index: -1;
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
                width: {INPUT_VUMETER_WIDTH}px;
                height: {INPUT_VUMETER_HEIGHT}px;
                border: 1px solid rgba(255,255,255,0.5);
                background-color: rgba(0,0,0,0.3);
                display: flex;
                flex-direction: column-reverse;
                border-radius: 2px;
                overflow: hidden;
            }}
            .replay-vu-meter {{
                width: {REPLAY_VUMETER_WIDTH}px;
                height: {REPLAY_VUMETER_HEIGHT}px;
                border: 1px solid rgba(255,255,255,0.5);
                background-color: rgba(0,0,0,0.3);
                display: flex;
                flex-direction: column-reverse;
                border-radius: 2px;
                overflow: hidden;
            }}
            .timecode {{
                color: white;
                font-size: 14px;
                font-weight: bold;
                text-shadow: 1px 1px 2px black;
                background-color: rgba(0,0,0,0.5);
                padding: 2px 5px;
                border-radius: 3px;
                margin-top: 5px;
                text-align: center;
                min-width: 100px;
            }}
            .timecode-ab {{
                display: flex;
                gap: 10px;
                margin-top: 5px;
            }}
            .timecode-ab span {{
                color: white;
                font-size: 14px;
                font-weight: bold;
                text-shadow: 1px 1px 2px black;
                background-color: rgba(0,0,0,0.5);
                padding: 2px 5px;
                border-radius: 3px;
                min-width: 100px;
            }}
        </style>
    </head>
    <body>
        <div class="background"></div>
        <div class="container">
            <!-- Inputs 1-4 -->
            <div class="vu-pair" style="top: 130px; left: 315px;">
                <div class="timecode" id="input_1_timecode">00:00:00.00</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_1_meterF1"></div>
                    <div class="input-vu-meter" id="input_1_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 130px; left: 690px;">
                <div class="timecode" id="input_2_timecode">00:00:00.00</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_2_meterF1"></div>
                    <div class="input-vu-meter" id="input_2_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 130px; left: 1050px;">
                <div class="timecode" id="input_3_timecode">00:00:00.00</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_3_meterF1"></div>
                    <div class="input-vu-meter" id="input_3_meterF2"></div>
                </div>
            </div>
            <div class="vu-pair" style="top: 130px; left: 1410px;">
                <div class="timecode" id="input_4_timecode">00:00:00.00</div>
                <div style="display: flex; gap: 4px;">
                    <div class="input-vu-meter" id="input_4_meterF1"></div>
                    <div class="input-vu-meter" id="input_4_meterF2"></div>
                </div>
            </div>
            
            <!-- Replays -->
            <div class="vu-pair" style="top: 560px; left: 670px;">
                <div class="timecode-ab">
                    <span id="replay_timecodeA">A: 00:00:00.00</span>
                    <span id="replay_timecodeB">B: 00:00:00.00</span>
                </div>
                <div style="display: flex; gap: 4px;">
                    <div class="replay-vu-meter" id="replay_meterF1"></div>
                    <div class="replay-vu-meter" id="replay_meterF2"></div>
                </div>
                <div class="timecode" id="replay_timecode">00:00:00.00</div>
            </div>
            <div class="vu-pair" style="top: 560px; left: 1390px;">
                <div class="timecode" id="replay_preview_timecode">00:00:00.00</div>
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
                        document.getElementById('replay_timecodeA').textContent = `A: ${{data.replay.timecodeA}}`;
                        document.getElementById('replay_timecodeB').textContent = `B: ${{data.replay.timecodeB}}`;
                        document.getElementById('replay_timecode').textContent = data.replay.timecode;
                        document.getElementById('replay_preview_timecode').textContent = data.replay_preview.timecode;
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
    return response

if __name__ == '__main__':
    # Verificar que la imagen existe
    if not os.path.exists(BACKGROUND_IMAGE):
        print(f"\nERROR: No se encuentra la imagen de fondo '{BACKGROUND_IMAGE}'")
        print(f"Por favor, coloca la imagen en la misma carpeta que este script:")
        print(f"Ubicación actual: {os.getcwd()}\n")
    else:
        print(f"Imagen de fondo encontrada: {BACKGROUND_IMAGE}")

    # Iniciar el hilo para obtener datos de vMix
    threading.Thread(target=fetch_vmix_audio_data, daemon=True).start()
    
    # Ejecutar la aplicación Flask
    print("\nServidor iniciado: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)