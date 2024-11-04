def update_topology(topo_path, device_name, device_type, device_interface, connected_device, connected_interface):
    try:
        # Read the existing file content
        with open(topo_path, 'r') as file:
            lines = file.readlines()

        # Prepare the new node and link entries
        new_node_entry = f"    {device_name}:\n      kind: {'ceos' if device_type in ['router', 'switch'] else 'linux'}\n"
        new_node_entry += f"      image: {'ceos:4.32.2F' if device_type in ['router', 'switch'] else 'ubu_hosts:latest'}\n"
        
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
    except Exception as e:
        print(f"Error updating topology: {e}")

# Example usage
# update_topology_text('/path/to/topo.yml', 'R6', 'router', 'eth0', 'R4', 'eth4')
