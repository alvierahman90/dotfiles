from os.path import expanduser
from os.path import isfile
from os import environ
from os import getcwd
from os import system
from jinja2 import Template


def create(filename, force_template=False):
    if isfile(filename):
        while True:
            overwrite = input(f"{filename} already exists. Overwrite? (y/n) ")
            if overwrite.lower() in ['n', 'no', 'ur mum gay']:
                return 0
            elif overwrite.lower() in ['y', 'yes', 'yeet']:
                break

    if not force_template:
        template_name = filename.split(".")[-1]
    else:
        template_name = force_template

    with open(expanduser("~/.templates/") + template_name) as file:
        template = Template(file.read())

    with open(filename, 'w+') as file:
        file.write(template.render(directory=getcwd()))

    system(f"chmod +x {filename}")

def open_file_in_editor(filename):
    system(f"{environ['EDITOR']} {filename}")
