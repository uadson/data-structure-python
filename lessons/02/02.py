from time import time

from math import inf


def max_num(iterable):
	"""
		Análise de algorítmo em tempo de execução O(n)

		Em memória O(1)
	"""
	# variável recebe um valor absurdamente baixo
	n_max = -inf 

	for n in iterable:
		# se n for maior que n_max, n_max é atualizado com o valor de n
		if n > n_max:
			n_max = n
	return n_max


if __name__ == '__main__':
	print(max_num([1]))
	print(max_num([10]))

	print("Estudo Experimental sobre o tempo de execução da função max_num\n")

	start = 10_000_000
	
	for n in range(0, start * 20 + 1, start):

		start = time()
		max_num(range(n))

		end = time()
		execution_time_seconds = end - start

		print('*' * int(execution_time_seconds * 10), n)

# 1 função constante => acessos a elementos acontecem de maneira constante

# exemplos: o máximo de uma lista ordenada, o acesso a um elemento (conhecido) de uma lista

# 2 função logarítmica
# 3 função linear => o tempo de execução é proporcional ao tamanho de entrada
# 4 função sub-linear
# 5 quadrática
# 6 função cúbica
# 7 função exponencial
