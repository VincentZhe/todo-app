# export the zip file

import shutil

shutil.make_archive("output", "zip", "__pycache__/files")