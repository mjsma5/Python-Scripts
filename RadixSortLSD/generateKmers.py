def generate_kmers(k):
    # Generates 'A', 'C', 'G', 'T' string combinations of k length from DNA sequence file to simulate DNA subsets
    f = open('longstring.txt', 'r')
    content = f.read()
    f.close()
    kmers = []
    for n in range(len(content)-k):
        kmers.append(content[n:k + n])
    integer_encoded_kmers = []
    for n in range(len(kmers)):
        integer_encoded_kmers.append(encoding_conversion(kmers[n]))
    f = open('kmers.txt', 'w')
    for n in range(len(integer_encoded_kmers)-1):
        f.write(str(kmers[n]) + '      ' + str(integer_encoded_kmers[n]) + '       ' + str(n) + '\n')
    f.close()


def encoding_conversion(kmer):
    kmer = kmer.replace("A", '0')
    kmer = kmer.replace("C", '1')
    kmer = kmer.replace("G", '2')
    kmer = kmer.replace("T", '3')
    return kmer



generate_kmers(17)
