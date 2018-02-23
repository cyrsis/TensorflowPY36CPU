

class Annotation(object):
    '''這是一個用戶示範註解的類別，
多行註解如果在類別或者函數的定義之後，
將被預設成doc string。
這裡註解的是該類別的功能性說明'''

    def __init__(self):
        self.run()

    def run(self):
        """函數裡的doc string，
這裡註解的是該函數的功能性說明
註解用單引號和雙引號沒有任何區別 """
        x = 333  # 定義了一個int類別型的變數x
        print('x = %d' % x)
        '''好了，這裡是單純的註解了。可以註解多行當然也可以註解單行了 '''


if __name__ == '__main__':
    a = Annotation()
