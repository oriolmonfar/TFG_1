# Interfície per a controlar Instant Replays de vMix amb operativa d'EVS:

Aquest projecte permet operar de forma remota la funció de repeticions instantànies (*Instant Replays*) de **vMix** amb l'operativa d'**EVS**. Aquest codi forma part d'un projecte amb un remot físic, però el codi sol ja és funcional, replicant el remot des de la pàgina de simulador.
El projecte és el treball de final de grau, que consta en el següent: 


**Controlador remot per a repeticions instantànies a vMix: replicant l’experiència d’EVS en un entorn més accessible:**


Aquest projecte presenta el disseny i la implementació d’un sistema de control remot per a repeticions instantànies amb vMix, com a alternativa més accessible i econòmica als sistemes d'EVS, habituals en produccions esportives professionals. Per desenvolupar-lo, s’ha realitzat un estudi de les solucions existents actualment per a la gestió de repeticions instantànies. A partir d’aquesta anàlisi, s’ha dissenyat una interfície gràfica amb QtDesigner i PySide2, reproduint els menús i interaccions del remot original. Les funcionalitats s’han implementat en Python, utilitzant crides HTTP a l’API de vMix i codi personalitzat. Pel que fa al maquinari, s'usa una Orange Pi 5+ i una placa ESP32 dins una carcassa impresa en 3D amb controls físics i pantalla tàctil. El sistema ha estat testejat per operadors professionals per avaluar-ne el funcionament i detectar possibles millores.

# REQUERIMENTS:
Es requereixen les llibreries: PySide2, Time, Datetime, Requests, Threading i Serial.

# EXECUCIÓ:
Per a executar el programa, s'executa el fitxer main_2.py. 


