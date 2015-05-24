from django.contrib import admin

from .models import Problem, Test, Solution, TestResult, PassReset, Confirmation

class TestInLine(admin.TabularInline):
	model = Test
	extra = 3

class ProblemAdmin(admin.ModelAdmin):
	fieldsets = [
		('Titel', {'fields': ['title',]}),
		(None, {'fields': ['statement',], 'classes': ['wide',]}),]

	inlines = [TestInLine]
	search_fields = ['title']

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(PassReset)
admin.site.register(Confirmation)
