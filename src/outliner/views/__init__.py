from pathlib import Path
from .script_obj import Script_Obj
from .running_obj import Running_Obj

sc = Script_Obj(Path("/mnt/d/projects/scripts/tests-outliner/test_imports.py"))
ab = Running_Obj(sc, "test()")
breakpoint()
