import random

def randomGeneric():
    return [random.randint(-999999, 999999) for _ in range(20000)]
 

if __name__ == '__main__':
    
 print(randomGeneric()[:20000])
