hora = float(input("Digite quanto você ganha por hora:"))

trabalhadas = float(input("número de horas trabalhadas no mês:"))

resultado = hora * trabalhadas

print("Selario bruto:", resultado)

resultado2 = resultado * 11
resultado3 = resultado2 / 100

print("Você pagou:", resultado3, "de ir")

resultado4 = resultado * 8 

resultado5 = resultado4 / 100

print("Você pagou:", resultado5, "de Inss")

resultado6 = resultado * 5
resultado7 = resultado6 / 100

print("Você pagou:", resultado7, "de Sindicato")

salarioL = resultado - resultado3 - resultado5 - resultado7
print("Salario Liquido é:", salarioL)