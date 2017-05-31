# -*- coding: utf-8 -*-
from xmlfunc import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse



conn = None
regKey = '6951bde581eb8618dbb0ef4d10922a18'
server = "apis.daum.net"     # 다음 OpenAPI 서버

# smtp 정보
host = "smtp.gmail.com"
port = "587"


#URI주소를 만들어 주는 함수
def userSearchURIBuilder(server,**user):
    str = "https://" + server + "/shopping/search" + "?"  #다음 검색 URL
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    else:
        #print("connection success!")
        return True


def extractData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    itemElements = tree.getiterator("item")  # return list type


    #print(itemElements)
    for item in itemElements:
        title = item.find("title")
        category_name = item.find("category_name")
        price_min = item.find("price_min")
        price_max = item.find("price_max")
        brand = item.find("brand")
        link = item.find("link")

        print("========================================================================================")
        if len(title.text) > 0 :
            print("이름 : ", title.text)
        if len(category_name.text) > 0 :
            print("카테고리 : " ,category_name.text)
        if len(price_min.text) > 0:
            print("최저가 : " , price_min.text)
        if len(price_max.text) > 0 :
            print("최고가 : " , price_max.text)
        if len(brand.text) > 0 :
            print("브랜드 : " , brand.text)
        if len(link.text)>0:
            print("링크 : ",link.text)
        print("========================================================================================")

    return itemElements

def SearchItems(keyword):

    ItemElement = SearchShopping(keyword)

    ItemList=[]
    for item in ItemElement:
        title = item.find("title")
        category_name = item.find("category_name")
        price_min = item.find("price_min")
        price_max = item.find("price_max")
        brand = item.find("brand")
        link = item.find("link")

        if len(title.text) > 0 :
            ItemList.append((item.attrib["이름"], title.text))
        if len(category_name.text) > 0 :
            ItemList.append((item.attrib["카테고리"], category_name.text))
        if len(price_min.text) > 0 :
            ItemList.append((item.attrib["최저가"], price_min.text))
        if len(price_max.text) > 0 :
            ItemList.append((item.attrib["최고가"], price_max.text))
        if len(brand.text) > 0 :
            ItemList.append((item.attrib["브랜드"], brand.text))
        if len(link.text)>0:
            ItemList.append((item.attrib["링크"], link.text))

    return ItemList


def SearchShopping(goods):
    global server, regKey, conn
    if conn == None:  # 커넥션이 된 상태에서 다른곳으로 커넥션 하면 안됨
        connectOpenAPIServer()

    #https://apis.daum.net/shopping/search?apikey={apikey}&q=카카오프렌즈&result=3&pageno=1&sort=pop&output=json
    uri = userSearchURIBuilder(server, apikey=regKey, q=goods, result="3",pageno="1",sort="pop",output="xml")

    #print(uri)
    checkConnection()

    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("data downloading complete!")
        return extractData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None
######################################################################################################################


def sendMain():
    global host, port
    html = ""
    title = str(input('메일 이름을 입력하세요 :'))
    senderAddr = str(input('보내는 사람의 이메일 주소를 입력하세요 :'))
    recipientAddr = str(input('받는 사람의 이메일 주소를 입력하세요 :'))
    msgtext = str(input('메세지를 입력하세요 :'))
    passwd = str(input(' Gmail 비밀번호를 입력하세요 :'))
    msgtext = str(input('내용을 검색하시겠습니까? (y/n):'))
    if msgtext == 'y':
        keyword = urllib.parse.quote_plus(str(input('검색할 내용을 입력하세요 :')))
        html = MakeHtmlDoc(SearchItems(keyword))

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchShopping(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.
