import os

# Podemos ingresar la direccion del archivo sin ingresar al codigo
file_path = input('Enter the root of the file: ')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('The file was deleted successfuly')
    print(file_path)
else:
    print('File was not found')
    print(file_path)
    
