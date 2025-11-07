def e_continued_fraction_terms(n):
    """Return the first n terms of e's continued fraction expansion."""
    terms = [2]
    k = 1
    while len(terms) < n:
        # pattern repeats as [1, 2k, 1]
        terms.extend([1, 2 * k, 1])
        k += 1
    return terms[:n]


def convergent_fraction(terms):
    """Compute numerator and denominator of the convergent given the terms."""
    # initialize previous two numerators (p) and denominators (q)
    p_minus2, p_minus1 = 0, 1
    q_minus2, q_minus1 = 1, 0
    for a in terms:
        p = a * p_minus1 + p_minus2
        q = a * q_minus1 + q_minus2
        p_minus2, p_minus1 = p_minus1, p
        q_minus2, q_minus1 = q_minus1, q
    return p, q


def sum_digits(n):
    return sum(int(d) for d in str(n))


if __name__ == '__main__':

    terms = e_continued_fraction_terms(100)
    numerator, denominator = convergent_fraction(terms)
    result = sum_digits(numerator)

    print("Numerator of 100th convergent:", numerator)
    print("Sum of its digits:", result)
