from django.contrib import admin
from .models import FirstTable, SecondTable, ThirdTable, FourthTable, FifthTable, Contact


class AdminFirstTable(admin.ModelAdmin):        # Admin view for First Table

    search_fields = ('TableHeaderBigText',      # Search fields for First Table
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'SecondRowHeader',
                    'SecondRowText',
                    'ThirdRowHeader',
                    'ThirdRowText',
                    'FourthRowHeader',
                    'FourthRowText',
                    'TableImage')

    list_display = ('TableHeaderBigText',       # Display fields for First Table
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'SecondRowHeader',
                    'SecondRowText',
                    'ThirdRowHeader',
                    'ThirdRowText',
                    'FourthRowHeader',
                    'FourthRowText',
                    'TableImage')

admin.site.register(FirstTable, AdminFirstTable)    # Add First Table form to admin site

"""
All other Tables are the same as First table.

"""

class AdminSecondTable(admin.ModelAdmin):

    search_fields = ('TableHeaderBigText',
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'SecondRowHeader',
                    'SecondRowText',
                    'ThirdRowHeader',
                    'ThirdRowText',
                    'FourthRowHeader',
                    'FourthRowText',
                    'FifthRowHeader',
                    'FifthRowText',
                    'SixthRowHeader',
                    'SixtRowText')

    list_display = ('TableHeaderBigText',
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'SecondRowHeader',
                    'SecondRowText',
                    'ThirdRowHeader',
                    'ThirdRowText',
                    'FourthRowHeader',
                    'FourthRowText',
                    'FifthRowHeader',
                    'FifthRowText',
                    'SixthRowHeader',
                    'SixtRowText')

admin.site.register(SecondTable, AdminSecondTable)


class AdminThirdTable(admin.ModelAdmin):

    search_fields = ('TableHeaderBigText',
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'FirstRowText2',
                    'Choose1',
                    'Choose2',
                    'Choose3',
                    'Choose4',
                    'Video'
                    )

    list_display = ('TableHeaderBigText',
                    'TableHeaderText',
                    'FirstRowHeader',
                    'FirstRowText',
                    'FirstRowText2',
                    'Choose1',
                    'Choose2',
                    'Choose3',
                    'Choose4',
                    'Video'
                    )

admin.site.register(ThirdTable, AdminThirdTable)

class AdminFourthTable(admin.ModelAdmin):

    search_fields = ('TableHeaderBigText',
                    'TableHeaderText',
                    'Circle1',
                    'Circle2',
                    'Circle3',
                    'Circle4',
                    'Circle5',
                    'Circle6',
                     )

    list_display = ('TableHeaderBigText',
                    'TableHeaderText',
                    'Circle1',
                    'Circle2',
                    'Circle3',
                    'Circle4',
                    'Circle5',
                    'Circle6',
                    )

admin.site.register(FourthTable, AdminFourthTable)



class AdminFifthTable(admin.ModelAdmin):

    search_fields = ('TableHeaderBigText',
                    'TableHeaderText',
                    'Column1_Image',
                    'Column1_Header',
                    'Column1_Text',
                    'Column2_Image',
                    'Column2_Header',
                    'Column2_Text',
                    'Column3_Image',
                    'Column3_Header',
                    'Column3_Text',
                     )

    list_display = ('TableHeaderBigText',
                    'TableHeaderText',
                    'Column1_Image',
                    'Column1_Header',
                    'Column1_Text',
                    'Column2_Image',
                    'Column2_Header',
                    'Column2_Text',
                    'Column3_Image',
                    'Column3_Header',
                    'Column3_Text',
                    )

admin.site.register(FifthTable, AdminFifthTable)



class AdminContactTable(admin.ModelAdmin):

    search_fields = ('Header', 'Text')

    list_display = ('Header', 'Text')

admin.site.register(Contact, AdminContactTable)