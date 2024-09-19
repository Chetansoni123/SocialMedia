from django.shortcuts import render, redirect
from posts.models import Post
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from users.models import Mobile, friends
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Get all the post from database table and render in template
# class PostListView(ListView):
#     model = Post
#     template_name = 'posts/home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']

#     def get_context_data(self,*args, **kwargs):
#         context = super(PostListView, self).get_context_data(*args,**kwargs)
#         connected_friends = friends.objects.filter(user_friend=self.request.user)
#         friends_list = []
#         for x in connected_friends:
#             friends_list.append(x.conn_user)
#         friends_list.append(self.request.user.username)
#         context['friends_list'] = friends_list
#         return context

@login_required
def showPost(request):
    posts = Post.objects.all().order_by('-date_posted')
    connected_friends = friends.objects.filter(user_friend=request.user)
    friends_list = []
    for x in connected_friends:
        friends_list.append(x.conn_user)
    friends_list.append(request.user.username)
    context = {
        'posts' : posts,
        'friends_list' : friends_list,
    }
    return render(request, 'posts/home.html', context)


class PostDetailView(DetailView):
    model = Post
    object = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_post = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'img']

    def form_valid(self, form):
        form.instance.user_post = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_post:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_post:
            return True
        return False


# class showAllUser(ListView):
#     model = User
#     template_name = 'posts/alluser.html'
#     context_object_name = 'all_user'


def showAllUser(request):
    all_user = User.objects.all()
    to_check_friend = friends.objects.filter(user_friend=request.user)
    request_user = request.user
    friend = []
    for x in to_check_friend:
        friend.append(x.conn_user)
    
    context = {
        'all_user' : all_user,
        'friend' : friend,
        'request_user' : request_user,
    }
    return render(request, 'posts/alluser.html', context)

class UserDetailView(DetailView):
    model = User
    template_name = 'posts/user_detail.html'

    def get_context_data(self,*args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args,**kwargs)
        all_friends = friends.objects.filter(user_friend=self.object)
        fri_list = []
        for x in all_friends:
            fri_list.append(x.conn_user)

        context['fri_list'] = fri_list
        context['hello'] = 'hello'
        return context


def search(request):
    query = request.GET['query']   
    all_user = User.objects.all()
    request_user = request.user
    to_check_friend = friends.objects.filter(user_friend=request.user)
    friend = []
    for x in to_check_friend:
        friend.append(x.conn_user)
        

    try:
        if type(int(query)) == int:
            mob_user = Mobile.objects.get(mobile=query)
            context = {
                'username' : mob_user.user_mobile.username,
                'email' : mob_user.user_mobile.email,
                'mobile' : mob_user.user_mobile.mobile.mobile,
                'all_user' : all_user,
                'request_user' : request_user,
                'friend' : friend,
                'mob_user' : mob_user,
                'query' : query,
            }
            return render(request, 'posts/search.html', context) 

    except ValueError:
        x = True

    if x:
        found = User.objects.filter(Q(username=query) | Q(email=query))
        context = {
            'found' : found,
            'all_user' : all_user,
            'request_user' : request_user,
            'to_check_friend' : to_check_friend,
            'friend' : friend,
            'query' : query,
        }
        return render(request, 'posts/search.html', context)



