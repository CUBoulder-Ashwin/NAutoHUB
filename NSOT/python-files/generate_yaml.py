import os
import yaml

def clean_empty(data):
    """Recursively remove empty lists, dictionaries, and None values from the data."""
    if isinstance(data, dict):
        return {k: clean_empty(v) for k, v in data.items() if v not in [None, {}, []]}
    elif isinstance(data, list):
        return [clean_empty(v) for v in data if v not in [None, {}, []]]
    return data

def create_yaml_from_form(device_data, filename="devices_config.yml"):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    yaml_file_path = os.path.join(base_dir, 'templates', filename)
    
    # Clean up device_data by removing empty values
    cleaned_data = clean_empty({'devices': [device_data]})
    
    # Write cleaned data to YAML
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(cleaned_data, yaml_file, default_flow_style=False, sort_keys=False)
    print(f"YAML file saved: {yaml_file_path}")

# Function to build device data with only non-empty fields
def build_device_data(device_id, router_type, interfaces, ospf=None, bgp=None, vlans=None, rip=None, dhcp=None):
    device_data = {
        'hostname': device_id,
        'device_type': router_type,
        'clear_config': 'no'
    }

    # Only add interfaces if there are valid entries
    if interfaces:
        device_data['interfaces'] = [
            {
                'name': iface['type'] + iface['number'],
                'ip_address': iface.get('ip'),
                'subnet_mask': iface.get('mask')
            }
            for iface in interfaces if iface.get('ip') and iface.get('mask')
        ]

    # Add VLANs if there are any valid entries
    if vlans:
        device_data['vlans'] = [{'id': vlan['id'], 'name': vlan['name']} for vlan in vlans if vlan.get('id') and vlan.get('name')]

    # Add OSPF details if present and valid
    if ospf and ospf.get('process_ids') and ospf['process_ids'][0]:  # Check if process_id exists and is non-empty
        device_data['ospf'] = {
            'process_id': ospf['process_ids'][0],
            'networks': [
                {
                    'ip': net['ip'],
                    'wildcard': net['wildcard'],
                    'area': net['area']
                }
                for net in ospf['networks'] if net.get('ip') and net.get('wildcard') and net.get('area')
            ],
            'redistribute': {
                'connected': ospf.get('redistribute_connected', False),
                'bgp': ospf.get('redistribute_bgp', False)
            }
        }

    # Add BGP details if present and valid
    if bgp and bgp.get('asn'):  # Check if as_number exists and is non-empty
        device_data['bgp'] = {
            'as_number': bgp['asn'],
            'address_families': [
                {
                    'type': family['type'],
                    'networks': [{'ip': net['ip']} for net in family.get('networks', []) if net.get('ip')]
                }
                for family in bgp.get('address_families', []) if family.get('type')
            ],
            'neighbors': [
                {'ip': neighbor['ip'], 'remote_as': neighbor['remote_as']}
                for neighbor in bgp['neighbors'] if neighbor.get('ip') and neighbor.get('remote_as')
            ]
        }

    # Add RIP configuration if present and valid
    if rip and rip.get('version') and any(rip.get('networks')):
        device_data['rip'] = {
            'version': rip['version'],
            'networks': [net['ip'] for net in rip['networks'] if net.get('ip')],
            'redistribute': {
                'bgp': rip.get('redistribute', {}).get('bgp', False),
                'metric': rip.get('redistribute', {}).get('metric', 1)
            }
        }

    return device_data


def create_yaml_from_form_data(device_id, router_type, interfaces, ospf=None, bgp=None, vlans=None, rip=None, dhcp=None):
    device_data = build_device_data(device_id, router_type, interfaces, ospf, bgp, vlans, rip, dhcp)
    create_yaml_from_form(device_data)
