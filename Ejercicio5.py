def romano_a_decimal(s):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Caso base: string vacío o un solo carácter
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return valores[s[0]]
    
    # Si el actual es menor que el siguiente → resta (ej: IV = -1 + 5)
    if valores[s[0]] < valores[s[1]]:
        return -valores[s[0]] + romano_a_decimal(s[1:])
    else:
        return valores[s[0]] + romano_a_decimal(s[1:])


# Pruebas
print(romano_a_decimal("III"))    # 3
print(romano_a_decimal("IV"))     # 4
print(romano_a_decimal("IX"))     # 9
print(romano_a_decimal("XIV"))    # 14
print(romano_a_decimal("XLII"))   # 42
print(romano_a_decimal("MCMXCIX")) # 1999