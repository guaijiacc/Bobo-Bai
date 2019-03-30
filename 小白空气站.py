import requests
import json
from tkinter import *
from return_class import city_air   #从文件return_class中导入类city__air

#定义Button函数的回调函数show（）
def show():
    city = entry.get()
    url = 'http://web.juhe.cn:8080/environment/air/cityair?city=' + city + '&key=eb8c5e0205779b04cc4031f2ceb2db50'
    response = requests.get(url)
    hjson = json.loads(response.text)
    print(hjson)
    if hjson['resultcode'] == '200':    #响应成功
        now = hjson['result'][0]['citynow']
        City = city_air(now)
        txt1 = City.answer()
    else:                               #响应失败
        txt1 = '无法找到此城市'
    lbl2.config(None,text = txt1)       #动态设置标签lbl2的显示文本
    lbl2.pack()

#创建GUI界面
root = Tk()
lbl1 = Label(root,text = '小白空气站\n输入您想查询的城市(输入汉字或拼音)：')
lbl1.pack()
entry = Entry(root,width = 80)
entry.pack()
lbl2 = Label(root)
btn = Button(root,text = '搜索',command = show)
btn.pack()
root.mainloop()



