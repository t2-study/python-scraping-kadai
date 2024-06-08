# -*- coding: utf-8 -*-
"""python-scraping-kadai2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zHretJbpB9bbeaGw_tJ6iXve6CfzPiWQ
"""

import requests
import pprint
from getpass import getpass

# APIキーの入力
api_key = getpass("APIキーを入力してください: ")

# 駅名の入力
station = input("検索する駅を入力してください: ")

# 駅の経度緯度の取得
station_loc_url = "https://maps.googleapis.com/maps/api/geocode/json"

station_loc = requests.get(
    station_loc_url,
    params = {
        "address": station,
        "key": api_key
    }
)

#pprint.pprint(station_loc.json())

# 駅の経度(lat)、緯度(lng)を指定する
station_loc_json = station_loc.json()

res_lat = station_loc_json["results"][0]["geometry"]["location"]["lat"]
res_lng = station_loc_json["results"][0]["geometry"]["location"]["lng"]

#print(res_lat, ": ", res_lng)

# 駅周辺のレストラン情報を取得する
rest_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json"

rest_loc = requests.get(
    rest_url,
    params={
        "location": f"{res_lat},{res_lng}",
        "language": "ja",
        "radius": 500,
        "type": "restaurant",
        "key": api_key
    }
)

rest_loc_json = rest_loc.json()

for item in rest_loc_json["results"]:
    rest_name = item["name"]
    rest_point = item["rating"]
    rest_address = item["vicinity"]

    print(f"{rest_name} {rest_point} {rest_address}")

}

]