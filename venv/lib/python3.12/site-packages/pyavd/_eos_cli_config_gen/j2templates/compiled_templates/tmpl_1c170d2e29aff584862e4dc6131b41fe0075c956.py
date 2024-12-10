from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/tunnel-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tunnel_interfaces = resolve('tunnel_interfaces')
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
    for l_1_tunnel_interface in t_1((undefined(name='tunnel_interfaces') if l_0_tunnel_interfaces is missing else l_0_tunnel_interfaces), 'name'):
        l_1_tcp_mss_ceiling_cli = resolve('tcp_mss_ceiling_cli')
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_tunnel_interface, 'name'))
        yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_tunnel_interface, 'description'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_3(environment.getattr(l_1_tunnel_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr(l_1_tunnel_interface, 'mtu'))
            yield '\n'
        if (t_3(environment.getattr(l_1_tunnel_interface, 'vrf')) and (environment.getattr(l_1_tunnel_interface, 'vrf') != 'default')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_tunnel_interface, 'vrf'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_tunnel_interface, 'ip_address'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ipv6_enable'), True):
            pass
            yield '   ipv6 enable\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ipv6_address')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_tunnel_interface, 'ipv6_address'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling')):
            pass
            l_1_tcp_mss_ceiling_cli = 'tcp mss ceiling'
            _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv4')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv4 ', environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv4'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv6')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv6 ', environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv6'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_3(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'direction')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ', environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'direction'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            yield '   '
            yield str((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'access_group_in')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_tunnel_interface, 'access_group_in'))
            yield ' in\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'access_group_out')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_tunnel_interface, 'access_group_out'))
            yield ' out\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_in')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_in'))
            yield ' in\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_out')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_out'))
            yield ' out\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'nat_profile')):
            pass
            yield '   ip nat service-profile '
            yield str(environment.getattr(l_1_tunnel_interface, 'nat_profile'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'tunnel_mode')):
            pass
            yield '   tunnel mode '
            yield str(environment.getattr(l_1_tunnel_interface, 'tunnel_mode'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'source_interface')):
            pass
            yield '   tunnel source interface '
            yield str(environment.getattr(l_1_tunnel_interface, 'source_interface'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'destination')):
            pass
            yield '   tunnel destination '
            yield str(environment.getattr(l_1_tunnel_interface, 'destination'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'path_mtu_discovery'), True):
            pass
            yield '   tunnel path-mtu-discovery\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'ipsec_profile')):
            pass
            yield '   tunnel ipsec profile '
            yield str(environment.getattr(l_1_tunnel_interface, 'ipsec_profile'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'underlay_vrf')):
            pass
            yield '   tunnel underlay vrf '
            yield str(environment.getattr(l_1_tunnel_interface, 'underlay_vrf'))
            yield '\n'
        if t_3(environment.getattr(l_1_tunnel_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_2(environment.getattr(l_1_tunnel_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_tunnel_interface = l_1_tcp_mss_ceiling_cli = missing

blocks = {}
debug_info = '7=30&9=35&10=37&11=40&13=42&15=45&18=48&19=51&21=53&22=56&24=58&25=61&27=63&30=66&31=69&33=71&34=73&35=75&36=77&38=79&39=81&41=83&42=85&44=88&46=90&47=93&49=95&50=98&52=100&53=103&55=105&56=108&58=110&59=113&61=115&62=118&64=120&65=123&67=125&68=128&70=130&73=133&74=136&76=138&77=141&79=143&80=146'