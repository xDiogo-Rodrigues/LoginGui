from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QCheckBox, QPushButton, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QPixmap('steam2.png'))
        self.setStyleSheet('background-color: #808080; color: white; font: 15px,Arial Narrow, sans-serif; font-weight: bold;')
        self.setWindowTitle('STEAM')
        self.setFixedSize(QSize(500,320))
        
        #QLabel
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(QPixmap('steam.png'))
        self.lbl_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.lbl_usuario = QLabel('INICIAR SESSÃO COM O NOME DE USUÁRIO')

       
        self.lbl_usuario.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lbl_usuario.setStyleSheet('color: blue')
        self.lbl_senha = QLabel('SENHA')
        self.lbl_senha.setStyleSheet('color: blue')
        self.lbl_senha.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #QLineEdit
        self.line_edit_usuario = QLineEdit()
        self.line_edit_usuario.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.line_edit_usuario.setStyleSheet('background-color: #3c3c3c;')

        self.line_edit_senha = QLineEdit()
        self.line_edit_senha.setEchoMode(QLineEdit.Password)
        self.line_edit_senha.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.line_edit_senha.setStyleSheet('background-color: #3c3c3c;')
        

        #QCheckbox
        self.check = QCheckBox('Lembre-me')

        #QPushButton
        self.button = QPushButton('Iniciar sessão')
        self.button.setStyleSheet('background-color: #1E90FF;')
   

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_img)
        layout.addWidget(self.lbl_usuario)
        layout.addWidget(self.line_edit_usuario)
        layout.addWidget(self.lbl_senha)
        layout.addWidget(self.line_edit_senha)
        layout.addWidget(self.check)
        layout.addWidget(self.button)

        container = QFrame()
        container.setLayout(layout)
        self.setCentralWidget(container)
        

