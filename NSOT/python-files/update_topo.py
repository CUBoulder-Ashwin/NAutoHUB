import os

def update_topology(topo_path, device_name, device_type, device_interface, connected_device, connected_interface, mac_address):
    try:
        # Read the existing file content
        with open(topo_path, 'r') as file:
            lines = file.readlines()

        # Prepare the new node entry
        if device_type in ['router', 'switch']:
            new_node_entry = (
                f"    {device_name}:\n"
                f"      kind: ceos\n"
                f"      image: ceos:4.32.2F\n"
                f"      startup-config: /home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/configs/{device_name}.cfg\n"
                f"      exec:\n"
                f"        - sudo dhclient {device_interface}\n"
            )
        else:
            new_node_entry = (
                f"    {device_name}:\n"
                f"      kind: linux\n"
                f"      image: ubu_hosts:latest\n"
            )

        # Prepare the new link entry
        new_link_entry = f'    - endpoints: ["{device_name}:{device_interface}", "{connected_device}:{connected_interface}"]\n'

        # Insert the new node if not present
        if f"    {device_name}:\n" not in lines:
            nodes_index = lines.index("  nodes:\n") + 1
            while lines[nodes_index].startswith("    "):
                nodes_index += 1
            lines.insert(nodes_index, new_node_entry)

        # Insert the new link at the end of the links section
        if new_link_entry not in lines:
            links_index = lines.index("  links:\n") + 1
            while lines[links_index].startswith("  -"):
                links_index += 1
            lines.insert(links_index, new_link_entry)

        # Write back the updated content
        with open(topo_path, 'w') as file:
            file.writelines(lines)

        print(f"Updated topology with {device_name}, link added.")

        # Create the base config file
        create_base_config(device_name, device_interface, mac_address)
        
    except Exception as e:
        print(f"Error updating topology: {e}")

def create_base_config(device_name, device_interface, mac_address):
    try:
        config_dir = '/home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/configs'
        os.makedirs(config_dir, exist_ok=True)
        config_path = os.path.join(config_dir, f'{device_name}.cfg')

        config_content = (
            f"hostname {device_name}\n"
            "!\n"
            "username admin privilege 15 role network-admin secret 0 admin\n"
            "!\n"
            f"interface {device_interface}\n"
            f"   mac-address {mac_address}\n"
            "    ip address dhcp"
        )

        with open(config_path, 'w') as config_file:
            config_file.write(config_content)

        print(f"Base config for {device_name} created at {config_path}.")
    except Exception as e:
        print(f"Error creating base config for {device_name}: {e}")
