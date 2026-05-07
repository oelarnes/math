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
In $\R^3$ there is a unique orthogonal space so the unit vector must be $\pm \v{e}_1$, and $\pm \v{e}_1 \cdot \v{e}_1 = \pm 1$. By exercise 4(a),
the orthogonal matrix with rows $\v{e}_i$ has determinant $\pm 1$. $\square$

### Exercise 8

Prove: the volume of the parallelepiped with sides $\v{u}, \v{v}, \v{w}$ is $\pm \v{u} \cdot \v{v} \times \v{w}$.

---

*Proof:* This is known to be given by the determinant according to Exercise 4. Proceeding geometrically using the property that areas and volumes are invariant
under shear transformations, first note that the norm of the cross product $\v{z} = \v{v} \times \v{w}$ is

```{math}
:enumerated: false

\|\v{z}\| = \|\v{v}\|\|\v{w}\|\sin(\theta_{\v{v}\v{w}}), 
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
$\vartheta_0$ is a number such that $f(0) = \cos\vartheta_0$ and $g(0) = \sin\vartheta_0$. If $\vartheta$ is the function such that

```{math}
:enumerated: false

\vartheta(t) = \theta_0 + \int_0^t (fg' - gf') du,
```

prove that

```{math}
:enumerated: false

f = \cos\vartheta, g = \sin\vartheta.
```

---

*Solution:*

Note that $ff' + gg' = 0$ by differentiating the relation $f^2 + g^2 = 1$. Following the hint, calculate by the chain rule and collecting like terms.

```{math}
:enumerated: false

\frac{1}{2}\frac{d}{dt}\left((f - \cos\vartheta)^2 + (g - \sin\vartheta)^2\right) \\
=(f - \cos\vartheta)(f' + \sin\vartheta (fg' - gf')) + (g - \sin\vartheta)(g' - \cos\vartheta (fg' - gf')) \\
=ff' + gg' + (ffg' - fgf' - g')\sin\vartheta + (ggf' - gfg' - f')\cos\vartheta \\
= ((1-gg)g' - fgf' - g')\sin\vartheta + ((1-ff)f' - gfg' - f')\cos\vartheta \\
= ((g' - g') - (ff' + gg')g)\sin\vartheta + ((f' - f') - (ff' + gg')f)\cos\vartheta \\
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

### Exercise 8

*Curves in the plane.* For a unit-speed curve $\beta(s) = (x(s), y(s))$ in $\R^2$, the unit tangent is $T = \beta' = (x', y')$ as usual, but the unit normal $N$ is defined by rotating $T$ through $+90°$, so $N = (-y', x')$. Thus $T'$ and $N$ are collinear, and the **plane curvature** $\tilde{\kappa}$ of $\beta$ is defined by the Frenet equation $T' = \tilde{\kappa}\,N$.

(a) Prove that $\tilde{\kappa} = T' \cdot N$ and $N' = -\tilde{\kappa}\,T$.

(b) The *slope angle* $\varphi(s)$ of $\beta$ is the differentiable function such that

$$T = (\cos\varphi,\, \sin\varphi) = \cos\varphi\, U_1 + \sin\varphi\, U_2.$$

(The existence of $\varphi$ derives from Ex. 12 of Sec. 1.) Show that $\tilde{\kappa} = \varphi'$.

(c) Find the curvature $\tilde{\kappa}$ of the following plane curves.

(i) $(r\cos(s/r),\, r\sin(s/r))$, counterclockwise circle.

(ii) $(r\cos(-s/r),\, r\sin(-s/r))$, clockwise circle.

(d) Show that if $\tilde{\kappa}$ does not change sign, then $|\tilde{\kappa}|$ is the usual $\R^3$ curvature $\kappa$. (For such comparisons we can always regard $\R^2$ as, say, the $xy$ plane in $\R^3$.)

---

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

