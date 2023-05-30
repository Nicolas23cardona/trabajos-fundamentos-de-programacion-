Algoritmo ejercicio_2
	//documentacion 
	//nombres de los estudiantes del grupo: nicolas cardona duque, johansebastian giraldo trujillo, andresjulian vallejo arango 
	//fecha:21/03/2023
	//version:1.0
	//enunciado: programa que tenga todas las formulas de m.u.a y las aplique 
	
	//declaracion de variables 
	
	definir r como real 
	definir velocidad_media Como Real
	definir velociad_instantanea Como Real
	definir aceleracion_media Como Real
	definir aceleracion como real 
	definir opc como entero 
	definir velocidad_final como real 
	definir velocidad_inicial como real 
	definir distancia como entero 
	definir tiempo como entero 
	definir tiempo_final como entero 
	definir tiempo_inicial como entero 
	definir operacion como caracter
	definir distancia_aceleracion como real
	
	//inicializacion de variables 
	r=0.0
	velocidad_media=0.0
	velociad_instantanea=0.0
	eceleracion_media=0.0
	aceleracion=0.0
	opc=0	
	velocidad_final=0.0
	velociad_inicial=0.0
	distancia=0	
	tiempo=0	
	tiempo_final=0
	tiempo_inicial=0
	operacion=""
	distancia_aceleracion=0.0
	//captura de datos 
	escribir"**************************************************"
	escribir"**        bienvenido ingrese su opcion          **"
	escribir"**1:calcular velocidad media, 2: calcular velocidad instantanea, 3: calcular aceleracion media, 4: aceleracion, 5 velocidad final, 6 distancia, 7 dintancia con aceleracion**"
    escribir "***************************************************************************************************************"
	leer opc 
	limpiar pantalla 
	
	//procesos
	si(opc==1) Entonces
		escribir "ingrese su velocidad final"
		leer velocidad_final 
		escribir "ingrese su veloccidad inicial"
		leer velocidad_inicial
		velocidad_media=velocidad_final+velocidad_inicial/2
		Escribir "su velocidad media es: ", velocidad_media
		operacion<-"velocidad media"
	FinSi
	Si (opc==2) Entonces
		escribir "ingrese su distancia"
		leer distancia
		escribir "ingrese su tiempo"
		leer tiempo
		velociad_instantanea=distancia/tiempo 
		escribir "su velocidad instantanea es: ", velociad_instantanea
		operacion<-"velocidad instantanea"
    fin si
	si (opc==3) Entonces
		escribir "ingrese su velocidad final"
		leer velocidad_final
		escribir "ingrese su velocidad inicial"
		leer velocidad_inicial
		escribir "ingrese su tiempo final"
		leer tiempo_final
		Escribir "ingrese su tiempo inicial"
		leer tiempo_inicial
		aceleracion_media=(velocidad_final-velociad_inicial)/(tiempo_final-tiempo_inicial)
		escribir "la aceleracion media es: ", aceleracion_media
	    operacion<-"aceleracion media"
	FinSi
	si(opc==4) Entonces
		escribir "ingrese su velocidad final"
		leer velocidad_final
		escribir "ingrese velocidad inicial"
		leer velocidad_inicial
		escribir "ingrese su tiempo"
		leer tiempo
		aceleracion=velocidad_final-velociad_inicial/tiempo
		Escribir "su aceleracion es: ", aceleracion
		operacion<-"aceleracion"
		
	FinSi
	si (opc==5) Entonces
		escribir "ingrese su aceleracion"
		leer aceleracion
		escribir "ingrese su distancia"
		leer distancia
		velocidad_final=2+2*(aceleracion*distancia)
		escribir "su velocidad final es: ", velocidad_final
		operacion<-"velocidad final"
	FinSi
	si (opc==6) Entonces
		escribir "ingrese su velocidad final"
		leer velocidad_final
		Escribir "ingrese su velocidade inicial"
		leer velociad_inicial
		escribir "ingrese su tiempo"
		leer tiempo
		distancia=(velocidad_final+velociad_inicial/2)*tiempo
		escribir "su distanci es: ", distancia
		operacion<- "distancia"
	FinSi
	si (opc==7) Entonces
		escribir "ingrese su velociad_inicial"
		leer velocidad_inicial
		escribir "ingrese su tiempo"
		leer tiempo
		escribir "ingrese su aceleracion"
		leer aceleracion
		escribir"ingrese su tiempo"
		leer tiempo
		Escribir "ingrese su tiempo"
		leer tiempo
		distancia_aceleracion=(velociad_inicial*tiempo)+(1/2)*aceleracion*(tiempo*tiempo)
		escribir "su distancia con respecto a la acelreacion es: ", distancia_aceleracion
		operacion="distancia_aceleracion"
	FinSi
	
	//salida 
FinAlgoritmo
