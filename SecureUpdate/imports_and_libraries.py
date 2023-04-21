import sys
sys.path.append('../')

from one_time_pad import *
from pseudo_random import *
import re
import json
import nltk
import os
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
NUMBER_OF_WORDS = 16
NUMBER_OF_FILE_BITS = 8
t = 8
d = 4
