from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-ospf.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_ospf = resolve('router_ospf')
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
    try:
        t_4 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    for l_1_process_id in t_1(environment.getattr((undefined(name='router_ospf') if l_0_router_ospf is missing else l_0_router_ospf), 'process_ids'), 'id'):
        l_1_redistribute_bgp_cli = resolve('redistribute_bgp_cli')
        l_1_redistribute_connected_cli = resolve('redistribute_connected_cli')
        l_1_redistribute_static_cli = resolve('redistribute_static_cli')
        l_1_timer_ospf_spf_delay = resolve('timer_ospf_spf_delay')
        l_1_timer_ospf_lsa_tx = resolve('timer_ospf_lsa_tx')
        l_1_max_metric_router_lsa_cli = resolve('max_metric_router_lsa_cli')
        l_1_default_information_originate_cli = resolve('default_information_originate_cli')
        l_1_graceful_restart_cli = resolve('graceful_restart_cli')
        _loop_vars = {}
        pass
        yield '!\n'
        if t_3(environment.getattr(l_1_process_id, 'vrf')):
            pass
            yield 'router ospf '
            yield str(environment.getattr(l_1_process_id, 'id'))
            yield ' vrf '
            yield str(environment.getattr(l_1_process_id, 'vrf'))
            yield '\n'
        else:
            pass
            yield 'router ospf '
            yield str(environment.getattr(l_1_process_id, 'id'))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'router_id')):
            pass
            yield '   router-id '
            yield str(environment.getattr(l_1_process_id, 'router_id'))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'auto_cost_reference_bandwidth')):
            pass
            yield '   auto-cost reference-bandwidth '
            yield str(environment.getattr(l_1_process_id, 'auto_cost_reference_bandwidth'))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'bfd_enable'), True):
            pass
            yield '   bfd default\n'
        if t_3(environment.getattr(l_1_process_id, 'bfd_adjacency_state_any'), True):
            pass
            yield '   bfd adjacency state any\n'
        if t_3(environment.getattr(l_1_process_id, 'distance')):
            pass
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'intra_area')):
                pass
                yield '   distance ospf intra-area '
                yield str(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'intra_area'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'external')):
                pass
                yield '   distance ospf external '
                yield str(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'external'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'inter_area')):
                pass
                yield '   distance ospf inter-area '
                yield str(environment.getattr(environment.getattr(l_1_process_id, 'distance'), 'inter_area'))
                yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'passive_interface_default'), True):
            pass
            yield '   passive-interface default\n'
        if t_3(environment.getattr(l_1_process_id, 'no_passive_interfaces')):
            pass
            for l_2_interface in t_1(environment.getattr(l_1_process_id, 'no_passive_interfaces')):
                _loop_vars = {}
                pass
                yield '   no passive-interface '
                yield str(l_2_interface)
                yield '\n'
            l_2_interface = missing
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'bgp'), 'enabled'), True):
            pass
            l_1_redistribute_bgp_cli = 'redistribute bgp'
            _loop_vars['redistribute_bgp_cli'] = l_1_redistribute_bgp_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'bgp'), 'include_leaked'), True):
                pass
                l_1_redistribute_bgp_cli = str_join(((undefined(name='redistribute_bgp_cli') if l_1_redistribute_bgp_cli is missing else l_1_redistribute_bgp_cli), ' include leaked', ))
                _loop_vars['redistribute_bgp_cli'] = l_1_redistribute_bgp_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'bgp'), 'route_map')):
                pass
                l_1_redistribute_bgp_cli = str_join(((undefined(name='redistribute_bgp_cli') if l_1_redistribute_bgp_cli is missing else l_1_redistribute_bgp_cli), ' route-map ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'bgp'), 'route_map'), ))
                _loop_vars['redistribute_bgp_cli'] = l_1_redistribute_bgp_cli
            yield '   '
            yield str((undefined(name='redistribute_bgp_cli') if l_1_redistribute_bgp_cli is missing else l_1_redistribute_bgp_cli))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'connected'), 'enabled'), True):
            pass
            l_1_redistribute_connected_cli = 'redistribute connected'
            _loop_vars['redistribute_connected_cli'] = l_1_redistribute_connected_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'connected'), 'include_leaked'), True):
                pass
                l_1_redistribute_connected_cli = str_join(((undefined(name='redistribute_connected_cli') if l_1_redistribute_connected_cli is missing else l_1_redistribute_connected_cli), ' include leaked', ))
                _loop_vars['redistribute_connected_cli'] = l_1_redistribute_connected_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'connected'), 'route_map')):
                pass
                l_1_redistribute_connected_cli = str_join(((undefined(name='redistribute_connected_cli') if l_1_redistribute_connected_cli is missing else l_1_redistribute_connected_cli), ' route-map ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'connected'), 'route_map'), ))
                _loop_vars['redistribute_connected_cli'] = l_1_redistribute_connected_cli
            yield '   '
            yield str((undefined(name='redistribute_connected_cli') if l_1_redistribute_connected_cli is missing else l_1_redistribute_connected_cli))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'static'), 'enabled'), True):
            pass
            l_1_redistribute_static_cli = 'redistribute static'
            _loop_vars['redistribute_static_cli'] = l_1_redistribute_static_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'static'), 'include_leaked'), True):
                pass
                l_1_redistribute_static_cli = str_join(((undefined(name='redistribute_static_cli') if l_1_redistribute_static_cli is missing else l_1_redistribute_static_cli), ' include leaked', ))
                _loop_vars['redistribute_static_cli'] = l_1_redistribute_static_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'static'), 'route_map')):
                pass
                l_1_redistribute_static_cli = str_join(((undefined(name='redistribute_static_cli') if l_1_redistribute_static_cli is missing else l_1_redistribute_static_cli), ' route-map ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'redistribute'), 'static'), 'route_map'), ))
                _loop_vars['redistribute_static_cli'] = l_1_redistribute_static_cli
            yield '   '
            yield str((undefined(name='redistribute_static_cli') if l_1_redistribute_static_cli is missing else l_1_redistribute_static_cli))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_process_id, 'distribute_list_in'), 'route_map')):
            pass
            yield '   distribute-list route-map '
            yield str(environment.getattr(environment.getattr(l_1_process_id, 'distribute_list_in'), 'route_map'))
            yield ' in\n'
        for l_2_area in t_1(environment.getattr(l_1_process_id, 'areas'), 'id'):
            l_2_stub_area_cli = resolve('stub_area_cli')
            l_2_namespace = resolve('namespace')
            l_2_ns = resolve('ns')
            l_2_nssa_area_cli = resolve('nssa_area_cli')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_2_area, 'type'), 'stub'):
                pass
                l_2_stub_area_cli = str_join(('area ', environment.getattr(l_2_area, 'id'), ' stub', ))
                _loop_vars['stub_area_cli'] = l_2_stub_area_cli
                if t_3(environment.getattr(l_2_area, 'no_summary'), True):
                    pass
                    l_2_stub_area_cli = str_join(((undefined(name='stub_area_cli') if l_2_stub_area_cli is missing else l_2_stub_area_cli), ' no-summary', ))
                    _loop_vars['stub_area_cli'] = l_2_stub_area_cli
                yield '   '
                yield str((undefined(name='stub_area_cli') if l_2_stub_area_cli is missing else l_2_stub_area_cli))
                yield '\n'
            if t_3(environment.getattr(l_2_area, 'type'), 'nssa'):
                pass
                l_2_ns = context.call((undefined(name='namespace') if l_2_namespace is missing else l_2_namespace), print_nssa=True, _loop_vars=_loop_vars)
                _loop_vars['ns'] = l_2_ns
                l_2_nssa_area_cli = str_join(('area ', environment.getattr(l_2_area, 'id'), ' nssa', ))
                _loop_vars['nssa_area_cli'] = l_2_nssa_area_cli
                if t_3(environment.getattr(l_2_area, 'no_summary'), True):
                    pass
                    if not isinstance(l_2_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_ns['print_nssa'] = False
                    yield '   '
                    yield str((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli))
                    yield ' no-summary\n'
                if t_4(environment.getattr(l_2_area, 'default_information_originate')):
                    pass
                    if not isinstance(l_2_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_ns['print_nssa'] = True
                    l_2_nssa_area_cli = str_join(((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli), ' default-information-originate', ))
                    _loop_vars['nssa_area_cli'] = l_2_nssa_area_cli
                    if t_3(environment.getattr(environment.getattr(l_2_area, 'default_information_originate'), 'metric')):
                        pass
                        l_2_nssa_area_cli = str_join(((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli), ' metric ', environment.getattr(environment.getattr(l_2_area, 'default_information_originate'), 'metric'), ))
                        _loop_vars['nssa_area_cli'] = l_2_nssa_area_cli
                    if t_3(environment.getattr(environment.getattr(l_2_area, 'default_information_originate'), 'metric_type')):
                        pass
                        l_2_nssa_area_cli = str_join(((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli), ' metric-type ', environment.getattr(environment.getattr(l_2_area, 'default_information_originate'), 'metric_type'), ))
                        _loop_vars['nssa_area_cli'] = l_2_nssa_area_cli
                if t_3(environment.getattr(l_2_area, 'nssa_only'), True):
                    pass
                    if not isinstance(l_2_ns, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_ns['print_nssa'] = True
                    l_2_nssa_area_cli = str_join(((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli), ' nssa-only', ))
                    _loop_vars['nssa_area_cli'] = l_2_nssa_area_cli
                if (environment.getattr((undefined(name='ns') if l_2_ns is missing else l_2_ns), 'print_nssa') == True):
                    pass
                    yield '   '
                    yield str((undefined(name='nssa_area_cli') if l_2_nssa_area_cli is missing else l_2_nssa_area_cli))
                    yield '\n'
            for l_3_filter_network in t_1(environment.getattr(environment.getattr(l_2_area, 'filter'), 'networks')):
                _loop_vars = {}
                pass
                yield '   area '
                yield str(environment.getattr(l_2_area, 'id'))
                yield ' filter '
                yield str(l_3_filter_network)
                yield '\n'
            l_3_filter_network = missing
            if t_3(environment.getattr(environment.getattr(l_2_area, 'filter'), 'prefix_list')):
                pass
                yield '   area '
                yield str(environment.getattr(l_2_area, 'id'))
                yield ' filter prefix-list '
                yield str(environment.getattr(environment.getattr(l_2_area, 'filter'), 'prefix_list'))
                yield '\n'
        l_2_area = l_2_stub_area_cli = l_2_namespace = l_2_ns = l_2_nssa_area_cli = missing
        for l_2_network_prefix in t_1(environment.getattr(l_1_process_id, 'network_prefixes'), 'ipv4_prefix'):
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_2_network_prefix, 'area')):
                pass
                yield '   network '
                yield str(environment.getattr(l_2_network_prefix, 'ipv4_prefix'))
                yield ' area '
                yield str(environment.getattr(l_2_network_prefix, 'area'))
                yield '\n'
        l_2_network_prefix = missing
        if t_3(environment.getattr(l_1_process_id, 'max_lsa')):
            pass
            yield '   max-lsa '
            yield str(environment.getattr(l_1_process_id, 'max_lsa'))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'log_adjacency_changes_detail'), True):
            pass
            yield '   log-adjacency-changes detail\n'
        if ((t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'initial')) and t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'min'))) and t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'max'))):
            pass
            l_1_timer_ospf_spf_delay = 'timers spf delay initial'
            _loop_vars['timer_ospf_spf_delay'] = l_1_timer_ospf_spf_delay
            l_1_timer_ospf_spf_delay = str_join(((undefined(name='timer_ospf_spf_delay') if l_1_timer_ospf_spf_delay is missing else l_1_timer_ospf_spf_delay), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'initial'), ))
            _loop_vars['timer_ospf_spf_delay'] = l_1_timer_ospf_spf_delay
            l_1_timer_ospf_spf_delay = str_join(((undefined(name='timer_ospf_spf_delay') if l_1_timer_ospf_spf_delay is missing else l_1_timer_ospf_spf_delay), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'min'), ))
            _loop_vars['timer_ospf_spf_delay'] = l_1_timer_ospf_spf_delay
            l_1_timer_ospf_spf_delay = str_join(((undefined(name='timer_ospf_spf_delay') if l_1_timer_ospf_spf_delay is missing else l_1_timer_ospf_spf_delay), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'spf_delay'), 'max'), ))
            _loop_vars['timer_ospf_spf_delay'] = l_1_timer_ospf_spf_delay
            yield '   '
            yield str((undefined(name='timer_ospf_spf_delay') if l_1_timer_ospf_spf_delay is missing else l_1_timer_ospf_spf_delay))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'rx_min_interval')):
            pass
            yield '   timers lsa rx min interval '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'rx_min_interval'))
            yield '\n'
        if ((t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'initial')) and t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'min'))) and t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'max'))):
            pass
            l_1_timer_ospf_lsa_tx = 'timers lsa tx delay initial'
            _loop_vars['timer_ospf_lsa_tx'] = l_1_timer_ospf_lsa_tx
            l_1_timer_ospf_lsa_tx = str_join(((undefined(name='timer_ospf_lsa_tx') if l_1_timer_ospf_lsa_tx is missing else l_1_timer_ospf_lsa_tx), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'initial'), ))
            _loop_vars['timer_ospf_lsa_tx'] = l_1_timer_ospf_lsa_tx
            l_1_timer_ospf_lsa_tx = str_join(((undefined(name='timer_ospf_lsa_tx') if l_1_timer_ospf_lsa_tx is missing else l_1_timer_ospf_lsa_tx), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'min'), ))
            _loop_vars['timer_ospf_lsa_tx'] = l_1_timer_ospf_lsa_tx
            l_1_timer_ospf_lsa_tx = str_join(((undefined(name='timer_ospf_lsa_tx') if l_1_timer_ospf_lsa_tx is missing else l_1_timer_ospf_lsa_tx), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'timers'), 'lsa'), 'tx_delay'), 'max'), ))
            _loop_vars['timer_ospf_lsa_tx'] = l_1_timer_ospf_lsa_tx
            yield '   '
            yield str((undefined(name='timer_ospf_lsa_tx') if l_1_timer_ospf_lsa_tx is missing else l_1_timer_ospf_lsa_tx))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'maximum_paths')):
            pass
            yield '   maximum-paths '
            yield str(environment.getattr(l_1_process_id, 'maximum_paths'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa')):
            pass
            l_1_max_metric_router_lsa_cli = 'max-metric router-lsa'
            _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'external_lsa')):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' external-lsa', ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'external_lsa'), 'override_metric')):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'external_lsa'), 'override_metric'), ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'include_stub'), True):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' include-stub', ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'on_startup')):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' on-startup ', environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'on_startup'), ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'summary_lsa')):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' summary-lsa', ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'summary_lsa'), 'override_metric')):
                pass
                l_1_max_metric_router_lsa_cli = str_join(((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_process_id, 'max_metric'), 'router_lsa'), 'summary_lsa'), 'override_metric'), ))
                _loop_vars['max_metric_router_lsa_cli'] = l_1_max_metric_router_lsa_cli
            yield '   '
            yield str((undefined(name='max_metric_router_lsa_cli') if l_1_max_metric_router_lsa_cli is missing else l_1_max_metric_router_lsa_cli))
            yield '\n'
        if t_4(environment.getattr(l_1_process_id, 'default_information_originate')):
            pass
            l_1_default_information_originate_cli = 'default-information originate'
            _loop_vars['default_information_originate_cli'] = l_1_default_information_originate_cli
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'default_information_originate'), 'always'), True):
                pass
                l_1_default_information_originate_cli = str_join(((undefined(name='default_information_originate_cli') if l_1_default_information_originate_cli is missing else l_1_default_information_originate_cli), ' always', ))
                _loop_vars['default_information_originate_cli'] = l_1_default_information_originate_cli
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'default_information_originate'), 'metric')):
                pass
                l_1_default_information_originate_cli = str_join(((undefined(name='default_information_originate_cli') if l_1_default_information_originate_cli is missing else l_1_default_information_originate_cli), ' metric ', environment.getattr(environment.getattr(l_1_process_id, 'default_information_originate'), 'metric'), ))
                _loop_vars['default_information_originate_cli'] = l_1_default_information_originate_cli
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'default_information_originate'), 'metric_type')):
                pass
                l_1_default_information_originate_cli = str_join(((undefined(name='default_information_originate_cli') if l_1_default_information_originate_cli is missing else l_1_default_information_originate_cli), ' metric-type ', environment.getattr(environment.getattr(l_1_process_id, 'default_information_originate'), 'metric_type'), ))
                _loop_vars['default_information_originate_cli'] = l_1_default_information_originate_cli
            yield '   '
            yield str((undefined(name='default_information_originate_cli') if l_1_default_information_originate_cli is missing else l_1_default_information_originate_cli))
            yield '\n'
        for l_2_summary_address in t_1(environment.getattr(l_1_process_id, 'summary_addresses'), 'prefix'):
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_2_summary_address, 'tag')):
                pass
                yield '   summary-address '
                yield str(environment.getattr(l_2_summary_address, 'prefix'))
                yield ' tag '
                yield str(environment.getattr(l_2_summary_address, 'tag'))
                yield '\n'
            elif t_3(environment.getattr(l_2_summary_address, 'attribute_map')):
                pass
                yield '   summary-address '
                yield str(environment.getattr(l_2_summary_address, 'prefix'))
                yield ' attribute-map '
                yield str(environment.getattr(l_2_summary_address, 'attribute_map'))
                yield '\n'
            elif t_3(environment.getattr(l_2_summary_address, 'not_advertise'), True):
                pass
                yield '   summary-address '
                yield str(environment.getattr(l_2_summary_address, 'prefix'))
                yield ' not-advertise\n'
            else:
                pass
                yield '   summary-address '
                yield str(environment.getattr(l_2_summary_address, 'prefix'))
                yield '\n'
        l_2_summary_address = missing
        if t_3(environment.getattr(environment.getattr(l_1_process_id, 'graceful_restart'), 'enabled'), True):
            pass
            l_1_graceful_restart_cli = 'graceful-restart'
            _loop_vars['graceful_restart_cli'] = l_1_graceful_restart_cli
            if t_3(environment.getattr(environment.getattr(l_1_process_id, 'graceful_restart'), 'grace_period')):
                pass
                l_1_graceful_restart_cli = str_join(((undefined(name='graceful_restart_cli') if l_1_graceful_restart_cli is missing else l_1_graceful_restart_cli), ' grace-period ', environment.getattr(environment.getattr(l_1_process_id, 'graceful_restart'), 'grace_period'), ))
                _loop_vars['graceful_restart_cli'] = l_1_graceful_restart_cli
            yield '   '
            yield str((undefined(name='graceful_restart_cli') if l_1_graceful_restart_cli is missing else l_1_graceful_restart_cli))
            yield '\n'
        if t_3(environment.getattr(l_1_process_id, 'mpls_ldp_sync_default'), True):
            pass
            yield '   mpls ldp sync default\n'
        if t_3(environment.getattr(l_1_process_id, 'graceful_restart_helper'), True):
            pass
            yield '   graceful-restart-helper\n'
        elif t_3(environment.getattr(l_1_process_id, 'graceful_restart_helper'), False):
            pass
            yield '   no graceful-restart-helper\n'
        if t_3(environment.getattr(l_1_process_id, 'eos_cli')):
            pass
            yield '   '
            yield str(t_2(environment.getattr(l_1_process_id, 'eos_cli'), 3, False))
            yield '\n'
    l_1_process_id = l_1_redistribute_bgp_cli = l_1_redistribute_connected_cli = l_1_redistribute_static_cli = l_1_timer_ospf_spf_delay = l_1_timer_ospf_lsa_tx = l_1_max_metric_router_lsa_cli = l_1_default_information_originate_cli = l_1_graceful_restart_cli = missing

