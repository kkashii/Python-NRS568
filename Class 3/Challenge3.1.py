# Tree Directory

import os

# I am creating a temporary directory to store these files and calling it "root_path"
root_path = "E:\Python_Challenge3"
os.mkdir(root_path)

# Identifying the first branch of folder in a list
branch_one = ["draft_code", "includes", "layouts", "sites"]

# Creating first set of folder by looping them through the root path
for folder in branch_one:
    os.mkdir(os.path.join(root_path, folder))

# Identifying second branch of folders in a list
branch_two = ["pending", "complete"]

# Looping second branch into draft_code folder
for folder in branch_two:
    os.mkdir(os.path.join(root_path, "draft_code", folder))

# Identifying third branch
branch_three = ["default", "post"]

# Looping third branch into layouts folder
for folder in branch_three:
    os.mkdir(os.path.join(root_path, "layouts", folder))

# Easier to add last folder manually instead of making a list loop
os.mkdir(os.path.join(root_path, "layouts", "post", "posted"))

# Shutil will delete a whole directory tree instead of individual folders
# os.rmdir will not work as the directory is not empty
import shutil

shutil.rmtree(root_path)
