Minimalistic spreadhseet processor for the console.

It reads a spreadsheet tsv (tab-separated-values) from stdin, evaluates it and prints the result to stdout.

The formulae are input as "s-expressions" (like LISP or Scheme); and are evaluated recursively. If a list does not start with a valid operator (see below), the result is a list itself (with each member being evaluated).

Supported opperators:

```
+ : addition
- : substraction
* : multiplication
/ : división
@ : cell reference
# : cell range
```

Example input:

```
(@ 1 1)	2	0
(/ 1 2)	(+ (@ 0 1)(@ 1 0))	(+ 1 2)
(+ (# 0 0 1 2))
```

Output for the example above:
```
2.5	2	0
0.5	2.5	3
4.5
```
