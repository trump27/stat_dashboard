import requests
import json
import json2csv
import os
import time

# api = 'https://dashboard.e-stat.go.jp/api/1.0/Json/getData?IndicatorCode={indicator}&TimeFrom={start}'
api = 'https://dashboard.e-stat.go.jp/api/1.0/Json/getData?IndicatorCode={indicator}&TimeFrom={start}&RegionCode=00000'

STATS = {
    "0702020201000010000": "銀行貸出",
    "0702010202000010030": "マネーストック（広義流動性）",
    "0702020300000010010": "コールレート（無担保Ｏ／Ｎ物）",
    "0702020300000010020": "新発10年国債利回り（月末終値）",
    "0702020401000010010": "東京インターバンク相場（円・ドル）",
    "0702020501000010010": "日経平均株価",
    "0702020590000090010": "東証株価指数（TOPIX）",
    "0703010401010090000": "消費者物価指数（総合）2015年基準",
    "0704010101000010000": "二人以上の世帯　消費支出",
    "0706010400000090010": "景気動向指数（一致）2015年基準"
}


def getData(indicator, start):
    url = api.format(indicator=indicator, start=start)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data


def main(indicator, start=20080100):
    df = getData(ind, start)  # dict型が返る
    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    for ind in STATS:
        print('start:', ind)
        df = getData(ind, 20080100)  # dict型が返る
        with open('data/{}.json'.format(ind), mode='w', encoding='UTF-8') as f:
            json.dump(df, f, ensure_ascii=False)  # 辞書型からjsonへ
        json2csv.jsondata2csv(df)
        time.sleep(2)

# if __name__ == "__main__":
#     ind = '0702010202000010030'
#     print('start:', ind)
#     df = getData(ind, 20080100)  # dict型が返る
#     with open('data/{}.json'.format(ind), mode='w', encoding='UTF-8') as f:
#         json.dump(df, f, ensure_ascii=False)  # 辞書型からjsonへ
#     json2csv.jsondata2csv(df)
