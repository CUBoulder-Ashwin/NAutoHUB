from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mpls-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mpls_configured = resolve('mpls_configured')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_loopback_interfaces = resolve('loopback_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
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
    if ((environment.getattr((undefined(name='mpls_configured') if l_0_mpls_configured is missing else l_0_mpls_configured), 'ethernet_interfaces') or environment.getattr((undefined(name='mpls_configured') if l_0_mpls_configured is missing else l_0_mpls_configured), 'loopback_interfaces')) or environment.getattr((undefined(name='mpls_configured') if l_0_mpls_configured is missing else l_0_mpls_configured), 'port_channel_interfaces')):
        pass
        yield '\n### MPLS Interfaces\n\n| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |\n| --------- | --------------- | ----------- | -------- |\n'
        for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            l_1_row_mpls_ip = resolve('row_mpls_ip')
            l_1_row_ldp_interface = resolve('row_ldp_interface')
            l_1_row_ldp_igp_sync = resolve('row_ldp_igp_sync')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_ethernet_interface, 'mpls')):
                pass
                l_1_row_mpls_ip = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ip'), '-')
                _loop_vars['row_mpls_ip'] = l_1_row_mpls_ip
                l_1_row_ldp_interface = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'interface'), '-')
                _loop_vars['row_ldp_interface'] = l_1_row_ldp_interface
                l_1_row_ldp_igp_sync = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'igp_sync'), '-')
                _loop_vars['row_ldp_igp_sync'] = l_1_row_ldp_igp_sync
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_mpls_ip') if l_1_row_mpls_ip is missing else l_1_row_mpls_ip))
                yield ' | '
                yield str((undefined(name='row_ldp_interface') if l_1_row_ldp_interface is missing else l_1_row_ldp_interface))
                yield ' | '
                yield str((undefined(name='row_ldp_igp_sync') if l_1_row_ldp_igp_sync is missing else l_1_row_ldp_igp_sync))
                yield ' |\n'
        l_1_ethernet_interface = l_1_row_mpls_ip = l_1_row_ldp_interface = l_1_row_ldp_igp_sync = missing
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            l_1_row_ldp_interface = resolve('row_ldp_interface')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_loopback_interface, 'mpls')):
                pass
                l_1_row_ldp_interface = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_loopback_interface, 'mpls'), 'ldp'), 'interface'), '-')
                _loop_vars['row_ldp_interface'] = l_1_row_ldp_interface
                yield '| '
                yield str(environment.getattr(l_1_loopback_interface, 'name'))
                yield ' | - | '
                yield str((undefined(name='row_ldp_interface') if l_1_row_ldp_interface is missing else l_1_row_ldp_interface))
                yield ' | - |\n'
        l_1_loopback_interface = l_1_row_ldp_interface = missing
        for l_1_port_channel_interface in t_2((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
            l_1_row_mpls_ip = resolve('row_mpls_ip')
            l_1_row_ldp_interface = resolve('row_ldp_interface')
            l_1_row_ldp_igp_sync = resolve('row_ldp_igp_sync')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_port_channel_interface, 'mpls')):
                pass
                l_1_row_mpls_ip = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'mpls'), 'ip'), '-')
                _loop_vars['row_mpls_ip'] = l_1_row_mpls_ip
                l_1_row_ldp_interface = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'mpls'), 'ldp'), 'interface'), '-')
                _loop_vars['row_ldp_interface'] = l_1_row_ldp_interface
                l_1_row_ldp_igp_sync = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'mpls'), 'ldp'), 'igp_sync'), '-')
                _loop_vars['row_ldp_igp_sync'] = l_1_row_ldp_igp_sync
                yield '| '
                yield str(environment.getattr(l_1_port_channel_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_mpls_ip') if l_1_row_mpls_ip is missing else l_1_row_mpls_ip))
                yield ' | '
                yield str((undefined(name='row_ldp_interface') if l_1_row_ldp_interface is missing else l_1_row_ldp_interface))
                yield ' | '
                yield str((undefined(name='row_ldp_igp_sync') if l_1_row_ldp_igp_sync is missing else l_1_row_ldp_igp_sync))
                yield ' |\n'
        l_1_port_channel_interface = l_1_row_mpls_ip = l_1_row_ldp_interface = l_1_row_ldp_igp_sync = missing

blocks = {}
debug_info = '7=33&13=36&14=42&15=44&16=46&17=48&18=51&21=60&22=64&23=66&24=69&27=74&28=80&29=82&30=84&31=86&32=89'