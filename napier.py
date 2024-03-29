def napier(n_decimal):
    result = "2."
    numerators = [1] * n_decimal
    denominators = [n_decimal-i+1 for i in range(n_decimal)]

    for i in range(n_decimal):
        lift_up = 0
        numerators = [10*i for i in numerators]
        for index, (n, d) in enumerate(zip(numerators, denominators)):
            numerators[index] = (n+lift_up) % d
            lift_up = (n+lift_up) // d
        result += str(lift_up)
    print(result)

napier(2000)
