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


def radix_sortLSD(content):
    for n in range(1, len(content[0][0])/4):
        buckets = [[] for i in range(256)]
        for x in range(len(content[0][0])):
            value = content[x][1]
            segment = value[-n:-((n*4)+1)]
            if len(segment) < 4:   # padding
                for l in range(4 - len(segment)):
                    segment = '0' + segment
            for t in range(4):
                value += int(segment[t]) * 5 ** (3-t)
            buckets[value].append(content[x])
        content = []
        for bucket in buckets:
            content.extend(bucket)
    return content