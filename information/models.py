from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    arxiv = models.CharField(max_length=200)
    journal = models.CharField(max_length=200, blank=True, default='')
    pub_date = models.DateField()
    coauthors = models.ManyToManyField(Author, blank=True)
    comment = models.CharField(max_length=200, blank=True, default='')
    pdf = models.FileField(upload_to = 'pdfs/')
    highlight = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Thesis(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to = 'pdfs/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Theses"


class Order(models.Model):
    position = models.IntegerField()


class Degree(models.Model):
    advisor = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=True)
    degree_type = models.CharField(max_length=200)
    end_date = models.DateField()
    start_date = models.DateField()
    thesis = models.ForeignKey(Thesis, blank=True, null=True, on_delete=models.CASCADE)
    university = models.CharField(max_length=200)

    def __str__(self):
        return self.degree_type


class Job(models.Model):
    employer = models.CharField(max_length=200)
    end_date = models.DateField()
    start_date = models.DateField()
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.employer


class Myself(models.Model):
    academic_description = models.TextField()
    current_employer = models.CharField(max_length=200)
    email = models.EmailField()
    general_description = models.TextField()
    git = models.URLField()
    linkedin = models.URLField()
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to = 'images/')
    professional_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Myself"


class Note(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to = 'pdfs/')

    def __str__(self):
        return self.title


class Poster(models.Model):
    pdf = models.FileField(upload_to = 'pdfs/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class PosterPresentation(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=200)
    occasion = models.CharField(max_length=200)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + ': ' + self.occasion + '. '+ self.location + '.'


class Talk(models.Model):
    CONFERENCE = "CT"
    LOCAL = "LT"
    SEMINAR = 'ST'
    date = models.DateField()
    location = models.CharField(max_length=200)
    occasion = models.CharField(max_length=200)
    talk_type = models.CharField(max_length=20,
                                 choices=[(CONFERENCE, 'Conference Talk'),
                                          (LOCAL, 'Local Talk'),
                                          (SEMINAR, 'Seminar Talk'),],
                                 default=LOCAL,)

    def __str__(self):
        return str(self.date) + ': ' + self.occasion + '. '+ self.location + '.'


class Skill(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
    BASIC = '1'
    INTERMEDIATE = '2'
    EXPERT = '3'
    skill_level = models.CharField(max_length=2,
                                   choices=[(BASIC, 'basic familiarity'),
                                            (INTERMEDIATE, 'regular usage'),
                                            (EXPERT, 'expert'),],
                                   default=BASIC,)
    LANGUAGE = 'LG'
    FRAMEWORK = 'FR'
    TOOL = 'TL'
    OTHERS = 'OT'
    type_of_skill = models.CharField(max_length=20,
                                     choices=[(LANGUAGE,
                                               'Programming language'),
                                              (FRAMEWORK,
                                               'Framework'),
                                              (TOOL,
                                               'Tool'),
                                              (OTHERS,
                                               'Other skills'),],
                                     default=OTHERS,)
    LT_ONE = '1-'
    ONE = '1'
    TWO = '2'
    GT_THREE = '3+'
    GT_FIVE = '5+'
    GT_TEN = '10+'
    years_of_experience = models.CharField(max_length=20,
                                     choices=[(LT_ONE, '< 1 year of experience'),
                                              (ONE, '1 year of experience'),
                                              (TWO, '2 years of experience'),
                                              (GT_THREE, '3+ years of experience'),
                                              (GT_FIVE, '5+ years of experience'),
                                              (GT_TEN, '10+ years of experience'),],
                                     default=ONE,)

    def __str__(self):
        return self.name


class SoftwareProject(models.Model):
    academic = models.BooleanField(default=False)
    comment = models.CharField(max_length=200)
    github = models.URLField()
    last_update = models.DateField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class TaughtClass(models.Model):
    course = models.CharField(max_length=200)
    date = models.DateField('Start of semester')
    institution = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)

    def __str__(self):
        return self.semester + ': ' + self.course

    class Meta:
        verbose_name_plural = "Taught classes"

