# Squared Errors in Potion Mixtures --- a solution to some problem

We need to compute an optimal partition of a list of numbers into
contiguous parts, where each part contributes the sum of all pairwise
squared errors within that part.  The total cost is the sum over all
parts.

$$\sum_{t=1}^{K} \sum_{\ell_t \leq a < b < r_t} (\text{data}[a] - \text{data}[b])^2$$

We can precompute in linear time `prefix_sum` and `prefix_sum_squared`
and thereby getting $O(1)$ time lookup for the sum of pairwise squared
errors for a block $[\ell, r)$:

```python
prefix_sum = [0] * (n + 1)
prefix_sum_sq = [0] * (n + 1)
for i, x in enumerate(data, 1):
    prefix_sum[i] = prefix_sum[i - 1] + x
    prefix_sum_sq[i] = prefix_sum_sq[i - 1] + x**2


def squared_error(l, r):
    L_sq = prefix_sum_sq[l]
    s = prefix_sum[l] - prefix_sum[r]
    return (l - r) * (L_sq - prefix_sum_sq[r]) - s**2
```


Now, for indices $a \leq b \leq c \leq d$, we have

$$E[a,c)+E[b,d) \leq E[a,d)+E[b,c),$$

so the cost function satisfies the [Monge property](https://en.wikipedia.org/wiki/Monge_array).

Therefore, we can use the [SMAWK algorithm](https://en.wikipedia.org/wiki/SMAWK_algorithm),
or straight-forward dynamic programming with divide-and-conquer
based on monotonicity, to improve the running time from the naïve
$\Omega(n^2 \cdot k)$ to $O(k \cdot n \log n)$.
