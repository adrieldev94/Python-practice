text = input ('\ningrese una frase\n')

string = text.split()

del_str = input ('\nelija una palabra para reemplazar\n')

new_str = input ('\nelija la palabra nueva\n')

if del_str in string:  

    indice = string.index(del_str)

    string [indice] = new_str

texto = ' '.join (string)    


print ("\nSu frase fue modificada con la palabra elegida ---> " ,texto)










