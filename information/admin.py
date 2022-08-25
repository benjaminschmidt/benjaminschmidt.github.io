from ast import Not
from django.contrib import admin

from .models import Author, Article, Degree, Job, Myself, Note, Poster
from .models import PosterPresentation, Skill, SoftwareProject, Talk
from .models import TaughtClass, Thesis

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Degree)
admin.site.register(Job)
admin.site.register(Myself)
admin.site.register(Note)
admin.site.register(Poster)
admin.site.register(PosterPresentation)
admin.site.register(Skill)
admin.site.register(SoftwareProject)
admin.site.register(Talk)
admin.site.register(TaughtClass)
admin.site.register(Thesis)
