"""Problem:Write Python code that asks a user for the day of the week in English and translates it to Spanish.  

English        Spanish

Sunday         Domingo

Monday         Lunes

Tuesday        Martes

Wednesday      Miercoles

Thursday       Jueves

Friday         Viernes

Saturday       Sabado

If the user enters a word other than the ones above, print "Invalido"."""

days=str(input("Enter the Day of the week and I will translate it into spanish:")).lower()
if days=="sunday":
    print("Domingo")
elif days=="monday":
    print("Lunes")
elif days=="tuesday":
    print("Martes")
elif days=="wednesday":
    print("Miercoles")
elif days=="thursday":
    print("Jueves")
elif days=="friday":
    print("Viernes")
elif days=="saturday":
    print("Sabado")
else:
    print("Invalido")

