import random

def randomGeneric():
    return [random.randint(-999999, 999999) for _ in range(20000)]

def vetorOrder(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    vetor = randomGeneric()
    
    print("Antes da ordenação:", vetor[:10])
    
    vetor_ordenado = vetorOrder(vetor)
    
    print("Depois da ordenação:", vetor_ordenado[:10])
