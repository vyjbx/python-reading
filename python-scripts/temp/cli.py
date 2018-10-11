import click



@click.command()
@click.argument('num')
@click.argument('num2')
@click.option('--operator', '-o', help='what operator')
def count7(num, num2, operator):
	'''
	please use this command line tool
	'''
	expression = num + operator + num2
	print eval(expression)

if __name__ == '__main__':
	count7()