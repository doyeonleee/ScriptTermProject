<<<<<<< HEAD
#######################################################################################
# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
Doc = None

def MemFree():
    if checkDocument():
        Doc.unlink()


def MakeHtmlDoc(ItemList):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for item in ItemList:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        TitleText = newdoc.createTextNode("1:" + item[0])
        b.appendChild(TitleText)
        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')
        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("2:" + item[1])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("3:" + item[2])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("4:" + item[3])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("5:" + item[4])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("6:" + item[5])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("7:" + item[6])
        p.appendChild(titleText)

        body.appendChild(p)



        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()


def checkDocument():
    global Doc
    if Doc == None:
        print("Error : Document is empty")
        return False
    return True
=======
#######################################################################################
# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
Doc = None

def MemFree():
    if checkDocument():
        Doc.unlink()


def MakeHtmlDoc(ItemList):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for item in ItemList:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        TitleText = newdoc.createTextNode("1:" + item[0])
        b.appendChild(TitleText)
        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')
        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("2:" + item[1])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("3:" + item[2])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("4:" + item[3])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("5:" + item[4])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("6:" + item[5])
        p.appendChild(titleText)

        body.appendChild(p)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("7:" + item[6])
        p.appendChild(titleText)

        body.appendChild(p)



        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()


def checkDocument():
    global Doc
    if Doc == None:
        print("Error : Document is empty")
        return False
    return True
>>>>>>> origin/master
