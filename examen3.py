class Persona:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.carnet = []
        self.celular = []
        self.estado = []

class administrativo(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.cargo = []
        self.area = []

    def registrarAdmi(self):
        print("*******REGISTRO DE PERSONAL ADMINISTRATIVO*******")
        nombre1 = input("Nombre: ")
        apellido1 = input("Apellido: ")
        carnet1 = input("Carnet: ")
        celular1 = input("Celular: ")
        estado1 = int(input("Estado (1): "))
        cargo1 = input("Cargo: ")
        area1 = input("Area: ")
        
        print(self.guardarAdministrativo(nombre1, apellido1, carnet1, celular1, estado1, cargo1, area1))
        agregarOtro=input("Desea agregar mas registros? s/n \n")
        if agregarOtro == 's' or agregarOtro =='S':
            self.registrarAdmi()
        return 'Administrativos registrados correctamente.!'

    def guardarAdministrativo(self, nombre, apellido, carnet, celular, estado, cargo, area):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(estado)
        self.cargo.append(cargo)
        self.area.append(area)
        return 'El Administrativo {} fue registrado exitosamente..!!'.format(self.nombre)
    
    def mostrarAdmi(self, posicion):
        print("Nombre: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("Carnet: {}".format(self.carnet[posicion]))
        print("Celular: {}".format(self.celular[posicion]))
        print("Estado: {}".format(self.estado[posicion]))
        print("Cargo: {}".format(self.cargo[posicion]))
        print("Area: {}".format(self.area[posicion]))
        pass

    def listarA(self, estado):
        if self.cargo:
            print("***************ADMINISTRATIVOS REGISTRADOS**************")
            for posicion in range(len(self.cargo)):
                self.mostrarAdmi(posicion)
                print("******************************************")
        else:
            return print("No hay Usuarios Registrados en el Sistema..!!")

    def listarAdmin(self):
        estado = 1
        self.listarA(estado)

class docente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.materia = []
        self.carrera = []
    
    def registrarDocente(self):
        print("*******REGISTRO DE DOCENTE*******")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        carnet = input("Carnet: ")
        celular = input("Celular: ")
        estado = int(input("Estado (1): "))
        materia = input("Materia: ")
        carrera = input("Carrera: ")

        print(self.guardarDocent(nombre, apellido, carnet, celular, estado, materia, carrera))
        agregarOtro=input("Desea agregar mas registros? s/n \n")
        if agregarOtro == 's' or agregarOtro =='S':
            self.registrarDocente()
        return 'Docentes registrados correctamente.!'
    
    def guardarDocent(self, nombre, apellido, carnet, celular, estado, materia, carrera):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.carnet.append(carnet)
        self.celular.append(celular)
        self.estado.append(estado)
        self.materia.append(materia)
        self.carrera.append(carrera)
        return 'El Docente {} fue registrado exitosamente..!!'.format(self.nombre)
    
    def mostrarDocente(self, posicion):
        print("Nombre: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("Carnet: {}".format(self.carnet[posicion]))
        print("Celular: {}".format(self.celular[posicion]))
        print("Estado: {}".format(self.estado[posicion]))
        print("Materia: {}".format(self.materia[posicion]))
        print("Carrera: {}".format(self.carrera[posicion]))
        pass

    def listarDo(self, estado):
        if self.carrera:
            print("*****************DOCENTES REGISTRADOS***************")
            for posicion in range(len(self.carrera)):
                self.mostrarDocente(posicion)
                print("*************************************")
        else:
            return print("No hay Usuarios Registrados en el Sistema..!!")

    def listarDocente(self):
        estado = 1
        self.listarDo(estado)

class Colegio(administrativo, docente):
    def __init__(self):
        administrativo.__init__(self)
        docente.__init__(self)
    
    def menu(self):
        print("""
        ****************** MENU ****************
        1.- REGISTRAR ADMINISTRATIVO
        2.- REGISTRAR DOCENTE
        3.- MOSTRAR REGISTRO DE ADMINISTRATIVO
        4.- MOSTRAR REGISTRO DE DOCENTE
        5.- MOSTRAR TODOS LOS REGISTROS
        6.- SALIR
        """)
        opcion = int(input("Elija una opcion del Menu: \n"))

        if opcion == 1:
            self.RegisAdmin()
            self.volverMenu()
        elif opcion == 2:
            self.RegisDocente()
            self.volverMenu()
        elif opcion == 3:
            self.mostrarAdmin1()
            self.volverMenu()
        elif opcion == 4:
            self.mostrarDocente1()
            self.volverMenu()
        elif opcion == 5:
            self.mostrarTodoRegis()
            self.volverMenu()
        elif opcion == 6:
            print("SE REALIZO LOS REGISTROS CORRECTAMENTE...!!)")
        else:
            print("Elija una opcion correcta del Menu..!!")

    def volverMenu(self):
        opcion = input("Desea volver al MENU? S/N: ")
        if opcion == "S" or opcion == "s":
            self.menu()
        elif opcion == "N" or opcion == "n":
            print("GRACIAS POR UTILIZAR NUESTRO SERVICIO... :)")
        else:
            print("Elija una opcion correcta S/N..!!")
            self.volverMenu()

    def RegisAdmin(self):
        self.registrarAdmi()
    
    def RegisDocente(self):
        self.registrarDocente()

    def mostrarAdmin1(self):
        self.listarAdmin()
    
    def mostrarDocente1(self):
        self.listarDocente()

    def mostrarTodoRegis(self):
        print("************REGISTRO DE ADMINISTRATIVOS Y DOCENTES**************")
        self.listarAdmin()
        print("*************************************")
        self.listarDocente()
        print("*************************************")


colegio = Colegio()
colegio.guardarAdministrativo('JOSE', 'MERCADO', '7723652', '76354210',1, 'ADMINISTRADOR GENERAL', 'ADMINISTRACION')
colegio.guardarAdministrativo('ANTONIO', 'MELGAR', '11223652', '69354210',1, 'EJECUTIVO DE VENTAS', 'MARKETING')
colegio.guardarAdministrativo('JUAN', 'MERCADO', '6323652', '69054210',1, 'EJECUTIVO DE VENTAS', 'MARKETING')
colegio.guardarDocent('MARCO','MERCADO', '11023652', '77254210',1, 'MICROECONOMIA', 'ADMINISTRACION DE EMPRESAS')
colegio.guardarDocent('MARIO','PEREZ', '11123652', '69054278',1, 'MACROECONOMIA', 'INGENIERA COMERCIAL')
colegio.menu()

