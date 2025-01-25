----{ BASIC TEMPLATE }----

En esta plantilla podrás ver y aprender cómo se estructuran la mayoría de proyectos en Python. Esta es una plantilla
bastante básica, de solo un directorio, aunque igualmente aprenderás de ella. ¡Empecemos a ver cómo se estructura
este proyecto!

¿Qué son todas estas carpetas?
- Puede parecer un poco abrumador al principio, ¡pero nada más lejos de la realidad! Todas las carpetas sirven un
propósito, empecemos:

assets: Esta carpeta se encarga de almacenar todos los elementos gráficos, modelos, sonidos y recursos que el
programa pueda necesitar a lo largo de la ejecución. Por ejemplo: Imaginemos que, al ejecutar el programa, este
muestra una imagen que actúa como logo. La imagen seguramente esté localizada en la carpeta llamada assets.

dist: La abreviatura "dist" proviene del inglés "distribution", es decir, el contenido que esta carpeta debería
tener serían solo archivos compilados (1) del mismo. Ejemplos de archivos: "win-program-x64.exe", "win10-test-x86.msi".

lib: La abreviatura "lib" proviene del inglés "library". Una librería es un conjunto de módulos que contienen
funciones, clases y herramientas reutilizables para facilitar tareas comunes. En lugar de escribir todo desde cero,
puedes usar estas librerías para ahorrar tiempo y esfuerzo.

sh: La abreviatura "sh" proviene de "shell". Esta carpeta se usa para insertar archivos de código que se ejecutan
luego en la consola. Por ejemplo: podrías crear una carpeta en un archivo ".sh" usando el comando "mkdir", en vez de
crear la carpeta en Python.

¡Perfecto! Ya sabemos qué significan todas las carpetas de esta plantilla. Recuerda que pueden haber muchas más
carpetas, incluso algunas inventadas por el propio desarrollador.

¿Por qué lo llamamos "main.py"?
- Llamarlo main (principal en inglés) se ha vuelto una regla no escrita entre los programadores. Siempre puedes
llamarlo como tú quieras, pero es mucho más recomendable llamarlo main.

¿Qué es el README.txt/.md?
- Lo que has estado leyendo se usa para dar información sobre el proyecto. Puede tener extensión .txt o .md.

(1) Compilados: Convertir un programa en lenguaje máquina a partir de otro programa de computadora escrito en otro
lenguaje. Según la R.A.E.
