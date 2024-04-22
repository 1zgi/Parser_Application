from Parser import Parser

nameTxt = input('Enter the name of the correct inputs file as "input.txt" \n or wrong inputs file as "inputWrong.txt" '
                'format: \n')
parser = Parser(nameTxt)

parser.G()
