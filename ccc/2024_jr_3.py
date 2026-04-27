N = int(input())

scores = {}
for _ in range(N):
    score = int(input())
    if score in scores:
        scores[score] += 1
    else:
        scores[score] = 1
different_scores = list(scores.keys())
different_scores.sort(reverse=True)
bronze_score = different_scores[2]
bronze_count = scores[bronze_score]
print(bronze_score, bronze_count)