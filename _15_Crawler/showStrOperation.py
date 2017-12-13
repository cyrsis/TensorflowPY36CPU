#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

def strCase():
    "字串大小寫轉換"
    print (u'示範字串大小寫轉換')
    print (u"示範字串S儲存值為：'  ThIs is a PYTHON  '")
    S = '  ThIs is a PYTHON  '
    print (u"大寫轉換成小寫：\tS.lower() \t= %s"%(S.lower()))
    print (u"小寫轉換成大寫：\tS.upper() \t= %s"%(S.upper()) )
    print (u"大小寫轉換：\t\tS.swapcase() \t= %s"%(S.swapcase()) )
    print (u"首字母大寫：\t\tS.title() \t= %s"%(S.title()) )
    print (u'\n' )

def strFind():
    "字串搜索、替換"
    print (u"示範字串搜索、替換等"   )
    print (u"示範字串S儲存值為：'  ThIs is a PYTHON  '"   )
    S = '  ThIs is a PYTHON  '
    print (u"字串搜索：\t\tS.find('is') \t= %s"%(S.find('is'))   )
    print (u"字串統計：\t\tS.count('s') \t= %s"%(S.count('s'))   )
    print (u"字串替換：\t\tS.replace('Is','is') = %s"%(S.replace('Is','is')) )
    print (u"去左右空格：\t\tS.strip() \t=#%s#"%(S.strip())  )
    print (u"去左邊空格：\t\tS.lstrip() \t=#%s#"%(S.lstrip()) )
    print (u"去右邊空格：\t\tS.rstrip() \t=#%s#"%(S.rstrip()) )
    print (u'\n'  )


def strTest():
    "字串測試"
    print (u"示範字串測試")
    print (u"示範字串S儲存值為：'abcd'")
    S1 = 'abcd'
    print (u"測試S.isalpha() = %s"%(S1.isalpha()) )
    print (u"測試S.isdigit() = %s"%(S1.isdigit()) )
    print (u"測試S.isspace() = %s"%(S1.isspace()) )
    print (u"測試S.islower() = %s"%(S1.islower()) )
    print (u"測試S.isupper() = %s"%(S1.isupper()) )
    print (u"測試S.istitle() = %s"%(S1.istitle()) )


def strSplit():
    "字串分割、組合"
    print (u"示範字串分割、組合"    )
    print (u"示範字串S儲存值為：'  ThIs is a PYTHON  '" )
    S = '  ThIs is a PYTHON  '
    print (u"字串分割：\t\tS.split() \t= %s"%(S.split()) )
    print (u"字串組合1： '#'.join(['this','is','a','python']) \t= %s"%('#'.join(['this','is','a','python']))  )
    print (u"字串組合2： '$'.join(['this','is','a','python']) \t= %s"%('$'.join(['this','is','a','python']))   )
    print (u"字串組合3： ' '.join(['this','is','a','python']) \t= %s"%(' '.join(['this','is','a','python']))   )
    print (u'\n'   )

def strCode():
    "字串編碼、解碼"
    print (u"示範字串編碼、解碼"   )
    print (u"示範字串S儲存值為：'編碼解碼測試'"   )
    S = '編碼解碼測試'
    print (u"utf-8編碼的S \t = %s"%(S)   )
    print (u"utf-8編碼的S轉換unicode編碼"   )
    print (u"S.decode('utf-8')= %s"%(S.decode("utf-8"))   )
    print (u"utf-8編碼的S轉換成utf8"   )
    print (u"S.decode('utf-8').encode('utf8') = %s"%(S.decode("utf-8").encode("utf8"))   )

    print (u"注意：不管是編碼還是解碼針對的都是unicode字串編碼，\n所以要編碼或者解碼前必須先將源字串轉換成unicode編碼格式" )
    print (u'\n')



if __name__ == '__main__':
        strCase()
        strFind()
        strSplit()
        strCode()
        strTest()
