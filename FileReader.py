
class FileReader:
    
    @staticmethod
    def leer_archivo(archivo):
        """ Función que genera una instancia de Coloracion
            a partir de leer un archivo en el que describe
            una gráfica.

        Args:
            archivo (string): nombre del archivo a leer

        Returns:
            Coloracion: Instancia de la clase Coloracion con
            la gráfica descrita en el archivo
        """
        pesos = []
        valores = []
        with open(archivo, 'r') as datos:
            for linea in datos:
                cadena = linea.strip().split()
                if len(cadena) != 2:
                    continue
                pesos.append(int(cadena[0]))
                valores.append(int(cadena[1]))
        return pesos, valores