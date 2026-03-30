---
  kernelspec:
    display_name: 'Python 3'
    name: python3
---

# Chapter 1

## Exercises 1.1

### Exercise 1

Let $f = x^2y$ and $g = y\sin{z}$ be functions on $\R^3$. Express the following
functions in terms of $x, y, z:$

(a) $fg^2$.

(b) $\pd{f}{x} g + \pd{g}{y} f$.

(c) $\spd{(fg)}{y}{z}$.

(d) $\pd{}{y}(\sin f)$.

---

*Solution:*

(a) $fg^2 = \bx{x^2y^3\sin^2{z}}$.

(b) $\pd{f}{x} g + \pd{g}{y} f = 2xy^2\sin{z} + x^2y\sin{z}$.

(c) $\spd{(fg)}{y}{z} = \pd{}{y} \pd{(fg)}{x} = \pd{}{y}2xy^2\sin{z} = \bx{4xy\sin{z}}.$

(d) $\pd{}{y}(\sin f) = \pd{}{f}(\sin f)\pd{f}{y} = \bx{x^2\cos(x^2y)}$.

*Notes:*

Notice the atypical formulation $f = x^2y$ instead of $f(x, y) = x^2y$. Rather than specifying
the behavior of $f$ on points $\v{p}$, it is written as an algebraic expression in the *functions*
$x, y,$ and $z$, since these may depend on other functions or variables. 
We will have to be especially careful about the application of the chain rule going
forward, and this notation should help avoid mistakes.

### Exercise 2

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

Let's check our answers by trying out [Sage](sagemath.org). In Sage, our
notion of the function as an algebraic expression of functions is
paralleled by defining the function as a symbolic expression.

```{code-cell} python
import os
from sage.all import *

var('x, y, z, a, t')

xyz = lambda v: {'x': v[0], 'y': v[1], 'z': v[2]}

f = x ** 2 * y - y ** 2 * z

cases = {
    'a': [1, 1, 1],
    'b': [3, -1, 1/2],
    'c': [t, t**2, t**3],
    'd': [a, 1, 1-a],
}

for case, args in cases.items():
    print(f"({case}): f(*{(args)}) = {f.subs(**xyz(args))}")
```

### Exercise 3

Express $\pd{f}{x}$ in terms of $x, y$ and $z$ if

(a) $f = x\sin(xy) + y\cos(xz).$ 

(b) $f = \sin g, g = e^h, h=x^2 + y^2 + z^2$.

---

*Solution:*

(a) 
```{math}
:enumerated: false
\pd{f}{x} &= \pd{x}{x}\sin(xy) + x\pd{}{x}\sin(xy) + y\pd{}{x}cos(xz)\\
        &= \bx{\sin(xy) + xy\cos(xy) - yz\sin(xz)}.
```

(b) $\pd{f}{x} = \pd{}{g}\sin g \cdot \pd{g}{x} = \cos g \cdot \pd{}{h}(e^h) \cdot \pd{h}{x} = \bx{2xe^{x^2 + y^2 + z^2}\cos e^{x^2 + y^2 + z^2}}$.

```{code-cell}{python}
f = x*sin(x*y) + y*cos(x*z)
print(f.diff(x))
f = sin(exp(x**2 + y**2 + z**2))
print(f.diff(x))
```

### Exercise 4

If $g_1, g_2, g_3,$ and $h$ are real-valued functions on $\R^3$, then

```{math}
:enumerated: false
f = h(g_1, g_2, g_3)
```

is the function such that

```{math}
:enumerated: false
f(\v{p}) = h(g_1(\v{p}), g_2(\v{p}), g_3(\v{p})) \text{ for all } \v{p}.
```

Express $\pd{f}{x}$ in terms of $x, y,$ and $z$, if $h = x^2 - yz$ and

(a) $f = h(x + y, y^2, x + z).$

(b) $f = h(e^z, e^{x + y}, e^x).$

(c) $f = h(x, -x, x).$

---

*Solution:*

Substituting expressions gives a function matching the definition above when
combined with the algebraic rules for adding and multiplying functions found in the chapter.
This can be supposed obvious, but proving it formally is a little bit subtle.
Suppose that $E, E_i$ are formal algebraic expressions (or operations) in three variables, and that
$h = E(x, y, z)$, and $g_i = E_i(x, y, z)$, then, given $E(f, g, h)(\v{p}) = E(f(\v{p}), g(\v{p}), h(\v{p}))$,
and $x(p_1, p_2, p_3) = p_1$ etc., as in the text,

