import os
import re
import string
import random
string.ascii_letters

# ---------------------------------- VALIDACIONES -------------------------------------------

def telefonoCorrecto(num):
    if len(num) == 8:
        return True
    else:
        return False

def is_num(num):
    reg = "[-+]?\d+$"
    return re.match(reg, num) is not None

# ---------------------------------- LISTA DOBLE ---------------------------------------------

class contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

class nodo_listaDoble:
    def __init__(self, contacto=None, siguiente=None, anterior=None):
        self.contacto = contacto
        self.siguiente = siguiente
        self.anterior = anterior

class lista_doblemente:
    def __init__(self, cabeza=None):
        self.cabeza = cabeza
        self.ultimo = cabeza
        self.size = 0

    def insertar_contacto(self, contacto):
        if self.size == 0:
            self.cabeza = nodo_listaDoble(contacto=contacto)
            self.ultimo = self.cabeza
        else:
            nuevo_nodo = nodo_listaDoble(contacto=contacto, siguiente=self.cabeza)
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.size += 1
 
    
    def imprimir(self):
        if self.cabeza is None:
            return
        nodo = self.cabeza
        print(nodo.contacto.nombre, end = " -> ")
        while nodo.siguiente:
            nodo = nodo.siguiente
            print(nodo.contacto.nombre, end = " -> ")
        print()
    
    def buscar(self, val):
        if self.cabeza is None:
            print('>>ERROR: No hay contactos...')
            print()
        nodo = self.cabeza
        while nodo:
            if nodo.contacto.telefono == val:
                print('     Nombre: ' + nodo.contacto.nombre)
                print('     Apellido: ' + nodo.contacto.apellido)
                print('     No. Telefonico: ' + nodo.contacto.telefono)
            else:
                agg = input('El Numero de telefono no existe ¿Desea Agregarlo? [S/N]: ')
                if agg == 'S' or agg =='s':
                    opcion1()
            nodo = nodo.siguiente
        print()

    def existe(self, val):
        nodo = self.cabeza
        while nodo:
            if nodo.contacto.telefono == val:
                return ('existe')             
            nodo = nodo.siguiente
        print()    


    def ordenar(self):
        if self.cabeza == None:
            print('No hay nada')
        else:
            p = self.cabeza
            while p.siguiente != None:
                q = p.siguiente
                while q != None:
                    if q.contacto < p.contacto:
                        aux = p.contacto
                        p.contacto = q.contacto
                        q.contacto = aux
                    q = q.siguiente
                p = p.siguiente

# ---------------------------------- GRAPHIZ -------------------------------------------------

terminar = True
listD = lista_doblemente()

nodosGrafic=[]

def nodoGraf(nombre,apellido,numero):
    return "[label=\"" + "Nombre: " + nombre + "\n  Apellido: " +  apellido + "\n  Numero:"+ numero + "\" , shape=box,style=filled, fillcolor =skyblue]\n"

def crearGraphis():
    file = open("graphiz1.dot", "w")
    file.write("digraph Tarea1{\n")
    file.write("edge[dir="'both'"]\n")

    file.write("AgendaM[label="'Agenda'" , shape=box,style=filled, fillcolor =skyblue]\n")
    k = []
    for aa in nodosGrafic:
        le = random.choice(string.ascii_letters)
        file.write( le +str(aa))
        k.append(le)



    file.write("AgendaM->") 
    contador= 0
    for m in k:
        if contador != len(k)-1:
            file.write(str(m) + "->")
        else:
            file.write(str(m))
        contador += 1


    file.write("\n")
    
    
        
       
    file.write("}")
    file.close()
    os.system("dot -Tpng graphiz1.dot -o graphiz1.png")
    os.startfile("graphiz1.png")



# ---------------------------------- VALIDAR NUMERO ------------------------------------------

def tele(): # Telefono para agregar -----------------------------------
    telefono = input('-> Ingrese numero: ')
    if is_num(telefono):
        if telefonoCorrecto(telefono):
            return telefono
        else:
            print('\n>>ERROR: Ingrese numero de 8 digitos\n')
            tele()
    else:
        print('\n>>ERROR: Ingrese solo digitos')
        print()
        tele()
        
def tele2(): # Telefono para buscar -------------------------------
    telefono = input('-> Ingrese numero: ')
    if is_num(telefono):
        if telefonoCorrecto(telefono):
            return telefono
        else:
            print('\n>>ERROR: Ingrese numero de 8 digitos\n')
            tele()
    else:
        print('\n>>ERROR: Ingrese solo digitos')
        print()
        tele()    

def opcion1(): # Opcion de Agregar -------------------------------
    nombre = input('-> Ingrese nombre: ')
    apellido = input('-> Ingrese apellido: ' )
    tel = tele()

    print()

    contact = contacto(nombre, apellido, tel)
    listD.insertar_contacto(contact)
    listD.imprimir()
    
    j = nodoGraf(nombre, apellido, str(tel))
    nodosGrafic.append(j)
    
# ---------------------------------- MENU ----------------------------------------------------

def opciones():
    print('''\n ------------- MENU --------------
    1. Ingresar nuevo contacto
    2. Buscar contacto
    3. Visualizar contactos
    4. Salir
    ''')
    res = input('>>>> Ingrese opcion: ')
    print()
    return res

while(terminar):    
    opc = opciones()
    if opc == '1': # Agregar 
        opcion1()
        
    elif opc == '2': # Buscar
        num = tele2()
        print()
        listD.buscar(num)

    elif opc == '3': # Imprimir
        listD.imprimir()
        crearGraphis()

    elif opc == '4': # Cerra
        terminar = False
    else:
        print('**Ingrese una opcion valida**')



