import matplotlib.pyplot as plt 
import numpy as np

class Graficacion:
    @staticmethod
    def grafica_txt(archivos, titulo, iteraciones, nombre_png):
        x = []
        y = []
        i = 0
        for archivo in archivos:
            z = []
            for linea in open(archivo, 'r'):
                lineas = [i for i in linea.split()]
                if(lineas[0] == "iteracion" or lineas[0] == "//"):
                    continue
                if int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1:
                    if i == 0:
                        x.append(lineas[0])
                    z.append(float(lineas[1]))
            y.append(z)
            i += 1
        plt.title(titulo)
        plt.xlabel("Iteraciones")
        plt.ylabel("Evaluacion")
        #plt.yticks(y)
        colores = ('r', 'b', 'g', 'c', 'm')
        labels = ('exponencial', 'lineal', 'generacional', 'generacional_elitismo', 'reemplazo_peores')
        for i in range(len(y)):
            plt.plot(x,y[i],marker ='o', c = colores[i], label=labels[i])
        plt.legend(loc='best')
        plt.savefig(nombre_png)
        plt.show()
        
    @staticmethod
    def grafica_distancias_euclidianas(archivos, titulo, iteraciones, nombre_png):
        x = []
        y = []
        i = 0
        for archivo in archivos:
            z = []
            for linea in open(archivo, 'r'):
                lineas = [i for i in linea.split()]
                if(lineas[0] == "iteracion" or lineas[0] == "//"):
                    continue
                if int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1:
                    if i == 0:
                        x.append(lineas[0])
                    if "Recocido" in archivo:    
                        z.append(float(lineas[2]))
                    elif "Genetico" in archivo:
                        z.append(float(lineas[4]))
            y.append(z)
            i += 1
        plt.title(titulo)
        plt.xlabel("Iteraciones")
        plt.ylabel("Distancia euclidiana")
        #plt.yticks(y)
        colores = ('r', 'b', 'g', 'c', 'm')
        labels = ('exponencial', 'lineal', 'generacional', 'generacional_elitismo', 'reemplazo_peores')
        for i in range(len(y)):
            plt.plot(x,y[i],marker ='o', c = colores[i], label=labels[i])
        plt.legend(loc='best')
        plt.savefig(nombre_png)
        plt.show()
    
    @staticmethod
    def grafica_distancias_hamming(archivos, titulo, iteraciones, nombre_png):
        x = []
        y = []
        i = 0
        for archivo in archivos:
            z = []
            for linea in open(archivo, 'r'):
                lineas = [i for i in linea.split()]
                if(lineas[0] == "iteracion" or lineas[0] == "//"):
                    continue
                if int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1:
                    if i == 0:
                        x.append(lineas[0])
                    if "Recocido" in archivo:    
                        z.append(float(lineas[3]))
                    elif "Genetico" in archivo:
                        z.append(float(lineas[5]))
            y.append(z)
            i += 1
        plt.title(titulo)
        plt.xlabel("Iteraciones")
        plt.ylabel("Distancia hamming")
        #plt.yticks(y)
        colores = ('r', 'b', 'g', 'c', 'm')
        labels = ('exponencial', 'lineal', 'generacional', 'generacional_elitismo', 'reemplazo_peores')
        for i in range(len(y)):
            plt.plot(x,y[i],marker ='o', c = colores[i], label=labels[i])
        plt.legend(loc='best')
        plt.savefig(nombre_png)
        plt.show()
        
    @staticmethod
    def grafica_entropia(archivos, titulo, iteraciones, nombre_png):
        x = []
        y = []
        i = 0
        for archivo in archivos:
            if "Recocido" in archivo: continue
            z = []
            for linea in open(archivo, 'r'):
                lineas = [i for i in linea.split()]
                if(lineas[0] == "iteracion" or lineas[0] == "//"):
                    continue
                if int(lineas[0]) != 0 and (int(lineas[0]) == 1 or int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1):
                    if i == 0:
                        x.append(lineas[0])
                    z.append(float(lineas[6]))
            y.append(z)
            i += 1
        plt.title(titulo)
        plt.xlabel("Iteraciones")
        plt.ylabel("Entropia")
        #plt.yticks(y)
        colores = ('r', 'b', 'g', 'c', 'm')
        labels = ('generacional', 'generacional_elitismo', 'reemplazo_peores')
        for i in range(len(y)):
            plt.plot(x,y[i],marker ='o', c = colores[i], label=labels[i])
        plt.legend(loc='best')
        plt.savefig(nombre_png)
        plt.show()
        
    @staticmethod
    def grafica_promedios():
            x = []
            funciones = {"sphere", "ackley", "griewank", "rastrigin", "rosenbrock"}
            enfriamientos = {"exponencial", "lineal"}
            reemplazos = {"generacional", "generacional_elitismo", "peores"}
            algoritmos = {"Recocido", "Genetico"}
            valor_x = 0
            iteraciones = 1000
            for funcion in funciones:
                y = {}
                for algoritmo in algoritmos:
                    if algoritmo == "Recocido":
                        for enfriamiento in enfriamientos:
                            promedio_estrategia = {}
                            z = []
                            for i in range(1,31):
                                archivo = "output/" + funcion + "/" + algoritmo + "/" + enfriamiento + "/" + funcion + "_" + enfriamiento + "_" + str(i) + ".txt"
                                for linea in open(archivo, 'r'):
                                    lineas = [i for i in linea.split()]
                                    if(lineas[0] == "iteracion" or lineas[0] == "//"):
                                        continue
                                    if int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1:
                                        if valor_x == 0:
                                            x.append(lineas[0])   
                                        if int(lineas[0]) in promedio_estrategia:
                                            promedio_estrategia[int(lineas[0])] += float(lineas[1])
                                        else:
                                            promedio_estrategia[int(lineas[0])] = float(lineas[1])
                                valor_x +=1
                            for s in promedio_estrategia:
                                promedio_estrategia[s] = promedio_estrategia[s]/30
                                z.append(promedio_estrategia[s])
                                    
                            y[enfriamiento] = z
                    else:
                        for reemplazo in reemplazos:
                            promedio_estrategia = {}
                            z = []
                            for i in range(1,31):
                                archivo = "output/" + funcion + "/" + algoritmo + "/" + reemplazo + "/" + funcion + "_" + reemplazo + "_" + str(i) + ".txt"
                                for linea in open(archivo, 'r'):
                                    lineas = [i for i in linea.split()]
                                    if(lineas[0] == "iteracion" or lineas[0] == "//"):
                                        continue
                                    if int(lineas[0])%int(iteraciones/20) == 0 or int(lineas[0]) == iteraciones-1:
                                        if valor_x == 0:
                                            x.append(lineas[0])   
                                        if int(lineas[0]) in promedio_estrategia:
                                            promedio_estrategia[int(lineas[0])] += float(lineas[1])
                                        else:
                                            promedio_estrategia[int(lineas[0])] = float(lineas[1])
                                valor_x +=1
                            for s in promedio_estrategia:
                                promedio_estrategia[s] = promedio_estrategia[s]/30
                                z.append(promedio_estrategia[s])
                            y[reemplazo] = z
                Graficacion.grafica_ejes(x, y, "Promedio", funcion)
                            
    @staticmethod
    def grafica_ejes(x, y, titulo, funcion):
        plt.title(str(titulo + " " + funcion))
        plt.xlabel("Iteraciones")
        plt.ylabel("Evaluacion")
        #plt.yticks(y)
        colores = {"exponencial":'r',"lineal": 'b',"generacional": 'g', "generacional_elitismo": 'c',"peores": 'm'}
        labels = {"exponencial":'exponencial',"lineal": 'lineal',"generacional": 'generacional',"generacional_elitismo": 'generacional_elitismo',"peores": 'reemplazo_peores'}
        for estrategia in labels:
            plt.plot(x,y[str(estrategia)],marker ='o', c = colores[estrategia], label=labels[estrategia])
        plt.legend(loc='best')
        plt.savefig('output/Graficas/evolucion_promedio_' + funcion +'_1.png')
        plt.show()

    @staticmethod
    def datos():
        funciones = {"sphere", "ackley", "griewank", "rastrigin", "rosenbrock"}
        enfriamientos = {"exponencial", "lineal"}
        reemplazos = {"generacional", "generacional_elitismo", "peores"}
        algoritmos = {"Recocido", "Genetico"}
        id = 1
        for funcion in funciones:
            for algoritmo in algoritmos:
                if algoritmo == "Recocido":
                    for enfriamiento in enfriamientos:
                        mejor = float('inf')
                        peor = float(-1)
                        promedio = 0
                        valores = []
                        for i in range(1,31):
                            archivo = "output/" + funcion + "/" + algoritmo + "/" + enfriamiento + "/" + funcion + "_" + enfriamiento + "_" + str(i) + ".txt"
                            with open(archivo, 'r') as f:
                                ultima = f.readlines()[-2]
                                lineas = [i for i in ultima.split()]
                                if float(lineas[1]) < mejor:
                                    mejor = float(lineas[1])
                                if float(lineas[1]) > peor:
                                    peor = float(lineas[1])
                                promedio += float(lineas[1])
                                valores.append(float(lineas[1]))
                        promedio /= 30
                        valores.sort()
                        mediana = .5 * (valores[15] + valores[16])
                        varianza = np.var(valores, ddof=1)
                        desviacion = np.sqrt(varianza)
                        print(f"Funcion {funcion}  Enfriamiento {enfriamiento} {id}")
                        print(f"Mejor {mejor}")
                        print(f"Peor {peor}")
                        print(f"Promedio {promedio}")
                        print(f"Mediana {mediana}")
                        print(f"Varianza {varianza}")
                        print(f"Desviacion {desviacion}")
                        id +=1
                elif algoritmo == "Genetico":
                    for reemplazo in reemplazos:
                        mejor = float('inf')
                        peor = float(-1)
                        promedio = 0
                        valores = []
                        for i in range(1,31):
                            archivo = "output/" + funcion + "/" + algoritmo + "/" + reemplazo + "/" + funcion + "_" + reemplazo + "_" + str(i) + ".txt"
                            with open(archivo, 'r') as f:
                                ultima = f.readlines()[-2]
                                lineas = [i for i in ultima.split()]
                                if float(lineas[1]) < mejor:
                                    mejor = float(lineas[1])
                                if float(lineas[2]) > peor:
                                    peor = float(lineas[2])
                                promedio += float(lineas[3])
                                valores.append(float(lineas[1]))
                        promedio /= 30
                        valores.sort()
                        mediana = .5 * (valores[15] + valores[16])
                        varianza = np.var(valores, ddof=1)
                        desviacion = np.sqrt(varianza)
                        print(f"Funcion {funcion}  Reemplazo {reemplazo} {id}")
                        print(f"Mejor {mejor}")
                        print(f"Peor {peor}")
                        print(f"Promedio {promedio}")
                        print(f"Mediana {mediana}")
                        print(f"Varianza {varianza}")
                        print(f"Desviacion {desviacion}")
                        id += 1
                                
        
    @staticmethod
    def grafica_boxplot(archivos, titulo, nombre_png):
        datos = []
        for archivo in archivos:
            z = []
            for linea in open(archivo, 'r'):
                lineas = [i for i in linea.split()]
                if(lineas[0] == "iteracion" or lineas[0] == "//"):
                    continue
    
                z.append(float(lineas[1]))
            datos.append(z)
        
        fig, ax = plt.subplots()
        ax.boxplot(datos)
        ax.set_xlabel("Estrategia")
        ax.set_ylabel("Aptitud")
        plt.title(titulo)
        xticklabels = ["Exponencial", "Lineal", "Generacional", "Generacional elitismo", "Reemplazo peores"]
        ax.set_xticklabels(xticklabels)
        plt.savefig(nombre_png)
        plt.show()
                                
