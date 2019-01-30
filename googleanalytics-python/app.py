# -*- coding: utf-8 -*-

import modules.helloanalytics as analytics
import pprint

viewid = '******'

def main():

    start_date = '7daysAgo'
    end_date = 'today'

    view = analytics.Analytics(viewid)
    # 戻り値はデータフレーム型
    df = view.get_report(start_date
                        , end_date
                        , ['sessions', 'pageviews']
                        , ['date']
#                        , {"ga:date" : "ASCENDING"}
    )
    print(df)

if __name__ == '__main__':
  main()
