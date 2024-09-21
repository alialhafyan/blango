from rest_framework import serializers
from blog.models import Post,Tag
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from blog.api.views import *
class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True,
        queryset=Tag.objects.all()
    )

    author_id = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        view_name="api_user_detail",
        lookup_field="email")

    class Meta:
      model = Post
      fields = [ "author","title", "slug", "summary", "content", "tags"]
      read_only_fields = ["modified_at", "created_at", "published_at"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
class Tagserializer(serializers.ModelSerializer):
  class Meta:
    model=Tag
    fields="__all__"
