# -*- coding: utf-8 -*-
from func import *
import urllib.request
import urllib.parse
from xml.dom.minidom import parse, parseString
from xmlfunc import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from tkinter import *
from tkinter import font
import tkinter.messagebox

loopFlag = 1

window = Tk()
window.geometry("400x600+750+200")

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
    MainText = Label(window, font = TempFont, text="[쇼핑 검색 프로그램]")
    MainText.pack()
    MainText.place(x=20,y=10)

def InitSearchListBox():
    global SearchListBox
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    ShowLabel=Label(window,font=TempFont,width=22,text="상품 이름을 입력하세요")
    ShowLabel.pack()
    ShowLabel.place(x=5,y=55)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=95)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=100)

def InitSortListBox():
    global SortListBow
    TempFont=font.Font(window, size=12, weight='bold', family = 'Consolas')

    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=135,y=155)

    SearchListBox = Listbox(window, font=TempFont,activestyle='none', width = 10, height = 1, borderwidth = 10, relief = 'ridge',yscrollcommand = ListBoxScrollbar.set)
    SearchListBox.insert(1, "인기도")
    SearchListBox.insert(2, "최고가")
    SearchListBox.insert(3, "최저가")
    SearchListBox.insert(4, "출시일")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=155)

def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def SearchButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchItem()
    RenderText.configure(state='disabled')

def SearchItem():

    import http.client
    from xml.dom.minidom import parse, parseString
    from http.client import HTTPConnection
    import urllib.parse

    conn = None

    conn=HTTPConnection("apis.daum.net")
    userSearchURIBuilder(server, apikey=regKey, q=urllib.parse.quote_plus(InputLabel.get()), result="1", pageno="1", sort="pop", output="xml")
    conn.request("GET",userSearchURIBuilder(server, apikey=regKey, q=urllib.parse.quote_plus(InputLabel.get()), result="1", pageno="1", sort="pop", output="xml"))
    req = conn.getresponse()

    if int(req.status) == 200:
        print("data downloading complete!")
        Data = req.read()
        from xml.etree import ElementTree
        tree = ElementTree.fromstring(Data)
        itemElements = tree.getiterator("item")
        for item in itemElements:
            title = item.find("title")
            category_name = item.find("category_name")
            price_min = item.find("price_min")
            price_max = item.find("price_max")
            brand = item.find("brand")
            link = item.find("link")
            image=item.find("image_url")

            if len(title.text) > 0:
                RenderText.insert(INSERT,"이름:")
                RenderText.insert(INSERT,title.text)
                RenderText.insert(INSERT,"\n")
            if len(category_name.text) > 0:
                RenderText.insert(INSERT,"카테고리:")
                RenderText.insert(INSERT,category_name.text)
                RenderText.insert(INSERT, "\n")
            if len(price_min.text) > 0:
                RenderText.insert(INSERT, "최저가:")
                RenderText.insert(INSERT, price_min.text)
                RenderText.insert(INSERT, "\n")
            if len(price_max.text) > 0:
                RenderText.insert(INSERT, "최고가:")
                RenderText.insert(INSERT, price_max.text)
                RenderText.insert(INSERT, "\n")
            if len(brand.text) > 0:
                RenderText.insert(INSERT, "브랜드:")
                RenderText.insert(INSERT, brand.text)
                RenderText.insert(INSERT, "\n")
            if len(link.text) > 0:
                RenderText.insert(INSERT, "링크:")
                RenderText.insert(INSERT, link.text)
                RenderText.insert(INSERT, "\n\n")
            if len(image.text)>0:
                from io import BytesIO
                import urllib
                import urllib.request
                from PIL import Image, ImageTk

                # openapi로 이미지 url을 가져옴.
                url = image.text
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()

                im = Image.open(BytesIO(raw_data))
                image = ImageTk.PhotoImage(im)

                label = Label(window, image=image, height=135, width=135)
                label.pack()
                label.place(x=100,y=350)

                RenderText.insert(INSERT, "이미지:")
                RenderText.insert(INSERT,image.text)
                RenderText.insert(INSERT, label)
                RenderText.insert(INSERT, "\n")

