import random
import numpy as np
from Knapsack import *

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

    def evaluar_poblacion(self, poblacion):
        """ Funcion para evaluar a toda la población actual

        Args:
            poblacion (list(array(int))): Población actual

        Returns:
            list(array,int): Lista con los individuos y evaluaciones
        """
        evaluaciones = []
        for individuo in poblacion:
            evaluacion = self.knapsack.funcion_evaluacion(individuo)
            evaluaciones.append((individuo, evaluacion))
        return evaluaciones

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
                    padres_seleccionados.append((individuo, evaluacion))
                    break
        return padres_seleccionados

    def seleccion_padres_torneo(self, poblacion_actual):
        """Función para seleccionar a 2 padres de la poblacion dada

        Args:
            poblacion_actual (array(array(int))): Poblacion actual

        Returns:
            tuple: Ambos padres seleccionados
        """
        padre1, padre2 = None, None
        for j in range(2):
            indices_individuos = np.random.choice(len(poblacion_actual), size=int(len(poblacion_actual)/10), replace=False)
            individuos = [poblacion_actual[i] for i in indices_individuos]
            mejor_evaluacion = 0
            mejor_individuo_actual = None
            for i in individuos:
                if self.knapsack.funcion_evaluacion(i) > mejor_evaluacion:
                    mejor_evaluacion = self.knapsack.funcion_evaluacion(i)
                    mejor_individuo_actual = i
            if j == 0:
                padre1 = mejor_individuo_actual
            else:
                padre2 =mejor_individuo_actual
        return padre1, padre2

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
            padres = self.seleccionar_padres(self.evaluar_poblacion(poblacion))
            hijo1, hijo2 = None, None
            if np.random.random() <= 0.7:
                hijo1, hijo2 = self.cruzar_padres(padres[0][0], padres[1][0])
            else:
                hijo1 = padres[0][0]
                hijo2 = padres[1][0]
            hijo1 = self.mutar(hijo1)
            hijo2 = self.mutar(hijo2)
            hijos.append(hijo1)
            hijos.append(hijo2)
        return hijos
        
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
            """ 
            #primera version
            evaluaciones = self.evaluar_poblacion(poblacion)
            padres = self.seleccionar_padres(evaluaciones)
            hijos = self.cruzar_padres(padres[0][0], padres[1][0])
            hijos_mutados = [self.mutar(hijo) for hijo in hijos]
            poblacion.extend(hijos_mutados)
            poblacion = sorted(poblacion, key=lambda x: self.funcion_evaluacion(x), reverse=True)[:self.poblacion_tamano] """

        #mejor_solucion = max(poblacion, key=lambda x: self.funcion_evaluacion(x))
        return mejor_solucion


if __name__ == "__main__":
    capacidad_mochila = 50
    pesos = [40, 20, 30, 15, 5]
    valores = [100, 250, 150, 80, 60]
    num_elementos = len(pesos)

    alg_gen = AlgoritmoGeneticoMochila(pesos, valores)
    mejor_solucion = alg_gen.algoritmo_genetico()

    print("Mejor solución encontrada:")
    for i in range(num_elementos):
        if mejor_solucion[i] == 1:
            print(f"Objeto {i+1} - Peso: {pesos[i]}, Valor: {valores[i]}")
    print(alg_gen.knapsack.funcion_evaluacion(mejor_solucion))
