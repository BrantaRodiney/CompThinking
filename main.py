import datetime
import os
import time


NOME_COMPLETO = "Rodiney Branta"


def obter_limite(salario_atual, idade_aproximada):
    valor_credito_disponivel = ((salario_atual*(idade_aproximada / 1000)) +100) 
    return valor_credito_disponivel

print(f"Seja bem-vindo a Poppy loja , sou {NOME_COMPLETO}, entre e escolha um produto")

cargo_atual = str(input("Para fazermos sua analise de credito, "
                        "solicitamos que voce entre com algumas informacoes:\nCargo atual: "))
salario_atual = float(input("Salario Atual: "))
ano_de_nascimento = int(input("Ano de nascimento: "))
ano_vigente = datetime.date.today()
idade_aproximada = (ano_vigente.year - ano_de_nascimento)

os.system("cls" if os.name == "nt" else "clear")
    
limite = obter_limite(salario_atual, idade_aproximada)
print(f"\nSeu cargo atual: {cargo_atual} \nSeu Salario atual: {salario_atual} \nSeu ano de nascimento: {ano_de_nascimento}")
print(f"Voce tem aproximadamente {idade_aproximada} anos.")
print(f"Voce possui o valor em credito de R$ {limite:.2f}, disponiveis para compras em nossa loja.")    

time.sleep(5)
