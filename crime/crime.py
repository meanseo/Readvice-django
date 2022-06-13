import pandas as pd
import numpy as np
from sklearn import preprocessing
from context.domains import Reader, File
import folium


class Solution(Reader):
    def __init__(self):
        self.file = File()
        # self.reader = Reader()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. crime_in_seoul.csv, 구글맵 API 를 이용해서 서울 시내 경찰서 주소 목록 파일을 작성하시오.')
            print('2. us-states.json, us_unemployment.csv 를 이용해서 미국 실업률 지도를 작성하시오.')
            print('3. cctv_in_seoul.csv, pop_in_seoul.csv 를 이용해서 서울시내 경찰서 주소목록파일(cctv_pop.csv)을 작성하시오.')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.save_police_pos()
            if menu == '2':
                self.folium_test()
            if menu == '3':
                self.save_cctv_pos()
            if menu == '4':
                self.save_cctv_norm()
            elif menu == '0':
                break

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

            # print(f'name {i} = {temp[0].get("formatted_address")}')
            station_addrs.append(temp[0].get('formatted_address'))
            t_loc = temp[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])

        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names #'구별'이라는 칼럼을 생성
        print(crime)
        '''
        혜화서
        '''
        crime.to_csv('./save/police_pos.csv', index=False) # 인덱스 랜덤 생성 방지

    def save_cctv_pos(self):
        file = self.file
        self.file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        self.file.fname = 'pop_in_seoul'
        pop = self.xls(file, 1, 'B, D, G, J, N', [2]) # 헤더 2행 사용, 사용 칼럼은 앞과 같이 사용, 3행 제거
        # print(cctv)
        '''
             기관명    소계  2013년도 이전  2014년  2015년  2016년
        0    강남구  2780       1292    430    584    932
        1    강동구   773        379     99    155    377
        2    강북구   748        369    120    138    204
        '''
        # print(pop)
        '''
             자치구          합계        한국인     등록외국인   65세이상고령자
        0     합계  10197604.0  9926968.0  270636.0  1321458.0
        1    종로구    162820.0   153589.0    9231.0    25425.0
        2     중구    133240.0   124312.0    8928.0    20764.0
        '''

        cctv.rename(columns={cctv.columns[0]:'구별'}, inplace=True)
        pop.rename(columns={'자치구':'구별',
                            '합계':'인구수',
                            '등록외국인':'외국인',
                            '65세이상고령자': '고령자'}, inplace=True)
        pop.drop(26, inplace=True) # axis=1은 열, default는 0(행)
        cctv.drop(cctv.columns[2:6], axis=1, inplace=True)
        # cctv.drop(['2013년도 이전','2014년','2015년','2016년'], axis=1, inplace=True)
        # pop.dropna() NaN 값이 하나라도 있으면 날리는 메소드 / pop.dropna(how ='all') 전부 NaN이면 날리는 메소드
        pop['고령자비율'] = pop['고령자'] / pop['인구수'] * 100
        pop['외국인비율'] = pop['외국인'] / pop['인구수'] * 100
        cctv_pop = pd.merge(cctv, pop, on='구별')
        print(cctv_pop)
        cor1 = cctv_pop['고령자비율'].corr(cctv_pop['소계'])
        cor2 = cctv_pop['외국인비율'].corr(cctv_pop['소계'])

        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """

        cctv_pop.to_csv('./save/cctv_pop.csv')

    def save_cctv_norm(self):
        '''
        표준화는 데이터의 평균을 0, 표준편차를 1로 만드는 것이다.
        x = (x - mu) / sigma
        scale = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
        정규화는 최대값을 1, 최솟값을 0으로 만드는 것이다.
        '''
        file = self.file
        file.context = './save/'
        file.fname = 'police_pos'
        police_pos = self.csv(file)
        police = pd.pivot_table(police_pos, index='구별', aggfunc=np.sum)
        police['살인검거율'] = police['살인 검거'] / police['살인 발생'] * 100
        police['강도검거율'] = police['강도 검거'] / police['강도 발생'] * 100
        police['강간검거율'] = police['강간 검거'] / police['강간 발생'] * 100
        police['절도검거율'] = police['절도 검거'] / police['절도 발생'] * 100
        police['폭력검거율'] = police['폭력 검거'] / police['폭력 발생'] * 100
        police.drop(['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'], axis=1, inplace=True)
        print(police)
        for j, i in enumerate(self.crime_rate_columns):
            police[i].loc[j, i] = 100
        # police.loc[police[self.crime_rate_columns] > 100] = 100
        print(police)
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns]
        min_max_scalar = preprocessing.MinMaxScaler()
        """     
        피쳐 스케일링(Feature scalining)은 해당 피쳐들의 값을 일정한 수준으로 맞춰주는 것이다.
        이때 적용되는 스케일링 방법이 표준화(standardization) 와 정규화(normalization)다.
        
        1단계: 표준화(공통 척도)를 진행한다.
            표준화는 정규분포를 데이터의 평균을 0, 분산이 1인 표준정규분포로 만드는 것이다.
            x = (x - mu) / sigma
            scale = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
        2단계: 이상치 발견 및 제거
        3단계: 정규화(공통 간격)를 진행한다.
            정규화에는 평균 정규화, 최소-최대 정규화, 분위수 정규화가 있다.
             * 최소최대 정규화는 모든 데이터를 최대값을 1, 최솟값을 0으로 만드는 것이다.
            도메인은 데이터의 범위이다.
            스케일은 데이터의 분포이다.
            목적은 도메인을 일치시키거나 스케일을 유사하게 만든다.     
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        # police_norm.to_csv('./save/police_norm.csv', sep=',', encoding='UTF-8')

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
    Solution().hook()
