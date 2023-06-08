for number in range(1, 101):
  # if number % 3 == 0 or number % 5 == 0:
  # En este caso no tenemos que usar un or, sino un and,
  # ya que se tienen que cumplir las dos condiciones para
  # que se imprima FizzBuzz
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # if number % 3 == 0:
  # En lugar de if, necesitamos una sentencia elif, para 
  # que no siga comparando las siguienten sentencias una 
  # vez que se cumpla alguna
  elif number % 3 == 0:
    print("Fizz")
  #  if number % 5 == 0:
  elif number % 5 == 0:
    print("Buzz")
  else:
    # print([number])
    # Cambiamos la sentencia print, ya que el número
    # se tiene que imprimir sin paréntesis cuadrados
    print(number)