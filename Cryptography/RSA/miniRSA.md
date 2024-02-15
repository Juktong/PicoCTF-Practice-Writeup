# 2019 miniRSA
In the RSA encryption scheme, the relationship between ciphertext ($ct$) and plaintext ($pt$) is given by $ct = pt^e \mod N$, where $ct$ represents the ciphertext, and $pt$ represents the plaintext. Therefore, there exists a $k \in \mathbb{Z}$ such that $k \cdot N + ct = pt^e$. Given that the encryption key ($e$) is small, specifically $e = 3$, we can incrementally search for $k$ starting from 1, and compute $pt = (k \cdot N + ct)^{\frac{1}{3}}$, continuing until $pt$ is an integer.

The implementation details can be found in the [miniRSA.sage](https://github.com/Juktong/PicoCTF-Practice-Writeup/blob/main/Cryptography/RSA/miniRSA.sage) file.

Reference:
1. num2str function: https://github.com/DuanYuFi/CTF_Crypto-all-in-one
