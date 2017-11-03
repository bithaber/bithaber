import feedparser
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from drum.links.models import Link


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        rss_urls = [
            {'url': 'https://www.google.com/alerts/feeds/04507271206462498045/4979610609707863101',
             'keywords': 'tr,blockchain'},
            {'url': 'https://www.google.com/alerts/feeds/04507271206462498045/13551361505744903169',
             'keywords': 'tr,bitcoin'},
            {'url': 'https://www.google.com/alerts/feeds/04507271206462498045/7226671419079300037',
             'keywords': 'en,blockchain'},
            {'url': 'https://www.google.com/alerts/feeds/04507271206462498045/7924818352809437602',
             'keywords': 'en,bitcoin'},

        ]

        from mezzanine.generic.models import Keyword, AssignedKeyword
        link_ct = ContentType.objects.get_for_model(Link)

        user = User.objects.get(pk=1)
        for url in rss_urls:
            data = feedparser.parse(url.get('url'))

            for entry in data.get('entries'):
                obj, created = Link.objects.get_or_create(
                    link=entry.get('link').split('url=')[1].split('&ct=ga')[0],
                    title=BeautifulSoup(entry.get('title')).text,
                    publish_date=entry.get('published'),
                    user=user)

                keywords = url.get('keywords').split(',')
                for keyword_item in keywords:
                    keyword_obj, created = Keyword.objects.get_or_create(title=keyword_item, slug=keyword_item)
                    obj2, created2 = AssignedKeyword.objects.get_or_create(content_type=link_ct, keyword=keyword_obj,
                                                                           object_pk=obj.id)
