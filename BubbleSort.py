#import random
import time
def bubble_sort(v):
    global count
    global troca
    fim = len (v)
    
    while fim > 0: 
       
        i = 0
#percorrendo o vetor de 0 até fim           
        while i< fim-1:
            if v[i] > v[i+1]:
                troca +=1
                #print ("troca: " + str(v))
                temp = v[i]
                v[i] = v[i+1]              
                v[i+1] = temp
                count+=1
                #print ("Comparações: " + str(v))                 
                #print(v) 
            i +=1
        fim -= 1
troca = 0 
count = 0
vetor = list (range(0,1000)) 
#random.shuffle (vetor)
vetor.sort(reverse = True)
print(vetor) #imprimir o vetor 
antes = time.time()
bubble_sort(vetor)
depois = time.time()

total = (depois - antes) * 1000 #conversão para ms

print(vetor)
print("A ordenação demorou %0.2f ms" % total)
print ("Trocas: " + str(troca))
print ("Comparações: " + str(count))


#https://github.com/linuz/Bubble-Sort/blob/master/bubblesort.py