import sys
print('Numeros de parametros: %d' % len(sys.argv))
for i, e in enumerate(sys.argv):
    print('parametro %d: %s' % (i, e))