def SetMail():
    global title, recipientAddr, msgText, titleInput, recipientAddrInput, msgInput

    #메일 이름 입력부
    filewin=Toplevel(window)
    filewin.geometry("400x400+750+200")

    TempFont = font.Font(filewin, size=10, family='Consolas')

    titleLabel = Label(filewin,font=TempFont, text="메일 이름을 입력하세요 :")
    titleInput = Entry(filewin,font=TempFont,width=26,borderwidth=12,relief='ridge')
    titleLabel.pack()
    titleInput.pack()

    #수신인 메일 주소 입력부
    recipientAddrLabel = Label(filewin, font=TempFont,text="받을 사람의 이메일 주소를 입력하세요 :")
    recipientAddrInput=Entry(filewin,font=TempFont,width=26,borderwidth=12,relief='ridge')
    recipientAddrLabel.pack()
    recipientAddrInput.pack()

    #메일 메세지 입력부
    msgLabel = Label(filewin, font=TempFont,text="메세지를 입력하세요 :")
    msgInput=Entry(filewin,font=TempFont,width=26,borderwidth=12,relief='ridge')
    msgLabel.pack()
    msgInput.pack()

    #이메일 전송 버튼
    TempFont = font.Font(filewin, size=12, weight='bold', family='Consolas')
    SendButton = Button(filewin, font=TempFont, text="이메일 전송",command=SendMail)
    SendButton.pack()

    #상태창
    global TopLevelRenderText
    TopLevelRenderTextScrollbar = Scrollbar(filewin)
    TopLevelRenderTextScrollbar.pack()
    TopLevelRenderTextScrollbar.place(x=375, y=180)
    #TempFont = font.Font(filewin, size=10, family='Consolas')
    TopLevelRenderText = Text(filewin, width=49, height=10, borderwidth=12, relief='ridge',
                      yscrollcommand=TopLevelRenderTextScrollbar.set)
    TopLevelRenderText.pack()
    TopLevelRenderText.place(x=10, y=235)
    TopLevelRenderTextScrollbar.config(command=TopLevelRenderText.yview)
    TopLevelRenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

def SendMail():
    global host, port, title, recipientAddr, msgText, senderAddr, passwd
    global TopLevelRenderText
    html = ""

    title = titleInput.get()
    recipientAddr = recipientAddrInput.get()
    msgText = msgInput.get()

    TopLevelRenderText.insert(INSERT,"메일 이름:")
    TopLevelRenderText.insert(INSERT,title)
    TopLevelRenderText.insert(INSERT,"\n")
    TopLevelRenderText.insert(INSERT, "받는 사람 주소:")
    TopLevelRenderText.insert(INSERT, recipientAddr)
    TopLevelRenderText.insert(INSERT,"\n")
    TopLevelRenderText.insert(INSERT, "메세지:")
    TopLevelRenderText.insert(INSERT, msgText)
    TopLevelRenderText.insert(INSERT,"\n")

    senderAddr = "to2395@gmail.com"
    passwd = "dlehdus11!"

    import mysmtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')

    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgText, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    TopLevelRenderText.insert(INSERT,"SMTP서버에 연결중입니다... ")
    TopLevelRenderText.insert(INSERT,"\n")

    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())

    s.close()
    TopLevelRenderText.insert(INSERT,"메일 전송 완료!!!")

def InitMenuBar():
    menubar=Menu(window)
    sendMenu=Menu(menubar,tearoff=0)
    sendMenu.add_command(label="전송",command=SetMail)
    menubar.add_cascade(label="이메일보내기",menu=sendMenu)
    window.config(menu=menubar)

InitMenuBar()
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitSortListBox()
window.mainloop()




