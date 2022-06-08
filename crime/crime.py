from context.domains import Reader, File, Printer


class Solution(Reader):
    def __init__(self):
        self.file = File()
        # self.reader = Reader()
        self.printer = Printer()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        # self.file_context = './data/'
        self.file.context = './data/'

    def save_police_pos(self):
        self.file.fname = 'cctv_in_seoul'
        print(self.csv(self.file))

    def save_cctv_pos(self):
        self.file.fname = 'crime_in_seoul'
        print(self.csv(self.file))

    def save_cctv_norm(self):
        pass

    def folium_test(self):
        pass

    def draw_crime_map(self):
        self.file.fname = 'geo_simple'
        print(self.json(self.file))

if __name__ == '__main__':
    s = Solution()
    s.save_police_pos()
    s.save_cctv_pos()
    s.draw_crime_map()
