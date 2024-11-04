class PostfixTranslator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '=': 0}
        self.output = []
        self.stack = []

    def precedence(self, operator):
        return self.operators.get(operator, -1)

    def is_operator(self, char):
        return char in self.operators

    def translate(self, expression):
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
        for token in tokens:
            if token.isalnum():  # Si es un número o una variable
                self.output.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  # Pop '('
            elif self.is_operator(token):
                while (self.stack and self.is_operator(self.stack[-1]) and
                       self.precedence(token) <= self.precedence(self.stack[-1])):
                    self.output.append(self.stack.pop())
                self.stack.append(token)

        while self.stack:
            self.output.append(self.stack.pop())

        return ' '.join(self.output)

# Ejemplo de uso
if __name__ == "__main__":
    translator = PostfixTranslator()
    expression = "A = 3 * 2"
    postfix = translator.translate(expression)
    print(f"Postfix: {postfix}")
