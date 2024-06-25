#la idea era que sea mas sencillo, pero me gusto implementar el if. para incorporar el segundo nombre, si es que tiene.

text = input ('\ningrese una frase\n')

string = text.split()

del_str = input ('\nelija una palabra para reemplazar\n')

new_str = input ('\nelija la palabra nueva\n')

if del_str in string:  

    indice = string.index(del_str) #la funcion .index () lo tuve que buscar por google. 

    string [indice] = new_str

texto = ' '.join (string)    


print ("\nSu frase fue modificada con la palabra elegida ---> " ,texto)










