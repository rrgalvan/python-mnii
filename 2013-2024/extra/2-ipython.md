
- Componentes de  un entorno de *Python científico*:

    - Intérprete del lenguaje Python

    - Bibliotecas científicas (`numpy`, `scipy`, `matplotlib`,...)

	- Editor o entorno integrado para el desarrollo de código

- *IPython*: un "intérprete mejorado":

    - Intérprete: programa encargado de ejecutar código Python

    - *IPython* es un *intérprete extendido*, que ofrece funcionalidades
      adicionales que lo hacen más cómodo de manejar del intérprete
      estándar de Python.

    - Algunas de estas funcionalidades:

	    - Completado de órdenes mediante la tecla `[TAB]`

		- Uso de `?` para información de objetos, `objeto?`

        - Funciones adicionales (ejemplo: `run` script)

        - Extensión *notebook* (entorno de tipo "Mathematica")

- *Bibliotecas* o paquetes en Python: extensiones al lenguaje

    - Formas de usarlas:

        - `from <biblioteca> import <objeto>`

		   Importa un objeto concreto (una variable, una función, etc)
           de una biblioteca

        - `from <biblioteca> import *`

           Importa todos los objetos contenidos en la Bibliotecas

        - `import biblioteca`

	       Importa la biblioteca pero no incluye los objetos en el
           espacio de nombres actual.

- *Entornos gráficos*: Spyder

	- Puede usar *ipython* (se recomienda)

    - Por defecto, incluye algunas bibliotecas científicas básicas:
      `numpy` (cálculo numérico básico con *arrays*), `matplotlib`
      (dibujo de gráficas).
