class deec:
    def __init__(self, *args):
        self.content = args

    def add_top(self, *args):
        self.content = args + self.content
    def add_bot(self, *args):
        self.content += args
    def del_top(self, num):
        self.content = self.content[num:]
    def del_bot(self, num):
        self.content = self.content[:-num]
    def see_top(self):
        return self.content[0]
    def see_bot(self):
        return self.content[-1]

d = deec('a', 1, 'b', None)
d.add_top('sippin')
d.add_bot('purp', 'sauce')
print(d.see_bot())
d.del_bot(2)
d.del_top(2)
print(d.see_top())
print(d.see_bot())

