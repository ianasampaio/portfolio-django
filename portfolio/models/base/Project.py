from django.db import models

class Project(models.Model): 


    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description',null=True, blank=True)
    technology = models.CharField('Technology',max_length=20)
    image = models.FilePathField(path="/img")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['title']


    def __str__(self):
        return self.title
