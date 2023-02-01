nome = 'Igor'

altura = 1.84
peso = 120
#imc = peso / (altura * altura)
imc = peso / altura ** 2

print(
    f'O IMC do {nome} é {imc:.2f} pois ele tem {altura}m de altura e tem um peso atual de {peso}kg')
