from django.contrib import admin

# Register your models here.
from dlibrary.models import Book, Branch, Feedback


class BookAdmin(admin.ModelAdmin):
    list_filter = ["course", "branch"]
    list_display = ["name", "course", "branch"]


admin.site.register(Book, BookAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


admin.site.register(Branch, BranchAdmin)


class Feedbackadmin(admin.ModelAdmin):
    list_display = ["name", "subject", "message", "user"]
    list_filter = ["name", "user", "subject"]


admin.site.register(Feedback, Feedbackadmin)
