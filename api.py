#!/usr/bin/env python2

# Stdlib imports
import os
import sys

# 3rd party imports
import yaml
import jinja2

# Logic
class Api:
    def __init__(self, fn=None):
        if type(fn) == str and os.path.isfile(fn):
            ext = os.path.basename(fn).split('.')[1]
            if ext == 'json':
                _data = json.loads(open(fn).read())
            elif ext in ('yml', 'yaml'):
                _data = yaml.load(open(fn).read())
        tmpl = jinja2.Template(open('base.py').read())
        ofn = '{0}.py'.format(_data['metadata']['name'])
        print("Generating {0}".format(ofn))
        open(ofn, 'w+').write(tmpl.render(**_data))

# Main entrypoint
def main():
    try: 
        o = Api(sys.argv[1])
    except IndexError:
        print('Usage: {0} <file.(json|yml)>'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

# Main entrypoint redirection
if __name__ == '__main__':
    main()
