import os
from jinja2 import Environment, FileSystemLoader


def generate_show_command(predicted_show_type, monitor=None):
    # Get the current directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up two levels to reach 'NSOT/' and then into 'templates/'
    templates_dir = os.path.join(current_dir, "..", "..", "templates")
    templates_dir = os.path.abspath(templates_dir)  # get absolute path

    # Setup Jinja2 environment pointing to templates directory
    env = Environment(loader=FileSystemLoader(templates_dir))

    # Load the show_template.j2
    template = env.get_template("show_template.j2")

    # Template expects these variables
    template_vars = {
        "show_type": predicted_show_type,
        "interface": monitor,
        "ip_address": None,
        "vlan_id": None,
        "subinterface": None,
    }

    # Render the command
    final_command = template.render(template_vars)

    return final_command.strip()
