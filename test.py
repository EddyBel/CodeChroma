if __name__ == "__main__":
    
    from CodeChroma import TerminalColors
    
    # We create an instance of the library
    termcolor = TerminalColors()
    
    #  Sample text for coloring
    text = \
"""
# Sintaxis de Java

## Variables

En Java, existen diferentes tipos de variables, como enteros, flotantes, caracteres y booleanos, además de variables de tipo objeto como String o Arrays. Es importante declarar el tipo de variable correcto para evitar errores en tiempo de ejecución. Por ejemplo, si quieres almacenar un valor numérico entero, se debe utilizar "int" como el tipo de dato.

```java
int numeroEntero = 10;
float decimal = 3.14f;
char letra = 'A';
boolean verdaderoOFalso = true;
```
"""

    # We color the text with its method "coloring_text", the text passed by parameter
    # The function returns a new string with the text already colored.
    colored_text = termcolor.coloring_text(text)
    # We can display the new text
    print(colored_text)