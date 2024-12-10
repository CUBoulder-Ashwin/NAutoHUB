from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dps-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dps_interfaces = resolve('dps_interfaces')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    for l_1_dps_interface in t_1((undefined(name='dps_interfaces') if l_0_dps_interfaces is missing else l_0_dps_interfaces), 'name'):
        l_1_tcp_mss_ceiling_cli = resolve('tcp_mss_ceiling_cli')
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_dps_interface, 'name'))
        yield '\n'
        if t_3(environment.getattr(l_1_dps_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_dps_interface, 'description'))
            yield '\n'
        if t_3(environment.getattr(l_1_dps_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_3(environment.getattr(l_1_dps_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_3(environment.getattr(l_1_dps_interface, 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr(l_1_dps_interface, 'mtu'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'hardware')):
            pass
            yield '   flow tracker hardware '
            yield str(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'hardware'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'sampled')):
            pass
            yield '   flow tracker sampled '
            yield str(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'sampled'))
            yield '\n'
        if t_3(environment.getattr(l_1_dps_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_dps_interface, 'ip_address'))
            yield '\n'
        if (t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv4')) or t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv6'))):
            pass
            l_1_tcp_mss_ceiling_cli = 'tcp mss ceiling'
            _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv4')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv4 ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv4'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv6')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv6 ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv6'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'direction')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'direction'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            yield '   '
            yield str((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli))
            yield '\n'
        if t_3(environment.getattr(l_1_dps_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_2(environment.getattr(l_1_dps_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_dps_interface = l_1_tcp_mss_ceiling_cli = missing

blocks = {}
debug_info = '7=30&9=35&10=37&11=40&13=42&15=45&18=48&19=51&21=53&22=56&24=58&25=61&27=63&28=66&30=68&31=70&32=72&33=74&35=76&36=78&38=80&39=82&41=85&43=87&44=90'