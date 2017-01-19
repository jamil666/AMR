from django.db import models
import PIL

class FirstTable(models.Model):
    TableHeaderBigText = models.CharField(max_length=255, blank=True)
    TableHeaderText = models.TextField(max_length=255, blank=True )
    FirstRowHeader = models.CharField(max_length=255, blank=True)
    FirstRowText = models.TextField(max_length=255, blank=True )
    SecondRowHeader = models.CharField(max_length=255, blank=True)
    SecondRowText = models.TextField(max_length=255, blank=True)
    ThirdRowHeader = models.CharField(max_length=255, blank=True)
    ThirdRowText = models.TextField(max_length=255, blank=True)
    FourthRowHeader = models.CharField(max_length=255, blank=True)
    FourthRowText = models.TextField(max_length=255, blank=True)
    TableImage = models.ImageField(blank=True, upload_to="static/images")


class SecondTable(models.Model):
    TableHeaderBigText = models.CharField(max_length=255, blank=True)
    TableHeaderText = models.TextField(max_length=255, blank=True )
    FirstRowHeader = models.CharField(max_length=255, blank=True)
    FirstRowText = models.TextField(max_length=255, blank=True )
    SecondRowHeader = models.CharField(max_length=255, blank=True)
    SecondRowText = models.TextField(max_length=255, blank=True)
    ThirdRowHeader = models.CharField(max_length=255, blank=True)
    ThirdRowText = models.TextField(max_length=255, blank=True)
    FourthRowHeader = models.CharField(max_length=255, blank=True)
    FourthRowText = models.TextField(max_length=255, blank=True)
    FifthRowHeader = models.CharField(max_length=255, blank=True)
    FifthRowText = models.TextField(max_length=255, blank=True)
    SixthRowHeader = models.CharField(max_length=255, blank=True)
    SixtRowText = models.TextField(max_length=255, blank=True)


class ThirdTable(models.Model):
    TableHeaderBigText = models.CharField(max_length=255, blank=True)
    TableHeaderText = models.TextField(max_length=255, blank=True )
    FirstRowHeader = models.CharField(max_length=255, blank=True)
    FirstRowText = models.TextField(max_length=255, blank=True )
    FirstRowText2 = models.TextField(max_length=255, blank=True)
    Choose1 = models.CharField(max_length=100, blank=True)
    Choose2 = models.CharField(max_length=100, blank=True)
    Choose3 = models.CharField(max_length=100, blank=True)
    Choose4 = models.CharField(max_length=100, blank=True)
    Video = models.CharField(max_length=255, blank=True)


class FourthTable(models.Model):
    TableHeaderBigText = models.CharField(max_length=255, blank=True)
    TableHeaderText = models.TextField(max_length=255, blank=True)
    Circle1 = models.CharField(max_length=100, blank=True)
    Circle2 = models.CharField(max_length=100, blank=True)
    Circle3 = models.CharField(max_length=100, blank=True)
    Circle4 = models.CharField(max_length=100, blank=True)
    Circle5 = models.CharField(max_length=100, blank=True)
    Circle6 = models.CharField(max_length=100, blank=True)


class FifthTable(models.Model):
    TableHeaderBigText = models.CharField(max_length=255, blank=True)
    TableHeaderText = models.TextField(max_length=255, blank=True)
    Column1_Image = models.ImageField(blank=True, upload_to="static/images")
    Column1_Header = models.CharField(max_length=255, blank=True)
    Column1_Text = models.TextField(max_length=255, blank=True)
    Column2_Image = models.ImageField(blank=True, upload_to="static/images")
    Column2_Header = models.CharField(max_length=255, blank=True)
    Column2_Text = models.TextField(max_length=255, blank=True)
    Column3_Image = models.ImageField(blank=True, upload_to="static/images")
    Column3_Header = models.CharField(max_length=255, blank=True)
    Column3_Text = models.TextField(max_length=255, blank=True)


class Contact(models.Model):
    Header = models.CharField(max_length=255, blank=True)
    Text = models.TextField(max_length=255, blank=True)
