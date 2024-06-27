class Meta:
    def __init__(self):
        self.num = 5

    def method(self):
        return self.num


class Son(Meta):

    pass


obj = Son()
obj.num = 8
print(obj.method())
