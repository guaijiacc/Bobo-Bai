#设计city_air类
class city_air:
    def __init__(self,now):           # __init__()方法中的参数now为一个字典变量，将now的值传给对象
        self.name = now['city']
        self.AQI = now['AQI']
        self.quality = now['quality']
        self.date = now['date']
    def answer(self):                 # answer（）方法整合对象携带的信息，将信息以字符串形式返回
        str1 = '\n' + self.name + '空气质量如下:\nAQI:' + self.AQI + '\nQuality:' + self.quality + '\nDate:' + self.date + '\n'
        if int(self.AQI)<=100:
            str2 = '空气不错，抽空去健身吧！'
        elif int(self.AQI)<=150:
            str2 = ('空气质量不是很好，尽量避免户外运动')
        else:
            str2 = 'Attention！，不要长时间呆在室外，保重身体最要紧！'
        return(str1 + str2)
