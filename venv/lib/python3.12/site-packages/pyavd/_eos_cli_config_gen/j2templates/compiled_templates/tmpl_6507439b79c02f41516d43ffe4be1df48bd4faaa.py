from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dhcp-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_dhcp_servers = resolve('dhcp_servers')
    l_0_ethernet_interfaces_dhcp_server = missing
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_ethernet_interfaces_dhcp_server = []
    context.vars['ethernet_interfaces_dhcp_server'] = l_0_ethernet_interfaces_dhcp_server
    context.exported_vars.add('ethernet_interfaces_dhcp_server')
    for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if (t_5(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv4'), True) or t_5(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv4'), True)):
            pass
            context.call(environment.getattr((undefined(name='ethernet_interfaces_dhcp_server') if l_0_ethernet_interfaces_dhcp_server is missing else l_0_ethernet_interfaces_dhcp_server), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    if ((t_4((undefined(name='ethernet_interfaces_dhcp_server') if l_0_ethernet_interfaces_dhcp_server is missing else l_0_ethernet_interfaces_dhcp_server)) > 0) or t_5((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers))):
        pass
        yield '\n## DHCP Server\n'
        if t_5((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers)):
            pass
            yield '\n### DHCP Servers Summary\n\n| DHCP Server Enabled | VRF | IPv4 DNS Domain | IPv4 DNS Servers | IPv4 Bootfile | IPv6 DNS Domain | IPv6 DNS Servers | IPv6 Bootfile |\n| ------------------- | --- | --------------- | ---------------- | ------------- | --------------- | ---------------- | ------------- |\n'
            for l_1_dhcp_server in t_2((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers), 'vrf'):
                l_1_enabled = l_1_dns_domain_ipv4 = l_1_dns_servers_ipv4 = l_1_tftp_server_file_ipv4 = l_1_dns_domain_ipv6 = l_1_dns_servers_ipv6 = l_1_tftp_server_file_ipv6 = missing
                _loop_vars = {}
                pass
                l_1_enabled = (not t_1(environment.getattr(l_1_dhcp_server, 'disabled'), False))
                _loop_vars['enabled'] = l_1_enabled
                l_1_dns_domain_ipv4 = t_1(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv4'), '-')
                _loop_vars['dns_domain_ipv4'] = l_1_dns_domain_ipv4
                l_1_dns_servers_ipv4 = t_3(context.eval_ctx, t_1(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv4'), ['-']), ', ')
                _loop_vars['dns_servers_ipv4'] = l_1_dns_servers_ipv4
                l_1_tftp_server_file_ipv4 = t_1(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv4'), '-')
                _loop_vars['tftp_server_file_ipv4'] = l_1_tftp_server_file_ipv4
                l_1_dns_domain_ipv6 = t_1(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv6'), '-')
                _loop_vars['dns_domain_ipv6'] = l_1_dns_domain_ipv6
                l_1_dns_servers_ipv6 = t_3(context.eval_ctx, t_1(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv6'), ['-']), ', ')
                _loop_vars['dns_servers_ipv6'] = l_1_dns_servers_ipv6
                l_1_tftp_server_file_ipv6 = t_1(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv6'), '-')
                _loop_vars['tftp_server_file_ipv6'] = l_1_tftp_server_file_ipv6
                yield '| '
                yield str((undefined(name='enabled') if l_1_enabled is missing else l_1_enabled))
                yield ' | '
                yield str(environment.getattr(l_1_dhcp_server, 'vrf'))
                yield ' | '
                yield str((undefined(name='dns_domain_ipv4') if l_1_dns_domain_ipv4 is missing else l_1_dns_domain_ipv4))
                yield ' | '
                yield str((undefined(name='dns_servers_ipv4') if l_1_dns_servers_ipv4 is missing else l_1_dns_servers_ipv4))
                yield ' | '
                yield str((undefined(name='tftp_server_file_ipv4') if l_1_tftp_server_file_ipv4 is missing else l_1_tftp_server_file_ipv4))
                yield ' | '
                yield str((undefined(name='dns_domain_ipv6') if l_1_dns_domain_ipv6 is missing else l_1_dns_domain_ipv6))
                yield ' | '
                yield str((undefined(name='dns_servers_ipv6') if l_1_dns_servers_ipv6 is missing else l_1_dns_servers_ipv6))
                yield ' | '
                yield str((undefined(name='tftp_server_file_ipv6') if l_1_tftp_server_file_ipv6 is missing else l_1_tftp_server_file_ipv6))
                yield ' |\n'
            l_1_dhcp_server = l_1_enabled = l_1_dns_domain_ipv4 = l_1_dns_servers_ipv4 = l_1_tftp_server_file_ipv4 = l_1_dns_domain_ipv6 = l_1_dns_servers_ipv6 = l_1_tftp_server_file_ipv6 = missing
            for l_1_dhcp_server in t_2((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers), 'vrf'):
                l_1_dhcp_server_subnets = l_1_dhcp_vendor_options = missing
                _loop_vars = {}
                pass
                l_1_dhcp_server_subnets = []
                _loop_vars['dhcp_server_subnets'] = l_1_dhcp_server_subnets
                l_1_dhcp_vendor_options = []
                _loop_vars['dhcp_vendor_options'] = l_1_dhcp_vendor_options
                for l_2_subnet in t_2(environment.getattr(l_1_dhcp_server, 'subnets')):
                    l_2_subnet_lease_time = resolve('subnet_lease_time')
                    l_2_subnet_ranges = resolve('subnet_ranges')
                    l_2_subnet_dns_servers = l_2_subnet_default_gw = missing
                    _loop_vars = {}
                    pass
                    l_2_subnet_dns_servers = t_3(context.eval_ctx, t_1(environment.getattr(l_2_subnet, 'dns_servers'), ['-']), ', ')
                    _loop_vars['subnet_dns_servers'] = l_2_subnet_dns_servers
                    if t_5(environment.getattr(l_2_subnet, 'lease_time')):
                        pass
                        l_2_subnet_lease_time = str_join((environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'days'), ' days, ', environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'hours'), ' hours, ', environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'minutes'), ' minutes', ))
                        _loop_vars['subnet_lease_time'] = l_2_subnet_lease_time
                    else:
                        pass
                        l_2_subnet_lease_time = '-'
                        _loop_vars['subnet_lease_time'] = l_2_subnet_lease_time
                    l_2_subnet_default_gw = t_1(environment.getattr(l_2_subnet, 'default_gateway'), '-')
                    _loop_vars['subnet_default_gw'] = l_2_subnet_default_gw
                    if (t_5(environment.getattr(l_2_subnet, 'ranges')) and (t_4(environment.getattr(l_2_subnet, 'ranges')) > 0)):
                        pass
                        l_2_subnet_ranges = []
                        _loop_vars['subnet_ranges'] = l_2_subnet_ranges
                        for l_3_range in t_2(environment.getattr(l_2_subnet, 'ranges'), 'start'):
                            _loop_vars = {}
                            pass
                            context.call(environment.getattr((undefined(name='subnet_ranges') if l_2_subnet_ranges is missing else l_2_subnet_ranges), 'append'), str_join((environment.getattr(l_3_range, 'start'), '-', environment.getattr(l_3_range, 'end'), )), _loop_vars=_loop_vars)
                        l_3_range = missing
                    else:
                        pass
                        l_2_subnet_ranges = ['-']
                        _loop_vars['subnet_ranges'] = l_2_subnet_ranges
                    context.call(environment.getattr((undefined(name='dhcp_server_subnets') if l_1_dhcp_server_subnets is missing else l_1_dhcp_server_subnets), 'append'), {'subnet': environment.getattr(l_2_subnet, 'subnet'), 'name': t_1(environment.getattr(l_2_subnet, 'name'), '-'), 'dns_servers': (undefined(name='subnet_dns_servers') if l_2_subnet_dns_servers is missing else l_2_subnet_dns_servers), 'lease_time': (undefined(name='subnet_lease_time') if l_2_subnet_lease_time is missing else l_2_subnet_lease_time), 'default_gateway': (undefined(name='subnet_default_gw') if l_2_subnet_default_gw is missing else l_2_subnet_default_gw), 'ranges': t_3(context.eval_ctx, (undefined(name='subnet_ranges') if l_2_subnet_ranges is missing else l_2_subnet_ranges), ', ')}, _loop_vars=_loop_vars)
                l_2_subnet = l_2_subnet_dns_servers = l_2_subnet_lease_time = l_2_subnet_default_gw = l_2_subnet_ranges = missing
                for l_2_option in t_2(environment.getattr(l_1_dhcp_server, 'ipv4_vendor_options'), 'vendor_id'):
                    _loop_vars = {}
                    pass
                    context.call(environment.getattr((undefined(name='dhcp_vendor_options') if l_1_dhcp_vendor_options is missing else l_1_dhcp_vendor_options), 'append'), {'vendor_id': environment.getattr(l_2_option, 'vendor_id'), 'sub_options': environment.getattr(l_2_option, 'sub_options')}, _loop_vars=_loop_vars)
                l_2_option = missing
                if ((t_4((undefined(name='dhcp_server_subnets') if l_1_dhcp_server_subnets is missing else l_1_dhcp_server_subnets)) > 0) or (t_4((undefined(name='dhcp_vendor_options') if l_1_dhcp_vendor_options is missing else l_1_dhcp_vendor_options)) > 0)):
                    pass
                    yield '\n#### VRF '
                    yield str(environment.getattr(l_1_dhcp_server, 'vrf'))
                    yield ' DHCP Server\n'
                    if (t_4((undefined(name='dhcp_server_subnets') if l_1_dhcp_server_subnets is missing else l_1_dhcp_server_subnets)) > 0):
                        pass
                        yield '\n##### Subnets\n\n| Subnet | Name | DNS Servers | Default Gateway | Lease Time | Ranges |\n| ------ | ---- | ----------- | --------------- | ---------- | ------ |\n'
                        for l_2_subnet in (undefined(name='dhcp_server_subnets') if l_1_dhcp_server_subnets is missing else l_1_dhcp_server_subnets):
                            _loop_vars = {}
                            pass
                            yield '| '
                            yield str(environment.getattr(l_2_subnet, 'subnet'))
                            yield ' | '
                            yield str(t_1(environment.getattr(l_2_subnet, 'name'), '-'))
                            yield ' | '
                            yield str(environment.getattr(l_2_subnet, 'dns_servers'))
                            yield ' | '
                            yield str(environment.getattr(l_2_subnet, 'default_gateway'))
                            yield ' | '
                            yield str(environment.getattr(l_2_subnet, 'lease_time'))
                            yield ' | '
                            yield str(environment.getattr(l_2_subnet, 'ranges'))
                            yield ' |\n'
                        l_2_subnet = missing
                    if (t_4((undefined(name='dhcp_vendor_options') if l_1_dhcp_vendor_options is missing else l_1_dhcp_vendor_options)) > 0):
                        pass
                        yield '\n##### IPv4 Vendor Options\n\n| Vendor ID | Sub-option Code | Sub-option Type | Sub-option Data |\n| --------- | ----------------| --------------- | --------------- |\n'
                        for l_2_option in t_2((undefined(name='dhcp_vendor_options') if l_1_dhcp_vendor_options is missing else l_1_dhcp_vendor_options), 'vendor_id'):
                            _loop_vars = {}
                            pass
                            for l_3_sub_option in t_2(environment.getattr(l_2_option, 'sub_options'), 'code'):
                                l_3_sub_option_type = resolve('sub_option_type')
                                l_3_sub_option_data = resolve('sub_option_data')
                                _loop_vars = {}
                                pass
                                if t_5(environment.getattr(l_3_sub_option, 'string')):
                                    pass
                                    l_3_sub_option_type = 'string'
                                    _loop_vars['sub_option_type'] = l_3_sub_option_type
                                    l_3_sub_option_data = environment.getattr(l_3_sub_option, 'string')
                                    _loop_vars['sub_option_data'] = l_3_sub_option_data
                                elif t_5(environment.getattr(l_3_sub_option, 'ipv4_address')):
                                    pass
                                    l_3_sub_option_type = 'ipv4-address'
                                    _loop_vars['sub_option_type'] = l_3_sub_option_type
                                    l_3_sub_option_data = environment.getattr(l_3_sub_option, 'ipv4_address')
                                    _loop_vars['sub_option_data'] = l_3_sub_option_data
                                elif t_5(environment.getattr(l_3_sub_option, 'array_ipv4_address')):
                                    pass
                                    l_3_sub_option_type = 'array ipv4-address'
                                    _loop_vars['sub_option_type'] = l_3_sub_option_type
                                    l_3_sub_option_data = t_3(context.eval_ctx, environment.getattr(l_3_sub_option, 'array_ipv4_address'), ' ')
                                    _loop_vars['sub_option_data'] = l_3_sub_option_data
                                if t_5((undefined(name='sub_option_type') if l_3_sub_option_type is missing else l_3_sub_option_type)):
                                    pass
                                    yield '| '
                                    yield str(environment.getattr(l_2_option, 'vendor_id'))
                                    yield ' | '
                                    yield str(environment.getattr(l_3_sub_option, 'code'))
                                    yield ' | '
                                    yield str((undefined(name='sub_option_type') if l_3_sub_option_type is missing else l_3_sub_option_type))
                                    yield ' | '
                                    yield str((undefined(name='sub_option_data') if l_3_sub_option_data is missing else l_3_sub_option_data))
                                    yield ' |\n'
                            l_3_sub_option = l_3_sub_option_type = l_3_sub_option_data = missing
                        l_2_option = missing
            l_1_dhcp_server = l_1_dhcp_server_subnets = l_1_dhcp_vendor_options = missing
            yield '\n### DHCP Server Configuration\n\n```eos\n'
            template = environment.get_template('eos/dhcp-servers.j2', 'documentation/dhcp-server.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_dhcp_server': l_0_ethernet_interfaces_dhcp_server})):
                yield event
            yield '```\n'
        if (t_4((undefined(name='ethernet_interfaces_dhcp_server') if l_0_ethernet_interfaces_dhcp_server is missing else l_0_ethernet_interfaces_dhcp_server)) > 0):
            pass
            yield '\n### DHCP Server Interfaces\n\n| Interface name | DHCP IPv4 | DHCP IPv6 |\n| -------------- | --------- | --------- |\n'
            for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces_dhcp_server') if l_0_ethernet_interfaces_dhcp_server is missing else l_0_ethernet_interfaces_dhcp_server)):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv4'), False))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv6'), False))
                yield ' |\n'
            l_1_ethernet_interface = missing

blocks = {}
debug_info = '7=44&8=47&9=50&10=52&13=54&16=57&22=60&23=64&24=66&25=68&26=70&27=72&28=74&29=76&30=79&32=96&33=100&34=102&35=104&36=110&37=112&38=114&40=118&42=120&43=122&44=124&45=126&46=129&49=133&51=135&53=137&54=140&56=142&58=145&59=147&65=150&66=154&69=167&75=170&76=173&77=178&78=180&79=182&80=184&81=186&82=188&83=190&84=192&85=194&87=196&88=199&99=211&102=215&108=218&109=222'