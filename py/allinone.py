import os
import gettasks
gettasks.run()
os.system('python py/transform.py')
os.system('python py/readjson.py')
os.system('python py/mergejson.py')
