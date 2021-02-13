import os

distdirex = os.path.isdir("./dist")
if distdirex == False:
    os.mkdir("./dist")

print("compiling alphatype to bytecode...")
os.system("python -m py_compile alphatype.py")

tagver = input("create a new tag (e.g. v1.2.9): ")
tagmsg = input("tag message: ")
os.system('''git tag -a %s -m "%s" ''' % (tagver, tagmsg))

print("renaming compiled file...")
os.chdir("__pycache__")
try:
    os.rename("alphatype.cpython-39.pyc", "../dist/alphatype_%s.pyc" % tagver)
except:
    os.replace("alphatype.cpython-39.pyc", "../dist/alphatype_%s.pyc" % tagver)

print("pushing tags...")
os.system("git push --tags")