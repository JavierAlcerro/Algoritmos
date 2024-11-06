from ColaEspecial import ColaEspecial
import time 

def PruebaColaEspecial():
    cola = ColaEspecial()
    elementos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    
    for elemento in elementos:
        cola.insertar(elemento) 
        cola.imprimir_cola()    
        time.sleep(0.5)         

if __name__ == "_main_":
    PruebaColaEspecial()