class Pycharm:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling check")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = MYEditor()    # if you use it like class this all print   output come
ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)
