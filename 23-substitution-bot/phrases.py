# Functions for utilizing phrases
import re
import random

ph_cat_rx = re.compile(r'\[(.+?)\]')

def collect_phrases(phrase_path):
    """Collects each line of the phrasefile in a phrases list"""
    phrasefile = open(phrase_path)
    phrases = phrasefile.readlines()
    phrasefile.close()
    
    for phrase in phrases:
        phrase = phrase.strip()
        
    return phrases

def sub_placeholder(match, sub_dic):
    """Returns a substitute for the phrase"""
    placeholder = match.group(1)
    if placeholder not in sub_dic:
        return "(-ERROR: '{0}' has no defined substitutes-)".format(placeholder)
    else:
        return random.choice(sub_dic[placeholder])

def substitute(phrase, sub_dic):
    """Substitutes all placeholders in the phrase"""
    return ph_cat_rx.sub(lambda match, sub_dic=sub_dic: sub_placeholder(match, sub_dic), phrase)