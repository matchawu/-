# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import os
import glob
from datetime import datetime

# 設定python檔執行路徑
mypath = 'C:\\Users\\wwj\\Pictures'
os.chdir(mypath)

# 列出所有符合副檔名的檔案
filelist = glob.glob('*.jpg') # for all jpg files
print(filelist)

# 列出今天日期(作為檔名)
dateTimeObj = datetime.now()
dateStr = dateTimeObj.strftime("%m-%d")
print(dateStr)

# 開始更新檔名
i = 1
for file in filelist:
    filename = dateStr+'_'+str(i)+'.jpg'
    os.rename(file, filename)
    i += 1
print("Finished.")
