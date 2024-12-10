from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/bfd.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_namespace = resolve('namespace')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    l_0_router_bfd = resolve('router_bfd')
    l_0_ethernet_interface_bfd = l_0_port_channel_interface_bfd = l_0_vlan_interface_bfd = l_0_loopback_interface_bfd = missing
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_ethernet_interface_bfd = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), configured=False)
    context.vars['ethernet_interface_bfd'] = l_0_ethernet_interface_bfd
    context.exported_vars.add('ethernet_interface_bfd')
    l_0_port_channel_interface_bfd = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), configured=False)
    context.vars['port_channel_interface_bfd'] = l_0_port_channel_interface_bfd
    context.exported_vars.add('port_channel_interface_bfd')
    l_0_vlan_interface_bfd = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), configured=False)
    context.vars['vlan_interface_bfd'] = l_0_vlan_interface_bfd
    context.exported_vars.add('vlan_interface_bfd')
    l_0_loopback_interface_bfd = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), configured=False)
    context.vars['loopback_interface_bfd'] = l_0_loopback_interface_bfd
    context.exported_vars.add('loopback_interface_bfd')
    for l_1_ethernet_interface in t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if ((t_2(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval')) and t_2(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))) and t_2(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))):
            pass
            if not isinstance(l_0_ethernet_interface_bfd, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_ethernet_interface_bfd['configured'] = True
    l_1_ethernet_interface = missing
    for l_1_port_channel_interface in t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
        _loop_vars = {}
        pass
        if ((t_2(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'interval')) and t_2(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'min_rx'))) and t_2(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'multiplier'))):
            pass
            if not isinstance(l_0_port_channel_interface_bfd, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_port_channel_interface_bfd['configured'] = True
    l_1_port_channel_interface = missing
    for l_1_vlan_interface in t_1((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
        _loop_vars = {}
        pass
        if ((t_2(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'interval')) and t_2(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'min_rx'))) and t_2(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'multiplier'))):
            pass
            if not isinstance(l_0_vlan_interface_bfd, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_vlan_interface_bfd['configured'] = True
    l_1_vlan_interface = missing
    if (((t_2((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd)) or environment.getattr((undefined(name='ethernet_interface_bfd') if l_0_ethernet_interface_bfd is missing else l_0_ethernet_interface_bfd), 'configured')) or environment.getattr((undefined(name='port_channel_interface_bfd') if l_0_port_channel_interface_bfd is missing else l_0_port_channel_interface_bfd), 'configured')) or environment.getattr((undefined(name='vlan_interface_bfd') if l_0_vlan_interface_bfd is missing else l_0_vlan_interface_bfd), 'configured')):
        pass
        yield '\n## BFD\n'
        template = environment.get_template('documentation/router-bfd.j2', 'documentation/bfd.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interface_bfd': l_0_ethernet_interface_bfd, 'loopback_interface_bfd': l_0_loopback_interface_bfd, 'port_channel_interface_bfd': l_0_port_channel_interface_bfd, 'vlan_interface_bfd': l_0_vlan_interface_bfd})):
            yield event
        template = environment.get_template('documentation/bfd-interfaces.j2', 'documentation/bfd.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interface_bfd': l_0_ethernet_interface_bfd, 'loopback_interface_bfd': l_0_loopback_interface_bfd, 'port_channel_interface_bfd': l_0_port_channel_interface_bfd, 'vlan_interface_bfd': l_0_vlan_interface_bfd})):
            yield event

blocks = {}
debug_info = '7=29&8=32&9=35&10=38&11=41&12=44&15=46&18=50&19=53&22=55&25=59&26=62&29=64&32=68&36=71&38=74'