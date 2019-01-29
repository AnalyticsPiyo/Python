# -*- coding: utf-8 -*-

import modules.helloanalytics as analytics
import pprint

viewid = '*********'

def make_argument(type, values):
    tmp_list = list()
    
    for i in values:
        tmp_dict = dict()
        tmp_dict[type] = i
        tmp_list.append(tmp_dict)
    return tmp_list

def make_order(values):
    tmp_list = list()
    for k, v in values.items():
        tmp_dict = dict()
        tmp_dict["fieldName"] = k
        tmp_dict["sortOrder"] = v
        tmp_list.append(tmp_dict)
    return tmp_list

def main():

    orders = []

    start_date = '7daysAgo'
    end_date = 'today'

    pre_metrics = ['ga:sessions', 'ga:pageviews']
    metrics = make_argument("expression", pre_metrics)
    
    pre_dimensions = ['ga:country', 'ga:date']
    dimensions = make_argument("name", pre_dimensions)

    pre_order = {"ga:country" : "ASCENDING", "ga:date" : "ASCENDING"}
    orders = make_order(pre_order)
    view = analytics.Analytics(viewid)
    
    columns = pre_dimensions + pre_metrics
    orders = []
        
    # 戻り値はデータフレーム型
    df = view.get_report(start_date, end_date, metrics, dimensions, orders, columns)
    print(df)

if __name__ == '__main__':
  main()