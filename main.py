#!/usr/bin/python

import os
import sys
import argparse
import logging
import pathlib
from jinja2 import Environment, FileSystemLoader


module = sys.modules['__main__'].__file__
log = logging.getLogger(module)

def parse_command_line(argv):

	formatter_class = argparse.RawDescriptionHelpFormatter

	parser = argparse.ArgumentParser(description=module, formatter_class=formatter_class)
	parser.add_argument('-o', dest="output", default="temp", help="directory for new project")
	parser.add_argument("-v", "--verbose", dest="verbose_count", action="count", default=0, help="increases log verbosity for each occurence.")
	arguments = parser.parse_args(argv[1:])
	log.setLevel(max(3 - arguments.verbose_count, 0) * 10)
	return arguments

def main():
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
											format='%(name)s (%(levelname)s): %(message)s')
	try:
		arguments = parse_command_line(sys.argv)
		THIS_DIR = os.path.dirname(os.path.abspath(__file__))
		J2_ENV = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True, lstrip_blocks=True)

		pathlib.Path(f"./{arguments.output}").mkdir(exist_ok=True) 
		J2_ENV.get_template("Makefile.tpl").stream(project_name=arguments.output).dump(f"./{arguments.output}/Makefile")
		J2_ENV.get_template("template.pcf.tpl").stream(project_name=arguments.output).dump(f"./{arguments.output}/{arguments.output}.pcf")
		J2_ENV.get_template("template.v.tpl").stream(project_name=arguments.output).dump(f"./{arguments.output}/{arguments.output}.v")
		J2_ENV.get_template("template_tb.v.tpl").stream(project_name=arguments.output).dump(f"./{arguments.output}/{arguments.output}_tb.v")

	except KeyboardInterrupt:
		log.error('Program interrupted!')
	finally:
		logging.shutdown()

if __name__ == "__main__":
	sys.exit(main())
