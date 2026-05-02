---
kernelspec:
  name: sagemath
  language: sage
  display_name: SageMath 10.7
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

(c) $\spd{(fg)}{y}{z} = \pd{}{y} \pd{(fg)}{z} = \pd{}{y}x^2y^2\cos{z} = \bx{2x^2y\cos{z}}.$

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

```{code-cell} sagemath
# Exercise 1.1.2
var('x, y, z, a, t')

xyz = lambda v: {'x': v[0], 'y': v[1], 'z': v[2]}
f = x**2 * y - y**2 * z

cases = {'a': [1, 1, 1], 'b': [3, -1, SR(1)/2], 'c': [t, t**2, t**3], 'd': [a, 1, 1-a]}
for case, args in cases.items():
    print(f"({case}): {f.subs(**xyz(args))}")
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
\pd{f}{x} &= \pd{x}{x}\sin(xy) + x\pd{}{x}\sin(xy) + y\pd{}{x}\cos(xz)\\
        &= \bx{\sin(xy) + xy\cos(xy) - yz\sin(xz)}.
```

(b) $\pd{f}{x} = \pd{}{g}\sin g \cdot \pd{g}{x} = \cos g \cdot \pd{}{h}(e^h) \cdot \pd{h}{x} = \bx{2xe^{x^2 + y^2 + z^2}\cos e^{x^2 + y^2 + z^2}}$.

*Notes:*

Sage confirms both partial derivatives directly.

```{code-cell} sagemath
# Exercise 1.1.3
var('x, y, z')
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

*Notes:*

Sage confirms by substituting and differentiating.

```{code-cell} sagemath
# Exercise 1.1.4
var('x, y, z')
h = x**2 - y*z
xyz = lambda v: {'x': v[0], 'y': v[1], 'z': v[2]}

subs = [[x+y, y**2, x+z], [exp(z), exp(x+y), exp(x)], [x, -x, x]]
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

