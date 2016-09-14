# -*- coding: utf-8 -*-
#!/usr/bin/python
import datetime
import sys
from PyQt4 import QtGui, QtCore
from PyQt4 import Qt

class Interfaz(QtGui.QWidget):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.initUI()

    def initUI(self):
    	#Tamano y titulo
        self.setWindowTitle("Viva Mexico!")
        self.resize(400,250)
        self.label_personajes = QtGui.QLabel('Personajes Importantes de la Independencia')
        self.label_per1 = QtGui.QLabel('Miguel Hidalgo y Costilla')
        self.label_per2 = QtGui.QLabel('Ignacio Allende')
        self.label_per3 = QtGui.QLabel('Jose Maria Morelos')
        self.button_Ap = QtGui.QPushButton('Aprietame')
        self.button_Ap.setCheckable(True)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.label_personajes)
        layout.addWidget(self.label_per1)
        layout.addWidget(self.label_per2)
        layout.addWidget(self.label_per3)
        layout.addWidget(self.button_Ap)
        self.button_Ap.clicked.connect(lambda:self.cambiar_texto())
        self.show()
    def cambiar_texto(self):
    	if self.button_Ap.isChecked():
    		self.button_Ap.setText(self.calc_fecha())
    	else:
    		self.button_Ap.setText("Aprietame")
    def calc_fecha(self):
    	hoy = datetime.date.today()
    	anio1=int(hoy.year)
    	anio2=int(hoy.year)+1
    	fes = datetime.date(anio1, 9, 15)
    	if (hoy > fes):
    		d = datetime.date(anio2, 9, 15) - hoy
    		return "Falta(n) " + str(d.days) + " dia(s) para el siguiente 15 de Septiembre"
    	else:
    		d = datetime.date(anio1, 9, 15) - hoy
    		return "Falta(n) " + str(d.days) + " dia(s) para el siguiente 15 de Septiembre"


def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('mex.png'))
    mainWindow = Interfaz()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()