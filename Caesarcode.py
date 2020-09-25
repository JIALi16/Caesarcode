#Time:2020/9/24
#Author:3120004699
#Python 3.8.6
#Name:凯撒密码

import urllib.request
import time

print("输入数字1进行加密，输入数字2进行解密，输入其他数字保存Bing的每日一图。")

first =int( input("请输入内容:"))                             #从控制台读取输入内容
if first==1:
    
    word1 = input("进入加密模式!!!\n请输入一串字符串:")        #从控制台读取输入内容
    key1 = int(input("输入偏移位数（默认偏移量为3）:"))
    print ("经过凯撒加密结果为:")
    
    for letter1 in word1 :
        
        if "a"<=letter1<="z":
            print(chr(ord("a")+(ord(letter1)-ord("a")+key1)%26),end="")       #区分字母大小写进行判断，取余运算%
        
        elif "A"<=letter1<="Z":
            print(chr(ord("A")+(ord(letter1)-ord("A")+key1)%26),end="")
            
        else :
            print(letter1,end="")
    
elif first==2:
        
    word2 = input("进入解密模式!!!\n请输入一串字符串:")
    key2 = int(input("输入偏移位数（默认偏移量为3）:"))
    print ("经过凯撒解密结果为:")
    
    for letter2 in word2 :

        if "a"<=letter2<="z":
                
            print(chr(ord("a")+(ord(letter2)-ord("a")-key2)%26),end="")
           
        elif "A"<=letter<="Z":
                
            print(chr(ord("A")+(ord(letter2)-ord("A")-key2)%26),end="")
            
        else :
            print(letter2,end="")
    
else :
    
    url="https://cn.bing.com/th?id=OHR.LoarreCastle_ZH-CN1136982025_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"      #打开必应每日一图
    addr=time.strftime('%Y.%m.%d',time.localtime(time.time())     #获取当前日期
    web=urllib.request.urlopen(url)
    picture=web.read()
                       
    with open("洛阿雷城堡，西班牙韦斯卡"+addr+".jpg","wb") as f:         #图片保存                                                     
        f.write(picture)
   
    


