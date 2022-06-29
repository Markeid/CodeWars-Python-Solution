def digital_root(n):
    return n if n < 10 else digital_root(sum([int(sum) for num in str(n)]))

# 2ª solução #
def digital_root(n):
    somas = soma([int(num) for num in str(n)])
    if len(str(somas)) >= 2:
        somas = digital_root(somas)
    return somas

# 3ª solução #
def digital_root(n):
    return n % 9 or n and 9