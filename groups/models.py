from django.db import models
#allows to use spaces etc for formatting
from django.utils.text import slugify
#for link embedding
import misaka

#gets the user models that's currently active in the project
from django.contrib.auth import get_user_model



#call things off the current user's session
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def__str__(self):
        return self.name

    def save(self,*args,**kwargs):
        #replacing and lowercasing things for the self.name
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    #attributes
    group = model.ForeignKey(Group,related_name='memberships')
    # this comes from the get_user_model
    user = models.ForeignKey(User,related_name='user_group')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
