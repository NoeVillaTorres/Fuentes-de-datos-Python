from tkinter import *


ventana = Tk()


ventana.title("Formulario de registro")

Label(ventana, text="Nombre").grid(row=0, column=0)
Entry(ventana).grid(row=0, column=1)

Label(ventana, text="Apellido Paterno").grid(row=1, column=0)
Entry(ventana).grid(row=1, column=1)

Label(ventana, text="Apellido Materno").grid(row=2, column=0)
Entry(ventana).grid(row=2, column=1)

Label(ventana, text="Correo").grid(row=3, column=0)
Entry(ventana).grid(row=3, column=1)

Label(ventana, text="Móvil").grid(row=4, column=0)
Entry(ventana).grid(row=4, column=1)


Label(ventana, text="Selecciona tu estado:").grid(row=5, column=0)
estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]
opcion_estado = StringVar()
opcion_estado.set(estados[0])
menu_estados = OptionMenu(ventana, opcion_estado, *estados)
menu_estados.grid(row=6, column=0)


Label(ventana, text="Selecciona tu ocupación:").grid(row=5, column=1)
ocupaciones = [("Estudiante"), ("Empleado"), ("Desempleado")]
opcion_ocupacion = StringVar()
opcion_ocupacion.set(ocupaciones[0])
for ocupacion in ocupaciones:
    Radiobutton(ventana, text=ocupacion, variable=opcion_ocupacion, value=ocupacion).grid(row=6, column=1)


Label(ventana, text="Aficiones:").grid(row=7, column=0)
aficiones = [("Leer"), ("Música"), ("Videojuegos")]
aficiones_seleccionadas = []
for aficion in aficiones:
    var = IntVar()
    Checkbutton(ventana, text=aficion, variable=var).grid(row=8, column=0, sticky=W)
    aficiones_seleccionadas.append(var)

Button(ventana, text="Guardar").grid(row=9, column=0)
Button(ventana, text="Cancelar").grid(row=9, column=1)

ventana.mainloop()