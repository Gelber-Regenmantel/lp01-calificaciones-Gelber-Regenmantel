from collections import namedtuple
from calificaciones import *
def solicita_notas():
    Notas = namedtuple('notas' , ['nombre', 'notas_teoricas', 'notas_practicas'])
    a = input("Introduzca su nombre: ")
    b = input("Introduzca la nota del examen teórico 1 (- si no se ha presentado): \n")
    c = input("Introduzca la nota del examen teórico 2 (- si no se ha presentado): \n")
    d = input("Introduzca la nota del examen teórico 3 (- si no se ha presentado): \n")
    e = input("Introduzca la nota del examen teórico 4 (- si no se ha presentado): \n")
    f = input("Introduzca la nota del examen práctico 1 (- si no se ha presentado): \n")
    g = input("Introduzca la nota del examen práctico 2 (- si no se ha presentado): \n")
    if b == "-":
        b = None
    if c == "-":
        c = None
    if d == "-":
        d = None
    if e == "-":
        e = None
    if f == "-":
        f = None
    if g == "-":
        g = None
    notas = Notas(a, (b,c,d,e), (f,g))
    return notas
def mostrar_notas():
    notas = solicita_notas()
    usuario = notas.nombre
    notasteorico = notas.notas_teoricas
    notaspracticas = notas.notas_practicas
    print(f"Hola, {usuario} \nTus notas del primer cuatrimentre son: \n teoria {nota_teoria(notasteorico[0],notasteorico[1])}, \
    práctica {notaspracticas[0]}, cuatrimentre {nota_cuatrimestre((notasteorico[0],notasteorico[1]),notaspracticas[0])}\nTus \
    notas del segundo cuatrimentre son: \n teoria {nota_teoria(notasteorico[2],notasteorico[3])}, práctica {notaspracticas[1]}, \
    cuatrimentre {nota_cuatrimestre((notasteorico[2],notasteorico[3]),notaspracticas[1])}\nTu nota final de la asignatura \
    es {nota_continua(notasteorico,notaspracticas)}")    

mostrar_notas()
