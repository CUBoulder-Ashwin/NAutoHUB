from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-segment-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_segment_security = resolve('router_segment_security')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security)):
        pass
        yield '!\nrouter segment-security\n'
        if t_3(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'enabled'), True):
            pass
            yield '   no shutdown\n   !\n'
        for l_1_policy in t_2(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'policies'), 'name'):
            _loop_vars = {}
            pass
            yield '   policy '
            yield str(environment.getattr(l_1_policy, 'name'))
            yield '\n'
            for l_2_sequence in t_2(environment.getattr(l_1_policy, 'sequence_numbers'), 'sequence'):
                l_2_eos_cli = resolve('eos_cli')
                _loop_vars = {}
                pass
                if ((t_3(environment.getattr(l_2_sequence, 'sequence')) and t_3(environment.getattr(l_2_sequence, 'action'))) and t_3(environment.getattr(l_2_sequence, 'application'))):
                    pass
                    l_2_eos_cli = environment.getattr(l_2_sequence, 'action')
                    _loop_vars['eos_cli'] = l_2_eos_cli
                    if (environment.getattr(l_2_sequence, 'action') == 'redirect'):
                        pass
                        if t_3(environment.getattr(l_2_sequence, 'next_hop')):
                            pass
                            l_2_eos_cli = str_join(((undefined(name='eos_cli') if l_2_eos_cli is missing else l_2_eos_cli), ' next-hop ', environment.getattr(l_2_sequence, 'next_hop'), ))
                            _loop_vars['eos_cli'] = l_2_eos_cli
                        else:
                            pass
                            continue
                    if t_1(environment.getattr(l_2_sequence, 'stateless'), True):
                        pass
                        l_2_eos_cli = str_join(((undefined(name='eos_cli') if l_2_eos_cli is missing else l_2_eos_cli), ' stateless', ))
                        _loop_vars['eos_cli'] = l_2_eos_cli
                    if t_3(environment.getattr(l_2_sequence, 'log'), True):
                        pass
                        l_2_eos_cli = str_join(((undefined(name='eos_cli') if l_2_eos_cli is missing else l_2_eos_cli), ' log', ))
                        _loop_vars['eos_cli'] = l_2_eos_cli
                    yield '      '
                    yield str(environment.getattr(l_2_sequence, 'sequence'))
                    yield ' application '
                    yield str(environment.getattr(l_2_sequence, 'application'))
                    yield ' action '
                    yield str((undefined(name='eos_cli') if l_2_eos_cli is missing else l_2_eos_cli))
                    yield '\n'
            l_2_sequence = l_2_eos_cli = missing
            yield '   !\n'
        l_1_policy = missing
        l_1_loop = missing
        for l_1_vrf, l_1_loop in LoopContext(t_2(environment.getattr((undefined(name='router_segment_security') if l_0_router_segment_security is missing else l_0_router_segment_security), 'vrfs'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            l_2_loop = missing
            for l_2_segment, l_2_loop in LoopContext(t_2(environment.getattr(l_1_vrf, 'segments'), 'name'), undefined):
                _loop_vars = {}
                pass
                yield '      segment '
                yield str(environment.getattr(l_2_segment, 'name'))
                yield '\n         definition\n'
                for l_3_interface in t_2(environment.getattr(environment.getattr(l_2_segment, 'definition'), 'interfaces')):
                    _loop_vars = {}
                    pass
                    yield '            match interface '
                    yield str(l_3_interface)
                    yield '\n'
                l_3_interface = missing
                if t_3(environment.getattr(environment.getattr(l_2_segment, 'definition'), 'match_lists')):
                    pass
                    for l_3_match_list in environment.getattr(environment.getattr(l_2_segment, 'definition'), 'match_lists'):
                        l_3_host_cli = resolve('host_cli')
                        _loop_vars = {}
                        pass
                        if (t_3(environment.getattr(l_3_match_list, 'address_family')) and (t_3(environment.getattr(l_3_match_list, 'prefix')) or t_3(environment.getattr(l_3_match_list, 'covered_prefix_list')))):
                            pass
                            if t_3(environment.getattr(l_3_match_list, 'prefix')):
                                pass
                                l_3_host_cli = str_join(('match prefix-', environment.getattr(l_3_match_list, 'address_family'), ' ', environment.getattr(l_3_match_list, 'prefix'), ))
                                _loop_vars['host_cli'] = l_3_host_cli
                            elif t_3(environment.getattr(l_3_match_list, 'covered_prefix_list')):
                                pass
                                l_3_host_cli = str_join(('match covered prefix-list ', environment.getattr(l_3_match_list, 'address_family'), ' ', environment.getattr(l_3_match_list, 'covered_prefix_list'), ))
                                _loop_vars['host_cli'] = l_3_host_cli
                            yield '            '
                            yield str((undefined(name='host_cli') if l_3_host_cli is missing else l_3_host_cli))
                            yield '\n'
                    l_3_match_list = l_3_host_cli = missing
                if t_3(environment.getattr(l_2_segment, 'policies')):
                    pass
                    yield '         !\n         policies\n'
                    for l_3_policy in t_2(environment.getattr(l_2_segment, 'policies'), 'from'):
                        _loop_vars = {}
                        pass
                        if (t_3(environment.getattr(l_3_policy, 'from')) and t_3(environment.getattr(l_3_policy, 'policy'))):
                            pass
                            yield '            from '
                            yield str(environment.getattr(l_3_policy, 'from'))
                            yield ' policy '
                            yield str(environment.getattr(l_3_policy, 'policy'))
                            yield '\n'
                    l_3_policy = missing
                    if t_3(environment.getattr(l_2_segment, 'fallback_policy')):
                        pass
                        yield '            fallback policy '
                        yield str(environment.getattr(l_2_segment, 'fallback_policy'))
                        yield '\n'
                if (not environment.getattr(l_2_loop, 'last')):
                    pass
                    yield '      !\n'
            l_2_loop = l_2_segment = missing
            yield '   !\n'
        l_1_loop = l_1_vrf = missing

blocks = {}
debug_info = '7=30&10=33&14=36&15=40&16=42&17=46&18=48&19=50&20=52&21=54&23=58&26=59&27=61&29=63&30=65&32=68&37=78&38=82&39=85&40=89&42=91&43=95&45=98&46=100&47=104&48=106&49=108&50=110&51=112&53=115&57=118&60=121&61=124&62=127&65=132&66=135&69=137'