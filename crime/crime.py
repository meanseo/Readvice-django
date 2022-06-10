from context.domains import Reader, File, Printer
import folium


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
        self.file.fname = 'crime_in_seoul'
        crime = self.csv(self.file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f'station_names range: {len(station_names)}')
        for i, name in enumerate(station_names):
            # print(f'name {i} = {name}')
            pass
        gmaps = self.gmaps()
        a = gmaps.geocode('서울종암경찰서', language='ko')
        '''
        a = gmaps.geocode('서울중부경찰서', language='ko')
        [{'address_components':
            [{'long_name': '２７', 'short_name': '２７', 'types': ['premise']}, 
            {'long_name': '수표로', 'short_name': '수표로', 'types': ['political', 'sublocality', 'sublocality_level_4']}, 
            {'long_name': '중구', 'short_name': '중구', 'types': ['political', 'sublocality', 'sublocality_level_1']}, 
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']}, 
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}], 'formatted_address': '대한민국 서울특별시 중구 수표로 27', 
            'geometry': 
                {'location': {'lat': 37.56361709999999, 'lng': 126.9896517}, 
                'location_type': 'ROOFTOP', 
                'viewport': {'northeast': {'lat': 37.5649660802915, 'lng': 126.9910006802915}, 
                'southwest': {'lat': 37.5622681197085, 'lng': 126.9883027197085}}}, 
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc', 
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시', 
                'global_code': '8Q98HX7Q+CV'}, 'types': ['establishment', 'point_of_interest', 'police']}]
        서울종암경찰서는 2021.12.20부터 이전함
        '''
        station_addrs = []
        station_lats = []
        station_lngs = []

        for i, name in enumerate(station_names):
            if name != '서울종암경찰서':
                temp = gmaps.geocode(name, language='ko')
            else:
                temp = [{'address_components':
            [{'long_name': '２７', 'short_name': '２７', 'types': ['premise']},
            {'long_name': '화랑로', 'short_name': '화랑로', 'types': ['political', 'sublocality', 'sublocality_level_4']},
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}],
            'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
            'geometry':
                {'location': {'lat': 37.603750999451265, 'lng': 127.0401798558862 },
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 37.603750999451265, 'lng': 127.0401798558862},
                'southwest': {'lat': 37.603750999451265, 'lng': 127.0401798558862}}},
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc',
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시',
                'global_code': '8Q98HX7Q+CV'}, 'types': ['establishment', 'point_of_interest', 'police']}]

            print(f'name {i} = {temp[0].get("formatted_address")}')

    def save_cctv_pos(self):
        file = self.file
        self.file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        self.file.fname = 'pop_in_seoul'
        pop = self.xls(file, 1, 'B, D, G, J, N', 2)
        print(pop)

    def save_cctv_norm(self):
        pass

    def folium_test(self):
        file = self.file
        self.file.fname = 'us-states.json'
        states = self.new_file(file)
        self.file.fname = 'us_unemployment'
        unemployment = self.csv(file)
        bins = list(unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        m = folium.Map(location=[48, -102], zoom_start=3)
        folium.Choropleth(
            geo_data=states, # dataframe이 아님
            name="choropleth",
            data=unemployment,
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Unemployment Rate (%)",
            bins=bins,
            reset=True
        ).add_to(m)
        # m = folium.Map(location=[45.5236, -122.6750]).
        m.save("./save/folium_test.html")

    def draw_crime_map(self):
        self.file.fname = 'geo_simple'
        print(self.json(self.file))

if __name__ == '__main__':
    s = Solution()
    s.folium_test()
    # s.save_cctv_pos()
    #s.draw_crime_map()
