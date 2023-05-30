# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# documentacion 
	# nombres de los estudiantes del grupo: nicolas cardona duque, johansebastian giraldo trujillo, andresjulian vallejo arango 
	# fecha:21/03/2023
	# version:1.0
	# enunciado: programa que tenga todas las formulas de m.u.a y las aplique 
	# declaracion de variables 
	r = float()
	velocidad_media = float()
	velociad_instantanea = float()
	aceleracion_media = float()
	aceleracion = float()
	opc = int()
	velocidad_final = float()
	velocidad_inicial = float()
	distancia = int()
	tiempo = int()
	tiempo_final = int()
	tiempo_inicial = int()
	operacion = str()
	distancia_aceleracion = float()
	# inicializacion de variables 
	r = 0.0
	velocidad_media = 0.0
	velociad_instantanea = 0.0
	eceleracion_media = 0.0
	aceleracion = 0.0
	opc = 0
	velocidad_final = 0.0
	velociad_inicial = 0.0
	distancia = 0
	tiempo = 0
	tiempo_final = 0
	tiempo_inicial = 0
	operacion = ""
	distancia_aceleracion = 0.0
	# captura de datos 
	print "**************************************************"
	print "**        bienvenido ingrese su opcion          **"
	print "**1:calcular velocidad media, 2: calcular velocidad instantanea, 3: calcular aceleracion media, 4: aceleracion, 5 velocidad final, 6 distancia, 7 dintancia con aceleracion**"
	print "***************************************************************************************************************"
	opc = int(raw_input())
	print "" # no hay forma directa de borrar la pantalla con Python estandar
	# procesos
	if (opc==1):
		print "ingrese su velocidad final"
		velocidad_final = float(raw_input())
		print "ingrese su veloccidad inicial"
		velocidad_inicial = float(raw_input())
		velocidad_media = velocidad_final+velocidad_inicial/2
		print "su velocidad media es: ",velocidad_media
		operacion = "velocidad media"
	if (opc==2):
		print "ingrese su distancia"
		distancia = int(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		velociad_instantanea = distancia/tiempo
		print "su velocidad instantanea es: ",velociad_instantanea
		operacion = "velocidad instantanea"
	if (opc==3):
		print "ingrese su velocidad final"
		velocidad_final = float(raw_input())
		print "ingrese su velocidad inicial"
		velocidad_inicial = float(raw_input())
		print "ingrese su tiempo final"
		tiempo_final = int(raw_input())
		print "ingrese su tiempo inicial"
		tiempo_inicial = int(raw_input())
		aceleracion_media = (velocidad_final-velociad_inicial)/(tiempo_final-tiempo_inicial)
		print "la aceleracion media es: ",aceleracion_media
		operacion = "aceleracion media"
	if (opc==4):
		print "ingrese su velocidad final"
		velocidad_final = float(raw_input())
		print "ingrese velocidad inicial"
		velocidad_inicial = float(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		aceleracion = velocidad_final-velociad_inicial/tiempo
		print "su aceleracion es: ",aceleracion
		operacion = "aceleracion"
	if (opc==5):
		print "ingrese su aceleracion"
		aceleracion = float(raw_input())
		print "ingrese su distancia"
		distancia = int(raw_input())
		velocidad_final = 2+2*(aceleracion*distancia)
		print "su velocidad final es: ",velocidad_final
		operacion = "velocidad final"
	if (opc==6):
		print "ingrese su velocidad final"
		velocidad_final = float(raw_input())
		print "ingrese su velocidade inicial"
		velociad_inicial = float(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		distancia = (velocidad_final+velociad_inicial/2)*tiempo
		print "su distanci es: ",distancia
		operacion = "distancia"
	if (opc==7):
		print "ingrese su velociad_inicial"
		velocidad_inicial = float(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		print "ingrese su aceleracion"
		aceleracion = float(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		print "ingrese su tiempo"
		tiempo = int(raw_input())
		distancia_aceleracion = (velociad_inicial*tiempo)+(1/2)*aceleracion*(tiempo*tiempo)
		print "su distancia con respecto a la acelreacion es: ",distancia_aceleracion
		operacion = "distancia_aceleracion"
	# salida 

