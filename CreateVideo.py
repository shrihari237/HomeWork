import os
import cv2




path = "C:/Users/shrih/Downloads/PRO-C105-Student-Boilerplate-main/PRO-C105-Student-Boilerplate-main/Images"


images = []




for file in os.listdir(path):
    name, ext = os.path.splitext(file)


    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file


      #  print(file_name)
               
        images.append(file_name)
       
print(len(images))
count = len(images)
frame = cv2.imread(images[-1])
height,width,channels = frame.shape


size = (width,height)
out = cv2.VideoWriter('Sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),6,size)


# for i in range(count):
#     frame = cv2.imread(images[i])
   
#     out.write(frame)
# out.release()
# print("Done")    
i = 0
while True:
    frame =cv2.imread(images[i])
    cv2.imshow('Sunset',frame)
    i = i-1
    out.write(frame)
    if i == count-1:
       break
    cv2.waitKey(1)





