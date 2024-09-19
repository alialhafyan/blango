from rest_framework import serializers
from blog.models import Post,Tag
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from .views import UserDetail,PostDetail,PostList
class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True,
        queryset=Tag.objects.all()
    )

    author_id = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail")
        def get_url(self, obj, view_name, request, format):
            url_kwargs = {
                'User_email': obj.User.email,
                'User_pk': obj.pk}
        
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

        def get_object(self, view_name, view_args, view_kwargs):
            lookup_kwargs = {
                'User_email': view_kwargs['User_email'],
                'User_pk': view_kwargs['User_pk']
        }
            return self.get_queryset().get(**lookup_kwargs)
    

    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
