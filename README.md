# 부산 취약지역 예측 함수


```python
!git clone https://github.com/soyoung33500/Safety.git
```

    Cloning into 'Safety'...
    


```python
cd Safety
```

safety.py의 safety 클래스 호출


```python
from safety import safety
```

변수에 safety() 클래스 입력


```python
test = safety()
```

check() 함수 실행   
입력 칸에 검색하고 싶은 주소 입력   
확인하고 싶은 격자 단위 입력


```python
test.check()
```

    확인하고 싶으신 주소를 입력해주세요 (부산광역시 도로명 주소만 이용가능합니다)
    예시 : 부산 남구 용소로 45
    부산 남구 용소로 45
    확인하고 싶은 단위를 적어주세요 (50, 100, 150, 200) : 50
    ======================================================================
    해당 지역은 안전 등급입니다
    주변에 경찰서와 CCTV가 있습니다.
    ======================================================================
    

해당 지역의 등급과 등급을 예측하는데 영향을 준 변수들을 출력해줌

---
point() 함수 실행   
검색한 위치와 주변 변수들의 위치를 마크   
마크를 클릭하면 어떤 변수인지 알려줌


```python
test.point()
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;head&gt;    
    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_4d2fc69aad957d3e465136ca62d32bc7 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;    

            &lt;div class=&quot;folium-map&quot; id=&quot;map_4d2fc69aad957d3e465136ca62d32bc7&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;    

            var map_4d2fc69aad957d3e465136ca62d32bc7 = L.map(
                &quot;map_4d2fc69aad957d3e465136ca62d32bc7&quot;,
                {
                    center: [35.1796, 129.0756],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_1a389fbd8239f5bf6fd01056f072ee79 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_4d2fc69aad957d3e465136ca62d32bc7);


            var marker_0385abdcc35fc9adcc4253cb73ea3883 = L.marker(
                [35.134925538, 129.109531096],
                {}
            ).addTo(map_4d2fc69aad957d3e465136ca62d32bc7);


            var icon_fea74fa80dbc10066fd623196719d4f4 = L.AwesomeMarkers.icon(
                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;info-sign&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;gray&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}
            );
            marker_0385abdcc35fc9adcc4253cb73ea3883.setIcon(icon_fea74fa80dbc10066fd623196719d4f4);


        var popup_07ee1bb2780181a89cc50297fb49726d = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_1cb074af6938cfe2494eb2c44fbcf1ed = $(`&lt;div id=&quot;html_1cb074af6938cfe2494eb2c44fbcf1ed&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;검색한위치&lt;/div&gt;`)[0];
            popup_07ee1bb2780181a89cc50297fb49726d.setContent(html_1cb074af6938cfe2494eb2c44fbcf1ed);


        marker_0385abdcc35fc9adcc4253cb73ea3883.bindPopup(popup_07ee1bb2780181a89cc50297fb49726d)
        ;




            var marker_d396f55794cde907839b25e528b2b2b3 = L.marker(
                [35.13783221, 129.1019868],
                {}
            ).addTo(map_4d2fc69aad957d3e465136ca62d32bc7);


            var icon_257758cc080b46bc7b24d453ede264f4 = L.AwesomeMarkers.icon(
                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;info-sign&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;blue&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}
            );
            marker_d396f55794cde907839b25e528b2b2b3.setIcon(icon_257758cc080b46bc7b24d453ede264f4);


        var popup_79359c36bda2d0ffeaefe7346cc6c0ef = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_359b0c91552226d703bcef8af09e320a = $(`&lt;div id=&quot;html_359b0c91552226d703bcef8af09e320a&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;경찰서&lt;/div&gt;`)[0];
            popup_79359c36bda2d0ffeaefe7346cc6c0ef.setContent(html_359b0c91552226d703bcef8af09e320a);


        marker_d396f55794cde907839b25e528b2b2b3.bindPopup(popup_79359c36bda2d0ffeaefe7346cc6c0ef)
        ;




            var marker_851eb6f614edf75d56429a9372362c87 = L.marker(
                [35.1343909, 129.110841],
                {}
            ).addTo(map_4d2fc69aad957d3e465136ca62d32bc7);


            var icon_58f12dd5d1df41fd08193b8159af9a73 = L.AwesomeMarkers.icon(
                {&quot;extraClasses&quot;: &quot;fa-rotate-0&quot;, &quot;icon&quot;: &quot;info-sign&quot;, &quot;iconColor&quot;: &quot;white&quot;, &quot;markerColor&quot;: &quot;green&quot;, &quot;prefix&quot;: &quot;glyphicon&quot;}
            );
            marker_851eb6f614edf75d56429a9372362c87.setIcon(icon_58f12dd5d1df41fd08193b8159af9a73);


        var popup_490d37626103a7317212c3ccb7593114 = L.popup({&quot;maxWidth&quot;: &quot;100%&quot;});


            var html_f9d39e175893f78fd29237b111497a16 = $(`&lt;div id=&quot;html_f9d39e175893f78fd29237b111497a16&quot; style=&quot;width: 100.0%; height: 100.0%;&quot;&gt;CCTV&lt;/div&gt;`)[0];
            popup_490d37626103a7317212c3ccb7593114.setContent(html_f9d39e175893f78fd29237b111497a16);


        marker_851eb6f614edf75d56429a9372362c87.bindPopup(popup_490d37626103a7317212c3ccb7593114)
        ;



&lt;/script&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python

```
