import datetime
import os


def obter_limite(limpar_tela):
    NOME_COMPLETO = "Rodiney Branta"
    print(f"Seja bem-vindo a Poppy loja , sou {NOME_COMPLETO}, entre e escolha um produto\n")
    cargo_atual = str(input("Para fazermos sua análise de crédito, precisamos que você entre com algumas informações:\nCargo atual:"))
    salario_atual = float(input("Salario Atual:"))
    ano_de_nascimento = int(input("Ano de nascimento:"))
    ano_atual = datetime.datetime.today()
    idade_aproximada = (ano_atual.year - ano_de_nascimento)
    credito = ((salario_atual*(idade_aproximada/1000))+100)
    limpar_tela()
    print(f"\nSeu cargo atual: {cargo_atual} \nSeu salário atual: {salario_atual} \n"
            f"Seu ano de nascimento: {ano_de_nascimento}\n"
            f"Voce possui R$ {credito:.2f} em créditos disponíveis para compras em nossa loja.\n")
    return credito, idade_aproximada, NOME_COMPLETO


def verificar_produto(limite_de_gastos):
    input("Informe o nome de um produto que você deseja: ")
    valor_produto=float(input("Informe o valor deste produto: "))
    avaliar = 100*valor_produto/limite_de_gastos[0]
    if avaliar <= 60:
        print("LIBERADO")
    elif avaliar <= 90:
        print("Liberado a parcelar em até 2 vezes")
    elif avaliar <= 100:
        print("Liberado a parcelar em 3 ou mais vezes")
    else:
        print("Bloqueado")
    nome_completo_caracteres = int(len(limite[2]))
    desmembramento_nome = (limite[2]).split(" ", 1)[0]
    primeiro_nome_caracteres = len(desmembramento_nome)
    valor_total_com_desconto = float(valor_produto - primeiro_nome_caracteres)
    if (nome_completo_caracteres <= valor_produto <= limite[1]) or (limite[1] <= valor_produto <= nome_completo_caracteres):
        print(f"Parabéns, você foi bonificado com um desconto em seu produto, no valor de R$ {float(primeiro_nome_caracteres)}")
        print(f"O valor do produto com descosto é: R$ {valor_total_com_desconto}")


limite = obter_limite(limpar_tela())

conta_produtos_cadastros = int(input("\nInforme quantos produtos você deseja cadastrar: "))

for contador in range(conta_produtos_cadastros):
    verificar_produto(limite)

print("\nAperte a tecla ENTER para sair")
input()
