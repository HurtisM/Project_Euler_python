import math


class Primes:
    """Efficient prime utilities for Project Euler problems."""

    def __init__(self, limit=100000):
        self.limit = limit
        self._sieve = self._generate_sieve(limit)
        self._primes = [i for i, is_p in enumerate(self._sieve) if is_p]

    def _generate_sieve(self, limit):
        sieve = bytearray(b"\x01") * (limit + 1)
        sieve[0:2] = b"\x00\x00"
        for i in range(2, int(math.isqrt(limit)) + 1):
            if sieve[i]:
                sieve[i * i:limit + 1:i] = b"\x00" * ((limit - i * i) // i + 1)
        return sieve

    def _extend_if_needed(self, n):
        while n > self.limit:
            self.limit *= 2
            self._sieve = self._generate_sieve(self.limit)
            self._primes = [i for i, is_p in enumerate(self._sieve) if is_p]

    def is_prime(self, n):
        self._extend_if_needed(n)
        return bool(self._sieve[n])

    def nth(self, k):
        while len(self._primes) < k:
            self.limit *= 2
            self._sieve = self._generate_sieve(self.limit)
            self._primes = [i for i, is_p in enumerate(self._sieve) if is_p]
        return self._primes[k - 1]

    def primes_up_to(self, n=None):
        if n is None or n > self.limit:
            n = self.limit
        return [p for p in self._primes if p <= n]


    def primes_in_range(self, start, end):
        """Return all primes between start and end inclusive."""
        if end > self.limit:
            # Extend sieve if needed
            self.limit = end
            self._sieve = self._generate_sieve(end)
            self._primes = [i for i, is_p in enumerate(self._sieve) if is_p]
        # Filter primes in the desired range
        return [p for p in self._primes if start <= p <= end]