#Sphere
#output = output/Graficas/evolucion_aptitud_sphere_1.png
#output1 = "output/Graficas/distancia_euclidiana_sphere_1.png"
#output2 = "output/Graficas/distancia_hamming_sphere_1.png"
#output3 = "output/Graficas/entropia_sphere_1.png"
#output4 = "output/Graficas/boxplot_sphere_1.png"
#files = ["output/sphere/Recocido/exponencial/sphere_exponencial_23.txt", "output/sphere/Recocido/lineal/sphere_lineal_8.txt", "output/sphere/Genetico/generacional/sphere_generacional_6.txt", "output/sphere/Genetico/generacional_elitismo/sphere_generacional_elitismo_17.txt", "output/sphere/Genetico/peores/sphere_peores_12.txt"]
#output = output/Graficas/evolucion_aptitud_sphere_2.png
#output1 = "output/Graficas/distancia_euclidiana_sphere_2.png"
#output2 = "output/Graficas/distancia_hamming_sphere_2.png"
#output3 = "output/Graficas/entropia_sphere_2.png"
#output4 = "output/Graficas/boxplot_sphere_2.png"
#files = ["output/sphere/Recocido/exponencial/sphere_exponencial_3.txt", "output/sphere/Recocido/lineal/sphere_lineal_28.txt", "output/sphere/Genetico/generacional/sphere_generacional_26.txt", "output/sphere/Genetico/generacional_elitismo/sphere_generacional_elitismo_3.txt", "output/sphere/Genetico/peores/sphere_peores_16.txt"]
#output = output/Graficas/evolucion_aptitud_sphere_3.png
#output1 = "output/Graficas/distancia_euclidiana_sphere_3.png"
#output2 = "output/Graficas/distancia_hamming_sphere_3.png"
#output3 = "output/Graficas/entropia_sphere_3.png"
#output4 = "output/Graficas/boxplot_sphere_3.png"
#files = ["output/sphere/Recocido/exponencial/sphere_exponencial_10.txt", "output/sphere/Recocido/lineal/sphere_lineal_10.txt", "output/sphere/Genetico/generacional/sphere_generacional_10.txt", "output/sphere/Genetico/generacional_elitismo/sphere_generacional_elitismo_10.txt", "output/sphere/Genetico/peores/sphere_peores_10.txt"]
#Ackley
#output = output/Graficas/evolucion_aptitud_ackley_1.png
#output1 = "output/Graficas/evolucion_euclidiana_ackley_1.png"
#output2 = "output/Graficas/evolucion_hamming_ackley_1.png"
#output3 = "output/Graficas/entropia_ackley_1.png"
#output4 = "output/Graficas/boxplot_ackley_1.png"
#files = ["output/ackley/Recocido/exponencial/ackley_exponencial_13.txt", "output/ackley/Recocido/lineal/ackley_lineal_15.txt", "output/ackley/Genetico/generacional/ackley_generacional_19.txt", "output/ackley/Genetico/generacional_elitismo/ackley_generacional_elitismo_12.txt", "output/ackley/Genetico/peores/ackley_peores_9.txt"]
#output = output/Graficas/evolucion_aptitud_ackley_2.png
#output1 = "output/Graficas/evolucion_euclidiana_ackley_2.png"
#output2 = "output/Graficas/evolucion_hamming_ackley_2.png"
#output3 = "output/Graficas/entropia_ackley_2.png"
#output4 = "output/Graficas/boxplot_ackley_2.png"
#files = ["output/ackley/Recocido/exponencial/ackley_exponencial_3.txt", "output/ackley/Recocido/lineal/ackley_lineal_25.txt", "output/ackley/Genetico/generacional/ackley_generacional_9.txt", "output/ackley/Genetico/generacional_elitismo/ackley_generacional_elitismo_1.txt", "output/ackley/Genetico/peores/ackley_peores_29.txt"]
#output = output/Graficas/evolucion_aptitud_ackley_3.png
#output1 = "output/Graficas/evolucion_euclidiana_ackley_3.png"
#output2 = "output/Graficas/evolucion_hamming_ackley_3.png"
#output3 = "output/Graficas/entropia_ackley_3.png"
#output4 = "output/Graficas/boxplot_ackley_3.png"
#files = ["output/ackley/Recocido/exponencial/ackley_exponencial_8.txt", "output/ackley/Recocido/lineal/ackley_lineal_6.txt", "output/ackley/Genetico/generacional/ackley_generacional_3.txt", "output/ackley/Genetico/generacional_elitismo/ackley_generacional_elitismo_30.txt", "output/ackley/Genetico/peores/ackley_peores_14.txt"]
#Griewank
#output = "output/Graficas/evolucion_aptitud_griewank_1.png"
#output1 = "output/Graficas/evolucion_euclidiana_griewank_1.png"
#output2 = "output/Graficas/evolucion_hamming_griewank_1.png"
#output3 = "output/Graficas/entropia_griewank_1.png"
#output4 = "output/Graficas/boxplot_griewank_1.png"
#files = ["output/griewank/Recocido/exponencial/griewank_exponencial_12.txt", "output/griewank/Recocido/lineal/griewank_lineal_8.txt", "output/griewank/Genetico/generacional/griewank_generacional_29.txt", "output/griewank/Genetico/generacional_elitismo/griewank_generacional_elitismo_18.txt", "output/griewank/Genetico/peores/griewank_peores_21.txt"]
#output = "output/Graficas/evolucion_aptitud_griewank_2.png"
#output1 = "output/Graficas/evolucion_euclidiana_griewank_2.png"
#output2 = "output/Graficas/evolucion_hamming_griewank_2.png"
#output3 = "output/Graficas/entropia_griewank_2.png"
#output4 = "output/Graficas/boxplot_griewank_2.png"
#files = ["output/griewank/Recocido/exponencial/griewank_exponencial_6.txt", "output/griewank/Recocido/lineal/griewank_lineal_3.txt", "output/griewank/Genetico/generacional/griewank_generacional_11.txt", "output/griewank/Genetico/generacional_elitismo/griewank_generacional_elitismo_25.txt", "output/griewank/Genetico/peores/griewank_peores_12.txt"]
#output = "output/Graficas/evolucion_aptitud_griewank_3.png"
#output1 = "output/Graficas/evolucion_euclidiana_griewank_3.png"
#output2 = "output/Graficas/evolucion_hamming_griewank_3.png"
#output3 = "output/Graficas/entropia_griewank_3.png"
#output4 = "output/Graficas/boxplot_griewank_3.png"
#files = ["output/griewank/Recocido/exponencial/griewank_exponencial_8.txt", "output/griewank/Recocido/lineal/griewank_lineal_16.txt", "output/griewank/Genetico/generacional/griewank_generacional_21.txt", "output/griewank/Genetico/generacional_elitismo/griewank_generacional_elitismo_6.txt", "output/griewank/Genetico/peores/griewank_peores_8.txt"]
#Rastrigin
#output = "output/Graficas/evolucion_aptitud_rastrigin_1.png"
#output1 = "output/Graficas/evolucion_euclidiana_rastrigin_1.png"
#output2 = "output/Graficas/evolucion_hamming_rastrigin_1.png"
#output3 = "output/Graficas/entropia_rastrigin_1.png"
#output4 = "output/Graficas/boxplot_rastrigin_1.png"
#files = ["output/rastrigin/Recocido/exponencial/rastrigin_exponencial_16.txt", "output/rastrigin/Recocido/lineal/rastrigin_lineal_23.txt", "output/rastrigin/Genetico/generacional/rastrigin_generacional_16.txt", "output/rastrigin/Genetico/generacional_elitismo/rastrigin_generacional_elitismo_12.txt", "output/rastrigin/Genetico/peores/rastrigin_peores_14.txt"]
#output = "output/Graficas/evolucion_aptitud_rastrigin_2.png"
#output1 = "output/Graficas/evolucion_euclidiana_rastrigin_2.png"
#output2 = "output/Graficas/evolucion_hamming_rastrigin_2.png"
#output3 = "output/Graficas/entropia_rastrigin_2.png"
#output4 = "output/Graficas/boxplot_rastrigin_2.png"
#files = ["output/rastrigin/Recocido/exponencial/rastrigin_exponencial_21.txt", "output/rastrigin/Recocido/lineal/rastrigin_lineal_3.txt", "output/rastrigin/Genetico/generacional/rastrigin_generacional_6.txt", "output/rastrigin/Genetico/generacional_elitismo/rastrigin_generacional_elitismo_22.txt", "output/rastrigin/Genetico/peores/rastrigin_peores_6.txt"]
#output = "output/Graficas/evolucion_aptitud_rastrigin_3.png"
#output1 = "output/Graficas/evolucion_euclidiana_rastrigin_3.png"
#output2 = "output/Graficas/evolucion_hamming_rastrigin_3.png"
#output3 = "output/Graficas/entropia_rastrigin_3.png"
#output4 = "output/Graficas/boxplot_rastrigin_3.png"
#files = ["output/rastrigin/Recocido/exponencial/rastrigin_exponencial_29.txt", "output/rastrigin/Recocido/lineal/rastrigin_lineal_13.txt", "output/rastrigin/Genetico/generacional/rastrigin_generacional_26.txt", "output/rastrigin/Genetico/generacional_elitismo/rastrigin_generacional_elitismo_2.txt", "output/rastrigin/Genetico/peores/rastrigin_peores_24.txt"]
#Rosenbrock
#output = "output/Graficas/evolucion_aptitud_rosenbrock_1.png"
#output1 = "output/Graficas/evolucion_euclidiana_rosenbrock_1.png"
#output2 = "output/Graficas/evolucion_hamming_rosenbrock_1.png"
#output3 = "output/Graficas/entropia_rosenbrock_1.png"
#output4 = "output/Graficas/boxplot_rosenbrock_1.png"
#files = ["output/rosenbrock/Recocido/exponencial/rosenbrock_exponencial_12.txt", "output/rosenbrock/Recocido/lineal/rosenbrock_lineal_15.txt", "output/rosenbrock/Genetico/generacional/rosenbrock_generacional_25.txt", "output/rosenbrock/Genetico/generacional_elitismo/rosenbrock_generacional_elitismo_5.txt", "output/rosenbrock/Genetico/peores/rosenbrock_peores_26.txt"]
#output = "output/Graficas/evolucion_aptitud_rosenbrock_2.png"
#output1 = "output/Graficas/evolucion_euclidiana_rosenbrock_2.png"
#output2 = "output/Graficas/evolucion_hamming_rosenbrock_2.png"
#output3 = "output/Graficas/entropia_rosenbrock_2.png"
#output4 = "output/Graficas/boxplot_rosenbrock_2.png"
#files = ["output/rosenbrock/Recocido/exponencial/rosenbrock_exponencial_15.txt", "output/rosenbrock/Recocido/lineal/rosenbrock_lineal_25.txt", "output/rosenbrock/Genetico/generacional/rosenbrock_generacional_5.txt", "output/rosenbrock/Genetico/generacional_elitismo/rosenbrock_generacional_elitismo_26.txt", "output/rosenbrock/Genetico/peores/rosenbrock_peores_6.txt"]
#output = "output/Graficas/evolucion_aptitud_rosenbrock_3.png"
#output1 = "output/Graficas/evolucion_euclidiana_rosenbrock_3.png"
#output2 = "output/Graficas/evolucion_hamming_rosenbrock_3.png"
#output3 = "output/Graficas/entropia_rosenbrock_3.png"
#output4 = "output/Graficas/boxplot_rosenbrock_3.png"
#files = ["output/rosenbrock/Recocido/exponencial/rosenbrock_exponencial_21.txt", "output/rosenbrock/Recocido/lineal/rosenbrock_lineal_5.txt", "output/rosenbrock/Genetico/generacional/rosenbrock_generacional_16.txt", "output/rosenbrock/Genetico/generacional_elitismo/rosenbrock_generacional_elitismo_13.txt", "output/rosenbrock/Genetico/peores/rosenbrock_peores_16.txt"]

#Graficacion.grafica_distancias_euclidianas(files, "Distancia euclidiana para Rosenbrock", 1000, output1)
#Graficacion.grafica_distancias_hamming(files, "Distancia hamming para Rosenbrock", 1000, output2)
#Graficacion.grafica_entropia(files, "Entropia para Rosenbrock", 1000, output3)
#Graficacion.grafica_boxplot(files, "Sphere", output4)
#Graficacion.grafica_promedios()
Graficacion.datos()