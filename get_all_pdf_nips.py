#!/usr/bin/env python

"""
Download all the pdfs linked on a given webpage
Usage -
    python grab_pdfs.py url <path/to/directory>
        url is required
        path is optional. Path needs to be absolute
        will save in the current directory if no path is given
        will save in the current directory if given path does not exist
Requires - requests >= 1.0.4
           beautifulsoup >= 4.0.0
Download and install using
    
    pip install requests
    pip install beautifulsoup4
"""


from requests import get
from urllib.parse import urljoin
from os import path, getcwd
from bs4 import BeautifulSoup as soup


"""
Author: Avijit Dasgupta

This script downloads all the pdf files of the accepted papers from "https://papers.nips.cc".

To run this code: python get_all_pdf_nips.py year where you need to specify the year (e.g.- 2011, 2012 etc.)

"""


from sys import argv
import pdb
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import numpy as np
import pdb
import os
import sys
from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models
import gensim
from stop_words import get_stop_words
import logging
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string



year = str(sys.argv[1])
#year = str(2015)
base_dir = "NIPS" + year
if not os.path.exists(base_dir):
    os.makedirs(base_dir)
base_url = "https://papers.nips.cc"
url= 'https://papers.nips.cc/book/advances-in-neural-information-processing-systems-29-'+year
logging.info("Connecting to URL: %s" % url)
page = urllib.request.urlopen(url)

soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
lists = soup.find_all('li') # Title and paper url
#print(len(lists))
lists = lists[1:]
n_pdfs = 0
for paper_link in lists:
    
    print(paper_link.find_all('a')[0]['href'])
    n_pdfs+= 1
    content= get(urljoin(base_url, paper_link.find_all('a')[0]['href']+ '.pdf'))

    with open(path.join(base_dir, paper_link.find_all('a')[0]['href'][7:]+'.pdf'), 'wb') as pdf: #remove /paper/
        pdf.write(content.content)


pdb.set_trace()