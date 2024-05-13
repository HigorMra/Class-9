 i = 1

 while i < 10:
     print(i)
     i += 1

 print("terminou")
 print(i)

crianças = ["Higor", "Junior", "Gabriel"]
#              0         1          2

 for item in crianças:
     print(item)

 canal = "Refatorando"

 for letra in canal:
     print(letra)

 for index in range(6,20,2): ###primeiro numero = inicio ###segundo numero valor obrigatório ### tercerio numero step = pular quantidade de numeros
     print(index)

 for index in range(len(crianças)):
     print(crianças[index],index)

 for index in range(5):
     if index == 0:
         print("primeira linha")
     else: 
         print(f"outras linhas {index}")

###

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    #print(linha) ### printa cada linha da matrix de forma normal
    print("----")
    for coluna in linha:
        print(coluna)

### printa cada linha em forma de coluna