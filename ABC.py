import random

capacidad_mochila = 50 
pesos = [40, 20, 30, 15, 5]  
valores = [100, 250, 150, 80, 60] 
num_elementos = len(pesos)  

num_abejas = 10  
iteraciones = 100


def evaluar(solucion):
    peso_total = sum(solucion[i] * pesos[i] for i in range(num_elementos))
    valor_total = sum(solucion[i] * valores[i] for i in range(num_elementos))
    if peso_total > capacidad_mochila:
        return 0  
    else:
        return valor_total

def generar_solucion():
    return [random.randint(0, 1) for _ in range(num_elementos)]

def abc_mochila():
    mejor_solucion = None
    mejor_valor = 0
    for _ in range(iteraciones):
        abejas = [generar_solucion() for _ in range(num_abejas)]
        for abeja in abejas:
            valor_abeja = evaluar(abeja)
            if valor_abeja > mejor_valor:
                mejor_solucion = abeja
                mejor_valor = valor_abeja
    return mejor_solucion, mejor_valor

mejor_solucion, mejor_valor = abc_mochila()

print("Mejor solución encontrada:", mejor_solucion)
print("Mejor valor encontrado:", mejor_valor)
