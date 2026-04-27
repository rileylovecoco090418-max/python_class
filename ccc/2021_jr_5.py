import sys

def main():
    input = sys.stdin.readline
    M = int(input().strip())
    N = int(input().strip())
    K = int(input().strip())
    row = bytearray(M + 1)
    col = bytearray(N + 1)
    
    for _ in range(K):
        typ, num = input().split()
        idx = int(num)
        if typ == 'R':
            row[idx] ^= 1
        else: 
            col[idx] ^= 1

    oddR = sum(row)
    oddC = sum(col)
    gold = oddR * (N - oddC) + (M - oddR) * oddC
    print(gold)

if __name__ == "__main__":
    main()