from random import random, randint
import math
def VIP(x):#determina el tipo de boleto
    if x > 0.330:
        return True
    else:
        return False

def destinos(x, bol,destC,bolT, acumT):#Evaluacion de las variables con sus respectivas ciudades
    if x>0 and x<=0.020:#'Tibet'
        destC[0]+=1 #Acumulacion de las personas que visitan esa ciudad
        if VIP(bol):
            acumT+=[750] #Acumulacion  de las ganacias totales de la agencia
            bolT[0]+=1 #Cantidad de boletos vendidos segun su tipo Primera 0 / 1 Turista
            
        else: 
            acumT+=[630] 
            bolT[1]+=1
    elif x>0.020 and x<=0.090:#'Madrid'   590  480
        destC[1]+=1
        if VIP(bol):
            acumT+=[590] 
            bolT[0]+=1
            
        else: 
            acumT+=[480] 
            bolT[1]+=1
    elif x>0.090 and x<=0.240:#'Venecia'   540  420
        destC[2]+=1
        if VIP(bol):
            acumT+=[540] 
            bolT[0]+=1
            
        else: 
            acumT+=[420] 
            bolT[1]+=1
    elif x>0.240 and x<=0.440:#'Aruba'   230  110
        destC[3]+=1
        if VIP(bol):
            acumT+=[230] 
            bolT[0]+=1
            
        else: 
            acumT+=[110] 
            bolT[1]+=1
    elif x>0.440 and x<=0.640:#'Miami'   310  190
        destC[4]+=1
        if VIP(bol):
            acumT+=[310] 
            bolT[0]+=1
            
        else: 
            acumT+=[190] 
            bolT[1]+=1
    elif x>0.640 and x<=0.800:#'Acapulco'  450  330
        destC[5]+=1
        if VIP(bol):
            acumT+=[450] 
            bolT[0]+=1
            
        else: 
            acumT+=[330] 
            bolT[1]+=1
    elif x>0.800 and x<=0.900:#'París'   665  545
        destC[6]+=1
        if VIP(bol):
            acumT+=[665] 
            bolT[0]+=1
            
        else: 
            acumT+=[545] 
            bolT[1]+=1
    elif x>0.900 and x<=0.960:#'Río de Janeiro'   428  308
        destC[7]+=1
        if VIP(bol):
            acumT+=[428] 
            bolT[0]+=1
            
        else: 
            acumT+=[308] 
            bolT[1]+=1
    elif x>0.960 and x<=0.990:#'Buenos Aires'  497  377
        destC[8]+=1
        if VIP(bol):
            acumT+=[497] 
            bolT[0]+=1
            
        else: 
            acumT+=[377] 
            bolT[1]+=1
    else:#'Londres'  685  565
        destC[9]+=1
        if VIP(bol):
            acumT+=[685]
            bolT[0]+=1
            
        else: 
            acumT+=[565] 
            bolT[1]+=1

def num_ale(n):#generador de numero aleatorio
    aleatorios = [randint(0, 1000)*0.001 for i in range (n)] #genera un lista con los numeros aleatorios
    return aleatorios

def simul():
    print("Ingrese el numero de intervalos")#ingrese le numero de intervalos
    n=int(input())
    paqt=num_ale(n)#numero de dias o intervalos
    i=0
    acumT=[0]
    destC=[0 for u in range(10)] #lista de los contadores de las ciudades
    bolT=[0, 0] #contador de la cantidad de boletos vendidos [0] primera/ [1] turista
    
    print(paqt)
    while i < n:
        paq15(paqt[i], destC, bolT, acumT)
        i+=1
    C=0
    i=0
    j=0
    while i<10:
        if destC[i]>C:
            C=destC[i]
            j=i
        i+=1
    destCN=["Tibet", "Madrid"," Venecia", "Aruba", "Miami", "Acapulco", "París"," Río de Janeiro", "Buenos", "Aires", "Londres"]
    print("El destino mas solicitado es : ",destCN[j], " ,"," con una cantidad de ", destC[j]," personas")
    if bolT[0]>bolT[1]:
        print("El mayor numero de boletos vendidos son los de Primera Clase con: ",bolT[0], " boletos ")
    else:
        print("El mayor numero de boletos vendidos son los de Clase Turista con: ",bolT[1], " boletos ")
    i=0
    z=bolT[0]+bolT[1]
    acumTT=0
    while i< z:
        acumTT+=acumT[i]
        i+=1
    print("Ganancia Total $",acumTT)

def paq15(paq, destC, bolT, acumT):
    z=0
    #cantidad de paquetes por dia
    if paq>0  and paq<=0.060:
        z=0#Buenas tardes nadie compro nada 
    elif paq>0.060 and paq<=0.150:#1
        z=1
        itpersn(z, destC, bolT, acumT)
    elif paq>0.150 and paq<=0.260:#2
        itpersn(2, destC, bolT, acumT)
    elif paq>0.260 and paq<=0.400:#3
        itpersn(3, destC, bolT, acumT)
    elif paq>0.400 and paq<=0.580:#4
        itpersn(4, destC, bolT, acumT)
    elif paq>0.580 and paq<=0.810:#5
        itpersn(5, destC, bolT, acumT)
    elif paq>0.810 and paq<=0.950:#6
        itpersn(6, destC, bolT, acumT)
    else:#7
        itpersn(7, destC, bolT, acumT)  

def itpersn(i, destC, bolT, acumT):
    j=0
    while j<i:
        a=0
        w=0
        aleP=num_ale(1)
        paqt=num_ale(1)
        if aleP[0]>=0 and aleP[0]<=0.250:#cantidad de personas 1
            bol=num_ale(1)
            destinos(paqt[0],bol[0],destC, bolT, acumT)
        elif aleP[0]>0.250 and aleP[0]<=0.730:#2
            a=2
            while w<a :
                bol=num_ale(1)
                destinos(paqt[0],bol[0],destC, bolT, acumT)
                w+=1
            
        elif aleP[0]>0.730 and aleP[0]<=0.880:#3
            a=3
            while w<a:
                bol=num_ale(1)
                destinos(paqt[0],bol[0],destC, bolT, acumT)
                w+=1
        
        elif aleP[0]>0.880 and aleP[0]<=0.960:#4
            a=4
            while w<a:
                bol=num_ale(1)
                destinos(paqt[0],bol[0],destC, bolT, acumT)
                w+=1
        else:#5"""
            a=5
            while w<a:
                bol=num_ale(1)
                destinos(paqt[0],bol[0],destC, bolT, acumT)
                w+=1
        j+=1

print("hola")
simul()
