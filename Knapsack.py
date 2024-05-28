import random
import numpy as np

class Knapsack:
    def __init__(self, pesos, valores):
        self.capacidad_mochila = 1000
        self.pesos = pesos
        self.valores = valores
        self.num_elementos = len(pesos)
        
    def funcion_evaluacion(self, solucion):
        """Funcion que evalúa una solución,
           suma el valor total de todos los objetos en la mochila
           penalizando aquellas que exceden la capacidad de la mochila.

        Args:
            solucion (array(int)): Representación de la solución

        Returns:
            int: Valor total de la carga de la mochila
        """
        peso_total = sum(solucion[i] * self.pesos[i] for i in range(self.num_elementos))
        valor_total = sum(solucion[i] * self.valores[i] for i in range(self.num_elementos))
        if peso_total > self.capacidad_mochila:
            return 0 
        else:
            return valor_total
        
    def generar_solucion(self):
        return [random.randint(0, 1) for _ in range(self.num_elementos)]
    
    def generar_solucion_numpy(self):
        return np.array([random.randint(0, 1) for _ in range(self.num_elementos)])
    
    def selecciona_mejor(self, poblacion):
        mejor_evaluacion = 0
        mejor = None
        for i in poblacion:
            evaluacion = self.funcion_evaluacion(i)
            if evaluacion > mejor_evaluacion:
                mejor_evaluacion = evaluacion
                mejor = i
        return mejor

    def selecciona_mejor_fuente(self, poblacion):
        mejor_evaluacion = 0
        mejor = None
        for i in poblacion:
            evaluacion = self.funcion_evaluacion(i.solucion)
            if evaluacion > mejor_evaluacion:
                mejor_evaluacion = evaluacion
                mejor = i
        return mejor

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
            for i in range(len(indices_individuos)):
                evaluacion = self.funcion_evaluacion(poblacion_actual[indices_individuos[i]])
                if evaluacion > mejor_evaluacion:
                    mejor_evaluacion = evaluacion
                    mejor_individuo_actual = poblacion_actual[indices_individuos[i]]
            if j == 0:
                padre1 = mejor_individuo_actual
            else:
                padre2 =mejor_individuo_actual
        return (padre1, padre2)
    
    def seleccion_fuente_torneo(self, colonia):
        """Función para seleccionar una fuente de la colonia

        Args:
            colonia (array(array(int))): colonia actual

        Returns:
            tuple: indice de la fuente seleccionada
        """
        indice= None
        indices_individuos = np.random.choice(len(colonia), size=int(len(colonia)/10), replace=False)
        mejor_evaluacion = 0
        for i in range(len(indices_individuos)):
            evaluacion = self.funcion_evaluacion(colonia[indices_individuos[i]].solucion)
            if evaluacion > mejor_evaluacion:
                mejor_evaluacion = evaluacion
                indice = indices_individuos[i]
            
        return indice
    