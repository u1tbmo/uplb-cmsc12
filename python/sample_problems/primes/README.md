# prime.py

This program takes a positive integer n, and determines whether n is prime or composite.

## Logic

1. Take an input n from the user (and check if it is a positive integer).
2. Check the range(2, sqrt of n) for factors of n.
3. If a factor is found, immediately break out of the loop and print that n is composite.
4. If no factor is found, print that n is prime.

## Code Explanation

> Take an input n from the user (and check if it is a positive integer).

```python
n = int(input("Enter a positive integer: "))

if n < 2:
    raise ValueError("n must be at least two.")
```

> Check the range(2, sqrt of n) for factors of n.

```python
is_prime = True
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
```

> Print that n is prime or composite.

```python
match is_prime:
    case True:
        print(f"{n} is prime.")
    case False:
        print(f"{n} is composite.")
```

### Further explanation

Why only up to the square root of the input?

This is because we can DEFINITELY find a factor of n in the range(2, sqrt of n) if there is one.

The proof is as follows.

Consider a number N, and its factors a and b.

$N=a\cdot b$

The factors a and b can be equal to each other or one is less that the other, assume a is less than or equal to b.

$a\leq b$

Multiply the relation by a and b.

$(a\leq b)\cdot a$

$=a^2\leq ab$

$(a\leq b)\cdot b$

$=ab\leq b^2$

Therefore we can conclude that $a^2\leq ab\leq b^2$

We know that $N = ab$

Therefore $a^2\leq N\leq b^2$

Taking the square root of all three terms, we get $\sqrt{a^2}\leq\sqrt{N}\leq\sqrt{b^2}$

Therefore $a\leq\sqrt{N}\leq b$

Which means that there is a factor of $N$ that is less than $\sqrt{n}$, $a$.

## number_of_primes.py

This program takes a positive integer n and prints the number of primes between n and 2n.

### Logic for number_of_primes.py

1. Use the logic for prime.py and define it as a function.
2. Take an input n from the user (and check if it is a positive integer).
3. Check the range(n, 2n) for primes.
4. If a number is prime, increment the counter by 1.
5. Print the counter.

#### Code Explanation for number_of_primes.py

> Use the logic for prime.py and define it as a function.

```python
def prime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime
```

> Check the `range(n, 2n)` for primes.

```python
count = 0
for number in range(n,2*n):
    count += 1 if prime(number) else 0
```

> Print the counter.

```python
print(f"There are {count} primes between {n} and {2*n}.")
```

## twin_primes.py

This program finds the first 30 pairs of twin primes.

### Logic for twin_primes.py

1. Define the logic for prime.py as a function.
2. Define the logic for twin primes as a function. Where twin primes are defined as two primes that differ by 2.
3. Starting from 3, check if the number is prime and if the next odd number is prime. Then check if they are twin primes.
4. If they are, print them and increment the counter by 1.

#### Code Explanation for twin_primes.py

> Define the logic for twin primes as a function. Where twin primes are defined as two primes that differ by 2.

```python
def twin_prime(num1, num2):
    difference = num1 - num2
    if difference < 0:
        difference *= -1
    is_twin_prime = True if difference == 2 else False
    return is_twin_prime
```

> Starting from 3, check if the number is prime and if the next odd number is prime. Then check if they are twin primes.
> If they are, print them and increment the counter by 1.

```python
i = 3
while count < 30:
    if (prime(i) and prime(i+2)) and twin_prime(i,i+2):
        count += 1
        print(f"{count}: ({i},{i+2})")
    i += 1
```
