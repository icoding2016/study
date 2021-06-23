"""
prefix/infix/postfix notation
-----------------------------

e.g. 
    Infix Expression        Prefix Expression       Postfix Expression
    A + B * C + D           + + A * B C D           A B C * + D +
    (A + B) * (C + D)       * + A B + C D           A B + C D + *
    A * B + C * D           + * A B * C D           A B * C D * +
    A + B + C + D           + + + A B C D           A B + C + D +
    10 + 3 * 5 / (16 - 4)   + 10 / * 3 5 - 16 4     10 3 5 * 16 4 - / +


[infix/prefix/postfix conversion]

infix -> prefix:  
  e.g.    (A+B)*(C+D)/E+F => (((A+B)*(C+D))/E)+F
                          => +/*+AB+CDEF

  solution:
  - recursive.
    Each recursion just handle the infix without (). the content inside a bracket is handled by recursion calls.
    stacking operators and operands, process expression based on poerator priority.
  - imperative.


  ref: https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
  

[infix calculation]:
  Brief idea: 
    Following the pattern "A <operator> B".  
    When reaching an operator with higher _PRIOrity or a '(', push the old operand/operator to stack and start a new "A <opertor> B"
    When reachnig an operator with lower _PRIOrity or a ')', calculate the preceding 'A <operator> B' and turn it into an operand A', then continue the pattern of A' <operator> B'
    The 'start new' status is used to decide if the calculation needs to be performed when reaching an operator, so need to be tracked for each step.

  3 types of elements (number, operator, bracket)
  - number:    adding up if there is a number in last step   (cache)-> operand
  - operator:
    what to do:
      1) end current operand:  if operand != None, push it and set operand=None     (for the case  'A <operator> B' )
      2) if current_operator <= last_operator, calculate current 'A <operator> B'.  e.g. 5+3-..     or 5*3-..
         the result and current_operator should be pushed to stack.  (there should be an operand following current operator)
      3) if current_operator > last_operator,  push the operator and the operand (then clear operand =None),  
         so the 'A <operator> B' pattern can continue
      4) push or restore 'start_new' status. 
         if no calculation, push start_new status and update it to False, else pop the old start_new status
  - (
    what to do:
      1) start of a new serial of formula, (before that could be nothing or have some operand/operator pushed)
         so operand should be None, 
         'start_new' flag should be pushed and updated to True (then the next operator may know it a new set of calculation, no need to compare with the last_operator)
       
  - )
    what to do:
      1) finish current 'A <operator> B' calculation (there must be an operand cached before this ")", and an operand and an operator in stack)
         the result should be cached in operand. e.g. "C <operator> (A+B)", the "A+B" result should be in operand when the "()" is processed
      2)'start_new' flag should be popped

  - 


"""


from utils.testtools import test_fixture


