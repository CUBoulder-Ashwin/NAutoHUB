from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-pim-sparse-mode.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_pim_sparse_mode = resolve('router_pim_sparse_mode')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode)):
        pass
        yield '!\nrouter pim sparse-mode\n'
        if t_2(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4')):
            pass
            yield '   ipv4\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4'), 'ssm_range')):
                pass
                yield '      ssm range '
                yield str(environment.getattr(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4'), 'ssm_range'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4'), 'bfd'), True):
                pass
                yield '      bfd\n'
            for l_1_rp_address in t_1(environment.getattr(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4'), 'rp_addresses'), 'address'):
                l_1_rp_options_cli = missing
                _loop_vars = {}
                pass
                l_1_rp_options_cli = ''
                _loop_vars['rp_options_cli'] = l_1_rp_options_cli
                if t_2(environment.getattr(l_1_rp_address, 'priority')):
                    pass
                    l_1_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli), ' priority ', environment.getattr(l_1_rp_address, 'priority'), ))
                    _loop_vars['rp_options_cli'] = l_1_rp_options_cli
                if t_2(environment.getattr(l_1_rp_address, 'hashmask')):
                    pass
                    l_1_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli), ' hashmask ', environment.getattr(l_1_rp_address, 'hashmask'), ))
                    _loop_vars['rp_options_cli'] = l_1_rp_options_cli
                if t_2(environment.getattr(l_1_rp_address, 'override'), True):
                    pass
                    l_1_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli), ' override', ))
                    _loop_vars['rp_options_cli'] = l_1_rp_options_cli
                if (t_2(environment.getattr(l_1_rp_address, 'groups')) or t_2(environment.getattr(l_1_rp_address, 'access_lists'))):
                    pass
                    if t_2(environment.getattr(l_1_rp_address, 'groups')):
                        pass
                        for l_2_group in t_1(environment.getattr(l_1_rp_address, 'groups')):
                            _loop_vars = {}
                            pass
                            yield '      rp address '
                            yield str(environment.getattr(l_1_rp_address, 'address'))
                            yield ' '
                            yield str(l_2_group)
                            yield str((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli))
                            yield '\n'
                        l_2_group = missing
                    if t_2(environment.getattr(l_1_rp_address, 'access_lists')):
                        pass
                        for l_2_access_list in t_1(environment.getattr(l_1_rp_address, 'access_lists')):
                            _loop_vars = {}
                            pass
                            yield '      rp address '
                            yield str(environment.getattr(l_1_rp_address, 'address'))
                            yield ' access-list '
                            yield str(l_2_access_list)
                            yield str((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli))
                            yield '\n'
                        l_2_access_list = missing
                else:
                    pass
                    yield '      rp address '
                    yield str(environment.getattr(l_1_rp_address, 'address'))
                    yield str((undefined(name='rp_options_cli') if l_1_rp_options_cli is missing else l_1_rp_options_cli))
                    yield '\n'
            l_1_rp_address = l_1_rp_options_cli = missing
            for l_1_anycast_rp in t_1(environment.getattr(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'ipv4'), 'anycast_rps'), 'address'):
                _loop_vars = {}
                pass
                for l_2_other_anycast_rp_address in t_1(environment.getattr(l_1_anycast_rp, 'other_anycast_rp_addresses'), 'address'):
                    l_2_other_anycast_rp_addresses_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_other_anycast_rp_addresses_cli = str_join(('anycast-rp ', environment.getattr(l_1_anycast_rp, 'address'), ' ', environment.getattr(l_2_other_anycast_rp_address, 'address'), ))
                    _loop_vars['other_anycast_rp_addresses_cli'] = l_2_other_anycast_rp_addresses_cli
                    if t_2(environment.getattr(l_2_other_anycast_rp_address, 'register_count')):
                        pass
                        l_2_other_anycast_rp_addresses_cli = str_join(((undefined(name='other_anycast_rp_addresses_cli') if l_2_other_anycast_rp_addresses_cli is missing else l_2_other_anycast_rp_addresses_cli), ' register-count ', environment.getattr(l_2_other_anycast_rp_address, 'register_count'), ))
                        _loop_vars['other_anycast_rp_addresses_cli'] = l_2_other_anycast_rp_addresses_cli
                    yield '      '
                    yield str((undefined(name='other_anycast_rp_addresses_cli') if l_2_other_anycast_rp_addresses_cli is missing else l_2_other_anycast_rp_addresses_cli))
                    yield '\n'
                l_2_other_anycast_rp_address = l_2_other_anycast_rp_addresses_cli = missing
            l_1_anycast_rp = missing
        for l_1_vrf in t_1(environment.getattr((undefined(name='router_pim_sparse_mode') if l_0_router_pim_sparse_mode is missing else l_0_router_pim_sparse_mode), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_vrf, 'ipv4')):
                pass
                yield '      ipv4\n'
                if t_2(environment.getattr(environment.getattr(l_1_vrf, 'ipv4'), 'bfd'), True):
                    pass
                    yield '         bfd\n'
                for l_2_rp_address in t_1(environment.getattr(environment.getattr(l_1_vrf, 'ipv4'), 'rp_addresses'), 'address'):
                    l_2_rp_options_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_rp_options_cli = ''
                    _loop_vars['rp_options_cli'] = l_2_rp_options_cli
                    if t_2(environment.getattr(l_2_rp_address, 'priority')):
                        pass
                        l_2_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli), ' priority ', environment.getattr(l_2_rp_address, 'priority'), ))
                        _loop_vars['rp_options_cli'] = l_2_rp_options_cli
                    if t_2(environment.getattr(l_2_rp_address, 'hashmask')):
                        pass
                        l_2_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli), ' hashmask ', environment.getattr(l_2_rp_address, 'hashmask'), ))
                        _loop_vars['rp_options_cli'] = l_2_rp_options_cli
                    if t_2(environment.getattr(l_2_rp_address, 'override'), True):
                        pass
                        l_2_rp_options_cli = str_join(((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli), ' override', ))
                        _loop_vars['rp_options_cli'] = l_2_rp_options_cli
                    if (t_2(environment.getattr(l_2_rp_address, 'groups')) or t_2(environment.getattr(l_2_rp_address, 'access_lists'))):
                        pass
                        if t_2(environment.getattr(l_2_rp_address, 'groups')):
                            pass
                            for l_3_group in t_1(environment.getattr(l_2_rp_address, 'groups')):
                                _loop_vars = {}
                                pass
                                yield '         rp address '
                                yield str(environment.getattr(l_2_rp_address, 'address'))
                                yield ' '
                                yield str(l_3_group)
                                yield str((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli))
                                yield '\n'
                            l_3_group = missing
                        if t_2(environment.getattr(l_2_rp_address, 'access_lists')):
                            pass
                            for l_3_access_list in t_1(environment.getattr(l_2_rp_address, 'access_lists')):
                                _loop_vars = {}
                                pass
                                yield '         rp address '
                                yield str(environment.getattr(l_2_rp_address, 'address'))
                                yield ' access-list '
                                yield str(l_3_access_list)
                                yield str((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli))
                                yield '\n'
                            l_3_access_list = missing
                    else:
                        pass
                        yield '         rp address '
                        yield str(environment.getattr(l_2_rp_address, 'address'))
                        yield str((undefined(name='rp_options_cli') if l_2_rp_options_cli is missing else l_2_rp_options_cli))
                        yield '\n'
                l_2_rp_address = l_2_rp_options_cli = missing
        l_1_vrf = missing

blocks = {}
debug_info = '7=24&10=27&12=30&13=33&15=35&18=38&19=42&20=44&21=46&23=48&24=50&26=52&27=54&29=56&30=58&31=60&32=64&35=70&36=72&37=76&41=85&44=89&45=92&46=96&47=98&48=100&50=103&54=107&56=111&57=113&59=116&62=119&63=123&64=125&65=127&67=129&68=131&70=133&71=135&73=137&74=139&75=141&76=145&79=151&80=153&81=157&85=166'