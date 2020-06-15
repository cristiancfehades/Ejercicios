# Read a string:
n = int(input())
Diccionario ={}
for i in range (n):
    a = list(input().split())
    Diccionario[a[0]] = a[1:]
m = int(input())
for t in range (m):
    b = input()
    for pais, ciudad in Diccionario.items():
        if b in ciudad:
            print(pais)
