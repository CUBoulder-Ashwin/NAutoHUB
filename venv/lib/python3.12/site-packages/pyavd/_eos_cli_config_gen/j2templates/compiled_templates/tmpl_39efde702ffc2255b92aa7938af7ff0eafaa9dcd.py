from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dhcp-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dhcp_servers = resolve('dhcp_servers')
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
        t_3 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_4 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    try:
        t_6 = environment.tests['true']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No test named 'true' found.")
    pass
    if t_5((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers)):
        pass
        l_1_loop = missing
        for l_1_dhcp_server, l_1_loop in LoopContext(t_2((undefined(name='dhcp_servers') if l_0_dhcp_servers is missing else l_0_dhcp_servers), 'vrf'), undefined):
            l_1_server_cli = missing
            _loop_vars = {}
            pass
            l_1_server_cli = 'dhcp server'
            _loop_vars['server_cli'] = l_1_server_cli
            if (environment.getattr(l_1_dhcp_server, 'vrf') != 'default'):
                pass
                l_1_server_cli = str_join(((undefined(name='server_cli') if l_1_server_cli is missing else l_1_server_cli), ' vrf ', environment.getattr(l_1_dhcp_server, 'vrf'), ))
                _loop_vars['server_cli'] = l_1_server_cli
            yield '!\n'
            yield str((undefined(name='server_cli') if l_1_server_cli is missing else l_1_server_cli))
            yield '\n'
            if ((t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'days')) and t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'hours'))) and t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'minutes'))):
                pass
                yield '   lease time ipv4 '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'days'))
                yield ' days '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'hours'))
                yield ' hours '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv4'), 'minutes'))
                yield ' minutes\n'
            if t_5(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv4')):
                pass
                yield '   dns domain name ipv4 '
                yield str(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv4'))
                yield '\n'
            if t_5(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv4')):
                pass
                yield '   dns server ipv4 '
                yield str(t_4(context.eval_ctx, t_2(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv4')), ' '))
                yield '\n'
            if ((t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'days')) and t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'hours'))) and t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'minutes'))):
                pass
                yield '   lease time ipv6 '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'days'))
                yield ' days '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'hours'))
                yield ' hours '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'lease_time_ipv6'), 'minutes'))
                yield ' minutes\n'
            if t_5(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv6')):
                pass
                yield '   dns domain name ipv6 '
                yield str(environment.getattr(l_1_dhcp_server, 'dns_domain_name_ipv6'))
                yield '\n'
            if t_5(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv6')):
                pass
                yield '   dns server ipv6 '
                yield str(t_4(context.eval_ctx, t_2(environment.getattr(l_1_dhcp_server, 'dns_servers_ipv6')), ' '))
                yield '\n'
            if t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv4')):
                pass
                yield '   tftp server file ipv4 '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv4'))
                yield '\n'
            if t_5(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv6')):
                pass
                yield '   tftp server file ipv6 '
                yield str(environment.getattr(environment.getattr(l_1_dhcp_server, 'tftp_server'), 'file_ipv6'))
                yield '\n'
            l_2_loop = missing
            for l_2_subnet, l_2_loop in LoopContext(t_2(environment.getattr(l_1_dhcp_server, 'subnets')), undefined):
                _loop_vars = {}
                pass
                yield '   !\n   subnet '
                yield str(environment.getattr(l_2_subnet, 'subnet'))
                yield '\n'
                if t_5(environment.getattr(l_2_subnet, 'reservations')):
                    pass
                    yield '      reservations\n'
                    l_3_loop = missing
                    for l_3_reservation, l_3_loop in LoopContext(t_2(environment.getattr(l_2_subnet, 'reservations'), 'mac_address'), undefined):
                        _loop_vars = {}
                        pass
                        yield '         mac-address '
                        yield str(environment.getattr(l_3_reservation, 'mac_address'))
                        yield '\n'
                        if t_5(environment.getattr(l_3_reservation, 'ipv4_address')):
                            pass
                            yield '            ipv4-address '
                            yield str(environment.getattr(l_3_reservation, 'ipv4_address'))
                            yield '\n'
                        if t_5(environment.getattr(l_3_reservation, 'ipv6_address')):
                            pass
                            yield '            ipv6-address '
                            yield str(environment.getattr(l_3_reservation, 'ipv6_address'))
                            yield '\n'
                        if t_5(environment.getattr(l_3_reservation, 'hostname')):
                            pass
                            yield '            hostname '
                            yield str(environment.getattr(l_3_reservation, 'hostname'))
                            yield '\n'
                        if (not environment.getattr(l_3_loop, 'last')):
                            pass
                            yield '         !\n'
                    l_3_loop = l_3_reservation = missing
                for l_3_range in t_2(t_2(environment.getattr(l_2_subnet, 'ranges'), 'end'), 'start'):
                    _loop_vars = {}
                    pass
                    yield '      !\n      range '
                    yield str(environment.getattr(l_3_range, 'start'))
                    yield ' '
                    yield str(environment.getattr(l_3_range, 'end'))
                    yield '\n'
                l_3_range = missing
                if t_5(environment.getattr(l_2_subnet, 'name')):
                    pass
                    yield '      name '
                    yield str(environment.getattr(l_2_subnet, 'name'))
                    yield '\n'
                if t_5(environment.getattr(l_2_subnet, 'dns_servers')):
                    pass
                    yield '      dns server '
                    yield str(t_4(context.eval_ctx, environment.getattr(l_2_subnet, 'dns_servers'), ' '))
                    yield '\n'
                if ((t_5(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'days')) and t_5(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'hours'))) and t_5(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'minutes'))):
                    pass
                    yield '      lease time '
                    yield str(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'days'))
                    yield ' days '
                    yield str(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'hours'))
                    yield ' hours '
                    yield str(environment.getattr(environment.getattr(l_2_subnet, 'lease_time'), 'minutes'))
                    yield ' minutes\n'
                if t_5(environment.getattr(l_2_subnet, 'default_gateway')):
                    pass
                    yield '      default-gateway '
                    yield str(environment.getattr(l_2_subnet, 'default_gateway'))
                    yield '\n'
            l_2_loop = l_2_subnet = missing
            if t_6(t_1(environment.getattr(l_1_dhcp_server, 'disabled'), False)):
                pass
                yield '   disabled\n'
            for l_2_option in t_2(environment.getattr(l_1_dhcp_server, 'ipv4_vendor_options'), 'vendor_id'):
                _loop_vars = {}
                pass
                yield '   !\n   vendor-option ipv4 '
                yield str(environment.getattr(l_2_option, 'vendor_id'))
                yield '\n'
                for l_3_sub_option in t_2(environment.getattr(l_2_option, 'sub_options'), 'code'):
                    _loop_vars = {}
                    pass
                    if t_5(environment.getattr(l_3_sub_option, 'string')):
                        pass
                        yield '      sub-option '
                        yield str(environment.getattr(l_3_sub_option, 'code'))
                        yield ' type string data "'
                        yield str(environment.getattr(l_3_sub_option, 'string'))
                        yield '"\n'
                    elif t_5(environment.getattr(l_3_sub_option, 'ipv4_address')):
                        pass
                        yield '      sub-option '
                        yield str(environment.getattr(l_3_sub_option, 'code'))
                        yield ' type ipv4-address data '
                        yield str(environment.getattr(l_3_sub_option, 'ipv4_address'))
                        yield '\n'
                    elif t_5(environment.getattr(l_3_sub_option, 'array_ipv4_address')):
                        pass
                        yield '      sub-option '
                        yield str(environment.getattr(l_3_sub_option, 'code'))
                        yield ' type array ipv4-address data '
                        yield str(t_4(context.eval_ctx, environment.getattr(l_3_sub_option, 'array_ipv4_address'), ' '))
                        yield '\n'
                l_3_sub_option = missing
            l_2_option = missing
            if t_5(environment.getattr(l_1_dhcp_server, 'eos_cli')):
                pass
                yield '   '
                yield str(t_3(environment.getattr(l_1_dhcp_server, 'eos_cli'), 3, False))
                yield '\n'
        l_1_loop = l_1_dhcp_server = l_1_server_cli = missing

blocks = {}
debug_info = '7=48&8=51&9=55&10=57&11=59&14=62&15=64&18=67&20=73&21=76&23=78&24=81&26=83&29=86&31=92&32=95&34=97&35=100&37=102&38=105&40=107&41=110&43=113&45=117&46=119&48=123&49=127&50=129&51=132&53=134&54=137&56=139&57=142&59=144&64=148&66=152&68=157&69=160&71=162&72=165&74=167&77=170&79=176&80=179&83=182&86=185&88=189&89=191&90=194&91=197&92=201&93=204&94=208&95=211&99=217&100=220'