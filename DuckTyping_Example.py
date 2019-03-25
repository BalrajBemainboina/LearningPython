'''Example of Duck Typing, Here execute method is same in Pycharm and Myeditor classes
 but they are called based on the IDE parameter, Hence what ever class execute belongs but it has IDE hence typing'''


class Pycharm:

    def execute(self):
        print('Pycharm Interpreter')


class MyEditor:

    def execute(self):
        print('MyEditor Interpreter')


class Laptop:

    def execute(self,IDE):
        IDE.execute()


IDE = MyEditor()
L = Laptop()
L.execute(IDE)
IDE = Pycharm()
L.execute(IDE)