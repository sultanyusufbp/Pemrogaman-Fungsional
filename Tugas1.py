# Fungsi Pengurangan
def minus(a, b):
    return a - b

# Fungsi Perkalian
def mult(a, b):
    return a * b

# Fungsi Pembagian
def div(a, b):
    if b == 0:
        return "Tidak dapat membagi oleh nol."
    return a / b

def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        if operator == '+':
            return tree(left) + tree(right)
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return expression

expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:",result)
