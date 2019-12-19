from django.shortcuts import render

# Create your views here.
def friends(request):
    name = ['kritika','shashank','nischal','aashish','ayush']
    d ={
        'friends_name': name
    }
    return render(request,'friend_app/friends_name.html',d)

def bestfriends(requests):
    name = ['Sumana','Sujena','Samika']
    d ={
        'best_friends':name
    }
    return render(requests,'friend_app/best_friends.html',d)