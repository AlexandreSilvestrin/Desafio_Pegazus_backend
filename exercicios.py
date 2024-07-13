#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print(' \n\n ####ex 1#### \n\n')
#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

respostas = []

for loja in response:
    for produto in loja['produtos']:
        if produto['preço'] > 30:
            respostas.append(produto)


for i in respostas:
    print(i)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 2#### \n\n')
#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

for produto in responsejson['produtos']:
    if produto['nome'] == 'Produto B':
        print(f'Preço do produto {produto['nome']} vale {produto["preço"]}')
        break

    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 3#### \n\n')
#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

#e possivel fazer de algumas forma
print('sorted(lista)')
lista_ordenada = sorted(lista)  # ordena a lista salvando em outra variavel 
print(f'{lista_ordenada}')
print(f'{lista}')

print('\n.sort()')
lista.sort() #ordena alterando a lista de uma vez 
print(lista)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 4#### \n\n')
#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]


# e possivel fazer com for dessa forma// usa o .strip() para tirar espacos da string
novalista = []
for nome in lista:
    novalista.append(nome.strip())

# e possivel simplificar usando list comprehension
novalista2 = [nome.strip() for nome in lista]

print(novalista)
print(novalista2)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 5#### \n\n')
#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

lista.pop(1) 
print(lista)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 6#### \n\n')
#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

novalista = []
for nome in lista: #bloco normal de for 
    if nome == 'joao':
        novalista.append('maria')
    else:
        novalista.append(nome)

print(novalista)

# usando list comprehension  com condicao 
novalista2 = ['maria' if nome == "joao" else nome for nome in lista]
print(novalista2)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 7#### \n\n')
#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

cont = 0
while cont < len(lista):
    if lista[cont] <= 5:
        print(lista[cont])
    cont+=1


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 8#### \n\n')
#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro 
# do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade 
# de tasks completadas, e a quantidade de tasks pendentes explique detalhadamente por que escolheu essa solução e não outra

import requests 

response = requests.get('https://jsonplaceholder.typicode.com/todos')

completas = []
pendentes = []
if response.status_code == 200:
    print(f'codigo -- {response.status_code}')
    dados = response.json()
    for dado in dados:
        if dado['completed']:
            completas.append(dado)
        else:
            pendentes.append(dado)
    print(f'''tem {len(dados)} task no total ,{len(pendentes)} pendentes e {len(completas)} completas''')
else:
    print(f'codigo -- {response.status_code}')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 9#### \n\n')
#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')


if response.status_code == 200:
    print(f'codigo -- {response.status_code}')
    dados = response.json()
    for usuario in dados:
        nome = usuario['name']
        username = usuario['username']
        email = usuario['email']
        rua = usuario['address']['street']
        numero = usuario['address']['suite']
        
        print(f"Nome: {nome}, Username: {username}, Email: {email}, Rua: {rua}, Número: {numero}")
else:
    print(f'codigo -- {response.status_code}')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 10#### \n\n')
#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

lista = []

lista.append('um')

lista.append('dois')

lista.append('tres')

print(lista)
lista.pop(0)
print(lista)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####ex 11#### \n\n')
#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

lista = []

lista.append('um')

lista.append('dois')

lista.append('tres')

print(lista)
lista.pop()
print(lista)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(' \n\n ####DESAFIO#### \n\n')
#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde
#  o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a 
# realização das operações de saque e deposito do saldo da conta

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

conta1 = Conta('Alexandre', '212312312313')

print(conta1.id)
print(conta1.nome)
print(conta1.cpf)
print(conta1.saldo)

conta1.depositar(200)
print(conta1.saldo)

conta1.sacar(100)
print(conta1.saldo)


# no arquivo banco.py fiz uma interface simples desse banco usando QTdesigner(acho simples pra projetos rapidos) para criar a janela e o PyQt5 para usar com o python
#para rodar so precisa dessa biblioteca 
# pip install PyQt5


