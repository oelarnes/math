---
  kernelspec:
    display_name: Python 3
    name: python3
---

# Chapter 1
## Problem Set 1

### Problem 1

Let $f = x^2y$ and $g = \sin{z}$ be functions on $\R^3$. Express the following
functions in terms of $x, y, z:$

(a) $fg^2$.

(b) $\pd{f}{x} g + \pd{g}{x} f$.

(c) $\spd{(fg)}{y}{z}$.

(d) $\pd{}{y}(\sin f)$.

---

*Solution:*

(a) $fg^2 = \bx{x^2y\sin^2{z}}$.

(b) $\pd{f}{x} g + \pd{g}{x} f = \pd{(fg)}{x}= \bx{2xy\sin{z}} $.

(c) $\spd{(fg)}{y}{z} = \pd{}{y} \pd{(fg)}{x} = \pd{}{y}2xy\sin{z} = \bx{2x\sin{z}}.$

(d) $\pd{}{y}(\sin f) = \pd{}{f}(\sin f)\pd{f}{y} = \bx{x^2\cos(x^2y)}$.

*Notes:*

Notice the atypical formulation $f = x^2y$ instead of $f(x, y) = x^2y$. Rather than specifying
the behavior of $f$ on points $\v{p}$, it is written as an algebraic expression in the *functions*
$x, y,$ and $z$, since these may depend on other functions or variables. 
We will have to be especially careful about the application of the chain rule going
forward, and this notation should help avoid mistakes.

### Problem 2

Find the value of the function $f = x^2y - y^2z$ at each point:

(a) $(1,1,1)$.

(b) $(3, -1, ½)$.

(c) $(a, 1, 1-a)$.

(d) $(t, t^2, t^3)$.

---

*Solution:*

(a) $f(1,1,1) = 1^2 \cdot 1 - 1^1 \cdot 1 = \bx{0}.$

(b) $f(3, -1, ½) = 3^2 \cdot (-1) - (-1)^2 \cdot ½ = \bx{-9½}.$

(c) $f(a, 1, 1 - a) = a^2  - (1 - a) = \bx{a^2 + a - 1}.$

(d) $f(t, t^2, t^3) = t^2t^2  - (t^2)^2t^3 = \bx{t^4 - t^7}.$

*Notes:*

Let's check our answers by trying out [Sage](sagemath.org).

```{code-cell}{python}
from sage.all import *

f = lambda x, y, z: x ** 2 * y - y ** 2 * z

a = var('a')
t = var('t')

cases = {
    'a': [1, 1, 1],
    'b': [3, -1, 1/2],
    'c': [t, t**2, t**3],
    'd': [a, 1, 1-a],
}

for case, args in cases.items():
    print(f"({case}): {f(*args)}")
```
