from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        self.view.main()

    
    def on_button_click(self, caption):
        print(f'Button {caption} clicked')

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
