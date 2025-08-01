def acessar_caixa():
    return

def acessar_estoque():
    while True:
        
        break

while True:
    print(f"1 - Caixa\n2 - Estoque\n3 - Sair")
    escolha = int(input(f"Escolha: "))
    if escolha == 1:
        acessar_caixa()
    elif escolha == 2:
        acessar_estoque()
    elif escolha == 3:
        break
    else:
        print(f"Erro!")
