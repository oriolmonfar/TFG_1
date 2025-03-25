
## ==> GUI FILE
from main import *
import requests
import xml.etree.ElementTree as ET
import time
import threading
from PySide2.QtCore import QTimer
from config_manager import *
from PySide2.QtCore import Qt
from bs4 import BeautifulSoup

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
timecodes = load_timecodes_list()
lastmark_index = -1

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
        
    def check_vmix_connection(self):
        """Comprueba la conexión con vMix y actualiza los frames de estado."""
        response = UIFunctions.send_request("api/")  # Comprueba conexión con vMix

        if response:
            # Conectado a vMix: Muestra el frame verde y oculta el rojo
            self.ui.vmix_conn_ok.show()
            self.ui.vmix_conn_no.setStyleSheet("border-radius: 5px; border: 1px solid rgb(0,0,0); background-color: rgb(40, 40, 40);")  # Gris
            
        else:
            # No conectado: Muestra el frame rojo y oculta el verde
            self.ui.vmix_conn_ok.setStyleSheet("border-radius: 5px; border: 1px solid rgb(0,0,0); background-color: rgb(40, 40, 40);")  # Gris
            self.ui.vmix_conn_no.show()
            

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
        global current_clip
        current_clip = load_current_clip()
        if text == "A":
            self.ui.label_pgm.setText(f'PGM : {current_clip}')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,0,0)")
        elif text == "B":
            self.ui.label_pgm.setText(f'PRV : {current_clip}')
            self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
        else: 
            self.ui.label_pgm.setText(f'LINKED A|B : {current_clip}')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,165,0)")
        self.ui.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.ui.contec_acc_actualclip.setText(f"{current_clip}")

        

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
    
    def function_estrella1_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella1)
    
    def function_estrella2_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella2)

    def function_estrella3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella3)

    



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

    def function_lastsearchtc():
        time = load_last_time()
        date = load_last_date()
        endpoint = f"api/?Function=ReplaySetTimecode&Value={date}T{time}0"
        UIFunctions.send_request(endpoint)


    def function_mark():
        """
        Obtiene el timecode actual de la API de vMix y lo añade a la lista de timecodes.
        """
        global timecodes
        timecodes = load_timecodes_list()
        response = UIFunctions.send_request("api/")
        
        if response:
            tree = ET.fromstring(response)
            timecode_element = tree.find(".//timecode")
            timecode = timecode_element.text if timecode_element is not None else "00:00:00"
            timecodes.append(timecode)
            save_timecodes_list(timecodes)
            print(f"Timecode añadido: {timecode}")
        else:
            print("No se pudo obtener el timecode de vMix. Conexión no disponible.")
        
    def function_lastmark():
        """
        Devuelve el último timecode añadido, luego el penúltimo y así sucesivamente.
        Si se han agotado los timecodes, devuelve None.
        """
        global lastmark_index, timecodes
        timecodes = load_timecodes_list()
        
        if not timecodes:
            print("No hay timecodes almacenados.")
            return None
        
        if abs(lastmark_index) <= len(timecodes):
            timecode = timecodes[lastmark_index]
            lastmark_index -= 1
            print(f"Último timecode obtenido: {timecode}")
            UIFunctions.send_request(f"api/?Function=ReplaySetTimecode&Value={timecode}")
            UIFunctions.send_request("api/?Function=ReplayPause&Channel=1")
        else:
            print("No hay más timecodes disponibles.")
        
    def function_reset_lastmark():
        """
        Reinicia la cuenta de los timecodes para que function_lastmark vuelva a empezar desde el último añadido.
        """
        global lastmark_index
        lastmark_index = -1
        print("Se ha reseteado la cuenta de los timecodes.")


    ########################################################################
    ## END - FUNCIONS CONTENT ACCESS
    ########################################################################

    ########################################################################
    ## START - FUNCTIONS CONFIG
    ########################################################################

    def function_clear_marks():
        """
        Vacía la lista de timecodes.
        """
        global timecodes, lastmark_index
        timecodes = []
        save_timecodes_list(timecodes)
        lastmark_index = -1
        print("Lista de timecodes vaciada.")

    ########################################################################
    ## START - FUNCTIONS CONFIG
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
        if clip_mode == True:
            # Intentar enviar la solicitud de reproducción
            response_1 = UIFunctions.send_request("api/?Function=ReplayPlaySelectedEvent&Channel=1")
            if not response_1:
                print("No se pudo ejecutar ReplayPlay. Saltando function_play.")
                return
        else: 
            # Intentar enviar la solicitud de reproducción
            response_1 = UIFunctions.send_request("api/?Function=ReplayPlay&Channel=1")
            if not response_1:
                print("No se pudo ejecutar ReplayPlay. Saltando function_play.")
                return


        # Intentar ajustar la velocidad de reproducción
        response_2 = UIFunctions.send_request("api/?Function=ReplaySetSpeed&Value=1&Channel=1")
        if not response_2:
            print("No se pudo ajustar la velocidad de reproducción.")

    def function_fastjog(dial):
        """Cambia entre modo normal (1 frame) y modo rápido (50 frames)."""
        FAST_JOG = load_fast_jog()
        dial.fast_mode = not dial.fast_mode
        mode = f"RÁPIDO ({FAST_JOG})" if dial.fast_mode else "NORMAL (1 frame)"
        print(f"Modo cambiado a: {mode}")

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

    #function PAGE declarada en main.py

    def function_prvctl(self):
        global current_clip
        current_clip = load_current_clip()
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
                    self.ui.label_pgm.setText(f'PRV : {current_clip}')
                    self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
                else:
                    self.ui.label_pgm.setText(f'PGM : {current_clip}')
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
    
    """"
    def function_out():
        
        # Endpoint para la función 'ReplayMarkOut'
        endpoint = "api/?Function=ReplayMarkOut"
        
        # Usamos UIFunctions.send_request para realizar la solicitud
        response = UIFunctions.send_request(endpoint)
        
        if not response:
            print("No se pudo marcar el 'Out' debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        # guardar clip a F
        
        # id++

        print("Replay mark 'Out' set successfully.")

    """

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

        time.sleep(0.2)  # Pequeña pausa

        # Step 2: ReplayPlay
        endpoint_play = "api/?Function=ReplayPlay&Channel=1"
        response_2 = UIFunctions.send_request(endpoint_play)  # Usamos la función send_request con el endpoint


        if not response_2:
            print("No se pudo iniciar la reproducción del replay debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        
        #Activar live si no esta activado 
        check_live = UIFunctions.send_request("api/")  # Usamos send_request con el endpoint de la API
        
        if not check_live:
            print("No se pudo obtener el XML debido a la falta de conexión con vMix.")
            return None  # Salimos de la función si no hay conexión

        # Paso 2: Parsear el XML
        try:
            root = ET.fromstring(check_live)  # Convertimos el texto XML en una estructura de árbol
        except ET.ParseError as e:
            print(f"Error al parsear el XML: {e}")
            return None  # Salimos si hay un error en el XML

        UIFunctions.function_reset_lastmark()
        # Paso 3: Iterar sobre todos los inputs y buscar el 'channelMode' en la sección de Replay
        result = None  # Inicializamos result como None por si no encontramos nada
        
        for input_element in root.findall(".//input"):
            replay_element = input_element.find('replay')
            
            if replay_element is not None:
                channel_mode = replay_element.get('live')
                if channel_mode:
                    result = channel_mode  # Guardamos el modo de canal encontrado

        if result == "False":
            time.sleep(0.2)
            endpoint_live = "api/?Function=ReplayLiveToggle"
            response_3 = UIFunctions.send_request(endpoint_live)
            if not response_3:
                print("No se pudo realizar el 'ReplayLiveToogle' debido a la falta de conexión con vMix.")
                return  # Salir si no hay conexión
        else: 
            print("Live already activated")

        # Desactivar clip_mode
        global clip_mode
        clip_mode = False  # Desactivamos el modo clip
        print(f"Modo clip desactivado: Clip_mode: {clip_mode}")

        # Guardar la configuración
        save_config("clip_mode", clip_mode)
        print("Configuración de clip_mode guardada.")  # Confirmación de guardado

        print("Replay jumped to now and playback started successfully.")




    #Gestio clips: 

    def show_dialog_overwrite_clip(self, clip_code, clip_management):
        self.popup = PopupOverwriteClip(clip_code, clip_management)
        self.popup.exec_()

    def get_tc_clip():
        # Paso 1: Hacer una llamada a la API de vMix para obtener el directorio del preset
        response_text = UIFunctions.send_request("api/")
        
        if not response_text:
            print("Error al obtener datos de la API de vMix")
            return None, None  # Devolver None si no hay respuesta de la API

        soup = BeautifulSoup(response_text, "lxml-xml")  # Usar lxml-xml para XML
        preset_path_tag = soup.find("preset")
        
        if not preset_path_tag or not preset_path_tag.text:
            print("No se pudo encontrar el directorio del preset en la respuesta de la API.")
            return None, None  # Devolver None si no se encuentra el directorio del preset

        preset_directory = os.path.dirname(preset_path_tag.text)  # Extraer el directorio base

        # Paso 2: Buscar el archivo replay2.xml en el directorio del preset
        replay_file_path = os.path.join(preset_directory, "replay2.xml")

        if not os.path.exists(replay_file_path):
            print(f"No se encontró el archivo {replay_file_path}")
            return None, None  # Devolver None si no se encuentra el archivo replay2.xml

        # Paso 3: Extraer el primer "segment" y su "time_stamp"
        with open(replay_file_path, "r", encoding="utf-8") as file:
            xml_content = file.read()

        soup = BeautifulSoup(xml_content, "lxml-xml")  # Usar lxml-xml para XML
        segment = soup.find("segment")

        if not segment:
            print("No se encontró el elemento 'segment' en el archivo XML.")
            return None, None  # Devolver None si no se encuentra el segmento

        # Acceder al contenido de la etiqueta <timestamp>
        timestamp_tag = segment.find("timestamp")
        if not timestamp_tag:
            print("No se encontró la etiqueta 'timestamp' dentro del 'segment'.")
            return None, None  # Devolver None si no se encuentra la etiqueta 'timestamp'

        time_stamp = timestamp_tag.text  # Obtener el texto de la etiqueta <timestamp>
        
        # Eliminar los últimos 10 caracteres
        truncated_time_stamp = time_stamp[:-10]  # Elimina los últimos 10 caracteres
        print(f"Time Stamp encontrado: {truncated_time_stamp}")
        
        # Devolver tanto el truncated_time_stamp como el replay_file_path
        return truncated_time_stamp, replay_file_path
    
    
    def get_event_in_out_points(xml_file_path, event_id):
        """
        Busca el evento con el id proporcionado en el archivo XML y obtiene sus puntos inPoint y outPoint.
        
        :param xml_file_path: Ruta del archivo XML donde se encuentran los eventos.
        :param event_id: ID del evento que se busca (es un int).
        :return: Una tupla con los valores de inPoint y outPoint, o None si no se encuentra el evento.
        """
        try:
            # Leer el archivo XML
            with open(xml_file_path, "r", encoding="utf-8") as file:
                xml_content = file.read()

            # Parsear el contenido XML
            soup = BeautifulSoup(xml_content, "lxml-xml")
            
            # Buscar todos los eventos en el archivo
            events = soup.find_all("event")
            
            # Buscar el evento con el ID proporcionado
            for event in events:
                event_id_tag = event.find("id")
                if event_id_tag and int(event_id_tag.text) == event_id:
                    # Encontrar los puntos inPoint y outPoint
                    in_point = event.find("inPoint")
                    print(in_point)
                    out_point = event.find("outPoint")
                    print(out_point)
                    
                    if in_point and out_point:
                        # Devolver los puntos encontrados como tupla
                        return int(in_point.text), int(out_point.text)
                    
            
            # Si no se encuentra el evento, devolver None
            print(f"No se encontró el evento con ID {event_id}.")
            return None
        except Exception as e:
            print(f"Error al procesar el archivo XML: {e}")
            return None
        
    def add_point_to_timestamp(truncated_time_stamp, in_point, out_point):
        """
        Suma los puntos de entrada (in_point) y salida (out_point) en segundos al truncated_time_stamp 
        y devuelve los nuevos timecodes correspondientes.
        
        :param truncated_time_stamp: El timestamp truncado en formato 'YYYY-MM-DDTHH:MM:SS.MS'.
        :param in_point: Punto de entrada en segundos a sumar (opcional).
        :param out_point: Punto de salida en segundos a sumar (opcional).
        :return: Nuevos timecodes para in_point y out_point en formato 'YYYY-MM-DDTHH:MM:SS.MS'.
        """
        
        # Separar la fecha (YYYY-MM-DD) y el tiempo (HH:MM:SS.MS)
        date_str, time_str = truncated_time_stamp.split('T')

        in_point_sec = in_point /10000000

        out_point_sec = out_point/10000000

        dur = out_point_sec - in_point_sec

        print(dur)
        
        # Convertir el tiempo a un objeto datetime
        time_obj = datetime.strptime(time_str, "%H:%M:%S.%f")
        
        # Convertir el tiempo a segundos
        time_in_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1000000.0
        
        # Inicializar los timecodes de salida
        clip_in_tc = None
        clip_out_tc = None
        
        # Si hay in_point, sumarlo al tiempo en segundos
        if in_point is not None:
            new_in_time_in_seconds = time_in_seconds + in_point_sec
            clip_in_tc = str(timedelta(seconds=new_in_time_in_seconds))

        # Si hay out_point, sumarlo al tiempo en segundos
        if out_point is not None:
            new_out_time_in_seconds = time_in_seconds + out_point_sec
            clip_out_tc = str(timedelta(seconds=new_out_time_in_seconds))
        
        # Convertir a formato de hora:minuto:segundo:milisegundo
        def convert_to_time_format(seconds):
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int((seconds - int(seconds)) * 1000):03}"
        
        # Si se ha calculado el clip_in_tc, darle formato
        if clip_in_tc:
            clip_in_tc = convert_to_time_format(new_in_time_in_seconds)
        
        # Si se ha calculado el clip_out_tc, darle formato
        if clip_out_tc:
            clip_out_tc = convert_to_time_format(new_out_time_in_seconds)
        
        # Crear los nuevos timecodes completos (fecha + nuevos tiempos)
        if clip_in_tc:
            clip_in_tc = f"{date_str}T{clip_in_tc}"
            print(clip_in_tc)
        
        if clip_out_tc:
            clip_out_tc = f"{date_str}T{clip_out_tc}"
            print(clip_out_tc)
        
        return clip_in_tc, clip_out_tc, dur








    

    






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
