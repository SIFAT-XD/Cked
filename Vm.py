import os, sys

os.system('git pull')

try:

    __import__("kudus_61").news()

except Exception as e:

    exit(str(e))
