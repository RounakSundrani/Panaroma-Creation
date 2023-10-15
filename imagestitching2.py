import cv2,os,sys
try:
    imgs = []
    n=int(input("Enter number of images"))
    for i in range(n):
        name=input("Enter the name of the image")
        if os.path.isfile(name):
            imgs.append(cv2.imread(name))
            imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
    for j in range(n):
        cv2.imshow(str(j+1),imgs[j])

    stitchy=cv2.Stitcher.create()
    (dummy,output)=stitchy.stitch(imgs)

    if dummy != cv2.STITCHER_OK:
        print("stitching ain't successful")
    else:
        print('Your Panorama is ready!!!')

# final output
    cv2.imshow('final result',output)

    cv2.waitKey(0)
except Exception as e:
    print(e)