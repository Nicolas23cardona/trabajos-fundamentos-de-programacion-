# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# documentacion 
	# nombres de los estudiantes del grupo: nicolas cardona duque, johansebastian giraldo trujillo, andresjulian vallejo arango 
	# fecha:21/03/2023
	# version:1.0
	# enunciado: crear un programa que pida por teclado el tamaño de un tornillo y muestre por pantalla el texto correspondiente al tamaño, segun la siguente tabla ç
	# declaracion de variables
	tornillo = float()
	# captura de datos
	print "intorduce el tamaño del tornillo en cm: "
	tornillo = float(raw_input())
	# procesos 
	if tornillo>=1 and tornillo<3:
		print "el tamaño del tornillo es pequeño"
	if tornillo>=3 and tornillo<5:
		print "el tamaño del tornillo es mediano"
	if tornillo>=5 and tornillo<6.5:
		print "el tamaño del tornillo es grande"
		if tornillo>=6.5 and tornillo<8.8:
			print "el tamaño del tornillo es muy grande"

