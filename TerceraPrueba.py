""""3.- Crear un programa que te pida crear una contraseña, dicha contraseña debe respetar las 
siguientes reglas:
1. Debe contener al menos 2 letras mayúsculas.
2. Debe contener al menos 3 números no repetidos.
3. Debe contener al menos 1 carácter de esta lista (* _ - ¿ ¡ ? # $)
4. No debe contener espacios en blanco.
5. Debe tener entre 8 y 15 caracteres, no más, no menos.
Ejemplo: 
Contraseña: “FaciliTo22 ” -> 
Error la contraseña no debe tener números repetidos
Error la contraseña debe tener 3 números
Error la contraseña debe tener al menos un carácter especial (* _ - ¿ ¡ ? # $)
Error la contraseña no debe tener espacios en blanco
Contraseña: “ContraseñA495*”
Contraseña valida"""

c_especiales = ["*","_","-","¿","¡","?","#","$"]
checar_validez = [False,False,False,False]

def primera_regla(pswrd):
    #funcion para comprobar que tiene almenos 2 letras mayusculas
    return (sum(c.isupper() for c in pswrd)>=2)

def segunda_regla(pswrd):
    #funcion para comprobar que tiene almenos 3 numeros y que no sean repetidos
    no_repetido = True
    for position, letter in enumerate(pswrd):
        if letter.isdigit():
            if pswrd.count(letter)>=2:
                no_repetido = False
                break
    return (sum(c.isdigit() for c in pswrd)>=3 and no_repetido)

def tercera_regla(pswrd):
    #funcion para comprobar si tiene minimo un caracter en la lista de caracters especiales
    return any(ele in pswrd for ele in c_especiales)

def cuarta_quinta_regla(pswrd):
    #funcion para comprobar que no tenga espacio y que no sea menor a 8 ni mayor a 15
    return (' ' not in pswrd and 8<= len(pswrd) and len(pswrd) <= 15)

print("ingrese la contraseña a validar")
p_checar = input().lower()

if primera_regla(p_checar):
    checar_validez[0] = True
else:
    print("Error la contraseña debe tener al menos 2 letras mayusculas")
if segunda_regla(p_checar):
    checar_validez[1] = True
else:
    print("Error la contraseña debe tener 3 numeros y que no se repitan")
if tercera_regla(p_checar):
    checar_validez[2] = True
else:
    print("Error la contraseña debe tener al menos un carácter especial (* _ - ¿ ¡ ? # $)")
if cuarta_quinta_regla(p_checar):
    checar_validez[3] = True
else:
    print("Error la contraseña no debe tener espacios en blanco y que no sea menor a 8 ni mayor a 15")
if all(checar_validez):
    print("Contraseña valida")