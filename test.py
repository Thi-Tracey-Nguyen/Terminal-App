import json
import gzip
 
with gzip.open('/Users/tramnguyenbichtram/Documents/Programming/Projects/term1/python/T1A3/.venv/lib/python3.10/site-packages/spellchecker/resources/en.json.gz', "rb") as f:
    d = json.loads(f.read().decode("ascii"))

print(d)

  import  jpype     
  import  asposecells     
  jpype.startJVM() 
  from asposecells.api import Workbook
  workbook = Workbook("input.json")
  workbook.Save("Output.txt")
  jpype.shutdownJVM()