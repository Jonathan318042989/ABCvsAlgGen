import random
import numpy as np
from Knapsack import *
from FileReader import *
import sys
import math

class AG:
    def __init__(self, pesos, valores, semilla, nombre_archivo,capacidad_mochila = 1000, poblacion_tamano=10, iteraciones=100, prob_mutacion=0.1, numero_ejecucion=0):
        self.knapsack = Knapsack(pesos, valores, semilla, capacidad_mochila)
        self.semilla = semilla
        self.capacidad_mochila = capacidad_mochila
        self.pesos = self.knapsack.pesos
        self.valores = self.knapsack.valores
        self.num_elementos = len(self.pesos)
        self.poblacion_tamano = poblacion_tamano
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion
        self.numero_ejecucion = numero_ejecucion
        self.nombre_archivo = nombre_archivo

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
        mejor = self.knapsack.selecciona_mejor(poblacion)
        hijos.append(mejor)
        while len(hijos) < self.poblacion_tamano:
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
        
    def algoritmo_genetico(self):
        """Funcion que ejecuta el algoritmo genetico

        Returns:
            : Mejor solucion
        """
        archivo = "output/AG/" + self.nombre_archivo + str(self.numero_ejecucion) + ".txt"
        file = open(archivo, 'w')
        file.write("iteracion  mejor_solucion       peor_solucion                               promedio                                 distancia_euclidiana                                  distancia_hamming                                    entropia\n")
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
            distancia_euclidiana = 0
            distancia_hamming = 0
            entropia = 0
            file.write(str(i) + "         " + str(mejor_evaluacion) + "         " + str(peor_evaluacion) + "                   "+ str(promedio_evaluacion) + "                   " + str(distancia_euclidiana) + "                                 " + str(distancia_hamming) + "                                     " + str(entropia) +  "\n")
        file.write("// Semilla: " + str(self.semilla))
        file.close()
        return mejor_solucion


if __name__ == "__main__":
    """ capacidad_mochila = 50
    pesos = [10, 20, 30, 15, 5, 45, 10, 70, 40]
    valores = [100, 250, 150, 80, 60, 50, 90, 70, 30]
    num_elementos = len(pesos)

    alg_gen = AG(pesos, valores, 0, "prueba")
    mejor_solucion = alg_gen.algoritmo_genetico()
    print(mejor_solucion)
    print("Mejor solución encontrada:")
    for i in range(num_elementos):
        if mejor_solucion[i] == 1:
            print(f"Objeto {i+1} - Peso: {pesos[i]}, Valor: {valores[i]}")
    print(alg_gen.knapsack.funcion_evaluacion(mejor_solucion)) """
    
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Uso: python AG.py [No. archivo] [No. ejecucion] [semilla]")
        sys.exit(1)
    archivo = int(sys.argv[1])
    numero_ejecucion = sys.argv[2]
    #semilla = np.random.randint(1, math.pow(2, 31))
    semilla = int(sys.argv[3]) if len(sys.argv) == 4 else np.random.randint(1, math.pow(2, 31))
    np.random.seed(semilla)
    random.seed(semilla)
    pesos,valores = None, None
    nombre = ""
    capacidad = 0
    if archivo == 1:
        nombre = "f2_l-d_kp_20_878_"
        pesos,valores = FileReader.leer_archivo("Instancias/low-dimensional/f2_l-d_kp_20_878")
        capacidad = 878
    elif archivo == 2:
        nombre = "f8_l-d_kp_23_10000_"
        pesos,valores = FileReader.leer_archivo("Instancias/low-dimensional/f8_l-d_kp_23_10000")
        capacidad = 10000
    alg_gen = AG(pesos, valores, semilla=semilla, numero_ejecucion=numero_ejecucion, nombre_archivo=nombre, capacidad_mochila=capacidad)
    mejor_solucion = alg_gen.algoritmo_genetico()
    print(f'Solución: {mejor_solucion}')
    print(f'Evaluación: {alg_gen.knapsack.funcion_evaluacion(mejor_solucion)}')
    print(f'Peso: {alg_gen.knapsack.peso_total(mejor_solucion)}')