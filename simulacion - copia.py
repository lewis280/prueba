from random import random, randint
import math
def VIP(x):#determina el tipo de boleto
    if x > 0.330:
        return True
    else:
        return False

def destinos(x, bol,destC,bolT, acumT):#Evaluacion de las variables con sus respectivas ciudades
    if x>=0 and x<0.020:#'Tibet'
        destC[0]+=1 #Acumulacion de las personas que visitan esa ciudad
        if VIP(bol):
            acumT+=[750] #Acumulacion  de las ganacias totales de la agencia
            bolT[0]+=1 #Cantidad de boletos vendidos segun su tipo Primera 0 / 1 Turista
            
        else: 
            acumT+=[630] 
            bolT[1]+=1
    elif x>=0.020 and x<0.090:#'Madrid'   590  480
        destC[1]+=1
        if VIP(bol):
            acumT+=[590] 
            bolT[0]+=1
            
        else: 
            acumT+=[480] 
            bolT[1]+=1
    elif x>=0.090 and x<0.240:#'Venecia'   540  420
        destC[2]+=1
        if VIP(bol):
            acumT+=[540] 
            bolT[0]+=1
            
        else: 
            acumT+=[420] 
            bolT[1]+=1
    elif x>=0.240 and x<0.440:#'Aruba'   230  110
        destC[3]+=1
        if VIP(bol):
            acumT+=[230] 
            bolT[0]+=1
            
        else: 
            acumT+=[110] 
            bolT[1]+=1
    elif x>=0.440 and x<0.640:#'Miami'   310  190
        destC[4]+=1
        if VIP(bol):
            acumT+=[310] 
            bolT[0]+=1
            
        else: 
            acumT+=[190] 
            bolT[1]+=1
    elif x>=0.640 and x<0.800:#'Acapulco'  450  330
        destC[5]+=1
        if VIP(bol):
            acumT+=[450] 
            bolT[0]+=1
            
        else: 
            acumT+=[330] 
            bolT[1]+=1
    elif x>=0.800 and x<0.900:#'París'   665  545
        destC[6]+=1
        if VIP(bol):
            acumT+=[665] 
            bolT[0]+=1
            
        else: 
            acumT+=[545] 
            bolT[1]+=1
    elif x>=0.900 and x<0.960:#'Río de Janeiro'   428  308
        destC[7]+=1
        if VIP(bol):
            acumT+=[428] 
            bolT[0]+=1
            
        else: 
            acumT+=[308] 
            bolT[1]+=1
    elif x>=0.960 and x<0.990:#'Buenos Aires'  497  377
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

#generador de numero aleatorio

def MetCMult(a1, xo1, m1, n, RN):#Metodo c Multiplicativo
    a=int(a1)
    xo=[int(xo1)]
    m=int(m1)
    i=0
    arr=[0]
    arrM=[0]
    while i<n:
        arr+=[a*xo[i]]
        i+=1
        arrM+=[arr[i] % m]
        xo+=[arrM[i]]
        RN+=[(int((xo[i-1]/m)*1000))/1000]

def MetCMix(a1,c1,xo1,m1,n, RN):#metodo C mixto
    a=int(a1)
    c=int(c1)
    xo=[int(xo1)]
    m=int(m1)
    i=0
    arr=[0]
    arrM=[0]
    while i<n:
        arr+=[a*xo[i]+c]
        i+=1
        arrM+=[arr[i] % m]
        xo+=[arrM[i]]
        RN+=[(int((xo[i-1]/m)*1000))/1000]

def cero(a, k):
    x=len(a)
    while ((x-k)<=0)or(((x-k)%2)!=0):
        a='0'+a
        x=len(a)
    x=len(a)
    h=""
    g=a
    while x!=k:
        h=g[1:-1]
        g=h
        x=len(h)
    a=g
    return(a)

def PmedioV(cs, x, n,RN):
    c=len(cs)
    xx=0
    cc=""
    i=0
    acum=[int(x)]
    while i<n:
        xx=int(cs)*acum[i]
        cc=str(xx)
        acum+=[int(cero(cc, c))]
        RN+=[cerocoma(acum[i+1], c)]
        i+=1

def cmedio(s,n,RN):
    acum=[int(s)]
    c=len(s)
    i=0
    x=0
    cc=""
    while i<n:
        x=acum[i]**2
        cc=str(x)
        acum+=[int(cero(cc, c))]
        RN+=[cerocoma(acum[i+1], c)]
        i+=1

def Pmedio(x1, x2, n,RN):
    c=len(x1)
    xx=0
    cc=""
    i=0
    acum=[int(x1), int(x2)]
    while i<n:
        xx=acum[i]*acum[i+1]
        cc=str(xx)
        acum+=[int(cero(cc, c))]
        RN+=[cerocoma(acum[i+2], c)]
        i+=1
