termo = int(input("Digite o termo que deseja encontrar: "))
termo = termo - 2
n1 = 1
n2 = 1
n3 = int()
resultados = []

print(n1)
print(n2)
for i in range(termo):
   n3 = n1 + n2
   resultados.append(n3)
   print(n3) 
   n1 = n2
   n2 = n3
