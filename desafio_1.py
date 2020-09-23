import math

dist = 149600000
vm = 28440
days = math.ceil((dist/vm) / 24)
print('Tempo em dias: {}'.format(days))

