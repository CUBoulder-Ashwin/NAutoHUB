from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'fabric_documentation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_fabric_name = resolve('fabric_name')
    l_0_fabric_switches = resolve('fabric_switches')
    l_0_topology_links = resolve('topology_links')
    l_0_uplink_ipv4_pools = resolve('uplink_ipv4_pools')
    l_0_loopback_ipv4_pools = resolve('loopback_ipv4_pools')
    l_0_has_isis = resolve('has_isis')
    l_0_vtep_loopback_ipv4_pools = resolve('vtep_loopback_ipv4_pools')
    try:
        t_1 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    pass
    yield '# '
    yield str((undefined(name='fabric_name') if l_0_fabric_name is missing else l_0_fabric_name))
    yield '\n\n## Table of Contents\n\n<!-- toc -->\n<!-- toc -->\n\n## Fabric Switches and Management IP\n\n| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |\n| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |\n'
    for l_1_fabric_switch in (undefined(name='fabric_switches') if l_0_fabric_switches is missing else l_0_fabric_switches):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_fabric_switch, 'pod'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'type'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'mgmt_ip'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'platform'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'provisioned'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'serial_number'))
        yield ' |\n'
    l_1_fabric_switch = missing
    yield '\n> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.\n\n### Fabric Switches with inband Management IP\n\n| POD | Type | Node | Management IP | Inband Interface |\n| --- | ---- | ---- | ------------- | ---------------- |\n'
    for l_1_fabric_switch in t_1(context, (undefined(name='fabric_switches') if l_0_fabric_switches is missing else l_0_fabric_switches), 'inband_mgmt_ip', 'arista.avd.defined'):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_fabric_switch, 'pod'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'type'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'inband_mgmt_ip'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'inband_mgmt_interface'))
        yield ' |\n'
    l_1_fabric_switch = missing
    yield '\n## Fabric Topology\n\n| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |\n| ---- | ---- | -------------- | --------- | ----------| -------------- |\n'
    for l_1_topology_link in (undefined(name='topology_links') if l_0_topology_links is missing else l_0_topology_links):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_topology_link, 'type'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'node_interface'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer_type'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer_interface'))
        yield ' |\n'
    l_1_topology_link = missing
    yield '\n## Fabric IP Allocation\n\n### Fabric Point-To-Point Links\n\n| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |\n| ---------------- | ------------------- | ------------------ | ------------------ |\n'
    for l_1_uplink_ipv4_pool in (undefined(name='uplink_ipv4_pools') if l_0_uplink_ipv4_pools is missing else l_0_uplink_ipv4_pools):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_uplink_ipv4_pool, 'pool'))
        yield ' | '
        yield str(environment.getattr(l_1_uplink_ipv4_pool, 'size'))
        yield ' | '
        yield str(environment.getattr(l_1_uplink_ipv4_pool, 'used'))
        yield ' | '
        yield str(environment.getattr(l_1_uplink_ipv4_pool, 'used_percent'))
        yield ' % |\n'
    l_1_uplink_ipv4_pool = missing
    yield '\n### Point-To-Point Links Node Allocation\n\n| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |\n| ---- | -------------- | --------------- | --------- | -------------- | --------------- |\n'
    for l_1_topology_link in t_1(context, (undefined(name='topology_links') if l_0_topology_links is missing else l_0_topology_links), 'node_ip_address', 'arista.avd.defined'):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_topology_link, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'node_interface'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'node_ip_address'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer_interface'))
        yield ' | '
        yield str(environment.getattr(l_1_topology_link, 'peer_ip_address'))
        yield ' |\n'
    l_1_topology_link = missing
    yield '\n### Loopback Interfaces (BGP EVPN Peering)\n\n| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |\n| ------------- | ------------------- | ------------------ | ------------------ |\n'
    for l_1_loopback_ipv4_pool in (undefined(name='loopback_ipv4_pools') if l_0_loopback_ipv4_pools is missing else l_0_loopback_ipv4_pools):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_loopback_ipv4_pool, 'pool'))
        yield ' | '
        yield str(environment.getattr(l_1_loopback_ipv4_pool, 'size'))
        yield ' | '
        yield str(environment.getattr(l_1_loopback_ipv4_pool, 'used'))
        yield ' | '
        yield str(environment.getattr(l_1_loopback_ipv4_pool, 'used_percent'))
        yield ' % |\n'
    l_1_loopback_ipv4_pool = missing
    yield '\n### Loopback0 Interfaces Node Allocation\n\n| POD | Node | Loopback0 |\n| --- | ---- | --------- |\n'
    for l_1_fabric_switch in t_1(context, (undefined(name='fabric_switches') if l_0_fabric_switches is missing else l_0_fabric_switches), 'loopback0_ip_address', 'arista.avd.defined'):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_fabric_switch, 'pod'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'loopback0_ip_address'))
        yield ' |\n'
    l_1_fabric_switch = missing
    if (undefined(name='has_isis') if l_0_has_isis is missing else l_0_has_isis):
        pass
        yield '\n### ISIS CLNS interfaces\n\n| POD | Node | CLNS Address |\n| --- | ---- | ------------ |\n'
        for l_1_fabric_switch in t_1(context, (undefined(name='fabric_switches') if l_0_fabric_switches is missing else l_0_fabric_switches), 'router_isis_net', 'arista.avd.defined'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_fabric_switch, 'pod'))
            yield ' | '
            yield str(environment.getattr(l_1_fabric_switch, 'node'))
            yield ' | '
            yield str(environment.getattr(l_1_fabric_switch, 'router_isis_net'))
            yield ' |\n'
        l_1_fabric_switch = missing
    yield '\n### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)\n\n| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |\n| ------------------ | ------------------- | ------------------ | ------------------ |\n'
    for l_1_vtep_loopback_ipv4_pool in (undefined(name='vtep_loopback_ipv4_pools') if l_0_vtep_loopback_ipv4_pools is missing else l_0_vtep_loopback_ipv4_pools):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_vtep_loopback_ipv4_pool, 'pool'))
        yield ' | '
        yield str(environment.getattr(l_1_vtep_loopback_ipv4_pool, 'size'))
        yield ' | '
        yield str(environment.getattr(l_1_vtep_loopback_ipv4_pool, 'used'))
        yield ' | '
        yield str(environment.getattr(l_1_vtep_loopback_ipv4_pool, 'used_percent'))
        yield ' % |\n'
    l_1_vtep_loopback_ipv4_pool = missing
    yield '\n### VTEP Loopback Node allocation\n\n| POD | Node | Loopback1 |\n| --- | ---- | --------- |\n'
    for l_1_fabric_switch in t_1(context, (undefined(name='fabric_switches') if l_0_fabric_switches is missing else l_0_fabric_switches), 'vtep_loopback_ip_address', 'arista.avd.defined'):
        _loop_vars = {}
        pass
        yield '| '
        yield str(environment.getattr(l_1_fabric_switch, 'pod'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'node'))
        yield ' | '
        yield str(environment.getattr(l_1_fabric_switch, 'vtep_loopback_ip_address'))
        yield ' |\n'
    l_1_fabric_switch = missing

blocks = {}
debug_info = '6=25&17=27&18=31&27=47&28=51&35=63&36=67&45=81&46=85&53=95&54=99&61=113&62=117&69=127&70=131&72=138&78=141&79=145&87=153&88=157&95=167&96=171'