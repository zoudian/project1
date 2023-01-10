# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# coding=utf-8
import urllib
import re
import datetime
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    # splitReg = r'[\s\"\,\，\']+'
    splitReg = r'[\s\"]+'  # 不区分,
    tempList = re.split(splitReg, html.decode('utf-8'))  # 分割后获得一个list （数组）

    imgUrls = []  # 一个空list

    x = 0
    for str in tempList:
        matchReg = r'https:.*.jpg'
        if re.match(matchReg, str):
            print
            '%s--' % x + str
            imgUrls.append(str)
            x = x + 1
            urllib.request.urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now(), x))
        matchReg1 = r'https:.*.png'
        if re.match(matchReg1, str):
            print
            '%s--' % x + str
            imgUrls.append(str)
            x = x + 1
            urllib.request.urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now().date(), x))
    print(imgUrls)
    return imgUrls

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    html = getHtml('http://www.thejoyrun.com')
    print(html)
    getImg(html)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
