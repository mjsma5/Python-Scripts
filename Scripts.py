def factorial(n):
    # calculates n factorial
    if n == 1 or n == 2:
        return n
    else:
        result = 1
        for a in range(1, n + 1):
            result = result * a
        return result


def baseConversion_ten_factorial(iteration, n):
    # converts Base-10 to Base-!
    remainder = iteration
    result = []
    for a in range(n - 1, -1, -1):
        if remainder != 0:
            count = 1
            truth = True
            while truth:
                total_f = count * factorial(a)
                if total_f == remainder:
                    result.append(count)
                    remainder -= total_f
                    truth = False
                elif total_f < remainder:
                    count += 1
                else:
                    count -= 1
                    result.append(count)
                    remainder -= (count * factorial(a))
                    truth = False
        else:
            result.append(int(0))
    return result
