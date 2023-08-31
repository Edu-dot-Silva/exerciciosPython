# usuario fornece numeros em um array,depois separar em dois arrays em de par e impar em order crescente e descrecente

arrayVazio = []
arrayPar = []
arrayImpar = []
 
while True:
    numeroFornecidos = int(input('DIgite um numero inteiro(0 para sair):'))
    
    if (numeroFornecidos == 0):
        print('Finalizado')
        break
    arrayVazio.append(numeroFornecidos)
    print(f'O array fornecido foi{arrayVazio}')
    
    if(numeroFornecidos % 2 == 0):
        arrayPar.append(numeroFornecidos)
        arrayPar.sort()
        print('O array de numeros pares em order crescente é',arrayPar)

        
    if(numeroFornecidos % 2 != 0):
        arrayImpar.append(numeroFornecidos)
        arrayImpar.sort(reverse=True)
        print('O array de numeros impares em order descrecente é',arrayImpar)
        
    if(len(arrayVazio) == 10):
        print("Finalizado")
        print(f'O array original é{arrayVazio}')
        print(f'O array de numeros pares em order crescente é{arrayPar}')
        print(f'O array de numeros impares em order descrecente é{arrayImpar}')
        
        break

            
    
    