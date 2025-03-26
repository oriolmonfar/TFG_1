
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QTimer,QEventLoop)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMouseEvent)
from PySide2.QtWidgets import *
import time
from datetime import datetime, timedelta


# GUI FILE
from app_modules import *
from ui_popup_recordtrains import Ui_Dialog as Dialog_recordtrains
from ui_popup_searchtc import Ui_Dialog as Dialog_searchtc
from ui_popup_fastjog import Ui_Dialog as Dialog_fastjog
from ui_popup_ipconfig import Ui_Dialog as Dialog_ipconfig
from ui_popup_myvmix import Ui_Dialog as Dialog_myvmix
from ui_popup_deleteip import Ui_Dialog as Dialog_deleteip
from ui_popup_confirm_no_connection import Ui_Dialog as Dialog_no_connection
from ui_popup_confirm_connected import Ui_Dialog as Dialog_connected
from ui_popup_overwrite_clip import Ui_Dialog as Dialog_overwrite
from ui_popup_delete_clip_dictionary import Ui_Dialog as Dialog_delete_clip_dictionary
from config_manager import *

IP_VMIX = load_ip_vmix()
FAST_JOG = load_fast_jog()
SHIFT = False
current_page = load_current_page()
current_bank = load_current_bank()
current_clip = load_current_clip()
current_camangle = load_current_camangle()
clip_mode = load_clip_mode()
modo_page = False
clip_id = load_current_clip_id()
last_date = load_last_date()
last_time = load_last_time()
mark_in_tc = load_mark_in_tc()
estrella1 = load_estrella1_list()
estrella2 = load_estrella2_list()
estrella3 = load_estrella3_list()



