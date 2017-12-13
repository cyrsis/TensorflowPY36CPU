#!/usr/bin/env python
#-*- coding:UTF-8 -*-

def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

def main():
    print('這是一個求階乘的程序\n')
    n = raw_input('請輸入一個正整數:')
    try:
        n = int(n)
    except ValueError:
        print('輸入錯誤，要求輸入一個正整數，退出重來吧。')
    print('%d! = %d' %(n,fac(n)))


if __name__ == '__main__':
    main()

