"""Renames all files in ./bin directory
to replace all underscores with dashes in the filename
"""
import os
import re

os.chdir('_posts')
print(f'CWD: {os.getcwd()}')
print(os.listdir('.'))
input("Press Enter to continue...")

for filename in os.listdir('.'):
    new_filename = re.sub('_', '-', filename)
    os.rename(filename, new_filename)
    print(f'Renamed {filename} to {new_filename}')

print('Done')
