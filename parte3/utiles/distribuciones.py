import math
from scipy.stats import norm, uniform, binom, nbinom, geom, bernoulli, gamma, expon

# DISTRIBUCIÓN NORMAL EN (0,1)
# fórmula de densidad
def normal_std_pdf(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-x**2 / 2)
    # norm.pdf(x, loc=0, scale=1)

# función de distribución acumulada
def normal_std_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))
    # norm.cdf(x, loc=0, scale=1)

# DISTRIBUCIÓN NORMAL EN (mu, sigma)
# fórmula de densidad
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu)**2) / (2 * sigma**2))
    # norm.pdf(x, loc=mu, scale=sigma)

# función de distribución acumulada
def normal_cdf(x, mu, sigma):
    z = (x - mu) / sigma
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))
    # norm.cdf(x, loc=mu, scale=sigma)

# UNIFORME CONTINUA EN (a, b)
def uniform_pdf(x, a, b):
    return 1 / (b - a) if a <= x <= b else 0
    # uniform.pdf(x, loc=a, scale=b - a)

def uniform_cdf(x, a, b):
    if x < a: return 0
    elif x > b: return 1
    return (x - a) / (b - a)
    # uniform.cdf(x, loc=a, scale=b - a)


# BINOMIAL Bin(n, p)
def binomial_pmf(k, n, p):
    return math.comb(n, k) * p**k * (1 - p)**(n - k)
    # binom.pmf(k, n, p)

def binomial_cdf(k, n, p):
    return sum(binomial_pmf(i, n, p) for i in range(k + 1))
    # binom.cdf(k, n, p)

# BINOMIAL NEGATIVA NegBin(r, p)
# X = nro de fallos hasta el r-ésimo éxito
def negbin_pmf(k, r, p):
    return math.comb(k + r - 1, k) * (1 - p)**k * p**r
    # nbinom.pmf(k, r, p)

def negbin_cdf(k, r, p):
    return sum(negbin_pmf(i, r, p) for i in range(k + 1))
    # nbinom.cdf(k, r, p)

# GEOMÉTRICA geom(p)
def geom_pmf(k, p):
    return (1 - p)**(k - 1) * p if k >= 1 else 0
    # geom.pmf(k, p)

def geom_cdf(k, p):
    return 1 - (1 - p)**k
    # geom.cdf(k, p)

# BERNOULLI Bern(p)
def bernoulli_pmf(x, p):
    if x == 0: return 1 - p
    elif x == 1: return p
    else: return 0
    # bernoulli.pmf(x, p)

def bernoulli_cdf(x, p):
    if x < 0: return 0
    elif x < 1: return 1 - p
    else: return 1
    # bernoulli.cdf(x, p)

# POISSON P(lambda)
def poisson_pmf(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)
    # poisson.pmf(k, lam)

def poisson_cdf(k, lam):
    return sum(poisson_pmf(i, lam) for i in range(k + 1))
    # poisson.cdf(k, lam)

# GAMMA G(alpha, beta)
def gamma_pdf(x, alpha, beta):
    if x < 0: return 0
    return (x**(alpha - 1) * math.exp(-x / beta)) / (math.gamma(alpha) * beta**alpha)
    # gamma.pdf(x, a=alpha, scale=beta)

# gamma.cdf(x, a=alpha, scale=beta)

# EXPONENCIAL e(lambda)
def expon_pdf(x, lamb):
    return lamb * math.exp(-lamb * x) if x >= 0 else 0
    # expon.pdf(x, scale=1/lamb)

def expon_cdf(x, lamb):
    return 1 - math.exp(-lamb * x) if x >= 0 else 0
    # expon.cdf(x, scale=1/lamb)

