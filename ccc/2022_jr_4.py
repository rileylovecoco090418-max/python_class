import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2022_jr_4.txt'
print(file_path)

# Read
f = open(file_path, 'r')


# 2022 j4
cond_together = []
X = int(f.readline())
for _ in range(X):
    a, b = f.readline().split()
    cond_together.append((a, b))

cond_separate = []
Y = int(f.readline())
for _ in range(Y):
    a, b = f.readline().split()
    cond_separate.append((a, b))

teams = []
G = int(f.readline())
for _ in range(G):
    a, b, c = f.readline().split()
    team = [a, b, c]
    # team.sort()
    teams.append(team)

# Check the same group rules
# Check a rule in each group
# If one of group matches rule: ok
# Else: not ok


# cnt_cond_together = 0
cnt_cond_separate_violation = 0
for team in teams:
    # Check the condition 1: Needs to be together
    for cond_t in cond_together:
        # This is a good conodition 1
        if set(team).issuperset(cond_t):
            cond_together.remove(cond_t)
            break
    
    # Check the condition 2: Needs to be separated
    cond_to_remove = []
    for cond_s in cond_separate:
        # This is the violation of condition 2
        if set(team).issuperset(cond_s):
            cnt_cond_separate_violation += 1
            cond_separate.remove(cond_s)
            break
        for item in cond_s:
            if item in team:
                cond_to_remove.append(cond_s)

    for cond_s in cond_to_remove:
        cond_separate.remove(cond_s)

num_violations = len(cond_together) + cnt_cond_separate_violation
print(num_violations)
