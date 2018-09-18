#! /usr/local/bin/python

import click

safety = set(['+', '-', '*', '/', '//', '**', '%'])

@click.command()
@click.argument('num1')
@click.argument('num2', default='1')
@click.option('--operator', '-o', help='what operator', default='+')
def count7(num1, num2, operator):
        print 'num1', num1 
	'''
	Command line tool to do simple demo calculation between two numbers.

        The operator list is {0} to avoid malicious injection.
	'''.format(safety)

        if num1.isdigit() and num2.isdigit() and operator in safety:
            try:
	        expression = num1 + operator + num2
	        print eval(expression)
            except:
                print 'something is wrong'
        else:
            print 'input number(s) and an arithmetic operator'

if __name__ == '__main__':
	count7()
