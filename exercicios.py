#Exercício 1: Verificação de Qualidade de Dados
#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
import random
print(f"Verificando qualidade de dados.")
print(f"=" * 20)
venda = {"vendas": [{"quantidade": random.randrange(-1,10), "preco": random.randrange(-1,10)}]}
print(venda.get("vendas"))
if venda["vendas"][0]["quantidade"] > 0 and venda["vendas"][0]["preco"] > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


#Exercício 2: Classificação de Dados de Sensor
#Imagine que você está trabalhando com dados de sensores IoT. 
#Os dados incluem medições de temperatura.
#Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

print(f"Iniciando programa de classificação de dados de sensor.")
print(f"=" * 20)
temperatura = random.randrange(-1, 27)
print(temperatura)
if temperatura < 18:
    print(f"Baixa")
elif temperatura >= 18 and temperatura <= 26:
    print(f"Normal")
elif temperatura > 26:
    print(f"Alta")

#Exercício 3: Filtragem de Logs por Severidade
#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
#, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
print(f"Filtragem de Logs por Severidade.")
print(f"=" * 20)
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log.get("level") == "ERROR":
    print(log.get("level"))

#Exercício 4: Validação de Dados de Entrada
#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que:
# Os dados de cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido.
#Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
dados_usuario = {"idade": random.randrange(0, 80), "email": "email@.com"}
print(dados_usuario)
if dados_usuario.get("idade") >= 18 and dados_usuario.get("idade") <= 65:
    print(f"Dados válidos")
else:
    print(f"Idade {dados_usuario.get('idade')} não válida")

#Exercício 5: Detecção de Anomalias em Dados de Transações
#Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
#Dada uma transação como a transacao = {'valor': 12000, 'hora': 20}
transacao = {'valor': 12000, 'hora': 20}
if transacao.get("valor") > 10000 or transacao.get("hora") < 9 or transacao.get("hora") > 18:
    print(f"Transação suspeita")
else:
    print(f"Transação normal")

#6. Contagem de Palavras em Textos
#Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "Hello, world!"
palavras = texto.split()
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

#7. Normalização de Dados
#Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.4
lista_numeros = [1, 2, 3, 4, 5]
for i in range(len(lista_numeros)):
    lista_numeros[i] = (lista_numeros[i] - min(lista_numeros)) / (max(lista_numeros) - min(lista_numeros))
print(lista_numeros)


#8. Filtragem de Dados Faltantes
#Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
dados = [{'nome': None, 'idade': 25}, {'nome': 'Maria', 'idade': 30}, {'nome': 'Pedro', 'idade': None}]

faltantes = {}
for dado in dados:
    if dado['nome'] == None or dado['idade'] == None:
        faltantes[dado['nome']] = dado['idade']

print(faltantes)


#9. Extração de Subconjuntos de Dados
#Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)

#10. Agregação de Dados por Categoria
#Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {'nome': 'Notebook', 'categoria': 'Informática', 'preco': 1000, 'quantidade': 5},
    {'nome': 'Mouse', 'categoria': 'Informática', 'preco': 50, 'quantidade': 10},
    {'nome': 'Teclado', 'categoria': 'Periferico', 'preco': 150, 'quantidade': 3}
]

total = {}
for venda in vendas:
    if venda['categoria'] in total:
        total[venda['categoria']] += (venda['preco'] * venda['quantidade'])
    else:
        total[venda['categoria']] = (venda['preco'] * venda['quantidade'])
print(total)


#11. Leitura de Dados até Flag
#Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
while True:
    entrada = input("Entrada: ")
    if entrada == "sair":
        break
    print(entrada)

#12. Validação de Entrada
#Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
intervalo = [1, 10]

while True:
    entrada = input("Entrada: ")
    if entrada.isdigit() and int(entrada) >= intervalo[0] and int(entrada) <= intervalo[1]:
        print(entrada)
        break
    else:
        print("Entrada inválida. Tente novamente.")
        continue


#13. Consumo de API Simulado
#Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
paginas = 5
for i in range(paginas):
    print(i)


#14. Tentativas de Conexão
#Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
limite = 5
tentativas = 0
while tentativas < limite:
    tentativas += 1
    print(f"Tentativa {tentativas}")

#15. Processamento de Dados com Condição de Parada
#Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in lista:
    if item == 5:
        break
    print(item)   