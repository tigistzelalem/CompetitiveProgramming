
def sentence(n):
        if n == 1:
            return 'I hate it'
        elif n == 2:
            return 'I hate that I love it'
        elif n == 3:
            return 'I hate that I love that I hate it'
        else:
            if n % 2 == 0:
                return 'I hate that I love ' +  sentence(n-1)
            else:
                return 'I hate that ' + sentence(n-1)
        

n = list(map(int, input().split()))

for num in n:
    if num < 0:
        continue
    print(sentence(num))
