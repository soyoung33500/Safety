import requests
import pandas as pd
import folium

class safety:
    def __init__(self, key="DBF152BC-6009-3CCF-94E1-2EA4D4774D19"):
        self.key = key
        self.lat = None
        self.lon = None
        self.address = None
        self.unit = None
        self.result = None

    def check(self):
        print("확인하고 싶으신 주소를 입력해주세요 (부산광역시 도로명 주소만 이용가능합니다)")
        print("예시 : 부산 남구 용소로 45")
        self.address = input()
        self.unit = input("확인하고 싶은 단위를 적어주세요 (50, 100, 150, 200) : ")
        print("=" * 70)

        apiurl = "https://api.vworld.kr/req/address?"
        params = {"service": "address", 
                  "request": "getcoord", 
                  "crs": "epsg:4326", 
                  "address": self.address, 
                  "format": "json", 
                  "type": "road", 
                  "key": self.key}
        
        response = requests.get(apiurl, params=params)
        json_data = response.json()
        if json_data["response"]["status"] == "NOT_FOUND": print("해당 지역을 찾을 수 없습니다")
        elif json_data["response"]["status"] == "ERROR": print("에러가 발생했습니다")
        else:
            self.lat = float(json_data['response']['result']['point']['y'])
            self.lon = float(json_data['response']['result']['point']['x'])
            
            if self.unit not in ["50", "100", "150", "200"]:  print("잘못된 단위입니다")
            else:
                df = pd.read_csv(f"grid{self.unit}.csv")
                try:
                    idx = df[(df["left"] < self.lat) & (df["right"] > self.lat) & (df["bottom"] < self.lon) & (df["top"] > self.lon)].index[0]
                    gnum = df.at[idx, "점수등급"]
                    grade = ["주의", "안전", "보통", "위험"]
                    print(f"해당 지역은 {grade[gnum]} 등급입니다")
    
                    filtered = df.loc[idx, ['경찰서', 'CCTV', '보안등']]
                    self.result = list(filtered[filtered == 1].index)
                    print(f"주변에 {'와 '.join(self.result)}{'이' if '보안등' in self.result else '가'} 있습니다.")
    
                    if df.at[idx, "유흥주점"] == 1:
                        self.result.append("유흥주점")
                        print("주변에 유흥주점도 있으니 주의하세요.")
                except IndexError: print("부산광역시 지역만 검색해주세요")
            
        print("=" * 70)
    
    def point(self):
        loca_lst = [["검색한위치", self.lat, self.lon]]
        for lst in self.result:
            loca_df = pd.read_csv(lst + ".csv")
            for idx in range(len(loca_df)):
                loca_df.at[idx, "거리"] = ((self.lat - loca_df.at[idx, "위도"]) ** 2 + (self.lon - loca_df.at[idx, "경도"]) ** 2) ** 0.5
            loca_lst.append([lst, loca_df.loc[loca_df["거리"].idxmin(), "위도"], loca_df.loc[loca_df["거리"].idxmin(), "경도"]])

        loca = pd.DataFrame(loca_lst, columns=["장소","위도","경도"])

        map_center = [35.1796, 129.0756]

        m = folium.Map(location=map_center, zoom_start=12)

        color_map = {'검색한위치':'gray','경찰서':'blue','CCTV':'green','보안등':'beige','유흥주점':'pink'}

        for i in range(len(loca)):
            folium.Marker(location=[loca.at[i,"위도"], loca.at[i,"경도"]],
                          popup=loca.at[i, "장소"],
                          icon=folium.Icon(color=color_map.get(loca.at[i, "장소"]))).add_to(m)

        return m