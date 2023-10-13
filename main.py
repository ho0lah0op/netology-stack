class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.is_empty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.is_empty():
            return self[-1]

    def size(self):
        return len(self)


def check_if_balanced(input_string):
    stack = Stack()
    for item in input_string:
        if item in bracket_dict:
            stack.push(item)
        elif item == bracket_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    bracket_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    input_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]

    for seq in input_list:
        is_balanced = check_if_balanced(seq)
        if is_balanced:
            print(f'{seq:<30}Сбалансированно')
        else:
            print(f'{seq:<30}Несбалансированно')
