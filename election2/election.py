from context.domains import Reader, File


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def new_df(self):
        pass

if __name__ == '__main__':
    pass