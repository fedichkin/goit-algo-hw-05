def caching_fibonacci():
    cache = {}

    def fibonacci(n: int):
        if n <= 0:
            return 0

        if n == 1:
            return 1

        # get fibonacci number from cache if it's on the cache
        if n in cache:
            return cache[n]

        # calc next fibonacci number if it's not on the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main():
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
    print(fib(25))


if __name__ == '__main__':
    main()
