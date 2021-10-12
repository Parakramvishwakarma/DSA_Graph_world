class Path():
    def __init__(self,path_stack, length):
        self.path = path_stack
        self.length = length
    def __str__(self) -> str:
        return (str(self.path) + " length: " + str(self.length))
    