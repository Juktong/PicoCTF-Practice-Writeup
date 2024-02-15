## Method 1

Known Parameter: $X=p+q$, $N=p * q$, Encryption Key: $e=65537$, Ciphertext

Knowing $x=p+q$ and $n=p*q$, we can calculate $p-q$ by $(p-q)^2=(p+q)^2-4pq$.

More specifically, $p-q=\sqrt{(p+q)^2-4pq}$

And then, we can calculate $p=((p+q)+(p-q))/2$, and $q=(p+q)-q$.

