################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

## ==> GUI FILE
from main import *
import requests
import xml.etree.ElementTree as ET
import time
import threading
from PySide2.QtCore import QTimer
from config_manager import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    def send_request(endpoint):
        """ Envía una request HTTP a la API de vMix y maneja errores. """
        IP_VMIX = load_ip_vmix()
        url = f"http://{IP_VMIX}/{endpoint}"
        
        try:
            response = requests.get(url, timeout=2)  # Timeout para evitar que se quede bloqueado
            
            if response.status_code == 200:
                return response.text  # Devuelve el contenido si la request fue exitosa
            else:
                print(f"Error en la request: {response.status_code}")
                return None
                
        except requests.ConnectionError:
            return None
        
    def check_vmix_connection(main_window):
        """Comprueba la conexión con vMix y actualiza los frames de estado."""
        response = UIFunctions.send_request("api/")  # Comprueba conexión con vMix

        if response:
            # Conectado a vMix: Muestra el frame verde y oculta el rojo
            main_window.ui.vmix_conn_ok.setStyleSheet("background-color: rgb(0, 255, 0);")  # Verde
            main_window.ui.vmix_conn_no.setStyleSheet("background-color: rgb(40, 40, 40);")  # Gris
            main_window.ui.vmix_conn_ok.show()
            main_window.ui.vmix_conn_no.hide()
        else:
            # No conectado: Muestra el frame rojo y oculta el verde
            main_window.ui.vmix_conn_no.setStyleSheet("background-color: rgb(255, 0, 0);")  # Rojo
            main_window.ui.vmix_conn_ok.setStyleSheet("background-color: rgb(40, 40, 40);")  # Gris
            main_window.ui.vmix_conn_no.show()
            main_window.ui.vmix_conn_ok.hide()

    def start_connection_monitor(main_window):
        """Inicia un temporizador para monitorear la conexión con vMix."""
        main_window.timer = QTimer(main_window)
        main_window.timer.timeout.connect(lambda: UIFunctions.check_vmix_connection(main_window))
        main_window.timer.start(5000)  # Ejecuta cada 3 segundos

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    def labelPGM_PRV(self, text):
        if text == "A":
            self.ui.label_pgm.setText(f'                                            PGM                        ')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,0,0)")
        elif text == "B":
            self.ui.label_pgm.setText(f'                                            PRV                      ')
            self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
        else: 
            self.ui.label_pgm.setText(f'                                     LINKED A|B                ')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,165,0)")

        

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################

    ########################################################################
    ## START - MAINWINDOW FUNCTIONS
    ########################################################################

    ########################################################################
    ## END - MAINWINDOW FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - FUNCIONS CLIP
    ########################################################################
 
    def function_plst_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_playlist)
        UIFunctions.resetStyle(self, "btn_playlist")
        UIFunctions.labelPage(self, "PLAYLIST")

    



    ########################################################################
    ## END - FUNCIONS CLIP
    ########################################################################

    ########################################################################
    ## START - FUNCIONS CONTROL
    ########################################################################

    def function_loop():
        """ Controla el estado de Loop en vMix Replay """
        
        # Obtener XML de vMix
        xml_vmix = UIFunctions.send_request("api/")
        if xml_vmix is None:
            return  # Si no hay conexión, salir de la función
        
        root = ET.fromstring(xml_vmix)

        # Buscar el input con type="Replay"
        for input_element in root.findall(".//input"):
            if input_element.get("type") == "Replay":
                key = input_element.get("key")
                loop_status = input_element.get("loop")  # Obtener el estado del loop

                # Determinar la acción según el estado del Loop
                if loop_status.lower() == "true":
                    response = UIFunctions.send_request(f"api/?Function=LoopOff&Input={key}")
                    print(f"Loop desactivado en {key}") if response else print("Error al desactivar loop")
                else:
                    response = UIFunctions.send_request(f"api/?Function=LoopOn&Input={key}")
                    print(f"Loop activado en {key}") if response else print("Error al activar loop")

                return  # Salir tras encontrar y procesar el primer input "Replay"

        print("No se encontró ningún input con type='Replay'.")
    ########################################################################
    ## END - FUNCIONS CONTROL
    ########################################################################

    ########################################################################
    ## START - FUNCIONS CONTENT ACCESS
    ########################################################################
 
    def function_syncprv(self):
        """ Sincroniza la vista previa en vMix Replay seleccionando los canales A y B. """
        response = UIFunctions.send_request("api/?Function=ReplaySelectChannelAB")
        
        if response is None:
            return  # Si no hay conexión, salir de la función
        
        UIFunctions.labelPGM_PRV(self, "A|B")



    ########################################################################
    ## END - FUNCIONS CONTENT ACCESS
    ########################################################################



    ########################################################################
    ## START - FUNCIONS SIMULATOR
    ########################################################################

    def function_A(self):
        """Fetches XML from vMix, checks the replay section, and sends the appropriate command based on channel mode."""
        
        # Step 1: Fetch the XML from vMix
        response = UIFunctions.send_request("api/")  # Usamos la función send_request con el endpoint "api/"
        
        if not response:
            print("No se pudo obtener la información de vMix debido a la falta de conexión.")
            return  # Salir si no hay conexión

        # Step 2: Parse the XML
        try:
            root = ET.fromstring(response)  # Intentamos analizar la respuesta como XML
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return  # Salir si el XML no es válido

        # Find the <replay> section inside <input type="Replay">
        replay_section = root.find(".//input[@type='Replay']/replay")

        if replay_section is None:
            print("Replay section not found in XML")
            return

        # Get the channelMode attribute
        channel_mode = replay_section.get("channelMode")  

        # Step 3: Determine the appropriate action based on channel_mode
        if channel_mode == "A":
            endpoint = "api/?Function=ReplayACamera1"
        elif channel_mode == "B":
            endpoint = "api/?Function=ReplayBCamera1"
        elif channel_mode == "AB":
            endpoint = "api/?Function=ReplayACamera1"
        else:
            print(f"Unexpected channel mode: {channel_mode}")
            return

        # Send the command to vMix
        api_response = UIFunctions.send_request(endpoint)  # Usamos send_request para enviar la solicitud

        if not api_response:
            print(f"No se pudo enviar la solicitud para {endpoint} debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print(f"Comando {endpoint} enviado correctamente.")

    def function_A_prima():
        print("ejecutando funcion A prima...")

    def function_B(self):
        """Fetches XML from vMix, checks the replay section, and sends the appropriate command based on channel mode."""
        
        # Step 1: Fetch the XML from vMix
        response = UIFunctions.send_request("api/")  # Usamos la función send_request con el endpoint "api/"
        
        if not response:
            print("No se pudo obtener la información de vMix debido a la falta de conexión.")
            return  # Salir si no hay conexión

        # Step 2: Parse the XML
        try:
            root = ET.fromstring(response)  # Intentamos analizar la respuesta como XML
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return  # Salir si el XML no es válido

        # Find the <replay> section inside <input type="Replay">
        replay_section = root.find(".//input[@type='Replay']/replay")

        if replay_section is None:
            print("Replay section not found in XML")
            return

        # Get the channelMode attribute
        channel_mode = replay_section.get("channelMode")  

        # Step 3: Determine the appropriate action based on channel_mode
        if channel_mode == "A":
            endpoint = "api/?Function=ReplayACamera2"
        elif channel_mode == "B":
            endpoint = "api/?Function=ReplayBCamera2"
        elif channel_mode == "AB":
            endpoint = "api/?Function=ReplayACamera2"
        else:
            print(f"Unexpected channel mode: {channel_mode}")
            return

        # Send the command to vMix
        api_response = UIFunctions.send_request(endpoint)  # Usamos send_request para enviar la solicitud

        if not api_response:
            print(f"No se pudo enviar la solicitud para {endpoint} debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print(f"Comando {endpoint} enviado correctamente.")

    def function_B_prima():
        print("ejecutando funcion B prima...")

    def function_C(self):
        """Fetches XML from vMix, checks the replay section, and sends the appropriate command based on channel mode."""
        
        # Step 1: Fetch the XML from vMix
        response = UIFunctions.send_request("api/")  # Usamos la función send_request con el endpoint "api/"
        
        if not response:
            print("No se pudo obtener la información de vMix debido a la falta de conexión.")
            return  # Salir si no hay conexión

        # Step 2: Parse the XML
        try:
            root = ET.fromstring(response)  # Intentamos analizar la respuesta como XML
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return  # Salir si el XML no es válido

        # Find the <replay> section inside <input type="Replay">
        replay_section = root.find(".//input[@type='Replay']/replay")

        if replay_section is None:
            print("Replay section not found in XML")
            return

        # Get the channelMode attribute
        channel_mode = replay_section.get("channelMode")  

        # Step 3: Determine the appropriate action based on channel_mode
        if channel_mode == "A":
            endpoint = "api/?Function=ReplayACamera3"
        elif channel_mode == "B":
            endpoint = "api/?Function=ReplayBCamera3"
        elif channel_mode == "AB":
            endpoint = "api/?Function=ReplayACamera3"
        else:
            print(f"Unexpected channel mode: {channel_mode}")
            return

        # Send the command to vMix
        api_response = UIFunctions.send_request(endpoint)  # Usamos send_request para enviar la solicitud

        if not api_response:
            print(f"No se pudo enviar la solicitud para {endpoint} debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print(f"Comando {endpoint} enviado correctamente.")

    def function_C_prima():
        print("ejecutando funcion C prima...")

    def function_D(self):
        """Fetches XML from vMix, checks the replay section, and sends the appropriate command based on channel mode."""
        
        # Step 1: Fetch the XML from vMix
        response = UIFunctions.send_request("api/")  # Usamos la función send_request con el endpoint "api/"
        
        if not response:
            print("No se pudo obtener la información de vMix debido a la falta de conexión.")
            return  # Salir si no hay conexión

        # Step 2: Parse the XML
        try:
            root = ET.fromstring(response)  # Intentamos analizar la respuesta como XML
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return  # Salir si el XML no es válido

        # Find the <replay> section inside <input type="Replay">
        replay_section = root.find(".//input[@type='Replay']/replay")

        if replay_section is None:
            print("Replay section not found in XML")
            return

        # Get the channelMode attribute
        channel_mode = replay_section.get("channelMode")  

        # Step 3: Determine the appropriate action based on channel_mode
        if channel_mode == "A":
            endpoint = "api/?Function=ReplayACamera4"
        elif channel_mode == "B":
            endpoint = "api/?Function=ReplayBCamera4"
        elif channel_mode == "AB":
            endpoint = "api/?Function=ReplayACamera4"
        else:
            print(f"Unexpected channel mode: {channel_mode}")
            return

        # Send the command to vMix
        api_response = UIFunctions.send_request(endpoint)  # Usamos send_request para enviar la solicitud

        if not api_response:
            print(f"No se pudo enviar la solicitud para {endpoint} debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print(f"Comando {endpoint} enviado correctamente.")

    def function_D_prima():
        print("ejecutando funcion D prima...")

    def function_network():
        print("Ejecutando funcion Network...")

    def function_play(self):
        # Intentar enviar la solicitud de reproducción
        response_1 = UIFunctions.send_request("api/?Function=ReplayPlay&Channel=1")
        if not response_1:
            print("No se pudo ejecutar ReplayPlay. Saltando function_play.")
            return

        # Intentar ajustar la velocidad de reproducción
        response_2 = UIFunctions.send_request("api/?Function=ReplaySetSpeed&Value=1&Channel=1")
        if not response_2:
            print("No se pudo ajustar la velocidad de reproducción.")

    def function_gototc():
        print("Ejecutando function Goto TC...")

    def function_lastcue():
        print("Ejecutando function Last Cue... ")

    def function_fastjog(dial):
        """Cambia entre modo normal (1 frame) y modo rápido (50 frames)."""
        FAST_JOG = load_fast_jog()
        dial.fast_mode = not dial.fast_mode
        mode = f"RÁPIDO ({FAST_JOG})" if dial.fast_mode else "NORMAL (1 frame)"
        print(f"Modo cambiado a: {mode}")

    def function_mark():
        print("Ejecutando funcion Mark...")

    def function_return():
        print("Ejectuando funcion Return...")

    def function_record():
        """Fetches vMix XML, checks replay recording status, and toggles it."""
        
        # Step 1: Fetch the XML from vMix
        response = UIFunctions.send_request("api/")  # Ahora pasamos solo el endpoint
        if not response:
            print("No se pudo obtener la información de vMix debido a la falta de conexión.")
            return  # Salir si no hay conexión

        # Step 2: Parse the XML
        try:
            root = ET.fromstring(response)  # Intentamos analizar la respuesta como XML
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return  # Salir si el XML no es válido

        # Find the <replay> section inside <input type="Replay">
        replay_section = root.find(".//input[@type='Replay']/replay")

        if replay_section is None:
            print("Replay section not found in XML")
            return

        # Get the recording attribute
        recording_status = replay_section.get("recording")  # Should be "True" or "False"

        # Step 3: Send the correct HTTP request
        if recording_status == "True":
            # Stop recording if it's already on
            toggle_url = "api/?Function=ReplayStopRecording"  # Solo el endpoint
            print("Stopping replay recording...")
        else:
            # Start recording if it's off
            toggle_url = "api/?Function=ReplayStartRecording"  # Solo el endpoint
            print("Starting replay recording...")

        # Usar UIFunctions.send_request para enviar la solicitud de cambiar el estado
        toggle_response = UIFunctions.send_request(toggle_url)  # Pasamos solo el endpoint
        if not toggle_response:
            print("No se pudo cambiar el estado de la grabación debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión

        print("Replay recording toggled successfully")

    def function_page():
        print("Ejecutando funcion Page...")

    def function_prvctl(self):
        # Step 1: Fetch the XML from vMix using send_request
        response = UIFunctions.send_request("api/")  # Only pass "api/" here

        if not response:
            print("No connection to vMix. Skipping function_prvctl.")
            return  # Exit the function if there's no connection

        try:
            # Step 2: Parse the XML
            root = ET.fromstring(response)  # response is already a string

            # Find the <replay> section inside <input type="Replay">
            replay_section = root.find(".//input[@type='Replay']/replay")

            if replay_section is None:
                print("Replay section not found in XML")
                return

            # Get the channel mode
            channel_mode = replay_section.get("channelMode")  

            # Dictionary for selecting the correct API function
            functions = {
                "A": "ReplaySelectChannelB",
                "B": "ReplaySelectChannelA",
                "AB": "ReplaySelectChannelA",
            }

            if channel_mode in functions:
                url = f"api/?Function={functions[channel_mode]}"  # Pass only the endpoint to send_request()
                UIFunctions.send_request(url)  # Use send_request correctly

                # Update UI labels
                if channel_mode == "A":
                    self.ui.label_pgm.setText('                                            PRV                        ')
                    self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
                else:
                    self.ui.label_pgm.setText('                                            PGM                        ')
                    self.ui.label_pgm.setStyleSheet("color: rgb(255,0,0)")

        except ET.ParseError:
            print("Error parsing XML response from vMix")

    #function_plst_page declarada a FUNCTIONS CLIP
    #function_loop declarada a FUNCTIONS CONTROL

    def function_insert():
        print("Ejecutando function Insert... ")

    def function_browse():
        print("Ejecutando function Browse... ")

    def function_gotoin():
        print("Ejecutando funcion Goto IN...")
        
    def function_in():
        """Marks the current position as 'in' for replay."""
        
        # Endpoint para la función 'ReplayMarkIn'
        endpoint = "api/?Function=ReplayMarkIn"
        
        # Usamos UIFunctions.send_request para realizar la solicitud
        response = UIFunctions.send_request(endpoint)
        
        if not response:
            print("No se pudo marcar el 'In' debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print("Replay mark 'In' set successfully.")

    def function_gotoout():
        print("Ejecutando funcion Goto OUT...")
    
    def function_out():
        """Marks the current position as 'out' for replay."""
        
        # Endpoint para la función 'ReplayMarkOut'
        endpoint = "api/?Function=ReplayMarkOut"
        
        # Usamos UIFunctions.send_request para realizar la solicitud
        response = UIFunctions.send_request(endpoint)
        
        if not response:
            print("No se pudo marcar el 'Out' debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print("Replay mark 'Out' set successfully.")

    def function_lever():
        print("Ejecutando funcion lever...")

    def function_take():
        """Realiza la acción ReplaySwapChannels en vMix, si hay conexión."""
        response = UIFunctions.send_request("api/?Function=ReplaySwapChannels")
        
        if not response:
            print("No se pudo ejecutar 'ReplaySwapChannels' porque no hay conexión con vMix.")
            return  # Sale de la función sin hacer nada si no hay conexión
        
        print("Acción 'ReplaySwapChannels' ejecutada correctamente.")


    #dial
    def function_rodeta(dial):
        """Configura el QDial para controlar la replay de vMix frame por frame."""

        dial.setWrapping(True)  # Permite giros infinitos
        dial.setNotchesVisible(False)
        dial.previous_value = dial.value()  # Guarda el estado inicial
        dial.fast_mode = False  # Modo normal por defecto

        def on_dial_moved(value):
            """Detecta el movimiento del dial y envía la petición HTTP a vMix."""
            FAST_JOG = load_fast_jog()
            step = FAST_JOG if dial.fast_mode else 1  # Define si avanza 1 o 25 frames
            direction = step if value > dial.previous_value else -step if value < dial.previous_value else 0

            if direction != 0:
                response = UIFunctions.send_request(f"api/?Function=ReplayJumpFrames&Value={direction}&Channel=1")
                
                if response:
                    print(f"Replay movido {direction} frame(s)")
                else:
                    print("No se pudo enviar la solicitud de ReplayJumpFrames. Saltando.")

            dial.previous_value = value  # Actualiza el valor previo

        dial.valueChanged.connect(on_dial_moved)


    #Slider
    def setup_replay_speed_slider(slider: QSlider):
        """Sets up the vertical slider to control vMix replay speed with smooth values between 0 (pause) and 1 (full speed)."""

        slider.setMinimum(0)    # Bottom = 0 (paused)
        slider.setMaximum(100)  # Top = 100 (full speed)
        slider.setValue(100)    # Default to full speed when app starts

        def send_replay_speed(value):
            """Sends an HTTP request to vMix to set the replay speed."""
            speed = f"0.{value:02d}"  # Converts value to '0.xx' format (e.g., 50 → 0.50)
            if value == 100:
                speed = "1.0"  # Ensure full speed is exactly '1.0'
            
            # Usar la función send_request desde UIFunctions
            response = UIFunctions.send_request(f"api/?Function=ReplaySetSpeed&Value={speed}&Channel=1")
            
            if not response:
                print("No se pudo establecer la velocidad de repetición debido a la falta de conexión con vMix.")
                return  # Salir de la función si no hay conexión
            
            print(f"Replay speed set to: {speed}")

        def on_slider_pressed():
            """Pauses the clip when the user starts interacting with the slider."""
            send_replay_speed(slider.value())

        def on_slider_released():
            """Ensures speed is updated when the slider is released."""
            send_replay_speed(slider.value())  # Send current speed

        def on_slider_changed(value):
            """Updates the speed dynamically while sliding."""
            send_replay_speed(value)

        # Connect signals
        slider.sliderPressed.connect(on_slider_pressed)   # Pause on touch
        slider.sliderReleased.connect(on_slider_released) # Resume with new speed
        slider.valueChanged.connect(on_slider_changed)    # Change speed while moving        


    def function_e_e():
        """Jumps to current time in replay and plays it."""
        
        # Step 1: ReplayJumpToNow
        endpoint_now = "api/?Function=ReplayJumpToNow&Channel=1"
        response_1 = UIFunctions.send_request(endpoint_now)  # Usamos la función send_request con el endpoint

        if not response_1:
            print("No se pudo realizar el 'ReplayJumpToNow' debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión

        time.sleep(0.01)  # Pequeña pausa

        # Step 2: ReplayPlay
        endpoint_play = "api/?Function=ReplayPlay&Channel=1"
        response_2 = UIFunctions.send_request(endpoint_play)  # Usamos la función send_request con el endpoint

        if not response_2:
            print("No se pudo iniciar la reproducción del replay debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión

        print("Replay jumped to now and playback started successfully.")







    

    






    ########################################################################
    ## END - FUNCIONS SIMULATOR
    ########################################################################

    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            #self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: self.close())


    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
