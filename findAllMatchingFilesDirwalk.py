'''
Function visits every folder in the specified directory and finds all files matching the search
'''

import os
import fnmatch

def getListOfFilePaths(path, search_criteria):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, search_criteria):
            matches.append(os.path.join(root, filename))
    return matches

# path = "/Users/tamirlan/Documents/Personal/iPhoto Library.migratedphotolibrary/Masters"
path = "/Users/tamirlan/Documents/Personal/iPhoto Library.migratedphotolibrary/Previews"
print len(getListOfFilePaths(path, '*.jpg'))