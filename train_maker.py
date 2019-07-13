import os

path='[enter path of your directory where the images are stored]'



imgList=os.listdir(path)

print(imgList)

textFile=open('train.txt','w')


for img in imgList:
    imgPath=path+ img +'\n'
    textFile.write(imgPath)
