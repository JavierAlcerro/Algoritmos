class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class PostfixEvaluator:
    def __init__(self):
        self.stack = Stack()
        self.variables = {}

    def evaluate(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():  # Si es un número
                self.stack.push(int(token))
            elif token.isalnum():  # Si es una variable
                if token in self.variables:
                    self.stack.push(self.variables[token])
                else:
                    print(f"Error: Variable {token} no está definida.")
                    return None
            elif token in ['+', '-', '*', '/']:
                self.perform_operation(token)
            elif token == '=':
                self.perform_assignment()
            self.print_stack()

        return self.stack.pop()

    def perform_operation(self, operator):
        right = self.stack.pop()
        left = self.stack.pop()
        if left is None or right is None:
            return
        if operator == '+':
            self.stack.push(left + right)
        elif operator == '-':
            self.stack.push(left - right)
        elif operator == '*':
            self.stack.push(left * right)
        elif operator == '/':
            self.stack.push(left / right)

    def perform_assignment(self):
        right = self.stack.pop()
        var = self.stack.pop()
        if var is not None and isinstance(var, str):
            self.variables[var] = right
            self.stack.push(right)  # La asignación devuelve el valor del lado derecho
        else:
            print("Error: Se requiere una variable en el lado izquierdo de la asignación.")

    def print_stack(self):
        print(f"Pila: {self.stack.items}")

# Ejemplo de uso
if __name__ == "__main__":
    evaluator = PostfixEvaluator()
    postfix_expression = "A 3 2 * ="
    result = evaluator.evaluate(postfix_expression)
    print(f"Resultado de la evaluación: {result}")
    print(f"Valor de A: {evaluator.variables.get('A')}")
