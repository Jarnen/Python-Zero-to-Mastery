# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    # overide __str__
    def __str__(self):
        return f"{self.color}"

    # overide __len__
    def __len__(self):
        return 5

    # overide __del__
    def __del__(self):
        return "deleted"

    # overide __call__
    def __call__(self):
        return('yes??')

    # overide __getitem__
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
