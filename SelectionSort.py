#import random
import time

def selection_sort(v):
    global count
    global troca
    i = 0
    while i < len (v) - 1: 
        menor = i
        j = i + 1
        #em busca do menor elemento
        while j < len (v):
            if v[j] < v [menor]:
                menor =j
            j += 1
        count+=1
        print ("Comparações: " + str(v))               
        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
            troca+=1
            #print ("troca: " + str(v))  
        i +=1                  
troca = 0 
count = 0
vetor = list (range(0,10000)) # Cria vetor/ lista 
#random.shuffle (vetor) # Medio caso - Ordem Aleatoria
vetor.sort(reverse = True) # Pior caso - Ordem Decrescente
print(vetor) #imprimir o vetor antes da ordenação.
antes = time.time()
selection_sort(vetor)
depois = time.time()

total = (depois - antes) * 1000 #conversão para ms

print(vetor) #imprimir o vetor depois da ordenação.
print("A ordenação demorou %0.2f ms" % total)
print ("Trocas: " + str(troca))
print ("Comparações: " + str(count))