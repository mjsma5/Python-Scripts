def setup():
    f = open('kmers.txt', 'r')
    content = []
    for line in f.readlines():
        content.append([x for x in line.split()])
    f.close()
    return content


def radix_sortLSD():
    # implements a radix sort algorithm on generated ACGT strings.
    content = setup()
    length = len(content)
    for n in range(len(content[0][1]) // 4):
        buckets = [[] for i in range(256)]
        for x in range(length):
            item = content[x][1]
            segment = item[len(item) - (n*4) - 4:len(item) - (n*4) + 1]
            segment = segment.rjust(4, '0') # padding
            index = 0
            for t in range(3, -1, -1):  # converts base4 to base 10 for bucket placement
                index += int(segment[t]) * 4 ** (t ** (3 - t))
            buckets[index].append(content[x])
        content = []
        for bucket in buckets:
            if len(bucket) != 0:
                for item in bucket:
                        content.append(item)
    f = open('out.txt', 'w')
    f.write('  Kmer            Integer Encodings          String Number\n')
    f.write('----------------------------------------------------------\n')
    for n in range(len(content)):
        f.write(str(content[n]) + '\n')
    f.close()


radix_sortLSD()
