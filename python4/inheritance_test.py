class Parent:
    def method(self):
        self.part1()
        self.part2()

    def part1(self):
        print("This is part 1 of the parent's method.")

    def part2(self):
        print("This is part 2 of the parent's method.")

class Child(Parent):
    def part1(self):
        print("This is the modified part 1 of the child's method.")

child = Child()
child.method()
