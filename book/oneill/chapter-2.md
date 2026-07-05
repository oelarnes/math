---
kernelspec:
  name: python3
  language: python
  display_name: Python 3
---

# Chapter 2

## Exercises 2.1

### Exercise 2

Prove that Euclidean distance has the properties

(a) $d(\v{p}, \v{q}) \geq 0$; $d(\v{p}, \v{q}) = 0$ if and only if $\v{p} = \v{q}$.

(b) $d(\v{p}, \v{q}) = d(\v{q}, \v{p})$.

(c) $d(\v{p}, \v{q}) + d(\v{q}, \v{r}) \geq d(\v{p}, \v{r})$ for any $\v{p}, \v{q}, \v{r}$ in $\R^3$.

---

*Solution:*

(a) Recall that $d(\v{p}, \v{q}) = \|p-q\|$. Of course the symbol indicates that it is a norm with the desired properties, 
    but let's check. If $\v{a} = \v{p} - \v{q},$ then $\|a\| = \sqrt{\sum{a_i^2}} \geq 0,$ and it is zero only when each
    $a_i = 0$, that is when $\v{p} = \v{q}$ as desired.

(b) Following the above, we see that $\sqrt{\sum{a_i^2}} = \sqrt{\sum{(-a_i)^2}}$, which implies the desired result.

(c) Let $\v{a}$ be as before and $\v{b} = \v{q} - \v{r}.$ Then we need

```{math}
:enumerated: false

\sqrt{\v{a} \cdot \v{a}} + \sqrt{\v{b} \cdot \v{b}} \geq \sqrt{(\v{a} + \v{b}) \cdot (\v{a} + \v{b})}.
```

Squaring both sides (since all terms are non-negative), we need

```{math}
:enumerated: false

\v{a} \cdot \v{a} + \v{b} \cdot \v{b} + 2\sqrt{(\v{a}\cdot\v{a})( \v{b}\cdot\v{b})} \geq (\v{a} + \v{b}) \cdot (\v{a} + \v{b}) = \v{a} \cdot \v{a} + \v{b} \cdot \v{b} + 2 \v{a} \cdot \v{b},
```

so

```{math}
:enumerated: false

\|a\|\|b\| \geq \v{a} \cdot \v{b},
```

which is the Cauchy-Schwarz inequality, as used in the text. To prove the inequality, extend $a$ into a orthonormal basis to see that $\v{a} \cdot \v{b}$ is maximized for $\v{b} = r\v{a}$. $\square$

(ex-2-1-4)=
### Exercise 4

Let $\v{u} = (u_1, u_2, u_3), \v{v} = (v_1, v_2, v_3), \v{w} = (w_1, w_2, w_3)$. Prove that 

(a) 
```{math}
:enumerated: false

\v{u} \cdot \v{v} \times \v{w} = 
\begin{vmatrix}
u_1 &u_2 &u_3 \\
v_1 &v_2 &v_3 \\
w_1 &w_2 &w_3 \\
\end{vmatrix}.
```

(b) $\v{u} \cdot \v{v} \times \v{w} \neq 0$ if and only if $\v{u}, \v{v},$ and $\v{w}$ are linearly independent.

(c) If any two vectors in $\v{u} \cdot \v{v} \times \v{w}$ are reversed, the product changes sign.

(d) $\v{u} \cdot \v{v} \times \v{w} = \v{u} \times \v{v} \cdot \v{w}$.

---

*Solution:*

(a)
```{math}
:enumerated: false

\v{u} \cdot \v{v} \times \v{w} = (u_1U_1 + u_2U_2 + u_3U_3) \cdot \begin{vmatrix}
U_1 &U_2 &U_3 \\
v_1 &v_2 &v_3 \\
w_1 &w_2 &w_3 \\
\end{vmatrix},
```

and formally the dot product substitutes the coefficients $u_i$ for the vectors $U_i$ in the RHS,
giving the desired result.

(b) The determinant of a matrix being zero is known from linear algebra to be equivalent to the matrix being singular,
    that is, its row or column vectors being linearly dependent. So the desired statement follow from (a).

(c) Reversing two vectors in the formula corresponds to transposing two rows in the matrix form. The permutation form of the determinant is
    given by

```{math}
:enumerated: false

\det(A) = \sum_{\sigma\in S_n} \text{sgn}(\sigma)\prod{a_{i, \sigma(i)}},
```

where the sign function is determined by writing the permutation as a product of transpositions and counting the parity.
Exchanging rows in a matrix corresponds to a single transposition compounded to each permutation in $S_n$. Therefore the sign of each permutation is flipped and

```{math}
:enumerated: false

\begin{vmatrix}
u_1 &u_2 &u_3 \\
v_1 &v_2 &v_3 \\
w_1 &w_2 &w_3 \\
\end{vmatrix} = -

\begin{vmatrix}
v_1 &v_2 &v_3 \\
u_1 &u_2 &u_3 \\
w_1 &w_2 &w_3 \\
\end{vmatrix},

```

and so on.

(d) Exchange $\v{u}$ and $\v{w}$, then exchange $\v{w}$ and $\v{v}$, and apply (c). $\square$

*Note:* This set of results (possibly) becomes more intuitive using the (multi-)vector product $\v{u}\v{v} = \v{u} \cdot \v{v} + \v{u} \wedge \v{v}$
    and considering the volume term of the product $\v{u}\v{v}\v{w}$.

### Exercise 6

If $\v{e}_1, \v{e}_2, \v{e}_3$ is a frame, show that

```{math}
:enumerated: false

\v{e}_1 \cdot \v{e}_2 \times \v{e}_3 = \pm 1.
```

Deduce that any orthogonal matrix has determinant $\pm 1$.

---

*Solution:*

