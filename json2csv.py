import json
import csv


def jsondata2csv(df):
    """ df: DICT型(json) """

    data = df['GET_STATS']['STATISTICAL_DATA']['DATA_INF']['DATA_OBJ']

    indicator = df['GET_STATS']['PARAMETER']['indicatorCode'][0]

    stat_name = df['GET_STATS']['STATISTICAL_DATA']['TABLE_INF']['STAT_NAME']
    print('STAT_NAME', stat_name[0]['$'])

    with open('data/{}.csv'.format(indicator), 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        for item in data:
            datev = item['VALUE']['@time']
            datef = datev[:4] + '-' + datev[4:6] + '-01'
            writer.writerow([datef, item['VALUE']['$']])


def jsonfile2csv(jsonfile):
    with open(jsonfile, encoding='UTF-8') as f:
        df = json.load(f)  # dict型
    jsondata2csv(df)


if __name__ == "__main__":
    jsonfile2csv('data/0702020300000010010.json')
