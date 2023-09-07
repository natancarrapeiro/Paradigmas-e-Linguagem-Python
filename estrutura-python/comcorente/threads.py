import threading
import time

# def funcao():
#     for i in range(5):
#         print(i,'Executando a thread!')
#         time.sleep(0.1)

# print ("Iniciando o progama")
# threading.Thread(target=funcao).start()
# print("finalixando o progama")


minha_lista = []

def adiciona():
    for i in range(100):
        minha_lista.append(1)


tarefas = []
 
for indice in range(10):
    t = Thread(target=adiciona)
    tarefas.append(t)
    t.start()

for indice in range(10):
    p = Process(target=adiciona)
    tarefas.append(t)
    p.start()
for tarefa in tarefas:
        tarefa.join()

print(len(minha_lista))
