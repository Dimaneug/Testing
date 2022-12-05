import pywinauto as pwa
import sys
from gui import graphic_interface


class BadFirstArg(Exception):
    pass


class BadSecondArg(Exception):
    pass


class BadOperation(Exception):
    pass


class Calculator:

    def __init__(self):
        self.last = None
        self.a = None
        self.b = None
        self.operation = None
        self.msg = None

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_last(self):
        return self.last

    def del_last(self):
        self.last = None

    def print_result(self):
        if self.operation == "+":
            self.sum()
        elif self.operation == "-":
            self.sub()
        elif self.operation == "*":
            self.mul()
        elif self.operation == "/":
            self.div()
        if self.last is not None:
            return self.last

    def print_error(self, exception):
        if isinstance(exception, BadFirstArg):
            self.msg = "Неправильная первая переменная"
        elif isinstance(exception, BadSecondArg):
            self.msg = "Неправильная вторая переменная"
        elif isinstance(exception, BadOperation):
            self.msg = "Несуществующая операция"
        elif isinstance(exception, ZeroDivisionError):
            self.msg = "Деление на ноль"
        else:
            self.msg = exception
        print("Ошибка:", self.msg)
        return self.msg

    def set_first_arg(self, a):
        try:
            self.a = float(a)
        except ValueError:
            raise BadFirstArg
        return self.a

    def set_second_arg(self, b):
        try:
            self.b = float(b)
        except ValueError:
            raise BadSecondArg
        return self.b

    def set_operation(self, operation):
        if operation in "+-*/":
            self.operation = operation
            return self.operation
        else:
            raise BadOperation

    def sum(self):
        self.last = self.a + self.b
        self.last = float('{:.14f}'.format(self.last))
        return self.last

    def sub(self):
        self.last = self.a - self.b
        self.last = float('{:.14f}'.format(self.last))
        return self.last

    def mul(self):
        self.last = self.a * self.b
        self.last = float('{:.14f}'.format(self.last))
        return self.last

    def div(self):
        if self.b == 0:
            raise ZeroDivisionError
        else:
            self.last = self.a / self.b
            self.last = float('{:.14f}'.format(self.last))
            return self.last


def click_button(main_window, button_name, button_list):
    index = button_list.index(button_name)
    button_id = "Button{}".format(str(index))
    button = main_window[button_id]
    button.click_input()


def test_my_app():
    button_list = ["btn_divide", "", "btn_res", "btn_0", "btn_dot",
                   "btn_multiply", "btn_3", "btn_2", "btn_1",
                   "btn_minus", "btn_6", "btn_5", "btn_4",
                   "btn_plus", "btn_9", "btn_8", "btn_7"]
    app = pwa.Application(backend="uia").connect(title="Калькулятор")
    main_window = app.window(title="Калькулятор")
    main_window.dump_tree()


def start():
    calculator = Calculator()
    graphic_interface(calculator)


def main() -> int:
    start()
    return 0


if __name__ == "__main__":
    sys.exit(main())