blocks = {}
debug_info = '7=36&9=48&10=51&12=58&14=60&15=63&17=65&18=68&20=70&23=73&26=76&27=78&28=81&30=83&31=86&33=88&34=91&37=93&40=96&41=98&42=102&45=105&46=107&47=109&48=111&50=113&51=115&53=118&55=120&56=122&57=124&58=126&60=128&61=130&63=133&65=135&66=137&67=139&68=141&70=143&71=145&73=148&75=150&76=153&78=155&80=162&81=164&82=166&83=168&85=171&88=173&90=175&91=177&92=179&93=181&94=185&96=187&97=189&98=192&99=194&100=196&102=198&103=200&106=202&107=204&108=207&110=209&111=212&115=214&116=218&118=223&119=226&122=231&123=234&124=237&127=242&128=245&130=247&133=250&136=252&137=254&138=256&139=258&140=261&142=263&143=266&145=268&148=270&149=272&150=274&151=276&152=279&154=281&155=284&157=286&158=288&159=290&160=292&162=294&163=296&165=298&166=300&168=302&169=304&171=306&172=308&174=310&175=312&177=315&179=317&180=319&181=321&182=323&184=325&185=327&187=329&188=331&190=334&192=336&193=339&194=342&195=346&196=349&197=353&198=356&200=361&203=364&204=366&205=368&206=370&208=373&210=375&213=378&215=381&218=384&219=387'