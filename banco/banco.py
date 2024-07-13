#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser 
#iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque 
# e deposito do saldo da conta


#intale o PyQt5 para rodar o codigo e se quiser verificar o arquivo da interface.ui baixe o QTdesigner
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Conta:
    id_ultimo = 0 
    def __init__(self, nome, cpf): #iniciando a classe criando os atributos id, nome, cpf e saldo
        Conta.id_ultimo +=1 # incremento do id para a proxima conta ter um id diferente 
        self.id = Conta.id_ultimo
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0
        
    def sacar(self, valor_saque): #funcao para sacar o valor nao deixando ser maior que o valor em conta ou tentar sacar um valor negativo
        if self.saldo >= valor_saque and valor_saque > 0:
            self.saldo -= valor_saque
            print(f'valor sacado, saldo de {self.saldo}')
            return True
        else:
            print(f'voce nao tem dinheiro suficente pra sacar, saldo de {self.saldo}')
            return False

    def depositar(self, valor_deposito): # funcao para depositar o valor nao deixando depositar valor negativo ou 0
        if valor_deposito > 0:
            self.saldo += valor_deposito
            print(f'valor depositado, saldo de {self.saldo}')
            return True
        else:
            print('digite um valor maior que 0')
            return False
        

class Janela(QMainWindow): # Classe da janela 
    def __init__(self):
        super().__init__()
        uic.loadUi('interface/janela.ui', self) # carregando a interface criando com QTdesiner da pasta interface
        self.contas = {} #lista das contas criadas (para salvar o objeto da classe CONTA criada )
        self.contaLogada = None #A conta atual que sera utilizada na transacao
        self.btn_criar.clicked.connect(self.criarconta) #eventos dos botoes
        self.btn_logar.clicked.connect(self.logar)
        self.btn_depositar.clicked.connect(self.depositar)
        self.btn_sacar.clicked.connect(self.sacar)


    def criarconta(self):
        nome = self.txtnomeC.text() # .text() pega os valores digitados dos campos da janela 
        cpf = self.txtcpfC.text()
        conta = Conta(nome, cpf) #cria a conta
        self.contas[int(conta.id)] = conta #salva o obj 
        QMessageBox.information(self, "CONTA CRIADA", f"ID: {conta.id} \nNOME: {conta.nome} \nCPF: {conta.cpf}")
        self.txtnomeC.setText('')
        self.txtcpfC.setText('')


    def logar(self):
        try:
            id = int(self.txtid.text())
            self.contaLogada = self.contas[id]
            self.txtid.setText('')
            QMessageBox.information(self, "LOGADO COM", f"ID: {self.contaLogada.id} \nNOME: {self.contaLogada.nome} \nCPF: {self.contaLogada.cpf}")
            self.label_id.setText(str(self.contaLogada.id))
            self.label_nome.setText(self.contaLogada.nome)
            self.label_cpf.setText(self.contaLogada.cpf)
            self.label_saldo.setText(f'{str(self.contaLogada.saldo)} R$')
        except Exception as e:
            QMessageBox.critical(self, "ERRO", f"CONTA NAO ENCONTRADA \nVerifique se digitou apenas numeros")
            print(e)


    def depositar(self):
        try:
            valor = float(self.txt_valorT.text())
            self.txt_valorT.setText('')
            if self.contaLogada.depositar(valor):
                self.label_saldo.setText(f'{str(self.contaLogada.saldo)} R$')
                QMessageBox.information(self, "DEPOSITADO", f"ID: {self.contaLogada.id} \nNOME: {self.contaLogada.nome} \nSALDO AUTAL: {self.contaLogada.saldo} R$")
            else:
                QMessageBox.critical(self, "ERRO", f"Voce esta tentando depositar 0 ou negativo")
        except Exception as e:
            self.txt_valorT.setText('')
            QMessageBox.critical(self, "ERRO", f"Verifique se digitou apenas numeros")
            print(e)

    def sacar(self):
        try:
            valor = float(self.txt_valorT.text())
            self.txt_valorT.setText('')
            if self.contaLogada.sacar(valor):
                self.label_saldo.setText(f'{str(self.contaLogada.saldo)} R$')
                QMessageBox.information(self, "SACADDO", f"ID: {self.contaLogada.id} \nNOME: {self.contaLogada.nome} \nSALDO AUTAL: {self.contaLogada.saldo} R$")
            else:
                QMessageBox.critical(self, "ERRO", f"voce nao tem dinheiro suficente pra sacar (ou esta tentando sacar 0)")
        except Exception as e:
            self.txt_valorT.setText('')
            QMessageBox.critical(self, "ERRO", f"Verifique se digitou apenas numeros")
            print(e)

if __name__ == "__main__":
    app = QApplication([])
    window = Janela()
    window.show()
    app.exec_()
