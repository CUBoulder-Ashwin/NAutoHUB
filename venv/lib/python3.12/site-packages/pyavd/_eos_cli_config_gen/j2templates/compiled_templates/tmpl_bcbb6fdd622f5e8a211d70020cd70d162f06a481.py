from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/application-traffic-recognition.j2'

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
        yield '!\napplication traffic recognition\n'
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications')):
            pass
            for l_1_application in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'ipv4_applications'), 'name'):
                _loop_vars = {}
                pass
                yield '   !\n   application ipv4 '
                yield str(environment.getattr(l_1_application, 'name'))
                yield '\n'
                if t_5(environment.getattr(l_1_application, 'src_prefix_set_name')):
                    pass
                    yield '      source prefix field-set '
                    yield str(environment.getattr(l_1_application, 'src_prefix_set_name'))
                    yield '\n'
                if t_5(environment.getattr(l_1_application, 'dest_prefix_set_name')):
                    pass
                    yield '      destination prefix field-set '
                    yield str(environment.getattr(l_1_application, 'dest_prefix_set_name'))
                    yield '\n'
                for l_2_protocol in t_2(environment.getattr(l_1_application, 'protocols')):
                    l_2_config = missing
                    _loop_vars = {}
                    pass
                    l_2_config = [l_2_protocol]
                    _loop_vars['config'] = l_2_config
                    if (l_2_protocol == 'tcp'):
                        pass
                        if t_5(environment.getattr(l_1_application, 'tcp_src_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('source port field-set ' + environment.getattr(l_1_application, 'tcp_src_port_set_name')), _loop_vars=_loop_vars)
                        if t_5(environment.getattr(l_1_application, 'tcp_dest_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('destination port field-set ' + environment.getattr(l_1_application, 'tcp_dest_port_set_name')), _loop_vars=_loop_vars)
                    if (l_2_protocol == 'udp'):
                        pass
                        if t_5(environment.getattr(l_1_application, 'udp_src_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('source port field-set ' + environment.getattr(l_1_application, 'udp_src_port_set_name')), _loop_vars=_loop_vars)
                        if t_5(environment.getattr(l_1_application, 'udp_dest_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('destination port field-set ' + environment.getattr(l_1_application, 'udp_dest_port_set_name')), _loop_vars=_loop_vars)
                    yield '      protocol '
                    yield str(t_3(context.eval_ctx, (undefined(name='config') if l_2_config is missing else l_2_config), ' '))
                    yield '\n'
                l_2_protocol = l_2_config = missing
                if t_5(environment.getattr(l_1_application, 'protocol_ranges')):
                    pass
                    yield '      protocol '
                    yield str(t_3(context.eval_ctx, t_2(environment.getattr(l_1_application, 'protocol_ranges'), 'name'), ', '))
                    yield '\n'
                if t_5(environment.getattr(l_1_application, 'dscp_ranges')):
                    pass
                    yield '      dscp '
                    yield str(t_3(context.eval_ctx, environment.getattr(l_1_application, 'dscp_ranges'), ' '))
                    yield '\n'
            l_1_application = missing
            for l_1_application in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'applications'), 'l4_applications'), 'name'):
                _loop_vars = {}
                pass
                yield '   !\n   application l4 '
                yield str(environment.getattr(l_1_application, 'name'))
                yield '\n'
                for l_2_protocol in t_2(environment.getattr(l_1_application, 'protocols')):
                    l_2_config = missing
                    _loop_vars = {}
                    pass
                    l_2_config = [l_2_protocol]
                    _loop_vars['config'] = l_2_config
                    if (l_2_protocol == 'tcp'):
                        pass
                        if t_5(environment.getattr(l_1_application, 'tcp_src_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('source port field-set ' + environment.getattr(l_1_application, 'tcp_src_port_set_name')), _loop_vars=_loop_vars)
                        if t_5(environment.getattr(l_1_application, 'tcp_dest_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('destination port field-set ' + environment.getattr(l_1_application, 'tcp_dest_port_set_name')), _loop_vars=_loop_vars)
                    if (l_2_protocol == 'udp'):
                        pass
                        if t_5(environment.getattr(l_1_application, 'udp_src_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('source port field-set ' + environment.getattr(l_1_application, 'udp_src_port_set_name')), _loop_vars=_loop_vars)
                        if t_5(environment.getattr(l_1_application, 'udp_dest_port_set_name')):
                            pass
                            context.call(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'append'), ('destination port field-set ' + environment.getattr(l_1_application, 'udp_dest_port_set_name')), _loop_vars=_loop_vars)
                    yield '      protocol '
                    yield str(t_3(context.eval_ctx, (undefined(name='config') if l_2_config is missing else l_2_config), ' '))
                    yield '\n'
                l_2_protocol = l_2_config = missing
                if t_5(environment.getattr(l_1_application, 'protocol_ranges')):
                    pass
                    yield '      protocol '
                    yield str(t_3(context.eval_ctx, t_2(environment.getattr(l_1_application, 'protocol_ranges'), 'name'), ', '))
                    yield '\n'
            l_1_application = missing
        for l_1_category in t_2(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'categories'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   category '
            yield str(environment.getattr(l_1_category, 'name'))
            yield '\n'
            for l_2_app_details in t_2(t_2(environment.getattr(l_1_category, 'applications'), 'name'), 'service', strict=False):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_2_app_details, 'service')):
                    pass
                    yield '      application '
                    yield str(environment.getattr(l_2_app_details, 'name'))
                    yield ' service '
                    yield str(environment.getattr(l_2_app_details, 'service'))
                    yield '\n'
                else:
                    pass
                    yield '      application '
                    yield str(environment.getattr(l_2_app_details, 'name'))
                    yield '\n'
            l_2_app_details = missing
        l_1_category = missing
        for l_1_application_profile in t_2(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'application_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   application-profile '
            yield str(environment.getattr(l_1_application_profile, 'name'))
            yield '\n'
            for l_2_application in t_2(t_2(environment.getattr(l_1_application_profile, 'applications'), 'name'), 'service', strict=False):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_2_application, 'service')):
                    pass
                    yield '      application '
                    yield str(environment.getattr(l_2_application, 'name'))
                    yield ' service '
                    yield str(environment.getattr(l_2_application, 'service'))
                    yield '\n'
                else:
                    pass
                    yield '      application '
                    yield str(environment.getattr(l_2_application, 'name'))
                    yield '\n'
            l_2_application = missing
            for l_2_transport in t_2(environment.getattr(l_1_application_profile, 'application_transports')):
                _loop_vars = {}
                pass
                yield '      application '
                yield str(l_2_transport)
                yield ' transport\n'
            l_2_transport = missing
            for l_2_category in t_2(environment.getattr(l_1_application_profile, 'categories')):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_2_category, 'service')):
                    pass
                    yield '      category '
                    yield str(environment.getattr(l_2_category, 'name'))
                    yield ' service '
                    yield str(environment.getattr(l_2_category, 'service'))
                    yield '\n'
                else:
                    pass
                    yield '      category '
                    yield str(environment.getattr(l_2_category, 'name'))
                    yield '\n'
            l_2_category = missing
        l_1_application_profile = missing
        if t_5(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets')):
            pass
            for l_1_prefix_set in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'ipv4_prefixes'), 'name'):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_prefix_set, 'name')):
                    pass
                    yield '   !\n   field-set ipv4 prefix '
                    yield str(environment.getattr(l_1_prefix_set, 'name'))
                    yield '\n'
                    if t_5(environment.getattr(l_1_prefix_set, 'prefix_values')):
                        pass
                        yield '      '
                        yield str(t_3(context.eval_ctx, t_4(environment, t_1(environment.getattr(l_1_prefix_set, 'prefix_values'), [])), ' '))
                        yield '\n'
            l_1_prefix_set = missing
            for l_1_port_set in t_2(environment.getattr(environment.getattr((undefined(name='application_traffic_recognition') if l_0_application_traffic_recognition is missing else l_0_application_traffic_recognition), 'field_sets'), 'l4_ports'), 'name'):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_port_set, 'name')):
                    pass
                    yield '   !\n   field-set l4-port '
                    yield str(environment.getattr(l_1_port_set, 'name'))
                    yield '\n'
                    if t_5(environment.getattr(l_1_port_set, 'port_values')):
                        pass
                        yield '      '
                        yield str(t_3(context.eval_ctx, t_2(environment.getattr(l_1_port_set, 'port_values')), ', '))
                        yield '\n'
            l_1_port_set = missing

blocks = {}
debug_info = '7=42&10=45&11=47&13=51&14=53&15=56&17=58&18=61&20=63&21=67&22=69&23=71&24=73&26=74&27=76&30=77&31=79&32=81&34=82&35=84&38=86&40=89&41=92&43=94&44=97&47=100&49=104&50=106&51=110&52=112&53=114&54=116&56=117&57=119&60=120&61=122&62=124&64=125&65=127&68=129&70=132&71=135&76=138&78=142&79=144&80=147&81=150&83=157&87=161&89=165&90=167&91=170&92=173&94=180&97=183&98=187&100=190&101=193&102=196&104=203&108=207&109=209&110=212&112=215&113=217&114=220&118=223&119=226&121=229&122=231&123=234'