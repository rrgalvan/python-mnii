# Python científico

## ¿Qué es Python?

Python es simplemente un *lenguaje de programación* interpretado[^1], con unas características concretas que, como veremos, lo hacen *apropiado para una asignatura como Métodos Numéricos II*.

El intérprete de Python tiene licencia libre[^2], en particular puede descargarse y copiarse gratuitamente. Del mismo modo que muchos entornos integrados para el desarrollo de software.

## ¿Cuáles son sus características?

1. Es un lenguaje de *propósito general*[^3]. Es decir, orientado a la escritura de todo tipo de software, no solamente a un ámbito específico.

2. Diseñado con énfasis en la *sencillez del código* y el *desarrollo rápido* de software.

3. Con *características muy avanzadas*[^5] y con una *enorme cantidad de bibliotecas*[^6] para todo tipo de propósitos, algunas de ellas idóneas para el desarrollo de software numérico (Numpy, Scipy, Matplotlib, Pandas...).

4. *Muy popular*: entre los programadores, para aplicaciones multipropósito[^4]. En particular, al ser fácilmente acoplable con otros lenguajes (C/C++, Fortran, etc.) constituye el lenguaje usual en interfaces de extensión y acceso rápido a programas y bibliotecas. Particularmente, en bibliotecas científicas de alto rendimiento.

## ¿Por qué usar Python en Métodos Numéricos II?

1. Python es un lenguaje moderno que, en computación científica, es hoy una opción consolidada[^7]

2. Sus características garantizan que los estudiantes programen en el ordenador los métodos numéricos que son objeto de la asignatura, de una forma satisfactoria.

3. La acreditación de conocimientos un lenguaje de programación de propósito general como Python supone un valor añadido en el currículum del Grado en Matemáticas y abre las puertas a su futuro uso, bien en otras asignaturas de grado o máster, bien en el ámbito laboral.


## ¿Cómo instalar Python en mi ordenador?

La idea será instalar, no sólo el intérprete de Python, sino una
distribución científica de Python, es decir que integre:

* El intérprete Python

* Un editor o un entorno de desarrollo adecuado

* Las bibliotecas científicas que utilizaremos en la asignatura

Para ello, existen distintas posibilidades, que agruparemos por sistemas operativos. Es importante subrayar que, en lo fundamental, todas estas distribuciones contienen *exactamente el mismo software* (python+bilbliotecas+editores):

### Entornos Windows

* [Python(x,y)](https://code.google.com/p/pythonxy/)
Versión muy completa.

* [WinPython](http://winpython.sourceforge.net/)
Versión menos completa pero más ligera.

* [Canopy Express](https://www.enthought.com/canopy-express/)
Basada en una versión más amplia (y comercial), Canopy.

### Entornos Macintosh

* [Canopy Express](https://www.enthought.com/canopy-express/)

### Entornos GNU/Linux

* [Canopy Express](https://www.enthought.com/canopy-express/)

* Para usuarios avanzados, se recomienda instalar los paquetes adecuados (en estos sistemas es muy fácil, por ejemplo, usando el centro de software): Python 2.7, Ipython, Numpy, Scipy, Matplotlib, Pandas. Como editor, se puede instalar el paquete Spyder.


[^1]: A diferencia de los lenguajes compilados, los programas en [lenguajes interpretados](http://es.wikipedia.org/wiki/Lenguaje_de_alto_nivel) se ejecutan mediante un *intérprete* (que en ciertos contextos es conocido como *kernel*)

[^2]: [Software libre en Wikipedia](http://es.wikipedia.org/wiki/Software_libre),

[^3]: [Lenguaje de propósito genral en Wikipedia](http://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_de_prop%C3%B3sito_general)

[^4]: Se encuentra entre el 7º y e 8º, entre los lenguajes de programación más usados (véase por ejemplo el índices de popularidad [tiobe.com](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html) o buscar en internet, por ejemplo usando las palabras clave: *programming language popularity*)

[^7]: [Introducción a la Computación Científica con Python](http://nbviewer.ipython.org/github/gfrubi/clases-python-cientifico/blob/master/Lecture-0-Scientific-Computing-with-Python.ipynb)
