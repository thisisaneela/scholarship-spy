from django.core.management.base import BaseCommand
import pandas as pd
from app1.models import Scholarship
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df=pd.read_csv('20k_data.csv')
        for TITLE,LINKS,IMAGELINK,TUITIONSTRUCTURE,UNIVERSITYNAME,COUNTRY,ELIGIBILITY,SUBJECT,DEGREE,APPLYDATE,DESCRIPTION in zip(df.Title,df.Link,df.ImageLink,df.TutionStructure,df.UniversityName,df.Country,df.eligiblity,df.subject,df.Degree,df.apply_date,df.scholarship_details):
            models=Scholarship(title=TITLE,link=LINKS,image_link=IMAGELINK,tution_structure=TUITIONSTRUCTURE, university_name=UNIVERSITYNAME, country=COUNTRY,eligibility=ELIGIBILITY,subject=SUBJECT, degree=DEGREE,apply_date=APPLYDATE,scholarship_details=DESCRIPTION)
            models.save()