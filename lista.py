entrada = open('entrada.txt', 'r')
lista = entrada.read()

lista=(lista).split('\n')
while("" in lista) : 
    lista.remove("")
