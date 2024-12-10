from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/traffic-policies.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_traffic_policies = resolve('traffic_policies')
    l_0_traffic_policy_interfaces = resolve('traffic_policy_interfaces')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
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
        t_5 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_6 = environment.filters['map']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'map' found.")
    try:
        t_7 = environment.filters['string']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No filter named 'string' found.")
    try:
        t_8 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_8((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies)):
        pass
        yield '\n### Traffic Policies information\n'
        if t_8(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets')):
            pass
            if t_8(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv4')):
                pass
                yield '\n#### IPv4 Field Sets\n\n| Field Set Name | IPv4 Prefixes |\n| -------------- | ------------- |\n'
                for l_1_field_set_ipv4 in t_2(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv4'), 'name'):
                    l_1_value = resolve('value')
                    _loop_vars = {}
                    pass
                    if t_8(environment.getattr(l_1_field_set_ipv4, 'prefixes')):
                        pass
                        l_1_value = t_3(context.eval_ctx, t_2(environment.getattr(l_1_field_set_ipv4, 'prefixes')), '<br/>')
                        _loop_vars['value'] = l_1_value
                    yield '| '
                    yield str(environment.getattr(l_1_field_set_ipv4, 'name'))
                    yield ' | '
                    yield str(t_1((undefined(name='value') if l_1_value is missing else l_1_value), '-'))
                    yield ' |\n'
                l_1_field_set_ipv4 = l_1_value = missing
            if t_8(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv6')):
                pass
                yield '\n#### IPv6 Field Sets\n\n| Field Set Name | IPv6 Prefixes |\n| -------------- | ------------- |\n'
                for l_1_field_set_ipv6 in t_2(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv6'), 'name'):
                    l_1_value = resolve('value')
                    _loop_vars = {}
                    pass
                    if t_8(environment.getattr(l_1_field_set_ipv6, 'prefixes')):
                        pass
                        l_1_value = t_3(context.eval_ctx, t_2(environment.getattr(l_1_field_set_ipv6, 'prefixes')), '<br/>')
                        _loop_vars['value'] = l_1_value
                    yield '| '
                    yield str(environment.getattr(l_1_field_set_ipv6, 'name'))
                    yield ' | '
                    yield str(t_1((undefined(name='value') if l_1_value is missing else l_1_value), '-'))
                    yield ' |\n'
                l_1_field_set_ipv6 = l_1_value = missing
            if t_8(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ports')):
                pass
                yield '\n#### L4 Port Field Sets\n\n| Field Set Name | L4 Ports |\n| -------------- | -------- |\n'
                for l_1_field_set_port in t_2(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ports'), 'name'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_field_set_port, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_field_set_port, 'port_range'), '-'))
                    yield ' |\n'
                l_1_field_set_port = missing
        if t_8(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'policies')):
            pass
            yield '\n#### Traffic Policies\n'
            for l_1_policy in t_2(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'policies'), 'name'):
                _loop_vars = {}
                pass
                yield '\n##### '
                yield str(environment.getattr(l_1_policy, 'name'))
                yield '\n'
                if t_8(environment.getattr(l_1_policy, 'matches')):
                    pass
                    yield '\n| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Source Field(s) | Destination port(s) | Destination Field(s) | Action |\n| --------- | ---- | ------- | ------------ | -------- | -------------- | --------------- | ------------------- | -------------------- | ------ |\n'
                    for l_2_match in t_2(environment.getattr(l_1_policy, 'matches'), 'name'):
                        l_2_namespace = resolve('namespace')
                        l_2_row = missing
                        _loop_vars = {}
                        pass
                        l_2_row = context.call((undefined(name='namespace') if l_2_namespace is missing else l_2_namespace), _loop_vars=_loop_vars)
                        _loop_vars['row'] = l_2_row
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['match_set'] = environment.getattr(l_2_match, 'name')
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['type'] = t_5(environment.getattr(l_2_match, 'type'))
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['src_net'] = ''
                        if t_8(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefix_lists')):
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_net'] = t_3(context.eval_ctx, t_2(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefix_lists')), '<br/>')
                        elif t_8(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefixes')):
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_net'] = t_3(context.eval_ctx, t_2(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefixes')), '<br/>')
                        else:
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_net'] = 'any'
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['dst_net'] = ''
                        if t_8(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefix_lists')):
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_net'] = t_3(context.eval_ctx, t_2(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefix_lists')), '<br/>')
                        elif t_8(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefixes')):
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_net'] = t_3(context.eval_ctx, t_2(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefixes')), '<br/>')
                        else:
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_net'] = 'any'
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['protocols'] = ''
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['src_port'] = []
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['dst_port'] = []
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['src_field'] = []
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['dst_field'] = []
                        if t_8(environment.getattr(l_2_match, 'protocols')):
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['protocols'] = t_3(context.eval_ctx, t_6(context, environment.getattr(l_2_match, 'protocols'), attribute='protocol'), '<br/>')
                            for l_3_protocol in environment.getattr(l_2_match, 'protocols'):
                                _loop_vars = {}
                                pass
                                if (t_5(environment.getattr(l_3_protocol, 'protocol')) in ['tcp', 'udp']):
                                    pass
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_port'), 'append'), t_1(environment.getattr(l_3_protocol, 'src_port'), 'any'), _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_field'), 'append'), t_1(environment.getattr(l_3_protocol, 'src_field'), '-'), _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_port'), 'append'), t_1(environment.getattr(l_3_protocol, 'dst_port'), 'any'), _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_field'), 'append'), t_1(environment.getattr(l_3_protocol, 'dst_field'), '-'), _loop_vars=_loop_vars)
                                else:
                                    pass
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_port'), 'append'), '-', _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_field'), 'append'), '-', _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_port'), 'append'), '-', _loop_vars=_loop_vars)
                                    context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_field'), 'append'), '-', _loop_vars=_loop_vars)
                            l_3_protocol = missing
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_port'] = t_3(context.eval_ctx, environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_port'), '<br/>')
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_port'] = t_3(context.eval_ctx, environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_port'), '<br/>')
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_field'] = t_3(context.eval_ctx, environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_field'), '<br/>')
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_field'] = t_3(context.eval_ctx, environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_field'), '<br/>')
                        else:
                            pass
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['protocols'] = '-'
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_port'] = '-'
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['src_field'] = '-'
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_port'] = '-'
                            if not isinstance(l_2_row, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_row['dst_field'] = '-'
                        if not isinstance(l_2_row, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_row['actions'] = []
                        if t_8(environment.getattr(l_2_match, 'actions')):
                            pass
                            if t_8(environment.getattr(environment.getattr(l_2_match, 'actions'), 'drop'), True):
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), 'action: DROP', _loop_vars=_loop_vars)
                            else:
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), 'action: PASS', _loop_vars=_loop_vars)
                            if t_8(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')):
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), ('counter: ' + environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')), _loop_vars=_loop_vars)
                            if t_8(environment.getattr(environment.getattr(l_2_match, 'actions'), 'log'), True):
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), 'logging', _loop_vars=_loop_vars)
                            if t_8(environment.getattr(environment.getattr(l_2_match, 'actions'), 'dscp')):
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), ('dscp marking: ' + t_7(environment.getattr(environment.getattr(l_2_match, 'actions'), 'dscp'))), _loop_vars=_loop_vars)
                            if t_8(environment.getattr(environment.getattr(l_2_match, 'actions'), 'traffic_class')):
                                pass
                                context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), ('traffic-class: ' + t_7(environment.getattr(environment.getattr(l_2_match, 'actions'), 'traffic_class'))), _loop_vars=_loop_vars)
                        else:
                            pass
                            context.call(environment.getattr(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), 'append'), 'default action: PASS', _loop_vars=_loop_vars)
                        yield '| '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'match_set'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'type'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_net'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_net'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'protocols'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_port'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'src_field'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_port'))
                        yield ' | '
                        yield str(environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'dst_field'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, environment.getattr((undefined(name='row') if l_2_row is missing else l_2_row), 'actions'), '<br/>'))
                        yield ' |\n'
                    l_2_match = l_2_namespace = l_2_row = missing
            l_1_policy = missing
        l_0_traffic_policy_interfaces = []
        context.vars['traffic_policy_interfaces'] = l_0_traffic_policy_interfaces
        context.exported_vars.add('traffic_policy_interfaces')
        for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_8(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'input')) or t_8(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'output'))):
                pass
                context.call(environment.getattr((undefined(name='traffic_policy_interfaces') if l_0_traffic_policy_interfaces is missing else l_0_traffic_policy_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        for l_1_port_channel_interface in t_2((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_8(environment.getattr(environment.getattr(l_1_port_channel_interface, 'traffic_policy'), 'input')) or t_8(environment.getattr(environment.getattr(l_1_port_channel_interface, 'traffic_policy'), 'output'))):
                pass
                context.call(environment.getattr((undefined(name='traffic_policy_interfaces') if l_0_traffic_policy_interfaces is missing else l_0_traffic_policy_interfaces), 'append'), l_1_port_channel_interface, _loop_vars=_loop_vars)
        l_1_port_channel_interface = missing
        if (t_4((undefined(name='traffic_policy_interfaces') if l_0_traffic_policy_interfaces is missing else l_0_traffic_policy_interfaces)) > 0):
            pass
            yield '\n##### Traffic-Policy Interfaces\n\n| Interface | Input Traffic-Policy | Output Traffic-Policy |\n| --------- | -------------------- | --------------------- |\n'
            for l_1_interface in (undefined(name='traffic_policy_interfaces') if l_0_traffic_policy_interfaces is missing else l_0_traffic_policy_interfaces):
                l_1_row_in_policy = l_1_row_out_policy = missing
                _loop_vars = {}
                pass
                l_1_row_in_policy = t_1(environment.getattr(environment.getattr(l_1_interface, 'traffic_policy'), 'input'), '-')
                _loop_vars['row_in_policy'] = l_1_row_in_policy
                l_1_row_out_policy = t_1(environment.getattr(environment.getattr(l_1_interface, 'traffic_policy'), 'output'), '-')
                _loop_vars['row_out_policy'] = l_1_row_out_policy
                yield '| '
                yield str(environment.getattr(l_1_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_in_policy') if l_1_row_in_policy is missing else l_1_row_in_policy))
                yield ' | '
                yield str((undefined(name='row_out_policy') if l_1_row_out_policy is missing else l_1_row_out_policy))
                yield ' |\n'
            l_1_interface = l_1_row_in_policy = l_1_row_out_policy = missing
        yield '\n#### Traffic Policies Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/traffic-policies.j2', 'documentation/traffic-policies.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'traffic_policy_interfaces': l_0_traffic_policy_interfaces})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=63&10=66&11=68&17=71&18=75&19=77&21=80&24=85&30=88&31=92&32=94&34=97&37=102&43=105&44=109&48=114&51=117&53=121&54=123&58=126&59=131&60=133&61=136&63=139&64=142&65=144&66=147&67=149&69=154&72=157&73=160&74=162&75=165&76=167&78=172&81=175&82=178&83=181&84=184&85=187&86=190&87=192&89=195&90=198&91=200&92=201&93=202&94=203&96=206&97=207&98=208&99=209&102=211&103=214&104=217&105=220&107=225&108=228&109=231&110=234&111=237&114=240&115=243&116=245&117=247&119=250&121=251&122=253&124=254&125=256&127=257&128=259&130=260&131=262&134=265&137=267&143=289&144=292&145=295&146=297&149=299&150=302&151=304&154=306&160=309&161=313&162=315&163=318&170=326'