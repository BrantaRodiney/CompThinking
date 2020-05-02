import datetime

def obter_limite():
    cargo_atual = str(input("Para fazermos sua analise de credito, "
                            "precisamos que voce entre com algumas informacoes:\nCargo atual: "))
    salario_atual = float(input("Salario Atual: "))
    ano_de_nascimento = int(input("Ano de nascimento: "))
    ano_vigente = datetime.date.today()
    idade_aproximada = (ano_vigente.year - ano_de_nascimento)
    valor_credito_disponivel = ((salario_atual*(idade_aproximada / 1000)) +100) 
    print(f"Seu cargo atual: {cargo_atual} \nSeu Salario atual: {salario_atual} \nSeu ano de nascimento: {ano_de_nascimento}")
    print(f"Voce tem aproximadamente {idade_aproximada} anos.")
    print(f"Voce possui o valor em credito de R$ {valor_credito_disponivel:.2f}, disponiveis para compras em nossa loja.")

print(obter_limite())
