import sys, os

# “__file__” is …/progs/main.py, so os.path.dirname(__file__) == “…/progs”
# We need to go up one directory, then into “Modules”
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
modules_dir = os.path.join(parent_dir, 'Packages')

# Now modules_dir == “…/Modules”
sys.path.append(modules_dir)

import module   # Python can now find Modules/module.py
