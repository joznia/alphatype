import os

print("compiling alphatype to bytecode...")
os.system("python -m py_compile alphatype.py")

os.system("git tag -l")
tagver = input("choose a tag to package: ")
print("renaming compiled file...")
os.chdir("__pycache__")
try:
    os.rename("alphatype.cpython-39.pyc", "../dist/alphatype_%s.pyc" % tagver)
except:
    os.replace("alphatype.cpython-39.pyc", "../dist/alphatype_%s.pyc" % tagver)