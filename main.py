from Parser import Parser

nameTxt = input('Enter the name of the correct inputs file as "input.txt" \n or wrong inputs file as "inputWrongs.txt" '
                'format: \n')
parser = Parser(nameTxt)

parser.G()
