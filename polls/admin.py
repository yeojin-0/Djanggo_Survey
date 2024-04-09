from django.contrib import admin
from .models import Choice, Question

import datetime
from django.utils import timezone

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    list_filter = ["pub_date"] # 필터별로 변경 목록을 필터링 할 수 있는 필터 사이드바
    search_fields = ["question_text"] # 검색기능 추가
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):  # self 인수 수정
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
