import csv
import os

from unesco.models import Category
from unesco.models import Iso
from unesco.models import Region
from unesco.models import Site
from unesco.models import State

CURRENT_DIR = os.path.dirname(__file__)
# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load


def run():
    """Runs the main routine to seed the database."""
    f_hand = open(
        os.path.join(CURRENT_DIR, '..', 'whc-sites-2018-clean.csv'),
        'r', encoding='utf-8'
    )
    reader = csv.reader(f_hand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Process each row
    for row in reader:
        (name, description, justification, year, longitude, latitude,
         area_hectares, category, state, region, iso) = row

        c, _ = Category.objects.get_or_create(name=category)
        s, _ = State.objects.get_or_create(name=state)
        iso, _ = Iso.objects.get_or_create(name=iso)
        r, _ = Region.objects.get_or_create(name=region)
        site = Site(
            name=name, year=year, latitude=latitude, longitude=longitude,
            description=description, justification=justification,
            area_hectares=area_hectares or None,
            category=c, state=s, iso=iso, region=r,
        )
        site.save()
