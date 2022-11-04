# Class Number of Quadratic Imaginary Orders

This program computes the class number of quadratic imaginary orders.

Given such an order of discriminant $d$, where $d \equiv 0,1 \pmod 4$, we enumerate the number of triplets $(a, b, c)$ of _coprime_ integers satisfying:
$$-a < b \le a < c, \quad \text{or} \quad 0 \le b \le a = c.$$
The number of such triplets is $h(d)$, the **class number** of $d$.

In the case where $d$ is square-free or 4 times (a square-free number which is not 1 mod 4), this is the class number of a quadratic imaginary field. 

E.g. by Heegner's theorem, this is 1 if and only if $d=-3, -4, -7, -8, -11, -19, -43, -67, -163$. See https://en.wikipedia.org/wiki/Stark%E2%80%93Heegner_theorem for more details.
