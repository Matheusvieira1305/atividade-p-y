def calcular_peso_ideal(sexo, altura):
    if sexo == "masculino":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "feminino":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido. Use 'masculino' ou 'feminino'.")
        return None

    return peso_ideal

altura_pessoa = float(input("Digite sua altura em metros: "))
sexo_pessoa = input("Digite seu sexo (masculino ou feminino): ").lower()

peso_ideal = calcular_peso_ideal(sexo_pessoa, altura_pessoa)
if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
