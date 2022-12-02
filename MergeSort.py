#import random
import time 

def mergesort(v, p, r): 
    #condicao de parada (condicao de existencia)
    if p < r: 
        q = (p+r) // 2 #posicao do elemento do meio
        mergesort(v, q, p) #quebrando o vetor em um sub-vetor 1 (metade da esquerda)
        mergesort(v, q+1, r) # quebrando o vetor em um sub-vetor 2 ( meatde de direita)
        intercalar(v, p, q, r)

def intercalar(v, p, q, r):
    global count
    global troca
    temp = v.copy() #copia do vetor real
    i = p 
    j = q+1
    k = p
    count+=1

    #momento em que a intercalacao sera realizada
    while k <= r:
        if i > q:
            v[k] = temp[j]
            j += 1
        elif j > r:
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            v[k] = temp[j]
            i += 1
        else:
            v[k] = temp [j]
            j += 1
            troca+=1
        k += 1
        
troca = 0 
count = 0 
vetor = list(range(0,100000))
#random.shuffle (vetor) # Medio caso - Ordem Aleatoria
vetor.sort(reverse = True) # Pior caso - Ordem Decrescente
antes = time.time()
mergesort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois-antes)*1000 

#print(vetor)

print ("o tempo total foi de:%0.2f ms" % total)
print ("Trocas: " + str(troca))
print ("Comparações: " + str(count))
