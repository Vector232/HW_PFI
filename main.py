class Stack:
    def __init__(self, *args):
        self.stack = [*args]

    def is_empty (self):
        if self.size() == 0:
            return True
        return False

    def push(self, elem):
        # self.stack.append(elem) или
        self.stack = [*self.stack, elem]

    def pop(self):
        if self.size() == 0: return None

        last = self.stack[-1]
        # del self.stack[-1] или
        self.stack = self.stack[:-1] 
        return last
    
    def peek(self):
        if self.size() == 0: return None

        return self.stack[-1]

    def size(self):
        # return len(self.stack) или
        len = 0
        for _ in self.stack:
            len += 1
        return len

    def __str__(self):
        return f'{self.stack}'
    

def is_balance(expr):
    stack = Stack()
    for bracket in expr:
        if bracket in ('(', '[', '{'):
            stack.push(bracket)
        elif bracket is ')' and stack.peek() is '('\
            or bracket is ']' and stack.peek() is '['\
            or bracket is '}' and stack.peek() is '{':
            stack.pop()
        else:
            return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    stack = Stack(1,2,3,4,5)
    print(f'Создадим непустой стек: {stack}')
    print(f'Проверим, действительно ли он непустой: {stack.is_empty()}')
    stack.push('NEW')
    print(f'Добавим элемент "NEW": {stack}')
    print(f'Достанем верхний елемент: {stack.pop()}')
    print(f'Стек изменился: {stack}')
    print(f'Теперь последний елемент это: {stack.peek()}')
    print(f'Стек не изменился: {stack}')
    print(f'Его размер равен: {stack.size()}')
