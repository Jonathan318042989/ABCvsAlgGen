import random
import matplotlib.pyplot as plt

capacidad_mochila = 50  
pesos = [10, 20, 30, 15, 5, 45, 10, 70, 40]
valores = [100, 250, 150, 80, 60, 50, 90, 70, 30]
num_elementos = len(pesos)

num_abejas = 10
num_iteraciones = 100  

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
    mejores_valores = []
    for _ in range(num_iteraciones):
        abejas = [generar_solucion() for _ in range(num_abejas)]
        for abeja in abejas:
            valor_abeja = evaluar(abeja)
            if valor_abeja > mejor_valor:
                mejor_solucion = abeja
                mejor_valor = valor_abeja
        mejores_valores.append(mejor_valor)
    return mejor_solucion, mejor_valor, mejores_valores

mejor_solucion, mejor_valor, mejores_valores = abc_mochila()

print("Mejor solución encontrada:", mejor_solucion)
print("Mejor valor encontrado:", mejor_valor)

plt.plot(mejores_valores)
plt.xlabel('Iteraciones')
plt.ylabel('Mejor valor encontrado')
plt.title('Rendimiento del algoritmo ABC para el problema de la mochila')
plt.grid(True)
plt.show()