$\v{e}_2 \times \v{e}_3$ is a vector orthogonal to $\v{e}_2$ and $\v{e}_3$ with magnitude $\|e_2\|\|e_3\| = 1$ since the vectors are orthogonal.
In $\R^3$ there is a unique orthogonal space so the unit vector must be $\pm \v{e}_1$, and $\pm \v{e}_1 \cdot \v{e}_1 = \pm 1$. By [Exercise 4(a)](#ex-2-1-4),
the orthogonal matrix with rows $\v{e}_i$ has determinant $\pm 1$. $\square$

### Exercise 8

Prove: the volume of the parallelepiped with sides $\v{u}, \v{v}, \v{w}$ is $\pm \v{u} \cdot \v{v} \times \v{w}$.

---

*Proof:* This is known to be given by the determinant according to [Exercise 4](#ex-2-1-4). Proceeding geometrically using the property that areas and volumes are invariant
under shear transformations, first note that the norm of the cross product $\v{z} = \v{v} \times \v{w}$ is

```{math}
:enumerated: false

\|\v{z}\| = \|\v{v}\|\|\v{w}\|\sin(\th{\v{v}\v{w}}), 
```

the area of the parallelogram
spanned by $\v{v}$ and $\v{w}$. Then the height of the paralellepiped is the component of $\v{u}$ in the $\pm\v{z}$ direction, since that is normal to the plane
of the base. That component is $\v{u} \cdot (\pm \v{z} / \|\v{z}\|)$, giving a volume, using base times height, of

```{math}
:enumerated: false

V &= \pm \v{u} \cdot \frac{\v{z}}{\|\v{z}\|} \|\v{z}\| \\
    &= \pm \v{u} \cdot \v{v} \times \v{w},
```

as desired. $\square$

### Exercise 10

In each case, let $S$ be the set of all points $\v{p}$ that satisfy the given condition. Describe $S$, and decide whether it is *open*.

(a) $p_1^2 + p_2^2 + p_3^2 = 1$.

(b) $p_3 \neq 0$.

(c) $p_1 = p_2 \neq p_3.$

(d) $p_1^2 + p_2^2 < 9$.

---

*Solution:*

(a) This describes the unit sphere, since the Euclidean distance of $\v{p}$ from the origin is fixed at one. For $\v{p}$ and given $\epsilon$, the point $(1 + \epsilon)\v{p}$
has distance $1 + \epsilon$ from the origin and is not in $S$, but is found arbitrarily close to $\v{p}$, so $S$ is not open.

(b) $p_3 = 0$ defines a plane, so $p_3 \neq 0$ is the complement of that plane, the two open half-spaces above and below. They are open because for $\v{p} = (p_1, p_2, p_3)$ with
$p_3 \neq 0$, if $\epsilon = p_3 / 2$, for $\v{z} \in \mathcal{N}_\epsilon, z_3 > p_3 / 2$ and $\v{z} \in S$. 

(c) $p_1 = p_2$ is a plane consisting of points $(u, u, v)$ for parameters $u, v$. Then as in (b), after intersecting with $p_2 \neq p_3$, this plane is divided into two open half-planes about the line $(t, t, t)$. However,
despite my describing $S$ as consisting of open half-planes, it is not an open set in $\R^3$ since a given $\epsilon$-ball contains the points e.g. $(u, u+\epsilon/2, v)$, which are not in $S$.

(d) This is a cylinder of radius $3$ about the $z$-axis, and is open since for a given point in the set there is some finite distance to the boundary which $\mathcal{N}_\epsilon$ can fit within.


### Exercise 12

Let $f$ and $g$ be differentiable real-valued functions on an interval $I$. Suppose that $f^2 + g^2 = 1$ and that
$\th_0$ is a number such that $f(0) = \cos\th_0$ and $g(0) = \sin\th_0$. If $\th$ is the function such that

```{math}
:enumerated: false

\th(t) = \th + \int_0^t (fg' - gf') du,
```

prove that

```{math}
:enumerated: false

f = \cos\th, g = \sin\th.
```

---

*Solution:*

Note that $ff' + gg' = 0$ by differentiating the relation $f^2 + g^2 = 1$. Following the hint, calculate by the chain rule and collecting like terms.

```{math}
:enumerated: false

\frac{1}{2}\frac{d}{dt}\left((f - \cos\th)^2 + (g - \sin\th)^2\right) \\
=(f - \cos\th)(f' + \sin\th (fg' - gf')) + (g - \sin\th)(g' - \cos\th (fg' - gf')) \\
=ff' + gg' + (ffg' - fgf' - g')\sin\th + (ggf' - gfg' - f')\cos\th \\
= ((1-gg)g' - fgf' - g')\sin\th + ((1-ff)f' - gfg' - f')\cos\th \\
= ((g' - g') - (ff' + gg')g)\sin\th + ((f' - f') - (ff' + gg')f)\cos\th \\
= 0.

```
The initial conditions are chosen so that the differential equation implies the functions are equal for all $t \in I$, and the statement is proved. $\square$

## Exercises 2.2

### Exercise 2

Show that a curve has **constant speed** if and only if its acceleration is
everywhere orthogonal to its velocity.

---

*Solution:*

The square of the speed of a curve $\alpha$ is given by $\alpha' \cdot \alpha'$, which is constant (thus the speed is constant) if and only if $(\alpha' \cdot \alpha')' = 0$. By the Leibniz property,

```{math}
:enumerated: false

(\alpha' \cdot \alpha')' = \alpha'' \cdot \alpha' + \alpha' \cdot \alpha'' = 2\,\alpha'' \cdot \alpha',
```

which is zero if and only if the acceleration $\alpha''$ is orthogonal to the velocity $\alpha'$, as desired. $\square$

---

### Exercise 4

Consider the curve $\alpha(t) = (2t,\; t^2,\; \log t)$ on $I\colon t > 0$.

(a) Show that $\alpha$ passes through the points $p = (2, 1, 0)$ and
$q = (4, 4, \log 2)$.

(b) Find the arc length of $\alpha$ between $p$ and $q$.

---

*Solution:*

(a) Evaluate at $t = 1$ and $t = 2$.

(b) The arc length is given by

```{math}
:enumerated: false

\int_1^2 \|\alpha'(t)\|\, dt
  &= \int_1^2 \sqrt{(2, 2t, \tfrac{1}{t}) \cdot (2, 2t, \tfrac{1}{t})}\, dt \\
  &= \int_1^2 \sqrt{4 + 4t^2 + \frac{1}{t^2}}\, dt \\
  &= \int_1^2 \sqrt{\left(2t + \frac{1}{t}\right)^2}\, dt \\
  &= \int_1^2 2t + \frac{1}{t}\, dt \quad (\text{since } t > 0) \\
  &= \left[t^2 + \log t\right]_1^2 \\
  &= \bx{3 + \log 2}.
```

---

### Exercise 6

Let $Y$ be a vector field on the helix $\alpha(t) = (\cos t,\; \sin t,\; t)$.
In each case below, express $Y$ in the form $\sum_i y_i U_i$.

(a) $Y(t)$ is the vector from $\alpha(t)$ to the origin of $\R^3$.

(b) $Y(t) = \alpha'(t) - \alpha''(t)$.

(c) $Y(t)$ has unit length and is orthogonal to both $\alpha'(t)$ and $\alpha''(t)$.

(d) $Y(t)$ is the vector from $\alpha(t)$ to $\alpha(t + \pi)$.

---

*Solution:*

(a)

```{math}
:enumerated: false

Y(t) &= 0 - \alpha(t) \\
     &= \bx{-\cos t\, U_1 - \sin t\, U_2 - t\, U_3}.
```

(b) $\alpha' = (-\sin t, \cos t, 1)$ and $\alpha'' = (-\cos t, -\sin t, 0)$, so

```{math}
:enumerated: false

Y(t) = \bx{(\cos t - \sin t)\, U_1 + (\cos t + \sin t)\, U_2 + U_3}.
```

(c) Let $Y(t) = \frac{\alpha'(t) \times \alpha''(t)}{\|\alpha'(t) \times \alpha''(t)\|}$, which has the desired property by Lemma 2.1.8. Using the definition, with $Z = \|\alpha'(t) \times \alpha''(t)\|$,

```{math}
:enumerated: false

Y(t) &= \frac{1}{Z}\begin{vmatrix} U_1 & U_2 & U_3 \\ -\sin t & \cos t & 1 \\ -\cos t & -\sin t & 0 \end{vmatrix} \\
     &= \frac{\sin t\, U_1 - \cos t\, U_2 + U_3}{\sqrt{\sin^2 t + \cos^2 t + 1}} \\
     &= \bx{\frac{\sqrt{2}}{2}\sin t\, U_1 - \frac{\sqrt{2}}{2}\cos t\, U_2 + \frac{\sqrt{2}}{2}\, U_3}.
```

(d)

```{math}
:enumerated: false

Y(t) &= \alpha(t + \pi) - \alpha(t) \\
     &= (\cos(t+\pi) - \cos t,\ \sin(t+\pi) - \sin t,\ t+\pi-t) \\
     &= \bx{-2\cos t\, U_1 - 2\sin t\, U_2 + \pi\, U_3}.
```

*Notes:*

```{code-cell} python3
# Exercise 2.2.6 — vector fields on the helix
# Written with Claude
import numpy as np
import plotly.graph_objects as go
from plot_dg import (
    dg_figure, make_curve_trace, make_point_trace,
    make_vector_traces, make_frame_traces,
    apply_animation_layout, case_visibility_buttons, traces_to_frame_data,
)

# --- problem definitions ---
def alpha(t):    return np.array([np.cos(t), np.sin(t), t])
def alpha_p(t):  return np.array([-np.sin(t), np.cos(t), 1.0])
def alpha_pp(t): return np.array([-np.cos(t), -np.sin(t), 0.0])

sq2 = np.sqrt(2) / 2
Y_FNS = {
    'a': lambda t: np.array([-np.cos(t), -np.sin(t), -t]),
    'b': lambda t: np.array([np.cos(t) - np.sin(t), np.cos(t) + np.sin(t), 1.0]),
    'c': lambda t: np.array([sq2*np.sin(t), -sq2*np.cos(t), sq2]),
    'd': lambda t: np.array([-2*np.cos(t), -2*np.sin(t), np.pi]),
}
PARTS = list(Y_FNS)
PART_COLOR = {'a': 'gold', 'b': 'darkorange', 'c': 'plum', 'd': 'cyan'}
USES_FRAME = {'a': False, 'b': True, 'c': True, 'd': False}

# --- traces ---
n_frames = 48
t_vals = np.linspace(0, 2*np.pi, n_frames, endpoint=False)
s_dense = np.linspace(0, 2*np.pi, 200)
helix_pts = np.column_stack([np.cos(s_dense), np.sin(s_dense), s_dense])

# Trace layout: helix, α(t), [coord frame at origin × 3], α', α'', [Y_p × 4]
def build_traces(t):
    a = alpha(t)
    out = [
        make_curve_trace(helix_pts, color='steelblue', width=4),
        make_point_trace(a, color='crimson', size=5),
    ]
    out += make_frame_traces(base=[0, 0, 0], scale=0.6)
    out += make_vector_traces(alpha_p(t),  base=a, color='lightskyblue', cone_scale=0.12, line_width=3)
    out += make_vector_traces(alpha_pp(t), base=a, color='palegreen',    cone_scale=0.12, line_width=3)
    for p in PARTS:
        out += make_vector_traces(Y_FNS[p](t), base=a, color=PART_COLOR[p], cone_scale=0.18)
    return out

def vis_pattern(part):
    pat = [True, True] + [True] * 6      # helix, point, coordinate frame
    pat += [USES_FRAME[part]] * 4         # α', α''
    for p in PARTS:
        pat += [p == part] * 2            # Y_p
    return pat

# --- assemble figure ---
fig = dg_figure(xlim=(-3, 3), ylim=(-3, 3), zlim=(-2, 8))
initial = build_traces(t_vals[0])
for tr, vis in zip(initial, vis_pattern('a')):
    tr.update(visible=vis)
for tr in initial:
    fig.add_trace(tr)

fig.frames = [
    go.Frame(name=str(i), data=traces_to_frame_data(build_traces(t)))
    for i, t in enumerate(t_vals)
]

apply_animation_layout(
    fig,
    case_buttons=case_visibility_buttons(PARTS, vis_pattern),
    n_frames=n_frames,
)
fig.show()
```

### Exercise 8

Let $Y$ be a vector field on a curve $\alpha$. If $\alpha(h)$ is a
reparametrization of $\alpha$, show that $Y(h)$ is a vector field on $\alpha(h)$,
and prove the **chain rule**

$$Y(h)' = h'\, Y'(h).$$

---

*Solution:*

This is formally equivalent to Lemma 1.4.5. $\square$

### Exercise 10

Let $\alpha, \beta\colon I \to \R^3$ be curves such that $\alpha'(t)$ and
$\beta'(t)$ have the same Euclidean coordinates at each $t$. Prove that
$\alpha$ and $\beta$ are **parallel**: there exists a fixed point $p \in \R^3$ such that

$$\beta(t) = \alpha(t) + p \qquad \text{for all } t \in I.$$

---

*Solution:*

Apply the fundamental theorem of calculus to each coordinate function. $\square$

## Exercises 2.3

### Exercise 2

Consider the curve

```{math}
:enumerated: false

\beta(s) = \left(\frac{(1+s)^{3/2}}{3},\; \frac{(1-s)^{3/2}}{3},\; \frac{s}{\sqrt{2}}\right)
```

defined on $I\colon -1 < s < 1$. Show that $\beta$ has unit speed, and compute its Frenet apparatus.

---
*Solution:*

Calculate

```{math}
:enumerated: false

\|\beta'(s)\|^2 &= \beta'(s) \cdot \beta'(s) \\
    &= \left(\frac{(1+s)^{1/2}}{2}, -\frac{(1-s)^{1/2}}{2}, 
        \frac{1}{\sqrt{2}}\right) \cdot \left(\frac{(1+s)^{1/2}}{2}, 
        -\frac{(1-s)^{1/2}}{2}, \frac{1}{\sqrt{2}}\right) \\
    &= \frac{1+s}{4} + \frac{1-s}{4} + \frac{1}{2} = 1,\\
```
where the square roots are positive on the interval $I$. So $\beta$ has unit speed. Then

```{math}
:enumerated: false

T &= \bx{\left(\frac{\sqrt{1+s}}{2}, -\frac{\sqrt{1-s}}{2}, \frac{1}{\sqrt{2}}\right)},\\
T' &= \left(\frac{1}{4\sqrt{1+s}}, \frac{1}{4\sqrt{1-s}}, 0\right),\\
\|T'\|^2 &= \frac{1}{16(1+s)} + \frac{1}{16(1-s)} \\
    &= \frac{1}{8(1-s^2)},
```
so $1/\kappa = 2\sqrt{2-2s^2}$, and 

```{math}
:enumerated: false

N = \bx{\left(\sqrt{\frac{1-s}{2}}, \sqrt{\frac{1+s}{2}}, 0\right)}.
```
Finally, 
```{math}
:enumerated: false
B &= \begin{vmatrix}
U_1 &U_2 &U_3 \\
\frac{\sqrt{1+s}}{2} &-\frac{\sqrt{1-s}}{2} &\frac{1}{\sqrt{2}} \\
\sqrt{\frac{1-s}{2}} &\sqrt{\frac{1+s}{2}} &0 \\
\end{vmatrix} \\
    &= \bx{\left(-\frac{\sqrt{1+s}}{2}, \frac{\sqrt{1-s}}{2}, \frac{1}{\sqrt{2}}\right)}.
```

### Exercise 4

Prove that

```{math}
:enumerated: false

T &= N \times B = -B \times N, \\
N &= B \times T = -T \times B, \\
B &= T \times N = -N \times T.
```

(A formal proof uses properties of the cross product established in the Exercises of Section 1—but one can recall these formulas by using the right-hand rule given at the end of that section.)

---
*Solution:*

We know that $T, N$ and $B$ are unit vectors, as are their cross-products (since they are mutually orthogonal), so if any pair $u, v$ has $u \cdot v = 1$, then
$u = v$.

```{math}
:enumerated: false

B \cdot T \times N = B \cdot B = 1,
```
since $B = T \times N$ by definition. Recall from [Exercise 2.1.4(c)](#ex-2-1-4) that reversing any vectors in the triple product expression above reverses the sign, which immediately gives
the alternating sign property. So we need to check the remaining pairs using the same property. We have

```{math}
:enumerated: false

N \cdot B \times T &= -B \cdot N \times T \\
    &= B \cdot T \times N \\
    &= B \cdot B \\
    &= 1
```
and

```{math}
:enumerated: false

T \cdot N \times B &= - N \cdot T \times B\\
&= N \cdot B \times T \\
&= N \cdot N \\
&= 1,
```
as required. Note that this set of properties holds for any orthonormal frame, justifying the future use of the right-hand rule to establish these relations in analagous settings,
once we verify things on our fingers, noting that a cycle in three dimensions, rotating each vector to a new position, is an even permutation. $\square$

### Exercise 6

A unit-speed parametrization of a circle may be written

```{math}
:enumerated: false

\gamma(s) = \v{c} + r\cos\frac{s}{r}\,\v{e}_1 + r\sin\frac{s}{r}\,\v{e}_2,
```

where $\v{e}_i \cdot \v{e}_j = \delta_{ij}$.

If $\beta$ is a unit-speed curve with $\kappa(0) > 0$, prove that there is one and only one circle $\gamma$ that approximates $\beta$ near $\beta(0)$ in the sense that

$$\gamma(0) = \beta(0), \quad \gamma'(0) = \beta'(0), \quad \text{and} \quad \gamma''(0) = \beta''(0).$$

Show that $\gamma$ lies in the osculating plane of $\beta$ at $\beta(0)$ and find its center $\v{c}$ and radius $r$. The circle $\gamma$ is called the **osculating circle** and $\v{c}$ the **center of curvature** of $\beta$ at $\beta(0)$. (The same results hold when $0$ is replaced by any number $s$.)

---
Suppose $\gamma_1(s) = \v{c_1} + r_1\cos\frac{s}{r_1}\,\v{e}_1 + r_1\sin\frac{s}{r_1}\,\v{e}_2$ and $\gamma_2(s) = \v{c_2} + r_2\cos\frac{s}{r_2}\,\v{f}_1 + r_2\sin\frac{s}{r_2}\,\v{f}_2$ are
two curves with the desired property, then we have

```{math}
:enumerated: false

\gamma_1(0) &= \gamma_2(0) \\
\gamma_1'(0) &= \gamma_2'(0) \\
\gamma_1''(0) &= \gamma_2''(0), \\

```
so

```{math}
:enumerated: false

\v{c}_1 + r_1\v{e}_1 = \v{c}_2 + r_2\v{f}_1\\
\v{e}_2 = \v{f}_2\\
-\frac{1}{r_1}\v{e}_1 = -\frac{1}{r_2}\v{f}_1.

```
From the third equation we see that $\v{e}_1$ and $\v{f}_1$ are colinear, and since they are unit vectors,
with the further assumption that $r>0$ (or else the circle is invariant under $(r, \v{e}_1) \mapsto (-r, -\v{e}_1))$,
we see that $\v{e}_1 = \v{f}_1$ and $r_1 = r_2$. Then $\v{c}_1 = \v{c}_2$ and we already have $\v{e}_2 = \v{f}_2$.

Now since $\beta$ is a unit-speed curve, we have $T(0) = \beta'(0)$ and $N(0) = \beta''(0) / \| \beta''(0) \|$. Let $\kappa = \| \beta''(0) \|$,
then

```{math}
:enumerated: false

\kappa N = -\frac{1}{r}\v{e}_1,
```
so $r = 1 / \kappa = 1 / \|\beta''(0)\|$. We also have

```{math}
:enumerated: false

\v{c} - \frac{1}{\kappa}N = \beta(0),
```
so $\v{c} = \beta(0) + 1/\|\beta''(0)\|.$

The vectors $T(0)$ and $N(0)$ are shared by $\beta$ and $\gamma$ at $t=0$, so they have the same osculating plane,
and by Corollary 3.5, the circle is a plane curve and therefore lies entirely in its osculating plane if $\tau = 0$.
By Theorem 3.2, $N' = -\kappa T + \tau B$, and we have

```{math}
:enumerated: false

T(t) = \beta'(t) = -\sin{\frac{s}{r}}\v{e}_1 + \cos{\frac{s}{r}}\v{e}_2,\\
N(t) = -\cos {\frac{s}{r}}\v{e}_1 - \sin {\frac{s}{r}}\v{e}_2,\\
N'(t) = \frac{1}{r}\sin{\frac{s}{r}}\v{e}_1 - \frac{1}{r}\cos{\frac{s}{r}}\v{e}_2 = -\kappa T,\\
```
and therefore $\tau = 0$ as desired and we are done.$\square$

(ex-2-3-8)=
### Exercise 8

*Curves in the plane.* For a unit-speed curve $\beta(s) = (x(s), y(s))$ in $\R^2$, the unit tangent is $T = \beta' = (x', y')$ as usual, but the unit normal $N$ is defined by rotating $T$ through $+90°$, so $N = (-y', x')$. Thus $T'$ and $N$ are collinear, and the **plane curvature** $\tilde{\kappa}$ of $\beta$ is defined by the Frenet equation $T' = \tilde{\kappa}\,N$.

(a) Prove that $\tilde{\kappa} = T' \cdot N$ and $N' = -\tilde{\kappa}\,T$.

(b) The *slope angle* $\th(s)$ of $\beta$ is the differentiable function such that

$$T = (\cos\th,\, \sin\th) = \cos\th\, U_1 + \sin\th\, U_2.$$

(The existence of $\th$ derives from [Ex. 12 of Sec. 1](#ex-2-1-12).) Show that $\tilde{\kappa} = \th'$.

(c) Find the curvature $\tilde{\kappa}$ of the following plane curves.

(i) $(r\cos(s/r),\, r\sin(s/r))$, counterclockwise circle.

(ii) $(r\cos(-s/r),\, r\sin(-s/r))$, clockwise circle.

(d) Show that if $\tilde{\kappa}$ does not change sign, then $|\tilde{\kappa}|$ is the usual $\R^3$ curvature $\kappa$. (For such comparisons we can always regard $\R^2$ as, say, the $xy$ plane in $\R^3$.)

---
*Solution:*

(a) $T' \cdot N = \tilde{\kappa}N \cdot N = \tilde{\kappa}.$ Following the definitions, we have $x'' = -\kappa y'$ and $y'' = \kappa x'$, so $N' = (-y'', x'') = -\tilde\kappa(x', y') = -\tilde\kappa T$.

(b) Differentiate $T$ and observe that $T'$ has the desired form.

(c)

(i) $T = (-\sin(s/r), \cos(s/r))$, since this has unit length, so 

```{math}
:enumerated: false

T' = \tilde{\kappa} N = \left(-\frac{1}{r}\cos{\frac{s}{r}}, -\frac{1}{r}\sin{\frac{s}{r}}\right),
```
and
```{math}
:enumerated: false

N = \left(-\cos{\frac{s}{r}}, -\sin{\frac{s}{r}}\right)
```
by definition, so $\boxed{\kappa = 1/r}$.

(ii) $T = (-\sin(s/r), -\cos(s/r))$ (passing the negative sign through from the beginning), so 

```{math}
:enumerated: false

T' = \tilde{\kappa} N = \left(-\frac{1}{r}\cos{\frac{s}{r}}, \frac{1}{r}\sin{\frac{s}{r}}\right),
```
and
```{math}
:enumerated: false

N = \left(\cos{\frac{s}{r}}, -\sin{\frac{s}{r}}\right)
```
by definition, so $\boxed{\kappa = -1/r}$. Or note that whatever $\th$ we have from part (i) can be replaced by $\tilde{\th} = -\th$ giving the result by (b). Note
that the sign of $\tilde\kappa$ follows the right-hand rule bending the curve in its direction of curvature.

(d) It's unclear whether changing sign has any effect, as $\kappa$ is defined to be $\|T'\|$ for unit-speed curves and since the third component of all derivatives is zero and
    does not contribute to the norm, $\|T'\| = |\tilde\kappa|\|N\| = |\tilde\kappa|. \square$

(ex-2-3-10)=
### Exercise 10

*Spherical curves.* Let $\alpha$ be a unit-speed curve with $\kappa > 0$, $\tau \neq 0$.

(a) If $\alpha$ lies on a sphere of center $\v{c}$ and radius $r$, show that

```{math}
:enumerated: false

\alpha - \v{c} = -\rho\, N - \rho'\sigma\, B,
```

where $\rho = 1/\kappa$ and $\sigma = 1/\tau$. Thus $r^2 = \rho^2 + (\rho'\sigma)^2$.

(b) Conversely, if $\rho^2 + (\rho'\sigma)^2$ has constant value $r^2$ and $\rho' \neq 0$, show that $\alpha$ lies on a sphere of radius $r$.

(*Hint:* For (b), show that the "center curve" $\gamma = \alpha + \rho\, N + \rho'\sigma\, B$—suggested by (a)—is constant.)

---
*Solution:*

Without loss of generality, suppose $\v{c} = 0$, then
```{math}
:enumerated: false

\alpha \cdot \alpha = 0,
```
so differentiate, getting

```{math}
:enumerated: false
\alpha \cdot \alpha' = \alpha \cdot T = 0,
```

implying that the $T$ component of $\alpha$ is zero, and differeniate again to get

```{math}
:enumerated: false

\|\alpha'\|^2 + \alpha \cdot \alpha'' = 0.
```
Since $\alpha$ is unit speed, we have

```{math}
:enumerated: false

\alpha \cdot N = -\frac{1}{\kappa} = -\rho,
```

giving the desired relation to $N$. Differentiate a third time, and

```{math}
:enumerated: false

\alpha' \cdot N + \alpha \cdot N' = -\rho',
```
and since $\alpha'$ is orthogonal to $N$, using Theorem 3.2, we have

```{math}
:enumerated: false

-\kappa\left(\alpha \cdot T\right) + \tau\left( \alpha \cdot B\right) = -\rho',
```
so since again $\alpha \cdot T = 0$,

```{math}
:enumerated: false

\alpha \cdot B = -\frac{\rho'}{\tau} = -\rho'\sigma.
```

The relation $r^2 = \rho^2 + (\rho'\sigma)^2$ is then given by the definition of the sphere and the orthogonality of the components of $\alpha$.

(b) Following the hint, let $\gamma = \alpha + \rho N + \rho' \sigma B$, and differentiate, getting

```{math}
:enumerated: false

\gamma' &= \alpha' + \rho' N + \rho N' + \rho'' \sigma B + \rho' \sigma' B + \rho' \sigma B'\\
    &= T + \rho' N - \rho \kappa T + \rho \tau B + \rho'' \sigma B + \rho' \sigma' B - \rho' \sigma \tau N\\
    &= (\rho \tau + \rho'' \sigma + \rho' \sigma' )B.
```
Then differentiate the relation $\rho^2 + (\rho'\sigma)^2 = r^2$ to get 

```{math}
:enumerated: false

-\rho''\sigma -\rho'\sigma' = \frac{\rho\rho'}{\rho'\sigma} = \rho\tau,
```
so now

```{math}
:enumerated: false

\gamma' = (\rho\tau - \rho\tau)B = 0,
```
and $\gamma = \v{c}$ is constant and $\alpha$ has radius $r$ by virtue of having the form assumed with the given relation. $\square$


## Exercises 2.4

(ex-2-4-2)=
### Exercise 2

Express the curvature and torsion of the curve $\alpha(t) = (\cosh t, \sinh t, t)$ in terms of arc length $s$ measured from $t = 0$.

---
*Solution:*

Calculate the necessary elements, starting with

$$
\alpha' = (\sinh t,\, \cosh t,\, 1).
$$

Then $\|\alpha'\|^2 = \sinh^2 t + \cosh^2 t + 1 = 2\cosh^2 t$, so $v = \sqrt{2}\cosh t$ and

$$
s = \int_0^t v\,dt = \sqrt{2}\sinh t.
$$

Next we need $\alpha'' = (\cosh t,\, \sinh t,\, 0)$ and

$$
\alpha' \times \alpha''
    &= (-\sinh t,\, \cosh t,\, \sinh^2 t - \cosh^2 t) \\
    &= (-\sinh t,\, \cosh t,\, -1).
$$

Then $\|\alpha' \times \alpha''\|^2 = \sinh^2 t + \cosh^2 t + 1 = \|\alpha'\|^2$, so $\|\alpha' \times \alpha''\| = v$.

Last we need $\alpha''' = (\sinh t,\, \cosh t,\, 0)$ and

$$
\alpha''' \cdot (\alpha' \times \alpha'') = -\sinh^2 t + \cosh^2 t = 1.
$$

Apply the formulas in Theorem 4.3 to get

$$
\kappa
    &= \frac{\|\alpha' \times \alpha''\|}{v^3} = \frac{1}{v^2} = \frac{1}{2\cosh^2 t} \\
    &= \frac{1}{2\sinh^2 t + 2} = \frac{1}{s^2 + 2},
$$

$$
\tau
    &= \frac{\alpha''' \cdot (\alpha' \times \alpha'')}{\|\alpha' \times \alpha''\|^2} \\
    &= \frac{1}{v^2} = \frac{1}{s^2 + 2}. \qquad \square
$$

### Exercise 4

Show that the curvature of a regular curve in $\R^3$ is given by

```{math}
:enumerated: false

\kappa^2 v^4 = \|\alpha''\|^2 - \left(\frac{dv}{dt}\right)^2.
```

---
*Solution:*

This follows directly from the square norm of $\alpha'' = \frac{dv}{dt}\,T + \kappa v^2\,N$ from Lemma 4.2, since $T, N, B$ is an orthonormal basis. $\square$

### Exercise 6

(a) If $\alpha$ is a cylindrical helix, prove that its unit vector $\v{u}$ (Thm. 4.5) is

```{math}
:enumerated: false

\v{u} = \frac{\tau}{\sqrt{\kappa^2 + \tau^2}}\, T + \frac{\kappa}{\sqrt{\kappa^2 + \tau^2}}\, B,
```

and the coefficients here are $\cos\th$ and $\sin\th$ (for $\th$ as in Def. 4.5).

(b) Check (a) for the cylindrical helix in Example 4.2 of Chapter 1, $\alpha(t) = (a\cos t, a\sin t, bt)$, $a > 0$, $b \neq 0$.

---
*Solution:*

Differentiate the definitional relation $T \cdot \v{u} = \cos\th$ to get $T' \cdot \v{u} = 0$, so $\kappa N \cdot \v{u} = 0$, and since $\kappa > 0$, $N \cdot \v{u} = 0$.

Since $\v{u}$ is a unit vector, it has form

$$
\v{u} = \cos\th\, T + \sin\th\, B.
$$

If $\cos\th = 0$, then $\v{u} = \pm B$, so $B$ is constant and $\tau = 0$, which implies the desired result (choosing $\v{u}$ along $B$). Supposing $\tau \neq 0$,
differentiate again and substitute $N' = -\kappa T + \tau B$, getting

$$
B \cdot \v{u} = \frac{\kappa}{\tau}\, T \cdot \v{u}.
$$

Then
$$
\sin\th &= \frac{\kappa}{\tau}\cos\th, \\
1 - \cos^2\th &= \frac{\kappa^2}{\tau^2}\cos^2\th, \\
\cos^2\th &= \frac{\tau^2}{\kappa^2 + \tau^2},
$$

and choosing the direction of $\v{u}$ such that $\cos\th > 0$, we get

$$
\cos\th = \frac{\tau}{\sqrt{\kappa^2 + \tau^2}}, \qquad \sin\th = \frac{\kappa}{\sqrt{\kappa^2 + \tau^2}},
$$

as desired. $\square$

(b) Calculate

```{math}
:enumerated: false

\alpha' = (-a\sin t, a\cos t, b), \\
\|\alpha'\|^2 = a^2 + b^2, \\
```
so $v = \sqrt{a^2 + b^2}$, and $T = (-a/v \sin t, a/v \cos t, b/v)$. Then

```{math}
:enumerated: false

\alpha'' = (-a\cos t, -a\sin t, 0), \\
\alpha''' = (a \sin t, -a\cos t, 0), \\
\alpha' \times \alpha'' = (ab\sin t, -ab\cos t, a^2),
```
and

```{math}
:enumerated: false

\| \alpha' \times \alpha''\|^2 = a^2b^2 + a^4 = a^2v^2.
```

Then $B = (b/v \sin t, -b/v \cos t, a/v)$, and

```{math}
:enumerated: false

\kappa = \frac{\|\alpha' \times \alpha''\|}{v^3} = \frac{av}{v^3} = \frac{a}{v^2},\\
\tau = \frac{\alpha''' \cdot \alpha' \times \alpha''}{\|\alpha' \times \alpha''\|^2} = \frac{a^2b}{a^2v^2} = \frac{b}{v^2}.
```

So $\tau/\kappa = b/a$ is constant, and check the formula part (a), which would give, with $\sqrt{\tau^2 + \kappa^2} = 1/v$,

```{math}
:enumerated: false

\v{u} &= \frac{b}{v}\left(-\frac{a}{v} \sin t, \frac{a}{v} \cos t, \frac{b}{v}\right) + \frac{a}{v}\left(\frac{b}{v}\sin t, -\frac{b}{v} \cos t, \frac{a}{v}\right)\\
    &= \left(0, 0, 1\right),
```
a constant unit vector, as desired. $\square$

### Exercise 8

Verify that the following curves are cylindrical helices and, for each, find the unit vector $\v{u}$, angle $\th$, and cross-sectional curve $\gamma$.

(a) The curve in Exercise 1, $\alpha(t) = (2t, t^2, t^3/3)$.

(b) The curve in Example 4.4, $\alpha(t) = (3t - t^3, 3t^2, 3t + t^3)$.

(c) The curve in [Exercise 2](#ex-2-4-2).

---
*Solution:*

(a) Start doing calculations:

```{math}
:enumerated: false

\alpha' &= (2, 2t, t^2),\\
\alpha'' &= (0, 2, 2t),\\
\alpha''' &= (0, 0, 2),\\
\|\alpha'\|^2 &= 4 + 4t^2 + t^4,\\
v &= 2 + t^2,\\
\alpha' \times \alpha'' &= (4t^2 - 2t^2, -4t, 4) = (2t^2, -4t, 4),\\
\|\alpha' \times \alpha''\|^2 &= 4t^4 + 16t^2 + 16,\\
\|\alpha' \times \alpha''\| &= 2t^2 + 4, \\
\kappa &= \frac{2t^2 + 4}{(2 + t^2)^3} = \frac{2}{t^4 + 4t^2 + 4}, \\
\tau &= \frac{\alpha''' \cdot \alpha' \times \alpha''}{\|\alpha' \times \alpha''\|^2} = \frac{2}{t^4 + 4t^2 + 4}, \\
T &= \frac{1}{2 + t^2}(2, 2t, t^2), \\
B &= \frac{1}{2 + t^2}(t^2, -2t, 2). \\
```
So $\tau/\kappa = 1$, 
$\cos \th = \sin \th$,
and $\boxed{\th = \pi/4},$ and 

```{math}
:enumerated: false

\v{u} = \frac{1}{\sqrt 2(2 + 2 t^2)}(2 + t^2, 0, 2 + t^2) = \boxed{\left(\frac{1}{\sqrt 2}, 0, \frac{1}{\sqrt 2}\right)},
```
which is a constant unit vector, as expected.

The cross-sectional curve $\gamma$ is defined as

```{math}
:enumerated: false

\gamma(t) = \alpha(t)-((\alpha(t)-\alpha(t_0))\cdot \v{u})\v{u}.
```
So substitute:

```{math}
:enumerated: false

\gamma(t) &= (2t, t^2, t^3/3) - \left((2t, t^2, t^3/3)\cdot \left(\frac{1}{\sqrt 2}, 0, \frac{1}{\sqrt 2}\right)\right)\left(\frac{1}{\sqrt 2}, 0, \frac{1}{\sqrt 2}\right)\\
 &= (2t, t^2, t^3/3) - \left(t + \frac{t^3}{6}, 0, t + \frac{t^3}{6}\right)\\
 &= \boxed{\left(t - \frac{t^3}{6}, t^2, -t + \frac{t^3}{6}\right)},

```
noting that $\gamma \cdot \v{u} = 0$, verifying that it is a plane curve including the origin.

(b) Calculate:


```{math}
:enumerated: false

\alpha' &= 3(1 - t^2, 2t, 1 + t^2), \\
\alpha'' &= 6(-t, 1, t),\\
\alpha''' &= 6(-1, 0, 1),\\
\|\alpha'\|^2 &= 9(1 - 2t^2 + t^4 + 4t^2 + 1 + 2t^2 + t^4)\\
    &= 18(t^2 + 1)^2,\\
v &= 3\sqrt2(t^2 + 1),\\
\alpha' \times \alpha'' &= 18\left(t^2 - 1, -2t, t^2 + 1\right),\\
\|\alpha' \times \alpha''\|^2 &= 18^2(2t^4 + 2 + 4t^2),\\
\|\alpha' \times \alpha''\| &= 18\sqrt{2}(t^2 + 1),\\
\kappa &= \frac{18\sqrt{2}(t^2 + 1)}{54\sqrt 2 (1+t^2)^3} = \frac{1}{3(t^2 + 1)^2},\\
\tau &= \frac{6 \cdot 18 \cdot 2}{2\cdot 18^2(t^2 + 1)^2} = \frac{1}{3(t^2 + 1)^2},\\
T &= \frac{1}{\sqrt2 (t^2 + 1)}(1 - t^2, 2t, t^2 + 1),\\
B &= \frac{1}{\sqrt2 (t^2 + 1)}(t^2 - 1, -2t, t^2 + 1),\\
\th &= \boxed{\frac{\pi}{4}},\\
\v{u} &= \frac{1}{2(t^2 + 1)}(0, 0, 2(t^2 + 1)) = \boxed{(0, 0, 1)}.\\

```

Finally

```{math}
:enumerated: false

\gamma(t) &= (3t-t^3, t^2, 3 + t^3) - (0, 0, 3 + t^3) \\
    &= (3t - t^3, t^2, 0),
```
which of course is the projection to the $(x,y)$ plane.

(c) $\alpha(t) = (\cosh t, \sinh t, t)$, and we've previously calculated

```{math}
:enumerated: false

\alpha' = (\sinh t, \cosh t, 1),\\
v = \sqrt2 \cosh t,\\
\alpha' \times \alpha'' = (-\sinh t, \cosh t, -1),\\
\|\alpha' \times \alpha''\| = v,\\
\tau / \kappa = 1,\\
```
so

```{math}
:enumerated: false

\th &= \boxed{\frac{\pi}{4}},\\
\v{u} &= \frac{1}{2\cosh t}\left((\sinh t, \cosh t, 1) + (-\sinh t, \cosh t, -1)\right)\\
    &= \boxed{(0, 1, 0)},
```
and finally

```{math}
:enumerated: false

\boxed{\gamma(t) = (\cosh t, 0, t)},
```
using the obvious projection.


### Exercise 10

(a) Prove that a curve is a cylindrical helix if and only if its spherical image is part of a circle.

(b) Sketch the spherical image of the cylindrical helix in Exercise 1, $\alpha(t) = (2t, t^2, t^3/3)$. Is it a complete circle? Find its center.

---
*Solution:*

(a) For $c \in \R$ and a unit vector $\v{u}$, suppose a curve $\alpha$ is a cylindrical helix,
so that $T \cdot \v{u} = c$ for some $c$ and unit vector $\v{u}$. Then

```{math}
:enumerated: false

\|T - c\v{u}\|^2 &= (T - c\v{u})\cdot(T - c\v{u})\\
 &= \|T\|^2 - 2cT\cdot \v{u} + c^2\|\v{u}\|^2 \\
 &= 1 + c^2 - 2cT\cdot \v{u}
```
is constant, and

```{math}
:enumerated: false

T \cdot \v{u} = c

```
is the relation defining the affine plane containing $c\v{u}$ so $\sigma = T$ is a circle centered at $c\v{u}$.
Now a circle is a plane curve so $\sigma$ lying in a circle implies the plane relation above for some choice of
$c$ and unit vector $\v{u}$
which is also the definition of the cylindrical helix.$\square$

(ex-2-1-12)=
### Exercise 12

If $\alpha(t) = (x(t), y(t))$ is a regular curve in $\R^2$, show that its plane curvature ([Ex. 8 of Sec. 3](#ex-2-3-8)) is given by

```{math}
:enumerated: false

\tilde\kappa = \frac{\alpha'' \cdot J(\alpha')}{v^3} = \frac{x' y'' - x'' y'}{(x'^2 + y'^2)^{3/2}},
```

where $J$ is the rotation operator $J(a, b) = (-b, a)$.

---
*Solution:*

Recalling that $J(T) = N$, $N \cdot T = 0$, and $T' = \tilde\kappa v N$ (using the same logic as Lemma 4.1), we have
```{math}
:enumerated: false

\alpha'' = (vT)' = v'T + vT',
```
so

```{math}
:enumerated: false

\alpha'' \cdot J(\alpha') &= (v'T + vT')\cdot J(vT) \\ 
&= v'v T \cdot N + v^2 (\tilde\kappa v N) \cdot N \\ 
&= v^3 \tilde\kappa,
```
and
```{math}
:enumerated: false

\tilde\kappa = \frac{\alpha''\cdot J(\alpha')}{v^3}

```
as desired. The coordinate formula just expands that. $\square$

### Exercise 14

(*Continuation, Computer graphics.*) In each case, plot the given plane curve and its evolute on the same figure, showing some of the construction lines $\ell_t$.

(a) The ellipse $\alpha(t) = (2\cos t, \sin t)$.

(b) The cycloid $\alpha(t) = (t + \sin t,\; 1 + \cos t)$ for $-2\pi \le t \le 2\pi$. (Here the evolute bears an unexpected relation to the original curve.)

---
*Solution:*



### Exercise 16

It is shown in advanced calculus that the function

```{math}
:enumerated: false

f(t) = \begin{cases} 0 & \text{if } t \le 0 \\ e^{-1/t^2} & \text{if } t > 0 \end{cases}
```

is infinitely differentiable (has continuous derivatives of all orders). Thus

```{math}
:enumerated: false

\alpha(t) = (t,\; f(t),\; f(-t))
```

is a well-defined differentiable curve.

(a) Sketch $\alpha$ on an interval $-a < t < a$.

(b) Show that the curvature of $\alpha$ is zero only at $t = 0$.

(c) What are the osculating planes of $\alpha$ for $t < 0$ and $t > 0$?

---
*Solution:*
(b) Calculate
```{math}
:enumerated: false

f'(t) = \begin{cases} 0 & \text{if } t \le 0 \\
    \frac{2}{t^3}e^{-1/t^2} & \text{if } t >0
\end{cases}
```

and recall that for $k \ge 0$,
```{math}
:enumerated: false

\lim_{t \rightarrow 0^+} \frac{e^{-1/t^2}}{t^k} = \lim_{x \rightarrow \infty} x^k e^{-x^2} = 0,
```
so all derivatives of $f$ will be zero at zero and obviously positive for $t > 0$. Then
```{math}
:enumerated: false

\alpha'(t) = (1, f'(t), -f'(-t)), \\
\alpha''(t) = (0, f''(t), f''(-t)),
```
so evaluate 
```{math}
:enumerated: false
\alpha' \times \alpha'' = (f'(t)f''(-t) + f''(t)f'(-t), -f''(-t), f''(t)),
```
which is seen to be only zero at $t=0$ by observing the second and third coordinates, and therefore $\kappa$ is only zero at $t=0$ since $v > 0$ due to the first coordinate.

(c) The osculating plane is determined by the direction of $\alpha' \times \alpha''$. For $t > 0$, calculate

```{math}
:enumerated: false

\alpha' \times \alpha'' = (0, 0, f''(t)),
```
so the osculating plane is parallel to the $xy$-plane, and for $t<0$,

```{math}
:enumerated: false

\alpha' \times \alpha'' = (0, -f''(-t), 0),
```
parallel to the $xz$-plane. So we observe discontinuity at $t=0$ despite the smooth curve. $\square$


### Exercise 18

One definition of convexity for a smoothly closed plane curve is that its curvature $\kappa$ is positive (hence its plane curvature $\tilde\kappa$
is either always positive or always negative). Prove that a convex closed plane curve has total curvature $2\pi$. (*Hint:* Consider its spherical image.)

---
*Solution:*
First of all, I don't believe *closed curve* is defined in the text. We use the definition of a *periodic* curve and further say that the total curvature is the curvature
for one period interval $I = (a, b)$.
From Exercise 17, the total curvature is given by $\int_I \kappa(s)ds$. We consider the spherical image $\sigma = T$, which lies in the plane $\sigma \cdot B = 0$
for the constant vector $B$.

First, note that $\sigma$ lies in a unit circle, since it satisfies $\|\sigma\| = 1$ and is a plane curve in a plane containing the origin, so it lies on a circle with the origin at its center.

$\sigma' = T' = \kappa N \neq 0$,
so $\sigma' \neq 0$ and $\sigma$ is a regular curve, and therefore has a unit-speed reparametrization $h(s)$ with $h' > 0$. Since $\sigma(a) = \sigma(b)$ by periodicity, if $\beta = \sigma(h)$,
then if $h(0) = a$ and $h(S) = b$, we must have $\beta(0) = \beta(S)$ be endpoints of a unit-speed curve lying within a unit circle. $S$ equals the total arclength along the
unit circle so must be a multiple of $2\pi$ given the monotonic reparametrization. It seems that multiple winding, e.g. $S = 4\pi$, would require self-intersection by $\alpha$.
Under the assumption of a simple curve with the necessary result granted, then the total curvature is given by

```{math}
:enumerated: false

\int_I \kappa(s)ds &= \int_I \kappa\|N\|ds \\
 &= \int_I \|\sigma'(s)\|ds\\ 
 &= \int_0^{2\pi} \|\sigma'(h(r))\|h'(r)dr \\
 &= \int_0^{2\pi} \|\beta'(r)\|dr \\
 &= 2\pi.
```
$\square$


### Exercise 20

(*Computer.*)

(a) Write a command that, given an arbitrary regular curve, returns the test function in [Exercise 10 of Section 3](#ex-2-3-10) whose constancy implies that the curve lies on a sphere. (Plotting this function provides a good test for constancy and does not require simplifying it.) (*Hint:* To allow for arbitrary parametrization, replace derivatives $f'(s)$ by $f'(t)\,v(t)$, where $v(t) = ds/dt$.)

(b) In each case, decide whether the curve lies on a sphere, and if so, find its radius and center:

(i) $\alpha(t) = (2\sin t,\; \sin 2t,\; 2\sin^2 t)$;

(ii) $\beta(t) = (\cos 2t,\; \sin 2t,\; 2\sin t)$;

(iii) $\gamma(t) = (\cos t,\; 1 + \sin t,\; 2\sin(t/2))$.

---
*Solution:*

## Exercises 2.5

### Exercise 2

Let $V = -yU_1 + xU_3$ and $W = \cos x\, U_1 + \sin x\, U_2$. Express the following covariant derivatives in terms of $U_1, U_2, U_3$:

(a) $\nabla_V W$.

(b) $\nabla_V V$.

(c) $\nabla_V(z^2 W)$.

(d) $\nabla_W V$.

(e) $\nabla_V(\nabla_V W)$.

(f) $\nabla_V(xV - zW)$.

---
*Solution:*

(a) Applying the Jacobean matrix $J_W$ to $V$ performs the same operation
as $\nabla_V W$, since the rows of $J$ are the vector representations of the differential forms 
used for the directional derivatives $V[w_i] = dw_i(V)$, so the matrix product matches the form in Lemma 5.2.

Calculate the Jacobean:
```{math}
:enumerated: false

J_W &= 
\left(\begin{matrix}
\pd{w_1}{x} && \pd{w_1}{y} && \pd{w_1}{z}\\
\pd{w_2}{x} && \pd{w_2}{y} && \pd{w_2}{z}\\
\pd{w_3}{x} && \pd{w_3}{y} && \pd{w_3}{z}\\
\end{matrix}\right) \\
    &= 
\left(\begin{matrix}
-\sin x && 0 && 0 \\
\cos x && 0 && 0 \\
0 && 0 && 0 \\
\end{matrix}\right), \\
```
so we can calculate $\nabla_V W$ as $\boxed{J_W V = y\sin x U_1 -y\cos x U_2}$.

(b)

```{math}
:enumerated: false

\nabla_V V = J_V V &= \left(
\begin{matrix}
0 && -1 && 0 \\
0 && 0 && 0 \\
1 && 0 && 0 \\
\end{matrix}\right) \left(\begin{matrix} -y \\ 0 \\ x \end{matrix}\right) \\
 &= \boxed{-y U_3}.
```

(c) Use Corollary 5.4(3) to get

```{math}
:enumerated: false

\nabla_V(z^2 W) &= V[z^2]W + z^2\nabla_V W \\
 &= 2zdz(V)W + yz^2\sin x U_1 - yz^2 \cos x U_2 \\
  &= \boxed{(2xz \cos x + yz^2\sin x) U_1 + (2xz \sin x - yz^2 \cos x) U_2}. 
```

(d) Use the Jacobean above to get

```{math}
:enumerated: false

\nabla_W V = J_V W &= \left(
\begin{matrix}
0 && -1 && 0 \\
0 && 0 && 0 \\
1 && 0 && 0 \\
\end{matrix}\right) \left(\begin{matrix} \cos x \\ \sin x \\ 0 \end{matrix}\right) \\
 &= \boxed{- \sin x U_1 + \cos x U_3}.
```
(e) We need the Jacobean of the field $\nabla_V W = y\sin x U_1 - y\cos x U_2$ from part (a).

```{math}
:enumerated: false

J_{\nabla_V W} = \left(\begin{matrix} y\cos x && \sin x && 0 \\ y\sin x && -\cos x && 0 \\ 0 && 0 && 0 \end{matrix}\right).
```
Then $\nabla_V(\nabla_V W) = J_{\nabla_V W} V = \boxed{-y^2 \cos x U_1 - y^2 \sin x U_2}$.

(f) Again, expand with Corollary 5.4:
```{math}
:enumerated: false

\nabla_V(xV - zW) &= V[x]V + x\nabla_V V - V[z]W - z\nabla_V W \\
 &= -y V - xy U_3 - xW - yz\sin x U_1 + yz \cos x U_2\\
 &= \boxed{(y^2 - x\cos x - yz\sin x)U_1 + (yz \cos x - x\sin x) U_2 - 2xy U_3}.
```

### Exercise 4

Let $X$ be the special vector field $\sum x_i U_i$, where $x_1, x_2, x_3$ are the natural coordinate functions of $\R^3$. Prove that $\nabla_V X = V$ for every vector field $V$.

---
*Solution:*

Using the Jacobean approach above, we see that $J_X = I$ and $\nabla_V X = J_X V = V$ as desired.$\square$

## Exercises 2.6

### Exercise 2

Express each of the following vector fields (i) in terms of the cylindrical frame field (with coefficients in terms of $r, \th, z$) and (ii) in terms of the spherical frame field (with coefficients in terms of $r, \th, \ph$):

(a) $U_1$.

(b) $\cos\th\, U_1 + \sin\th\, U_2 + U_3$.

(c) $xU_1 + yU_2 + zU_3$.

---
*Solution:*

We take advantage of a property of orthogonal matrics: For a matrix $A$ with orthonormal columns or rows, $A^{-1} = A^T$, that is, the inverse of the matrix is the transpose. This follows directly from the
    orthonormal property since for columns $A_i, A_j$ of $A$, $A_i \cdot A_j = A_i^T A_j = A^TA_{ij} = \delta_{ij},$ so $A^TA = I$, and $AA^T = I$.

(i)

Now we write the matrix for the cylindrical frame so that $E = AU$ where $U = (U_1, U_2, U_3)$. From some point of view, you could say that $U = I$, so $A$
just gives the coordinate functions of $E$ in matrix form. Following the given formulas, we have

$$
A = \left(\begin{matrix}
    \cos\th & \sin\th & 0 \\
    -\sin\th & \cos\th & 0 \\
    0 & 0 & 1 \\
    \end{matrix}\right),
$$ so 

$$
\left(\begin{matrix}U_1 \\ U_2 \\ U_3 \end{matrix}\right) = \left(\begin{matrix}
    \cos\th & -\sin\th & 0 \\
    \sin\th & \cos\th & 0 \\
    0 & 0 & 1 \\
    \end{matrix}\right) \left(\begin{matrix} E_1 \\ E_2 \\ E_3 \end{matrix}\right).
$$

(a) From the above, we have $U_1 = \boxed{\cos\th E_1 - \sin\th E_2}$.

(b) $\cos\th U_1 + \sin\th U_2 = E_1$, so $\boxed{E_1 + E_3}$. 

(c) $xU_1 + yU_2 + zU_3 = (x, y, z) \cdot (U_1, U_2, U_3)$, so calculate

$$
\left(\begin{matrix} x \\ y \\ z \end{matrix}\right)^T
\left(\begin{matrix}
    \cos\th & -\sin\th & 0 \\
    \sin\th & \cos\th & 0 \\
    0 & 0 & 1 \\
    \end{matrix}\right) \left(\begin{matrix} E_1 \\ E_2 \\ E_3 \end{matrix}\right) &=
\left(\begin{matrix} r\cos\th \\ r\sin\th \\ z \end{matrix}\right)^T  
\left(\begin{matrix}\cos\th E_1 - \sin\th E_2 \\ \sin\th E_1 + \cos\th E_2 \\ E_3 \end{matrix}\right) \\
    &= \boxed{rE_1 + zE_3}.
$$

(ii)

Now as given we have
$$
A = \left(\begin{matrix}
    \cos\ph \cos\th & \cos\ph \sin\th & \sin\ph \\
    -\sin\th & \cos\th & 0 \\
    -\sin\ph \cos\th & -\sin\ph \sin\th & \cos \ph \\
    \end{matrix}\right),
$$
so

$$
\left(\begin{matrix}U_1 \\ U_2 \\ U_3 \end{matrix}\right) = \left(\begin{matrix}
    \cos\ph \cos\th  & -\sin\th & -\sin\ph \cos\th \\
    \cos\ph \sin\th & \cos\th & -\sin\ph \sin\th  \\
    \sin\ph & 0 & \cos \ph \\
    \end{matrix}\right) \left(\begin{matrix} F_1 \\ F_2 \\ F_3 \end{matrix}\right).
$$

(a) As before, $U_1 = \boxed{\cos\ph \cos\th F_1 -\sin\th F_2 -\sin\ph \cos\th F_3}$.

(b) Calculate

```{math}
:enumerated: false

&\left(\begin{matrix} \cos\th \\ \sin\th \\ 1 \end{matrix}\right)^T
\left(\begin{matrix}
    \cos\ph \cos\th  & -\sin\th & -\sin\ph \cos\th \\
    \cos\ph \sin\th & \cos\th & -\sin\ph \sin\th  \\
    \sin\ph & 0 & \cos \ph \\
    \end{matrix}\right) \left(\begin{matrix} F_1 \\ F_2 \\ F_3 \end{matrix}\right) \\
    &= (\cos\ph + \sin\ph, 0, \cos\ph - \sin\ph)\cdot(F_1, F_2, F_3)  \\
    &= \boxed{(\cos\ph + \sin\ph)F_1 + (\cos\ph - \sin\ph)F_3}.

```
(b) Calculate

```{math}
:enumerated: false

&\left(\begin{matrix} \rho\cos\ph\cos\th \\ \rho\cos\ph\sin\th \\ \rho\sin\ph \end{matrix}\right)^T
\left(\begin{matrix}
    \cos\ph \cos\th  & -\sin\th & -\sin\ph \cos\th \\
    \cos\ph \sin\th & \cos\th & -\sin\ph \sin\th  \\
    \sin\ph & 0 & \cos \ph \\
    \end{matrix}\right) \left(\begin{matrix} F_1 \\ F_2 \\ F_3 \end{matrix}\right) \\
    &= (\rho, 0, 0)\cdot(F_1, F_2, F_3)  \\
    &= \boxed{\rho F_1}.

```

## Exercises 2.7

### Exercise 2

Find the connection forms of the natural frame field $U_1, U_2, U_3$.

---
*Solution:*

Each is 0 since the field is constant. $\square$.

### Exercise 4

Prove that the connection forms of the spherical frame field are

$$
\omega_{12} = \cos\ph\, d\th, \qquad
\omega_{13} = d\ph, \qquad
\omega_{23} = \sin\ph\, d\th.
$$

---
*Solution:*

From 2.6.2, we have the attitude matrix

```{math}
:enumerated: false

A = \left(\begin{matrix}
    \cos\ph \cos\th & \cos\ph \sin\th & \sin\ph \\
    -\sin\th & \cos\th & 0 \\
    -\sin\ph \cos\th & -\sin\ph \sin\th & \cos \ph \\
    \end{matrix}\right),
```
so

```{math}
:enumerated: false

dA = \left(\begin{matrix}
    -\sin\ph\cos\th d\ph - \cos\ph\sin\th d\th & -\sin\ph\sin\th d\ph + \cos\ph\cos\th d\th & \cos\ph d\ph \\
    -\cos\th d\th & -\sin\th d\th & 0 \\
    -\cos\ph\cos\th d\ph + \sin\ph\sin\th d\th & -\cos\ph\sin\th d\ph - \sin\ph\cos\th d\th & -\sin\ph d\ph \\

    \end{matrix}\right),
```
and to get $\omega_{12}$ we need the dot product of the first row of $dA$ with the second row of $A$, so

```{math}
:enumerated: false
\omega_{12} &= 
\left(\begin{matrix}
    -\sin\ph\cos\th d\ph - \cos\ph\sin\th d\th \\ -\sin\ph\sin\th d\ph + \cos\ph\cos\th d\th \\ \cos\ph d\ph \\
\end{matrix}\right) \cdot
\left(\begin{matrix}
    -\sin\th \\ \cos\th \\ 0 \\
\end{matrix}\right) \\
    &= \sin\ph\cos\th\sin\th d\ph + \cos\ph\sin^2\th d\th - \sin\ph\cos\th\sin\th d\ph + \cos\ph \cos^2\th d\th \\ 
    &= \cos\ph d\th.
```

Similarly

```{math}
:enumerated: false
\omega_{13} &= 
\left(\begin{matrix}
    -\sin\ph\cos\th d\ph - \cos\ph\sin\th d\th \\ -\sin\ph\sin\th d\ph + \cos\ph\cos\th d\th \\ \cos\ph d\ph \\
\end{matrix}\right) \cdot
\left(\begin{matrix}
    -\sin\ph \cos\th \\ -\sin\ph \sin\th \\ \cos \ph \\
\end{matrix}\right) \\
    &= \sin^2\ph\cos^2\th d\ph  + \sin^2\ph\sin^2\th d\ph  + \cos^2\ph d\ph \\
    &= d\ph.
```
Finally, by formal parallelism we can see that $\omega_{32} = -\sin\ph d\th$ so $\omega_{23} = \sin\ph d\th$, as desired. $\square$.

### Exercise 6

Let $E_1, E_2, E_3$ be the cylindrical frame field. If $V$ is a vector field such that $V[r] = r$ and $V[\th] = 1$, compute $\nabla_V(r\cos\th\, E_1 + r\sin\th\, E_3)$.

---
*Solution:*

By the example after Theorem 7.3, we see that $\omega_{12} = d\th$ (so $\omega_{12}(V) = V[\th] = 1$) is the only nonzero connection form for $E$. By Theorem 5.3, expand
```{math}
:enumerated: false

\nabla_V(r\cos\th E_1 + r\sin\th E_3) &= V[r\cos\th]E_1 + r\cos\th \nabla_V E_1 + V[r\sin\th] E_3 + r\sin\th \nabla_V E_3 \\
 &= (V[r]\cos\th - r\sin\th V[\th])E_1 + r\cos\th V[\th] E_2 + (V[r]\sin\th + r\cos\th V[\th])E_3 \\
 &= \boxed{(r\cos\th - r\sin\th)E_1 + r\cos\th E_2 + (r\sin\th + r\cos\th)E_3}. \\
```


### Exercise 8

Let $\beta$ be a unit-speed curve in $\R^3$ with $\kappa > 0$, and suppose that $E_1, E_2, E_3$ is a frame field on $\R^3$ such that the restriction of these vector fields to $\beta$ gives the Frenet frame field $T, N, B$ of $\beta$. Prove that

$$
\omega_{12}(T) = \kappa, \qquad \omega_{13}(T) = 0, \qquad \omega_{23}(T) = \tau.
$$

---
*Solution:*

This amounts to the assertion that $\nabla_T{E_1} = T'$ and so on for the frame vectors since in that case the result holds formally. Since the curve is unit speed, this is effectively what we did in Exercise 1.7.8. A bit more could be said here...

## Exercises 2.8

### Exercise 2

Check all the structural equations of the spherical frame field.

---

We are checking first the dual forms and connection forms:

```{math}
:enumerated: false

\theta_1 &= d\rho, & \omega_{12} &= \cos\ph d\th, \\
\theta_2 &= \rho\cos\ph d\th, & \omega_{13} &= d\ph, \\
\theta_3 &= \rho d\ph, & \omega_{23} &= \sin\ph d\th. \\
```

Recall that the attitude matrix for the spherical frame field is given by
```{math}
:enumerated: false
A = \left(\begin{matrix}
\cos\ph\cos\th && \cos\ph\sin\th && \sin\ph \\
-\sin\th && \cos\th && 0 \\
-\sin\ph\cos\th && -\sin\ph\sin\th && \cos\ph \\
\end{matrix}\right),
```
and that 

```{math}
:enumerated: false

\rho^2 &= x^2 + y^2 + z^2,\\
x &= \rho\cos\ph\cos\th,\\
y &= \rho\cos\ph\sin\th,\\
z &= \rho\sin\ph,\\
```
so 

```{math}
:enumerated: false

d(\rho^2) = 2\rho d\rho = 2xdx + 2ydx + 2zdz,
```

and since 
```{math}
:enumerated: false

F_1 = x/\rho U_1 + y/\rho U_2 + z/\rho U_3,  \\
\theta_1 = \frac{x dx + y dy + z dz}{\rho}, 
```

we have $\theta_1 = d\rho$, as desired. 

Now consider

```{math}
:enumerated: false

dx = \cos\ph \cos\th d\rho - \rho\sin\ph\cos\th d\ph - \rho\cos\ph\sin\th d\th, \\
dy = \cos\ph \sin\th d\rho - \rho\sin\ph\sin\th d\ph + \rho\cos\ph\cos\th d\th, \\
dz = \sin\ph d\rho+ \rho\cos\ph d\ph.
```
So we have

```{math}
:enumerated: false

\theta_2 =& -\sin\th dx + \cos\th dy \\
    =& -\cos\ph\sin\th\cos\th d\rho + \rho\sin\ph\sin\th\cos\th d\ph + \rho\cos\ph\sin^2\th d\th \\
    &+ \cos\ph\sin\th\cos\th d\rho - \rho\sin\ph\sin\th\cos\th d\ph + \rho\cos\ph\cos^2\th d\th \\
    =& \rho\cos\ph d\th.
```

Finally,

```{math}
:enumerated: false

\theta_3 =& -\sin\ph\cos\th dx -\sin\ph\sin\th dy + \cos\ph dz \\
    =& -\sin\ph\cos\ph\cos^2\th d\rho + \rho\sin^2\ph\cos^2\th d\ph + \rho\sin\ph\cos\ph\sin\th\cos\th d\th \\
    & -\sin\ph\cos\ph\sin^2\th d\rho + \rho\sin^2\ph\sin^2\th d\ph - \rho\sin\ph\cos\ph\sin\th\cos\th d\th \\
    & +\sin\ph\cos\ph d\rho + \rho\cos^2\ph d\ph \\
    =& \rho d\ph.
```
The connection forms were derived in Ex. 2.7.4.

Now the structural equations. Calculate

```{math}
:enumerated: false

d\theta_1 &= d^2\rho = 0,
```
and

```{math}
:enumerated: false

\omega_{12} \wedge \theta_2 + \omega_{13} \wedge \theta_3 = \cos\ph d\th \wedge \rho\cos\ph d\th + d\ph \wedge \rho d\ph = 0, \\
```
so $d\theta_1 = \omega_{12} \wedge \theta_2 + \omega_{13} \wedge \theta_3$ as desired.

Next,

```{math}
:enumerated: false

d\theta_2 &= d(\rho\cos\ph d\th) \\
    &= \cos\ph d\rho \wedge d\th - \rho\sin\ph d\ph \wedge d\th,
```
and

```{math}
:enumerated: false

\omega_{21} \wedge \theta_1 + \omega_{23} \wedge \theta_3 &= -\cos\ph d\th \wedge d\rho + \sin\ph d\th \wedge \rho d\ph \\
    &= \cos\ph d\rho \wedge d\th - \rho\sin\ph d\ph \wedge d\th,
```
as desired. $d\theta_3$ was checked in the text.

For the second equations, $d\omega_{12}$ is established in the text, then

```{math}
:enumerated: false

d\omega_{23} &= d(\sin\ph d\th) \\
 &= \cos\ph d\ph d\th, \\

```
and

```{math}
:enumerated: false

\omega_{21} \wedge \omega_{13} &= (-\cos\ph d\th) \wedge (d\ph) \\
 &= \cos\ph d\ph d\th,
```
as desired, and

```{math}
:enumerated: false

d\omega_{13} &= d(d\ph) = 0, \\
```
and

```{math}
:enumerated: false

\omega_{12} \wedge \omega_{23} &= (\cos\ph d\th) \wedge (\sin\ph d\th) \\ 
 &= ... d\th \wedge d\th = 0, \\
```
and we're done. $\square$

### Exercise 4

*Frame fields on $\R^2$.* Given a frame field $E_1, E_2$ on $\R^2$, there is an angle function $\psi$ such that

$$
E_1 = \cos\psi\, U_1 + \sin\psi\, U_2, \qquad E_2 = -\sin\psi\, U_1 + \cos\psi\, U_2.
$$

(a) Express the connection form and dual 1-forms in terms of $\psi$ and the natural coordinates $x, y$.

(b) What are the structural equations in this case? Check that the results in part (a) satisfy these equations.

(*Hint:* Defining $E_3 = U_3$ gives a frame field on $\R^3$.)

--- 
