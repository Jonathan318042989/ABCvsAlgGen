import random

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