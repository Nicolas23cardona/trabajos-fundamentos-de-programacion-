Algoritmo ejercicio_1
	//documentacion 
	//nombres de los estudiantes del grupo: nicolas cardona duque, johansebastian giraldo trujillo, andresjulian vallejo arango 
	//fecha:21/03/2023
	//version:1.0
	//enunciado: crear un programa que pida por teclado el tama�o de un tornillo y muestre por pantalla el texto correspondiente al tama�o, segun la siguente tabla �

	//declaracion de variables
	definir tornillo Como real
	
	//captura de datos
	escribir "intorduce el tama�o del tornillo en cm: "
	leer tornillo 
	
	//procesos 
	Si tornillo >= 1 y tornillo < 3 entonces
		escribir "el tama�o del tornillo es peque�o"
	 fin si 
	Si tornillo >=3 y tornillo <5 Entonces
		escribir "el tama�o del tornillo es mediano"
		fin si 
	
	Si tornillo >=5 y tornillo <6.5 Entonces
		escribir "el tama�o del tornillo es grande"
		Si tornillo >= 6.5 y tornillo <8.8 Entonces 
			escribir "el tama�o del tornillo es muy grande"
		fin si 
		
	Fin Si
	
	
	
	
	
FinAlgoritmo
