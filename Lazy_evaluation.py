import time 
import psutil # pip install psutil 
import os 

#Cria um gerador que retorna 100 mihoes de elementos multiplicados por 2

def transform_generator():
    for x in range(10**8):
        yield x*2

start = time.time() #Inicia a contagem de tempo

gen = transform_generator() #cria o gerador
result = next(gen) #pega o primeiro elemento do gerador

end = time.time() #finaliza a contagem de tempo
process = psutil.Process(os.getpid())
memory = process.memory_info().rss / (1024 * 1024)

print("Resultado:", result) #resultado 0
print("Tempo:", round(end - start, 2)) #0.0 segundos 
print("Memoria Utilizada:", round(memory, 2), "MB") #12mb