# Sum-O-Primes

Source: https://play.picoctf.org/practice/challenge/310

Known RSA Parameter: $X=p+q$, $N=p * q$, Encryption Key: $e=65537$, Ciphertext

### Method 1

While this method is more labor-intensive, it also enables the computation of the two prime numbers $p$ and $q$.

Given that $x = p + q$ and $n = p \cdot q$, we can deduce $p - q$ using the formula $(p - q)^2 = (p + q)^2 - 4pq$.

More explicitly, $p - q = \sqrt{(p + q)^2 - 4pq}$.

Subsequently, we can find $p$ by calculating $p = \frac{(p + q) + (p - q)}{2}$, and $q$ can be derived as $q = (p + q) - p$.
### Method 2

Personally, I prefer this approach. In my opinion, this approach is more intuitive and straightforward. 

We can directly compute Euler's totient function, $\phi(n) = (p-1)(q-1)$. This simplifies to $\phi(n) = pq - p - q + 1 = N - (p + q) + 1$, where $N = pq$ represents the product of the primes and $X = p + q$.

With these values, calculating the decryption key $d$, which is the modular multiplicative inverse of $e$ modulo $N$, becomes straightforward. Consequently, decrypting the ciphertext is also achievable.
