while True:
    print('---' * 10)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('---' * 10)
    if num < 0:
        break
    for c in range(1, 11):
        mult = num * c
        print(f'{num} * {c} = {mult}')
print('FIM')
