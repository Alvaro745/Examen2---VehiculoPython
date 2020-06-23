from datetime import datetime, date, timedelta
class Permiso:
    def __init__(self):
        self.codigo = []
        self.conductor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.fecha_solicitud = []
        self.motivo = []
        self.habilitado = []
    
    def menu(self):
        opciones = """
        1.- MOSTRAR EL MENU PARA VER TODOS LOS PERMISOS SOLICITADOS
        2.- HABILITAR LOS PERMISOS PARA LAS SOLICITUDES QUE HAYAN SIDO REALIZADAS HASTA EL 31/05/2020
        3.- MOSTRAR LOS PERMISOS HABILITADOS
        4.- MOSTRAR LOS PERMISOS NO HABILITADOS
        5.- Salir
        """

        print(opciones)
        seleccionar= int(input("Seleccione una opcion: \n"))
        if (seleccionar == 1):
            print(self.mostrarTodo())
            print(self.volverMenu())
        elif (seleccionar == 2):
            print(self.habilitarPermiso())
            print(self.volverMenu())
        elif (seleccionar == 3):
            print(self.verVehiculoAlta())
            print(self.volverMenu())
        elif (seleccionar == 4):
            print(self.verVehiculoBaja())
            print(self.volverMenu())
        elif (seleccionar == 5):
            print("Registros realizados exitosamente")
        else:
            print("Seleccione una opcion del menu")
            self.menu()
    
    def volverMenu(self):
        eleccion = input("Desea volver al menu: y/n \n")
        if (eleccion == 'y' or eleccion == 'Y'):
            self.menu()
        return "-------Transacciones Terminadas-----------"

    def mostrarTodo(self):
        self.verVehiculoAlta()
        self.verVehiculoBaja()
        pass

    def guardarPermisos(self, cod, conduc, model, marca, placa, ciudad, fechaSoli, motivo, habilitado):
        self.codigo.append(cod)
        self.conductor.append(conduc)
        self.modelo.append(model)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.fecha_solicitud.append(fechaSoli)
        self.motivo.append(motivo)
        self.habilitado.append(habilitado)
        return "El permiso de la persona {} fue guardado correctamente..!!".format(conduc)
    
    def descripcionPermisos(self, posicion, habilitado):
        if (self.habilitado[posicion] == habilitado):
            print("*****DESCRIPCION DEL PERMISO DE LA PERSONA {}*****".format(self.conductor[posicion]))
            print("CODIGO DEL PERMISO: {}".format(self.codigo[posicion]))
            print("MODELO DEL VEHICULO: {}".format(self.modelo[posicion]))
            print("MARCA DEL VEHICULO: {}".format(self.marca[posicion]))
            print("PLACA DE VEHICULO: {}".format(self.placa[posicion]))
            print("CIUDAD: {}".format(self.ciudad[posicion]))
            print("FECHA DE SOLICITUD: {}".format(self.fecha_solicitud[posicion]))
            print("MOTIVO: {}".format(self.motivo[posicion]))
            print("HABILITADO: {}".format(self.habilitado[posicion]))
            print("**********************************************")
            pass

    def verVehiculoAlta(self):
        return self.baseDatosVehiculo(1)
    
    def verVehiculoBaja(self):
        return self.baseDatosVehiculo(0)
    
    def baseDatosVehiculo(self, habilitado):
        if(self.conductor):
            for i in range(len(self.conductor)):
                self.descripcionPermisos(i, habilitado)
            return "Base datos Cargados Correctamente"
        else:
            return "NO HAY SOLICITUDES AGREGADAS EN LA BASE DE DATOS..!!"

    def buscarPermisos(self, habilitado):
        print(self.baseDatosVehiculo(habilitado))
        eleccion = input("Digite la fecha del Permiso a Habilitar: \n")
        posicion = self.fecha_solicitud.index(eleccion)
        self.baseDatosVehiculo(posicion)
        return posicion

    def habilitarPermiso(self):
        print("*****************HABILITAR PERMISOS***************")
        posicion = self.buscarPermisos(0)
        return self.habilitarPermi(posicion)

    def habilitarPermi(self, posicion):
        self.habilitado[posicion] = 1
        return "El Permiso de la persona {} fue habilitado..!!".format(self.conductor[posicion])

permisos = Permiso()
permisos.guardarPermisos(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardarPermisos(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '22/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.menu()