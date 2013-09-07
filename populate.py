from PPPPP.models import Sponsor, Prize, Api

def populate(data_directory, api_filename, prizes_filename):
  api_file = open(data_directory + api_filename)
  prizes_file = open(data_directory + prizes_filename)
  populate_apis(api_file)
  populate_prizes(prizes_file)

def populate_apis(api_file):
  print api_file
  api_file.close()

def populate_prizes(prizes_file):
  print prizes_file
  prizes_file.close()
