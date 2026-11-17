# Skill update model

Core skill (latent) $s$. Estimates $s \sim \mathcal N(m, P)$.

Set-specific skill $a \sim \mathcal N(0, S)$.

Let

$$
p(x) = \frac{1}{1 + e^{-x}}, \quad \text{then} \quad p'(x) = \frac{e^{-x}}{(1 + e^{-x})^2} = p(1 - p) = v.
$$

For one game,

$$
E[W] = P[\text{win}] = p(s + a)
$$

(rank handled as $s + a - o_r$ but not in this note)

$$
\operatorname{Var}[W] = p(1 - p)^2 + (1 - p)p^2 = p(1 - p) = v.
$$

Assuming $n$ independent games,

$$
P[w \text{ wins in } n \text{ games},\ s \in ds,\ a \in da] \propto p^w (1 - p)^{n - w}\, e^{-\frac{(s - m)^2}{2P}}\, e^{-\frac{a^2}{2S}}
$$

Calculate log-likelihood as a function of $s$ and $a$

$$
\ell(s, a) = w \log p + (n - w) \log(1 - p) - \frac{(s - m)^2}{2P} - \frac{a^2}{2S}
$$

$p$ is constant along lines $x = s + a$, so we can simplify the fit by minimizing the contribution of $s$ and $a$ subject to $s + a = x$:

We want
$$
\min_s \frac{(s - m)^2}{2P} + \frac{(x - s)^2}{2S},
$$

so take the derivative with respect to $s$ to see

$$
\frac{s - m}{P} - \frac{x-s}{S} = 0, \qquad a = (s - m)\frac{S}{P}.
$$

Then

$$
\frac{a^2}{2S} = \frac{(s - m)^2}{2P}\,\frac{S}{P},
$$

so let $\lambda = 1 + \frac{S}{P}$ and let

$$
q(s) = p\!\left(s + \frac{S}{P}(s - m)\right) = p\!\left(\lambda s - \frac{S}{P}m\right)
$$

so

$$
\ell(s) = w \log q + (n - w) \log(1 - q) - \frac{\lambda (s - m)^2}{2P}, \qquad q' = \lambda v.
$$

Take

```{math}
\ell'(s) &= w\frac{q'}{q} - (n - w)\frac{q'}{1 - q} - \frac{\lambda(s - m)}{P} \\
&= w(1 - q)\lambda - (n - w)q\lambda - \frac{\lambda(s - m)}{P} \\
&= \lambda\left[(w - nq) - \frac{s - m}{P}\right],
```

so we find the (Bayesian) maximum likelihood solution, or posterior mode, at the solution to

$$
\boxed{\frac{s - m}{P} = w - nq(s)}.
$$

To solve, we use Newton's method. Let $y = \frac{w}{n}$ then let

$$
f = n(y - q(s)) - \frac{s - m}{P}, 
$$

and 

$$
f'(s) = - \lambda v n - \frac{1}{P},
$$

so we iterate using the rule

$$
s \to s + \frac{n(y - q(s)) - \frac{s - m}{P}}{\lambda v n + \frac{1}{P}}.
$$

## The Gaussian observation model

To infer the posterior distribution, construct a Gaussian observation model centered at $p = p\!\left(s + \frac{S}{P}(s - m)\right)$ for a fixed $s$, e.g. the fixed point of the MAP solution. Then model

```{math}
y &= p(x + a) + \varepsilon \\
&\approx p + v a + v\left(x - \left(s + \frac{S}{P}(s - m)\right)\right) + \varepsilon.
```

For $n$ independent observations $\varepsilon \sim \mathcal N\!\left(0, \frac{p(1 - p)}{n}\right)$, but game results are not independent. Local autocorrelation (e.g. over one event) means that we can model $\varepsilon \sim \mathcal N\!\left(0, \frac{\kappa p(1 - p)}{n}\right)$ for $\kappa > 0$: $\kappa < 1$ results from negative autocorrelation due to e.g. record-based pairing, $\kappa > 1$ results from e.g. shared deck strength variance. Then $v a + \varepsilon$ is a Gaussian variable $\mathcal N\!\left(0, v^2 S + \frac{\kappa p(1 - p)}{n}\right)$, and the joint density for $x$ and $y$ is

```{math}
P_{x,y} &\propto \exp\left(-\frac{\left(y - p - v\left(x - \left(s + \frac{S}{P}(s - m)\right)\right)\right)^2}{2\left(v^2 S + \frac{\kappa p(1 - p)}{n}\right)} - \frac{(x - m)^2}{2P}\right) \\
&= \exp\left(-\frac{\left(x - \left(\frac{y - p}{v} + s + \frac{S}{P}(s - m)\right)\right)^2}{2\left(S + \frac{\kappa}{n v}\right)} - \frac{(x - m)^2}{2P}\right)
```

so

