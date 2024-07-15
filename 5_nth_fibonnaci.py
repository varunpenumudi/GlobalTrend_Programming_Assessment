def fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("0th Fibbonaci number is:", fib(0))
    print("6th Fibbonaci number is:", fib(6))
    print("4th Fibbonaci number is:", fib(4))
