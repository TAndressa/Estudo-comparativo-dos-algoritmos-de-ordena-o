#import random
import time

def insertion_sort(v):
    global count
    global troca
    i = 1
    while i < len (v): 
        temp = v[i]
        trocou = False
        j = i -1
        while j >= 0 and v[j] > temp:
            v[j+1] = v[j]
            trocou = True
            troca +=1
            #print ("troca: " + str(v))
            j -= 1
        if trocou:
            v[j+1] = temp
            count+=1
            print ("Comparações: " + str(v))  
        i +=1       
troca = 0 
count = 0
vetor = list (range(0,10000))
#random.shuffle (vetor)
vetor.sort(reverse = True)
#print(vetor) #imprimir o vetor 
antes = time.time()
insertion_sort(vetor)
depois = time.time()

total = (depois - antes) * 1000 #conversão para ms

print(vetor)
print("A ordenação demorou %0.2f ms" % total)
print ("Trocas: " + str(troca))
print ("Comparações: " + str(count))