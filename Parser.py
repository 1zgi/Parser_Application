class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.error = False
        self.next_token = ''
        self.unconsumed_input = ''

    def lex(self):
        with open(self.filename, 'r') as file:
            data = file.read().replace(' ', '')
            self.unconsumed_input = data
            self.next_token = data[0]
            self.unconsumed_input = self.unconsumed_input[1:]

    def unconsumed_input(self):
        return self.unconsumed_input

    def G(self):
        self.lex()
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
        if self.next_token == '+':
            print("R -> + T R")
            self.lex()
            self.T()
            self.R()
        elif self.next_token == '-':
            print("R -> - T R")
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
        if self.next_token == '*':
            print("S -> * F S")
            self.lex()
            self.F()
            self.S()
        elif self.next_token == '/':
            print("S -> / F S")
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
                print("error: unexpected token ", self.next_token)
                print("unconsumed input ", self.unconsumed_input)
                return
        elif self.next_token in ['a', 'b', 'c', 'd']:
            print("F -> M")
            self.M()
        elif self.next_token in ['0', '1', '2', '3']:
            print("F -> N")
            self.N()
        else:
            self.error = True
            print("error: unexpected token ", self.next_token)
            print("unconsumed input ", self.unconsumed_input)

    def M(self):
        if self.error:
            return
        if self.next_token in ['a', 'b', 'c', 'd']:
            print("M -> ", self.next_token)
            self.lex()
        else:
            self.error = True
            print("error: unexpected token ", self.next_token)
            print("unconsumed input ", self.unconsumed_input)

    def N(self):
        if self.error:
            return
        if self.next_token in ['0', '1', '2', '3']:
            print("N -> ", self.next_token)
            self.lex()
        else:
            self.error = True
            print("error: unexpected token ", self.next_token)
            print("unconsumed input ", self.unconsumed_input)
