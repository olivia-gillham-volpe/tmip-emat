#

__version__ = '0.2.9'


import logging

def require_version(required_version, pkg):
	if required_version.split('.') > pkg.__version__.split('.'):
		raise ValueError(f"this {pkg.__name__} is version {pkg.__version__}")
	if 'CS' in required_version and 'CS' not in pkg.__version__:
		raise ValueError(f"this {pkg.__name__} is version {pkg.__version__}, a 'CS' patched version is required\n"
						 "try using: conda update ema_workbench -c tmip")

import ema_workbench
require_version('2.1.507', ema_workbench)

_currently_captured = (logging._warnings_showwarning is not None)
logging.captureWarnings(True)

try:

	from ._pkg_constants import *
	from .configuration import config
	from .scope.scope import Scope
	from .scope.scope import Measure
	from .scope.parameter import Constant, Parameter, make_parameter
	from .scope.box import Box, Boxes, ChainedBox, Bounds
	from .database.sqlite.sqlite_db import SQLiteDB
	from .model.core_python import PythonCoreModel
	from .model.meta_model import MetaModel, create_metamodel
	from .optimization.optimization_result import OptimizationResult
	from .exceptions import *
	from .versions import versions

	try:
		from .model.core_excel import ExcelCoreModel
	except (ModuleNotFoundError, ImportError):
		ExcelCoreModel = None

	from ema_workbench import Constraint

finally:
	logging.captureWarnings(_currently_captured)

def package_file(*args):
	"""Return the filename of a file within this package."""
	import os
	return os.path.join(
		os.path.dirname(__file__),
		*args
	)


def find_file(*args):
	"""Return the unique filename of a file within this package."""
	import os, glob
	pth = os.path.normpath( package_file("**",*args) )
	candidates = glob.glob(pth, recursive=True)
	if len(candidates) == 1:
		return candidates[0]
	elif len(candidates) > 1:
		raise FileNotFoundError("more than one match")
	else:
		raise FileNotFoundError("no match")

