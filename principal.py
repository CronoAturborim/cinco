import sqlite3
import time

def add_one(number):
    return number + 1
class Ejemplo():
    def __init__(self):
        self.ejemplo = sqlite3.connect("notass.db")
        cursor = self.ejemplo.cursor()
        #Acá se supera el error de crear la tabla y generarel mensaje la tabla ya existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS DATOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,apellido TEXT , nombre TEXT, codigo TEXT, primer VARCHAR,  segundo VARCHAR, tercer VARCHAR, cuarto VARCHAR, asistencia VARCHAR, quiz VARCHAR ,fecha TEXT)''') 
        cursor.close()
        print('tabla de datos creada con éxito')

    def menu(self):
        try:
            self.a=int(input('''
            ingrese una de las opciones:
            1:Agregar un dato a la base de datos
            2:Ver los datos guardados
            3:Buscar datos de la base de datos
            4:Borrar datos de la base de datos
            5:actualizar
            6:salir\n'''))
            a=self.a
        except:
            print('el valor ingresado debe ser númerico')
        if a==1:
            self.agrega()
        elif a==2:
            self.ver()
        elif a==3:
            self.buscar()
        elif a==4:
            self.borrar()
        elif a==6:
            exit()
        elif a==5:
            self.actualizar()
        else:
            print('la opción no se encuentra en menu dado, intente de nuevo')
            print()
            print()
            self.menu()
    
    def agrega(self):
        self.ejempl = sqlite3.connect("notass.db")
        cursor = self.ejempl.cursor()
        apellido= input("Apellido del estudiante: ")
        nombre= input("Nombre del estudiante: ")
        codigo= input("Código del estudiante: ")
        primer= eval(input("ingrese la nota y multipliquela por el porcentaje correpondiente: "))
        segundo= eval(input("ingrese la nota y multipliquela por el porcentaje correpondiente: "))
        tercero= eval(input("ingrese la nota y multipliquela por el porcentaje correspondiente: "))
        cuarto= eval(input("ingrese la nota y multipliquela por el porsentaje correspondiente: "))
        asistencia = eval(input("ingrese la nota y multipliquela por el porsentaje correspondiente: "))
        quiz = eval(input("ingrese la nota y multipliquela por el porsentaje correspondiente: "))
        fecha= time.strftime("%d/%m/%y")
        lista=[(apellido, nombre,codigo,primer,segundo,tercero,cuarto,asistencia,quiz,fecha)]
        cursor.executemany("INSERT INTO DATOS  values (NULL,?,?,?,?,?,?,?,?,?,?)",lista)
        self.ejempl.commit()
        print ("Los datos fueron agregados con éxito")
        cursor.close()
        time.sleep(2)
        print()
       
        self.menu()
    def ver(self):
        self.ejempl=sqlite3.connect("notass.db")
        cursor=self.ejempl.cursor()
        cursor.execute("SELECT * FROM DATOS")
        #fetchall este método devuelve los datos guardados en cursor.
        datos=cursor.fetchall()
        self.ejempl.commit()
        cursor.close()
        time.sleep(2)
        print(datos)
        self.menu()
    def buscar(self):
        try:
            self.a=int(input('''
            ingrese una de las opciones:
            1:buscar por nombre
            2:buscar por apellido
            3:buscar por codigo
            4:salir\n'''))
            a=self.a
        except:
            print('el valor ingresado debe ser númerico')
        if a==1:
            self.nom()
        elif a==2:
            self.app()
        elif a==3:
            self.cod()
        
        else:
            print('la opción no se encuentra en menu dado, intente de nuevo')
            print()
            print()
            
    
        
        
    def nom(self):   
        self.g=input("ingrese el nombre a buscar")
        vio=[]
        vio.append(self.g)
        self.ejempl=sqlite3.connect("notass.db")
        cursor=self.ejemplo.cursor()        
        cursor.execute("SELECT * FROM DATOS WHERE nombre=(?)",vio)
        datos=cursor.fetchall()
        self.ejempl.commit()
        cursor.close()
        time.sleep(2)
        print(datos)

    def app(self):
        self.g=input("ingrese el apellido a buscar")
        vio=[]
        vio.append(self.g)
        self.ejempl=sqlite3.connect("notass.db")
        cursor=self.ejemplo.cursor()
    
        
        cursor.execute("SELECT * FROM DATOS WHERE apellido=(?)",vio)
        datos=cursor.fetchall()
        self.ejempl.commit()
        cursor.close()
        time.sleep(2)
        print(datos)
        self.menu()
    
    def cod(self):
        self.g=input("ingrese el codigo a buscar")
        vio=[]
        vio.append(self.g)
        self.ejempl=sqlite3.connect("notass.db")
        cursor=self.ejemplo.cursor()
    
        cursor.execute("SELECT * FROM DATOS WHERE codigo=(?)",vio)
        datos=cursor.fetchall()
        self.ejempl.commit()
        cursor.close()
        time.sleep(2)
        print(datos)
        self.menu()

    def borrar(self):
        self.ri=input("ingrese el codigo del estudiante a eliminar")
        ca=[]
        ca.append(self.ri)
        self.ejempl=sqlite3.connect("notass.db")
        cursor=self.ejempl.cursor()
        cursor.execute("DELETE FROM DATOS WHERE codigo=(?)",ca)
        datos=cursor.fetchall()
        self.ejempl.commit()
        cursor.close()
        time.sleep(2)
        print(datos)
        print("base de datos actualizada")
        
        self.menu()
    
    def actualizar(self):
        alf = int(input('''¿Qué dato desea cambiar?
                    1. Nombre
                    2. Apellido
                    3. Código
                    4. Primer corte
                    5. Segundo corte
                    6. Tercer corte
                    7. Cuarto corte
                    8. Asistencia
                    9. Quiz\n'''))
    
        if alf in range(1, 10):
            nombre_actual = input("Ingrese el codigo del estudiante a actualizar: ")
            nuevo_dato = input("Ingrese el nuevo dato: ")

            self.ejemplo = sqlite3.connect("notass.db")
            cursor = self.ejemplo.cursor()

        if alf == 1:
            query = "UPDATE DATOS SET nombre = ? WHERE codigo = ?"
        elif alf == 2:
            query = "UPDATE DATOS SET apellido = ? WHERE codigo = ?"
        elif alf == 3:
            query = "UPDATE DATOS SET codigo = ? WHERE codigo = ?"
        elif alf == 4:
            query = "UPDATE DATOS SET primer = ? WHERE codigo = ?"
        elif alf == 5:
            query = "UPDATE DATOS SET segundo = ? WHERE codigo = ?"
        elif alf == 6:
            query = "UPDATE DATOS SET tercer = ? WHERE codigo = ?"
        elif alf == 7:
            query = "UPDATE DATOS SET cuarto = ? WHERE codigo = ?"
        elif alf == 8:
            query = "UPDATE DATOS SET asistencia = ? WHERE codigo = ?"
        elif alf == 9:
            query = "UPDATE DATOS SET quiz = ? WHERE codigo = ?"

        cursor.execute(query, (nuevo_dato, nombre_actual))
        self.ejemplo.commit()
        cursor.close()
        print("Dato actualizado correctamente.")
        self.menu()




z=Ejemplo()
z.menu()