class PopupRecordTrains(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_recordtrains()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_recordtrains.clicked.connect(lambda: self.showMinimized())
        ## ==> MAXIMIZE/RESTORE
        self.ui.maximizerecord_trains.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_recordtrains.clicked.connect(lambda: self.close())

class PopupOverwriteClip(QDialog):  
    def __init__(self, clip_code, clip_management):  
        super().__init__()  
        self.ui = Dialog_overwrite()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ## ==> MAXIMIZE/RESTORE
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_overwrite.clicked.connect(lambda: self.close())
        self.ui.overwrite_no.clicked.connect(lambda: no(clip_code))
        self.ui.overwrite_yes.clicked.connect(lambda: yes(self, clip_code, clip_management))

        def yes(self, clip_code, clip_management):
            """Overwrites the clip ID in clip_manager.json."""
            id = load_current_clip_id()
            clip_management[clip_code] = str(id)
            save_clip_management(clip_management)
            id += 1
            save_current_clip_id(id)
            #print(f"Clip {clip_code} registrado con ID {clip_id - 1}")
            print(f"El clip {clip_code} ya está registrado con ID {clip_management[clip_code]}")
            time.sleep(0.2)
            self.close()

        def no(clip_code): 
            id = load_current_clip_id()
            endpoint = f"api/?Function=ReplayDeleteSelectedEvent&Value={id}&Channel=1"
            UIFunctions.send_request(endpoint)
            print(f"Se mantuvo el ID original para el clip {clip_code}.")
            id +=1 
            save_current_clip_id(id)
            time.sleep(0.1)
            self.close()

class PopupDeleteClipDictionary(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_delete_clip_dictionary()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ## ==> MAXIMIZE/RESTORE
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_confirm_deleteclipdic.clicked.connect(lambda: self.close())
        self.ui.confirm_deleteclipdic_no.clicked.connect(lambda: self.close())
        self.ui.confirm_deleteclipdic_yes.clicked.connect(lambda: reset_clip_dictionary_and_clip_id())

        def reset_clip_dictionary_and_clip_id():
            """Resetea todos los clips a 'void' en clip_dictionary.json y establece clip_id en 0 en config.json."""

            # Cargar el archivo clip_dictionary.json
            clip_dictionary = load_clip_dictionary()

            # Iterar sobre los códigos de clip y restablecer todos los elementos de la lista a "void"
            for clip_code in clip_dictionary.keys():
                clip_dictionary[clip_code] = ["void"] * 7

            # Guardar los cambios en clip_dictionary.json
            save_clip_dictionary(clip_dictionary)
            print("Todos los clips han sido restablecidos a 'void'.")

            # Cargar y actualizar config.json
            config = load_config()
            config["clip_id"] = 0
            save_config("clip_id", 0)
            
            print("clip_id ha sido restablecido a 0 en 'config.json'.")

            time.sleep(0.1)
            self.close()


class PopupSearchTC(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_searchtc()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_searchtc.clicked.connect(lambda: self.showMinimized())
        ## ==> MAXIMIZE/RESTORE
        self.ui.maximize_searchtc.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_searchtc.clicked.connect(lambda: self.close())

        self.ui.searchtc_0.clicked.connect(lambda: self.write("0"))
        self.ui.searchtc_1.clicked.connect(lambda: self.write("1"))
        self.ui.searchtc_2.clicked.connect(lambda: self.write("2"))
        self.ui.searchtc_3.clicked.connect(lambda: self.write("3"))
        self.ui.searchtc_4.clicked.connect(lambda: self.write("4"))
        self.ui.searchtc_5.clicked.connect(lambda: self.write("5"))
        self.ui.searchtc_6.clicked.connect(lambda: self.write("6"))
        self.ui.searchtc_7.clicked.connect(lambda: self.write("7"))
        self.ui.searchtc_8.clicked.connect(lambda: self.write("8"))
        self.ui.searchtc_9.clicked.connect(lambda: self.write("9"))
        self.ui.searchtc_dospunts.clicked.connect(lambda: self.write(":"))
        self.ui.searchtc_punt_2.clicked.connect(lambda: self.write("."))
        self.ui.searchtc_delete.clicked.connect(lambda: self.delete())
        self.ui.searchtc_confirm.clicked.connect(lambda: self.confirm())

    def write(self, text):
        self.ui.searchtc_textedit.insertPlainText(text)

    def delete(self):
        """Elimina el último carácter directamente en la interfaz"""
        if self.ui.searchtc_textedit:  # Verifica que el QTextEdit esté inicializado
            cursor = self.ui.searchtc_textedit.textCursor()  # Obtiene el cursor de QTextEdit
            cursor.movePosition(cursor.End)  # Mueve el cursor al final
            cursor.deletePreviousChar()  # Borra el último carácter
    def confirm(self): 
        global last_date, last_time
        texto = self.ui.searchtc_textedit.toPlainText()  # Recupera el texto
        date = datetime.now().date()
        last_time = save_last_time(texto)
        last_date = save_last_date(date)
        endpoint = f"api/?Function=ReplaySetTimecode&Value={date}T{texto}0"
        UIFunctions.send_request(endpoint)
        time.sleep(0.1)
        self.close()
        
    
class PopupFastJog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialog_fastjog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.ui.minimize_fastjog.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_fastjog.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_fastjog.clicked.connect(lambda: self.close())

        self.ui.fastjogconfig_0.clicked.connect(lambda: self.write("0"))
        self.ui.fastjogconfig_1.clicked.connect(lambda: self.write("1"))
        self.ui.fastjogconfig_2.clicked.connect(lambda: self.write("2"))
        self.ui.fastjogconfig_3.clicked.connect(lambda: self.write("3"))
        self.ui.fastjogconfig_4.clicked.connect(lambda: self.write("4"))
        self.ui.fastjogconfig_5.clicked.connect(lambda: self.write("5"))
        self.ui.fastjogconfig_6.clicked.connect(lambda: self.write("6"))
        self.ui.fastjogconfig_7.clicked.connect(lambda: self.write("7"))
        self.ui.fastjogconfig_8.clicked.connect(lambda: self.write("8"))
        self.ui.fastjogconfig_9.clicked.connect(lambda: self.write("9"))
        self.ui.fastjogconfig_delete.clicked.connect(lambda: self.delete())
        self.ui.fastjogconfig_confirm.clicked.connect(lambda: self.confirm())

        # Inicializar con el valor actual de FAST_JOG
        self.ui.textedit_fastjog.setPlainText(str(FAST_JOG))  

    def write(self, text):
        self.ui.textedit_fastjog.insertPlainText(text)

    def delete(self):
        if self.ui.textedit_fastjog:
            cursor = self.ui.textedit_fastjog.textCursor()
            cursor.movePosition(cursor.End)
            cursor.deletePreviousChar()

    def confirm(self):
        global FAST_JOG  # Asegurar que trabajamos con la variable global

        texto = self.ui.textedit_fastjog.toPlainText().strip()
        if texto.isdigit():  
            save_fast_jog(int(texto))  # Guardamos el nuevo valor en el JSON
            
            # Recargamos la variable global desde el archivo JSON
            FAST_JOG = load_fast_jog()

            print(f"Nuevo valor de FAST_JOG guardado y recargado: {FAST_JOG}")
            time.sleep(0.2)
            self.close()

        else:
            print("Entrada no válida. Ingresa un número.")

class PopupIpConfig(QDialog):
    def __init__(self, vmix_window):
        super().__init__()
        self.vmix_window = vmix_window
        self.ui = Dialog_ipconfig()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_ipconfig.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_ipconfig.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_ipconfig.clicked.connect(lambda: self.close())

        # Conectar botones para escribir en el QTextEdit
        self.ui.ipconfig_0.clicked.connect(lambda: self.write("0"))
        self.ui.ipconfig_1.clicked.connect(lambda: self.write("1"))
        self.ui.ipconfig_2.clicked.connect(lambda: self.write("2"))
        self.ui.ipconfig_3.clicked.connect(lambda: self.write("3"))
        self.ui.ipconfig_4.clicked.connect(lambda: self.write("4"))
        self.ui.ipconfig_5.clicked.connect(lambda: self.write("5"))
        self.ui.ipconfig_6.clicked.connect(lambda: self.write("6"))
        self.ui.ipconfig_7.clicked.connect(lambda: self.write("7"))
        self.ui.ipconfig_8.clicked.connect(lambda: self.write("8"))
        self.ui.ipconfig_9.clicked.connect(lambda: self.write("9"))
        self.ui.ipconfig_A.clicked.connect(lambda: self.write("A"))
        self.ui.ipconfig_B.clicked.connect(lambda: self.write("B"))
        self.ui.ipconfig_C.clicked.connect(lambda: self.write("C"))
        self.ui.ipconfig_D.clicked.connect(lambda: self.write("D"))
        self.ui.ipconfig_E.clicked.connect(lambda: self.write("E"))
        self.ui.ipconfig_F.clicked.connect(lambda: self.write("F"))
        self.ui.ipconfig_G.clicked.connect(lambda: self.write("G"))
        self.ui.ipconfig_H.clicked.connect(lambda: self.write("H"))
        self.ui.ipconfig_I.clicked.connect(lambda: self.write("I"))
        self.ui.ipconfig_J.clicked.connect(lambda: self.write("J"))
        self.ui.ipconfig_K.clicked.connect(lambda: self.write("K"))
        self.ui.ipconfig_L.clicked.connect(lambda: self.write("L"))
        self.ui.ipconfig_M.clicked.connect(lambda: self.write("M"))
        self.ui.ipconfig_N.clicked.connect(lambda: self.write("N"))
        self.ui.ipconfig_O.clicked.connect(lambda: self.write("O"))
        self.ui.ipconfig_P.clicked.connect(lambda: self.write("P"))
        self.ui.ipconfig_Q.clicked.connect(lambda: self.write("Q"))
        self.ui.ipconfig_R.clicked.connect(lambda: self.write("R"))
        self.ui.ipconfig_S.clicked.connect(lambda: self.write("S"))
        self.ui.ipconfig_T.clicked.connect(lambda: self.write("T"))
        self.ui.ipconfig_U.clicked.connect(lambda: self.write("U"))
        self.ui.ipconfig_V.clicked.connect(lambda: self.write("V"))
        self.ui.ipconfig_W.clicked.connect(lambda: self.write("W"))
        self.ui.ipconfig_X.clicked.connect(lambda: self.write("X"))
        self.ui.ipconfig_Y.clicked.connect(lambda: self.write("Y"))
        self.ui.ipconfig_Z.clicked.connect(lambda: self.write("Z"))
        self.ui.ipconfig_barra.clicked.connect(lambda: self.write("-"))
        self.ui.ipconfig_barra_baixa.clicked.connect(lambda: self.write("_"))
        self.ui.ipconfig_punt.clicked.connect(lambda: self.write("."))
        self.ui.ipconfig_dospunts.clicked.connect(lambda: self.write(":"))
        self.ui.ipconfig_delete.clicked.connect(lambda: self.delete())
        self.ui.ipconfig_confirm.clicked.connect(lambda: self.confirm())

        # Inicialmente, no hay QTextEdit activo
        self.active_textedit = None

        # Conectar eventos de foco para detectar qué QTextEdit está seleccionado
        self.ui.textedit_ipconfig.installEventFilter(self)
        self.ui.textedit_ipconfig_name.installEventFilter(self)

    def eventFilter(self, obj, event):
        """Detecta cuándo un QTextEdit recibe el foco."""
        if event.type() == event.FocusIn:
            self.active_textedit = obj  # Guarda el QTextEdit activo
        return super().eventFilter(obj, event)

    def write(self, text):
        """Escribe el texto en el QTextEdit activo."""
        if self.active_textedit:
            self.active_textedit.insertPlainText(text)

    def delete(self):
        """Elimina el último carácter del QTextEdit activo."""
        if self.active_textedit:
            cursor = self.active_textedit.textCursor()
            cursor.movePosition(cursor.End)
            cursor.deletePreviousChar()

    def confirm(self):
        """Guarda los valores y los añade a la ComboBox en PopupMyVmix."""
        name = self.ui.textedit_ipconfig_name.toPlainText().strip()
        ip_port = self.ui.textedit_ipconfig.toPlainText().strip()

        if name and ip_port:
            formatted_text = f"{name} ({ip_port})"

            # Añadir a la ComboBox en UI
            self.vmix_window.myvmix_combobox.addItem(formatted_text)

            # Obtener la lista actual de VMIX desde el archivo
            vmix_list = load_vm_list()
            vmix_list.append(formatted_text)  # Añadir el nuevo valor

            # Guardar la lista actualizada en el archivo JSON
            save_vm_list(vmix_list)
            time.sleep(0.2)

            self.close()
    
    def add_to_combobox(self, name, ip_port):
        """Añade la configuración a la QComboBox en el formato correcto."""
        formatted_text = f"{name} ({ip_port})"
        self.vmix_window.myvmix_combobox.addItem(formatted_text)
    

class PopupMyVmix(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_myvmix()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.myvmix_success_label.setText("                ")
        self.ui.minimize_myvmix.clicked.connect(lambda: self.showMinimized())
        ## ==> MAXIMIZE/RESTORE
        self.ui.maximize_myvmix.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_myvmix.clicked.connect(lambda: self.close())

        self.ui.myvmix_add.clicked.connect(lambda: self.show_dialog_ipconfig())
        self.ui.myvmix_delete.clicked.connect(lambda: self.show_dialog_deleteip())
        self.ui.myvmix_checkconnection.clicked.connect(lambda: self.check_connection())
        self.ui.myvmix_confirm.clicked.connect(lambda: self.confirm_selection())
        
        self.myvmix_combobox= self.ui.myvmix_combobox 

        self.load_combobox_items()

    def load_combobox_items(self):
        """Carga los elementos guardados en el ComboBox desde config.json."""
        vmix_list = load_vm_list()  # Cargar la lista de VMIX desde el archivo
        self.myvmix_combobox.clear()  # Limpiar la ComboBox para evitar duplicados
        for item in vmix_list:
            self.myvmix_combobox.addItem(item)  # Añadir a la ComboBox


    def show_dialog_ipconfig(self):
        self.popup = PopupIpConfig(self)  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_deleteip(self):
        self.popup = PopupDeleteIp(self)  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def load_combobox_items(self):
        """Carga los elementos guardados en el ComboBox desde config.json."""
        vmix_list = load_vm_list()  # Cargar la lista de VMIX desde el archivo
        for item in vmix_list:
            self.myvmix_combobox.addItem(item)  # Añadir a la ComboBox

    def check_connection(self):
        """Verifica la conexión con vMix usando la API HTTP."""
        selected_text = self.ui.myvmix_combobox.currentText()

        if not selected_text:  # Verificar si hay un valor seleccionado
            self.ui.myvmix_success_label.setText("No selection")
            self.ui.myvmix_success_label.setStyleSheet("color: orange;")
            return

        # Extraer IP y puerto del texto seleccionado (Formato: "Nombre (IP:PUERTO)")
        try:
            ip_port = selected_text.split("(")[-1].strip(")")  # Extrae solo la parte IP:PUERTO
        except IndexError:
            self.ui.myvmix_success_label.setText("Invalid format")
            self.ui.myvmix_success_label.setStyleSheet("color: orange;")
            return

        url = f"http://{ip_port}/api/"

        try:
            response = requests.get(url, timeout=3)  # Tiempo de espera de 3 segundos
            if response.status_code == 200:
                self.ui.myvmix_success_label.setText("        Successful")
                self.ui.myvmix_success_label.setStyleSheet("color: rgb(0,255,0); font-size: 20px;")
                
            else:
                self.ui.myvmix_success_label.setText("     No connection")
                self.ui.myvmix_success_label.setStyleSheet("color: rgb(255,0,0); font-size: 20px;")
        except requests.exceptions.RequestException:
            self.ui.myvmix_success_label.setText("     No connection")
            self.ui.myvmix_success_label.setStyleSheet("color: rgb(255,0,0); font-size: 20px;")

    def confirm_selection(self):
        """Confirma la selección verificando la conexión y actualizando la IP_VMIX."""
        selected_text = self.ui.myvmix_combobox.currentText()
        print(selected_text)

        if not selected_text:
            return  # No hay nada seleccionado, salir de la función

        try:
            ip_port = selected_text.split("(")[-1].strip(")")
        except IndexError:
            return  # Formato inválido, salir de la función

        url = f"http://{ip_port}/api/"

        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                # Conexión exitosa, guardar la nueva IP en config.json
                save_ip_vmix(ip_port)  # Guardamos la nueva IP_VMIX
                update_vmix_list(selected_text)  # Mueve el seleccionado al inicio
                self.show_dialog_connected()
            else:
                self.show_dialog_noconnection() # Mostrar Popup de error
        except requests.exceptions.RequestException:
            self.show_dialog_noconnection()  # Mostrar Popup de error

    def show_dialog_noconnection(self):
        self.popup = PopupNoConnection()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_connected(self):
        self.popup = PopupConnected()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal


class PopupDeleteIp(QDialog):  
    def __init__(self, myvmix_instance):  
        super().__init__()  
        self.ui = Dialog_deleteip()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.myvmix_instance = myvmix_instance  # Guardamos la referencia
        self.ui.minimize_deleteip.clicked.connect(lambda: self.showMinimized())
        ## ==> MAXIMIZE/RESTORE
        self.ui.maximize_deleteip.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_deleteip.clicked.connect(lambda: self.close())

        self.ui.deleteip_no.clicked.connect(lambda: self.close())
        self.ui.deleteip_yes.clicked.connect(lambda: self.delete_selected_item())
    def delete_selected_item(self):
        """Elimina el elemento seleccionado de la ComboBox y actualiza la lista en config.json."""
        if not self.myvmix_instance:  # Verificar que la referencia es válida
            return

        combobox = self.myvmix_instance.ui.myvmix_combobox  # Acceder a la combobox
        selected_index = combobox.currentIndex()

        if selected_index != -1:  # Si hay un elemento seleccionado
            selected_item = combobox.currentText()

            # Eliminar el item de la combobox
            combobox.removeItem(selected_index)

            # Obtener la lista actualizada del archivo JSON
            vmix_list = load_vm_list()

            # Eliminar el item si existe en la lista
            if selected_item in vmix_list:
                vmix_list.remove(selected_item)

            # Guardar la lista actualizada en config.json
            save_vm_list(vmix_list)
            time.sleep(0.2)
            self.close()

class PopupNoConnection(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_no_connection()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_noconn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_noconn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_noconn.clicked.connect(lambda: self.close())

class PopupConnected(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_connected()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_conn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_conn.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_conn.clicked.connect(lambda: self.close())

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.check_vmix_connection(self)
        UIFunctions.start_connection_monitor(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        #UIFunctions.labelTitle(self, 'Main Window - Python Base')
        self.ui.label_page.setText(f"PAGE {current_page}  ")
        self.ui.label_bank.setText(f" {current_bank} BANK")  # Actualiza QLabel
        UIFunctions.labelDescription(self, 'PL11:  113A, 232A, 342A')
        
        ################################# SET PGM
        def get_channelmode(self):
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
        
        pgm = get_channelmode(self)
        UIFunctions.labelPGM_PRV(self, pgm)

        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1024, 600)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "CLIP", "btn_home", "url(:/16x16/icons/16x16/cil-media-play.png)", True)
        UIFunctions.addNewMenu(self, "CONTENT ACCESS", "btn_new_user", "url(:/16x16/icons/16x16/cil-input.png)", True)
        UIFunctions.addNewMenu(self, "CONTROL", "btn_control", "url(:/16x16/icons/16x16/cil-clipboard.png)", True)
        UIFunctions.addNewMenu(self, "EXPORT", "btn_export", "url(:/16x16/icons/16x16/cil-paper-plane.png)", True)
        UIFunctions.addNewMenu(self, "GENERIC", "btn_generic", "url(:/16x16/icons/16x16/cil-folder-open.png)", True)
        UIFunctions.addNewMenu(self, "PLAYLIST", "btn_playlist", "url(:/16x16/icons/16x16/cil-featured-playlist.png)", True)
        UIFunctions.addNewMenu(self, "CLIP MANAGEMENT", "btn_clipmanagement", "url(:/16x16/icons/16x16/cil-library-add.png)", True)
        UIFunctions.addNewMenu(self, "SIMULATOR", "btn_simulator", "url(:/16x16/icons/16x16/cil-devices.png)", True)
        UIFunctions.addNewMenu(self, "CONFIGURATION", "btn_config", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        #UIFunctions.addNewMenu(self, "WIDGETS", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "WM", "", False)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        

        #################################### START - MAINWINDOW PARAMETERS
    
       
        #################################### END - MAINWINDOW PARAMETERS

        #################################### START- BOTONS CLIP

        self.ui.clip_addtoplaylist.clicked.connect(lambda: UIFunctions.function_plst_page(self))
        UIFunctions.refresh_estrella1_list(self)
        self.ui.clip_estrella1.clicked.connect(lambda: UIFunctions.function_estrella1(self))
        UIFunctions.refresh_estrella2_list(self)
        self.ui.clip_button_onwidget_estrelles2.clicked.connect(lambda: UIFunctions.function_estrella2(self))
        UIFunctions.refresh_estrella3_list(self)
        self.ui.clip_button_onwidget_estrelles3.clicked.connect(lambda: UIFunctions.function_estrella3(self))
        self.ui.clip_gotoestrella1.clicked.connect(lambda: UIFunctions.function_estrella1_page(self))
        self.ui.clip_gotoestrella2.clicked.connect(lambda: UIFunctions.function_estrella2_page(self))
        self.ui.clip_gotoestrella3.clicked.connect(lambda: UIFunctions.function_estrella3_page(self))
        self.ui.estrella1_delete.clicked.connect(lambda: UIFunctions.remove_estrella1(self))
        self.ui.estrella2_delete.clicked.connect(lambda: UIFunctions.remove_estrella2(self))
        self.ui.estrella3_delete.clicked.connect(lambda: UIFunctions.remove_estrella3(self))

        #################################### END - BOTONS CLIP

        #################################### START - BOTONS CONTROL
        self.ui.control_syncprv.clicked.connect(lambda: UIFunctions.function_syncprv(self))
        self.ui.control_loop.clicked.connect(lambda: UIFunctions.function_loop())
        self.ui.control_fast_jog.clicked.connect(lambda: UIFunctions.function_fastjog(self.dial))

        #################################### END - BOTONS CONTROL

        #################################### START - BOTONS CONTENT ACCESS
        self.ui.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.ui.contec_acc_actualclip.setText(f"{current_clip}")
        self.ui.cont_acc_mark.clicked.connect(lambda: UIFunctions.function_mark())
        self.ui.cont_acc_lastmark.clicked.connect(lambda: UIFunctions.function_lastmark())
        self.ui.cont_acc_recordtrains.clicked.connect(self.show_dialog_recordtrains)
        self.ui.cont_acc_searchtc.clicked.connect(self.show_dialog_searchtc)
        self.ui.cont_acc_lastsearchtc.clicked.connect(lambda: UIFunctions.function_lastsearchtc())


        #################################### END - BOTONS CONTENT ACCESS

        #################################### START- BOTONS SIMULATOR

        def toggle_shift(self):
            """Alterna el estado de SHIFT y cambia el color del botón."""
            global SHIFT
            SHIFT = not SHIFT

            if SHIFT:
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: rgba(255,40,40,150);} QPushButton:hover {background-color: rgba(255,40,40,50);} QPushButton:pressed { background-color: rgba(255,40,40,50);}")  # Rojo cuando está activado
            else:
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}")   # Transparente cuando está desactivado

            print(f"Shift activado: {SHIFT}")  # Depuración

        def reset_shift(self):
            """Desactiva SHIFT si está activado y restablece el color."""
            global SHIFT
            if SHIFT:
                SHIFT = False
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}") 
                print("Shift desactivado")

        self.ui.sim_shift.setCheckable(True)
        self.ui.sim_shift.clicked.connect(lambda: toggle_shift(self))

        def execute_functions_A(self):
            """Ejecuta la función correspondiente según el estado de SHIFT."""
            global SHIFT, clip_mode, current_camangle, current_clip
            if clip_mode:
                save_current_camangle("A")
                current_camangle = load_current_camangle()
                print(f"Clip Mode activo: current_camangle actualizado a {current_camangle}")
                current_clip = load_current_clip()
                clip_no_camangle = current_clip[:-1]
                save_current_clip(f"{clip_no_camangle}{current_camangle}")
                print(current_clip)
                channel_mode = get_channelmode(self)
                UIFunctions.labelPGM_PRV(self, channel_mode)
            else: 
                if SHIFT:
                    UIFunctions.function_A_prima()
                    reset_shift(self)
                else:
                    UIFunctions.function_A(self)
        self.ui.sim_A.clicked.connect(lambda: execute_functions_A(self))

        def execute_functions_B(self):
            global SHIFT, clip_mode, current_camangle, current_clip
            if clip_mode:
                save_current_camangle("B")
                current_camangle = load_current_camangle()
                print(f"Clip Mode activo: current_camangle actualizado a {current_camangle}")
                current_clip = load_current_clip()
                clip_no_camangle = current_clip[:-1]
                save_current_clip(f"{clip_no_camangle}{current_camangle}")
                print(current_clip)
                channel_mode = get_channelmode(self)
                UIFunctions.labelPGM_PRV(self, channel_mode)
            else: 
                if SHIFT:
                    UIFunctions.function_B_prima()
                    reset_shift(self)
                else:
                    UIFunctions.function_B(self)
        self.ui.sim_B.clicked.connect(lambda: execute_functions_B(self))

        def execute_functions_C(self):
            global SHIFT, clip_mode, current_camangle, current_clip
            if clip_mode:
                save_current_camangle("C")
                current_camangle = load_current_camangle()
                print(f"Clip Mode activo: current_camangle actualizado a {current_camangle}")
                current_clip = load_current_clip()
                clip_no_camangle = current_clip[:-1]
                save_current_clip(f"{clip_no_camangle}{current_camangle}")
                print(current_clip)
                channel_mode = get_channelmode(self)
                UIFunctions.labelPGM_PRV(self, channel_mode)
            else: 
                if SHIFT:
                    UIFunctions.function_C_prima()
                    reset_shift(self)
                else:
                    UIFunctions.function_C(self)
        self.ui.sim_C.clicked.connect(lambda: execute_functions_C(self))

        def execute_functions_D(self):
            global SHIFT, clip_mode, current_camangle, current_clip
            if clip_mode:
                save_current_camangle("D")
                current_camangle = load_current_camangle()
                print(f"Clip Mode activo: current_camangle actualizado a {current_camangle}")
                current_clip = load_current_clip()
                clip_no_camangle = current_clip[:-1]
                save_current_clip(f"{clip_no_camangle}{current_camangle}")
                print(current_clip)
                channel_mode = get_channelmode(self)
                UIFunctions.labelPGM_PRV(self, channel_mode)
            else: 
                if SHIFT:
                    UIFunctions.function_D_prima()
                    reset_shift(self)
                else:
                    UIFunctions.function_D(self)
        self.ui.sim_D.clicked.connect(lambda: execute_functions_D(self))

        def execute_functions_play(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_network()
                reset_shift(self)
            else:
                UIFunctions.function_play(self)
        self.ui.sim_play.clicked.connect(lambda: execute_functions_play(self))

        def execute_functions_gototc(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gototc()
                reset_shift(self)
            else:
                UIFunctions.function_lastmark()
        self.ui.sim_gototc.clicked.connect(lambda: execute_functions_gototc(self))

        def execute_functions_fastjog(self, dial):
            global SHIFT
            if SHIFT:
                UIFunctions.function_fastjog(dial)
                reset_shift(self)
            else:
                UIFunctions.function_mark()
        self.ui.sim_fastjog.clicked.connect(lambda: execute_functions_fastjog(self, self.dial))

        def execute_functions_record(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_record()
                reset_shift(self)
            else:
                UIFunctions.function_e_e()
        self.ui.sim_record.clicked.connect(lambda: execute_functions_record(self))

        def execute_functions_prvctl(self):
            global SHIFT
            if SHIFT:
                function_page_activate()
                reset_shift(self)
            else:
                UIFunctions.function_prvctl(self)
        self.ui.sim_prvctl.clicked.connect(lambda: execute_functions_prvctl(self))

        def execute_functions_loop(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_loop()
                reset_shift(self)
            else:
                UIFunctions.function_plst_page(self)
        self.ui.sim_loop.clicked.connect(lambda: execute_functions_loop(self))

        def execute_functions_insert(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_insert()
                reset_shift(self)
            else:
                UIFunctions.function_browse()
        self.ui.sim_insert.clicked.connect(lambda: execute_functions_insert(self))

        def execute_functions_in(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gotoin()
                reset_shift(self)
            else:
                UIFunctions.function_in()
        self.ui.sim_in.clicked.connect(lambda: execute_functions_in(self))

        def execute_functions_out(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gotoout()
                reset_shift(self)
            else:
                function_out()
        self.ui.sim_out.clicked.connect(lambda: execute_functions_out(self))

        def execute_functions_take(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_lever()
                reset_shift(self)
            else:
                UIFunctions.function_take()
        self.ui.sim_take.clicked.connect(lambda: execute_functions_take(self))

        #self.ui.sim_e_e.clicked.connect(lambda: UIFunctions.function_e_e())

        self.ui.sim_rodeta.setMinimum(0)
        self.ui.sim_rodeta.setMaximum(100)
        self.ui.sim_rodeta.setWrapping(True)  # Hacer que el dial sea cíclico
        self.dial = self.findChild(QDial, "sim_rodeta")  # Busca el QDial en la UI
        UIFunctions.function_rodeta(self.dial)  # Configura el dial

        self.slider = self.findChild(QSlider, "sim_palanqueta")  # Find the slider
        UIFunctions.setup_replay_speed_slider(self.slider)  # Setup slider functionality
        #self.ui.sim_lever.clicked.connect(lambda: UIFunctions.function_lever(self.slider))

        #Gestio clips

        def function_page_activate():
            """Activa el modo de selección de página."""
            global modo_page
            modo_page = True
            print("Modo de selección de página activado.")
        
        def function_out():
    
            global clip_id, mark_in_tc
            
            endpoint_1 = "api/?Function=ReplayMarkOut"
            response_1 = UIFunctions.send_request(endpoint_1)
            clip_out_tc = UIFunctions.get_tc()
            mark_in_tc = load_mark_in_tc()
            
            
            if not response_1:
                print("No se pudo marcar el 'Out' debido a la falta de conexión con vMix.")
                return
 
            print("Replay mark 'Out' set successfully.")
            
            print("Esperando selección de clip...")
            selected_clip = wait_for_clip_selection()
            
            if selected_clip:
                clip_management = load_clip_dictionary()
                
                if clip_management.get(selected_clip, ["void"] * 7)[0] == "void":
                    clip_id = load_current_clip_id()
                    clip_dur_tc = UIFunctions.calculate_clip_duration(mark_in_tc, clip_out_tc)
                    clip_management[selected_clip][0] = str(clip_id)  # Guardar en el primer elemento de la lista
                    clip_management[selected_clip][4] = str(mark_in_tc)
                    clip_management[selected_clip][5] = str(clip_out_tc)
                    clip_management[selected_clip][6] = str(clip_dur_tc)
                    save_clip_dictionary(clip_management)
                    
                    clip_id += 1
                    save_current_clip_id(clip_id)
                    print(f"Clip {selected_clip} registrado con ID {clip_id - 1}")
                else:
                    UIFunctions.show_dialog_overwrite_clip(self, selected_clip, clip_management)
        
                    
        
        def wait_for_clip_selection():
            while True:
                button_number = get_button_event()  # Captura el número del botón (1-10)

                if isinstance(button_number, int):  # Verifica que sea un número
                    current_page = load_config().get("CURRENT_PAGE", 1)
                    current_bank = load_config().get("last_bank_per_page", {}).get(str(current_page), 1)

                    clip_code = f"{current_page}{current_bank}{button_number}"
                    print(f"Clip code generado: {clip_code}")  # Para depuración
                    return clip_code
        
                
        def get_button_event():
            """Espera la pulsación de un botón sim_f y devuelve su número."""
            loop = QEventLoop()
            button_pressed = None

            def on_button_press(button_number):
                """Captura el número del botón pulsado y sale del loop."""
                nonlocal button_pressed
                button_pressed = button_number
                loop.quit()

            # Conectar cada botón a la función
            self.ui.sim_f1.clicked.connect(lambda: on_button_press(1))
            self.ui.sim_f2.clicked.connect(lambda: on_button_press(2))
            self.ui.sim_f3.clicked.connect(lambda: on_button_press(3))
            self.ui.sim_f4.clicked.connect(lambda: on_button_press(4))
            self.ui.sim_f5.clicked.connect(lambda: on_button_press(5))
            self.ui.sim_f6.clicked.connect(lambda: on_button_press(6))
            self.ui.sim_f7.clicked.connect(lambda: on_button_press(7))
            self.ui.sim_f8.clicked.connect(lambda: on_button_press(8))
            self.ui.sim_f9.clicked.connect(lambda: on_button_press(9))
            self.ui.sim_f10.clicked.connect(lambda: on_button_press(0))

            # Establecer un timeout para evitar bloqueos
            QTimer.singleShot(5000, loop.quit)  # Máximo 5 segundos de espera

            loop.exec_()  # Espera a que se presione un botón

            return button_pressed  # Retorna el botón presionado o None si se agotó el tiempo

        def handle_sim_f_button(self, f_button_number):
            """Maneja la funcionalidad de los botones sim_f1 a sim_f10."""
            global current_page, current_bank, SHIFT, clip_mode, modo_page


            # Si SHIFT está activado, cambiar el banco
            if SHIFT:
                change_bank(f_button_number)  # Cambiar banco de la página actual
                print("function change bank")
                reset_shift(self)

            elif modo_page:
                function_page(f_button_number)  # Cambiar página según el número del botón
                print("function change page")
                modo_page = False

            # Activar el modo clip y mostrar el código correspondiente
            else:
                clip_mode = True  # Activar modo clip
                clip_code = f"{current_page}{current_bank}{f_button_number}{current_camangle}"
                print(clip_mode)
                print(f"Código del clip: {clip_code}")  # Mostrar el código del clip
                save_current_clip(clip_code)
                channel_mode = get_channelmode(self)
                UIFunctions.labelPGM_PRV(self, channel_mode)
                # Remover el último carácter (letra del cam angle)
                numeric_code = clip_code[:-1]  
                # Cargar el archivo JSON
                try:
                    with open(CLIP_DICTIONARY_FILE, "r") as file:
                        clip_data = json.load(file)
                except FileNotFoundError:
                    print(f"Error: El archivo {CLIP_DICTIONARY_FILE} no existe.")
                    return None

                # Obtener la lista asignada al código
                clip_list = clip_data.get(numeric_code, ["void"] * 7)

                # Comprobar si el primer elemento de la lista es "void"
                if clip_list[0] == "void":
                    print("No hay ningún clip asignado.")
                    return None
                
                else: 
                    id = clip_list[0].zfill(4)
                    endpoint_1 = f"api/?Function=ReplayPlayEventsByID&Value={id}&Channel=1"
                    endpoint_2 = "api/?Function=ReplayPause&Channel=1"
                    UIFunctions.send_request(endpoint_1)
                    UIFunctions.send_request(endpoint_2)

                #endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
                #endpoint_2 = "api/?Function=ReplaySelectNextEvent&Channel=1"
                #UIFunctions.send_request(endpoint_1)
                
                #for _ in range(int(clip_list[0])):
                 #   UIFunctions.send_request(endpoint_2)

                
            
        def function_page(page_number):
            """Cambia la página y muestra el banco correspondiente."""
            global current_page, current_bank, SHIFT
            
            # Cambiar la página
            current_page = page_number
            save_current_page(current_page)
            self.ui.label_page.setText(f"PAGE {current_page}")  # Actualiza QLabel
            
            # Mostrar el banco de la página seleccionada
            current_bank = load_current_bank()
            self.ui.label_bank.setText(f" {current_bank} BANK")  # Actualiza QLabel
            print(f"Página {current_page} seleccionada. Banco actual: {current_bank}")

            

        def change_bank(button_number):
            """Cambia el banco para la página actual si Shift está presionado."""
            global current_bank
            if SHIFT:
                save_current_bank(button_number)
                current_bank = button_number  # Actualizamos la variable global
                self.ui.label_bank.setText(f"{current_bank} BANK")  # Actualiza QLabel
                print(f"Banco actualizado a {button_number} para la página {current_page}.")
                if current_bank == 0:
                    self.ui.label_bank.setText("   PL. BANK")  # Actualiza QLabel

            else:
                print("Shift no está presionado, no se puede cambiar el banco.")


        # Conectar los botones ya creados en Qt Designer
        self.ui.sim_f1.clicked.connect(lambda: handle_sim_f_button(self, 1))
        self.ui.sim_f2.clicked.connect(lambda: handle_sim_f_button(self, 2))
        self.ui.sim_f3.clicked.connect(lambda: handle_sim_f_button(self, 3))
        self.ui.sim_f4.clicked.connect(lambda: handle_sim_f_button(self, 4))
        self.ui.sim_f5.clicked.connect(lambda: handle_sim_f_button(self, 5))
        self.ui.sim_f6.clicked.connect(lambda: handle_sim_f_button(self, 6))
        self.ui.sim_f7.clicked.connect(lambda: handle_sim_f_button(self, 7))
        self.ui.sim_f8.clicked.connect(lambda: handle_sim_f_button(self, 8))
        self.ui.sim_f9.clicked.connect(lambda: handle_sim_f_button(self, 9))
        self.ui.sim_f10.clicked.connect(lambda: handle_sim_f_button(self, 0))


        #################################### END - BOTONS SIMULATOR
        

        #################################### START - BOTONS CONFIGURATION


        self.ui.config_ipconfig.clicked.connect(self.show_dialog_myvmix)
        self.ui.config_fastjogconfig.clicked.connect(self.show_dialog_fastjog)
        self.ui.config_deleteclipdict.clicked.connect( self.show_dialog_deleteclipdic)
        self.ui.config_resetmarks.clicked.connect(lambda: UIFunctions.function_clear_marks())




        #################################### END - BOTONS CONFIGURATION

        #################################### START - BOTONS PLAYLIST


        #################################### END - BOTONS PLAYLIST

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        
        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def show_dialog_recordtrains(self):
        self.popup = PopupRecordTrains()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_searchtc(self):
        self.popup = PopupSearchTC()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal
    

    def show_dialog_fastjog(self):
        self.popup = PopupFastJog()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_myvmix(self):
        self.popup = PopupMyVmix()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_deleteclipdic(self):
        self.popup = PopupDeleteClipDictionary()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal


    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "CLIP")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))


        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_contentacc)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "CONTENT ACCESS")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_control":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_control)
            UIFunctions.resetStyle(self, "btn_control")
            UIFunctions.labelPage(self, "CONTROL")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_export":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_export)
            UIFunctions.resetStyle(self, "btn_export")
            UIFunctions.labelPage(self, "EXPORT")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_simulator":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_simulator)
            UIFunctions.resetStyle(self, "btn_simulator")
            UIFunctions.labelPage(self, "SIMULATOR")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_generic":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_generic)
            UIFunctions.resetStyle(self, "btn_generic")
            UIFunctions.labelPage(self, "GENERIC")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_playlist":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_playlist)
            UIFunctions.resetStyle(self, "btn_playlist")
            UIFunctions.labelPage(self, "PLAYLIST")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_clipmanagement":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_clipmanagement)
            UIFunctions.resetStyle(self, "btn_clipmanagement")
            UIFunctions.labelPage(self, "CLIP MANAGEMENT")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            
        if btnWidget.objectName() == "btn_config":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_configuration)
            UIFunctions.resetStyle(self, "btn_config")
            UIFunctions.labelPage(self, "CONFIGURATION")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    """""
        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "CONFIGURATION")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    """
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    """""
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##
    """

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
