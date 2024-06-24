from django.shortcuts import render,get_object_or_404
from .models import Course,Subject,Chapter,Question,Quiz
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def home(request):
    course=Course.objects.all()

    data={
        "course":course
    }
    return render(request,"home.html",data)
# def home(request):
#     course=Course.objects.all()
#     if request.method == "POST":
#        a=request.POST.get("1")
#        b=request.POST.get("2")
#        c=int(a)+int(b)
#        return render(request,"home.html",{"c":c})
             

#     data={
#         "course":course
#     }
#     return render(request,"home.html",data)
@login_required
def subject(request,id):
    subject=Subject.objects.filter(course=id)
    print(subject)
    data={
        "subject":subject

    }
    return render(request,"subject.html",data)

@login_required
def chapter(request ,pk,id):
    chapters=Chapter.objects.filter(subject=pk )  
    
    return render(request,"chapter.html",{"chapter":chapters})
@login_required
def content (request,pk,id,dk):
    content = get_object_or_404(Chapter, id=dk)
    data=None
    try:
    # Assuming `dk` is a variable containing the chapter value you're querying for
     data = get_object_or_404(Quiz, chapter=dk)
    # Process `data` as needed
    except Http404:
    # If the object is not found, do nothing (continue execution without any action)
     pass
    print(content.name)
    return render(request,"content.html",{"content1":content ,"data":data}) 
@login_required
def about(request):
    return render(request,"about.html")

# def quiz(request,id):
#     quiz=Quiz.objects.all()

#     return render(request,"quizname.html",{"quiz":quiz})


def quiz(request,id):
    question=Question.objects.filter(quiz=id)
    if request.method=="POST":
        score=0
        num=0
        for i in question:
          num+=1
          c=i.answer  
          g=request.POST.get(str(i.id))
          if str(c)==g:
              score+=4

        return render(request,"quizresult.html",{"score":score,"quiz_name": question[0].quiz.name,"num":num})      
    

    return render(request,"quiz.html",{"question":question,"quiz_name": question[0].quiz.name})