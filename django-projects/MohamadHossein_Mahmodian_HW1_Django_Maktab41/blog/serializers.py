from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    slug = serializers.SlugField()
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField()
    draft = serializers.BooleanField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('code', instance.slug)
        instance.content = validated_data.get('linenos', instance.content)
        instance.update_at = validated_data.get('linenos', instance.update_at)
        instance.image = validated_data.get('style', instance.image)
        instance.draft = validated_data.get('style', instance.draft)
        instance.save()
        return instance
