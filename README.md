Es un pequeño procesador de hojas de cálculo en modo texto. Lee por la entrada estándar una hoja de cálculo, con las celdas separadas por tabuladores, que contienen fórmulas en "s-expressions" (tipo lisp), con la salvedad de que sólo intenta evaluar una función si es válida, en el caso contrario evalúa el contenido de la lista y devuelve la lista y que los operadores aritméticos se aplican de forma recursiva a las sublistas.

Operaciones soportadas:

```
+ : suma
- : resta
* : producto
/ : división
@ : referencia a otra celda
# : rango de celdas
```

Ejemplo de entrada (las columnas están separadas con tabuladores):

```
(@ 1 1)	2	0
(/ 1 2)	(+ (@ 0 1)(@ 1 0))	(+ 1 2)
(+ (# 0 0 1 2))
```

Ejemplo de salida:
```
2.5	2	0
0.5	2.5	3
4.5
```