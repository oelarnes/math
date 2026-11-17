# Two-state updates: core skill and Bo3 offset

State $x = (s, d)$: core skill $s$, Bo3 offset $d$. Bo3 skill $t = s + d$.
Observation $y = Hx + \varepsilon$, $\varepsilon \sim \mathcal N(0, Q)$.
General update: $S = H\Sigma H^\top + Q$, $K = \Sigma H^\top / S$, $\mu' = \mu + K(y - H\mu)$, $\Sigma' = \Sigma - K S K^\top$.

## Bo3 observation, independent priors

Prior $s \sim \mathcal N(m, P)$, $d \sim \mathcal N(0, D)$, independent. $H = [1, 1]$.

$$
S = P + D + Q, \qquad K = \left(\frac{P}{S}, \frac{D}{S}\right)
$$

$$
s' = m + \frac{P}{S}(y - m), \qquad d' = \frac{D}{S}(y - m)
$$

```{math}
\operatorname{Var}(s') &= P - \frac{P^2}{S} = \frac{P(D + Q)}{S} \\
\operatorname{Var}(d') &= D - \frac{D^2}{S} = \frac{D(P + Q)}{S} \\
\operatorname{Cov}(s', d') &= -\frac{PD}{S}
```

$$
t' = m + \frac{P + D}{S}(y - m), \qquad \operatorname{Var}(t') = \frac{(P + D)\,Q}{S}
$$

Checks: $\operatorname{Var}(s') = 1/\big(1/P + 1/(D + Q)\big)$; $\operatorname{Var}(t') = 1/\big(1/(P + D) + 1/Q\big)$.

## Bo1 observation, correlated prior

Prior $s \sim \mathcal N(m_s, P)$, $d \sim \mathcal N(m_d, D)$, $\operatorname{Cov}(s, d) = C$. $H = [1, 0]$.

$$
S = P + Q, \qquad K = \left(\frac{P}{S}, \frac{C}{S}\right)
$$

$$
s' = m_s + \frac{P}{S}(y - m_s), \qquad d' = m_d + \frac{C}{S}(y - m_s)
$$

```{math}
\operatorname{Var}(s') &= P - \frac{P^2}{S} = \frac{PQ}{S} \\
\operatorname{Var}(d') &= D - \frac{C^2}{S} \\
\operatorname{Cov}(s', d') &= C - \frac{PC}{S} = \frac{CQ}{S}
```

$$
t' = m_s + m_d + \frac{P + C}{S}(y - m_s), \qquad
\operatorname{Var}(t') = P + D + 2C - \frac{(P + C)^2}{S}
$$

Checks: $C = 0$ leaves $d$ unchanged. $C = -P$, $D = P$ ($t$ known exactly) gives $\Delta d = -\Delta s$, $\Delta t = 0$.