The plotting library `plot_dg` (in the [repository](https://github.com/oelarnes/math/blob/main/src/plot_dg.py)) provides helpers for figures, points, and arrowed vectors.

```{code-cell} sagemath
# Exercise 1.2.1
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

```{code-cell} sagemath
# Exercise 1.2.2
E = EuclideanSpace(names=('x', 'y', 'z'))
(x, y, z) = E._first_ngens(3)

[U1, U2, U3] = E.cartesian_frame()
V = x * U1 + y * U2
W = 2*x**2*U2 - U3
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

Sketch the following Curves in $\R^2,$ and find parametrizations for each.

(a) $C: 4x^2 + y^2 = 1,$

(b) $C: 3x + 4y = 1,$

(c) $C: y = e^x.$

---

*Solution:*

In each case the domain is $\R$.

(a) The curve $\alpha(t) = (a\cos{t}, b\sin{t})$ has $(x/a)^2 + (y/b)^2 = 1$, so let $a = 1/2$ and $b = 1$ to get

```{math}
:enumerated: false

\bx{\alpha(t) = \left(\frac{\cos{t}}{2}, \sin{t}\right)}.
```

(b) Solve for $y$ and parametrize by $x$ to get

```{math}
:enumerated: false

\bx{\alpha(t) = \left(t, \frac{1-3t}{4}\right)}. 
```

(c) 

```{math}
:enumerated: false

\bx{\alpha(t) = (t, e^t)}.
```

## Exercises 1.5

### Exercise 2

If $\phi = \sum f_i dx_i$ and $V = \sum v_i U_i,$ show that the 1-form $\phi$ evaluated on the vector field $V$ is the function
$\phi(V) = \sum f_i v_i.$

---

*Solution:*

By linearity, expand 

```{math}
:enumerated: false

\begin{align}
\phi(V) &= \left(\sum f_i dx_i\right) \left(\sum v_j U_j\right) \\
    &= \sum f_i dx_i \left(\sum v_j U_j\right) \\
    &= \sum_{(i, j)} f_i v_j dx_i (U_j) \\
    &= \sum_{(i, j)} f_i v_j U_j[x_i] \\
    &= \sum_{(i, j)} f_i v_j \pd{x_i}{x_j} \\
    &= \sum_{(i, j)} f_i v_j \delta_{ij} \\
    &= \sum_i f_i v_i. \;\square
\end{align}
```

### Exercise 4

Express the following differentials in terms of $df$:

(a) $d(f^5).$

(b) $d(\sqrt{f}),$ where $f > 0,$

(c) $d(\log{(1 + f^2)}).$

---

*Solution:*

Let's check one with the definition for an arbitrary vector field $V$ first.

(a)

```{math}
:enumerated: false
d(f^5)(V) = V[f^5] = \sum v_i \pd{(f^5)}{x^i} = \sum v_i 5f^4 \pd {f}{x^i} = 5f^4 V[f] = 5f^4 df(V),
```
so

```{math}
:enumerated: false

\bx{d(f^5) =  5f^4df},
```

using the vector field version of Lemma 3.2 and the usual chain rule. Going forward apply
Lemma 5.7 which is effectively the calculation above in the general case.

(b) 

```{math}
:enumerated: false
    d(\sqrt{f}) = \bx{{\frac{1}{2}f^{-1/2}df}}.

```

(c)

```{math}
:enumerated: false

d(\log{(1 + f^2)}) = \bx{\frac{2f}{1 + f^2}df}.
```

### Exercise 6

In each case compute the differential of $f$ and find the directional derivative
$\v{v}_p[f]$, for $\v{v}_p$ as in Exercise 1.

(a) $f = xy^2 - yz^2.$

(b) $f = xe^{yz}$.

(c) $f = \sin{(xy)}\cos{(xz)}.$

---

*Solution:*

(a)

```{math}
:enumerated: false

df = d(xy^2 - yz^2) = y^2dx + (2xy - z^2)dy - 2yzdz.
```

We can treat $V = (1, 2, -3)$ as a constant vector field and apply the result of problem 2, so that with 

$\v{p} = (0, -2, 1)$, 

```{math}
:enumerated: false

\begin{align}
\v{v}_p[f] = df(V)(\v{p}) &= 1 \cdot y^2(\v{p}) + 2 \cdot (2xy - z^2)(\v{p}) - 3 \cdot(-2yz)(\v{p}).\\
    &= 1 \cdot 4 + 2 \cdot -1 - 3 \cdot 4 = \bx{-10}.
\end{align}
```

(b)

```{math}
:enumerated: false

df = d(xe^{yz}) = e^{yz}dx + xze^{yz}dy + xye^{yz}dz.
```

At $\v{p}$, $e^{yz} = e^{-2}$, so $df = -2dx,$ and

```{math}
:enumerated: false
\v{v}_p[f] = \bx{-2}.

```

(c)

```{math}
:enumerated: false
\begin{align}
df &= d(\sin{(xy)}\cos{(xz)})  \\
&= \sin{(xy)}d\cos{(xz)} + \cos{(xz)}d\sin{(xy)} \\
    &= -\sin{(xy)}\sin{(xz)}(zdx + xdz) + \cos{(xy)}\cos{(xz)}(ydx + xdy) \\
    &= (y\cos{(xy)}\cos{(xz) - z\sin{(xy)}\sin{(xz)})}dx + x\cos{(xy)}\cos{(xz)}dy - x\sin{(xy)}\sin{(xz)}dz. 
\end{align}
```

With $x = 0$ each term is $0$ except the first, so $df = ydx$ and 

```{math}
:enumerated: false

\v{v}_p[f] = \bx{-4}.
```

### Exercise 8

Prove Lemma 5.6 directly from the definition of $d$.

---

*Solution:*

We need $d(fg)(\v{v}_p) = f(\v{p})dg(\v{v}_p) + g(\v{p})df(\v{v}_p)$ for $\v{p}\in\R^3, \v{v}_p \in T_p(\R^3),$ or,
using the definition,

```{math}
:enumerated: false
\v{v}_p[fg] = f(\v{p})\v{v}_p[g] + g(\v{p})\v{v}_p[f].
```

But

```{math}
:enumerated: false

\v{v}_p[fg] &= v_1 \pd{fg}{x}(\v{p}) + v_2 \pd{fg}{y}(\v{p}) + v_3\pd{fg}{z}(\v{p}) \\
    &= \sum v_i \left(f(\v{p}) \pd{g}{x_i}(\v{p}) + g(\v{p}) \pd{f}{x_i}(\v{p})\right) \\
    &= f(\v{p}) \sum v_i \pd{g}{x_i}(\v{p}) + g(\v{p}) \sum v_i \pd{f}{x_i}(\v{p}) \\
    &= f(\v{p})\v{v}_p[g] + g(\v{p})\v{v}_p[f],
```

as desired. $\square$

### Exercise 10

Prove that the local minima and local maxima of a function $f$ are critical points of $f$.

---

*Solution:*

Critical points, as in Exercise 9, are those points $\v{p}$ such that $df = 0$ at $\v{p}$ (i.e. $df(\v{v}_p) = 0 \; \text{for all } \v{v}_p \in T_p$).
Suppose that $df \neq 0$ at $\v{p}$, so there is some $\v{v}_p$ such that $df(\v{v}_p) \neq 0$. Suppose without loss of generality that $df(\v{v}_p) = a > 0$. This is the derivative
of a real-valued function $h(t)$ at $0$, so there exists $d$ such that 

```{math}
:enumerated: false


\frac{h(\delta) - h(0)}{\delta} > \frac{a}{2},
```
 so $h(\delta) > a\delta/2 + h(0)$.
In particular, $h(0) = f(\v{p})$ is not at a local maximum. By taking $-\delta$, we can see that $f(\v{p})$ is also not at a local minimum, so $\v{p}$ 
is neither a local minimum nor a local maximum of $f$, as desired. $\square$

## Exercises 1.6

### Exercise 2

Let $\phi = dx/y$ and $\psi = z\,dy$. Check the Leibnizian formula (3) of Theorem 6.4 in this case by computing each term separately.

---

*Solution:*

From definitions (actually the comment above Definition 6.3),
```{math}
:enumerated: false

d(\phi \wedge \psi) &= d\left(\frac{z}{y}\,dx\,dy\right) \\
    &= d\left(\frac{z}{y}\right) dx\,dy \\
    &= \left(\frac{-z}{y^2}dy + \frac{1}{y}dz\right)dx\,dy \\
    &= \frac{1}{y}dx\,dy\,dz,
```

since there are two changes of sign moving $dz$ to the end. By Theorem 6.4, 

```{math}
:enumerated: false

d(\phi \wedge \psi) &= d\phi \wedge \psi - \phi \wedge d\psi \\
    &= \frac{-1}{y^2}dy \wedge z dy - \frac{1}{y}dx \wedge dzdy \\
    &= \frac{1}{y}\,dx\,dy\,dz,
```

as desired. $\square$

### Exercise 4

Simplify the following forms:

(a) $d(f\,dg + g\,df).$

(b) $d((f - g)(df + dg)).$

(c) $d(f\,dg \wedge g\,df).$

(d) $d(gf\,df) + d(f\,dg).$

---

*Solution:*

(a) $d(f\,dg + g\,df) = d(d(fg)) = \bx{0},$

using Theorem 6.4 and Ex. 3.

(b) $d((f - g)(df + dg)) = df \wedge df + df \wedge dg - dg \wedge df - dg \wedge dg = \bx{2\,df \wedge dg}.$

(c) $d(f\,dg \wedge g\,df) = d(df\wedge dg \wedge g\,df - f\,dg \wedge dg \wedge g\,df) = \bx{0}.$

(d) 

```{math}
:enumerated: false


d(gf\,df) + d(f\,dg) &= d(gf) \wedge df + df \wedge dg \\
    &= f\,dg \wedge df + df \wedge dg   \\
    &= \bx{(1 - f)\,df \wedge dg}.
```

### Exercise 6

If $r, \vartheta, z$ are the cylindrical coordinate functions in $\R^3$, then $x = r \cos \vartheta$,
$y = r \sin \vartheta, z = z$. Compute the *volume element* $dx\,dy\,dz$ in terms of the functions
$r, \vartheta, z$ and their differentials.

---

*Solution:*

```{math}
:enumerated: false

dx = \cos \vartheta dr - r\sin \vartheta d\vartheta,\\
dy = \sin \vartheta dr + r\cos \vartheta d\vartheta,
```

so

```{math}
:enumerated: false

dx\,dy\,dz &= (\cos \vartheta dr - r\sin \vartheta d\vartheta) \wedge (\sin \vartheta dr + r\cos \vartheta d\vartheta) \, dz \\
    &= (r \cos^2 \vartheta dr\,d\vartheta + r\sin^2 \vartheta dr\,d\vartheta)\,dz \\
    &= \bx{r\,dr\,d\vartheta\,dz}.

```

### Exercise 8

Classical *vector analysis* avoids the use of differential forms on $\R^3$ by converting 1-forms and 2-forms into
vector fields by means of the following one-to-one correspondences:

```{math}
:enumerated: false

\sum f_i dx_i \overset{(1)}{\leftrightarrow} \sum f_i U_i \overset{(2)}{\leftrightarrow} f_3 dx_1 dx_2- f_2 dx_1 dx_3 + f_1 dx_2 dx_3.

```

Vector analysis uses three basic operations based on partial differentiation.

- *Gradient* of a function $f$:

```{math}
:enumerated: false

\text{grad}\,f = \sum \pd{f}{x_i}U_i.
```

- *Curl* of a vector field $V = \sum f_i U_i$:

```{math}
:enumerated: false

\text{curl}\,f = \left(\pd{f_3}{x_2} - \pd{f_2}{x_3}\right)U_1 + \left(\pd{f_1}{x_3} - \pd{f_3}{x_1}\right)U_2 + \left(\pd{f_2}{x_1} - \pd{f_1}{x_2}\right)U_3.
```

- *Divergence* of a vector field $V = \sum f_i U_i$:

```{math}
:enumerated: false

\text{div}\,V = \sum \pd{f_i}{x_i}.
```

Prove that all three operations may be expressed by exterior derivatives as follows:

(a) $df \overset{(1)}\leftrightarrow \text{grad}\,f.$

(b) If $\phi \overset{(1)}\leftrightarrow V$, then $d\phi \overset{(2)}{\leftrightarrow} \text{curl}\,V.$

(c) If $\eta \overset{(2)}\leftrightarrow V$, then $d\eta = (\text{div}\,V)\,dx\,dy\,dz.$

---

*Solution:*

(a) $df = \sum \pd{f_i}{x_i}dx_i \overset{(1)}\leftrightarrow \sum \pd{f_i}{x_i}U_i = \text{grad}\,f.$

(b) Suppose $\phi = \sum f_idx_i$ and $V = \sum f_iU_i$. Then calculate $d\phi$:

```{math}
:enumerated: false

d\phi = &\sum df_i dx_i \\
    = &\sum_i \sum_j \pd{f_i}{x_j}dx_jdx_i \\
    = &\pd{f_2}{x_1} dx_1dx_2 + \pd{f_3}{x_1} dx_1dx_3 + \pd{f_3}{x_2} dx_2dx_3 \\
    +&\pd{f_1}{x_2} dx_2dx_1 + \pd{f_1}{x_3} dx_3dx_1 + \pd{f_2}{x_3} dx_3dx_2 \\
    = &\pd{f_2}{x_1} dx_1dx_2 + \pd{f_3}{x_1} dx_1dx_3 + \pd{f_3}{x_2} dx_2dx_3 \\
    -&\pd{f_1}{x_2} dx_1dx_2 - \pd{f_1}{x_3} dx_1dx_3 - \pd{f_2}{x_3} dx_2dx_3 \\
    \overset{(2)}\leftrightarrow &\text{curl}\,V.
```

(c) Suppose $\eta = f_1dx_2dx_3 + f_2dx_3dx_1 + f_3dx_1dx_2 \overset{(2)}\leftrightarrow V$. Calculate $d\eta$:

```{math}
:enumerated: false

d\eta &= df_1dy\,dz + df_2dz\,dx + df_3dx\,dy \\
    &= \pd{f_1}{x}dx\,dy\,dz + \pd{f_2}{y}dy\,dz\,dx + \pd{f_3}{z}dz\,dx\,dy \\
    &= \text{div}\,V dx\,dy\,dz.
```

## Exercises 1.7

### Exercise 2

$F(u, v) = (u^2 - v^2, 2uv)$.

(a) Sketch the horizontal line $v = 1$ and its image under $F$ (a parabola).

(b) Do the same for the vertical $u = 1$.

(c) Describe the image of the unit square $0 \leq u, v \leq 1$ under $F$.

---

*Solution:*

See code (eventually) for a and b. We will follow the boundary of the unit square counterclockwise from the origin. For $v = 0$, $0 \leq u \leq 1$ traces its own image.
Then at $u = 1$, we trace the curve $(1 - v^2, 2v)$, $0 \leq v \leq 1$, a left-facing parabola terminating at $(0, 2).$ Now with $v=1$, Let $t =  1 - u$ and as $0 \leq t \leq 1$
we trace the curve $(t^2 - 2t, 2 - 2t)$, which is a right-facing parabola with vertex at $(-1, 0)$. Finally with $u = 0$ we trace the line back to the origin. So the figure is a pointed
arch with bilateral symmetry above the line $[(-1, 0), (1, 0)]$ with the upper boundary formed from parabolic segments as described. $\square$

### Exercise 4

Find a formula for the Jacobian matrix of $F$ at all points, and deduce that $F*_p$ is a linear isomorphism at all every point of $R^2$ except the origin.

---

*Solution:*

Recall the formula for the Jacobian,

```{math}
:enumerated: false

J = \left(\pd{f_i}{x_j}\right)_{i,j}.
```

Calculate to obtain

```{math}
:enumerated: false

J = \left(
\begin{matrix}
2u & -2v \\
2v & 2u
\end{matrix}\right).
```

The determinant is $4u^2 + 4v^2$, which is nonzero except at the origin, meaning $J$ is non-singular except at the origin.
Nonsingularity, invertibility, and linear isomorphism are synonymous in the case of finite-dimensional linear operators.

*Note:* The mapping is the holomorphic complex map $z \mapsto z^2$.

### Exercise 6

Give an example to demonstrate that a one-to-one and onto mapping need not be diffeomorphic.

---

*Solution:*

Let $F(x) = x^3$, then $F^{-1}(y) = y^{1/3}$, which is not differentiable at $0$. $\square$

### Exercise 8

In the definition of the tangent map (Def 7.4), the straight line $t = \v{p} + t\v{v}$ can be replaced
by any curve $\alpha$ with initial velocity $\v{v}_p$.

---

*Solution:* Thankfully this problem left out the "prove". There's nothing to do anyway, this is a repeat of problem 6 from
Section 1.4, and that one was the trivial observation that Lemma 4.6 can be taken as a definition. The mapping version just
requires a repetition of the same notation. $\square$

### Exercise 10

Show (in two ways) that the map $F: \R^2 \rightarrow \R^2$ such that $F(u, v) = (ve^u, 2u)$ is a diffeomorphism.

(a) Prove that it is one-to-one, onto, and regular.

(b) Find a formula for its inverse $F^{-1}:\R^2 \rightarrow \R^2$ an observe that $F^{-1}$ is differentiable. Verify the formula
by checking that $FF^{-1}$ and $F^{-1}F$ are identity maps.

---

*Solution:*

(a) Suppose $(x, y) = (ve^u, 2u)$. Then $u = y/2$ and $v = x e^{-y/2}$, so $F$ is one-to-one. This same formula demonstrates that $F$ is onto since the expressions
are well-defined for all $u, v$. Finally, the Jacobian

```{math}
:enumerated: false

J = \left(\begin{matrix}
ve^u & e^u \\
2 & 0
\end{matrix}\right)
```

has determinant $-2e^u \neq 0$, so is nonsingular and $F$ is regular. By the inverse mapping theorem, there is a differentiable local inverse function
in a neighborhood each point which must be the function $F^{-1}$, which
is therefore itself a mapping, and therefore $F$ is a diffeomorphism.

(b) See above for $F^{-1}(x, y) = (y/2, xe^{-y/2})$, which is differentiable. I'm not doing the rest, don't insult me like that bro.

