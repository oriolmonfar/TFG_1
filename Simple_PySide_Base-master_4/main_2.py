
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QTimer,QEventLoop)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMouseEvent)
from PySide2.QtWidgets import *
import time
from datetime import datetime
import requests
import threading
import serial



# GUI FILE
from app_modules import *
from ui_popup_searchtc import Ui_Dialog as Dialog_searchtc
from ui_popup_delete_marks import Ui_Dialog as Dialog_deletemarks
from ui_popup_name_clip import Ui_Dialog as Dialog_nameclip
from ui_popup_fastjog import Ui_Dialog as Dialog_fastjog
from ui_popup_ipconfig import Ui_Dialog as Dialog_ipconfig
from ui_popup_myvmix import Ui_Dialog as Dialog_myvmix
from ui_popup_deleteip import Ui_Dialog as Dialog_deleteip
from ui_popup_confirm_no_connection import Ui_Dialog as Dialog_no_connection
from ui_popup_confirm_connected import Ui_Dialog as Dialog_connected
from ui_popup_overwrite_clip import Ui_Dialog as Dialog_overwrite
from ui_popup_delete_clip_dictionary import Ui_Dialog as Dialog_delete_clip_dictionary
from ui_popup_modo_page import Ui_Dialog as Dialog_modo_page
from config_manager import *


NUM_LEDS = 30
#SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_PORT = "COM10"
BAUDRATE = 115200

#DECLARE GLOBAL VARIABLES
IP_VMIX = load_ip_vmix()
FAST_JOG = load_fast_jog()
SEC_FAST_JOG = load_sec_fast_jog()
SHIFT = False
current_page = load_current_page()
current_bank = load_current_bank()
current_clip = load_current_clip()
current_clip_pgm = load_current_clip_pgm()
current_clip_prv = load_current_clip_prv()
current_camangle = load_current_camangle()
current_camangleA = load_current_camangleA()
current_camangleB = load_current_camangleB()
clip_mode = load_clip_mode()
modo_page = False
clip_id = load_current_clip_id()
last_date = load_last_date()
last_time = load_last_time()
mark_in_tc = load_mark_in_tc()
estrella1 = load_estrella1_list()
estrella2 = load_estrella2_list()
estrella3 = load_estrella3_list()
modo_playlist = False
active_playlist = load_active_playlist()
playlist1 = load_plst(1)
playlist2 = load_plst(2)
playlist3 = load_plst(3)
playlist4 = load_plst(4)
playlist5 = load_plst(5)
playlist6 = load_plst(6)
playlist7 = load_plst(7)
playlist8 = load_plst(8)
playlist9 = load_plst(9)
playlist10 = load_plst(10)
playlist11 = load_plst(11)
playlist12 = load_plst(12)
playlist13 = load_plst(13)
playlist14 = load_plst(14)
playlist15 = load_plst(15)
playlist16 = load_plst(16)
playlist17 = load_plst(17)
playlist18 = load_plst(18)
CLEAR_MODE = False
CLEAR_SELECTION = None
browse_mode = False
modo_loop = False

########################################################################
## START - POPUPS CLASSES
########################################################################

class PopupModoPage(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_modo_page()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.NonModal)

        self.ui.minimize_modo_page.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_modo_page.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_modo_page.clicked.connect(lambda: self.close())


    def cancel(self): 
        global modo_page
        modo_page = False
        save_page_mode(modo_page)
        print(f'modo safe desactivado : {modo_page}')
        self.close()
    
    def close_popup(self):
        self.close()


