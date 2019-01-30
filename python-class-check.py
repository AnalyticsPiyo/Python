class Spam():
    # ここに書いた変数はリストや辞書のような時にすべてのインスタンスに影響する
    egg_list = list()
    egg = "Hello World"
    def __init__(self, ham):
        self.ham = ham

    def hoge(self):
        print(self.ham)
        print(self.egg)
        print(self.egg_list)

a = Spam("OK")
b = Spam("NO")

a.hoge()
print("--")

a.egg = "change"
a.egg_list.append("change")
b.hoge()
print("--")

b.egg_list.append("chance")
a.hoge()
print("--")
