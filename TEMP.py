class Parent:
    def __init__(self):
        return
    def step(self):
        print("ParentStep")

    def run(self):
        for i in range(5):
            self.step()


class Child(Parent):
    def step(self):
        print("Child")


c = Child()

c.run()
