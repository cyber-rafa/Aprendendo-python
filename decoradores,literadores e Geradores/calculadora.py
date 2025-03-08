def calculadora(operacao):
  def soma(a, b):
    return a + b

  def subtracao(a, b):
    return a - b
  
  def mult(a, b):
    return a * b

  def div(a, b):
    return a / b

  match operacao:
    case '+':
      return soma
    case '-':
      return subtracao
    case '*':
      return mult
    case '/':
      return div 

op = calculadora('+')
print(op(2,3))

op = calculadora('-')
print(op(2,3))  

op = calculadora('*')
print(op(2,3))

op = calculadora('/')
print(op(2,2))