import random
import matplotlib.pyplot as plt

class AlgoritmoGeneticoMochila:
    def __init__(self, capacidad_mochila, pesos, valores, num_elementos, poblacion_tamano=20, iteraciones=1000, prob_mutacion=0.1):
        self.capacidad_mochila = capacidad_mochila
        self.pesos = pesos
        self.valores = valores
        self.num_elementos = num_elementos
        self.poblacion_tamano = poblacion_tamano
        self.iteraciones = iteraciones
        self.prob_mutacion = prob_mutacion

    def funcion_objetivo(self, solucion):
        peso_total = sum(solucion[i] * self.pesos[i] for i in range(self.num_elementos))
        valor_total = sum(solucion[i] * self.valores[i] for i in range(self.num_elementos))
        if peso_total > self.capacidad_mochila:
            return 0 
        else:
            return valor_total

    def evaluar_poblacion(self, poblacion):
        evaluaciones = []
        for individuo in poblacion:
            evaluacion = self.funcion_objetivo(individuo)
            evaluaciones.append((individuo, evaluacion))
        return evaluaciones

    def seleccionar_padres(self, evaluaciones):
        total_fitness = sum(1 / (evaluacion[1] + 1) for evaluacion in evaluaciones)
        padres_seleccionados = []
        while len(padres_seleccionados) < 2:
            punto = random.uniform(0, total_fitness)
            acumulado = 0
            for individuo, evaluacion in evaluaciones:
                acumulado += 1 / (evaluacion + 1)
                if acumulado > punto:
                    padres_seleccionados.append(individuo)  # Almacenar el individuo, no la tupla
                    break
        return padres_seleccionados

    def cruzar_padres(self, padre1, padre2):
        punto_cruza = random.randint(0, self.num_elementos - 1)
        hijo1 = padre1[:punto_cruza] + padre2[punto_cruza:]
        hijo2 = padre2[:punto_cruza] + padre1[punto_cruza:]
        return hijo1, hijo2

    def mutar(self, individuo):
        for i in range(self.num_elementos):
            if random.random() < self.prob_mutacion:
                individuo[i] = 1 - individuo[i] 
        return individuo

    def algoritmo_genetico(self):
        poblacion = [self.generar_solucion() for _ in range(self.poblacion_tamano)]
        mejores_valores = []

        for _ in range(self.iteraciones):
            evaluaciones = self.evaluar_poblacion(poblacion)
            mejor_evaluacion = max(evaluaciones, key=lambda x: x[1])[1]
            mejores_valores.append(mejor_evaluacion)
            padres = self.seleccionar_padres(evaluaciones)
            hijos = self.cruzar_padres(padres[0], padres[1])
            hijos_mutados = [self.mutar(hijo) for hijo in hijos]
            poblacion.extend(hijos_mutados)
            poblacion = sorted(poblacion, key=lambda x: self.funcion_objetivo(x), reverse=True)[:self.poblacion_tamano]

        mejor_solucion = max(poblacion, key=lambda x: self.funcion_objetivo(x))
        return mejor_solucion, mejores_valores

    def generar_solucion(self):
        return [random.randint(0, 1) for _ in range(self.num_elementos)]


if __name__ == "__main__":
    capacidad_mochila = 50
    pesos = [10, 20, 30, 15, 5]
    valores = [100, 250, 150, 80, 60]
    num_elementos = len(pesos)

    alg_gen = AlgoritmoGeneticoMochila(capacidad_mochila, pesos, valores, num_elementos)
    mejor_solucion, mejores_valores = alg_gen.algoritmo_genetico()

    print("Mejor solución encontrada:")
    for i in range(num_elementos):
        if mejor_solucion[i] == 1:
            print(f"Objeto {i+1} - Peso: {pesos[i]}, Valor: {valores[i]}")

    plt.plot(mejores_valores)
    plt.xlabel('Iteraciones')
    plt.ylabel('Mejor valor de la función objetivo')
    plt.title('Evolución del valor de la función objetivo')
    plt.grid(True)
    plt.show()
