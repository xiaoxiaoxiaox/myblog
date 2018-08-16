from django.contrib import admin

from .models import Question, Choice
# Register your models here.


# 创建一个关联类
# class ChoiceInline(admin.StackedInline):
# 已一个表格单行的形式展示关联类
class ChoiceInline(admin.TabularInline):
    # 绑定的模型
    model = Choice
    # 展示的关联数量 如  1:3
    extra = 3


# 创建一个后台管理类
class QuestionAdmin(admin.ModelAdmin):
    # 定义字段集
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('datetime', {'fields': ['pub_date']})
    ]
    # 关联的对象
    inlines = [ChoiceInline]
    # 需要展示出去的信息，可以是函数
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加一个过滤器
    list_filter = ['pub_date']
    # 在后台显示一个查询框，设置查询的字段，以like方式查询
    search_fields = ['question_text']


# 注册后台管理对象
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
