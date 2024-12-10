from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/tunnel-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tunnel_interfaces = resolve('tunnel_interfaces')
    l_0_tunnel_interfaces_ipv4 = resolve('tunnel_interfaces_ipv4')
    l_0_tunnel_interfaces_ipv6 = resolve('tunnel_interfaces_ipv6')
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
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='tunnel_interfaces') if l_0_tunnel_interfaces is missing else l_0_tunnel_interfaces)):
        pass
        yield '\n### Tunnel Interfaces\n\n#### Tunnel Interfaces Summary\n\n'
        l_0_tunnel_interfaces_ipv4 = []
        context.vars['tunnel_interfaces_ipv4'] = l_0_tunnel_interfaces_ipv4
        context.exported_vars.add('tunnel_interfaces_ipv4')
        l_0_tunnel_interfaces_ipv6 = []
        context.vars['tunnel_interfaces_ipv6'] = l_0_tunnel_interfaces_ipv6
        context.exported_vars.add('tunnel_interfaces_ipv6')
        yield '| Interface | Description | VRF | Underlay VRF | MTU | Shutdown | NAT Profile | Mode | Source Interface | Destination | PMTU-Discovery | IPsec Profile |\n| --------- | ----------- | --- | ------------ | --- | -------- | ----------- | ---- | ---------------- | ----------- | -------------- | ------------- |\n'
        for l_1_tunnel_interface in t_2((undefined(name='tunnel_interfaces') if l_0_tunnel_interfaces is missing else l_0_tunnel_interfaces), 'name'):
            l_1_description = l_1_vrf = l_1_underlay_vrf = l_1_mtu = l_1_shutdown = l_1_nat_profile = l_1_tunnel_mode = l_1_row_source_interface = l_1_row_destination = l_1_row_pmtu = l_1_ipsec_profile = missing
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_tunnel_interface, 'ipv6_address')):
                pass
                context.call(environment.getattr((undefined(name='tunnel_interfaces_ipv6') if l_0_tunnel_interfaces_ipv6 is missing else l_0_tunnel_interfaces_ipv6), 'append'), l_1_tunnel_interface, _loop_vars=_loop_vars)
            if t_4(environment.getattr(l_1_tunnel_interface, 'ip_address')):
                pass
                context.call(environment.getattr((undefined(name='tunnel_interfaces_ipv4') if l_0_tunnel_interfaces_ipv4 is missing else l_0_tunnel_interfaces_ipv4), 'append'), l_1_tunnel_interface, _loop_vars=_loop_vars)
            l_1_description = t_1(environment.getattr(l_1_tunnel_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            l_1_vrf = t_1(environment.getattr(l_1_tunnel_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            l_1_underlay_vrf = t_1(environment.getattr(l_1_tunnel_interface, 'underlay_vrf'), 'default')
            _loop_vars['underlay_vrf'] = l_1_underlay_vrf
            l_1_mtu = t_1(environment.getattr(l_1_tunnel_interface, 'mtu'), '-')
            _loop_vars['mtu'] = l_1_mtu
            l_1_shutdown = t_1(environment.getattr(l_1_tunnel_interface, 'shutdown'), '-')
            _loop_vars['shutdown'] = l_1_shutdown
            l_1_nat_profile = t_1(environment.getattr(l_1_tunnel_interface, 'nat_profile'), '-')
            _loop_vars['nat_profile'] = l_1_nat_profile
            l_1_tunnel_mode = t_1(environment.getattr(l_1_tunnel_interface, 'tunnel_mode'), '-')
            _loop_vars['tunnel_mode'] = l_1_tunnel_mode
            l_1_row_source_interface = t_1(environment.getattr(l_1_tunnel_interface, 'source_interface'), '-')
            _loop_vars['row_source_interface'] = l_1_row_source_interface
            l_1_row_destination = t_1(environment.getattr(l_1_tunnel_interface, 'destination'), '-')
            _loop_vars['row_destination'] = l_1_row_destination
            l_1_row_pmtu = t_1(environment.getattr(l_1_tunnel_interface, 'path_mtu_discovery'), '-')
            _loop_vars['row_pmtu'] = l_1_row_pmtu
            l_1_ipsec_profile = t_1(environment.getattr(l_1_tunnel_interface, 'ipsec_profile'), '-')
            _loop_vars['ipsec_profile'] = l_1_ipsec_profile
            yield '| '
            yield str(environment.getattr(l_1_tunnel_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='underlay_vrf') if l_1_underlay_vrf is missing else l_1_underlay_vrf))
            yield ' | '
            yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
            yield ' | '
            yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
            yield ' | '
            yield str((undefined(name='nat_profile') if l_1_nat_profile is missing else l_1_nat_profile))
            yield ' | '
            yield str((undefined(name='tunnel_mode') if l_1_tunnel_mode is missing else l_1_tunnel_mode))
            yield ' | '
            yield str((undefined(name='row_source_interface') if l_1_row_source_interface is missing else l_1_row_source_interface))
            yield ' | '
            yield str((undefined(name='row_destination') if l_1_row_destination is missing else l_1_row_destination))
            yield ' | '
            yield str((undefined(name='row_pmtu') if l_1_row_pmtu is missing else l_1_row_pmtu))
            yield ' | '
            yield str((undefined(name='ipsec_profile') if l_1_ipsec_profile is missing else l_1_ipsec_profile))
            yield ' |\n'
        l_1_tunnel_interface = l_1_description = l_1_vrf = l_1_underlay_vrf = l_1_mtu = l_1_shutdown = l_1_nat_profile = l_1_tunnel_mode = l_1_row_source_interface = l_1_row_destination = l_1_row_pmtu = l_1_ipsec_profile = missing
        if (t_3((undefined(name='tunnel_interfaces_ipv4') if l_0_tunnel_interfaces_ipv4 is missing else l_0_tunnel_interfaces_ipv4)) > 0):
            pass
            yield '\n##### IPv4\n\n| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |\n| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |\n'
            for l_1_tunnel_interface in t_2((undefined(name='tunnel_interfaces_ipv4') if l_0_tunnel_interfaces_ipv4 is missing else l_0_tunnel_interfaces_ipv4), 'name'):
                l_1_row_vrf = l_1_row_ip_addr = l_1_row_tcp_mss = l_1_row_tcp_mss_direction = l_1_row_acl_in = l_1_row_acl_out = missing
                _loop_vars = {}
                pass
                l_1_row_vrf = t_1(environment.getattr(l_1_tunnel_interface, 'vrf'), 'default')
                _loop_vars['row_vrf'] = l_1_row_vrf
                l_1_row_ip_addr = t_1(environment.getattr(l_1_tunnel_interface, 'ip_address'), '-')
                _loop_vars['row_ip_addr'] = l_1_row_ip_addr
                l_1_row_tcp_mss = t_1(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv4'), '-')
                _loop_vars['row_tcp_mss'] = l_1_row_tcp_mss
                l_1_row_tcp_mss_direction = t_1(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'direction'), '-')
                _loop_vars['row_tcp_mss_direction'] = l_1_row_tcp_mss_direction
                l_1_row_acl_in = t_1(environment.getattr(l_1_tunnel_interface, 'access_group_in'), '-')
                _loop_vars['row_acl_in'] = l_1_row_acl_in
                l_1_row_acl_out = t_1(environment.getattr(l_1_tunnel_interface, 'access_group_out'), '-')
                _loop_vars['row_acl_out'] = l_1_row_acl_out
                yield '| '
                yield str(environment.getattr(l_1_tunnel_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
                yield ' | '
                yield str((undefined(name='row_ip_addr') if l_1_row_ip_addr is missing else l_1_row_ip_addr))
                yield ' | '
                yield str((undefined(name='row_tcp_mss') if l_1_row_tcp_mss is missing else l_1_row_tcp_mss))
                yield ' | '
                yield str((undefined(name='row_tcp_mss_direction') if l_1_row_tcp_mss_direction is missing else l_1_row_tcp_mss_direction))
                yield ' | '
                yield str((undefined(name='row_acl_in') if l_1_row_acl_in is missing else l_1_row_acl_in))
                yield ' | '
                yield str((undefined(name='row_acl_out') if l_1_row_acl_out is missing else l_1_row_acl_out))
                yield ' |\n'
            l_1_tunnel_interface = l_1_row_vrf = l_1_row_ip_addr = l_1_row_tcp_mss = l_1_row_tcp_mss_direction = l_1_row_acl_in = l_1_row_acl_out = missing
        if (t_3((undefined(name='tunnel_interfaces_ipv6') if l_0_tunnel_interfaces_ipv6 is missing else l_0_tunnel_interfaces_ipv6)) > 0):
            pass
            yield '\n##### IPv6\n\n| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out |\n| --------- | --- | ------------ | ------- | ----------------- | ----------- | ------------ |\n'
            for l_1_tunnel_interface in t_2((undefined(name='tunnel_interfaces_ipv6') if l_0_tunnel_interfaces_ipv6 is missing else l_0_tunnel_interfaces_ipv6), 'name'):
                l_1_row_vrf = l_1_row_ip_addr = l_1_row_tcp_mss = l_1_row_tcp_mss_direction = l_1_row_acl_in = l_1_row_acl_out = missing
                _loop_vars = {}
                pass
                l_1_row_vrf = t_1(environment.getattr(l_1_tunnel_interface, 'vrf'), 'default')
                _loop_vars['row_vrf'] = l_1_row_vrf
                l_1_row_ip_addr = t_1(environment.getattr(l_1_tunnel_interface, 'ipv6_address'), '-')
                _loop_vars['row_ip_addr'] = l_1_row_ip_addr
                l_1_row_tcp_mss = t_1(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'ipv6'), '-')
                _loop_vars['row_tcp_mss'] = l_1_row_tcp_mss
                l_1_row_tcp_mss_direction = t_1(environment.getattr(environment.getattr(l_1_tunnel_interface, 'tcp_mss_ceiling'), 'direction'), '-')
                _loop_vars['row_tcp_mss_direction'] = l_1_row_tcp_mss_direction
                l_1_row_acl_in = t_1(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_in'), '-')
                _loop_vars['row_acl_in'] = l_1_row_acl_in
                l_1_row_acl_out = t_1(environment.getattr(l_1_tunnel_interface, 'ipv6_access_group_out'), '-')
                _loop_vars['row_acl_out'] = l_1_row_acl_out
                yield '| '
                yield str(environment.getattr(l_1_tunnel_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
                yield ' | '
                yield str((undefined(name='row_ip_addr') if l_1_row_ip_addr is missing else l_1_row_ip_addr))
                yield ' | '
                yield str((undefined(name='row_tcp_mss') if l_1_row_tcp_mss is missing else l_1_row_tcp_mss))
                yield ' | '
                yield str((undefined(name='row_tcp_mss_direction') if l_1_row_tcp_mss_direction is missing else l_1_row_tcp_mss_direction))
                yield ' | '
                yield str((undefined(name='row_acl_in') if l_1_row_acl_in is missing else l_1_row_acl_in))
                yield ' | '
                yield str((undefined(name='row_acl_out') if l_1_row_acl_out is missing else l_1_row_acl_out))
                yield ' |\n'
            l_1_tunnel_interface = l_1_row_vrf = l_1_row_ip_addr = l_1_row_tcp_mss = l_1_row_tcp_mss_direction = l_1_row_acl_in = l_1_row_acl_out = missing
        yield '\n#### Tunnel Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/tunnel-interfaces.j2', 'documentation/tunnel-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'tunnel_interfaces_ipv4': l_0_tunnel_interfaces_ipv4, 'tunnel_interfaces_ipv6': l_0_tunnel_interfaces_ipv6})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=38&13=41&14=44&17=48&18=52&19=54&21=55&22=57&24=58&25=60&26=62&27=64&28=66&29=68&30=70&31=72&32=74&33=76&34=78&35=81&38=106&44=109&45=113&46=115&47=117&48=119&49=121&50=123&51=126&55=141&61=144&62=148&63=150&64=152&65=154&66=156&67=158&68=161&75=177'