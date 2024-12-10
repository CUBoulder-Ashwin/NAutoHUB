from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_switchport_default = resolve('switchport_default')
    l_0_interface_defaults = resolve('interface_defaults')
    l_0_interface_profiles = resolve('interface_profiles')
    l_0_dps_interfaces = resolve('dps_interfaces')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_loopback_interfaces = resolve('loopback_interfaces')
    l_0_tunnel_interfaces = resolve('tunnel_interfaces')
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    l_0_vxlan_interface = resolve('vxlan_interface')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (((((((((t_1((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default)) or t_1((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults))) or t_1((undefined(name='interface_profiles') if l_0_interface_profiles is missing else l_0_interface_profiles))) or t_1((undefined(name='dps_interfaces') if l_0_dps_interfaces is missing else l_0_dps_interfaces))) or t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces))) or t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces))) or t_1((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces))) or t_1((undefined(name='tunnel_interfaces') if l_0_tunnel_interfaces is missing else l_0_tunnel_interfaces))) or t_1((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces))) or t_1((undefined(name='vxlan_interface') if l_0_vxlan_interface is missing else l_0_vxlan_interface))):
        pass
        yield '\n## Interfaces\n'
        template = environment.get_template('documentation/switchport-default.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/interface-defaults.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/interface-profiles.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/dps-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ethernet-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/port-channel-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/loopback-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/tunnel-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/vlan-interfaces.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/vxlan-interface.j2', 'documentation/interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '6=27&19=30&21=33&23=36&25=39&27=42&29=45&31=48&33=51&35=54&37=57'