name = input("\ningrese su nombre\n")

apellido = input ("\ningrese su apellido\n")

segundo_nombre = str (input ('\ningrese segundo nombre, si no lo tiene apriete ENTER\n'))

if segundo_nombre:
    print (f"\nSu nombre completo es ----> {name.title()} {segundo_nombre.title()} {apellido.title()}\n")

else:
    print (f"\nSu nombre completo es ---->", name.title() + " " + apellido.title())