class InfixExpression():
    _OPERATORS = ['+', '-', '*', '/']
    _PRIO = { '(':5, ')':5, '*':2, '/':2, '+':1, '-':1}  # the bigger the higher

    def __init__(self):
        pass

    @classmethod
    def value(cls, infix:str) -> float:
        """Calculate the input maths formula. (imperative solutoin)
           
           Assume the operands are digit numbers (int).
           well if need support float, then cache c into num if c.isdigit() or c=='.', then convert float(num)
        """
        return cls._value_r(infix)
        # return cls._value(infix)

    def _value(cls, infix:str) -> float:
        """Calculate the input maths formula. (imperative solutoin)
        """
        stack_operator = []
        stack_operand = []
        stack_status = []
        operand = None
        start_new = True
        # infix = f'({infix})'
        for c in infix:
            if c.isdigit():
                if operand == None:
                    operand = int(c)
                else:
                    operand = operand * 10 + int(c)
            elif c in cls._OPERATORS:
                if start_new:
                    # stack_status.append(start_new)
                    start_new = False
                else:
                    # notice: use while here not if, e.g. case  a-b*c-e*f+g -> a-<x>-<x>+g
                    while not start_new and stack_operator and cls._PRIO[c] <= cls._PRIO[stack_operator[-1]]:   
                        operand = cls._calc(stack_operator.pop(), stack_operand.pop(), operand)
                        start_new = stack_status.pop()
                stack_operand.append(operand)
                operand = None
                stack_operator.append(c)
                stack_status.append(start_new)
            elif c == '(':
                stack_status.append(start_new)
                start_new = True
            elif c == ')':
                if stack_operator:
                    operand1 = stack_operand.pop()
                    operand = cls._calc(stack_operator.pop(), operand1, operand)
                start_new = stack_status.pop()
        while stack_operator:
            operand1 = stack_operand.pop()
            operand = cls._calc(stack_operator.pop(), operand1, operand)
        return operand  #stack_operand[0]

    @classmethod
    def _value_r(cls, infix:str) -> float:
        """Calculate the input maths formula. (recursive solutoin)
           
           Assume the operands are digit numbers (int).
           well if need support float, then cache c into num if c.isdigit() or c=='.', then convert float(num)
        """
        stack_num = []
        stack_opr = []
        opr = num = None
        i = 0
        while i < len(infix):
            c = infix[i]
            jumpto = None
            if c == ' ':
                continue
            elif c.isdigit():
                num = int(c) if num==None else num*10+int(c)
            elif c == '(':
                j = i + 1
                count = 1
                while j<len(infix):
                    if infix[j] == '(':
                        count += 1
                    elif infix[j] == ')':
                        count -= 1
                        if count == 0:
                            break
                    j += 1
                num = cls._value_r(infix[i+1:j])
                jumpto = j+1
            elif c == ')':
                raise Exception('should not happen.')
                #while stack_opr:
            elif c in cls._OPERATORS:
                while stack_opr and cls._PRIO[c] <= cls._PRIO[stack_opr[-1]]:
                    num = num if num != None else stack_num.pop()
                    num = cls._calc(stack_opr.pop(), stack_num.pop(), num)
                stack_opr.append(c)
                stack_num.append(num)
                num = None
            i = jumpto if jumpto else i+1
        while stack_opr:
            num = num if num != None else stack_num.pop()
            num = cls._calc(stack_opr.pop(), stack_num.pop(), num)
        return num

    @classmethod
    def _calc(cls, operator:str, operand1:float, operand2:float) -> float:
        """Do calculation.
        """
        # Can handle by each operator or simply use eval()

        # if operator == '+':
        #     return operand1 + operand2
        # elif operator == '-':
        #     return operand1 - operand2
        # elif operator == '*':
        #     return operand1 * operand2
        # elif operator == '/':
        #     return operand1 / operand2
        return eval(f'{operand1}{operator}{operand2}')


    @classmethod
    def infix_to_prefix(cls, infix:str) -> str:
        """Convert infix expression to prefix expression (space separated)."""
        # return cls._infix_to_prefix_r(infix)
        return cls._infix_to_prefix(infix)

    # has issue
    @classmethod
    def _infix_to_prefix(cls, infix:str) -> str:
        """Convert infix expression to prefix expression (space separated). (imperative solution)"""
        stack_opr = []
        stack_obj = []
        stack_state = []
        obj = None
        restart = True
        for c in infix:
            if c==' ':
                continue
            elif c in cls._OPERATORS:
                while not restart and stack_opr and cls._PRIO[c] <= cls._PRIO[stack_opr[-1]]:
                    if None == obj:
                        obj = stack_obj.pop()
                    obj = f'{stack_opr.pop()} {stack_obj.pop()} {obj}'
                stack_opr.append(c)
                restart = False
                if obj:
                    stack_obj.append(obj)
                obj = None
            elif c == '(':
                if obj:
                    stack_obj.append(obj)
                    obj = None
                stack_state.append(restart)
                restart = True
            elif c == ')':
                obj = f'{stack_opr.pop()} {stack_obj.pop()} {obj}'
                stack_obj.append(obj)
                obj = None
                restart = stack_state.pop()
            else:
                if None == obj:
                    obj = c
                else:
                    obj += c
        while stack_opr:
            if obj == None:
                obj = stack_obj.pop()
            obj = f'{stack_opr.pop()} {stack_obj.pop()} {obj}'
        return obj if obj else stack_obj[-1]

    @classmethod
    def _infix_to_prefix_r(cls, infix:str) -> str:
        """Convert infix expression to prefix expression (space separated). (recursive solution)"""
        stack_opr = []
        stack_obj = []
        obj = None
        opr = None
        i = j = 0
        while i < len(infix):
            jump = 0
            c = infix[i]
            if c == ' ':
                continue
            elif c == '(':
                if obj:
                    stack_obj.append(obj)
                    obj = None
                j = i + 1
                count = 1
                while j < len(infix):  # find the pairing bracket
                    if infix[j] == '(':
                        count += 1
                    elif infix[j] == ')':
                        count -= 1
                        if count == 0:
                            break
                    j += 1
                obj = cls._infix_to_prefix_r(infix[i+1:j])
                # stack_obj.append(obj)
                # obj = None
                jump = j + 1
            elif c == ')':
                while stack_opr:
                    obj = stack_obj.pop()
                    obj1 = stack_obj.pop()
                    opr = stack_opr.pop()
                    obj = f'{opr} {obj1} {obj}'
                stack_obj.append(obj)
            elif c in cls._OPERATORS:
                while stack_opr and cls._PRIO[c] <= cls._PRIO[stack_opr[-1]]:
                    if not obj:
                        obj = stack_obj.pop()
                    obj1 = stack_obj.pop()
                    opr = stack_opr.pop()
                    obj = f'{opr} {obj1} {obj}'
                stack_opr.append(c)                    
                stack_obj.append(obj)
                obj = None
            else:
                if obj == None:
                    obj = c
                else:
                    obj += c
            i = jump if jump else i+1
        while stack_opr:
            obj = stack_obj.pop() if obj == None else obj
            obj1 = stack_obj.pop()
            obj = f'{stack_opr.pop()} {obj1} {obj}'
        return obj if obj != None else stack_obj[-1]

    @classmethod
    def infix_to_postfix(cls, infix:str):
        # TODO
        pass



def test():
    data = [
        (('2+3',),5),
        (('2+3*2',),8),
        (('(2+3)+(3-2)',),6),
        (('3+12*(5-4)/2-2',), 3+12*(5-4)/2-2),
        (('10-4*3/2',), 10-4*3/2),
        (('(15-(2+2)*3-1)*3/2+(1+2)*3',), (15-(2+2)*3-1)*3/2+(1+2)*3),
        # ((,),),
        # ((,),),
        # ((,),),
    ]
    ife = InfixExpression()
    test_fixture(ife.value, data)

    data = [
        (('2+3',), '+ 2 3'),
        (('2+3*2',), '+ 2 * 3 2'),
        (('(2+3)+(3-2)',), '+ + 2 3 - 3 2'),
        (('3+12*(5-4)/2-2',), '- + 3 / * 12 - 5 4 2 2'),
        (('10-4*3/2',), '- 10 / * 4 3 2'),
        (('(15-(2+2)*3-1)*3/2+(1+2)*3',), '+ / * - - 15 * + 2 2 3 1 3 2 * + 1 2 3'),
    ]
    test_fixture(ife.infix_to_prefix, data)

test()





