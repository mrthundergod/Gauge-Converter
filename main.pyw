from converterGUI import *


AWG = ['8.25', '7.35', '6.54', '5.83', '5.19', '4.62', '4.11', '3.67', '3.26', '2.91', '2.59', '2.3', '2.05', '1.83', '1.63', '1.45', '1.29', '1.15', '1.02', '0.912', '0.813', '0.724', '0.643', '0.574', '0.511', '0.455', '0.404', '0.61', '0.320', '0.287', '0.254', '0.226', '0.203', '0.180', '0.160', '0.142', '0.127', '0.114', '0.102', '0.089', '0.079', '0.071', '0.064', '0.056', '0.051', '0.046']
SWG = ['8.23', '7.62', '7.01', '6.40', '5.89', '5.38', '4.88', '4.47', '4.06', '3.66', '3.25', '2.95', '2.64', '2.34', '2.03', '1.83', '1.63', '1.42', '1.22', '1.02', '0.914', '0.813', '0.711', '0.610', '0.559', '0.508', '0.457', '0.417', '0.376', '0.345', '0.315', '0.295', '0.274', '0.254', '0.234', '0.213', '0.193', '0.173', '0.152', '0.132', '0.122', '0.112', '0.102', '0.091', '0.081', '0.071']
AWGDict = {'Gauge': 'AWG', '0': '8.25', '1': '7.35', '2': '6.54', '3': '5.83', '4': '5.19', '5': '4.62', '6': '4.11', '7': '3.67', '8': '3.26', '9': '2.91', '10': '2.59', '11': '2.3', '12': '2.05', '13': '1.83', '14': '1.63', '15': '1.45', '16': '1.29', '17': '1.15', '18': '1.02', '19': '0.912', '20': '0.813', '21': '0.724', '22': '0.643', '23': '0.574', '24': '0.511', '25': '0.455', '26': '0.404', '27': '0.61', '28': '0.320', '29': '0.287', '30': '0.254', '31': '0.226', '32': '0.203', '33': '0.180', '34': '0.160', '35': '0.142', '36': '0.127', '37': '0.114', '38': '0.102', '39': '0.089', '40': '0.079', '41': '0.071', '42': '0.064', '43': '0.056', '44': '0.051', '45': '0.046'}
SWGDict = {'Gauge': 'SWG', '0': '8.23', '1': '7.62', '2': '7.01', '3': '6.40', '4': '5.89', '5': '5.38', '6': '4.88', '7': '4.47', '8': '4.06', '9': '3.66', '10': '3.25', '11': '2.95', '12': '2.64', '13': '2.34', '14': '2.03', '15': '1.83', '16': '1.63', '17': '1.42', '18': '1.22', '19': '1.02', '20': '0.914', '21': '0.813', '22': '0.711', '23': '0.610', '24': '0.559', '25': '0.508', '26': '0.457', '27': '0.417', '28': '0.376', '29': '0.345', '30': '0.315', '31': '0.295', '32': '0.274', '33': '0.254', '34': '0.234', '35': '0.213', '36': '0.193', '37': '0.173', '38': '0.152', '39': '0.132', '40': '0.122', '41': '0.112', '42': '0.102', '43': '0.091', '44': '0.081', '45': '0.071'}


def signals(self):
    self.populateComboBox()
    self.pushButton.clicked.connect(self.reset_1)
    self.pushButton_2.clicked.connect(self.reset_2)
    self.pushButton_3.clicked.connect(self.reset_3)
    self.comboBox.activated[str].connect(self.convert1)
    self.comboBox_2.activated[str].connect(self.convert2)
    self.comboBox_3.activated[str].connect(self.convert3)


def populateComboBox(self):
    for i in range(0,46):
        self.comboBox.addItem(str(i))

    for j in AWG:
        self.comboBox_2.addItem(j)

    for k in SWG:
        self.comboBox_3.addItem(k)

def reset_1(self):
    self.lineEdit.setText(" ")
    self.lineEdit_2.setText(" ")

def reset_2(self):
    self.lineEdit_4.setText(" ")
    self.lineEdit_3.setText(" ")

def reset_3(self):
    self.lineEdit_5.setText(" ")
    self.lineEdit_6.setText(" ")
    
def convert1(self):
    val1 = int(self.comboBox.currentText())
    awg1 = AWG[val1]
    swg1 = SWG[val1]
    self.lineEdit.setText(awg1)
    self.lineEdit_2.setText(swg1)

def convert2(self):
    val2 = self.comboBox_2.currentText()
    gauge = AWG.index(val2)
    swg2 = SWG[int(gauge)]
    self.lineEdit_4.setText(str(gauge))
    self.lineEdit_3.setText(str(swg2))        

def convert3(self):
    val3 = self.comboBox_3.currentText()
    gauge2 = SWG.index(val3)
    awg2 = AWG[int(gauge2)]
    self.lineEdit_6.setText(str(gauge2))
    self.lineEdit_5.setText(str(awg2))

        
Ui_GaugeToolBox.signals = signals
Ui_GaugeToolBox.populateComboBox = populateComboBox
Ui_GaugeToolBox.reset_1 = reset_1
Ui_GaugeToolBox.reset_2 = reset_2
Ui_GaugeToolBox.reset_3 = reset_3
Ui_GaugeToolBox.convert1 = convert1
Ui_GaugeToolBox.convert2 = convert2
Ui_GaugeToolBox.convert3 = convert3


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GaugeToolBox = QtGui.QDialog()
    ui = Ui_GaugeToolBox()
    ui.setupUi(GaugeToolBox)
    ui.signals()
    GaugeToolBox.show()
    sys.exit(app.exec_())
