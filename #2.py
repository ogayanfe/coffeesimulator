class Machine:
    def __init__(self):
        self.water_aval = 400
        self.milk_aval = 540
        self.beans_aval = 120
        self.cups_aval = 9
        self.money = 550

    def display(self):
        print('\nThe coffee machine has:')
        print(f'{self.water_aval} of water')
        print(f'{self.milk_aval} of milk')
        print(f'{self.beans_aval} of coffee beans')
        print(f'{self.cups_aval} of disposable cups')
        print(f'{self.money} of money')

    def check_low(self, water_req, milk_req, bean_req):  # req means required
        if self.water_aval < water_req:
            print('Sorry, not enough water!')
        if self.milk_aval < milk_req:
            print('Sorry, not enough milk!')
        if self.beans_aval < bean_req:
            print('Sorry, not enough coffee beans!')
        if self.cups_aval == 0:
            print('Sorry, not enough cups!')

    def resources(self, water_req, milk_req, bean_req, profit):
        self.water_aval -= water_req
        self.milk_aval -= milk_req
        self.beans_aval -= bean_req
        self.cups_aval -= 1
        self.money += profit
        print('I have enough resources, making you a coffee!')

    def espresso(self):
        if self.water_aval > 250 and self.beans_aval > 16 and self.cups_aval > 0:
            self.resources(250, 0, 16, 4)
        else:
            self.check_low(250, 16, 0)

    def latte(self):
        if self.water_aval > 350 and self.milk_aval > 75 and self.beans_aval > 20 \
                and self.cups_aval > 0:
            self.resources(350, 75, 20, 7)
        else:
            self.check_low(350, 75, 20)

    def cappuccino(self):
        if self.water_aval > 200 and self.milk_aval > 100 and self.beans_aval > 12 \
                and self.cups_aval > 0:
            self.resources(200, 100, 12, 6)
        else:
            self.check_low(200, 100, 12)

    def buy(self):
        prompt = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if prompt != 'back':
            if prompt == '1':
                self.espresso()
            elif prompt == '2':
                self.latte()
            elif prompt == '3':
                self.cappuccino()

    def fill(self):
        add_water = int(input('Write how many ml of water you want to add:\n'))
        add_milk = int(input('Write how many ml of milk you want to add:\n'))
        add_beans = int(input('Write how many grams of coffee beans you want to add:\n'))
        add_cups = int(input('Write how many disposable coffee cups you want to add:\n'))
        self.water_aval += add_water
        self.milk_aval += add_milk
        self.beans_aval += add_beans
        self.cups_aval += add_cups

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def main(self):
        while True:
            action = input('\nWrite action (buy, fill, take, remaining, exit):\n')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.display()
            elif action == 'exit':
                break


shop = Machine()
shop.main()
