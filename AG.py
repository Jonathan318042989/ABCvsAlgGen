import random
import numpy as np
from Knapsack import *
import matplotlib.pyplot as plt

class Solucion:
    def __init__(self, solucion):
        self.solucion = solucion

class AlgoritmoGeneticoMochila:
    def __init__(self, pesos, valores, poblacion_tamano=50, iteraciones=1000, prob_mutacion=0.1):
        self.knapsack = Knapsack(pesos, valores)
        self.capacidad_mochila = 1000
        self.pesos = self.knapsack.pesos
        self.valores = self.knapsack.valores
        self.num_elementos = len(self.pesos)
        self.poblacion_tamano = poblacion_tamano
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion

    def evaluar_diversidad(self, poblacion):
        num_individuos = len(poblacion)
        distancias_hamming = []
        distancias_euclidiana = []
        for i in range(num_individuos):
            for j in range(i + 1, num_individuos):
                dist_hamming = self.distancia_hamming(poblacion[i], poblacion[j])
                dist_euclidiana = self.distancia_euclidiana(poblacion[i], poblacion[j])
                distancias_hamming.append(dist_hamming)
                distancias_euclidiana.append(dist_euclidiana)
        promedio_hamming = np.mean(distancias_hamming) if distancias_hamming else 0
        promedio_euclidiana = np.mean(distancias_euclidiana) if distancias_euclidiana else 0
        return promedio_hamming, promedio_euclidiana

    def seleccionar_padres(self, evaluaciones):
        """ Funció para seleccionar los padres para la cruza

        Args:
            evaluaciones: Evaluaciones de la poblacion

        Returns:
            list: lista con ambos padres
        """
        total_fitness = sum(1 / (evaluacion[1] + 1) for evaluacion in evaluaciones)
        padres_seleccionados = []
        while len(padres_seleccionados) < 2:
            punto = random.uniform(0, total_fitness)
            acumulado = 0
            for individuo, evaluacion in evaluaciones:
                acumulado += 1 / (evaluacion + 1)
                if acumulado > punto:
                    padres_seleccionados.append(individuo)  
                    break
        return padres_seleccionados

    def cruzar_padres(self, padre1, padre2):
        """Funcion que cruza dos padres para generar dos nuevos individuos

        Args:
            padre1 (array(int)): Primer padre
            padre2 (array(int)): Segundo padre

        Returns:
            tuple: Regresa ambos hijos generados
        """
        punto_cruza = random.randint(0, self.num_elementos - 1)
        hijo1 = padre1[:punto_cruza] + padre2[punto_cruza:]
        hijo2 = padre2[:punto_cruza] + padre1[punto_cruza:]
        return hijo1, hijo2

    def mutar(self, individuo):
        """Operador de mutacion para los individuos

        Args:
            individuo (list(int)): Representacion del individuo

        Returns:
            list(int): El individuo mutado o no dependiendo la probabilidad
        """
        for i in range(self.num_elementos):
            if random.random() < self.prob_mutacion:
                individuo[i] = 1 - individuo[i] 
        return individuo

    def encuentra_peor_evaluacion(self, poblacion):
        peor_evaluacion = float("inf")
        for i in poblacion:
            evaluacion = self.knapsack.funcion_evaluacion(i)
            if evaluacion < peor_evaluacion:
                peor_evaluacion = evaluacion
        return peor_evaluacion

    def calcula_promedio(self, poblacion):
        promedio = 0
        for i in poblacion:
            promedio += self.knapsack.funcion_evaluacion(i)
        promedio = promedio/len(poblacion)
        return promedio

    def genera_siguiente_poblacion(self, poblacion):
        hijos = []
        hijos.append(self.knapsack.selecciona_mejor(poblacion))
        while len(hijos) < len(poblacion):
            padres = self.knapsack.seleccion_padres_torneo(poblacion)
            hijo1, hijo2 = None, None
            if np.random.random() <= 0.7:
                hijo1, hijo2 = self.cruzar_padres(padres[0], padres[1])
            else:
                hijo1 = padres[0]
                hijo2 = padres[1]
            hijo1 = self.mutar(hijo1)
            hijo2 = self.mutar(hijo2)
            hijos.append(hijo1)
            hijos.append(hijo2)
        return hijos

    def distancia_hamming(self, sol1, sol2):
        """Calcula la distancia de Hamming entre dos soluciones"""
        return sum(el1 != el2 for el1, el2 in zip(sol1, sol2))

    def distancia_euclidiana(self, sol1, sol2):
        """Calcula la distancia Euclidiana entre dos soluciones"""
        return np.sqrt(sum((el1 - el2)**2 for el1, el2 in zip(sol1, sol2)))

    def algoritmo_genetico(self):
        """Funcion que ejecuta el algoritmo genetico

        Returns:
            : Mejor solucion
        """
        file = open('EjecucionAG.txt', 'w')
        poblacion = [self.knapsack.generar_solucion() for _ in range(self.poblacion_tamano)]
        mejor_solucion = None
        peor_evaluacion = 0
        promedio_evaluacion = 0
        for i in range(self.iteraciones):
            poblacion = self.genera_siguiente_poblacion(poblacion)
            mejor_solucion = self.knapsack.selecciona_mejor(poblacion)
            peor_evaluacion = self.encuentra_peor_evaluacion(poblacion)
            promedio_evaluacion = (self.calcula_promedio(poblacion) + promedio_evaluacion)/2
            mejor_evaluacion = self.knapsack.funcion_evaluacion(mejor_solucion)
            
            promedio_hamming, promedio_euclidiana = self.evaluar_diversidad(poblacion)
            file.write(f"Iteración {i}: Mejor evaluación: {mejor_evaluacion}, Peor evaluación: {peor_evaluacion}, Promedio evaluación: {promedio_evaluacion}, Diversidad Hamming: {promedio_hamming}, Diversidad Euclidiana: {promedio_euclidiana}\n")

        file.close()
        return mejor_solucion


if __name__ == "__main__":
    capacidad_mochila = 50
    pesos = [10, 20, 30, 15, 5, 45, 10, 70, 40]
    valores = [100, 250, 150, 80, 60, 50, 90, 70, 30]
    num_elementos = len(pesos)

    alg_gen = AlgoritmoGeneticoMochila(pesos, valores)
    mejor_solucion = alg_gen.algoritmo_genetico()
    print(mejor_solucion)
    print("Mejor solución encontrada:")
    for i in range(num_elementos):
        if mejor_solucion[i] == 1:
            print(f"Objeto {i+1} - Peso: {pesos[i]}, Valor: {valores[i]}")
    print(alg_gen.knapsack.funcion_evaluacion(mejor_solucion))
