a, b = float(input()), float(input())

print({
    '+':   a + b,
    '-':   a - b,
    '*':   a * b,
    '/':   a / b if b != 0 else "Деление на 0!",
    'mod': a % b if b != 0 else "Деление на 0!",
    'pow': a ** b,
    'div': a // b if b != 0 else "Деление на 0!"
}[input()])