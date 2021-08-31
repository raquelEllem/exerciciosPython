print('==' * 10)
print('   10 TERMOS DE UMA PA     ')
print('==' * 10)
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
#decimo = primeiroTermo + (10 - 1) * razao
decimo = razao * 10
#for c in range(primeiroTermo, decimo + razao, razao):
for c in range(primeiroTermo, decimo, razao):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