def cerocoma(x, c):
    cadena=0
    i=0
    cadena2=""
    cadena3=0
    while i<c:
        cadena2='0' + cadena2
        i+=1
    cadena2='1'+cadena2
    cadena3=int(cadena2)
    cadena=x/cadena3
    return cadena

def escojermet(RN):# procedimiento de entrada de valores y validacion
    i=1
    z=0
    nn=0
    opc=0
    while i==1:
        print("Seleccione el metodo de generacion de numeros aleatorios")
        print("1-Metodo de Cuadrado Medio")
        print("2-Metodo Producto Medio")
        print("3-Metodo Producto Medio Variacion")
        print("4-Metodo Congruencial Mixto")
        print("5-Metodo Congruencial Multiplicativo")
        opc=int(input())
        if opc==1:
            i=0
            while z==0:
                print("Ingrese el numero de intervalos")
                n=input()
                print("Ingrese la semilla")
                s=input()
                if n.isdigit() and s.isdigit():
                    nn=int(n)*50
                    cmedio(s, nn, RN)
                    z=1
                else:
                    print("Ingrese solo numeros")
        elif opc==2:
             i=0
             while z==0:
                print("Ingrese el numero de intervalos")
                n=input()
                print("Ingrese la semilla 1")
                x1=input()
                print("Ingrese la semilla 2")
                x2=input()
                if n.isdigit() and x1.isdigit() and x2.isdigit():
                    nn=int(n)*50
                    Pmedio(x1, x2, nn, RN)
                    z=1
                else:
                    print("Ingrese solo numeros")
        elif opc==3:
            i=0
            while z==0:
                print("Ingrese el numero de intervalos")
                n=input()
                print("Ingrese la semilla")
                x1=input()
                print("Ingrese la constante")
                con=input()
                if n.isdigit() and x1.isdigit() and con.isdigit():
                    nn=int(n)*50
                    PmedioV(con, x1, nn, RN)
                    z=1
                else:
                    print("Ingrese solo numeros")
        elif opc==4:
            i=0
            while z==0:
                print("Ingrese el numero de intervalos")
                n=input()
                print("Ingrese el multiplicador")
                a1=input()
                print("Ingrese la constante")
                c1=input()
                print("Ingrese la semilla")
                xo1=input()
                print("Ingrese el modulo")
                m1=input()
                if n.isdigit() and a1.isdigit() and c1.isdigit() and xo1.isdigit() and m1.isdigit():
                    if (int(m1)<int(xo1) and int(m1)<int(c1) and int(m1)<int(a1)) and (int(a1)<0 and int(c1)<0 and int(xo1)<0):
                        print("Ingrese los valores adecuados.Multiplicador constante y semilla mayor a 0.")
                        print("Modulo mayor a los anteriores")
                    else:
                        nn=int(n)*50
                        MetCMix(a1, c1, xo1, m1, nn, RN)
                        z=1
                else:
                    print("Ingrese solo numeros")
        elif opc==5:
            i=0
            while z==0:
                print("Ingrese el numero de intervalos")
                n=input()
                print("Ingrese el multiplicador")
                a1=input()
                print("Ingrese la semilla")
                xo1=input()
                print("Ingrese el modulo")
                m1=input()
                mm=[2]
                i=0
                while i<100:
                    mm+=[mm[i]*2]
                    i+=1
                if n.isdigit() and a1.isdigit() and xo1.isdigit() and m1.isdigit():
                    if ((((int(a1)-3) / 8)-int((int(a1)-3) / 8))==0) or ((((int(a1)+3) / 8)-int((int(a1)+3) / 8))==0) and (int(m1) in mm) and (((int(xo1) % 2)!=0) and ((int(xo1) % 3)!=0) and ((int(xo1) % 5)!=0)):
                        nn=int(n)*50
                        MetCMult(a1, xo1, m1, nn, RN)
                        z=1
                    else:
                        print("Ingrese los valores adecuados.Multiplicador adecuado y semilla mayor a 0, no divisible entre 3 y 5.")
                        print("Modulo potencia de 2")
                else:
                    print("Ingrese solo numeros")
        else:
            print("Seleccione una opcion valida")
        return n
