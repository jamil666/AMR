from .models import FirstTable, SecondTable, ThirdTable, FourthTable, FifthTable, Contact
from django.shortcuts import render


# Create your views here.


def MainPage(request):

    FirstTableForm = FirstTable.objects.get(id=1)
    SecondTableForm = SecondTable.objects.get(id=1)
    ThirdTableForm = ThirdTable.objects.get(id=1)
    FourthTableForm = FourthTable.objects.get(id=1)
    FifthTableForm = FifthTable.objects.get(id=1)
    ContactForm = Contact.objects.get(id=2)

    context = {"FirstTableForm": FirstTableForm,
               "SecondTableForm": SecondTableForm,
               "ThirdTableForm": ThirdTableForm,
               "FourthTableForm": FourthTableForm,
               "FifthTableForm": FifthTableForm,
               "ContactForm": ContactForm
               }
    return render(request, 'index.html', context)