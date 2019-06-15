diccionario={'Nombres' : 'vacio', "Apellidos" : "vacio1" , "RUT" : "vacio2", "Sexo" : "vacio0", 'edad' : "vacio3", "Estado Civil" : "vacio4" , "Domicilio" : "vacio5", "Grupo Sanguíneo" : "vacio6" , "Fono" : "vacio7" , "Diagnositivos" : "none"}
acompañante={'Nombres' : '--', "Apellidos" : "-- " , "Rut" : "19191762-6" , 'edad' : 22, "Grado de Parentesco" : "---" }
medicamentos={"Medicamentos" : "none"}
hombre=0
mujer=0
reposo=0
import os


while True:

    os.system('cls') 
    print ("SERVICIO DE ATENCION MEDICA DE URGENCIA")
    print("-----------------------------------------------------------------")
    print ("\t1)Ingresar Ficha del Paciente")
    print ("\t2)Actualizar Ficha por el Medico")
    print ("\t3)Asignacion de Medicamentos")
    print ("\t4)Obtencion de Estadísticas")
    print ("\t5)Salir")

    opcionMenu = input("Elija una opción >> ")

 
  
    if opcionMenu=="1":
        diccionario["Nombres"]=(input("Ingrese su nombre: "))
        diccionario["Apellidos"]=(input("Ingrese su apellido: "))
        diccionario["RUT"]=(input("Ingrese su Rut: "))
        diccionario["edad"]=(input("Ingrese su edad: "))
        sexo=input("Sexo \n mujer\n hombre\nseleccione :")
        diccionario["Estado Civil"]=(input("Ingrese su estado civil: "))
        diccionario["Domicilio"]=(input("Ingrese su domicilio: "))
        diccionario["Grupo Sanguíneo"]=(input("Ingrese su grupo sanguineo: "))
        diccionario["Fono"]=(input("Ingrese su fono: "))
        diccionario["Diagnosticos"]=(input("Ingrese diagnosticos previos: "))
        medico=input("reposo \n si\n no\nseleccione :"  )
        for key in diccionario:
            print(key, ":", diccionario[key])
    elif opcionMenu=="2":
        for key in diccionario:
            print(key, ":", diccionario[key])
    elif opcionMenu=="3":
        Paracetamol = 0
        Lidocaina = 0
        Omeprazol = 0
        Penicilina = 0
        Salbutamol = 0
        medicamentos = int(input("Ingrese Cantidad de Medicamentos: "))
        for m in range(0,medicamentos):
            print("-----------------------------------------------------------------")
            print ("\t1)Paracetamol")
            print ("\t2)Lidocaína")
            print ("\t3)Omeprazol")
            print ("\t4)Penicilina")
            print ("\t5)Salbutamol")

            opcionMenu = input("Elija una opción >> ")

            if opcionMenu == "1":
                Paracetamol = int(input("Ingrese Cantidad de Paracetamol que desea: "))
            elif opcionMenu == "2":
                Lidocaina = int(input("Ingrese Cantidad de Lidocaína que desea: "))
            elif opcionMenu == "3":
                Omeprazol = int(input("Ingrese Cantidad de Omeprazol que desea: "))
            elif opcionMenu == "4":
                Penicilina= int(input("Ingrese Cantidad de Penicilina que desea: "))
            elif opcionMenu == "5":
                Salbutamol = int(input("Ingrese Cantidad de Salbutamol que desea: "))
    elif opcionMenu=="4" :
        if diccionario["Sexo"]==+1 :
            mujer=mujer+1
        if diccionario["Sexo"]==+1:
            hombre=hombre+1
        if medico=="si":
            reposo=reposo+1
        Total_med = Paracetamol + Lidocaina + Omeprazol + Penicilina + Salbutamol
        print("El total de medicamentos solicitados es: ",Total_med)
        print("Se solicitaron ", Paracetamol, "Paracetamol, ", Lidocaina, "Lidocaína", Omeprazol, "Omeprazol", Penicilina, "Penicilina, y", Salbutamol, "Salbutamol.")
        print("Total de mujeres atendidas:", mujer, "Total de hombres:", hombre , "Total de reposo: ", reposo,)
    elif opcionMenu=="5":
        print("Seción cerrada.")
        break