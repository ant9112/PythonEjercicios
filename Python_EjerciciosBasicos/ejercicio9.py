from datetime import datetime
fecha_nacimiento = (input("Ingrese tu fecha de nacimiento AAAA-MM-DD: "))
#fecha_nacimiento = "1988-05-24"
hoy = str(datetime.today().strftime('%Y-%m-%d'))
d1 = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
d2 = datetime.strptime(hoy, "%Y-%m-%d")
print("Fecha nacimiento: ", d1, " Hoy: ", d2)
print("Cantidad de meses: ", abs((d1.year - d2.year) * 12 + d1.month - d2.month))
