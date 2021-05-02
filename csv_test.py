import csv
import matplotlib.pyplot as plt
from datetime import datetime

"""

fn='Weather.csv'

with open(fn) as file:
    csvReader=csv.reader(file)
    headerRow=next(csvReader)    # 讀取文件下一行（讀取標題的方法）
for i,header in enumerate(headerRow):
    print(i,header)

"""

"""
一、enumerate( )函数说明

1.enumerate()是python的内置函数

2.enumerate在字典上是枚举、列举的意思

3.对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。（即可以将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标。）

4.enumerate多用于在for循环中得到计数

"""

"""

# 讀取最高溫與最低溫，並繪製圖形

fn='Weather.csv'
with open (fn) as file:
    csvReader=csv.reader(file)
    #headerRow=next(csvReader)     # 讀取文件下一行
    highTemps,lowTemps=[],[]       # 設定空字串
    for row in csvReader:
        highTemps.append(row[1])   # 儲存最高溫
        lowTemps.append(row[3])    # 儲存最低溫

print("最高溫",highTemps)
print("最低溫",lowTemps)


plt.plot(highTemps)

plt.show()

# 設定繪圖區大小
# figure(dpi=n,figsize(width,height))
# plt.figure(dpi=80,figsize=(12,8))

"""
"""
# 利用strptime(string,format)將日期字串解析為日期物件
# string:是要解析日期字串
# format:是該日期字串目前格式

dateObj=datetime.strptime('2017/1/1','%Y/%m/%d')
print(dateObj)

"""

"""
# 在圖表增加日期刻度
# 日期位置的旋轉
# fig=plt.figure(相關設定資訊)
# fig.autofmt_xdate(rotation=xx) #rotation若省略則系統使用最佳化預設


fn='Weather.csv'

with open(fn) as file:
    csvReader=csv.reader(file)
    headerRow=next(csvReader)     # 讀取文件的下一行
    dates,highTemps=[],[]         # 設定空串列
    for row in csvReader:
        highTemps.append(int(row[1]))
        currentDate=datetime.strptime(row[0],"%Y/%m/%d" )
        dates.append(currentDate)
    
fig=plt.figure(dpi=80,figsize=(12,8))  # 設定繪圖區大小
plt.plot(dates,highTemps)              # 圖標增加日期刻度
fig.autofmt_xdate()                    # 日期旋轉
plt.title("Weather Report Jan. 2017",fontsize=24)
plt.xlabel("",fontsize=14)
plt.ylabel("Temperature",fontsize=14)
plt.tick_params(axis='both',labelsize=12,color='red')   # 指標變紅色的
plt.show()

"""

# 繪製最高溫及最低溫，並填滿之間的區域

# 可以使用fill_between()方法執行填滿最高溫與最低溫

fn='Weather.csv'

with open(fn) as file:
    csvReader=csv.reader(file)
    headerRow=next(csvReader)                 # 讀取文件的下一行
    dates,highTemps,lowTemps=[],[],[]         # 設定空串列
    for row in csvReader:
        try:
            currentDate=datetime.strptime(row[0],"%Y/%m/%d" )
            highTemp=int(row[1])     # 設定最高溫
            lowTemp=int(row[3])      # 設定最低溫
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)   # 儲存最高溫
            lowTemps.append(lowTemp)     # 儲存最低溫
            dates.append(currentDate)    # 儲存日期

fig=plt.figure(dpi=80,figsize=(12,8))    # 設定繪圖區大小
plt.plot(dates,highTemps)                # 繪製最高溫
plt.plot(dates,lowTemps)                 # 繪製最低溫
fig.autofmt_xdate()                      # 日期旋轉
plt.fill_between(dates,highTemps,lowTemps,color='y',alpha=0.2)
plt.show()