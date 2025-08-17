N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

fraud_scores = 0
for n in scores:
    fraud_score = (n / max_score) * 100
    fraud_scores += fraud_score

result = fraud_scores / N

print(result)