import importlib
from pathlib import Path
from views import Script_Obj, Running_Obj
from modules import Trace,Display


sc = Script_Obj(Path("/mnt/d/projects/scripts/outliner/tests-outliner/test_imports.py"))

ab = Running_Obj(sc, "test()")

breakpoint()

tra = Trace().trace_obj(ab)



disp = Display(tra.detailed_data,tra.functions_flow)