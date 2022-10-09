from django.http import HttpResponse
from django.template import loader

from .models import Article, Degree, Job, Myself, Note, PosterPresentation
from .models import Skill, SoftwareProject, Talk, TaughtClass

def coding(request):
    degrees = Degree.objects.order_by('-end_date')
    frameworks = Skill.objects.filter(type_of_skill=Skill.FRAMEWORK)
    jobs = Job.objects.order_by('-start_date')
    languages = Skill.objects.filter(type_of_skill=Skill.LANGUAGE)
    myself = Myself.objects.get(id = 1)
    others = Skill.objects.filter(type_of_skill=Skill.OTHERS)
    software_projects = SoftwareProject.objects.order_by('-last_update')
    template = loader.get_template('information/coding.html')
    tools = Skill.objects.filter(type_of_skill=Skill.TOOL)
    return HttpResponse(template.render({'degrees': degrees,
                                         'frameworks': frameworks,
                                         'jobs': jobs,
                                         'myself': myself,
                                         'others': others,
                                         'languages': languages,
                                         'software_projects': software_projects,
                                         'tools': tools},
                                        request))

def math(request):
    articles = Article.objects.order_by('-pub_date')
    classes = TaughtClass.objects.order_by('-date')
    conference_talks = Talk.objects.filter(talk_type=Talk.CONFERENCE).order_by('-date')
    degrees = Degree.objects.order_by('-end_date')
    jobs = Job.objects.order_by('-end_date')
    local_talks = Talk.objects.filter(talk_type=Talk.LOCAL).order_by('-date')
    myself = Myself.objects.get(id = 1)
    notes = Note.objects.order_by('-title')
    posters_presentations = PosterPresentation.objects.order_by('-date')
    seminar_talks = Talk.objects.filter(talk_type=Talk.SEMINAR).order_by('-date')
    software_projects = SoftwareProject.objects.filter(academic=True).order_by('-last_update')
    template = loader.get_template('information/math.html')
    return HttpResponse(template.render({'articles': articles,
                                         'classes': classes,
                                         'conference_talks': conference_talks,
                                         'degrees': degrees,
                                         'jobs': jobs,
                                         'local_talks': local_talks,
                                         'myself': myself,
                                         'notes': notes,
                                         'posters_presentations': posters_presentations,
                                         'seminar_talks': seminar_talks,
                                         'software_projects': software_projects},
                                        request))
