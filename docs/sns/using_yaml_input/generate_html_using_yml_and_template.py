#!/usr/bin/python
import jinja2, yaml
from pathlib import Path


def generate_email_output(template_file_name, var_input_yml):
    # Declare email template file path.
    templateFilePath = jinja2.FileSystemLoader('./templates/')

    # Set Jinja2 environment
    jinja2_env = jinja2.Environment(loader=templateFilePath)

    # Provide Email html template file.
    #email_html_template = template_file_name
    #jinja_template = jinja2_env.get_template("email_html_template.j2")
    jinja_template = jinja2_env.get_template(template_file_name)

    # Provide jinja2 variables input file. Note: It's using yaml file. all
    # key names and will be used in jinja2 template file and values are replaced accordingly.
    #template_input_file = "files/email_input.yml"
    dirname = 'files/'
    # dirname = '/home/reports'
    # filename = 'daily'
    # suffix = '.pdf'
    # Example to join path.
    # Path(dirname, filename).with_suffix(suffix)
    # Or use os.path.join - to join paths.
    template_input_file = Path(dirname, var_input_yml)
    #template_input_file = "files/email_input.yml"

    # Provide email output path. e.g. signup.html
    email_html_output_file = "signup.html"

    with open(template_input_file) as file:
        input_data = yaml.load(file, Loader=yaml.FullLoader)
        output = jinja_template.render(input_data)
        print("Output:", output)
        #print (output)

    with open(email_html_output_file, 'w') as output_file:
        output_file.write(output)
        #outFileH = open('index.html', 'w')
        #outFileH.write(output)
        #outFileH.close()

generate_email_output("email_html_template.j2", "email_input.yml")