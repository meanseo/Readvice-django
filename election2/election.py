from context.domains import Reader, File


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def new_df(self):
        self.file.fname = 'total_election.xlsx'
        election_result_raw = self.xlsx(self.file)
        election_result_raw = {'광역시도': [],
                               '시군': [],
                               'pop': [],
                               'moon': [],
                               'hong': [],
                               'ahn': []}
if __name__ == '__main__':
    pass