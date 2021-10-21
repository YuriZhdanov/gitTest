import git
import datetime
import os
from time import *
from os import path
from git import Repo


curr_dir = os.path.dirname(os.path.realpath(__file__))
repo = Repo(curr_dir)

origin = repo.remote()
print(origin)
repo.create_head('my_new_branch')
# origin.push('my_new_branch')