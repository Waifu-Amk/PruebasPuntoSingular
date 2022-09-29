""""
2.- Crear un programa que dada una palabra la separe en sus distintas silabas, siguiendo las 
siguientes reglas:
1. Una sola consonante entre dos vocales se agrupa con la vocal que sigue.
Ejemplos: a-gu-je-ro, pe-lo-te-ro.
2. Dos consonantes entre dos vocales se agrupan una para cada vocal. 
Ejemplos: in-men-son, gim-nas-ta.
Esta regla tiene una excepción: los grupos consonánticos pr, pl, br, bl, fr, fl, tr, tl, dr, dl, cr, 
cl, gr, se unen a la vocal siguiente. 
Ejemplos re-fres-co, a-flo-jar.
Las consonantes dobles en la escritura ch, ll, rr, responden a un solo fonema, por lo que 
se consideran a los efectos de la separación silábica como una sola consonante. 
Ejemplo, ca-lle, ce-rro.
3. Tres consonantes en medio de dos vocales se agrupan dos con la primera vocal y la 
tercera con la vocal que sigue. 
Ejemplos; ins-pec-tor, obs-ta-cu-li-zar.
Esta regla tiene la excepción anterior. 
Ejemplos: A-tlan-ti-co, ham-bre.
4. Cuatro consonantes en medio de dos vocales se agrupan dos con la primera vocal y las 
otras dos con la vocal que sigue. 
Ejemplos: Cons-truc-ción, ins-truc-ción."""

import pyphen

excepciones = ["agujero","atlantico","aflojar"]
excepciones_separadas = ["a-gu-je-ro","a-tlan-ti-co","a-flo-jar"]
separador = pyphen.Pyphen(lang='es_US')

"""def test():
    words_test=["agujero","pelotero","inmenson","gimnasta","refresco","aflojar","calle","cerro",
    "inspector","obstaculizar","atlantico","hambre","construccion","instrucción"]
    for element in words_test:
        print(separador.inserted(element))"""
    
print("ingrese una palabra que quiera separa por silabas")
palabra = input().lower()
if any(element in palabra for element in excepciones):
    for position,element in enumerate(excepciones):
        if palabra == element:
            print(excepciones_separadas[position])
            break
else:
    print(separador.inserted(palabra))
