import random
import numpy as np
from Knapsack import *

class Fuente:
    def __init__(self, solucion):
        self.solucion = solucion
        self.contador = 0
        
class ACAA:
    
    def __init__(self, pesos, valores, numero_fuentes=50, numero_abejas = 30 iteraciones=1000, prob_mutacion=0.1):
        self.knapsack = Knapsack(pesos, valores)
        self.capacidad_mochila = 1000
        self.pesos = self.knapsack.pesos
        self.valores = self.knapsack.valores
        self.num_elementos = len(self.pesos)
        self.numero_fuentes = numero_fuentes
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion
        self.numero_abejas = numero_abejas
        
        
    def abc(self):
        fuentes = [Fuente(self.knapsack.generar_solucion()) for _ in range(self.numero_fuentes)]
        mejor_fuente = self.knapsack.selecciona_mejor_fuente(fuentes)
        for j in range(self.iteraciones):
            for i in range(self.numero_fuentes):
                fuentes = self.abeja_empleada(i, fuentes)
            
                
    def abeja_empleada(self, indice_fuente, fuentes):
        xi = fuentes[indice_fuente].solucion
        diferente_fuente = indice_fuente
        while (diferente_fuente == indice_fuente): diferente_fuente = random.randint(0, len(fuentes)-1)
        int_rand = random.randint(-1,1)
        xk = fuentes[diferente_fuente].solucion
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
        
    