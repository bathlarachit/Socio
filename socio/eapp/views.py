from django.shortcuts import render,get_list_or_404,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib import auth
from django.db.models import Q
from eapp import models
# Create your views here.
class home(TemplateView):
    template_name='eapp/index.html'

    
def h(request):
    return render(request,'eapp/index.html')
class list(LoginRequiredMixin,ListView):
    template_name='eapp/friends.html'
    context_object_name='list'
    #
    model=models.friend

    def get_queryset(self):
        qs=super(list,self).get_queryset()
        return qs.filter(user1__exact=self.request.user)
class ListAll(LoginRequiredMixin,ListView):
    template_name='eapp/all.html'
    context_object_name='list'
    model=models.friend


def addfriend(request,pk):
    print(request.user.id)
    f=models.friend.objects.create(user1_id=request.user.id,fri1_id=pk)
    f2=models.friend.objects.create(user1_id=pk,fri1_id=request.user.id)
    #f.save()
    return HttpResponseRedirect(reverse('home'))
def chat(request,pk):
    try:
        friends=models.friend.objects.filter(user1_id=request.user.id)
    except:
        pass


    if request.method =='POST':
        mg=request.POST.get('msg')
        code=mg[:1]

        try:
            import googletrans
            #
            trs=googletrans.Translator()
            if "0" in code:
                mg=mg[1:]
            elif "1" in code:
                mg=trs.translate(str(mg[1:]),dest='en').text


            elif "2"in code:
                m=trs.translate(str(mg[1:]),dest='en').text
                mg=trs.translate(str(t),src='en',dest='de').text

            elif "3" in code:
                m=trs.translate(str(mg[1:]),dest='en').text
                mg=trs.translate(str(t),src='en',dest='fr').text

        except:
            pass




        ms=models.chat.objects.create(user_id=request.user.id,fri3_id=pk,msg=mg)

        ms.save()
        try:

            combi=models.chat.objects.filter(Q(user_id=request.user.id,fri3_id=pk) |Q(user_id=pk,fri3_id=request.user.id)).order_by('time')
            chat={}
            x=0
            for i in combi:
                a={}
                a["mg"]=i.msg
                #print(i.msg)
                a["time"]=i.time
                a["main"]="media w-50 ml-auto mb-3"
                a["mid"]="media-body"
                a["end"]="bg-primary rounded py-2 px-3 mb-2"
                a["t"]="w"
                if i.user == request.user:
                    a["main"]="media w-50 ml-auto mb-3"
                    a["mid"]="media-body"
                    a["end"]="bg-primary rounded py-2 px-3 mb-2"
                    a["t"]="w"
                else:
                    a["main"]="media w-50 mb-3"
                    a["mid"]="media-body ml-3"
                    a["end"]="bg-light rounded py-2 px-3 mb-2"
                    a["t"]="t"

                #    print("not match")
                chat[x]=a
                x=x+1


        except:pass
        return render(request,'eapp/check.html',{'combi':combi,'chat':chat,'friends':friends})
    else:
        try:

            combi=models.chat.objects.filter(Q(user_id=request.user.id,fri3_id=pk) |Q(user_id=pk,fri3_id=request.user.id)).order_by('time')
            chat={}
            x=0
            for i in combi:
                a={}
                a["mg"]=i.msg

                a["time"]=i.time
                a["main"]="media w-50 ml-auto mb-3"
                a["mid"]="media-body"
                a["end"]="bg-primary rounded py-2 px-3 mb-2"
                a["t"]="w"
                if i.user == request.user:
                    a["main"]="media w-50 ml-auto mb-3"
                    a["mid"]="media-body"
                    a["end"]="bg-info rounded py-2 px-3 mb-2"
                    a["t"]="w"
                else:
                    a["main"]="media w-50 mb-3"
                    a["mid"]="media-body ml-3"
                    a["end"]="bg-light rounded py-2 px-3 mb-2"
                    a["t"]="t"


                chat[x]=a
                x=x+1
        except:pass
        return render(request,'eapp/check.html',{'combi':combi,'chat':chat,'friends':friends})


def makeFriends(request):
    if request.method=='POST':
            try:
                uname=request.POST.get('search')
                qs=auth.models.User.objects.filter(username__startswith=uname)
                length=len(qs)
                if length > 0:
                    msg ='We got something for you'
                else :msg='No found'
                return render(request,'eapp/result.html',{'qs':qs,'name':uname,'msg':msg})
            except:pass


    else:
        return render(request,'eapp/all.html',{})

class Profile(LoginRequiredMixin,CreateView):
    template_name='eapp/profile.html'
    model=models.Profile
    fields=('photo','profession','city','country')
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(Profile,self).form_valid(form)

    #

class ProfileDetail(LoginRequiredMixin,DetailView):
    model=models.Profile
    template_name='eapp/detail.html'
    context_object_name='detail'

    #def get_context_data
class CreateWeb(LoginRequiredMixin,CreateView):
    template_name='eapp/web.html'
    model=models.web
    fields='__all__'
    success_url=reverse_lazy('home')
def check(request):
    try:
        qs=models.Profile.objects.filter(user_id=request.user.id)
        if len(qs) == 0:
            return HttpResponseRedirect(reverse('profile'))
        else:
            return render(request,'eapp/index.html')
    except:pass
    return HttpResponseRedirect(reverse('home'))

class CreatePost(LoginRequiredMixin,CreateView):
    template_name='eapp/post.html'
    fields=('photo','caption')
    success_url=reverse_lazy('out')
    model=models.post
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super(CreatePost,self).form_valid(form)


def postlist(request):
    lt={}
    try:
        flist=models.friend.objects.filter(user1_id=request.user.id)
        ow=models.post.objects.filter(owner_id=request.user.id)
        for i in flist:
            q=models.post.objects.filter(owner_id=i.fri1.id)
            ow=ow.union(q)

    except:
        pass
    return render(request,'eapp/postlist.html',{'list':ow})
