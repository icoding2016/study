# Expression Evaluation (infix)
# Medium
#  
# to support basic calculation with:
#  - operator: + - * / ^ 
#  - operand: int/float
#  - Parenthesis are permitted
#  - blank(s) allowed in the expression
#
# 
# Solution include 2 parts:
#   1) parse the str, identify operators and operands
#   2) Expression Evaluate 
#      Method ref: http://csis.pace.edu/~murthy/ProgrammingProblems/Programming_Problems.htm#16_Evaluation_of_infix_expressions
# 
# Expression Evaluate:
# Use two stacks:
#   Operand stack: to keep values (numbers)  and
#   Operator stack: to keep operators (+, -, *, . and ^). 
# In the following, “process” means, 
#   (i) pop operand stack once (value1) 
#   (ii) pop operator stack once (operator) 
#   (iii) pop operand stack again (value2) 
#   (iv) compute value1 operator  value2
#   (v) push the value obtained in operand stack.          
# Algorithm:
# Until the end of the expression is reached, get one character and perform only one of the steps (a) through (f):
#   (a) If the character is an operand, push it onto the operand stack.
#   (b) If the character is an operator, and the operator stack is empty then push it onto the operator stack.
#   (c) If the character is an operator and the operator stack is not empty, and the character's precedence is
#       greater than the precedence of the stack top of operator stack, then push the character onto the operator stack.
#   (d) If the character is "(", then push it onto operator stack.
#   (e) If the character is ")", then "process" as explained above until the corresponding "(" is encountered in operator stack.
#       At this stage POP the operator stack and ignore "(."
#   (f) If cases (a), (b), (c), (d) and (e) do not apply, then process as explained above.
# When there are no more input characters, keep processing until the operator stack becomes empty.
#   The values left in the operand stack is the final result of the expression.
# 
# Note
# 
#    
# e.g. 
#   10*3-((6+5)-2*4)^2+20/4 = 
#


class InvalidInput(Exception):
    pass

class ExpressionEvaluator(object):
    OPERATOR = ['+', '-', '*', '/', '^', '(', ')']
    PRIO = {'(':4, ')':4, '^':3, '*':2, '/':2, '+':1, '-':1}

    def __init__(self):
        #self._init_evaluator()
        pass

    def _init_evaluator(self):
        self.operators = []
        self.operands = []
    
    def parse(self, expression: str) -> list[str]:
        """Prase the expression str, split the operators and operand into a list."""
        output = []
        number = ''
        number_exp = [str(i) for i in range(0,10)] + ['.']
        expression.replace(' ', '')  # remove blanks
        for c in expression:
            if c in self.OPERATOR:
                if number:
                    output.append(number)
                    number = ''
                output.append(c)
            elif c in number_exp:
                number += c
            else:
                raise InvalidInput('Expression contains invalid operator/number')
        if number:
            output.append(number)
        # print(output)
        return output

    def evaluate(self, expression: str):
        self._init_evaluator()
        if len(expression) < 3:
            raise InvalidInput('Invalid input.')
        
        for c in self.parse(expression):
            if c not in self.OPERATOR:
                # validate c as a number
                self.operands.append(c)
            elif not self.operators:
                self.operators.append(c)
            elif c == '(':
                self.operators.append(c)
            elif c == ')':
                # process until reach '('
                while self.operators[-1]!='(':
                    self.process()
                if self.operators[-1]=='(':
                    self.operators.pop()     # pop '('
            elif self.PRIO[c] > self.PRIO[self.operators[-1]]:
                self.operators.append(c)
            elif self.PRIO[c] <= self.PRIO[self.operators[-1]]:
                while self.operators and self.operators[-1]!='(':
                    self.process()
                self.operators.append(c)
        while self.operators and self.operators[-1]!='(':
            self.process()
        return self.operands[0]

    def process(self):
        if not self.operands or not self.operators:
            return
        v2 = self.operands.pop()
        op = self.operators.pop()
        v1 = self.operands.pop()
        if op == '^':
            exp = f'int({v1})**int({v2})'
        else:
            exp = f'{v1}{op}{v2}'
        self.operands.append(str(eval(exp)))





def test_fixture(s:ExpressionEvaluator):
    testdata = [  # (input, expect),
        (('3+5*2-1',), 12),
        (('2*3-((6+5)-2*4)+2',), 5),
        (('2+3-(2^2+3*(5-6/2)^2)*2+20',),-7),
        (('5-6/2',),2.0),
        (('3-2',),1),
        (('4*5',),20),
        (('3.0*2+(4.0+2.5*(4/2)+3.5*2)/2.0',),14.0),
    ]
    for i in range(len(testdata)):
        ret = s.evaluate(*testdata[i][0])
        exp = str(testdata[i][1])
        #exp = s.maxProfit_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = ExpressionEvaluator()
    test_fixture(s)
test()
