n,m = input().split()
n = int(n)
m= int(m)


matrizA = []
matrizB = []

for i in range(n):
    p = [int(x) for x in input().split()]
    matrizA.append(p)
for j in range(n):
    k = [int(x) for x in input().split()]
    matrizB.append(k)

linhas = n
colunas = m

for l in range(linhas):
    for c in range(colunas):
       matrizA[l][c] -= matrizB[l][c]
print("The original list is : " + str(matrizA)) 
lst_str = str(matrizA)[1:-1] 
res = str(matrizA)[1:-1] 
print(+ res)