
# AND = para ser true yudo tem que ser true
# OR = para ser true um dos dois tem que ser true

print(True and True)
print(True and False)
print(False or True)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp1)

saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial = (conta_especial and saldo >= saque)

exp3 = (saldo_suficiente or conta_especial)
print(exp3)
