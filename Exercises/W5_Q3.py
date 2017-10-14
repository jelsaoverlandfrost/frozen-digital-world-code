def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        answer = n * factorial(n - 1)
    return answer

print factorial(-5)