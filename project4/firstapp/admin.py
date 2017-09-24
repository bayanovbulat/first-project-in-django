from django.contrib import admin
from firstapp.models import Graphs
from firstapp.models import FileModel

class FileModelAdmin(admin.ModelAdmin):
	list_display = ('number','file')
	search_fields = ('number','file')

class GraphsAdmin(admin.ModelAdmin):
	list_display = ('name', 'text')
	search_fields = ('name', 'text')

# Register your models here.
admin.site.register(Graphs, GraphsAdmin)
admin.site.register(FileModel, FileModelAdmin)