#Fin de procedimientos de numeros aleatorios
def simul():
    RN=[]
    n=int(escojermet(RN))#ingrese le numero de intervalos
    paqt=RN#Conjunto con los numeros aleatorios
    i=0
    ig=0
    nn=0
    nnn=0
    acumT=[0]
    destC=[0 for u in range(10)] #lista de los contadores de las ciudades
    bolT=[0, 0] #contador de la cantidad de boletos vendidos [0] primera/ [1] turista
    acumN(paqt, n, nn, nnn)
    while i < n:
        paq15(paqt[i], destC, bolT, acumT,paqt, n, nn, nnn, ig)#Primer ciclo iterativo donde se determinan los paquetes
        i+=1
    C=0
    i=0
    j=0
    while i<10:
        if destC[i]>C:#Variable de la ciudad mas visitada
            C=destC[i]
            j=i
        i+=1
    destCN=["Tibet", "Madrid"," Venecia", "Aruba", "Miami", "Acapulco", "París"," Río de Janeiro", "Buenos Aires", "Londres"]
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
    #print(paqt)
def paq15(paq, destC, bolT, acumT, paqt, n, nn, nnn, ig):
    z=0
    #cantidad de paquetes por dia
    if paq>0  and paq<=0.060:
        z=0#Buenas tardes nadie compro nada 
    elif paq>=0.060 and paq<0.150:#1
        z=1
        itpersn(z, destC, bolT, acumT, paqt, n, nn, nnn, ig)
    elif paq>=0.150 and paq<0.260:#2
        itpersn(2, destC, bolT, acumT, paqt, n, nn, nnn, ig)
    elif paq>=0.260 and paq<0.400:#3
        itpersn(3, destC, bolT, acumT, paqt, n ,nn, nnn, ig)
    elif paq>=0.400 and paq<0.580:#4
        itpersn(4, destC, bolT, acumT, paqt, n, nn, nnn, ig)
    elif paq>=0.580 and paq<0.810:#5
        itpersn(5, destC, bolT, acumT, paqt, n, nn, nnn, ig)
    elif paq>=0.810 and paq<0.950:#6
        itpersn(6, destC, bolT, acumT, paqt, n, nn, nnn, ig)
    else:#7
        itpersn(7, destC, bolT, acumT, paqt, n, nn, nnn, ig)  

def acumN(paqt, n, nn, nnn):#Evaluacion de las variables con sus respectivas ciudades
    i=0
    z=0
    while i<n:
        if paqt[i]>=0  and paqt[i]<0.060:
            z=0#Buenas tardes nadie compro nada 
        elif paqt[i]>=0.060 and paqt[i]<0.150:#1
            nn+=1
        elif paqt[i]>=0.150 and paqt[i]<0.260:#2
            nn+=2
        elif paqt[i]>=0.260 and paqt[i]<0.400:#3
            nn+=3
        elif paqt[i]>=0.400 and paqt[i]<0.580:#4
            nn+=4
        elif paqt[i]>=0.580 and paqt[i]<0.810:#5
            nn+=5
        elif paqt[i]>=0.810 and paqt[i]<0.950:#6
            nn+=6
        else:#7
            nn+=7
        i+=1
    
    jj=0
    nnn=0
    while jj<nn:
        if paqt[n+nn+jj]>=0 and paqt[n+nn+jj]<0.250:#cantidad de personas 1
            nnn+=1
        elif paqt[n+nn+jj]>=0.250 and paqt[n+nn+jj]<0.730:#2
            nnn+=2    
        elif paqt[n+nn+jj]>=0.730 and paqt[n+nn+jj]<0.880:#3
            nnn+=3
        elif paqt[n+nn+jj]>=0.880 and paqt[n+nn+jj]<0.960:#4
            nnn+=4
        else:#5"""
            nnn+=5
        jj+=1
    
def itpersn(i, destC, bolT, acumT, paqt, n, nn, nnn, ig):
    j=0
    while j<i:
        a=0
        w=0
        if paqt[n+nn+j]>=0 and paqt[n+nn+j]<0.250:#cantidad de personas 1
            destinos(paqt[n+nn+j],paqt[n+nn+nnn+ig],destC, bolT, acumT)
            ig+=1
        elif paqt[n+nn+j]>=0.250 and paqt[n+nn+j]<0.730:#2
            a=2
            while w<a :
                destinos(paqt[n+nn+j],paqt[n+nn+nnn+ig+w],destC, bolT, acumT)
                w+=1
            ig+=w    
            
        elif paqt[n+nn+j]>=0.730 and paqt[n+nn+j]<0.880:#3
            a=3
            while w<a:
                destinos(paqt[n+nn+j],paqt[n+nn+nnn+ig+w],destC, bolT, acumT)
                w+=1
            ig+=w 
        elif paqt[n+nn+j]>=0.880 and paqt[n+nn+j]<0.960:#4
            a=4
            while w<a:
                destinos(paqt[n+nn+j],paqt[n+nn+nnn+ig+w],destC, bolT, acumT)
                w+=1
            ig+=w 
        else:#5"""
            a=5
            while w<a:
                destinos(paqt[n+nn+j],paqt[n+nn+nnn+ig+w],destC, bolT, acumT)
                w+=1
            ig+=w 
        j+=1
    
simul()
