from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_interfaces = resolve('management_interfaces')
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
    for l_1_management_interface in t_1((undefined(name='management_interfaces') if l_0_management_interfaces is missing else l_0_management_interfaces), 'name'):
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_management_interface, 'name'))
        yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_management_interface, 'description'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_3(environment.getattr(l_1_management_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_3(environment.getattr(l_1_management_interface, 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr(l_1_management_interface, 'mtu'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'mac_address')):
            pass
            yield '   mac-address '
            yield str(environment.getattr(l_1_management_interface, 'mac_address'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'speed')):
            pass
            yield '   speed '
            yield str(environment.getattr(l_1_management_interface, 'speed'))
            yield '\n'
        if (t_3(environment.getattr(l_1_management_interface, 'vrf')) and (environment.getattr(l_1_management_interface, 'vrf') != 'default')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_management_interface, 'vrf'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_management_interface, 'ip_address'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'ipv6_enable'), True):
            pass
            yield '   ipv6 enable\n'
        if t_3(environment.getattr(l_1_management_interface, 'ipv6_address')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_management_interface, 'ipv6_address'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_management_interface, 'lldp'), 'transmit'), False):
            pass
            yield '   no lldp transmit\n'
        if t_3(environment.getattr(environment.getattr(l_1_management_interface, 'lldp'), 'receive'), False):
            pass
            yield '   no lldp receive\n'
        if t_3(environment.getattr(environment.getattr(l_1_management_interface, 'lldp'), 'ztp_vlan')):
            pass
            yield '   lldp tlv transmit ztp vlan '
            yield str(environment.getattr(environment.getattr(l_1_management_interface, 'lldp'), 'ztp_vlan'))
            yield '\n'
        if t_3(environment.getattr(l_1_management_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_2(environment.getattr(l_1_management_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_management_interface = missing

blocks = {}
debug_info = '7=30&9=34&10=36&11=39&13=41&15=44&18=47&19=50&21=52&22=55&24=57&25=60&27=62&28=65&30=67&31=70&33=72&36=75&37=78&39=80&42=83&45=86&46=89&48=91&49=94'