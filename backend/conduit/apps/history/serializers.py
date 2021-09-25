from rest_framework import serializers

from conduit.apps.profiles.serializers import ProfileSerializer

from .models import History
from .relations import TagRelatedField


class HistorySerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    tagList = TagRelatedField(many=True, required=False, source='tags')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = History
        fields = (
            'author',
            'body',
            'description',
            'slug',
            'tagList',
            'title',
            'updatedAt',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        tags = validated_data.pop('tags', [])

        article = History.objects.create(author=author, **validated_data)

        for tag in tags:
            article.tags.add(tag)

        return article

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def get_article_history(self, instance):
        pass