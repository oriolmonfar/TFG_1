
# GUI FILE
from main import *
import requests
import xml.etree.ElementTree as ET
import time
from PySide2.QtCore import QTimer
from config_manager import *
from PySide2.QtCore import Qt


#DECLARE GLOBAL VARIABLES
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
timecodes = load_timecodes_list()
lastmark_index = -1

# COUNT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    # GLOBALS
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

    def check_modo_playlist(self):
        global modo_playlist
        if modo_playlist == True:
            self.ui.sim_loop.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; background-color: red; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        elif modo_loop == True:
            self.ui.sim_loop.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: green; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        else:
            self.ui.sim_loop.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")

    def start_connection_monitor(main_window):
        """Inicia un temporizador para monitorear la conexión con vMix."""
        main_window.timer = QTimer(main_window)
        main_window.timer.timeout.connect(lambda: UIFunctions.check_vmix_connection(main_window))
        main_window.timer.start(5000)  # Ejecuta cada 5 segundos

    def start_modo_playlist_monitor(main_window):
        global modo_playlist, modo_loop
        """Inicia un temporizador para monitorear la conexión con vMix."""
        main_window.timer = QTimer(main_window)
        main_window.timer.timeout.connect(lambda: UIFunctions.check_modo_playlist(main_window))
        print(f"connection checked, modo playlist: {modo_playlist}, modo loop: {modo_loop}")
        main_window.timer.start(500)  # Ejecuta cada 5 segundos


    def get_vmix_replay_cameras():
        """
        Obtiene cameraA y cameraB del input tipo replay en vMix.

        Retorna:
            tuple: (cameraA, cameraB) si se encuentra el input tipo replay,
                o (None, None) si no se encuentra o hay error.
        """
        try:
            # Solicita el XML usando send_request
            xml_data = UIFunctions.send_request("api/")
            if xml_data is None:
                return None, None

            # Parsear el XML
            root = ET.fromstring(xml_data)

            # Buscar input de tipo 'Replay'
            for input_elem in root.findall('inputs/input'):
                if input_elem.get('type') == 'Replay':
                    replay_elem = input_elem.find('replay')
                    if replay_elem is not None:
                        cameraA = replay_elem.get('cameraA')
                        cameraB = replay_elem.get('cameraB')

            if cameraA == "1":
                angleA = "A"
            elif cameraA == "2":
                angleA = "B"
            elif cameraA == "3":
                angleA = "C"
            elif cameraA == "4":
                angleA = "D"
            
            if cameraB == "1":
                angleB = "A"
            elif cameraB == "2":
                angleB = "B"
            elif cameraB == "3":
                angleB = "C"
            elif cameraB == "4":
                angleB = "D"

        
            return angleA, angleB

        except Exception as e:
            print(f"Error al procesar XML de vMix: {e}")
            return None, None
        
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

    #Maximize - Restore
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

    # Return Status
    def returStatus():
        return GLOBAL_STATE

    #Set State
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    #Enable Maximum Size
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    #Toggle Menu
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

    #Set Title Bar
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    # Label Title
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    #Label Title according to channel mode
    def labelPGM_PRV(self, text):
        global current_clip_pgm, current_clip_prv
        current_clip_pgm = load_current_clip_pgm()
        current_clip_prv = load_current_clip_prv()
        if text == "A":
            self.ui.label_pgm.setText(f'PGM : {current_clip_pgm}')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,0,0)")
        elif text == "B":
            self.ui.label_pgm.setText(f'PRV : {current_clip_prv}')
            self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
            self.ui.sim_prvctl.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white; background-color: green; padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        else: 
            self.ui.label_pgm.setText(f'LINKED A|B : {current_clip_pgm}')
            self.ui.label_pgm.setStyleSheet("color: rgb(255,165,0)")
        self.ui.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.ui.contec_acc_actualclip.setText(f"{current_clip_pgm}")

        
    # Label Description
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    #Dynamic Menus
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


    # Select Menu
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    # Deselect menu
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    #Start selection
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    #Reset Selection
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    #Change Page Label Text
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    #User Icon
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
    ## START - VMIX TO EVS FUNCTIONS
    ########################################################################

    ########################################################################
    ## START - FUNCIONS CLIP
    ########################################################################

    def refresh_estrella1_list(self):
        global estrella1
        estrella1 = load_estrella1_list()  # Cargar la lista desde el archivo
        self.ui.list_estrella1.clear()  # Limpiar la QListWidget antes de actualizarla

        updated_estrella1 = []  # Nueva lista actualizada con la información formateada

        clip_data = load_clip_dictionary()  # Cargar el diccionario de clips

        for item in estrella1:
            numeric_code = item[:3]  # Extraer los primeros 3 caracteres

            if numeric_code in clip_data:
                clip_list = clip_data[numeric_code]

                # Extraer información del diccionario con valores por defecto
                name = "No name assigned" if clip_list[1] == "void" else clip_list[1]
                pl = "No Playlist assigned" if clip_list[3] == "void" else clip_list[3]
                tc_in = "No TC IN assigned" if clip_list[4] == "void" else clip_list[4][11:]
                tc_out = "No TC OUT assigned" if clip_list[5] == "void" else clip_list[5][11:]
                dur = "No duration assigned" if clip_list[6] == "void" else clip_list[6]

                # Crear string formateado con la información
                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"

                # Añadir a la lista actualizada
                updated_estrella1.append(clip_info)

                # Añadir el nuevo elemento a la QListWidget
                self.ui.list_estrella1.addItem(clip_info)

        # Guardar la lista actualizada
        estrella1 = updated_estrella1
        save_estrella1_list(estrella1)

    def refresh_estrella2_list(self):
        global estrella2
        estrella2 = load_estrella2_list()  # Cargar la lista desde el archivo
        self.ui.list_estrella2.clear()  # Limpiar la QListWidget antes de actualizarla

        updated_estrella2 = []  # Nueva lista actualizada con la información formateada

        clip_data = load_clip_dictionary()  # Cargar el diccionario de clips

        for item in estrella2:
            numeric_code = item[:3]  # Extraer los primeros 3 caracteres

            if numeric_code in clip_data:
                clip_list = clip_data[numeric_code]

                # Extraer información del diccionario con valores por defecto
                name = "No name assigned" if clip_list[1] == "void" else clip_list[1]
                pl = "No Playlist assigned" if clip_list[3] == "void" else clip_list[3]
                tc_in = "No TC IN assigned" if clip_list[4] == "void" else clip_list[4][11:]
                tc_out = "No TC OUT assigned" if clip_list[5] == "void" else clip_list[5][11:]
                dur = "No duration assigned" if clip_list[6] == "void" else clip_list[6]

                # Crear string formateado con la información
                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"

                # Añadir a la lista actualizada
                updated_estrella2.append(clip_info)

                # Añadir el nuevo elemento a la QListWidget
                self.ui.list_estrella2.addItem(clip_info)

        # Guardar la lista actualizada
        estrella2 = updated_estrella2
        save_estrella2_list(estrella2)

    def refresh_estrella3_list(self):
        global estrella3
        estrella3 = load_estrella3_list()  # Cargar la lista desde el archivo
        self.ui.list_estrella3.clear()  # Limpiar la QListWidget antes de actualizarla

        updated_estrella3 = []  # Nueva lista actualizada con la información formateada

        clip_data = load_clip_dictionary()  # Cargar el diccionario de clips

        for item in estrella3:
            numeric_code = item[:3]  # Extraer los primeros 3 caracteres

            if numeric_code in clip_data:
                clip_list = clip_data[numeric_code]

                # Extraer información del diccionario con valores por defecto
                name = "No name assigned" if clip_list[1] == "void" else clip_list[1]
                pl = "No Playlist assigned" if clip_list[3] == "void" else clip_list[3]
                tc_in = "No TC IN assigned" if clip_list[4] == "void" else clip_list[4][11:]
                tc_out = "No TC OUT assigned" if clip_list[5] == "void" else clip_list[5][11:]
                dur = "No duration assigned" if clip_list[6] == "void" else clip_list[6]

                # Crear string formateado con la información
                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"

                # Añadir a la lista actualizada
                updated_estrella3.append(clip_info)

                # Añadir el nuevo elemento a la QListWidget
                self.ui.list_estrella3.addItem(clip_info)

        # Guardar la lista actualizada
        estrella3 = updated_estrella3
        save_estrella3_list(estrella3)

    def function_estrella1(self):
        global current_clip, estrella1
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]

        try:
            # Cargar el clip_dictionary.json usando la función ya definida
            clip_data = load_clip_dictionary()

            # Verificar si el código numérico existe en el diccionario
            if numeric_code in clip_data:
                # Obtener la lista correspondiente a ese código numérico
                clip_list = clip_data[numeric_code]
                
                # Escribir "*" en la tercera posición (índice 2)
                clip_list[2] = "*"
                
                # Guardar los cambios en el archivo clip_dictionary.json usando la función ya definida
                save_clip_dictionary(clip_data)

                if clip_list[1]== "void":
                    name = "No name assigned"
                else: 
                    name = clip_list[1]

                if clip_list[3]== "void":
                    pl = "No Playlist assigned"
                else: 
                    pl = clip_list[3]

                if clip_list[4]== "void":
                    tc_in = "No TC IN assigned"
                else: 
                    tc_in = clip_list[4][11:]

                if clip_list[5]== "void":
                    tc_out = "No TC OUT assigned"
                else: 
                    tc_out = clip_list[5][11:]

                if clip_list[6]== "void":
                    dur = "No duration assigned"
                else: 
                    dur = clip_list[6]
                
                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"

                # Añadir el numeric_code a la QListWidget

                self.ui.list_estrella1.addItem(clip_info)
                estrella1 = load_estrella1_list()
                estrella1.append(clip_info)
                save_estrella1_list(estrella1)

                print(f"Se ha actualizado el código {clip_info} en clip_dictionary.json y añadido a la lista.")
            else:
                print(f"El código {clip_info} no existe en el archivo clip_dictionary.json.")

        except FileNotFoundError:
            print("Error: El archivo clip_dictionary.json no existe.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el archivo tiene el formato correcto.")

    def function_estrella2(self):
        global current_clip, estrella2
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]

        try:
            # Cargar el clip_dictionary.json usando la función ya definida
            clip_data = load_clip_dictionary()

            # Verificar si el código numérico existe en el diccionario
            if numeric_code in clip_data:
                # Obtener la lista correspondiente a ese código numérico
                clip_list = clip_data[numeric_code]
                
                # Escribir "*" en la tercera posición (índice 2)
                clip_list[2] = "**"
                
                # Guardar los cambios en el archivo clip_dictionary.json usando la función ya definida
                save_clip_dictionary(clip_data)
                if clip_list[1]== "void":
                    name = "No name assigned"
                else: 
                    name = clip_list[1]

                if clip_list[3]== "void":
                    pl = "No Playlist assigned"
                else: 
                    pl = clip_list[3]

                if clip_list[4]== "void":
                    tc_in = "No TC IN assigned"
                else: 
                    tc_in = clip_list[4][11:]

                if clip_list[5]== "void":
                    tc_out = "No TC OUT assigned"
                else: 
                    tc_out = clip_list[5][11:]

                if clip_list[6]== "void":
                    dur = "No duration assigned"
                else: 
                    dur = clip_list[6]

                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"
                

                # Añadir el numeric_code a la QListWidget

                self.ui.list_estrella2.addItem(clip_info)
                estrella2 = load_estrella2_list()
                estrella2.append(clip_info)
                save_estrella2_list(estrella2)

                print(f"Se ha actualizado el código {clip_info} en clip_dictionary.json y añadido a la lista.")
            else:
                print(f"El código {clip_info} no existe en el archivo clip_dictionary.json.")

        except FileNotFoundError:
            print("Error: El archivo clip_dictionary.json no existe.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el archivo tiene el formato correcto.")

    def function_estrella3(self):
        global current_clip, estrella3
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]

        try:
            # Cargar el clip_dictionary.json usando la función ya definida
            clip_data = load_clip_dictionary()

            # Verificar si el código numérico existe en el diccionario
            if numeric_code in clip_data:
                # Obtener la lista correspondiente a ese código numérico
                clip_list = clip_data[numeric_code]
                
                # Escribir "*" en la tercera posición (índice 2)
                clip_list[2] = "***"
                
                # Guardar los cambios en el archivo clip_dictionary.json usando la función ya definida
                save_clip_dictionary(clip_data)

                if clip_list[1]== "void":
                    name = "No name assigned"
                else: 
                    name = clip_list[1]

                if clip_list[3]== "void":
                    pl = "No Playlist assigned"
                else: 
                    pl = clip_list[3]

                if clip_list[4]== "void":
                    tc_in = "No TC IN assigned"
                else: 
                    tc_in = clip_list[4][11:]

                if clip_list[5]== "void":
                    tc_out = "No TC OUT assigned"
                else: 
                    tc_out = clip_list[5][11:]

                if clip_list[6]== "void":
                    dur = "No duration assigned"
                else: 
                    dur = clip_list[6]
                

                clip_info = f"{current_clip},   {name},   {pl},   {tc_in},   {tc_out},   {dur}"
                

                # Añadir el numeric_code a la QListWidget

                self.ui.list_estrella3.addItem(clip_info)
                estrella3 = load_estrella3_list()
                estrella3.append(clip_info)
                save_estrella3_list(estrella3)

                print(f"Se ha actualizado el código {clip_info} en clip_dictionary.json y añadido a la lista.")
            else:
                print(f"El código {clip_info} no existe en el archivo clip_dictionary.json.")

        except FileNotFoundError:
            print("Error: El archivo clip_dictionary.json no existe.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el archivo tiene el formato correcto.")
        
    def remove_estrella1(self):
        global estrella1
        selected_item = self.ui.list_estrella1.currentItem()  # Obtener el ítem seleccionado
        
        if selected_item:  # Verificar que hay un ítem seleccionado
            item_text = selected_item.text()  # Obtener el texto del elemento
            self.ui.list_estrella1.takeItem(self.ui.list_estrella1.row(selected_item))  # Eliminar el ítem

            if item_text in estrella1:  # Verificar si está en la lista estrella1
                estrella1.remove(item_text)  # Eliminar de la lista estrella1
                print(f"Elemento '{selected_item.text()}' eliminado de la lista.")
                save_estrella1_list(estrella1)
        else:
            print("No hay ningún elemento seleccionado para eliminar.")

    def remove_estrella2(self):
        global estrella2
        selected_item = self.ui.list_estrella2.currentItem()  # Obtener el ítem seleccionado
        
        if selected_item:  # Verificar que hay un ítem seleccionado
            item_text = selected_item.text()  # Obtener el texto del elemento
            self.ui.list_estrella2.takeItem(self.ui.list_estrella2.row(selected_item))  # Eliminar el ítem

            if item_text in estrella2:  # Verificar si está en la lista estrella1
                estrella2.remove(item_text)  # Eliminar de la lista estrella1
                print(f"Elemento '{selected_item.text()}' eliminado de la lista.")
                save_estrella2_list(estrella2)
        else:
            print("No hay ningún elemento seleccionado para eliminar.")

    def remove_estrella3(self):
        global estrella3
        selected_item = self.ui.list_estrella3.currentItem()  # Obtener el ítem seleccionado
        
        if selected_item:  # Verificar que hay un ítem seleccionado
            item_text = selected_item.text()  # Obtener el texto del elemento
            self.ui.list_estrella3.takeItem(self.ui.list_estrella3.row(selected_item))  # Eliminar el ítem

            if item_text in estrella3:  # Verificar si está en la lista estrella1
                estrella3.remove(item_text)  # Eliminar de la lista estrella1
                print(f"Elemento '{selected_item.text()}' eliminado de la lista.")
                save_estrella3_list(estrella3)
        else:
            print("No hay ningún elemento seleccionado para eliminar.")
        
    
    def function_estrella1_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella1)
        UIFunctions.refresh_estrella1_list(self)
    
    def function_estrella2_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella2)
        UIFunctions.refresh_estrella2_list(self)

    def function_estrella3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_estrella3)
        UIFunctions.refresh_estrella3_list(self)

    def clip_gotopl(self):
        global active_playlist
        active_playlist = load_active_playlist()
        num = active_playlist[2:]
        print(num)
        UIFunctions.add_to_playlist(self, num)
        UIFunctions.goto_pl(self, num)

    ########################################################################
    ## END - FUNCIONS CLIP
    ########################################################################

    ########################################################################
    ## START - FUNCIONS CONTENT ACCESS
    ########################################################################

    def cont_acc_gotopl(self):
        global active_playlist
        active_playlist = load_active_playlist()
        num = active_playlist[-1]
        UIFunctions.goto_pl(self, num)

    def function_lasttc():
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
    ## START - FUNCIONS CONTROL
    ########################################################################

    def function_fastjog(self, dial):
        """Cambia entre modo normal (1 frame) y modo rápido (50 frames)."""
        FAST_JOG = load_fast_jog()
        dial.fast_mode = not dial.fast_mode
        dial.super_fast_mode = False
        mode = f"RÁPIDO ({FAST_JOG})" if dial.fast_mode else "NORMAL (1 frame)"
        if dial.fast_mode:
            self.ui.sim_fastjog.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: green; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}") 
        else:
            self.ui.sim_fastjog.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        print(f"Modo cambiado a: {mode}")

    def function_sec_fastjog(self, dial):
        """Cambia entre modo normal (1 frame) y modo super rápido (100 frames)."""
        SEC_FAST_JOG = load_sec_fast_jog()
        dial.super_fast_mode = not dial.super_fast_mode
        dial.fast_mode = False
        mode = f"RÁPIDO ({SEC_FAST_JOG})" if dial.super_fast_mode else "NORMAL (1 frame)"
        if dial.super_fast_mode:
            self.ui.sim_fastjog.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: red; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}") 
        else:
            self.ui.sim_fastjog.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        print(f"Modo cambiado a: {mode}")

    def function_syncprv(self):
        """ Sincroniza la vista previa en vMix Replay seleccionando los canales A y B. """
        response = UIFunctions.send_request("api/?Function=ReplaySelectChannelAB")
        
        if response is None:
            return  # Si no hay conexión, salir de la función
        
        UIFunctions.labelPGM_PRV(self, "A|B")

    def function_prvctl(self):
        global current_clip_pgm, current_clip_prv
        current_clip_pgm = load_current_clip_pgm()
        current_clip_prv = load_current_clip_prv()
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
                    self.ui.label_pgm.setText(f'PRV : {current_clip_prv}')
                    self.ui.label_pgm.setStyleSheet("color: rgb(0,255,0)")
                    self.ui.sim_prvctl.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white; background-color: green; padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                else:
                    self.ui.label_pgm.setText(f'PGM : {current_clip_pgm}')
                    self.ui.label_pgm.setStyleSheet("color: rgb(255,0,0)")
                    self.ui.sim_prvctl.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white; padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")

        except ET.ParseError:
            print("Error parsing XML response from vMix")

    def function_loop(self):
        global modo_loop
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
                    modo_loop = False
                    response = UIFunctions.send_request(f"api/?Function=LoopOff&Input={key}")
                    self.ui.sim_loop.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                    print(f"Loop desactivado en {key}") if response else print("Error al desactivar loop")
                else:
                    modo_loop = True
                    response = UIFunctions.send_request(f"api/?Function=LoopOn&Input={key}")
                    self.ui.sim_loop.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: green; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                    print(f"Loop activado en {key}") if response else print("Error al activar loop")

                return  # Salir tras encontrar y procesar el primer input "Replay"

        print("No se encontró ningún input con type='Replay'.")

    def function_gotoin():
        global current_clip
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]
        try:
            # Cargar el clip_dictionary.json usando la función ya definida
            clip_data = load_clip_dictionary()
            

            # Verificar si el código numérico existe en el diccionario
            if numeric_code in clip_data:
                # Obtener la lista correspondiente a ese código numérico
                clip_list = clip_data[numeric_code]
                
                # Escribir "*" en la tercera posición (índice 2)
                tc_in = clip_list[4]
                endpoint_1 = f"api/?Function=ReplaySetTimecode&Value={tc_in}"
                endpoint_2 = "api/?Function=ReplayPause&Channel=1"
                UIFunctions.send_request(endpoint_1)
                UIFunctions.send_request(endpoint_2)

        except FileNotFoundError:
            print("Error: El archivo clip_dictionary.json no existe.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el archivo tiene el formato correcto.")

    def function_gotoout():
        global current_clip
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]
        try:
            # Cargar el clip_dictionary.json usando la función ya definida
            clip_data = load_clip_dictionary()
            

            # Verificar si el código numérico existe en el diccionario
            if numeric_code in clip_data:
                # Obtener la lista correspondiente a ese código numérico
                clip_list = clip_data[numeric_code]
                
                # Escribir "*" en la tercera posición (índice 2)
                tc_out = clip_list[5]
                endpoint_1 = f"api/?Function=ReplaySetTimecode&Value={tc_out}"
                endpoint_2 = "api/?Function=ReplayPause&Channel=1"
                UIFunctions.send_request(endpoint_1)
                UIFunctions.send_request(endpoint_2)

        except FileNotFoundError:
            print("Error: El archivo clip_dictionary.json no existe.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el archivo tiene el formato correcto.")

    def function_gototc(self):
        self.show_dialog_searchtc()

    def function_cancel_in(self):
        global clip_id
        UIFunctions.send_request("api/?Function=ReplayMarkCancel")
        clip_id = load_current_clip_id()
        clip_id +=1
        save_current_clip_id(clip_id)
        self.ui.sim_in.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
               



    ########################################################################
    ## END - FUNCIONS CONTROL
    ########################################################################


    ########################################################################
    ## START - FUNCTIONS EXPORT
    ########################################################################

    def export_playlist():
        active_playlist = load_active_playlist()
        plst_num = active_playlist[-1]
        event = int(plst_num) + 1
        print(event)
        endpoint_1 = f"api/?Function=ReplaySelectEvents{event}&Channel=1"
        UIFunctions.send_request(endpoint_1)
        try:
            # Paso 1: Hacer la solicitud a la API de vMix
            response_text = UIFunctions.send_request("api/")  # Reemplaza esto con la URL correcta si es necesario
            if response_text is None:
                print("Error al hacer la solicitud a la API de vMix")
                return
            
            # Paso 2: Parsear el XML de la respuesta usando ET
            root = ET.fromstring(response_text)

            # Buscar la etiqueta <preset> y extraer el valor
            preset_tag = root.find(".//preset")
            if preset_tag is not None:
                preset_path = preset_tag.text

                # Paso 3: Extraer el directorio de la ruta del preset
                base_directory = os.path.dirname(preset_path)

                # Paso 4: Añadir el directorio "export"
                export_directory = os.path.join(base_directory, "export")

                # Paso 5: Crear la carpeta "playlistX" dentro de "export", donde X es active_playlist
                playlist_folder = os.path.join(export_directory, f"playlist{plst_num}")
                os.makedirs(playlist_folder, exist_ok=True)

                print(f"Directorio creado: {playlist_folder}")

                # Paso 6: Hacer la siguiente solicitud a la API de vMix para exportar el evento
                export_url = f"api/?Function=ReplayExportLastEvent&Value={playlist_folder}&Channel=1"
                
                # Utilizar UIFunctions.send_request para realizar la solicitud
                export_response_text = UIFunctions.send_request(export_url)

                if export_response_text is not None:
                    print(f"Exportación de evento realizada en {playlist_folder}")
                else:
                    print(f"Error al hacer la solicitud de exportación")
            else:
                print("No se encontró la etiqueta <preset> en la respuesta XML.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")


    def export_clip():
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]

        clip_data = load_clip_dictionary()
        clip_id = load_current_clip_id()
        clip_list = clip_data.get(numeric_code, ["void"] * 7)
        id = int(clip_list[0])
         
        endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
        endpoint_2 =  "api/?Function=ReplaySelectNextEvent&Channel=1"

        endpoint_3 = "api/?Function=ReplayCopySelectedEvent&Value=19"
        endpoint_4 = "api/?Function=ReplaySelectEvents20&Channel=1"
     

    
        UIFunctions.send_request(endpoint_1)

        for _ in range(id):
            UIFunctions.send_request(endpoint_2)

        time.sleep(0.2)    
        UIFunctions.send_request(endpoint_3)
        time.sleep(0.2)
        UIFunctions.send_request(endpoint_4)
        time.sleep(0.2)
        UIFunctions.send_request(endpoint_1)
        time.sleep(0.2)

        clip_id += 1
        save_current_clip_id(clip_id)

        try:
            # Paso 1: Hacer la solicitud a la API de vMix
            response_text = UIFunctions.send_request("api/")  # Reemplaza esto con la URL correcta si es necesario
            if response_text is None:
                print("Error al hacer la solicitud a la API de vMix")
                return
            
            # Paso 2: Parsear el XML de la respuesta usando ET
            root = ET.fromstring(response_text)

            # Buscar la etiqueta <preset> y extraer el valor
            preset_tag = root.find(".//preset")
            if preset_tag is not None:
                preset_path = preset_tag.text

                # Paso 3: Extraer el directorio de la ruta del preset
                base_directory = os.path.dirname(preset_path)

                # Paso 4: Añadir el directorio "export"
                export_directory = os.path.join(base_directory, "export")

                # Paso 5: Crear la carpeta "playlistX" dentro de "export", donde X es active_playlist
                clip_folder = os.path.join(export_directory, f"{current_clip}")
                os.makedirs(clip_folder, exist_ok=True)

                print(f"Directorio creado: {current_clip}")

                # Paso 6: Hacer la siguiente solicitud a la API de vMix para exportar el evento
                export_url = f"api/?Function=ReplayExportLastEvent&Value={clip_folder}&Channel=1"
                
                # Utilizar UIFunctions.send_request para realizar la solicitud
                export_response_text = UIFunctions.send_request(export_url)

                if export_response_text is not None:
                    print(f"Exportación de evento realizada en {clip_folder}")
                else:
                    print(f"Error al hacer la solicitud de exportación")
            else:
                print("No se encontró la etiqueta <preset> en la respuesta XML.")

        except Exception as e:
            print(f"Ocurrió un error: {e}")


    ########################################################################
    ## END - FUNCTIONS EXPORT
    ########################################################################



    ########################################################################
    ## START - FUNCTIONS PLAYLIST
    ########################################################################

    def add_to_playlist(self, plst_num):
        global current_clip, clip_id

        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]
        endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
        endpoint_2 = "api/?Function=ReplaySelectNextEvent&Channel=1"
        UIFunctions.send_request(endpoint_1)

        try:
            with open(CLIP_DICTIONARY_FILE, "r") as file:
                clip_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: El archivo {CLIP_DICTIONARY_FILE} no existe.")
            return None

        clip_list = clip_data.get(numeric_code, ["void"] * 7)

        if clip_list[0] == "void":
            print("No hay ningún clip asignado.")
            return None

        new_playlist = f"PL{plst_num}"

        # Añadir la nueva playlist al campo correspondiente del clip
        if clip_list[3] == "void":
            clip_list[3] = new_playlist
        else:
            if clip_list[3].startswith("{") and clip_list[3].endswith("}"):
                existing_playlists = [pl.strip() for pl in clip_list[3][1:-1].split(",")]
            else:
                existing_playlists = [clip_list[3].strip()]

            if new_playlist not in existing_playlists:
                existing_playlists.append(new_playlist)

            if len(existing_playlists) == 1:
                clip_list[3] = existing_playlists[0]
            else:
                clip_list[3] = "{" + ", ".join(existing_playlists) + "}"

        # Construir la información del clip actualizada
        name = clip_list[1] if clip_list[1] != "void" else "No name assigned"
        rank = clip_list[2] if clip_list[2] != "void" else "No ranking assigned"
        tc_in = clip_list[4][11:] if clip_list[4] != "void" else "No TC IN assigned"
        tc_out = clip_list[5][11:] if clip_list[5] != "void" else "No TC OUT assigned"
        dur = clip_list[6] if clip_list[6] != "void" else "No duration assigned"

        clip_info = f"{current_clip},  {name},   {rank}, {clip_list[3]},  {tc_in},   {tc_out},   {dur}"

        # Actualizar la QListWidget actual y guardar en la playlist correspondiente
        list_name = f"list_pl{plst_num}"
        list_widget = getattr(self.ui, list_name, None)
        if list_widget:
            list_widget.addItem(clip_info)

        # Guardar el clip en la lista persistente
        playlist_data = load_plst(plst_num)
        playlist_data.append(clip_info)
        save_plst(plst_num, playlist_data)


        # Actualizar otras playlists en las que ya estaba este clip
        if clip_list[3].startswith("{") and clip_list[3].endswith("}"):
            playlists = [pl.strip() for pl in clip_list[3][1:-1].split(",")]
        else:
            playlists = [clip_list[3].strip()]

        for pl in playlists:
            pl_number = int(pl.replace("PL", ""))
            if pl_number == plst_num:
                continue  # Ya se ha añadido

            old_data = load_plst(pl_number)
            updated_data = []
            for item in old_data:
                if item.startswith(current_clip):
                    updated_data.append(clip_info)
                else:
                    updated_data.append(item)
            save_plst(pl_number, updated_data)

            # También actualizar visualmente en la lista
            other_list_widget = getattr(self.ui, f"list_pl{pl_number}", None)
            if other_list_widget:
                for row in range(other_list_widget.count()):
                    if other_list_widget.item(row).text().startswith(current_clip):
                        other_list_widget.item(row).setText(clip_info)

        # Guardar clip_dictionary actualizado
        save_clip_dictionary(clip_data)

        # Avanzar eventos en vMix
        for _ in range(int(clip_list[0])):
            UIFunctions.send_request(endpoint_2)

        event = plst_num
        endpoint_3 = f"api/?Function=ReplayCopySelectedEvent&Value={event}"
        UIFunctions.send_request(endpoint_3)

        clip_id = load_current_clip_id()
        clip_id += 1
        save_current_clip_id(clip_id)

        UIFunctions.dur_playlist(self, plst_num)
        UIFunctions.num_clips_playlist(self, plst_num)


    def goto_pl(self, page_number):
        UIFunctions.refresh_playlist(self, page_number)
        global active_playlist, modo_playlist
        modo_playlist = True
        pl = f"PL{page_number}"
        save_active_playlist(pl)
        UIFunctions.labelDescription(self, f"PL{page_number}")
        page_name = f"page_pl{page_number}"
        page_widget = getattr(self.ui, page_name, None)  # Obtiene el widget dinámicamente
        active_playlist = load_active_playlist()
        self.ui.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.ui.cont_acc_actualplaylist.setText(f"{active_playlist}") 

        if page_widget:  # Verifica si la página existe
            self.ui.stackedWidget.setCurrentWidget(page_widget)
        else:
            print(f"La página {page_name} no existe.")

    def restore_all_playlists_on_startup(self):
        total_playlists = 18  # Cambia este número según cuántas playlists tengas

        for plst_num in range(1, total_playlists + 1):
            list_name = f"list_pl{plst_num}"
            list_widget = getattr(self.ui, list_name, None)
            UIFunctions.dur_playlist(self, plst_num)
            UIFunctions.num_clips_playlist(self, plst_num)

            if list_widget is not None:
                list_widget.clear()  # Limpiar por si ya tenía elementos

                saved_playlist = load_plst(plst_num)

                for item in saved_playlist:
                    list_widget.addItem(item)

            else:
                print(f"Advertencia: No se encontró QListWidget con el nombre '{list_name}'")

        
    def delete_element_plst(self, num_plst):
        """Elimina el clip seleccionado de la QListWidget, de la lista de la playlist, del clip_dictionary, y realiza la eliminación en vMix."""

        list_widget = getattr(self.ui, f"list_pl{num_plst}", None)
        if not list_widget:
            print(f"No se encontró list_pl{num_plst}")
            return

        selected_item = list_widget.currentItem()
        if not selected_item:
            print("No hay ningún item seleccionado.")
            return

        # 1. Obtener el texto del elemento seleccionado
        clip_info = selected_item.text()
        current_clip = clip_info.split(",")[0].strip()
        numeric_code = current_clip[:3]

        # 2. Eliminar del QListWidget
        list_widget.takeItem(list_widget.row(selected_item))

        # 3. Eliminar de la lista global
        pl_list_name = f"playlist{num_plst}"
        pl_list = globals().get(pl_list_name, [])
        
        # Eliminar solo el clip seleccionado de la lista, sin eliminar todos los clips con el mismo código
        updated_pl_list = [clip for clip in pl_list if clip.split(",")[0].strip() != current_clip]

        # ✅ Actualizar lista global
        globals()[pl_list_name] = updated_pl_list

        # ✅ Guardar la lista en archivo
        save_plst(num_plst, updated_pl_list)

        # 4. Eliminar la playlist del campo del clip en el diccionario
        clip_data = load_clip_dictionary()
        if numeric_code in clip_data:
            clip_entry = clip_data[numeric_code]
            playlist_field = clip_entry[3]

            if playlist_field.startswith("{") and playlist_field.endswith("}"):
                playlists = [pl.strip() for pl in playlist_field[1:-1].split(",")]
                if f"PL{num_plst}" in playlists:
                    playlists.remove(f"PL{num_plst}")
                    clip_entry[3] = "{" + ", ".join(playlists) + "}" if playlists else "void"
            elif playlist_field == f"PL{num_plst}":
                clip_entry[3] = "void"

            save_clip_dictionary(clip_data)
            print(f"Se eliminó PL{num_plst} del clip {numeric_code} en clip_dictionary.")
            
            # --- Interacción con vMix ---
            # Obtener el ID del clip para interactuar con vMix
            id_vmix = clip_entry[0].zfill(4)  # Asumimos que clip_entry[0] es el ID de vMix

            # 5. Realizar las solicitudes a vMix
            event = num_plst + 1
            endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
            endpoint_2 = "api/?Function=ReplaySelectNextEvent&Channel=1"
            endpoint_3 = f"api/?Function=ReplaySelectEvents{event}&Channel=1"

            # Seleccionamos el primer evento
            UIFunctions.send_request(endpoint_3)
            UIFunctions.send_request(endpoint_1)

            # Avanzamos hasta el evento con el ID correspondiente
            for _ in range(int(clip_entry[0])):
                UIFunctions.send_request(endpoint_2)


            # Eliminar el evento seleccionado en vMix
            endpoint_4 = f"api/?Function=ReplayDeleteSelectedEvent&Value={id_vmix}&Channel=1"
            UIFunctions.send_request(endpoint_4)

        else:
            print(f"Clip {numeric_code} no encontrado en el diccionario.")

        # 6. Volver a cargar la lista actual desde el archivo para estar seguros
        updated_pl_list_final = load_plst(num_plst)
        globals()[pl_list_name] = updated_pl_list_final  # Aseguramos la sincronización final

        # ✅ Recalcular la duración y el número de clips con la lista ya actualizada
        UIFunctions.dur_playlist(self, num_plst)
        UIFunctions.num_clips_playlist(self, num_plst)

        endpoint_5 = "api/?Function=ReplaySelectEvents1&Channel=1"
        UIFunctions.send_request(endpoint_5)


    def refresh_playlist(self, num_plst):
        """
        Refresca visual y lógicamente la playlist especificada.
        - Actualiza la QListWidget correspondiente.
        - Reconstruye los datos desde el clip_dictionary.
        - Guarda la nueva lista formateada.
        """
        # Acceder a la lista global de la playlist
        pl_list_name = f"playlist{num_plst}"
        pl_list = load_plst(num_plst)  # <-- Cargar desde archivo
        globals()[pl_list_name] = pl_list  # <-- Actualizar variable global

        # Limpiar la QListWidget
        getattr(self.ui, f"list_pl{num_plst}").clear()

        updated_playlist = []
        clip_data = load_clip_dictionary()

        for item in pl_list:
            clip_code = item.split(",")[0].strip()
            numeric_code = clip_code[:3]

            if numeric_code in clip_data:
                clip_list = clip_data[numeric_code]

                # Extraer información con valores por defecto
                name = "No name assigned" if clip_list[1] == "void" else clip_list[1]
                rank = "No rank assigned" if clip_list[2] == "void" else clip_list[2]
                pl = "No Playlist assigned" if clip_list[3] == "void" else clip_list[3]
                tc_in = "No TC IN assigned" if clip_list[4] == "void" else clip_list[4][11:]
                tc_out = "No TC OUT assigned" if clip_list[5] == "void" else clip_list[5][11:]
                dur = "No duration assigned" if clip_list[6] == "void" else clip_list[6]

                # Construir string formateado
                clip_info = f"{clip_code},   {name}, {rank},   {pl},   {tc_in},   {tc_out},   {dur}"

                # Añadir a lista actualizada y widget
                updated_playlist.append(clip_info)
                getattr(self.ui, f"list_pl{num_plst}").addItem(clip_info)

        # Guardar la lista actualizada en la variable global y archivo
        globals()[pl_list_name] = updated_playlist
        save_plst(num_plst, updated_playlist)
        UIFunctions.dur_playlist(self, num_plst)
        UIFunctions.num_clips_playlist(self, num_plst)

    def refresh_all_playlists(self, num_of_plst):
        for i in range(1, num_of_plst + 1): 
            UIFunctions.refresh_playlist(self, i)

    def dur_playlist(self, num_plst):
        # Construir nombres de lista y labels
        
        label1_name = f"label_dur_{num_plst}"
        label2_name = f"playlist_dur_pl{num_plst}"

        # Obtener la lista de la playlist correspondiente
        pl_list = load_plst(num_plst)
        clip_data = load_clip_dictionary()

        total_ms = 0

        # Iterar sobre todos los elementos de la playlist
        for item in pl_list:
            numeric_code = item[:3]  # Obtener el código del clip
            if numeric_code in clip_data:
                dur_str = clip_data[numeric_code][6]  # Duración en formato "hh:mm:ss.mmm"

                if dur_str != "void":
                    try:
                        # Separar en hh:mm:ss y milisegundos
                        time_part, ms_part = dur_str.split(".")
                        h, m, s = map(int, time_part.split(":"))
                        ms = int(ms_part)
                        
                        # Sumar la duración al total en milisegundos
                        total_ms += (((h * 60 + m) * 60 + s) * 1000) + ms
                    except ValueError:
                        print(f"Error en el formato de duración para el clip {numeric_code}: {dur_str}")
                        continue  # Si el formato es incorrecto, lo ignoramos

        # Convertir total_ms a hh:mm:ss.mmm
        h = total_ms // 3600000
        m = (total_ms % 3600000) // 60000
        s = (total_ms % 60000) // 1000
        ms = total_ms % 1000

        # Formatear el total en "hh:mm:ss.mmm"
        duracion_total = f"{h:02}:{m:02}:{s:02}.{ms:03}"

        # Actualizar las labels correspondientes
        getattr(self.ui, label1_name).setText(duracion_total)
        getattr(self.ui, label2_name).setText(duracion_total)

    def num_clips_playlist(self, num_plst):
        # Nombre de la lista y labels basados en el número de playlist
        label1_name = f"label_nclips_{num_plst}"
        label2_name = f"playlist_numclip_pl{num_plst}"

        # Obtener la lista desde las variables globales
        pl_list = load_plst(num_plst)

        # Contar el número de clips
        num_clips = len(pl_list)

        # Formatear el texto
        texto = f"{num_clips} clips"

        # Actualizar los QLabel
        getattr(self.ui, label1_name).setText(texto)
        getattr(self.ui, label2_name).setText(texto)


    ########################################################################
    ## END - FUNCTIONS PLAYLIST
    ########################################################################


    ########################################################################
    ## START - FUNCIONS SIMULATOR
    ########################################################################

    #Toggle Shift declared in main.py

    def function_menu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_configuration)

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

    def function_play(self):
        if modo_playlist == True:
            plst = load_active_playlist()
            num_plst = plst[-1]
            vmix_event = int(num_plst) + 1
            endpoint_1 = f"api/?Function=ReplaySelectEvents{vmix_event}&Channel=1"
            UIFunctions.send_request(endpoint_1)
            response_3 = UIFunctions.send_request("api/?Function=ReplayPlayAllEvents&Channel=1")
            if not response_3:
                print("No se pudo ejecutar ReplayPlay. Saltando function_play.")
                return


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

    #function PAGE declared in main.py
    #function gotopl declarada a FUNCTIONS CLIP
    #function_loop declarada a FUNCTIONS CONTROL

    def function_in(self):
        """Marks the current position as 'in' for replay."""
        global mark_in_tc

        current_mark_in_tc = UIFunctions.get_tc()
        mark_in_tc = save_mark_in_tc(current_mark_in_tc)

        pgm = UIFunctions.get_channelmode()

        if pgm == "B": 
            self.ui.sim_in.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: green; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        else: 
            self.ui.sim_in.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: red; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")

        # Endpoint para la función 'ReplayMarkIn'
        endpoint = "api/?Function=ReplayMarkIn"
        
        # Usamos UIFunctions.send_request para realizar la solicitud
        response = UIFunctions.send_request(endpoint)


        
        
        if not response:
            print("No se pudo marcar el 'In' debido a la falta de conexión con vMix.")
            return  # Salir si no hay conexión
        
        print("Replay mark 'In' set successfully.")

    #Function out declared in main.py
    
    def function_take():
        """Realiza la acción ReplaySwapChannels en vMix, si hay conexión."""
        response = UIFunctions.send_request("api/?Function=ReplaySwapChannels")
        response_1 = UIFunctions.send_request("api/?Function=ReplayPlay&Channel=1")
        if not response_1:
            print("No se pudo ejecutar ReplayPlay. Saltando function_play.")
            return
        
        if not response:
            print("No se pudo ejecutar 'ReplaySwapChannels' porque no hay conexión con vMix.")
            return  # Sale de la función sin hacer nada si no hay conexión
        
        print("Acción 'ReplaySwapChannels' ejecutada correctamente.")


    #Dial
    def toggle_browse_mode(self):
        """
        Activa o desactiva el modo BROWSE.
        Este modo puede ser usado, por ejemplo, para navegar entre ítems sin ejecutar acciones.
        """
        if not hasattr(self, "browse_mode"):
            self.browse_mode = False  # Inicializa si no existe

        self.browse_mode = not self.browse_mode  # Alternar estado

        if self.browse_mode:
            print("🔍 Browse mode ACTIVADO")
            self.ui.sim_insert.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: red; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
        else:
            print("🔚 Browse mode DESACTIVADO")
            self.ui.sim_insert.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white; padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")


    def function_rodeta(self, dial):
        """Configura el QDial para controlar la replay de vMix frame por frame o navegar en la lista de reproducción dependiendo del modo."""

        dial.setWrapping(True)  # Permite giros infinitos
        dial.setNotchesVisible(False)
        dial.previous_value = dial.value()  # Guarda el estado inicial
        dial.fast_mode = False  # Modo normal por defecto
        dial.super_fast_mode = False

        def on_dial_moved(value):

            # 1. Revisar si estamos en browse_mode
            if getattr(self, "browse_mode", False):  # Verifica si estamos en browse_mode
                plst = load_active_playlist()  # Carga la lista activa
                plst_num = plst[2:]  # Obtiene el número de la lista activa
                list_name = f"list_pl{plst_num}"  # Define el nombre de la lista en UI

                if hasattr(self.ui, list_name):  # Verifica si la lista existe en la UI
                    list_widget = getattr(self.ui, list_name)
                    total_items = list_widget.count()

                    if total_items == 0:
                        return  # Si la lista está vacía, no hacer nada

                    current_index = list_widget.currentRow()
                    direction = 1 if value > dial.previous_value else -1 if value < dial.previous_value else 0
                    new_index = (current_index + direction) % total_items  # Calcular el nuevo índice con scroll circular

                    list_widget.setCurrentRow(new_index)  # Actualiza la fila seleccionada
                    list_widget.scrollToItem(list_widget.item(new_index))  # Desplázate al nuevo elemento
                    self.selected_index = new_index  # Guarda el índice seleccionado

                    print(f"📜 Browse Mode: seleccionado índice {new_index}")
                else:
                    print(f"⚠️ No existe {list_name} en self.ui")

                dial.previous_value = value  # Actualiza el valor previo solo si estamos en browse_mode
                return  # Salir para no ejecutar el resto de la lógica de ReplayJumpFrames

            # 2. Si no estamos en browse_mode, gestionar la reproducción de vMix

            # Activar live si no está activado
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

            # Paso 3: Iterar sobre todos los inputs y buscar el 'channelMode' en la sección de Replay
            result = None  # Inicializamos result como None por si no encontramos nada
            
            for input_element in root.findall(".//input"):
                replay_element = input_element.find('replay')
                
                if replay_element is not None:
                    channel_mode = replay_element.get('live')
                    if channel_mode:
                        result = channel_mode  # Guardamos el modo de canal encontrado

            if result == "True":
                time.sleep(0.2)
                endpoint_live = "api/?Function=ReplayLiveToggle"
                response_3 = UIFunctions.send_request(endpoint_live)
                if not response_3:
                    print("No se pudo realizar el 'ReplayLiveToogle' debido a la falta de conexión con vMix.")
                    return  # Salir si no hay conexión
            else: 
                print("Live already desactivated")

            # 3. Detecta el movimiento del dial y envía la petición HTTP a vMix

            direction = 1 if value > dial.previous_value else -1 if value < dial.previous_value else 0

            if direction == 0:
                return  # No hay movimiento, salir

            # Determinar el valor de step basado en los modos fast_jog y super_fast_jog
            FAST_JOG = load_fast_jog()
            SEC_FAST_JOG = load_sec_fast_jog()

            if dial.fast_mode:
                step = FAST_JOG
            elif dial.super_fast_mode:
                step = SEC_FAST_JOG
            else:
                step = 1  # Modo normal, paso de 1 frame

            # Ajustar la dirección usando el valor de step
            direction *= step  # Multiplicamos la dirección por el paso para que sea más grande en los modos rápidos

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
        
        UIFunctions.send_request("api/?Function=ReplaySelectEvents1&Channel=1")
        UIFunctions.function_reset_lastmark()
        
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
        global clip_mode, modo_playlist
        modo_playlist = False
        clip_mode = False  # Desactivamos el modo clip
        print(f"Modo clip desactivado: Clip_mode: {clip_mode}")

        # Guardar la configuración
        save_config("clip_mode", clip_mode)
        print("Configuración de clip_mode guardada.")  # Confirmación de guardado

        print("Replay jumped to now and playback started successfully.")


    #Toggle clear declared in main.py

    def function_enter(self):
        global modo_playlist, active_playlist
        plst = load_active_playlist()
        num_plst = plst[2:]
        print(num_plst)
        UIFunctions.add_to_playlist(self, num_plst)

    ########################################################################
    ## END - FUNCIONS SIMULATOR
    ########################################################################


    ########################################################################
    ## START - CLIP MANAGEMENT FUNCTIONS
    ########################################################################

    def show_dialog_overwrite_clip(self, clip_code, clip_management):
        self.popup = PopupOverwriteClip(clip_code, clip_management)
        self.popup.exec_()

    
    def get_tc(): 
        response = UIFunctions.send_request("api/")
        
        if response:
            tree = ET.fromstring(response)
            timecode_element = tree.find(".//timecode")
            timecode = timecode_element.text if timecode_element is not None else "00:00:00:00"
            print(f"Timecode obtenido: {timecode}")
        else:
            print("No se pudo obtener el timecode de vMix. Conexión no disponible.")
        return timecode
    
    def calculate_clip_duration(clip_tc_in, clip_tc_out):
        """
        Calcula la duración entre clip_tc_in y clip_tc_out en formato "HH:MM:SS.sss".

        Parámetros:
            clip_tc_in (str): Timecode de entrada en formato "YYYY-MM-DDTHH:MM:SS.sss".
            clip_tc_out (str): Timecode de salida en formato "YYYY-MM-DDTHH:MM:SS.sss".

        Retorna:
            str: Duración del clip en formato "HH:MM:SS.sss".
        """
        # Formato de los timecodes proporcionados con "T" entre fecha y hora
        format_tc = "%Y-%m-%dT%H:%M:%S.%f"

        # Convertir los timecodes a objetos datetime
        time_in = datetime.strptime(clip_tc_in, format_tc)
        time_out = datetime.strptime(clip_tc_out, format_tc)

        print(time_in)
        print(time_out)

        # Calcular la diferencia (duración)
        duration = time_out - time_in

        print(duration)

        # Convertir la duración a segundos (float) y luego formatear a horas, minutos, segundos y milisegundos
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds % 1) * 1000)

        # Formatear el resultado en formato HH:MM:SS.sss
        duration_str = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

        print(duration_str)

        return duration_str
    
    ########################################################################
    ## START - CLIP MANAGEMENT FUNCTIONS
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
    ## END - FUNCTIONS CONFIG
    ########################################################################

    
    ########################################################################
    ## END - VMIX TO EVS FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    #UI definitions
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        #Remove standard title bar
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        #Show drop shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        #Resize window
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        #Maximize - Restore
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## Close Application
        self.ui.btn_close.clicked.connect(lambda: close_app())
        
        def close_app():
            UIFunctions.function_record()
            self.close()

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
