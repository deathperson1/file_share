from django.shortcuts import render

# Create your views here.
def Home(request):
    return render (request,"home/home.html")



def file(request):
    return render(request,"file.html")




def upload_file(request):





    
    return render(request,"file/upload.html")