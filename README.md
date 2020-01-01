# 経済データをAPIで取得

## 統計Dashboard

- [統計Dashboard](https://dashboard.e-stat.go.jp/)
- [APIについて](https://dashboard.e-stat.go.jp/static/api)

主に以下のデータを取得する目的
```
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
```

## 利用

- ``dataフォルダ``を作成する
```
> python call_api.py
```
- 月単位のデータを取得する
- 開始日時は ``yyyymm00``形式。現在までのデータを取得する
- 取得したjsonファイル、日付と値のcsvファイルをIndicatorCode単位に一括出力する
- APIキー、認証などは不要