from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/application-traffic-recognition.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_application_traffic_recognition = resolve('application_traffic_recognition')
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
        t_4 = environment.filters['sort']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'sort' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition)):
        pass
        yield '\n## Application Traffic Recognition\n'
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications')):
            pass
            yield '\n### Applications\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'ipv4_applications')):
                pass
                yield '\n#### IPv4 Applications\n\n| Name | Source Prefix | Destination Prefix | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set | DSCP |\n| ---- | ------------- | ------------------ | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ | ---- |\n'
                for l_1_application in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'ipv4_applications'), 'name'):
                    l_1_src_prefix = l_1_dest_prefix = l_1_tcp_src_port = l_1_tcp_dest_port = l_1_udp_src_port = l_1_udp_dest_port = l_1_protocol_ranges = l_1_protocol = l_1_dscp_ranges = missing
                    _loop_vars = {}
                    pass
                    l_1_src_prefix = t_1(environment.getattr(l_1_application, 'src_prefix_set_name'), '-')
                    _loop_vars['src_prefix'] = l_1_src_prefix
                    l_1_dest_prefix = t_1(environment.getattr(l_1_application, 'dest_prefix_set_name'), '-')
                    _loop_vars['dest_prefix'] = l_1_dest_prefix
                    l_1_tcp_src_port = t_1(environment.getattr(l_1_application, 'tcp_src_port_set_name'), '-')
                    _loop_vars['tcp_src_port'] = l_1_tcp_src_port
                    l_1_tcp_dest_port = t_1(environment.getattr(l_1_application, 'tcp_dest_port_set_name'), '-')
                    _loop_vars['tcp_dest_port'] = l_1_tcp_dest_port
                    l_1_udp_src_port = t_1(environment.getattr(l_1_application, 'udp_src_port_set_name'), '-')
                    _loop_vars['udp_src_port'] = l_1_udp_src_port
                    l_1_udp_dest_port = t_1(environment.getattr(l_1_application, 'udp_dest_port_set_name'), '-')
                    _loop_vars['udp_dest_port'] = l_1_udp_dest_port
                    l_1_protocol_ranges = t_3(context.eval_ctx, t_1(environment.getattr(l_1_application, 'protocol_ranges'), ['-']), ', ')
                    _loop_vars['protocol_ranges'] = l_1_protocol_ranges
                    l_1_protocol = t_3(context.eval_ctx, t_1(environment.getattr(l_1_application, 'protocols'), ['-']), ', ')
                    _loop_vars['protocol'] = l_1_protocol
                    l_1_dscp_ranges = t_3(context.eval_ctx, t_1(environment.getattr(l_1_application, 'dscp_ranges'), ['-']), ' ')
                    _loop_vars['dscp_ranges'] = l_1_dscp_ranges
                    yield '| '
                    yield str(environment.getattr(l_1_application, 'name'))
                    yield ' | '
                    yield str((undefined(name='src_prefix') if l_1_src_prefix is missing else l_1_src_prefix))
                    yield ' | '
                    yield str((undefined(name='dest_prefix') if l_1_dest_prefix is missing else l_1_dest_prefix))
                    yield ' | '
                    yield str((undefined(name='protocol') if l_1_protocol is missing else l_1_protocol))
                    yield ' | '
                    yield str((undefined(name='protocol_ranges') if l_1_protocol_ranges is missing else l_1_protocol_ranges))
                    yield ' | '
                    yield str((undefined(name='tcp_src_port') if l_1_tcp_src_port is missing else l_1_tcp_src_port))
                    yield ' | '
                    yield str((undefined(name='tcp_dest_port') if l_1_tcp_dest_port is missing else l_1_tcp_dest_port))
                    yield ' | '
                    yield str((undefined(name='udp_src_port') if l_1_udp_src_port is missing else l_1_udp_src_port))
                    yield ' | '
                    yield str((undefined(name='udp_dest_port') if l_1_udp_dest_port is missing else l_1_udp_dest_port))
                    yield ' | '
                    yield str((undefined(name='dscp_ranges') if l_1_dscp_ranges is missing else l_1_dscp_ranges))
                    yield ' |\n'
                l_1_application = l_1_src_prefix = l_1_dest_prefix = l_1_tcp_src_port = l_1_tcp_dest_port = l_1_udp_src_port = l_1_udp_dest_port = l_1_protocol_ranges = l_1_protocol = l_1_dscp_ranges = missing
            if t_5(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'l4_applications')):
                pass
                yield '\n#### Layer 4 Applications\n\n| Name | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set |\n| ---- | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ |\n'
                for l_1_application in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'l4_applications'), 'name'):
                    l_1_tcp_src_port = l_1_tcp_dest_port = l_1_udp_src_port = l_1_udp_dest_port = l_1_protocol_ranges = l_1_protocol = missing
                    _loop_vars = {}
                    pass
                    l_1_tcp_src_port = t_1(environment.getattr(l_1_application, 'tcp_src_port_set_name'), '-')
                    _loop_vars['tcp_src_port'] = l_1_tcp_src_port
                    l_1_tcp_dest_port = t_1(environment.getattr(l_1_application, 'tcp_dest_port_set_name'), '-')
                    _loop_vars['tcp_dest_port'] = l_1_tcp_dest_port
                    l_1_udp_src_port = t_1(environment.getattr(l_1_application, 'udp_src_port_set_name'), '-')
                    _loop_vars['udp_src_port'] = l_1_udp_src_port
                    l_1_udp_dest_port = t_1(environment.getattr(l_1_application, 'udp_dest_port_set_name'), '-')
                    _loop_vars['udp_dest_port'] = l_1_udp_dest_port
                    l_1_protocol_ranges = t_3(context.eval_ctx, t_1(environment.getattr(l_1_application, 'protocol_ranges'), ['-']), ', ')
                    _loop_vars['protocol_ranges'] = l_1_protocol_ranges
                    l_1_protocol = t_3(context.eval_ctx, t_1(environment.getattr(l_1_application, 'protocols'), ['-']), ', ')
                    _loop_vars['protocol'] = l_1_protocol
                    yield '| '
                    yield str(environment.getattr(l_1_application, 'name'))
                    yield ' | '
                    yield str((undefined(name='protocol') if l_1_protocol is missing else l_1_protocol))
                    yield ' | '
                    yield str((undefined(name='protocol_ranges') if l_1_protocol_ranges is missing else l_1_protocol_ranges))
                    yield ' | '
                    yield str((undefined(name='tcp_src_port') if l_1_tcp_src_port is missing else l_1_tcp_src_port))
                    yield ' | '
                    yield str((undefined(name='tcp_dest_port') if l_1_tcp_dest_port is missing else l_1_tcp_dest_port))
                    yield ' | '
                    yield str((undefined(name='udp_src_port') if l_1_udp_src_port is missing else l_1_udp_src_port))
                    yield ' | '
                    yield str((undefined(name='udp_dest_port') if l_1_udp_dest_port is missing else l_1_udp_dest_port))
                    yield ' |\n'
                l_1_application = l_1_tcp_src_port = l_1_tcp_dest_port = l_1_udp_src_port = l_1_udp_dest_port = l_1_protocol_ranges = l_1_protocol = missing
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'application_profiles')):
            pass
            yield '\n### Application Profiles\n'
            for l_1_application_profile in t_2(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'application_profiles'), 'name'):
                _loop_vars = {}
                pass
                yield '\n#### Application Profile Name '
                yield str(environment.getattr(l_1_application_profile, 'name'))
                yield '\n'
                if ((t_5(environment.getattr(l_1_application_profile, 'applications')) or t_5(environment.getattr(l_1_application_profile, 'categories'))) or t_5(environment.getattr(l_1_application_profile, 'application_transports'))):
                    pass
                    yield '\n| Type | Name | Service |\n| ---- | ---- | ------- |\n'
                    for l_2_application in t_2(t_2(environment.getattr(l_1_application_profile, 'applications'), 'service', strict=False), 'name'):
                        _loop_vars = {}
                        pass
                        yield '| application | '
                        yield str(environment.getattr(l_2_application, 'name'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_application, 'service'), '-'))
                        yield ' |\n'
                    l_2_application = missing
                    for l_2_category in t_2(t_2(environment.getattr(l_1_application_profile, 'categories'), 'service', strict=False), 'name'):
                        _loop_vars = {}
                        pass
                        yield '| category | '
                        yield str(environment.getattr(l_2_category, 'name'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_category, 'service'), '-'))
                        yield ' |\n'
                    l_2_category = missing
                    for l_2_transport in t_2(environment.getattr(l_1_application_profile, 'application_transports')):
                        _loop_vars = {}
                        pass
                        yield '| transport | '
                        yield str(l_2_transport)
                        yield ' | - |\n'
                    l_2_transport = missing
            l_1_application_profile = missing
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'categories')):
            pass
            yield '\n### Categories\n\n| Category | Application(Service) |\n| -------- | -------------------- |\n'
            for l_1_category in t_2(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'categories'), 'name'):
                l_1_apps = missing
                _loop_vars = {}
                pass
                l_1_apps = []
                _loop_vars['apps'] = l_1_apps
                for l_2_app_details in t_2(t_2(environment.getattr(l_1_category, 'applications'), 'service', strict=False), 'name'):
                    _loop_vars = {}
                    pass
                    if t_5(environment.getattr(l_2_app_details, 'service')):
                        pass
                        context.call(environment.getattr((undefined(name='apps') if l_1_apps is missing else l_1_apps), 'append'), (((environment.getattr(l_2_app_details, 'name') + '(') + t_1(environment.getattr(l_2_app_details, 'service'), '-')) + ')'), _loop_vars=_loop_vars)
                    else:
                        pass
                        context.call(environment.getattr((undefined(name='apps') if l_1_apps is missing else l_1_apps), 'append'), environment.getattr(l_2_app_details, 'name'), _loop_vars=_loop_vars)
                l_2_app_details = missing
                yield '| '
                yield str(environment.getattr(l_1_category, 'name'))
                yield ' | '
                yield str(t_3(context.eval_ctx, t_1((undefined(name='apps') if l_1_apps is missing else l_1_apps), []), '<br>'))
                yield ' |\n'
            l_1_category = l_1_apps = missing
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets')):
            pass
            yield '\n### Field Sets\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'l4_ports')):
                pass
                yield '\n#### L4 Port Sets\n\n| Name | Ports |\n| ---- | ----- |\n'
                for l_1_port_set in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'l4_ports'), 'name'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_port_set, 'name'))
                    yield ' | '
                    yield str(t_3(context.eval_ctx, t_2(t_1(environment.getattr(l_1_port_set, 'port_values'), ['-'])), ', '))
                    yield ' |\n'
                l_1_port_set = missing
            if t_5(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'ipv4_prefixes')):
                pass
                yield '\n#### IPv4 Prefix Sets\n\n| Name | Prefixes |\n| ---- | -------- |\n'
                for l_1_prefix_set in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'ipv4_prefixes'), 'name'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_prefix_set, 'name'))
                    yield ' | '
                    yield str(t_3(context.eval_ctx, t_4(environment, t_1(environment.getattr(l_1_prefix_set, 'prefix_values'), ['-'])), '<br>'))
                    yield ' |\n'
                l_1_prefix_set = missing
        yield '\n### Router Application-Traffic-Recognition Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/application-traffic-recognition.j2', 'documentation/application-traffic-recognition.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=42&10=45&13=48&19=51&20=55&21=57&22=59&23=61&24=63&25=65&26=67&27=69&28=71&29=74&32=95&38=98&39=102&40=104&41=106&42=108&43=110&44=112&45=115&49=130&52=133&54=137&55=139&59=142&60=146&62=151&63=155&65=160&66=164&71=168&77=171&78=175&79=177&80=180&81=182&83=185&86=188&89=193&92=196&98=199&99=203&102=208&108=211&109=215&117=221'