```{math}
:enumerated: false

f(\v{p}) &= h(g_1(\v{p}), g_2(\v{p}), g_3(\v{p})) \\
    &= E(x, y, z)(g_1(\v{p}), g_2(\v{p}), g_3(\v{p})) \\
    &= E(x(g_1(\v{p}), g_2(\v{p}), g_3(\v{p})), ... ) \\
    &= E(g_1(\v{p}), g_2(\v{p}), g_3(\v{p})) \\
    &= E(E_1(x, y, z)(\v{p}), E_2(x, y, z)(\v{p}), E_3(x, y, z)(\v{p})) \\
    &= E(E_1(x, y, z), E_2(x, y, z), E_3(x, y, z))(\v{p}), \\
```

so

```{math}
:enumerated: false
f = E(E_1(x, y, z), E_2(x, y, z), E_3(x, y, z)), \text{ as desired.}
```

Back to the very simple solutions to this exercise.

(a) $f = (x + y)^2 - y^2(x + z)$, so $\pd{f}{x} = \bx{2(x + y) - y^2}.$

(b) $f = (e^z)^2 - e^{x + y}e^x = e^{2z} - e^{2x + y}$, so $\pd{f}{x} = \bx{-2e^{2x + y}}.$

(c) $f = x^2 + x^2 = 2x^2$, so $\pd{f}{x} = \bx{4x}.$

```{code-cell}{python}
h = x**2 - y*z

subs = [
    [x + y, y**2, x + z],
    [exp(z), exp(x + y), exp(x)],
    [x, -x, x],
]

for args in subs:
    print(h.subs(**xyz(args)).diff(x))
```

## Exercises 1.2

### Exercise 1

Let $\v{v} = (-2, 1, -1)$ and $\v{w} = (0, 1, 3).$

(a) At an arbitrary point $\v{p}$, express the tangent vector $3\v{v}_p - 2\v{w}_p$ as a linear
combination of $U_1(\v{p}), U_2(\v{p}), U_3(\v{p})$ .

(b) For $\v{p} = (1, 1, 0),$ make an accurate sketch showing the four tangent vectors $\v{v}_p, \v{w}_p, -2\v{v}_p,$ and $\v{v}_p + \v{w}_p$.

---

*Solution:*

(a)
```{math}
:enumerated: false

3\v{v}_p - 2\v{w}_p
    &= 3(-2, 1, -1)_p - 2(0, 1, 3)_p \\
    &= (-6, 1, -9)_p \\
    &= \bx{-6U_1(\v{p}) + U_2(\v{p}) - 9U_3(\v{p})}.
```

(b)

