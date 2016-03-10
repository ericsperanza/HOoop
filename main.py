import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #Construyor un nuevo generador de senales
    new_Gen = generador.Generador(amplitud,fase,frecuencia)
    senal_generada = (new_Gen.generar(tiempo_inicial,tiempo_final))
    print senal_generada
    #TODO construir un detector
    new_Det = detector.Detector()
    print(new_Det.detectar(senal_generada))

    #TODO construir un nuevo radar


    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO contruir un nuevo blanco


    #TODO contruir un medio

    #TODO llamar al radar

if __name__ == "__main__":
    main()
