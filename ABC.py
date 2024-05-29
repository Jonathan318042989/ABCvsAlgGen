import random
import numpy as np
from Knapsack import *
from FileReader import *
import sys
import math

class Fuente:
    def __init__(self, solucion):
        self.solucion = solucion
        self.contador = 0
        
class ABC:
    
    def __init__(self, pesos, valores, semilla, nombre_archivo, capacidad_mochila = 1000, numero_fuentes=100, iteraciones=1500, prob_mutacion=0.1, numero_ejecucion = 0):
        self.knapsack = Knapsack(pesos, valores, semilla, capacidad_mochila)
        self.semilla = semilla
        self.capacidad_mochila = capacidad_mochila
        self.pesos = self.knapsack.pesos
        self.valores = self.knapsack.valores
        self.num_elementos = len(self.pesos)
        self.numero_fuentes = numero_fuentes
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion
        self.limite_contador = int(0.1*numero_fuentes)
        self.numero_ejecucion = numero_ejecucion
        self.nombre_archivo = nombre_archivo
        
    def evaluar_diversidad(self, fuentes):
        num_individuos = len(fuentes)
        distancias_hamming = []
        distancias_euclidiana = []
        for i in range(num_individuos):
            for j in range(i + 1, num_individuos):
                dist_hamming = self.distancia_hamming(fuentes[i].solucion, fuentes[j].solucion)
                dist_euclidiana = self.distancia_euclidiana(fuentes[i].solucion, fuentes[j].solucion)
                distancias_hamming.append(dist_hamming)
                distancias_euclidiana.append(dist_euclidiana)
        promedio_hamming = np.mean(distancias_hamming) if distancias_hamming else 0
        promedio_euclidiana = np.mean(distancias_euclidiana) if distancias_euclidiana else 0
        return promedio_hamming, promedio_euclidiana, distancias_hamming

    def distancia_hamming(self, sol1, sol2):
            """Calcula la distancia de Hamming entre dos soluciones"""
            return sum(el1 != el2 for el1, el2 in zip(sol1, sol2))

    def distancia_euclidiana(self, sol1, sol2):
        """Calcula la distancia Euclidiana entre dos soluciones"""
        return np.sqrt(sum((el1 - el2)**2 for el1, el2 in zip(sol1, sol2)))

    def entropia(self, distancias):
        frecuencias = self.calcula_frecuencia_hamming(distancias)
        total = len(distancias)
        entropia = 0
        for distancia in frecuencias:
            frecuencias[distancia] = frecuencias[distancia]/total
            entropia += frecuencias[distancia] * math.log(frecuencias[distancia])
        return entropia*-1

    def calcula_frecuencia_hamming(self, distancias_hamming):
        frecuencia = {}
        for distancia in distancias_hamming:
            if distancia in frecuencia:
                frecuencia[distancia] += 1
            else:
                frecuencia[distancia] = 1
        return frecuencia
        
    def encuentra_peor_evaluacion(self, fuentes):
        peor_evaluacion = float("inf")
        for i in fuentes:
            evaluacion = self.knapsack.funcion_evaluacion(i.solucion)
            if evaluacion < peor_evaluacion:
                peor_evaluacion = evaluacion
        return peor_evaluacion

    def calcula_promedio(self, fuentes):
        promedio = 0
        for i in fuentes:
            promedio += self.knapsack.funcion_evaluacion(i.solucion)
        promedio = promedio/len(fuentes)
        return promedio
        
    def abc(self):
        archivo = "output/ABC/" + self.nombre_archivo + str(self.numero_ejecucion) + ".txt"
        file = open(archivo, 'w')
        file.write("iteracion  mejor_solucion       peor_solucion                   promedio                             distancia_euclidiana                         distancia_hamming                             entropia\n")
        mejor_evaluacion = 0
        peor_evaluacion = 0
        promedio_evaluacion = 0
        fuentes = [Fuente(self.knapsack.generar_solucion_numpy()) for _ in range(self.numero_fuentes)]
        mejor_fuente = self.knapsack.selecciona_mejor_fuente(fuentes)
        for j in range(self.iteraciones):
            for i in range(self.numero_fuentes):
                fuentes = self.abeja_empleada(i, fuentes)
            fuentes = self.abeja_observadora(fuentes)
            fuentes = self.abeja_exploradora(fuentes)
            mejor_fuente = self.knapsack.selecciona_mejor_fuente(fuentes)
            mejor_evaluacion = self.knapsack.funcion_evaluacion(mejor_fuente.solucion)
            peor_evaluacion = self.encuentra_peor_evaluacion(fuentes)
            promedio_evaluacion = self.calcula_promedio(fuentes)
            promedio_hamming, promedio_euclidiana, distancias = self.evaluar_diversidad(fuentes)
            entropia = self.entropia(distancias)
            file.write(str(j) + "               " + str(mejor_evaluacion) + "                " + str(peor_evaluacion) + "                    "+ str(promedio_evaluacion) + "                             " + str(promedio_euclidiana) + "                                    " + str(promedio_hamming) + "                                        " + str(entropia) +  "\n")
        file.write("// Semilla: " + str(self.semilla))
        file.close()
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
    """ capacidad_mochila = 50
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
    print(abc.knapsack.funcion_evaluacion(mejor_solucion.solucion)) """
    
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Uso: python ABC.py [No. archivo] [No. ejecucion] [semilla]")
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
    abc = ABC(pesos, valores, semilla=semilla, numero_ejecucion=numero_ejecucion, nombre_archivo=nombre, capacidad_mochila=capacidad)
    mejor_solucion = abc.abc()
    print(f'Solución: {mejor_solucion.solucion}')
    print(f'Evaluación: {abc.knapsack.funcion_evaluacion(mejor_solucion.solucion)}')
    print(f'Peso: {abc.knapsack.peso_total(mejor_solucion.solucion)}')