farenheit = int(input(f"Qual a temperatura que estamos agora aqui na pensyvalnia? "))

def func1(x):
    return 5 * ((x-32) / 9)

celsius = func1(farenheit)

print(f"The temperature {farenheit} in farenheit is {celsius}")
