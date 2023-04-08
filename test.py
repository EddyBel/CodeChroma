if __name__ == "__main__":
    from CodeChroma import TerminalColors, Colors
    
    # We create an instance of the library
    colors = Colors()
    termcolor = TerminalColors(title="yellow", list_item="magenta")
    
    # Options
    # termcolor.view_lang = False
    # termcolor.format_code = False
    # termcolor.elements = { 
    #     "title": colors.bg_cyan,
    #     "block": colors.yellow,
    #     "list-item": colors.magenta,
    #     "url": colors.cyan,
    #     "parentheses": colors.light_red,
    #     "string": colors.light_green,
    #     "code": colors.yellow,
    #     "lang": colors.red 
    # }
    
    def test_content_by_file () :
        with open("./assets/test-1.md", "r", encoding="utf-8") as file:
            content = file.read()
        print(termcolor.coloring_text(content))
        
    def test__text ():
        #   Sample text for coloring
        text = \
    """
    # Sintaxis de Java

    ## Variables

    En "Java", existen diferentes tipos de variables, como (enteros, flotantes, caracteres y booleanos), además de variables de tipo objeto como String o Arrays.   Es importante declarar el tipo de variable correcto para evitar errores en tiempo de ejecución. Por ejemplo, si quieres almacenar un valor numérico entero, se    debe utilizar "int" como el tipo de dato.

    ```java
    int numeroEntero = 10;
    float decimal = 3.14f;
    char letra = 'A';
    boolean verdaderoOFalso = true;
    ```
    """

        colored_text = termcolor.coloring_text(text)
        print(colored_text)
    
    
    def test_code () :
        
        code = \
    """
    ```
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Vite + React + TS</title>
      </head>
      <body>
        <div id="root"></div>
        <script type="module" src="/src/main.tsx"></script>
      </body>
    </html>
    ```
    """
        code_colored = termcolor.color_code(code)
        print(code_colored)
        
    # Run test
    # test_code()
    test__text()
    # test_content_by_file()