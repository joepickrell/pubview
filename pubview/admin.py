from django.contrib import admin
from pubview.models import Journal, Author, Paper, Account, Vote
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class VoteInline(admin.StackedInline):
	model = Vote
	extra = 1

class AccountAdmin(admin.ModelAdmin):
	model = Account
	inlines = (VoteInline,)

class AccountInline(admin.StackedInline):
	model = Account

class UserAdmin(UserAdmin):
	inlines = (AccountInline,)

class AuthorInline(admin.StackedInline):
    model = Author.papers.through
    extra = 3

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'journal', 'abstract']}),
        ('Date information', {'fields': ['year'], 'classes': ['collapse']}),
    ]
    inlines = [AuthorInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(Author)
#admin.site.register(Vote)
#admin.site.register(Account)
admin.site.register(Paper, PaperAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
