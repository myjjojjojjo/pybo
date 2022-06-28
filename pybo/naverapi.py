import os
import sys
import urllib.request
import json

def naver_blog() :
    # -*- coding: utf-8 -*-
    client_id = "K2GtvITL3NsaxJnVr7Iv"
    client_secret = "_Rdp1ruoid"

    url = "https://openapi.naver.com/v1/datalab/search";
    body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()  #json
        response_json = json.loads(response_body)
        blog_list=response_json['items']
        blog_list[0]['title']

        title_list = []
        for temp in blog_list:
            title_list.append(temp['title'])
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


    return title_list