import os, glob, importlib
files = glob.glob(os.path.dirname(os.path.abspath(__file__)) + os.sep + "*.py")
for f in files:
    f = os.path.basename(f)
    if f != __file__:
        print('- '*5 + f)
        importlib.import_module(f[:-3])
