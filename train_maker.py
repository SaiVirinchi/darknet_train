import os
path=os.path.dirname(os.path.abspath(__file__))
#path='[enter path of your directory where the images are stored]'
print('Your Image folder name')
image= input()
imgList=os.listdir(image)
print(imgList)
textFile=open('trainy.txt','a')
for img in imgList:
    file = os.path.splitext(img)[1]
    if file == '.JPG':
        imgPath=path+image+'/'+ img +'\n'
        textFile.write(imgPath)
        print('success')
    elif file == '.jpg':
        imgPath=path+image+'/'+ img +'\n'
        textFile.write(imgPath)
        print('success')
    else:
        print(file)
