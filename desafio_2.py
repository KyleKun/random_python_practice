prime = []

for i in range(2, 121):
    qtd = 0
    for j in range(1, i+1):
        if i % j == 0:
            qtd+=1

    if qtd == 2:
        prime.append(i)

print(prime)
