#!/usr/bin/env python
import os,sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PPPPP.settings")

from PPPPP.models import Sponsor,Prize,Api

def populate(argv):
  if len(argv) != 4:
    print 'Usage: ./populate.py <data_dir> <api_list> <prizes>'
    return

  api_file = open(argv[1] + argv[2])
  populate_apis(api_file)
  prizes_file = open(argv[1] + argv[3])
  populate_prizes(prizes_file)


def populate_apis(api_file):
  for line in api_file:
    entry = line.split(',')
    sponsorName = entry[0].strip()
    url = entry[1].strip()

    try:
      sponsor = Sponsor.objects.get(name=sponsorName)
    except:
      sponsor = Sponsor(name=sponsorName)
      sponsor.save()
    
    api = Api(sponsor=sponsor, url=url)
    api.save()

  api_file.close()


def populate_prizes(prizes_file):
  for line in prizes_file:
    entry = line.split(',', 2)
    sponsorName = entry[0].strip()
    title = entry[1].strip()
    description = entry[2].strip()
    
    try:
      sponsor = Sponsor.objects.get(name=sponsorName)
    except:
      sponsor = Sponsor(name=sponsorName)
      sponsor.save()
    
    prize = Prize(sponsor=sponsor, title=title, description=description)
    prize.save()

  prizes_file.close()


populate(sys.argv)