```{math}
m' &= \frac{P\left(\frac{y - p}{v} + s + \frac{S}{P}(s - m)\right) + \left(S + \frac{\kappa}{n v}\right) m}{P + S + \frac{\kappa}{n v}} \\
&= \frac{s\left(P + S + \frac{\kappa}{n v}\right) + P\frac{y - p}{v} - \frac{\kappa}{n v}(s - m)}{P + S + \frac{\kappa}{n v}} \\
&= s + \frac{\frac{n}{\kappa}(y - p) - \frac{s - m}{P}}{\frac{\lambda n v}{\kappa} + \frac{1}{P}}.
```

When $\kappa = 1$, this is fixed under the Newton's method MAP solution (it's the same process), justifying the model. Then

$$
P' = \frac{P\left(S + \frac{\kappa}{n v}\right)}{P + S + \frac{\kappa}{n v}}.
$$

## Bias of the dispersion estimate: geometric events

Take a single-elimination event: the player keeps playing until the first loss, so the number of games is $N \sim \mathrm{Geo}(1 - p)$ and the wins are $W = N - 1$. Then

```{math}
E[N] &= \frac{1}{1 - p} = \mu, \qquad p = 1 - \frac{1}{\mu}, \\
\operatorname{Var}(N) &= \frac{p}{(1 - p)^2} = \mu^2 - \mu, \\
E[N^2] &= \frac{1 + p}{(1 - p)^2}, \qquad E[N^3] = \frac{1 + 4p + p^2}{(1 - p)^3},
```

and $U = W - pN = (1 - p)N - 1 = \frac{N}{\mu} - 1$.

Find $B = E\left[(W - \hat p N)^2\right] - E[U^2]$ to first order in $\gamma = \frac{1}{D}$, where

$$
\hat p = \frac{\sum_{i=1}^{D} W_i}{\sum_{i=1}^{D} N_i} = 1 - \frac{D}{\sum_i N_i} = 1 - \frac{1}{\hat\mu}, \qquad \hat\mu = \frac{\sum_i N_i}{D}.
$$

Say without loss of generality $N_0 = N$. Then

$$
\hat\mu = \frac{D - 1}{D}\mu' + \gamma N, \qquad \mu' \sim \mathcal N\!\left(\mu, \frac{\mu^2 - \mu}{D - 1}\right),
$$

so

$$
\hat\mu \approx (1 - \gamma)\mu + \sqrt{\gamma - \gamma^2}\sqrt{\mu^2 - \mu}\, z + \gamma N, \qquad z \sim \mathcal N(0, 1) \text{ independent of } N.
$$

If $\hat\mu = \mu + \eta$, then

$$
\eta \approx \gamma(N - \mu) + \sqrt{\gamma}\sqrt{\mu^2 - \mu}\, z, \qquad E[z] = 0, \quad E[z^2] = 1.
$$

Expand

```{math}
B &= E\left[\left(U + (p - \hat p)N\right)^2\right] - E[U^2] \\
&= E\left[2\left(\frac{N}{\mu} - 1\right)(p - \hat p)N + (p - \hat p)^2 N^2\right],
```

and write

$$
p - \hat p = \frac{1}{\hat\mu} - \frac{1}{\mu} \approx -\frac{\eta}{\mu^2} + \frac{\eta^2}{\mu^3}.
$$

Substitute, keeping only first-order terms in $\gamma$, dropping terms with $E[z] = 0$ and substituting $E[z^2] = 1$:

```{math}
B &= E\left[2\left(\frac{N}{\mu} - 1\right)\left(-\frac{\gamma(N - \mu)}{\mu^2} + \frac{\gamma(\mu^2 - \mu)}{\mu^3}\right)N + \frac{\gamma(\mu^2 - \mu)}{\mu^4}N^2\right] \\
&= \frac{\gamma}{\mu^3} E\left[2(N - \mu)(2\mu - N - 1)N + (\mu - 1)N^2\right] \\
&= \frac{\gamma}{\mu^3} E\left[6\mu N^2 - 2N^3 - 2N^2 - 4\mu^2 N + 2\mu N + \mu N^2 - N^2\right] \\
&= \frac{\gamma}{\mu^3}\left[-2E[N^3] + (7\mu - 3)E[N^2] + (2\mu - 4\mu^2)E[N]\right] \\
&= \gamma(1 - p)^3\left[\frac{-2 - 8p - 2p^2}{(1 - p)^3} + \frac{\left(7 - 3(1 - p)\right)(1 + p)}{(1 - p)^3} + \frac{2(1 - p) - 4}{(1 - p)^3}\right] \\
&= \gamma\left[-2 - 8p - 2p^2 + 4 + 7p + 3p^2 + 2 - 2p - 4\right],
```

so

$$
B = \gamma\left(p^2 - 3p\right).
$$

Over the $D$ events of a row the scatter is $E\left[\sum_i (W_i - \hat p N_i)^2\right] \approx Dp + p^2 - 3p = p(D - 3 + p)$, against $Dp$ from Wald's identity with the true $p$.
