import pyfiglet
import string
import itertools
import time
print ("\n Simulador de:")
print (pyfiglet.figlet_format("Brute Force"))
while True:
	senha = input("\nDigite a senha:\n").strip()
	if senha == "":
		print ("A senha não pode ficar em branco.")
	else:
		break
inicio = time.time()
letras = string.ascii_letters
numeros = string.digits
dicionario = (letras + numeros)
caracteres = list(dicionario)
encontrado = False
tentativas = 0
for tamanho in range (1, 13):
	for combinacao in itertools.product(caracteres, repeat = tamanho):
		tentativa = "".join(combinacao)
		tentativas += 1
#		print (tentativa)
		if tentativa == senha:
			encontrado = True
			break
	if encontrado:
		break
fim = time.time()
print("\n--- RESULTADO ---")
print(f"Senha encontrada: {tentativa}")
print(f"Tentativas feitas: {tentativas}")
print(f"Tempo total: {fim - inicio:.2f} segundos")
