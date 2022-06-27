class Stack:

    list_var = [1, 4, 'sdhfbg', [45, 'erwt'],'[(({}))]']

    def __init__(self, stack = list_var):
        self.stack = stack

    def isEmpty(self):

        print()
        if len(self.stack) == 0:
            print('TRUE')
        else:
            print('FALSE')

    def push(self, item):
        self.item = item
        self.stack.insert(0, self.item)

    def pop(self, index = 0):
        value = self.stack.pop(index)
        return value

    def peek(self, index = 0):
        value = self.stack[index]
        return value

    def size(self):
        count_ = len(self.stack)
        return count_

    def scoba(self, index = -1):
        list_scoba = [items for items in self.stack[index]]
        print()
        print(list_scoba)
        while len(list_scoba) >0:
            if list_scoba.count('(') == list_scoba.count(')') \
                    and list_scoba.count('{') == list_scoba.count('}')\
                    and list_scoba.count('[') == list_scoba.count(']'):

                if list_scoba[0] == '(' and list_scoba[-1] == ')' or list_scoba[0] == '[' and list_scoba[-1] == ']' or list_scoba[0] == '{' and list_scoba[-1] == '}':
                    list_scoba.pop(0)
                    list_scoba.pop(-1)
                    if len(list_scoba) == 0:
                        print('Сбалансированно')

                else:
                    print('Несбалансированные')
                    break
            else:
                print('Несбалансированные')
                break


pr1 = Stack()
pr1.isEmpty()
pr1.push('jnk')
pr1.pop()
pr1.peek()
pr1.size()
pr1.scoba()



