#백준_20492

N = int(input())

tax = N * 0.78

tax_neces = N - (N * 0.2 * 0.22)

print(int(tax), int(tax_neces))