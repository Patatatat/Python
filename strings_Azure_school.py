    #.center es para centrar cadenas 
    #.rjust es para mover una cadena a la derecha
    #.ljust para la izquierda
    #.zfill rellena un numero con 0 al inicio
    #.strip elimia los '.' antes y despues de la cadena
    #.rstrip elimina la derecha
    #.upper()
    #.lower()
    #.casefold() cambia las letras mayusculas a minusculas
    #.swapcase() intercambia las mayuscualas de una palabra a otra y viseversa con minusculas
    #.title() no explicacion es muy obvio
    #.capitalize() ejemplo 'andres'.capitalize() 'Andres'
    #.find() encuentra las letras
    #.index() lo mismo que find pero avisa con un error
    #.rfind() Funciona de manera similar a find, a diferencia de que devuelve la posición más alta de la búsqueda.
    #.rindex() Su funcionamiento es igual a rfind, pero eleva ValueError en caso que la búsqueda no sea exitosa.
    #.endswith() devolvera true si el caracter esta en la ultima palabra si no sera false
    #.isalpha() devolvera true si el string es solo alphabetico (osea una palabra como esta) si tiene numeros retornara false
    #.isascii() Devuelve True si la cadena está vacía o todos los caracteres son ASCII, False en caso contrario. Los caracteres ASCII se encuentran en el rango  U+0000-U+007F de la tabla Unicode.
    #.isdecimal() Devuelve True si todos los caracteres en la cadena son caracteres decimales y hay al menos un carácter.
    #.isdigit() Similar a isdecimal, a diferencia de que también reconoce los números del sistema Kharosthi.
    #.isnumeric() Similar a isdigit pero también reconoce fracciones vulgares de Unicode, como por ejemplo ‘\u00BD’ para ½.
    #.isidentifier() Devuelve True si la cadena es un identificador válido de acuerdo con la definición del lenguaje.
    #.islower() devolvera verdadero si la palabra esta en minusculas
    #.isupper() devolvera verdadero si la palabra esta en mayusculas
    #.isprintable() Devuelve True si todos los caracteres de la cadena son imprimibles o la cadena está vacía
    #.isspace() Devuelve True en la cadena solo hay caracteres espaciadores y hay -al menos- un carácter, False de lo contrario. 
    #.istitle() Devuelve True si la cadena es una cadena con formato str.title() y hay al menos un carácter.
    #.isalnum() Devuelve True si todos los caracteres de la cadena son alfanuméricos y hay al menos un caracter, False en caso contrario.
    #.join() Devuelve una cadena concatenando los elementos de un iterable (como list, string y tuple), separándolos con la cadena str (a la que se aplica el método).
    #.partition() Devuelve una tupla de 3 elementos, donde se divide la cadena en la primer aparición del parámetro sep.
    #.rpartition() Similar a partition, a diferencia que parte la cadena en la última aparición del separador sep. Si no se encuentra el separador en la cadena, también devuelve una tupla de 3 elementos
    #.split() Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador.
    #.rsplit() Su comportamiento es similar a split, a diferencia de que al especificar un valor para maxsplit, se comienza a separar desde la derecha.
    #.splitlines() Devuelve una lista de las líneas en la cadena, rompiendo las mismas en los finales de línea.
    #.replace() Devuelve una cadena reemplazando todas las apariciones de la subcadena ‘old‘ reemplazadas por la nueva ‘new‘.
    #.format() De los más utilizados para cadenas, realiza una operación para formatear una cadena.
    #.format_map() Es similar a format, a diferencia de que los campos de reemplazo deben indicar los nombres de claves incluidas en el parámetro mapping.
    #.encode() Tal como vimos, el tipo str en Python está destinado a representar texto legible por humanos y puede contener cualquier caracter Unicode.
    #.decode() Devuelve una cadena decodificada de los bytes dados, donde la codificación predeterminada es ‘utf-8’.
    #list.extend(iterable) Añade todos los elementos de iterable a la lista list. 
    #list.insert(i, x) Al igual que list.append(x), agrega el elemento x a la lista list, a diferencia que lo agrega en la posición i, desplazando los siguientes elementos hacia la derecha.
    #list.clear() Elimina todos los elementos de la lista list.
    #list.sort(key=None, reverse=False) Ordena los elementos de la lista de menor a mayor.
    #list.reverse() Invierte los elementos de una lista. Es equivalente a realizar list[::-1], a diferencia que los valores de la lista son modificados.
    #list.copy() Devuelve una copia de la lista y es equivalente a utilizar list[:].
    #dict.update() Actualiza el diccionario con las palabras clave de other. Update acepta como argumento otro diccionario o argumentos de palabras clave con su valor. 
    #dict.get() Devuelve el valor de la clave key si la misma se encuentra en el diccionario; en caso contrario, devolverá el valor informado como default.
    #dict.keys() Devuelve una lista con todas las claves que posee el diccionario.
    #dict.values() Devuelve una lista con todos los valores de cada clave del diccionario. Cada elemento de la lista es el valor de una clave del diccionario.
    #dict.items() Devuelve una vista de todos los elementos del diccionario (claves y valores). 
    #dict.reserved() Si bien no es un método de los diccionarios, es una función que devuelve la vista de un diccionario en orden inverso al que se le indica como argumento.
    #dict.pop() Si la clave key existe en el diccionario, elimina la pareja clave/valor y devuelve el valor.
    #dict.popitem() Elimina y devuelve la última pareja clave:valor del diccionario. Al utilizar este método sobre un diccionario vacío, se eleva una excepción KeyError.
    #dict.setdefault() Si la clave key existe en el diccionario, devuelve su valor. Si la clave no existe, agrega la misma al diccionario con el valor indicado en default y devuelve dicho valor. 
    #dict.clear() Elimina todas las parejas clave:valor de un diccionario.
    #Dado a que en Python no se especifica el tipo de dato de cada parámetro que recibe y del valor que devuelve, en Python 3 se pueden incluir anotaciones para cada uno de estos parámetros (PEP 3107)(PEP 257).
    #*args La expresión *args se puede usar como parámetro de una lista y representa un número variable de argumentos que puede recibir la función sin que sean nombrados por una palabra clave.
    #**kwargs La expresión **kwargs se utiliza para pasar un número variable de argumentos, pero a diferencia de *args, estos deben ser nombrados con una clave en formato clave=valor.
    # def suma(*args):
    #   num = 0
    #    for arg in args:
    #        num += arg
    #    return num
    # 
    # def producto(*args):
    #    num = 1
    #    for arg in args:
    #        num *= arg
    #    return num
    # 
    # OPERACIONES = {
    #    "suma": suma,
    #    "producto": producto,
    # }
    # 
    # def operacion(*args, **kwargs):
    #    return OPERACIONES.get(kwargs.get("operacion"))(*args)
    #    
    # print(operacion(2, 3, 4, operacion="suma"))
    # print(operacion(2, 3, 4, operacion="producto"))