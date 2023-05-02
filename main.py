import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Login(QWidget):

    def __init__(self):
        super().__init__()


        self.setWindowTitle('Tela de Login')
        self.setGeometry(500,250,300,200)

        layout = QVBoxLayout()

        self.label_usuario = QLabel('Usuario:')
        self.input_usuario = QLineEdit()
        self.label_senha = QLabel('Senha:')
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton('Login')
        self.label_result_pos = QLabel('Login feito com sucesso!')
        self.label_result_neg = QLabel('Usuario ou Senha incorretos!')

        self.setLayout(layout)

        self.layout().addWidget(self.label_usuario)
        self.layout().addWidget(self.input_usuario)
        self.layout().addWidget(self.label_senha)
        self.layout().addWidget(self.input_senha)
        self.layout().addWidget(self.btn_login)


        self.btn_login.clicked.connect(self.check_login)

    def check_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        users = pd.read_csv('./data/users.csv', dtype=str, sep='|')

        if(len(users.loc[ (users['login'] == usuario) & (users['senha'] == senha) ]) == 1):
            self.label_result_pos.setVisible(True)
            self.label_result_neg.setVisible(False)
            self.layout().addWidget(self.label_result_pos)
            self.label_result_pos.setStyleSheet('color: green; font-size: 20px;')
        else:
            self.label_result_neg.setVisible(True)
            self.label_result_pos.setVisible(False)
            self.layout().addWidget(self.label_result_neg)
            self.label_result_neg.setStyleSheet('color: red; font-size: 20px;')


class createUser(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Criar Usuario')
        self.setGeometry(500,250,300,200)

        layout = QVBoxLayout()

        self.label_usuario = QLabel('Usuario:')
        self.input_usuario = QLineEdit()
        self.label_senha = QLabel('Senha:')
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.label_senha_verif = QLabel('Confirmar senha:')
        self.input_senha_verif = QLineEdit()
        self.input_senha_verif.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton('Cadastrar')
        self.label_result_pos = QLabel('Usuario Criado')
        self.label_result_neg = QLabel('Usuario ou Senha incorretos!')

        self.setLayout(layout)
        
        self.layout().addWidget(self.label_usuario)
        self.layout().addWidget(self.input_usuario)
        self.layout().addWidget(self.label_senha)
        self.layout().addWidget(self.input_senha)
        self.layout().addWidget(self.label_senha_verif)
        self.layout().addWidget(self.input_senha_verif)
        self.layout().addWidget(self.btn_login)


        self.btn_login.clicked.connect(self.check_user)

    def check_user(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()
        verif_senha = self.input_senha_verif.text()

        users = pd.read_csv('./data/users.csv', dtype=str, sep='|')

        if((len(users.loc[users['login'] == usuario]) < 1) & (senha == verif_senha)):

            users.loc[len(users)] = [usuario, senha]
            users.to_csv('./data/users.csv', sep='|', index=False)

            self.label_result_pos.setVisible(True)
            self.label_result_neg.setVisible(False)
            self.layout().addWidget(self.label_result_pos)
            self.label_result_pos.setStyleSheet('color: green; font-size: 20px;')

        else:   
            self.label_result_neg.setVisible(True)
            self.label_result_pos.setVisible(False)
            self.layout().addWidget(self.label_result_neg)
            self.label_result_neg.setStyleSheet('color: red; font-size: 20px;')


class menu(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Criar Usuario')
        self.setGeometry(500,250,300,200)

        layout = QVBoxLayout()

        self.label_acao = QLabel('Selecione uma opção:')
        self.btn_logar = QPushButton('Logar')
        self.btn_cadastrar = QPushButton('Cadastrar')

        self.setLayout(layout)

        self.layout().addWidget(self.label_acao)
        self.layout().addWidget(self.btn_logar)
        self.layout().addWidget(self.btn_cadastrar)

        
        self.btn_logar.clicked.connect(self.login)
        self.btn_cadastrar.clicked.connect(self.cadastro)

    def login(self):
        self.janela_login = Login()
        self.janela_login.show()
        self.hide()
        
    
    def cadastro(self):
        self.janela_cadastro = createUser()
        self.janela_cadastro.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    men = menu()
    men.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())