Let's write some utilities for [plotly](https://plotly.com/python).
I'm going to maintain a plotting library `plot_dg` in a separate
script which you can find in the [repository](https://github.com/oelarnes/math/blob/main/src/plot_dg.py).

We'll want functions to create a figure and add point markers and arrowed vectors.
I used Claude to help set up the functions. Learning plotting libraries is a pain!

```{code-cell}{python}
# v3
import numpy as np
from plot_dg import dg_figure, add_point, add_vector

p = [1, 1, 0]
v = np.array([-2, 1, -1])
w = np.array([0, 1, 3])

fig = dg_figure(xlim=(-2, 6))

add_point(fig, p, name="p")
add_vector(fig, v, p, name="v_p", color="blue")
add_vector(fig, w, p, name="w_p", color="red")
add_vector(fig, -2*v, p, name="-2v_p", color="green")
add_vector(fig, v + w, p, name="v_p + w_p", color="purple")
add_vector(fig, v, p + w, color="blue", line_style="dash")
add_vector(fig, w, p + v, color="red", line_style="dash")

fig.show()
```

### Exercise 2

Let $V = xU_1 + yU_2$ and $W = 2x^2U_2 - U_3.$ Compute the vector $W - xV$, and find its value at the point $\v{p} = (-1, 0, 2).$

---

*Solution:*

```{math}
:enumerated: false

W - xV &= 2x^2U_2 - U_3 - x(xU_1 + yU_2) \\
    &= 2x^2U_2 - U_3 - x^2U_1 - xyU_2 \\
    &= -x^2U_1 + (2x^2 - xy)U_2 - U_3. \\
    \\

(W-xV)_{(-1, 0, 2)} &= -U_1 + 2U_2 - U_3 = \bx{(-1, 2, -1)}.
```

```{code-cell}{python}
E = EuclideanSpace(names=('x', 'y', 'z'))
(x, y, z) = E._first_ngens(3)

V = E.vector_field(x, y, 0)
W = E.vector_field(0, 2*x**2, -1)
Z = W - x*V

print(Z.display())
print(Z.at(E((-1, 0, 2)))[:])
```

### Exercise 3

In each case, express the given vector field $V$ in the standard form $\sum v_iU_i$.

(a) $2z^2U_1 = 7V + xyU_3.$

(b) $V(\v{p}) = (p_1, p_3 - p_1, 0)_p$ for all $\v{p}$.

(c) $V = 2(xU_1 + yU_2) - x(U_1 - y^2U_3).$

(d) At each point $\v{p}$, $V(\v{p})$ is the vector from the point $(p_1, p_2, p_3)$
    to the point $(1~+~p_1, p_2p_3, p_2)$.

(e) At each point $\v{p}, V(\v{p})$ is the vector from $\v{p}$ to the origin.

---

*Solution:*

(a) $V = \bx{-2z^2U_1 + xyU_3}.$

(b) $V = \bx{xU_1 + (z - x)U_2}.$

(c) $V = \bx{xU_1 + yU_2 + xy^2U_3}.$

(d) $V = \bx{U_1 + y(z - 1)U_2 + (y-z)U_3}.$

(e) $V = \bx{-xU_1 - yU_2 -zU_3}.$

### Exercise 4

If $V = y^2U_1 - x^2U_3$ and $W = x^2U_1 - zU_2$, find functions $f$ and $g$ such
that the vector field $fV + gW$ can be represented in terms of $U_2$ and $U_3$ only.

---

*Solution:*

We need $v_1 = fy^2 + gx^2 = 0$, so $f = x^2$ and $g = -y^2$ will suffice. $\square$

### Exercise 5

Let $V_1 = U_1 - xU_3$, $V_2 = U_2$, and $V_3 = xU_1 + U_3$.

(a) Prove that the vectors $V_1(\v{p}), V_2(\v{p}), V_3(\v{p})$ are linearly independent at
each point of $R^3$.

(b) Express the vector field $xU_1 + yU_2 + zU_3$ as a linear combination of $V_1, V_2, V_3$.

---

*Solution:*

(a) We consider the equation $V = aV_1 + bV_2 + cV_3 = 0$ and consider whether it has nonzero solutions
for any $x, y, z$. Suppose $V = (a + cx)U_1 + bU_2 + (c - ax)U_3 = 0$, and we need each component to be zero,
that is, solutions to the system

```{math}
:enumerated: false

a + cx &= 0 \\
b &= 0 \\
c - ax &= 0. \\
```

We have $c = ax$, then $a + ax^2 = a(1 + x^2) = 0$, but since $1 + x^2 > 0$, that implies $a = 0$, whence
$c = 0$, so since $b = 0$, $(a, b, c) = (0, 0, 0)$ for all $\v{p}$ and the vectors are linearly
independent as desired. $\square$

(b) Now let

```{math}
:enumerated: false

a + cx &= x \\
b &= y \\
c - ax &= z, \\
```

and we see that $a = x - cx$, so solve $c - (x - cx)x = z$ for $c$, getting

```{math}
:enumerated: false

c - (x - cx)x = z \\
c + cx^2 = z + x^2 \\
c = \frac{z + x^2}{1 + x^2}, \\
```

and

```{math}
:enumerated: false

a = x - cx = x - \frac{z + x^2}{1 + x^2}x = \frac{x^3 - x^3 + x - zx}{1 + x^2} = \frac{x - zx}{1 + x^2},
```

so the vector field in terms of the new basis is

```{math}
:enumerated: false

xU_1 + yU_2 + zU_3 = \bx{\frac{x - zx}{1 + x^2}V_1 + yV_2 + \frac{x^2 + z}{1 + x^2}V_3}.
```

## Exercises 1.3

### Exercise 1

Let $\v{v}_p$ be the tangent vector to $\R^3$ with $\v{v} = (2, -1, 3)$ and $\v{p} = (2, 0, -1).$
Working directly from the definition, compute the directional derivative $\v{v}_p[f]$, where

(a) $f = y^2z$.

(b) $f = y^7$.

(c) $f = e^x\cos{y}.$

### Exercise 2

Compute the derivatives in Exercise 1 using Lemma 3.2.

---

*Solution:*

(a)
```{math}
:enumerated: false

\v{v}_p[f] &= 2U_1\pd{f}{x}(\v{p}) - U_2\pd{f}{y}(\v{p}) + 3U_3\pd{f}{z}(\v{p}) \\
    &= -U_2(2yz)_{|(2, 0, -1)} + 3U_3(y^2)_{|(2, 0, -1)} \\
    &= \bx{0}.
```

(b)
```{math}
:enumerated: false

\v{v}_p[f] &= 2U_1\pd{f}{x}(\v{p}) - U_2\pd{f}{y}(\v{p}) + 3U_3\pd{f}{z}(\v{p}) \\
    &= -U_2(7y^6)_{|(2, 0, -1)} \\
    &= \bx{0}.
```

(c)
```{math}
:enumerated: false

\v{v}_p[f] &= 2U_1\pd{f}{x}(\v{p}) - U_2\pd{f}{y}(\v{p}) + 3U_3\pd{f}{z}(\v{p}) \\
    &= 2U_1(e^x\cos{y})_{|(2, 0, -1)} + U_2(e^x\sin{y})_{|(2, 0, -1)} \\
    &= \bx{2e^2U_1}.
```

### Exercise 4

Prove the identity $V = \sum V[x_i]U_i$, where $x_1, x_2, x_3$ are the natural coordinate
functions.

---

*Solution:*

Since $V = \sum v_iU_i$, we need only prove $V[x_i] = v_i$ for $i \in \{1,2,3\}$. By Lemma 3.2 and the pointwise principle,

```{math}
:enumerated: false

V[x_i] &= \sum_j v_j \pd{x_i}{x_j} \\
    &= \sum_j v_j \delta_{ij}\\
    &= v_i,

```
as desired. $\square$

## Exercises 1.4

### Exercise 2

Find the unique curve such that $\alpha(0) = (1, 0, 5)$ and $\alpha'(t) = (t^2, t, e^t)$.

---

*Solution:*

Integrate to get 

```{math}
:enumerated: false

\alpha(t) = \left(\frac{t^3}{3} + C_1, \frac{t^2}{2} + C_2, e^t + C_3\right).
```

We need $C_1 = 1, C_2 = 0, \text{ and } 1 + C_3 = 5$, giving

```{math}
:enumerated: false

\alpha(t) = \bx{\left(\frac{t^3}{3} + 1, \frac{t^2}{2}, e^t + 4\right)}.
```

$\square$.

### Exercise 4

Reparametrize the curve $\alpha$ in Example 4.2(4) using $h(s) = \log{s}$ on
$J: s > 0.$ Check the equation in Lemma 4.5 in this case by calculating each
side separately.

---

*Solution:*

The curve in question is 

```{math}
:enumerated: false

\alpha(t) = (e^t, e^{-t}, \sqrt{2}t).
```

The reparametrization is given by 

```{math}
:enumerated: false

\beta(s) = \alpha(h(s)) &= (e^{\log s}, e^{-\log s}, \sqrt{2}\log s) \\
    &= (s, \frac{1}{s}, \sqrt{2}\log s).
```

Lemma 4.5 gives 

```{math}
:enumerated: false

\beta'(s) = (dh/ds)(s)\alpha'(h(s)),
```

so calculate

```{math}
:enumerated: false

\frac{dh}{ds} = \frac{1}{s},\\
\alpha'(t) = (e^t, -e^t, \sqrt{2}),\\
```

so

```{math}
:enumerated: false

\frac{dh}{ds}(s)\alpha'(h(s)) &= \frac{1}{s}(s, -\frac{1}{s}, \sqrt{2}) \\
    &= (1, -\frac{1}{s^2}, \frac{\sqrt{2}}{s}),
```

which is also the directly calculated

```{math}
:enumerated: false


\beta'(s) = (1, -\frac{1}{s^2}, \frac{\sqrt{2}}{s}),\\
```

as desired. $\square$

### Exercise 8


```{code-cell}{python}
```
