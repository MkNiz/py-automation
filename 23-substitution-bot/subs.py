# Functions for working with the substitutions
import re

REGX = {
    'line': re.compile(r'(\[.+\])+:(.*)'),
    'category': re.compile(r'\[(.+?)\]')
}

def cat_exists(cat, dic):
    """Returns true if category exists, false if not"""
    if cat in dic:
        return True
    else:
        return False
    
def ensure_cat_exists(cat, dic):
    """Adds a category array to the dictionary if it doesn't exist"""
    if cat not in dic:
        dic[cat] = []
        
def add_entry_to_cat(cat, entry, dic):
    """Adds an entry to the category in the dictionary"""
    ensure_cat_exists(cat, dic)
    dic[cat].append(entry)
    
def build_cat_array(cats):
    """Builds an array of categories enclosed in [] within the passed string"""
    cat_array = []
    results = REGX['category'].findall(cats)
    for category in results:
        cat_array.append(category.strip())
    return cat_array
    
def interpret_line(line, dic):
    """Interprets a line string and adds its contents to the dictionary"""
    valid_line = REGX['line'].search(line)
    if valid_line:
        categories = valid_line.group(1).strip()
        entry = valid_line.group(2).strip()
        cat_array = build_cat_array(categories)
        for category in cat_array:
            add_entry_to_cat(category, entry, dic)
    
def collect_dictionary(subpath):
    """Collects and returns the substitution dictionary by reading substitutions.txt"""
    substitutions = {}
    subfile = open(subpath)
    sublines = subfile.readlines()
    
    for line in sublines:
        interpret_line(line, substitutions)
    
    subfile.close()
    return substitutions
        
    