import os
import sys

import django
from faker import Faker
import random
from django.db import models

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings')

django.setup()

from blogapp.models import article, author, category, comment
from django.contrib.auth.models import User


fake = Faker()

categories = ['Internet', 'IT', 'Sports', 'Security', 'Technology', 'Apps', 'IOT', 'other']

choice = ['Article', 'Audio', 'Video']

keywords = ['IT', 'IOT', 'Good', 'Bad']

content = '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. ' \
          'Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet ' \
          'quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et ' \
          'sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, ' \
          'wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus ' \
          'enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus ' \
          'faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, ' \
          'tincidunt quis, accumsan porttitor, facilisis luctus, metus</p> '

photos = [
    '/slide-img-1.jpg',
    '/slide-img-2.jpg',
    '/slide-img-3.jpg',
    '/slide-img-4.jpg',
    '/slide-img-5.jpg',
    '/slide-img-6.jpg',
    '/slide-img-7.jpg',
    '/slide-img-8.jpg',
]



video_url = [
    'https://www.youtube.com/embed/N1-Jmq7BLFE',
    'https://www.youtube.com/embed/OFDAGiPJHL8?showinfo=0',
    'https://www.youtube.com/embed/rDZ1AjDJjFI?rel=0&amp;showinfo=0',
]

def create_category(_range):
    for x in range(_range):
         r = category.objects.create(
            name = random.choice(categories)
        )
       
def create_article_post(_range):
    for x in range(_range):
        r = article.objects.get_or_create(
            article_author=author.objects.all()[0],
            title=fake.word(ext_word_list=None),
            body=content,
            category = random.choice(category.objects.all()),
            image=random.choice(photos),
            posted_on=fake.date_this_century(before_today=True, after_today=False),
            updated_on=fake.date_this_century(before_today=True, after_today=False)
           
        )[0]
        r.save()
    

def create_author(_range):
    for x in range(_range):
        r = author.objects.create(
            name=random.choice(User.objects.all()),
            profile_picture=random.choice(photos),
            details = fake.text()
        )
    
def crate_comment(_range):
    for x in range(_range):
        r = comment.objects.create(
            email=fake.email(),
            name = fake.name(),
            post_comment=fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
            post=random.choice(article.objects.all())
        )



def populate():
    
    category.objects.all().delete()
    create_category(10)
    create_article_post(50)
    crate_comment(1000)
    
    
   


if __name__ == '__main__':
    print('Populating script')
    populate()
    print('Populating complete')
