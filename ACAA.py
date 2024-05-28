import random
import numpy as np
from Knapsack import *

class Fuente:
    def __init__(self, solucion):
        self.solucion = solucion
        self.contador = 0
        
class ACAA:
    
    def __init__(self, pesos, valores, numero_fuentes=50, numero_abejas = 30, iteraciones=1000, prob_mutacion=0.1):
        self.knapsack = Knapsack(pesos, valores)
        self.capacidad_mochila = 1000
        self.pesos = self.knapsack.pesos
        self.valores = self.knapsack.valores
        self.num_elementos = len(self.pesos)
        self.numero_fuentes = numero_fuentes
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion
        self.numero_abejas = numero_abejas
        self.limite_contador = int(0.6*numero_fuentes)
        
        
    def abc(self):
        fuentes = [Fuente(self.knapsack.generar_solucion_numpy()) for _ in range(self.numero_fuentes)]
        mejor_fuente = self.knapsack.selecciona_mejor_fuente(fuentes)
        for j in range(self.iteraciones):
            for i in range(self.numero_fuentes):
                fuentes = self.abeja_empleada(i, fuentes)
            fuentes = self.abeja_observadora(fuentes)
            fuentes = self.abeja_exploradora(fuentes)
            mejor_fuente = self.knapsack.selecciona_mejor_fuente(fuentes)
        return mejor_fuente
                
    def abeja_empleada(self, indice_fuente, fuentes, indice_torneo = None):
        xi = np.array(fuentes[indice_fuente].solucion)
        diferente_fuente = indice_fuente
        if indice_torneo == None:
            while (diferente_fuente == indice_fuente): diferente_fuente = random.randint(0, len(fuentes)-1)
        else:
            diferente_fuente = indice_torneo
        int_rand = random.randint(-1,1)
        xk = np.array(fuentes[diferente_fuente].solucion)
        ui = xi + int_rand*(xi - xk)
        ui = self.verifica(ui)
        if self.knapsack.funcion_evaluacion(xi) < self.knapsack.funcion_evaluacion(ui):
            fuentes[indice_fuente].solucion = ui
        else:
            fuentes[indice_fuente].contador+=1
        return fuentes
    
    def verifica(self, nueva_fuente):
        for i in range(len(nueva_fuente)):
            if nueva_fuente[i] >= 1:
                nueva_fuente[i] = 1
            elif nueva_fuente[i] <= 0:
                nueva_fuente[i] = 0
        return nueva_fuente
    
    def abeja_observadora(self, fuentes):
        for i in range(self.numero_fuentes):
            seleccion = self.knapsack.seleccion_fuente_torneo(fuentes)
            fuentes = self.abeja_empleada(i, fuentes, seleccion)
        return fuentes
    
    def abeja_exploradora(self, fuentes):
        for i in range(len(fuentes)):
            if fuentes[i].contador > self.limite_contador:
                fuentes[i] = Fuente(self.knapsack.generar_solucion())
        return fuentes
    
if __name__ == "__main__":
    capacidad_mochila = 50
    pesos = [10, 20, 30, 15, 5, 45, 10, 70, 40]
    valores = [100, 250, 150, 80, 60, 50, 90, 70, 30]
    num_elementos = len(pesos)
    abc = ACAA(pesos, valores)
    mejor_solucion = abc.abc()
    print(mejor_solucion.solucion)
    print("Mejor solución encontrada:")
    for i in range(num_elementos):
        if mejor_solucion.solucion[i] == 1:
            print(f"Objeto {i+1} - Peso: {pesos[i]}, Valor: {valores[i]}")
    print(abc.knapsack.funcion_evaluacion(mejor_solucion.solucion))