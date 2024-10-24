from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
from . models import Brain
import os

# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request,"about.html")


def upload(request):
    if request.method=='POST':
        Classes=[]
        m1 = int(request.POST['alg'])
        paths=os.listdir('app/Data/test/')
        for i in paths:
            Classes.append(i)
        File=request.FILES['brain']
        s=Brain(image=File)
        s.save()
        path1='app/static/saved/' + s.Imagename()

        print(path1)

        if m1==1:
            model=load_model('app/models/Cnn.h5')
            x1=image.load_img(path1,target_size=(224,224))
            x1=image.img_to_array(x1)
            x1=np.expand_dims(x1,axis=0)
            x1/=255
            
        elif m1==2:
            model=load_model('app/models/SVM model.h5')
            x1=image.load_img(path1,target_size=(128,128))
            x1=image.img_to_array(x1)
            x1=np.expand_dims(x1,axis=0)
            x1/=255

        

        result= model.predict(x1)        
        # a = classes[]
        b = np.argmax(result)
        results=Classes[b]
        print(results)
        return render(request,"result.html",{"message":results,"path":'/static/saved/' + s.Imagename()})

    return render (request,"upload.html")

