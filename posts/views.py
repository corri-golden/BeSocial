from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequireMixin
from django.core.urlresolvers import reverse_lazy

# to return a 404 page
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from . import forms
# a function model that allows to set a user object = to get_user_model and call it
from django.contrib.auth import get_user_model

User = get_user_model()

class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    # mixin that allows to provide tuple related model basically the foreignkey
    select_related = ('user', 'group')


class UserPosts(generic.ListView):
    model = model.Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        # get where the username is exactly = to whatever user is clicked on
        try:
            self.post.user = User.objects.prefetch_related('post').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    selected_related = ('user', 'group')

    def def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    # check if the form is valid.  connecting the post to user.
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

    
    