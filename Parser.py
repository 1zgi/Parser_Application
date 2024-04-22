class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.error = False
        self.next_token = ''
        self.unconsumed_input = ''
        self.lex()  # Prime the lexer to get the first token

    def lex(self):
        if not self.unconsumed_input:
            with open(self.filename, 'r') as file:
                self.unconsumed_input = file.read().replace(' ', '') + '$'
        self.next_token = self.unconsumed_input[0]
        self.unconsumed_input = self.unconsumed_input[1:]

    def unconsumed_input(self):
        return self.unconsumed_input

    def G(self):
        print("G -> E")
        self.E()
        if self.next_token == '$' and not self.error:
            print("success")
        else:
            print("failure: unconsumed input=%s" % self.unconsumed_input)

    def E(self):
        if self.error:
            return
        print("E -> T R")
        self.T()
        self.R()

    def R(self):
        if self.error:
            return
        if self.next_token in ['+', '-']:
            print("R -> %s T R" % self.next_token)
            self.lex()
            self.T()
            self.R()
        else:
            print("R -> e")

    def T(self):
        if self.error:
            return
        print("T -> F S")
        self.F()
        self.S()

    def S(self):
        if self.error:
            return
        if self.next_token in ['*', '/']:
            print("S -> %s F S" % self.next_token)
            self.lex()
            self.F()
            self.S()
        else:
            print("S -> e")

    def F(self):
        if self.error:
            return
        if self.next_token == '(':
            print("F -> ( E )")
            self.lex()
            self.E()
            if self.next_token == ')':
                self.lex()
            else:
                self.error = True
                print("error: expected ')' but got '%s'" % self.next_token)
        elif self.next_token in ['a', 'b', 'c', 'd']:
            print("F -> M")
            self.M()
        elif self.next_token in ['0', '1', '2', '3']:
            print("F -> N")
            self.N()
        else:
            self.error = True
            print("error: unexpected token '%s'" % self.next_token)

    def M(self):
        if self.error:
            return
        if self.next_token in ['a', 'b', 'c', 'd']:
            print("M -> %s" % self.next_token)
            self.lex()
        else:
            self.error = True
            print("error: unexpected token '%s'" % self.next_token)

    def N(self):
        if self.error:
            return
        if self.next_token in ['0', '1', '2', '3']:
            print("N -> %s" % self.next_token)
            self.lex()
        else:
            self.error = True
            print("error: unexpected token '%s'" % self.next_token)
