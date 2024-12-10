from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/bfd-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vlan_interface_bfd = resolve('vlan_interface_bfd')
    l_0_ethernet_interface_bfd = resolve('ethernet_interface_bfd')
    l_0_port_channel_interface_bfd = resolve('port_channel_interface_bfd')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((environment.getattr((undefined(name='vlan_interface_bfd') if l_0_vlan_interface_bfd is missing else l_0_vlan_interface_bfd), 'configured') or environment.getattr((undefined(name='ethernet_interface_bfd') if l_0_ethernet_interface_bfd is missing else l_0_ethernet_interface_bfd), 'configured')) or environment.getattr((undefined(name='port_channel_interface_bfd') if l_0_port_channel_interface_bfd is missing else l_0_port_channel_interface_bfd), 'configured')):
        pass
        yield '\n### BFD Interfaces\n\n| Interface | Interval | Minimum RX | Multiplier | Echo |\n| --------- | -------- | ---------- | ---------- | ---- |\n'
        if environment.getattr((undefined(name='ethernet_interface_bfd') if l_0_ethernet_interface_bfd is missing else l_0_ethernet_interface_bfd), 'configured'):
            pass
            for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                l_1_interval = resolve('interval')
                l_1_min_rx = resolve('min_rx')
                l_1_multiplier = resolve('multiplier')
                l_1_echo = resolve('echo')
                _loop_vars = {}
                pass
                if ((t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval')) and t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))) and t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))):
                    pass
                    l_1_interval = environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval')
                    _loop_vars['interval'] = l_1_interval
                    l_1_min_rx = environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx')
                    _loop_vars['min_rx'] = l_1_min_rx
                    l_1_multiplier = environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier')
                    _loop_vars['multiplier'] = l_1_multiplier
                    l_1_echo = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'echo'), '-')
                    _loop_vars['echo'] = l_1_echo
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='interval') if l_1_interval is missing else l_1_interval))
                    yield ' | '
                    yield str((undefined(name='min_rx') if l_1_min_rx is missing else l_1_min_rx))
                    yield ' | '
                    yield str((undefined(name='multiplier') if l_1_multiplier is missing else l_1_multiplier))
                    yield ' | '
                    yield str((undefined(name='echo') if l_1_echo is missing else l_1_echo))
                    yield ' |\n'
            l_1_ethernet_interface = l_1_interval = l_1_min_rx = l_1_multiplier = l_1_echo = missing
        if environment.getattr((undefined(name='port_channel_interface_bfd') if l_0_port_channel_interface_bfd is missing else l_0_port_channel_interface_bfd), 'configured'):
            pass
            for l_1_port_channel_interface in t_2((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
                l_1_interval = resolve('interval')
                l_1_min_rx = resolve('min_rx')
                l_1_multiplier = resolve('multiplier')
                l_1_echo = resolve('echo')
                _loop_vars = {}
                pass
                if ((t_3(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'interval')) and t_3(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'min_rx'))) and t_3(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'multiplier'))):
                    pass
                    l_1_interval = environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'interval')
                    _loop_vars['interval'] = l_1_interval
                    l_1_min_rx = environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'min_rx')
                    _loop_vars['min_rx'] = l_1_min_rx
                    l_1_multiplier = environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'multiplier')
                    _loop_vars['multiplier'] = l_1_multiplier
                    l_1_echo = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'bfd'), 'echo'), '-')
                    _loop_vars['echo'] = l_1_echo
                    yield '| '
                    yield str(environment.getattr(l_1_port_channel_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='interval') if l_1_interval is missing else l_1_interval))
                    yield ' | '
                    yield str((undefined(name='min_rx') if l_1_min_rx is missing else l_1_min_rx))
                    yield ' | '
                    yield str((undefined(name='multiplier') if l_1_multiplier is missing else l_1_multiplier))
                    yield ' | '
                    yield str((undefined(name='echo') if l_1_echo is missing else l_1_echo))
                    yield ' |\n'
            l_1_port_channel_interface = l_1_interval = l_1_min_rx = l_1_multiplier = l_1_echo = missing
        if environment.getattr((undefined(name='vlan_interface_bfd') if l_0_vlan_interface_bfd is missing else l_0_vlan_interface_bfd), 'configured'):
            pass
            for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
                l_1_interval = resolve('interval')
                l_1_min_rx = resolve('min_rx')
                l_1_multiplier = resolve('multiplier')
                l_1_echo = resolve('echo')
                _loop_vars = {}
                pass
                if ((t_3(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'interval')) and t_3(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'min_rx'))) and t_3(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'multiplier'))):
                    pass
                    l_1_interval = environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'interval')
                    _loop_vars['interval'] = l_1_interval
                    l_1_min_rx = environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'min_rx')
                    _loop_vars['min_rx'] = l_1_min_rx
                    l_1_multiplier = environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'multiplier')
                    _loop_vars['multiplier'] = l_1_multiplier
                    l_1_echo = t_1(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'echo'), '-')
                    _loop_vars['echo'] = l_1_echo
                    yield '| '
                    yield str(environment.getattr(l_1_vlan_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='interval') if l_1_interval is missing else l_1_interval))
                    yield ' | '
                    yield str((undefined(name='min_rx') if l_1_min_rx is missing else l_1_min_rx))
                    yield ' | '
                    yield str((undefined(name='multiplier') if l_1_multiplier is missing else l_1_multiplier))
                    yield ' | '
                    yield str((undefined(name='echo') if l_1_echo is missing else l_1_echo))
                    yield ' |\n'
            l_1_vlan_interface = l_1_interval = l_1_min_rx = l_1_multiplier = l_1_echo = missing

blocks = {}
debug_info = '7=35&13=38&14=40&15=47&18=49&19=51&20=53&21=55&22=58&26=69&27=71&28=78&31=80&32=82&33=84&34=86&35=89&39=100&40=102&41=109&44=111&45=113&46=115&47=117&48=120'