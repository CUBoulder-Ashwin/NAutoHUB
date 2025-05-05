import os
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "golden_configs"))
TEMPLATE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "templates"))


def generate_day0_config(device_name, mgmt_ip, username, password):
    print(f"The management ip is {mgmt_ip}")
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("day0_config.j2")
    rendered = template.render(
        device_name=device_name, mgmt_ip=mgmt_ip, username=username, password=password
    )

    os.makedirs(CONFIG_DIR, exist_ok=True)
    config_path = os.path.join(CONFIG_DIR, f"goldenconfigs_{device_name}.cfg")
    with open(config_path, "w") as f:
        f.write(rendered)
    return config_path
