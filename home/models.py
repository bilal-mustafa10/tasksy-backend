from django.db import models
from wagtail.models import Page
from modelcluster.models import ClusterableModel
from django.contrib.auth.models import User


class Application(ClusterableModel):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
    companyName = models.CharField(verbose_name="Company Name", max_length=200, blank=False, null=True)
    position = models.CharField(verbose_name="Position", max_length=200, blank=False, null=True)
    description = models.TextField(verbose_name="Job Description", max_length=5000, blank=True, null=True)
    notes = models.TextField(verbose_name="Notes", max_length=5000, blank=True, null=True)
    deadline = models.DateField(verbose_name="Application Deadline", blank=False, null=True)
    status = models.BooleanField(verbose_name="Application Status", blank=False, null=True)
    progress = models.CharField(verbose_name='Application Progress', max_length=200, blank=False, null=True)
    assessment = models.BooleanField(verbose_name="Assessment", blank=False, null=True)
    interviewCall = models.BooleanField(verbose_name="Interview Call", blank=False, null=True)
    interviewFinal = models.BooleanField(verbose_name="Interview Final", blank=False, null=True)
    offer = models.BooleanField(verbose_name="Offer", blank=False, null=True)
    accepted = models.BooleanField(verbose_name="Accepted", blank=False, null=True)

    def __str__(self):
        return str(self.id)


class Document(ClusterableModel):
    id = models.AutoField(primary_key=True)
    applicationId = models.ForeignKey(Application, null=True, blank=False, on_delete=models.SET_NULL)
    userId = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
    title = models.CharField(max_length=255, verbose_name="title", blank=False, null=True)
    type = models.CharField(max_length=255, verbose_name="type", blank=False, null=True)
    file = models.FileField(upload_to="documents", verbose_name="file")

    def __str__(self):
        return str(self.id)
