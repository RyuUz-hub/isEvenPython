arqv = open('utils.py', 'w', encoding='utf-8')
num = 1
arqv.write('def isEven(number):\n')
arqv.write('    if number == 0: return True\n')
arqv.close()
arqv = open('utils.py', 'a', encoding='utf-8')
while num <= 1000000:
    arqv.write(f'    elif number == {num}: return {num % 2 == 0}\n')
    num += 1

arqv.close()