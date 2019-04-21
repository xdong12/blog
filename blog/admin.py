from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


class PictureAdmin(admin.ModelAdmin):

    list_display = ['title', 'image', 'link']
    fields = ['title', 'image']

    def save_model(self, request, obj, form, change):
    #     with open(obj.image.path, 'rb') as f:
    #         img_data = f.read()
    #
    #     from utils.qiniu_storage import storage
    #     ret = storage(img_data)
    #     obj.link = 'http://pps8t245f.bkt.clouddn.com/' + ret
        obj.link = 'http://47.107.86.48/media/image/' + obj.image.name
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Picture, PictureAdmin)
