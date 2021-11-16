from stack_and_queue.stack import Stack

def validate_brackets(bracket = None):
    """
    function to check if group of brackets are match or not (return boolean value)
    Ex: {}(){}----> match
        [({}] ----> not match

    """
    # order is important if you change the order it will cause in-valid output 
    open_brackets = ["[","{","("]
    close_brackets = ["]","}",")"]
    stack = Stack()
    if (bracket == None):
        raise Exception ('no brackets to check ')
    for i in bracket:
        # if bracket is inside open array push it to stack
        if i in open_brackets:
            stack.push(i) 
        elif i in close_brackets:
            # for close brackets find its index
            pos = close_brackets.index(i)
            # check if stack not empty and the brackets inside the stack is in the open brackets array
            if (( not stack.is_empty()) and
                (open_brackets[pos] == stack.peek())):
                # if it is true then pop from stack
                stack.pop()
        else: # if there is an charachters inside the string 
            continue
    # stack is empty means that all brackets match---> return true / else---> return false
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print (validate_brackets('({)'))

