import os
import datetime #informa ano atual - ATP ETAPA2

#mostrar e somente mostrar o nome ao usuario 

print("Seja bem-vindo a loja de coelhos, entre e escolha um Rodiney Branta")

Cargo_Atual = str(input("Para fazermos sua analise de credito, precisamos que voce entre com algumas informacoes:\nCargo atual:"))
Salario_Atual = float(input("Salario Atual:"))
Ano_Nascimento = int(input("Ano de nascimento:"))
Ano_Atual = datetime.datetime.today() #ATP_ETAPA2
Idade_Aproximada = (Ano_Atual.year - Ano_Nascimento) #ATP_ETAPA2
Credito_Atual = ((Salario_Atual*(Idade_Aproximada / 1000)) +100) #ATP_ETAPA2
meuNomeCompleto = "Rodiney Branta"

os.system("cls")

print(f"Seu cargo atual: {Cargo_Atual} \nSeu Salario atual: {Salario_Atual} \nSeu ano de nascimento: {Ano_Nascimento}")
print(f"Voce tem aproximadamente {Idade_Aproximada} anos.") #ATP_ETAPA2
print(f"Voce possui o valor em credito de R$ {Credito_Atual:.2f}, disponiveis para compras em nossa loja.") #ATP_ETAPA2

#ATP_ETAPA3
NomeProduto=str(input("Informe o nome de um produto que voce deseja: "))
ValorProduto=float(input("Informe o valor deste produto: "))

# print("Produto: {} \nValor: R$ {}".format(NomeProduto, ValorProduto))

avaliar = 100 * ValorProduto / Credito_Atual

 #Avaliar quando esta liberado ou bloqueado ao parcelar
if avaliar <= 60:
     print("LIBERADO")
elif avaliar <= 90:
    print("Liberado a parcelar em até 2 vezes")
elif avaliar <= 100:
    print("Liberado a parcelar em 3 ou mais vezes")
else:
    print("Bloqueado")


def ContaCaracter(contador):
    resultado =  len(contador)
    return resultado


def CaracteresPrimeiroNome(meuNomeCompleto):
    primeiroNome = meuNomeCompleto.find(' ')
    if primeiroNome != -1:
        return(primeiroNome)
    else:
        return(len(meuNomeCompleto))


def LiberaDesconto(simNao, valorProduto, meuNomeCompleto):
    valorTotalComDesconto = float(valorProduto - CaracteresPrimeiroNome(meuNomeCompleto))
    if  (simNao <= ContaCaracter(meuNomeCompleto)) or (simNao <= Idade_Aproximada):
        print("Liberado")
        print(f"Valor produto com desconto: R$ {valorTotalComDesconto}")

print("", ContaCaracter(meuNomeCompleto))
print("", CaracteresPrimeiroNome(meuNomeCompleto))
print("", LiberaDesconto(ValorProduto, ValorProduto, meuNomeCompleto))