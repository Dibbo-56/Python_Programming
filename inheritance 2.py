class Parent():
    def override(self):
        print("Parent override")

    def implicit(self):
        print("Parent implicit")

    def alter(self):
        print("Parent alter")

class Child(Parent):
    def override(self):
        print("Child override")

    def alter(self):
        print("Child alter before")
        super().alter()
        print("Child alter after")

parent_obj = Parent()
child_obj = Child()

parent_obj.implicit()
child_obj.implicit()

parent_obj.override()
child_obj.override()

parent_obj.alter()
child_obj.alter()
