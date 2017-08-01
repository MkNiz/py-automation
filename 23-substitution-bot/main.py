import re
import os
import subs
import phrases
import random
from datetime import datetime

# Set random seed
random.seed(datetime.now())

# Store file paths
cwd = os.getcwd()
sub_file_path = os.path.join(cwd, "data", "substitutions.txt")
phrase_file_path = os.path.join(cwd, "data", "phrases.txt")

# Gleam data from files
sub_dic = subs.collect_dictionary(sub_file_path)
phrase_list = phrases.collect_phrases(phrase_file_path)

# Select a random phrase
phrase = random.choice(phrase_list)

# Process the phrase for substitution
completed_phrase = phrases.substitute(phrase, sub_dic)
print(completed_phrase)

