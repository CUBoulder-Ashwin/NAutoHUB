from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/multicast.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    l_0_ip_igmp_snooping = resolve('ip_igmp_snooping')
    l_0_router_multicast = resolve('router_multicast')
    l_0_router_pim_sparse_mode = resolve('router_pim_sparse_mode')
    l_0_router_msdp = resolve('router_msdp')
    l_0_router_igmp = resolve('router_igmp')
    l_0_pim_interfaces = missing
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_pim_interfaces = []
    context.vars['pim_interfaces'] = l_0_pim_interfaces
    context.exported_vars.add('pim_interfaces')
    for l_1_ethernet_interface in t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
            pass
            context.call(environment.getattr((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    for l_1_port_channel_interface in t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
            pass
            context.call(environment.getattr((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces), 'append'), l_1_port_channel_interface, _loop_vars=_loop_vars)
    l_1_port_channel_interface = missing
    for l_1_vlan_interface in t_1((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
            pass
            context.call(environment.getattr((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces), 'append'), l_1_vlan_interface, _loop_vars=_loop_vars)
    l_1_vlan_interface = missing
    if (((((t_3((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping)) or t_3((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast))) or t_3((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode))) or (t_2((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces)) > 0)) or t_3((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp))) or t_3((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp))):
        pass
        yield '\n## Multicast\n'
        template = environment.get_template('documentation/ip-igmp-snooping.j2', 'documentation/multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'pim_interfaces': l_0_pim_interfaces})):
            yield event
        template = environment.get_template('documentation/router-multicast.j2', 'documentation/multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'pim_interfaces': l_0_pim_interfaces})):
            yield event
        template = environment.get_template('documentation/pim-sparse-mode.j2', 'documentation/multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'pim_interfaces': l_0_pim_interfaces})):
            yield event
        template = environment.get_template('documentation/router-msdp.j2', 'documentation/multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'pim_interfaces': l_0_pim_interfaces})):
            yield event
        template = environment.get_template('documentation/router-igmp.j2', 'documentation/multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'pim_interfaces': l_0_pim_interfaces})):
            yield event

blocks = {}
debug_info = '6=38&7=41&8=44&9=46&12=48&13=51&14=53&17=55&18=58&19=60&22=62&31=65&33=68&35=71&37=74&39=77'