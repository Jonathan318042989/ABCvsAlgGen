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
                    z.append(float(lineas[5])) #Cambiar dependiendo que se quiere graficar
            y.append(z)
            i += 1
        plt.title(titulo)
        plt.xlabel("Iteraciones")
        plt.ylabel("Distancia")
        #plt.yticks(y)
        colores = ('r', 'b')
        labels = ('AG', 'ABC')
        for i in range(len(y)):
            plt.plot(x,y[i],marker ='o', c = colores[i], label=labels[i])
        plt.legend(loc='best')
        plt.savefig(nombre_png)
        #plt.show()
        plt.clf()
    
        
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
        xticklabels = ["AG", "ABC"]
        ax.set_xticklabels(xticklabels)
        plt.savefig(nombre_png)
        #plt.show()
        plt.clf()
                                

#Mejores
""" for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Mejor/mejor_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Mejor/mejor_f8_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_txt(files1, "Mejores evaluaciones", 1000, output1)
    Graficacion.grafica_txt(files11, "Mejores evaluaciones", 1000, output11) """
    
#Promedio
""" for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Promedio/promedio_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Promedio/promedio_f8_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_txt(files1, "Promedio evaluaciones", 1000, output1)
    Graficacion.grafica_txt(files11, "Promedio evaluaciones", 1000, output11) """
    
#Euclidiana
""" for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Euclidiana/euclidiana_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Euclidiana/euclidiana_f8_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_txt(files1, "Distancia Euclidiana", 1000, output1)
    Graficacion.grafica_txt(files11, "Distancia Euclidiana", 1000, output11) """
    
#Hamming
""" for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Hamming/hamming_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Hamming/hamming_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_txt(files1, "Distancia Hamming", 1000, output1)
    Graficacion.grafica_txt(files11, "Distancia Hamming", 1000, output11)"""  
    
#Entropia
""" for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Entropia/entropia_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Entropia/entropia_f8_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_txt(files1, "Entropia", 1000, output1)
    Graficacion.grafica_txt(files11, "Entropia", 1000, output11)"""
    
#Boxplot
for i in range(30):
    archivo1 = "output/AG/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    archivo2 = "output/ABC/f2_l-d_kp_20_878_" + str(i+1) + ".txt"
    files1 = [archivo1, archivo2]
    output1 = "output/Graficas/Boxplot/boxplot_kp_20_878_" + str(i+1) + ".png"
    archivo11 = "output/AG/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    archivo22 = "output/ABC/f8_l-d_kp_23_10000_" + str(i+1) + ".txt"
    files11 = [archivo11, archivo22]
    output11 = "output/Graficas/Boxplot/boxplot_f8_l-d_kp_23_10000_" + str(i+1) + ".png"
    Graficacion.grafica_boxplot(files1, "", output1)
    Graficacion.grafica_boxplot(files11, "", output11)