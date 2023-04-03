import os

# Podemos ingresar la direccion del archivo sin ingresar al codigo
file_path = input('Ingresa la direccion de tu archivo: ')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('El archivo se elimio exitosamente')
    print(file_path)
else:
    print('No se pudo encontrar el archivo')
    print(file_path)
    
