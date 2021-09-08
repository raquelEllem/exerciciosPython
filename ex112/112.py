from ex112.utilidadeCeV import moeda
from ex112.utilidadeCeV import dados

p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 15)
