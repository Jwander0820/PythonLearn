class Revital():
    def __init__(self):
        self.book_name = "book_name"
        self.book_path = "./book_path"
        # print(self.book_name)
        # print(self.book_path)


class test_class(Revital):
    def test_inheritance(self):
        print(self.book_name)


test = test_class()
test_class().test_inheritance()


class father():          # father 類別
    def __init__(self):  # father 的方法
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

    def language(self):  # mother 的方法
        print('chinese')


class mother():          # mother 類別
    def language(self):  # mother 的方法
        print('english')
    def skill(self):
        print('painting')


class son(father, mother):    # 繼承 father 和 mother
    def play(self):           # son 自己的方法
        print('ball')


son_class = son()
print(son_class.eye)        # 2
son_class.skill()           # painting
son_class.play()            # ball
son_class.language()        # chinese (在前的優先度較高)