class PopupNameClip(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialog_nameclip()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.minimize_nameclip.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_nameclip.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.close_nameclip.clicked.connect(lambda: self.close())

        # Conectar botones para escribir en el QTextEdit
        self.ui.nameclip_0.clicked.connect(lambda: self.write("0"))
        self.ui.nameclip_1.clicked.connect(lambda: self.write("1"))
        self.ui.nameclip_2.clicked.connect(lambda: self.write("2"))
        self.ui.nameclip_3.clicked.connect(lambda: self.write("3"))
        self.ui.nameclip_4.clicked.connect(lambda: self.write("4"))
        self.ui.nameclip_5.clicked.connect(lambda: self.write("5"))
        self.ui.nameclip_6.clicked.connect(lambda: self.write("6"))
        self.ui.nameclip_7.clicked.connect(lambda: self.write("7"))
        self.ui.nameclip_8.clicked.connect(lambda: self.write("8"))
        self.ui.nameclip_9.clicked.connect(lambda: self.write("9"))
        self.ui.nameclip_A.clicked.connect(lambda: self.write("A"))
        self.ui.nameclip_B.clicked.connect(lambda: self.write("B"))
        self.ui.nameclip_C.clicked.connect(lambda: self.write("C"))
        self.ui.nameclip_D.clicked.connect(lambda: self.write("D"))
        self.ui.nameclip_E.clicked.connect(lambda: self.write("E"))
        self.ui.nameclip_F.clicked.connect(lambda: self.write("F"))
        self.ui.nameclip_G.clicked.connect(lambda: self.write("G"))
        self.ui.nameclip_H.clicked.connect(lambda: self.write("H"))
        self.ui.nameclip_I.clicked.connect(lambda: self.write("I"))
        self.ui.nameclip_J.clicked.connect(lambda: self.write("J"))
        self.ui.nameclip_K.clicked.connect(lambda: self.write("K"))
        self.ui.nameclip_L.clicked.connect(lambda: self.write("L"))
        self.ui.nameclip_M.clicked.connect(lambda: self.write("M"))
        self.ui.nameclip_N.clicked.connect(lambda: self.write("N"))
        self.ui.nameclip_O.clicked.connect(lambda: self.write("O"))
        self.ui.nameclip_P.clicked.connect(lambda: self.write("P"))
        self.ui.nameclip_Q.clicked.connect(lambda: self.write("Q"))
        self.ui.nameclip_R.clicked.connect(lambda: self.write("R"))
        self.ui.nameclip_S.clicked.connect(lambda: self.write("S"))
        self.ui.nameclip_T.clicked.connect(lambda: self.write("T"))
        self.ui.nameclip_U.clicked.connect(lambda: self.write("U"))
        self.ui.nameclip_V.clicked.connect(lambda: self.write("V"))
        self.ui.nameclip_W.clicked.connect(lambda: self.write("W"))
        self.ui.nameclip_X.clicked.connect(lambda: self.write("X"))
        self.ui.nameclip_Y.clicked.connect(lambda: self.write("Y"))
        self.ui.nameclip_Z.clicked.connect(lambda: self.write("Z"))
        self.ui.nameclip_barra.clicked.connect(lambda: self.write("-"))
        self.ui.nameclip_barra_baixa.clicked.connect(lambda: self.write("_"))
        self.ui.nameclip_punt.clicked.connect(lambda: self.write("."))
        self.ui.nameclip_dospunts.clicked.connect(lambda: self.write(":"))
        self.ui.nameclip_delete.clicked.connect(lambda: self.delete())
        self.ui.nameclip_confirm.clicked.connect(lambda: self.confirm())

        # Inicialmente, no hay QTextEdit activo
        self.active_textedit = None

        # Conectar eventos de foco para detectar qué QTextEdit está seleccionado

    def write(self, text):
        self.ui.textedit_clipname_name.insertPlainText(text)

    def delete(self):
        """Elimina el último carácter directamente en la interfaz"""
        if self.ui.textedit_clipname_name:  # Verifica que el QTextEdit esté inicializado
            cursor = self.ui.textedit_clipname_name.textCursor()  # Obtiene el cursor de QTextEdit
            cursor.movePosition(cursor.End)  # Mueve el cursor al final
            cursor.deletePreviousChar()  # Borra el último carácter

    def confirm(self):
        current_clip = load_current_clip()
        numeric_code = current_clip[:-1]
        texto = self.ui.textedit_clipname_name.toPlainText().strip()

        clip_data = load_clip_dictionary()
        if numeric_code in clip_data:
            clip_entry = clip_data[numeric_code]

            # Extraer información con valores por defecto
            id = clip_entry[0]
            clip_entry[1] = f"{texto}"

        save_clip_dictionary(clip_data)

        endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
        endpoint_2 = "api/?Function=ReplaySelectNextEvent&Channel=1"
        UIFunctions.send_request(endpoint_1)

        for _ in range(int(id)):
            UIFunctions.send_request(endpoint_2)

        endpoint_3 = f"api/?Function=ReplaySetSelectedEventText&Value={texto}"
        UIFunctions.send_request(endpoint_3)

        time.sleep(0.1)
        self.close()

class PopupDeleteMarks(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.ui = Dialog_deletemarks()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ## ==> MAXIMIZE/RESTORE
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_confirm_deletemarks.clicked.connect(lambda: self.close())
        self.ui.confirm_deletemarks_no.clicked.connect(lambda: self.close())
        self.ui.confirm_deletemarks_yes.clicked.connect(lambda: PopupDeleteMarks.yes(self))

    def yes(self):
        """
        Vacía la lista de timecodes.
        """
        global timecodes, lastmark_index
        timecodes = []
        save_timecodes_list(timecodes)
        lastmark_index = -1
        print("Lista de timecodes vaciada.")

        time.sleep(0.1)
        self.close()

class PopupOverwriteClip(QDialog):  

    def __init__(self, clip_code, clip_management):  
        super().__init__()  
        self.ui = Dialog_overwrite()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ## ==> MAXIMIZE/RESTORE
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_overwrite.clicked.connect(lambda: self.close())
        self.ui.overwrite_no.clicked.connect(lambda: self.no(clip_code))
        self.ui.overwrite_yes.clicked.connect(lambda: self.yes(clip_code, clip_management))

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

    def no(self, clip_code): 
        endpoint_1 = "api/?Function=ReplaySelectFirstEvent&Channel=1"
        endpoint_2 = "api/?Function=ReplaySelectNextEvent&Channel=1"
        PopupOverwriteClip.send_request(endpoint_1)
        id = load_current_clip_id()
        for _ in range(int(id)):
            PopupOverwriteClip.send_request(endpoint_2) 
        id += 1
        save_current_clip_id(id)
        time.sleep(0.1)
        endpoint = f"api/?Function=ReplayDeleteSelectedEvent&Value=1&Channel=1"
        PopupOverwriteClip.send_request(endpoint)
        time.sleep(0.1)
        self.close()

class PopupDeleteClipDictionary(QDialog):  
    def __init__(self, main_window):  
        super().__init__()  
        self.ui = Dialog_delete_clip_dictionary()  # Instancia de la UI generada
        self.ui.setupUi(self)  # Aplica la UI a la ventana de diálogo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ## ==> MAXIMIZE/RESTORE
        ## SHOW ==> CLOSE APPLICATION
        self.ui.close_confirm_deleteclipdic.clicked.connect(lambda: self.close())
        self.ui.confirm_deleteclipdic_no.clicked.connect(lambda: self.close())
        self.ui.confirm_deleteclipdic_yes.clicked.connect(lambda: reset_clip_dictionary_and_clip_id(self))

        def reset_clip_dictionary_and_clip_id(self):
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

            # Guardar las listas de las playlists vacías
            for i in range(1, 19):  # Desde playlist1 hasta playlist18
                save_plst(i, [])  # Guardar la lista vacía en la función save_plst

            save_estrella1_list([])
            save_estrella2_list([])
            save_estrella3_list([])

            save_current_clip(" ")
            save_current_clip_pgm(" ")
            save_current_clip_prv(" ")

            save_current_camangle(" ")
            save_current_camangleA(" ")
            save_current_camangleB(" ")

            pgm = UIFunctions.get_channelmode()
            UIFunctions.labelPGM_PRV(main_window, pgm)
            
            PopupDeleteMarks.yes(self)
            
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
        last_date = load_last_date()
        last_time = load_last_time()
        texto = self.ui.searchtc_textedit.toPlainText()  # Recupera el texto
        date = datetime.now().date()
        last_time = save_last_time(str(texto))
        last_date = save_last_date(str(date))
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

        self.ui.tabWidget.setTabText(0, "Fast Jog")
        self.ui.tabWidget.setTabText(1, "2nd Fast Jog")

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

        self.ui.sec_fastjogconfig_0.clicked.connect(lambda: self.write_sec("0"))
        self.ui.sec_fastjogconfig_1.clicked.connect(lambda: self.write_sec("1"))
        self.ui.sec_fastjogconfig_2.clicked.connect(lambda: self.write_sec("2"))
        self.ui.sec_fastjogconfig_3.clicked.connect(lambda: self.write_sec("3"))
        self.ui.sec_fastjogconfig_4.clicked.connect(lambda: self.write_sec("4"))
        self.ui.sec_fastjogconfig_5.clicked.connect(lambda: self.write_sec("5"))
        self.ui.sec_fastjogconfig_6.clicked.connect(lambda: self.write_sec("6"))
        self.ui.sec_fastjogconfig_7.clicked.connect(lambda: self.write_sec("7"))
        self.ui.sec_fastjogconfig_8.clicked.connect(lambda: self.write_sec("8"))
        self.ui.sec_fastjogconfig_9.clicked.connect(lambda: self.write_sec("9"))
        self.ui.sec_fastjogconfig_delete.clicked.connect(lambda: self.delete_sec())
        self.ui.sec_fastjogconfig_confirm.clicked.connect(lambda: self.confirm_sec())

        # Inicializar con el valor actual de FAST_JOG
        self.ui.textedit_fastjog.setPlainText(str(FAST_JOG))  
        self.ui.textedit_sec_fastjog.setPlainText(str(SEC_FAST_JOG)) 

        

    def write(self, text):
        self.ui.textedit_fastjog.insertPlainText(text)

    def write_sec(self, text):
        self.ui.textedit_sec_fastjog.insertPlainText(text)

    def delete(self):
        if self.ui.textedit_fastjog:
            cursor = self.ui.textedit_fastjog.textCursor()
            cursor.movePosition(cursor.End)
            cursor.deletePreviousChar()

    def delete_sec(self):
        if self.ui.textedit_sec_fastjog:
            cursor = self.ui.textedit_sec_fastjog.textCursor()
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

    def confirm_sec(self):
        global SEC_FAST_JOG  # Asegurar que trabajamos con la variable global

        texto = self.ui.textedit_sec_fastjog.toPlainText().strip()
        if texto.isdigit():  
            save_sec_fast_jog(int(texto))  # Guardamos el nuevo valor en el JSON
            
            # Recargamos la variable global desde el archivo JSON
            SEC_FAST_JOG = load_sec_fast_jog()

            print(f"Nuevo valor de SEC_FAST_JOG guardado y recargado: {SEC_FAST_JOG}")
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

########################################################################
## END - POPUPS CLASSES
########################################################################



########################################################################
## START - MAINWINDOW
########################################################################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #SET LED COLORS
        self.led_colors = [QColor(0,0,0) for _ in range(NUM_LEDS)]
       
        try:
            self.ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
        except serial.SerialException as e:
            print(f"Error obrint el port serial dels leds ESP32: {e}")
            self.ser = None

        UIFunctions.start_cam_angle_monitor(self)
        UIFunctions.start_available_clips_monitor(self)
        UIFunctions.function_record(self)
        UIFunctions.function_e_e(self)
        UIFunctions.check_vmix_connection(self)
        UIFunctions.start_connection_monitor(self)
        UIFunctions.start_modo_playlist_monitor(self)




        #REMOVE TITLE BAR
        UIFunctions.removeTitleBar(True)

        #SET WINDOW TITLE AND PAGE - BANK LABEL
        self.setWindowTitle('Main Window - Python Base')
        self.ui.label_page.setText(f"PAGE {current_page}  ")
        label_bank = current_bank
        if label_bank == 0:
            text = "PL"
        else: 
            text = current_bank
        self.ui.label_bank.setText(f" {text} BANK")  # Actualiza Q
        UIFunctions.labelDescription(self, f"{active_playlist}")



        #SET PGM - PRV (or LINKED A|B)

        pgm = UIFunctions.get_channelmode()

        angleA, angleB = UIFunctions.get_vmix_replay_cameras()

        if pgm == "B":

            save_current_camangle(angleB)
        else: 
            save_current_camangle(angleA)
        
        save_current_camangleA(angleA)
        save_current_camangleB(angleB)

        ## Set window size
        startSize = QSize(1024, 600)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        #self.showFullScreen()

        #################################### START - CREATE MENUS
        # Toggle menu size
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # Add menus
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "CLIP", "btn_home", "url(:/16x16/icons/16x16/cil-media-play.png)", True)
        UIFunctions.addNewMenu(self, "CONTENT ACCESS", "btn_new_user", "url(:/16x16/icons/16x16/cil-input.png)", True)
        UIFunctions.addNewMenu(self, "CONTROL", "btn_control", "url(:/16x16/icons/16x16/cil-clipboard.png)", True)
        UIFunctions.addNewMenu(self, "EXPORT", "btn_export", "url(:/16x16/icons/16x16/cil-paper-plane.png)", True)
        UIFunctions.addNewMenu(self, "PLAYLIST", "btn_playlist", "url(:/16x16/icons/16x16/cil-library-add.png)", True)
        UIFunctions.addNewMenu(self, "SIMULATOR", "btn_simulator", "url(:/16x16/icons/16x16/cil-devices.png)", True)
        UIFunctions.addNewMenu(self, "CONFIGURATION", "btn_config", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        
        # Standard Menu
        UIFunctions.selectStandardMenu(self, "btn_home")

        #Starting Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        ## Hide user icon
        UIFunctions.userIcon(self, "WM", "", False)
        #################################### END - CREATE MENUS

        #################################### START - MOVE WINDOW - MAXIMIZE - RESTORE - CLOSE
        def moveWindow(event):
            # If maximized change to normal
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # Move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Widget to move
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        #Load uiDefinitions
        UIFunctions.uiDefinitions(self)
        #################################### END - MOVE WINDOW - MAXIMIZE - RESTORE - CLOSE

        
        ########################################################################
        ## START - BUTTON ASSIGNMENT
        ######################################################################## 

        #################################### START- BOTONS CLIP
        self.ui.clip_addtoplaylist.clicked.connect(lambda: UIFunctions.clip_gotopl(self))
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
        self.ui.estrella1_add.clicked.connect(lambda: UIFunctions.function_estrella1(self))
        self.ui.estrella2_add.clicked.connect(lambda: UIFunctions.function_estrella2(self))
        self.ui.estrella3_add.clicked.connect(lambda: UIFunctions.function_estrella3(self))
        self.ui.clip_nameclip.clicked.connect(lambda: self.show_dialog_nameclip())
        #################################### END - BOTONS CLIP

        #################################### START - BOTONS CONTENT ACCESS
        UIFunctions.restore_all_playlists_on_startup(self)
        self.ui.contec_acc_actualclip.setAlignment(Qt.AlignCenter)
        self.ui.contec_acc_actualclip.setText(f"{current_clip}")
        self.ui.cont_acc_actualplaylist.setText(f"{active_playlist}")
        self.ui.cont_acc_actualplaylist.clicked.connect(lambda: UIFunctions.cont_acc_gotopl(self))
        self.ui.cont_acc_page.clicked.connect(lambda: function_page_activate())
        self.ui.cont_acc_mark.clicked.connect(lambda: UIFunctions.function_mark())
        self.ui.cont_acc_lastmark.clicked.connect(lambda: UIFunctions.function_lastmark())
        self.ui.cont_acc_lasttc.clicked.connect(lambda: UIFunctions.function_lasttc())
        #################################### END - BOTONS CONTENT ACCESS

        #################################### START - BOTONS CONTROL
        self.ui.control_syncprv.clicked.connect(lambda: UIFunctions.function_syncprv(self))
        self.ui.control_prv_ctl.clicked.connect(lambda: UIFunctions.function_prvctl(self))
        self.ui.control_loop.clicked.connect(lambda: UIFunctions.function_loop(self))
        self.ui.control_fast_jog.clicked.connect(lambda: UIFunctions.function_fastjog(self, self.dial))
        self.ui.control_2ndfastjog.clicked.connect(lambda: UIFunctions.function_sec_fastjog(self, self.dial))
        self.ui.control_gotoin.clicked.connect(lambda: UIFunctions.function_gotoin())
        self.ui.control_gotoout.clicked.connect(lambda: UIFunctions.function_gotoout())
        self.ui.control_cancel_in.clicked.connect(lambda: UIFunctions.function_cancel_in(self))
        self.ui.control_gototc.clicked.connect(self.show_dialog_searchtc)
        #################################### END - BOTONS CONTROL

        #################################### START - BOTONS EXPORT
        self.ui.export_playlist.clicked.connect(lambda: UIFunctions.export_playlist())
        self.ui.export_export_clip.clicked.connect(lambda: UIFunctions.export_clip())
        #################################### END - BOTONS EXPORT

        #################################### START- BOTONS SIMULATOR
        self.ui.sim_shift.setCheckable(True)
        self.ui.sim_shift.clicked.connect(lambda: toggle_shift(self))

        self.ui.sim_clear.setCheckable(True)
        self.ui.sim_clear.clicked.connect(lambda: toggle_clear_mode(self))

        def execute_functions_A(self):
            """Ejecuta la función correspondiente según el estado de SHIFT."""
            global SHIFT, clip_mode, current_camangle, current_clip, current_camangleA, current_camangleB
            clip_mode = load_clip_mode()
            if clip_mode:
                channel_mode = UIFunctions.get_channelmode()
                save_current_camangle("A")
                new_angle = load_current_camangle()  # Cargar el clip actual desde vMix
                if channel_mode == 'A':
                    if new_angle != current_camangleA:
                        current_camangle = new_angle
                        current_camangleA = new_angle
                        save_current_camangleA(current_camangleA)
                        current_clip = load_current_clip()
                    clip_no_camangle = current_clip_pgm[:-1]
                    save_current_clip_pgm(f"{clip_no_camangle}{current_camangleA}")
                    print(current_clip_pgm)
                    UIFunctions.labelPGM_PRV(self, channel_mode)
                    endpoint = "api/?Function=ReplayToggleSelectedEventCamera1"
                    UIFunctions.send_request(endpoint)
                    print(f"angle asignado al canal A (PGM): {current_camangleA}")
                elif channel_mode == 'B':
                    if new_angle != current_camangleB:
                        current_camangle = new_angle
                        current_camangleB = new_angle
                        save_current_camangleB(current_camangleB)
                        clip_no_camangle = current_clip_prv[:-1]
                        save_current_clip_prv(f"{clip_no_camangle}{current_camangleB}")
                        print(current_clip_prv)
                        UIFunctions.labelPGM_PRV(self, channel_mode)
                        endpoint = "api/?Function=ReplayToggleSelectedEventCamera1"
                        UIFunctions.send_request(endpoint)
                        print(f"Angle asignado al canal B (PRV): {current_camangleB}")
            else: 
                if SHIFT:
                    UIFunctions.function_A(self)
                    reset_shift(self)
                else: 
                    UIFunctions.function_A(self)
        self.ui.sim_A.clicked.connect(lambda: execute_functions_A(self))

        def execute_functions_B(self):
            global SHIFT, clip_mode, current_camangle, current_clip, current_camangleA, current_camangleB
            clip_mode = load_clip_mode()
            if clip_mode:
                channel_mode = UIFunctions.get_channelmode()
                save_current_camangle("B")
                new_angle = load_current_camangle()  # Cargar el clip actual desde vMix
                if channel_mode == 'A':
                    if new_angle != current_camangleA:
                        current_camangle = new_angle
                        current_camangleA = new_angle
                        save_current_camangleA(current_camangleA)
                        current_clip = load_current_clip()
                    clip_no_camangle = current_clip_pgm[:-1]
                    save_current_clip_pgm(f"{clip_no_camangle}{current_camangleA}")
                    print(current_clip_pgm)
                    UIFunctions.labelPGM_PRV(self, channel_mode)
                    endpoint = "api/?Function=ReplayToggleSelectedEventCamera2"
                    UIFunctions.send_request(endpoint)
                    print(f"angle asignado al canal A (PGM): {current_camangleA}")
                elif channel_mode == 'B':
                    if new_angle != current_camangleB:
                        current_camangle = new_angle
                        current_camangleB = new_angle
                        save_current_camangleB(current_camangleB)
                        clip_no_camangle = current_clip_prv[:-1]
                        save_current_clip_prv(f"{clip_no_camangle}{current_camangleB}")
                        print(current_clip_prv)
                        UIFunctions.labelPGM_PRV(self, channel_mode)
                        endpoint = "api/?Function=ReplayToggleSelectedEventCamera2"
                        UIFunctions.send_request(endpoint)
                        print(f"Angle asignado al canal B (PRV): {current_camangleB}")
            else: 
                if SHIFT:
                    UIFunctions.function_B(self)
                    reset_shift(self)
                else:
                    UIFunctions.function_B(self)
        self.ui.sim_B.clicked.connect(lambda: execute_functions_B(self))

        def execute_functions_C(self):
            global SHIFT, clip_mode, current_camangle, current_clip, current_camangleA, current_camangleB
            clip_mode = load_clip_mode()
            if clip_mode:
                channel_mode = UIFunctions.get_channelmode()
                save_current_camangle("C")
                new_angle = load_current_camangle()  # Cargar el clip actual desde vMix
                if channel_mode == 'A':
                    if new_angle != current_camangleA:
                        current_camangle = new_angle
                        current_camangleA = new_angle
                        save_current_camangleA(current_camangleA)
                        current_clip = load_current_clip()
                    clip_no_camangle = current_clip_pgm[:-1]
                    save_current_clip_pgm(f"{clip_no_camangle}{current_camangleA}")
                    print(current_clip_pgm)
                    UIFunctions.labelPGM_PRV(self, channel_mode)
                    endpoint = "api/?Function=ReplayToggleSelectedEventCamera3"
                    UIFunctions.send_request(endpoint)
                    print(f"angle asignado al canal A (PGM): {current_camangleA}")
                elif channel_mode == 'B':
                    if new_angle != current_camangleB:
                        current_camangle = new_angle
                        current_camangleB = new_angle
                        save_current_camangleB(current_camangleB)
                        clip_no_camangle = current_clip_prv[:-1]
                        save_current_clip_prv(f"{clip_no_camangle}{current_camangleB}")
                        print(current_clip_prv)
                        UIFunctions.labelPGM_PRV(self, channel_mode)
                        endpoint = "api/?Function=ReplayToggleSelectedEventCamera3"
                        UIFunctions.send_request(endpoint)
                        print(f"Angle asignado al canal B (PRV): {current_camangleB}")
            else: 
                if SHIFT:
                    UIFunctions.function_C(self)
                    reset_shift(self)
                else:
                    UIFunctions.function_C(self)
        self.ui.sim_C.clicked.connect(lambda: execute_functions_C(self))

        def execute_functions_D(self):
            global SHIFT, clip_mode, current_camangle, current_clip, current_camangleA, current_camangleB
            clip_mode = load_clip_mode()
            if clip_mode:
                channel_mode = UIFunctions.get_channelmode()
                save_current_camangle("D")
                new_angle = load_current_camangle()  # Cargar el clip actual desde vMix
                if channel_mode == 'A':
                    if new_angle != current_camangleA:
                        current_camangle = new_angle
                        current_camangleA = new_angle
                        save_current_camangleA(current_camangleA)
                        current_clip = load_current_clip()
                    clip_no_camangle = current_clip_pgm[:-1]
                    save_current_clip_pgm(f"{clip_no_camangle}{current_camangleA}")
                    print(current_clip_pgm)
                    UIFunctions.labelPGM_PRV(self, channel_mode)
                    endpoint = "api/?Function=ReplayToggleSelectedEventCamera4"
                    UIFunctions.send_request(endpoint)
                    print(f"angle asignado al canal A (PGM): {current_camangleA}")
                elif channel_mode == 'B':
                    if new_angle != current_camangleB:
                        current_camangle = new_angle
                        current_camangleB = new_angle
                        save_current_camangleB(current_camangleB)
                        clip_no_camangle = current_clip_prv[:-1]
                        save_current_clip_prv(f"{clip_no_camangle}{current_camangleB}")
                        print(current_clip_prv)
                        UIFunctions.labelPGM_PRV(self, channel_mode)
                        endpoint = "api/?Function=ReplayToggleSelectedEventCamera4"
                        UIFunctions.send_request(endpoint)
                        print(f"Angle asignado al canal B (PRV): {current_camangleB}")
            else: 
                if SHIFT:
                    UIFunctions.function_D(self)
                    reset_shift(self)
                else:
                    UIFunctions.function_D(self)
        self.ui.sim_D.clicked.connect(lambda: execute_functions_D(self))

        def execute_functions_play(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_play()
                reset_shift(self)
            else:
                UIFunctions.function_play(self)
        self.ui.sim_play.clicked.connect(lambda: execute_functions_play(self))

        def execute_functions_gototc(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gototc(self)
                reset_shift(self)
            else:
                UIFunctions.function_lastmark()
        self.ui.sim_gototc.clicked.connect(lambda: execute_functions_gototc(self))

        def execute_functions_fastjog(self, dial):
            global SHIFT
            if SHIFT:
                UIFunctions.function_fastjog(self, dial)
                reset_shift(self)
            else:
                UIFunctions.function_mark()
        self.ui.sim_fastjog.clicked.connect(lambda: execute_functions_fastjog(self, self.dial))

        def execute_functions_record(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_record(self)
                reset_shift(self)
            else:
                UIFunctions.function_e_e(self)
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
                UIFunctions.function_loop(self)
                reset_shift(self)
            else:
                UIFunctions.cont_acc_gotopl(self)
        self.ui.sim_loop.clicked.connect(lambda: execute_functions_loop(self))

        def execute_functions_insert(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_cancel_in(self)
                reset_shift(self)
            else:
                UIFunctions.toggle_browse_mode(self)
        self.ui.sim_insert.clicked.connect(lambda: execute_functions_insert(self))

        def execute_functions_in(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gotoin()
                reset_shift(self)
            else:
                UIFunctions.function_in(self)

        def handle_sim_in(self):
            global CLEAR_MODE, CLEAR_SELECTION
            if CLEAR_MODE:
                CLEAR_SELECTION = "in"
                print("Modo CLEAR: Seleccionado IN")
                UIFunctions.send_request("api/?Function=ReplayUpdateSelectedInPoint&Channel=1")
                reset_clear_mode(self)  # Se desactiva el modo después de la request
            else:
                execute_functions_in(self)
        self.ui.sim_in.clicked.connect(lambda: handle_sim_in(self))

        def execute_functions_out(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_gotoout()
                reset_shift(self)
            else:
                function_out(self)
        def handle_sim_out(self):
            global CLEAR_MODE, CLEAR_SELECTION
            if CLEAR_MODE:
                CLEAR_SELECTION = "out"
                print("Modo CLEAR: Seleccionado OUT")
                UIFunctions.send_request("api/?Function=ReplayUpdateSelectedOutPoint&Channel=1")
                reset_clear_mode(self)  # Se desactiva el modo después de la request
            else:
                execute_functions_out(self)            
        self.ui.sim_out.clicked.connect(lambda: handle_sim_out(self))
            
        def execute_functions_take(self):
            global SHIFT
            if SHIFT:
                UIFunctions.function_lever()
                reset_shift(self)
            else:
                UIFunctions.function_take()
        self.ui.sim_take.clicked.connect(lambda: execute_functions_take(self))

        self.ui.sim_rodeta.setMinimum(0)
        self.ui.sim_rodeta.setMaximum(100)
        self.ui.sim_rodeta.setWrapping(True)  # Hacer que el dial sea cíclico
        self.dial = self.findChild(QDial, "sim_rodeta")  # Busca el QDial en la UI
        UIFunctions.function_rodeta(self, self.dial)  # Configura el dial

        self.slider = self.findChild(QSlider, "sim_palanqueta")  # Find the slider
        UIFunctions.setup_replay_speed_slider(self.slider)  # Setup slider functionality

        def function_menu(self):
            global modo_page
            if modo_page: 
                self.popup_modo_page.cancel()
            else:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_configuration)

        self.ui.sim_menu.clicked.connect(lambda: function_menu(self))
        self.ui.sim_enter.clicked.connect(lambda: UIFunctions.function_enter(self))
        #################################### END - BOTONS SIMULATOR

        #################################### START - BOTONS PLAYLIST
        self.ui.playlist_btnadd_1.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 1))
        self.ui.playlist_btnadd_2.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 2))
        self.ui.playlist_btnadd_3.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 3))
        self.ui.playlist_btnadd_4.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 4))
        self.ui.playlist_btnadd_5.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 5))
        self.ui.playlist_btnadd_6.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 6))
        self.ui.playlist_btnadd_7.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 7))
        self.ui.playlist_btnadd_8.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 8))
        self.ui.playlist_btnadd_9.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 9))
        self.ui.playlist_btnadd_10.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 10))
        self.ui.playlist_btnadd_11.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 11))
        self.ui.playlist_btnadd_12.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 12))
        self.ui.playlist_btnadd_13.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 13))
        self.ui.playlist_btnadd_14.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 14))
        self.ui.playlist_btnadd_15.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 15))
        self.ui.playlist_btnadd_16.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 16))
        self.ui.playlist_btnadd_17.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 17))
        self.ui.playlist_btnadd_18.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 18))

        self.ui.pl1_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 1))
        self.ui.pl2_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 2))
        self.ui.pl3_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 3))
        self.ui.pl4_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 4))
        self.ui.pl5_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 5))
        self.ui.pl6_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 6))
        self.ui.pl7_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 7))
        self.ui.pl8_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 8))
        self.ui.pl9_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 9))
        self.ui.pl10_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 10))
        self.ui.pl11_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 11))
        self.ui.pl12_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 12))
        self.ui.pl13_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 13))
        self.ui.pl14_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 14))
        self.ui.pl15_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 15))
        self.ui.pl16_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 16))
        self.ui.pl17_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 17))
        self.ui.pl18_add.clicked.connect(lambda: UIFunctions.add_to_playlist(self, 18))


        self.ui.playlist_button_pl1.clicked.connect(lambda: UIFunctions.goto_pl(self, 1))
        self.ui.playlist_button_pl2.clicked.connect(lambda: UIFunctions.goto_pl(self, 2))
        self.ui.playlist_button_pl3.clicked.connect(lambda: UIFunctions.goto_pl(self, 3))
        self.ui.playlist_button_pl4.clicked.connect(lambda: UIFunctions.goto_pl(self, 4))
        self.ui.playlist_button_pl5.clicked.connect(lambda: UIFunctions.goto_pl(self, 5))
        self.ui.playlist_button_pl6.clicked.connect(lambda: UIFunctions.goto_pl(self, 6))
        self.ui.playlist_button_pl7.clicked.connect(lambda: UIFunctions.goto_pl(self, 7))
        self.ui.playlist_button_pl8.clicked.connect(lambda: UIFunctions.goto_pl(self, 8))
        self.ui.playlist_button_pl9.clicked.connect(lambda: UIFunctions.goto_pl(self, 9))
        self.ui.playlist_button_pl10.clicked.connect(lambda: UIFunctions.goto_pl(self, 10))
        self.ui.playlist_button_pl11.clicked.connect(lambda: UIFunctions.goto_pl(self, 11))
        self.ui.playlist_button_pl12.clicked.connect(lambda: UIFunctions.goto_pl(self, 12))
        self.ui.playlist_button_pl13.clicked.connect(lambda: UIFunctions.goto_pl(self, 13))
        self.ui.playlist_button_pl14.clicked.connect(lambda: UIFunctions.goto_pl(self, 14))
        self.ui.playlist_button_pl15.clicked.connect(lambda: UIFunctions.goto_pl(self, 15))
        self.ui.playlist_button_pl16.clicked.connect(lambda: UIFunctions.goto_pl(self, 16))
        self.ui.playlist_button_pl17.clicked.connect(lambda: UIFunctions.goto_pl(self, 17))
        self.ui.playlist_button_pl18.clicked.connect(lambda: UIFunctions.goto_pl(self, 18))

        self.ui.pl1_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 1))
        self.ui.pl2_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 2))
        self.ui.pl3_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 3))
        self.ui.pl4_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 4))
        self.ui.pl5_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 5))
        self.ui.pl6_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 6))
        self.ui.pl7_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 7))
        self.ui.pl8_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 8))
        self.ui.pl9_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 9))
        self.ui.pl10_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 10))
        self.ui.pl11_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 11))
        self.ui.pl12_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 12))
        self.ui.pl13_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 13))
        self.ui.pl14_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 14))
        self.ui.pl15_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 15))
        self.ui.pl16_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 16))
        self.ui.pl17_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 17))
        self.ui.pl18_delete.clicked.connect(lambda: UIFunctions.delete_element_plst(self, 18))
        #################################### END - BOTONS PLAYLIST
        
        #################################### START - BOTONS CONFIGURATION
        self.ui.config_ipconfig.clicked.connect(self.show_dialog_myvmix)
        self.ui.config_fastjogconfig.clicked.connect(self.show_dialog_fastjog)
        self.ui.config_deleteclipdict.clicked.connect( self.show_dialog_deleteclipdic)
        self.ui.config_resetmarks.clicked.connect(self.show_dialog_delete_marks)
        self.ui.config_refresh_multi.clicked.connect(lambda: UIFunctions.send_request("api/?Function=BrowserNavigate&Input=8&Value=http://localhost:5000/"))
        #################################### END - BOTONS CONFIGURATION


        ########################################################################
        ## END - BUTTON ASSIGNMENT
        ########################################################################


        ########################################################################
        ## START - CLIP MANAGEMENT
        ########################################################################

        def toggle_shift(self):
            """Alterna el estado de SHIFT y cambia el color del botón."""
            global SHIFT
            SHIFT = load_shift()
            SHIFT = not SHIFT

            if SHIFT:
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: rgba(255,40,40,150);} QPushButton:hover {background-color: rgba(255,40,40,50);} QPushButton:pressed { background-color: rgba(255,40,40,50);}")  # Rojo cuando está activado
                self.setLeds(1, QColor(255,0,0))
            else:
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}")   # Transparente cuando está desactivado
                self.setLeds(1, QColor(0,0,0))

            print(f"Shift activado: {SHIFT}")  # Depuración
            save_shift(SHIFT)

        def reset_shift(self):
            """Desactiva SHIFT si está activado y restablece el color."""
            global SHIFT
            SHIFT = load_shift()
            if SHIFT:
                SHIFT = False
                self.ui.sim_shift.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}") 
                self.setLeds(1, QColor(0,0,0))
                print("Shift desactivado")
                save_shift(SHIFT)

        def toggle_clear_mode(self):
            """Activa o desactiva el modo CLEAR y espera la selección de IN u OUT."""
            global CLEAR_MODE, CLEAR_SELECTION
            CLEAR_MODE = not CLEAR_MODE

            if CLEAR_MODE:
                self.ui.sim_clear.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: red;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}")
                self.setLeds(2, QColor(255,0,0))
                print("Modo CLEAR activado")
            else:
                CLEAR_SELECTION = None
                self.ui.sim_clear.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}")
                self.setLeds(2, QColor(0,0,0))
                print("Modo CLEAR desactivado")


        def reset_clear_mode(self):
            """Apaga el modo CLEAR y resetea estilos del botón CLEAR únicamente"""
            global CLEAR_MODE, CLEAR_SELECTION
            CLEAR_MODE = False
            CLEAR_SELECTION = None
            self.ui.sim_clear.setStyleSheet("QPushButton { font-family: Arial; font-size: 8px; font-weight: bold; color: white; padding: 10px;border-radius: 15px;border: 2px solid rgba(255,255,255,255); background-color: transparent;} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed { background-color: rgba(0,150,250,50);}") 
            self.setLeds(2, QColor(0,0,0))
            print("Modo CLEAR desactivado automáticamente después de la selección")


        def function_page_activate():
            """Activa el modo de selección de página."""
            global modo_page
            modo_page = True
            save_page_mode(modo_page)
            self.show_dialog_modopage()
            print("Modo de selección de página activado.")
        

        def function_out(self):
            global clip_id, mark_in_tc

            set_page_mode(False)
            set_shift(False)

            pgm = UIFunctions.get_channelmode()

            if pgm == "B":
                self.ui.sim_out.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: green; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                self.setLeds(27, QColor(0, 255,0))
            else: 
                self.ui.sim_out.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; background-color: red; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                self.setLeds(27, QColor(255, 0,0))
            
            
            # 1. Marcar el Out en vMix
            endpoint = "api/?Function=ReplayMarkOut"
            if not UIFunctions.send_request(endpoint):
                print("Error: No se pudo marcar el 'Out'")
                return
            
            clip_out_tc = UIFunctions.get_tc()
            mark_in_tc = load_mark_in_tc()
            print("Replay mark 'Out' set successfully.")

            # Estado inicial
            operation_mode = "normal"  # Puede ser: "normal", "page", "bank"
            
            while True:
                # Obtener el estado ACTUAL de los botones especiales
                current_shift = load_shift()
                current_page_mode = load_page_mode()
                
                # Determinar el modo de operación actual
                if current_page_mode:
                    operation_mode = "page"
                elif current_shift:
                    operation_mode = "bank"
                else:
                    operation_mode = "normal"

                print(f"Modo actual: {operation_mode}")  # Debug
                
                # Esperar pulsación de botón
                button_num = wait_for_button_press()
                
                if button_num is None:
                    continue  # Timeout, reintentar
                    
                # Manejar según el modo actual
                if operation_mode == "page":
                    print(f"Cambiando a página {button_num}")
                    function_page(button_num)
                    set_page_mode(False)  # Desactivar modo página
                    continue
                    
                elif operation_mode == "bank":
                    print(f"Cambiando banco a {button_num}")
                    change_bank(button_num)
                    set_shift(False)  # Desactivar shift
                    continue
                    
                elif operation_mode == "normal":
                    # Guardar clip - TU LÓGICA ORIGINAL
                    page = load_config().get("CURRENT_PAGE", 1)
                    bank = load_config().get("last_bank_per_page", {}).get(str(page), 1)
                    clip_pos = f"{page}{bank}{button_num}"
                    
                    clips = load_clip_dictionary()
                    if clips.get(clip_pos, ["void"] * 7)[0] == "void":
                        clip_id = load_current_clip_id()
                        duration = UIFunctions.calculate_clip_duration(mark_in_tc, clip_out_tc)
                        
                        clips[clip_pos] = [
                            str(clip_id), "void", "void", "void",
                            str(mark_in_tc), str(clip_out_tc), str(duration)
                        ]
                        save_clip_dictionary(clips)
                        
                        clip_id += 1
                        save_current_clip_id(clip_id)
                        print(f"Clip guardado en {clip_pos} (ID: {clip_id-1})")
                    else:
                        show_dialog_overwrite_clip(self, clip_pos, clips)
                    
                    break  # Salir del bucle después de guardar

            # Limpieza final
            set_page_mode(False)
            set_shift(False)

        def set_page_mode(active):
            """Activa o desactiva el modo de cambio de página"""
            global modo_page
            modo_page = active
            save_page_mode(active)

        def set_shift(active):
            """Activa o desactiva el modo de cambio de banco (SHIFT)"""
            global SHIFT
            SHIFT = active
            save_shift(active)

        def wait_for_button_press():
            """Espera la pulsación de un botón F de manera segura"""
            button_pressed = None
            loop = QEventLoop()
            timer = QTimer()
            timer.setSingleShot(True)
            
            # Mapeo de botones
            buttons = {
                1: self.ui.sim_f1,
                2: self.ui.sim_f2,
                3: self.ui.sim_f3,
                4: self.ui.sim_f4,
                5: self.ui.sim_f5,
                6: self.ui.sim_f6,
                7: self.ui.sim_f7,
                8: self.ui.sim_f8,
                9: self.ui.sim_f9,
                0: self.ui.sim_f10
            }
            
            # Handler que captura el parámetro checked
            def create_handler(num):
                def handler(checked):
                    nonlocal button_pressed
                    self.ui.sim_in.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                    self.setLeds(26, QColor(0, 0,0))
                    self.ui.sim_out.setStyleSheet("QPushButton {font-family: Arial; font-size: 16px; font-weight: bold; color: white;	padding: 10px; border-radius: 15px; border: 2px solid rgba(255,255,255,255);} QPushButton:hover {background-color: rgba(0,150,250,50);} QPushButton:pressed {background-color: rgba(0,150,250,50);}")
                    self.setLeds(27, QColor(0, 0,0))
                    button_pressed = num
                    loop.quit()
                return handler
            
            # Conectar todos los botones
            connections = []
            for num, btn in buttons.items():
                handler = create_handler(num)
                btn.clicked.connect(handler)
                connections.append((btn, handler))
            
            # Configurar timeout
            timer.timeout.connect(loop.quit)
            timer.start(200)  # 0.2 segundos
            
            # Ejecutar el loop de eventos
            loop.exec_()
            
            # Limpieza garantizada
            timer.stop()
            for btn, handler in connections:
                try:
                    btn.clicked.disconnect(handler)
                except RuntimeError:
                    pass  # Ignorar si ya está desconectado
            
            return button_pressed


        def handle_sim_f_button(self, f_button_number):
            """Maneja la funcionalidad de los botones sim_f1 a sim_f10."""
            global current_page, current_bank, SHIFT, clip_mode, modo_page

            # Si SHIFT está activado, cambiar el banco
            if SHIFT:
                change_bank(f_button_number)  # Cambiar banco de la página actual
                print("function change bank")
                reset_shift(self)

            elif modo_page:
                self.popup_modo_page.close_popup()
                function_page(f_button_number)  # o directamente function_page si es global
                print("function change page")
                modo_page = False

            # Activar el modo clip y mostrar el código correspondiente
            else:
                clip_mode = True  # Activar modo clip
                save_clip_mode(clip_mode)
                current_camangle = load_current_camangle()
                clip_code = f"{current_page}{current_bank}{f_button_number}{current_camangle}"
                numeric_code = clip_code[:-1]  
                print(f"Código del clip: {clip_code}")  # Mostrar el código del clip
                save_current_clip(clip_code)
                # Cargar el archivo JSON
                if numeric_code == "101":
                    UIFunctions.goto_pl(self, 1)
                if numeric_code == "102":
                    UIFunctions.goto_pl(self, 2)
                if numeric_code == "201":
                    UIFunctions.goto_pl(self, 3)
                if numeric_code == "202":
                    UIFunctions.goto_pl(self, 4)
                if numeric_code == "301":
                    UIFunctions.goto_pl(self, 5)
                if numeric_code == "302":
                    UIFunctions.goto_pl(self, 6)
                if numeric_code == "401":
                    UIFunctions.goto_pl(self, 7)
                if numeric_code == "402":
                    UIFunctions.goto_pl(self, 8)
                if numeric_code == "501":
                    UIFunctions.goto_pl(self, 8)
                if numeric_code == "502":
                    UIFunctions.goto_pl(self, 9)
                if numeric_code == "602":
                    UIFunctions.goto_pl(self, 10)
                if numeric_code == "701":
                    UIFunctions.goto_pl(self, 11)
                if numeric_code == "702":
                    UIFunctions.goto_pl(self, 12)
                if numeric_code == "801":
                    UIFunctions.goto_pl(self, 13)
                if numeric_code == "802":
                    UIFunctions.goto_pl(self, 14)
                if numeric_code == "901":
                    UIFunctions.goto_pl(self, 15)
                if numeric_code == "902":
                    UIFunctions.goto_pl(self, 16)
                if numeric_code == "001":
                    UIFunctions.goto_pl(self, 17)
                if numeric_code == "002":
                    UIFunctions.goto_pl(self, 18)
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
                    pgm = UIFunctions.get_channelmode()
                    if pgm == "B":
                        current_camangleB = load_current_camangleB()
                        clip_prv = f"{numeric_code}{current_camangleB}"
                        save_current_clip_prv(clip_prv)
                    else:
                        current_camangleA = load_current_camangleA()
                        clip_pgm = f"{numeric_code}{current_camangleA}"
                        save_current_clip_pgm(clip_pgm)      
                    UIFunctions.labelPGM_PRV(self, pgm)
                    id = clip_list[0].zfill(4)
                    endpoint_0 = "api/?Function=ReplaySelectEvents1&Channel=1"
                    endpoint_1 = f"api/?Function=ReplayPlayEventsByID&Value={id}&Channel=1"
                    endpoint_2 = "api/?Function=ReplayPause&Channel=1"
                    UIFunctions.send_request(endpoint_0)
                    UIFunctions.send_request(endpoint_1)
                    UIFunctions.send_request(endpoint_2)
               
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
            global current_bank
            SHIFT = load_shift()
            if SHIFT:
                save_current_bank(button_number)
                current_bank = button_number  # Actualizamos la variable global
                self.ui.label_bank.setText(f"{current_bank} BANK")  # Actualiza QLabel
                print(f"Banco actualizado a {button_number} para la página {current_page}.")
                if current_bank == 0:
                    self.ui.label_bank.setText("PL. BANK")  # Actualiza QLabel

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
  
        ########################################################################
        ## END - CLIP MANAGEMENT
        ########################################################################
        def start_serial_listener(self):
            print('Serial listener started')
            if self.ser is None:
                print("Serial no disponible.")
                return

            def listen():
                print("Listening on serial port...")
                while True:
                    try:
                        line = self.ser.readline().decode().strip()
                        if not line:
                            continue
                        #print(f"Received: {line}")

                        if line.startswith("BTN:"):
                            try:
                                btn_id = int(line.split(":")[1])
                                handle_button_press(self, btn_id)
                            except ValueError:
                                print(f"Línea malformada: {line}")

                        elif line.startswith("FADER:"):
                            try:
                                fader_val = int(line.split(":")[1])
                                handle_fader_change(self, fader_val)
                            except ValueError:
                                print(f"Línea malformada fader: {line}")

                        elif line.startswith("ENCODER:"):
                            try:
                                encoder_val = int(line.split(":")[1])
                                handle_encoder_change(self, encoder_val)
                            except ValueError:
                                print(f"Línea malformada encoder: {line}")

                        elif line == "ENC_BTN":
                            handle_encoder_button(self)

                        else:
                            print(f"Línea desconocida: {line}")

                    except Exception as e:
                        print(f"Error leyendo del puerto serial: {e}")
                        break

            self.listener_thread = threading.Thread(target=listen, daemon=True)
            self.listener_thread.start()
        start_serial_listener(self)

        def handle_button_press(self, btn_id):
            print(f"Botón presionado: {btn_id}")
            if btn_id == 0:
                function_menu(self)
            elif btn_id == 1:
                toggle_shift(self)
            elif btn_id == 2:
                toggle_clear_mode(self)
            elif btn_id == 3:
                UIFunctions.function_enter(self)
            elif btn_id == 4:
                handle_sim_f_button(self, 1)
            elif btn_id == 5:
                handle_sim_f_button(self, 2)
            elif btn_id == 6:
                handle_sim_f_button(self, 3)
            elif btn_id == 7:
                handle_sim_f_button(self, 4)
            elif btn_id == 8:
                handle_sim_f_button(self, 5)
            elif btn_id == 9:
                handle_sim_f_button(self, 6)
            elif btn_id == 10:
                handle_sim_f_button(self, 7)
            elif btn_id == 11:
                handle_sim_f_button(self, 8)
            elif btn_id == 12:
                handle_sim_f_button(self, 9)
            elif btn_id == 13:
                handle_sim_f_button(self, 0)
            elif btn_id == 14:
                execute_functions_A(self)
            elif btn_id == 15:
                execute_functions_B(self)
            elif btn_id == 16:
                execute_functions_C(self)
            elif btn_id == 17:
                execute_functions_D(self)
            elif btn_id == 18:
                print('18')
            elif btn_id == 19:
                execute_functions_play(self)
            elif btn_id == 20:
                execute_functions_gototc(self)
            elif btn_id == 21:
                execute_functions_fastjog(self, self.dial)
            elif btn_id == 22:
                execute_functions_record(self)
            elif btn_id == 23:
                execute_functions_prvctl(self)
            elif btn_id == 24:
                execute_functions_loop(self)
            elif btn_id == 25:
                execute_functions_insert(self)
            elif btn_id == 26:
                handle_sim_in(self)
            elif btn_id == 27:
                handle_sim_out(self)
            elif btn_id == 28:
                execute_functions_take(self)


        def handle_fader_change(self, value):
            print(f"Fader cambiado a: {value}")
            slider_val = value

            # Para evitar llamadas repetidas si no cambia el valor:
            if slider_val != self.slider.value():
                self.slider.blockSignals(True)
                self.slider.setValue(slider_val)
                self.slider.blockSignals(False)
                speed = value/100
                UIFunctions.send_request(f"api/?Function=ReplaySetSpeed&Value={speed}&Channel=1")

        def handle_encoder_change(self, value):
            print(f"Encoder cambiado a: {value}")
            self.ui.sim_rodeta.setValue(value)

        def handle_encoder_button(self):
            print("Botón del encoder presionado")
            UIFunctions.function_fastjog(self, self.dial)


    



        #QTableWidget Parameters
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        ################### SHOW MAIN WINDOW ################ 
        self.show()
        #####################################################

        self.popup_modo_page = PopupModoPage()
        
        def show_dialog_overwrite_clip(self, clip_code, clip_management):
            self.popup = PopupOverwriteClip(clip_code, clip_management)
            self.popup.exec_()

    ########################################################################
    ## START - SHOW POPUPS
    ########################################################################
    def show_dialog_modopage(self):
        #self.popup_modo = PopupModoPage()  # Guardar en un atributo para evitar que se elimine
        #self.popup.setModal(False)  # Asegurás que no sea modal
        self.popup_modo_page.show()  # Muestra el diálogo de forma modal
    

    
    def show_dialog_delete_marks(self):
        self.popup = PopupDeleteMarks()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_searchtc(self):
        self.popup = PopupSearchTC()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_nameclip(self):
        self.popup = PopupNameClip()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal
    

    def show_dialog_fastjog(self):
        self.popup = PopupFastJog()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_myvmix(self):
        self.popup = PopupMyVmix()  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal

    def show_dialog_deleteclipdic(self):
        self.popup = PopupDeleteClipDictionary(self)  # Guardar en un atributo para evitar que se elimine
        self.popup.exec_()  # Muestra el diálogo de forma modal


    ########################################################################
    ## END - SHOW POPUPS
    ########################################################################

    ########################################################################
    ## START - MENU ASSIGNMENT
    ########################################################################

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
            UIFunctions.refresh_all_playlists(self, 18)
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


    ########################################################################
    ## END - MENU ASSIGNMENT
    ########################################################################

    #############################################################
    ## START - LED CONTROLLER FUNCTIONS
    #############################################################

    
    def setLeds(self, numLed, color):
        self.led_colors[numLed] = color
        self.send_colors()

    def send_colors(self):
        if self.ser and self.ser.is_open:
            data = bytearray()
            for color in self.led_colors:
                data += bytes([color.red(), color.green(), color.blue()])
            self.ser.write(data)

    def closeEvent(self, event):
        if self.ser and self.ser.is_open:
            self.ser.close()
        event.accept()
    

    ##############################################################
    ## END - LED CONTROLLER FUNCTIONS
    ###############################################################


    ########################################################################
    ## START - APP EVENTS
    ########################################################################

    #Mouse Double Click
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    

    #Mouse Click
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    #Key Pressed
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    #Resize Event
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

    ########################################################################
    ## END - APP EVENTS
    ########################################################################
    
from multiview import run_flask
def start_flask_thread():
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()


########################################################################
## END - MAINWINDOW
########################################################################

if __name__ == "__main__":
    start_flask_thread()
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
