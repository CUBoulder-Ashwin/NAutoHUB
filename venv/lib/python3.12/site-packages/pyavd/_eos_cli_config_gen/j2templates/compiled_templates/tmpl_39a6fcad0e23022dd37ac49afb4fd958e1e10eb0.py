from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/traffic-policies.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_traffic_policies = resolve('traffic_policies')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_5 = environment.filters['string']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'string' found.")
    try:
        t_6 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    try:
        t_7 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_6((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies)):
        pass
        yield '!\ntraffic-policies\n'
        l_1_loop = missing
        for l_1_field_set_port, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ports'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   field-set l4-port '
            yield str(environment.getattr(l_1_field_set_port, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_field_set_port, 'port_range')):
                pass
                yield '      '
                yield str(environment.getattr(l_1_field_set_port, 'port_range'))
                yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_field_set_port = missing
        l_1_loop = missing
        for l_1_field_set_ipv4, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv4'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   field-set ipv4 prefix '
            yield str(environment.getattr(l_1_field_set_ipv4, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_field_set_ipv4, 'prefixes')):
                pass
                yield '      '
                yield str(t_2(context.eval_ctx, t_1(environment.getattr(l_1_field_set_ipv4, 'prefixes')), ' '))
                yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_field_set_ipv4 = missing
        l_1_loop = missing
        for l_1_field_set_ipv6, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'field_sets'), 'ipv6'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   field-set ipv6 prefix '
            yield str(environment.getattr(l_1_field_set_ipv6, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_field_set_ipv6, 'prefixes')):
                pass
                yield '      '
                yield str(t_2(context.eval_ctx, t_1(environment.getattr(l_1_field_set_ipv6, 'prefixes')), ' '))
                yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_field_set_ipv6 = missing
        if t_6(environment.getattr(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'options'), 'counter_per_interface'), True):
            pass
            yield '   counter interface per-interface ingress\n   !\n'
        l_1_loop = missing
        for l_1_policy, l_1_loop in LoopContext(t_1(environment.getattr((undefined(name='traffic_policies') if l_0_traffic_policies is missing else l_0_traffic_policies), 'policies'), 'name'), undefined):
            l_1_namespace = resolve('namespace')
            l_1_transient_values = resolve('transient_values')
            _loop_vars = {}
            pass
            yield '   traffic-policy '
            yield str(environment.getattr(l_1_policy, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_policy, 'matches')):
                pass
                l_1_transient_values = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), _loop_vars=_loop_vars)
                _loop_vars['transient_values'] = l_1_transient_values
                if not isinstance(l_1_transient_values, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_transient_values['counters'] = []
                for l_2_match in environment.getattr(l_1_policy, 'matches'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')):
                        pass
                        context.call(environment.getattr(environment.getattr((undefined(name='transient_values') if l_1_transient_values is missing else l_1_transient_values), 'counters'), 'append'), t_5(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')), _loop_vars=_loop_vars)
                l_2_match = missing
                if (t_3(environment.getattr((undefined(name='transient_values') if l_1_transient_values is missing else l_1_transient_values), 'counters')) > 0):
                    pass
                    yield '      counter '
                    yield str(t_2(context.eval_ctx, t_1(environment.getattr((undefined(name='transient_values') if l_1_transient_values is missing else l_1_transient_values), 'counters')), ' '))
                    yield '\n      !\n'
                for l_2_match in environment.getattr(l_1_policy, 'matches'):
                    l_2_bgp_flag = resolve('bgp_flag')
                    _loop_vars = {}
                    pass
                    yield '      match '
                    yield str(environment.getattr(l_2_match, 'name'))
                    yield ' '
                    yield str(t_4(environment.getattr(l_2_match, 'type')))
                    yield '\n'
                    if t_6(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefixes')):
                        pass
                        yield '         source prefix '
                        yield str(t_2(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefixes')), ' '))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefix_lists')):
                        pass
                        yield '         source prefix field-set '
                        yield str(t_2(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_2_match, 'source'), 'prefix_lists')), ' '))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefixes')):
                        pass
                        yield '         destination prefix '
                        yield str(t_2(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefixes')), ' '))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefix_lists')):
                        pass
                        yield '         destination prefix field-set '
                        yield str(t_2(context.eval_ctx, t_1(environment.getattr(environment.getattr(l_2_match, 'destination'), 'prefix_lists')), ' '))
                        yield '\n'
                    if t_6(environment.getattr(l_2_match, 'protocols')):
                        pass
                        l_2_bgp_flag = True
                        _loop_vars['bgp_flag'] = l_2_bgp_flag
                        for l_3_protocol in environment.getattr(l_2_match, 'protocols'):
                            l_3_protocol_neighbors_cli = resolve('protocol_neighbors_cli')
                            l_3_bgp_flag = l_2_bgp_flag
                            l_3_protocol_cli = resolve('protocol_cli')
                            l_3_protocol_port_cli = resolve('protocol_port_cli')
                            l_3_protocol_field_cli = resolve('protocol_field_cli')
                            _loop_vars = {}
                            pass
                            if ((t_4(environment.getattr(l_3_protocol, 'protocol')) in ['neighbors', 'bgp']) and (undefined(name='bgp_flag') if l_3_bgp_flag is missing else l_3_bgp_flag)):
                                pass
                                if (t_4(environment.getattr(l_3_protocol, 'protocol')) == 'neighbors'):
                                    pass
                                    l_3_protocol_neighbors_cli = 'protocol neighbors bgp'
                                    _loop_vars['protocol_neighbors_cli'] = l_3_protocol_neighbors_cli
                                    if t_6(environment.getattr(l_3_protocol, 'enforce_gtsm'), True):
                                        pass
                                        l_3_protocol_neighbors_cli = str_join(((undefined(name='protocol_neighbors_cli') if l_3_protocol_neighbors_cli is missing else l_3_protocol_neighbors_cli), ' enforce ttl maximum-hops', ))
                                        _loop_vars['protocol_neighbors_cli'] = l_3_protocol_neighbors_cli
                                    yield '         '
                                    yield str((undefined(name='protocol_neighbors_cli') if l_3_protocol_neighbors_cli is missing else l_3_protocol_neighbors_cli))
                                    yield '\n'
                                else:
                                    pass
                                    yield '         protocol bgp\n'
                                break
                            else:
                                pass
                                l_3_bgp_flag = False
                                _loop_vars['bgp_flag'] = l_3_bgp_flag
                                l_3_protocol_cli = str_join(('protocol ', t_4(environment.getattr(l_3_protocol, 'protocol')), ))
                                _loop_vars['protocol_cli'] = l_3_protocol_cli
                                if (t_6(environment.getattr(l_3_protocol, 'flags')) and (t_4(environment.getattr(l_3_protocol, 'protocol')) == 'tcp')):
                                    pass
                                    for l_4_flag in environment.getattr(l_3_protocol, 'flags'):
                                        _loop_vars = {}
                                        pass
                                        yield '         '
                                        yield str((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli))
                                        yield ' flags '
                                        yield str(l_4_flag)
                                        yield '\n'
                                    l_4_flag = missing
                                if ((t_4(environment.getattr(l_3_protocol, 'protocol')) in ['tcp', 'udp']) and (((t_6(environment.getattr(l_3_protocol, 'src_port')) or t_6(environment.getattr(l_3_protocol, 'dst_port'))) or t_6(environment.getattr(l_3_protocol, 'src_field'))) or t_6(environment.getattr(l_3_protocol, 'dst_field')))):
                                    pass
                                    if (t_6(environment.getattr(l_3_protocol, 'src_port')) or t_6(environment.getattr(l_3_protocol, 'dst_port'))):
                                        pass
                                        l_3_protocol_port_cli = (undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli)
                                        _loop_vars['protocol_port_cli'] = l_3_protocol_port_cli
                                        if t_6(environment.getattr(l_3_protocol, 'src_port')):
                                            pass
                                            l_3_protocol_port_cli = str_join(((undefined(name='protocol_port_cli') if l_3_protocol_port_cli is missing else l_3_protocol_port_cli), ' source port ', environment.getattr(l_3_protocol, 'src_port'), ))
                                            _loop_vars['protocol_port_cli'] = l_3_protocol_port_cli
                                        if t_6(environment.getattr(l_3_protocol, 'dst_port')):
                                            pass
                                            l_3_protocol_port_cli = str_join(((undefined(name='protocol_port_cli') if l_3_protocol_port_cli is missing else l_3_protocol_port_cli), ' destination port ', environment.getattr(l_3_protocol, 'dst_port'), ))
                                            _loop_vars['protocol_port_cli'] = l_3_protocol_port_cli
                                        yield '         '
                                        yield str((undefined(name='protocol_port_cli') if l_3_protocol_port_cli is missing else l_3_protocol_port_cli))
                                        yield '\n'
                                    if (t_6(environment.getattr(l_3_protocol, 'src_field')) or t_6(environment.getattr(l_3_protocol, 'dst_field'))):
                                        pass
                                        l_3_protocol_field_cli = (undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli)
                                        _loop_vars['protocol_field_cli'] = l_3_protocol_field_cli
                                        if t_6(environment.getattr(l_3_protocol, 'src_field')):
                                            pass
                                            l_3_protocol_field_cli = str_join(((undefined(name='protocol_field_cli') if l_3_protocol_field_cli is missing else l_3_protocol_field_cli), ' source port field-set ', environment.getattr(l_3_protocol, 'src_field'), ))
                                            _loop_vars['protocol_field_cli'] = l_3_protocol_field_cli
                                        if t_6(environment.getattr(l_3_protocol, 'dst_field')):
                                            pass
                                            l_3_protocol_field_cli = str_join(((undefined(name='protocol_field_cli') if l_3_protocol_field_cli is missing else l_3_protocol_field_cli), ' destination port field-set ', environment.getattr(l_3_protocol, 'dst_field'), ))
                                            _loop_vars['protocol_field_cli'] = l_3_protocol_field_cli
                                        yield '         '
                                        yield str((undefined(name='protocol_field_cli') if l_3_protocol_field_cli is missing else l_3_protocol_field_cli))
                                        yield '\n'
                                elif (t_6(environment.getattr(l_3_protocol, 'icmp_type')) and (t_4(environment.getattr(l_3_protocol, 'protocol')) == 'icmp')):
                                    pass
                                    yield '         '
                                    yield str((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli))
                                    yield ' type '
                                    yield str(t_2(context.eval_ctx, t_1(environment.getattr(l_3_protocol, 'icmp_type')), ' '))
                                    yield ' code all\n'
                                else:
                                    pass
                                    yield '         '
                                    yield str((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli))
                                    yield '\n'
                        l_3_protocol = l_3_protocol_neighbors_cli = l_3_bgp_flag = l_3_protocol_cli = l_3_protocol_port_cli = l_3_protocol_field_cli = missing
                    if t_6(environment.getattr(environment.getattr(l_2_match, 'fragment'), 'offset')):
                        pass
                        yield '         fragment offset '
                        yield str(environment.getattr(environment.getattr(l_2_match, 'fragment'), 'offset'))
                        yield '\n'
                    elif t_7(environment.getattr(l_2_match, 'fragment')):
                        pass
                        yield '         fragment\n'
                    if t_6(environment.getattr(l_2_match, 'ttl')):
                        pass
                        yield '         ttl '
                        yield str(environment.getattr(l_2_match, 'ttl'))
                        yield '\n'
                    if (((t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')) or t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'traffic_class'))) or t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'dscp'))) or t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'drop'), True)):
                        pass
                        yield '         !\n         actions\n'
                        if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count')):
                            pass
                            yield '            count '
                            yield str(environment.getattr(environment.getattr(l_2_match, 'actions'), 'count'))
                            yield '\n'
                        if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'drop'), True):
                            pass
                            yield '            drop\n'
                            if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'log'), True):
                                pass
                                yield '            log\n'
                        if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'dscp')):
                            pass
                            yield '            set dscp '
                            yield str(environment.getattr(environment.getattr(l_2_match, 'actions'), 'dscp'))
                            yield '\n'
                        if t_6(environment.getattr(environment.getattr(l_2_match, 'actions'), 'traffic_class')):
                            pass
                            yield '            set traffic class '
                            yield str(environment.getattr(environment.getattr(l_2_match, 'actions'), 'traffic_class'))
                            yield '\n'
                    yield '      !\n'
                l_2_match = l_2_bgp_flag = missing
            yield '      match ipv4-all-default ipv4\n'
            if t_6(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4')):
                pass
                yield '         actions\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'count')):
                    pass
                    yield '            count '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'count'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'drop'), True):
                    pass
                    yield '            drop\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'log'), True):
                        pass
                        yield '            log\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'dscp')):
                    pass
                    yield '            set dscp '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'dscp'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'traffic_class')):
                    pass
                    yield '            set traffic class '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv4'), 'traffic_class'))
                    yield '\n'
            yield '      !\n      match ipv6-all-default ipv6\n'
            if t_6(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6')):
                pass
                yield '         actions\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'count')):
                    pass
                    yield '            count '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'count'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'drop'), True):
                    pass
                    yield '            drop\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'log'), True):
                        pass
                        yield '            log\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'dscp')):
                    pass
                    yield '            set dscp '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'dscp'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'traffic_class')):
                    pass
                    yield '            set traffic class '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_policy, 'default_actions'), 'ipv6'), 'traffic_class'))
                    yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_policy = l_1_namespace = l_1_transient_values = missing

blocks = {}
debug_info = '7=54&12=58&13=62&14=64&15=67&17=69&22=74&23=78&24=80&25=83&27=85&32=90&33=94&34=96&35=99&37=101&42=105&47=109&48=115&49=117&51=119&52=121&53=124&54=127&55=129&58=131&59=134&63=136&64=141&66=145&67=148&68=150&69=153&72=155&73=158&74=160&75=163&78=165&79=167&80=169&81=177&82=179&83=181&84=183&85=185&87=188&91=193&93=196&94=198&95=200&96=202&97=206&100=211&106=213&107=215&108=217&109=219&111=221&112=223&114=226&117=228&118=230&119=232&120=234&122=236&123=238&125=241&127=243&128=246&130=253&136=256&137=259&138=261&142=264&143=267&146=269&150=272&151=275&154=277&157=280&162=283&163=286&166=288&167=291&176=296&179=299&180=302&183=304&186=307&191=310&192=313&195=315&196=318&201=321&204=324&205=327&208=329&211=332&216=335&217=338&220=340&221=343&225=345'