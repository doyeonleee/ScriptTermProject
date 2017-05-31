# -*- coding: utf-8 -*-
from func import *
import urllib.parse
loopFlag = 1

def printMenu():
    print("----------------------")
    print("   쇼핑검색 프로그램   ")
    print("----------------------")
    print("========메뉴==========")
    print("1. 검색 및 출력")
    print("2. G메일 보내기")
    print("3. 종료")


def launcherFunction(menu):
    if menu == '1':
        goods = urllib.parse.quote_plus(str(input("검색할 상품을 입력하세요: ")))
        print("================================================")
        Items = SearchShopping(goods)
    elif menu == '2':
        sendMain()

    elif menu == '3':
        QuitMgr()
    else:
        print("오류 : 잘못된 입력입니다.")

def QuitMgr():
    global loopFlag
    loopFlag = 0
    MemFree()

while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('메뉴를 선택하세요 :'))
    launcherFunction(menuKey)
else:
    print ("Bye")
