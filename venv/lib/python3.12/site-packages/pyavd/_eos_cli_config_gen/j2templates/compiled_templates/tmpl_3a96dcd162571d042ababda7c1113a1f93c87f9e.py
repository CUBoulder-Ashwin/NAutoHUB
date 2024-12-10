from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-isis.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_isis = resolve('router_isis')
    l_0_spf_interval_cli = resolve('spf_interval_cli')
    l_0_wait_hold_interval_unit = resolve('wait_hold_interval_unit')
    l_0_timers_lsp_generation = resolve('timers_lsp_generation')
    l_0_isis_auth_cli = resolve('isis_auth_cli')
    l_0_both_key_ids = resolve('both_key_ids')
    l_0_lu_cli = resolve('lu_cli')
    l_0_ti_lfa_cli = resolve('ti_lfa_cli')
    l_0_ti_lfa_srlg_cli = resolve('ti_lfa_srlg_cli')
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
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'instance')):
        pass
        yield '!\nrouter isis '
        yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'instance'))
        yield '\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'net')):
            pass
            yield '   net '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'net'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'router_id')):
            pass
            yield '   router-id ipv4 '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'router_id'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'is_type')):
            pass
            yield '   is-type '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'is_type'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'log_adjacency_changes'), True):
            pass
            yield '   log-adjacency-changes\n'
        elif t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'log_adjacency_changes'), False):
            pass
            yield '   no log-adjacency-changes\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'mpls_ldp_sync_default'), True):
            pass
            yield '   mpls ldp sync default\n'
        for l_1_redistribute_route in t_2(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'redistribute_routes'), 'source_protocol'):
            l_1_redistribute_route_cli = resolve('redistribute_route_cli')
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_redistribute_route, 'source_protocol')):
                pass
                l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                if (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'isis'):
                    pass
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' instance', ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                elif (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'ospf'):
                    pass
                    if t_4(environment.getattr(l_1_redistribute_route, 'include_leaked'), True):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (not t_4(environment.getattr(l_1_redistribute_route, 'ospf_route_type'))):
                        pass
                        continue
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                elif (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'ospfv3'):
                    pass
                    if (not t_4(environment.getattr(l_1_redistribute_route, 'ospf_route_type'))):
                        pass
                        continue
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                elif (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['static', 'connected']):
                    pass
                    if t_4(environment.getattr(l_1_redistribute_route, 'include_leaked'), True):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                if t_4(environment.getattr(l_1_redistribute_route, 'route_map')):
                    pass
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                yield '   '
                yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                yield '\n'
        l_1_redistribute_route = l_1_redistribute_route_cli = missing
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'local_convergence'), 'protected_prefixes'), True):
            pass
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'local_convergence'), 'delay')):
                pass
                yield '   timers local-convergence-delay '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'local_convergence'), 'delay'))
                yield ' protected-prefixes\n'
            else:
                pass
                yield '   timers local-convergence-delay protected-prefixes\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'enabled')):
            pass
            yield '   set-overload-bit\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup')):
            pass
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup'), 'delay')):
                pass
                yield '   set-overload-bit on-startup '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup'), 'delay'))
                yield '\n'
            elif t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup'), 'wait_for_bgp'), 'enabled'), True):
                pass
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup'), 'wait_for_bgp'), 'timeout')):
                    pass
                    yield '   set-overload-bit on-startup wait-for-bgp timeout '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'set_overload_bit'), 'on_startup'), 'wait_for_bgp'), 'timeout'))
                    yield '\n'
                else:
                    pass
                    yield '   set-overload-bit on-startup wait-for-bgp\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'advertise'), 'passive_only'), True):
            pass
            yield '   advertise passive-only\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval')):
            pass
            l_0_spf_interval_cli = str_join(('spf-interval ', environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval'), ))
            context.vars['spf_interval_cli'] = l_0_spf_interval_cli
            context.exported_vars.add('spf_interval_cli')
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval_unit')):
                pass
                l_0_spf_interval_cli = str_join(((undefined(name='spf_interval_cli') if l_0_spf_interval_cli is missing else l_0_spf_interval_cli), ' ', environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval_unit'), ))
                context.vars['spf_interval_cli'] = l_0_spf_interval_cli
                context.exported_vars.add('spf_interval_cli')
                l_0_wait_hold_interval_unit = ' milliseconds'
                context.vars['wait_hold_interval_unit'] = l_0_wait_hold_interval_unit
                context.exported_vars.add('wait_hold_interval_unit')
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'wait_interval')):
                pass
                l_0_spf_interval_cli = str_join(((undefined(name='spf_interval_cli') if l_0_spf_interval_cli is missing else l_0_spf_interval_cli), ' ', environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'wait_interval'), t_1((undefined(name='wait_hold_interval_unit') if l_0_wait_hold_interval_unit is missing else l_0_wait_hold_interval_unit), ''), ))
                context.vars['spf_interval_cli'] = l_0_spf_interval_cli
                context.exported_vars.add('spf_interval_cli')
                if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'hold_interval')):
                    pass
                    l_0_spf_interval_cli = str_join(((undefined(name='spf_interval_cli') if l_0_spf_interval_cli is missing else l_0_spf_interval_cli), ' ', environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'hold_interval'), t_1((undefined(name='wait_hold_interval_unit') if l_0_wait_hold_interval_unit is missing else l_0_wait_hold_interval_unit), ''), ))
                    context.vars['spf_interval_cli'] = l_0_spf_interval_cli
                    context.exported_vars.add('spf_interval_cli')
            yield '   '
            yield str((undefined(name='spf_interval_cli') if l_0_spf_interval_cli is missing else l_0_spf_interval_cli))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'interval')):
            pass
            yield '   timers csnp generation interval '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'interval'))
            yield ' seconds\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'p2p_disabled'), True):
            pass
            yield '   timers csnp generation p2p disabled\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'out_delay')):
            pass
            yield '   timers lsp out-delay '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'out_delay'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'refresh_interval')):
            pass
            yield '   timers lsp refresh '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'refresh_interval'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'interval')):
            pass
            l_0_timers_lsp_generation = str_join(('timers lsp generation ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'interval'), ))
            context.vars['timers_lsp_generation'] = l_0_timers_lsp_generation
            context.exported_vars.add('timers_lsp_generation')
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'initial_wait_time')):
                pass
                l_0_timers_lsp_generation = str_join(((undefined(name='timers_lsp_generation') if l_0_timers_lsp_generation is missing else l_0_timers_lsp_generation), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'initial_wait_time'), ))
                context.vars['timers_lsp_generation'] = l_0_timers_lsp_generation
                context.exported_vars.add('timers_lsp_generation')
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'wait_time')):
                    pass
                    l_0_timers_lsp_generation = str_join(((undefined(name='timers_lsp_generation') if l_0_timers_lsp_generation is missing else l_0_timers_lsp_generation), ' ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'wait_time'), ))
                    context.vars['timers_lsp_generation'] = l_0_timers_lsp_generation
                    context.exported_vars.add('timers_lsp_generation')
            yield '   '
            yield str((undefined(name='timers_lsp_generation') if l_0_timers_lsp_generation is missing else l_0_timers_lsp_generation))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'min_remaining_lifetime')):
            pass
            yield '   timers lsp min-remaining-lifetime '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'min_remaining_lifetime'))
            yield '\n'
        if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode') == 'sha') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'sha'), 'key_id')))) or (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode') == 'shared-secret') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'shared_secret'), 'profile'))) and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'shared_secret'), 'algorithm'))))):
            pass
            l_0_isis_auth_cli = str_join(('authentication mode ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode'), ))
            context.vars['isis_auth_cli'] = l_0_isis_auth_cli
            context.exported_vars.add('isis_auth_cli')
            if (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode') == 'sha'):
                pass
                l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'sha'), 'key_id'), ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
            elif (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'mode') == 'shared-secret'):
                pass
                l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'shared_secret'), 'profile'), ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
                l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'shared_secret'), 'algorithm'), ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'rx_disabled'), True):
                pass
                l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' rx-disabled', ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
            yield '   '
            yield str((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli))
            yield '\n'
        else:
            pass
            if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode') == 'sha') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'sha'), 'key_id')))) or (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode') == 'shared-secret') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'shared_secret'), 'profile'))) and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'shared_secret'), 'algorithm'))))):
                pass
                l_0_isis_auth_cli = str_join(('authentication mode ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode'), ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
                if (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode') == 'sha'):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'sha'), 'key_id'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                elif (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'mode') == 'shared-secret'):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'shared_secret'), 'profile'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'shared_secret'), 'algorithm'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'rx_disabled'), True):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' rx-disabled', ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                yield '   '
                yield str((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli))
                yield ' level-1\n'
            if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode') == 'sha') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'sha'), 'key_id')))) or (((environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode') == 'shared-secret') and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'shared_secret'), 'profile'))) and t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'shared_secret'), 'algorithm'))))):
                pass
                l_0_isis_auth_cli = str_join(('authentication mode ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode'), ))
                context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                context.exported_vars.add('isis_auth_cli')
                if (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode') == 'sha'):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'sha'), 'key_id'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                elif (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'mode') == 'shared-secret'):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'shared_secret'), 'profile'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'shared_secret'), 'algorithm'), ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'rx_disabled'), True):
                    pass
                    l_0_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli), ' rx-disabled', ))
                    context.vars['isis_auth_cli'] = l_0_isis_auth_cli
                    context.exported_vars.add('isis_auth_cli')
                yield '   '
                yield str((undefined(name='isis_auth_cli') if l_0_isis_auth_cli is missing else l_0_isis_auth_cli))
                yield ' level-2\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart')):
            pass
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'enabled'), True):
                pass
                yield '   graceful-restart\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_1_wait_time')):
                pass
                yield '   graceful-restart t2 level-1 '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_1_wait_time'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_2_wait_time')):
                pass
                yield '   graceful-restart t2 level-2 '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_2_wait_time'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'restart_hold_time')):
                pass
                yield '   graceful-restart restart-hold-time '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'restart_hold_time'))
                yield '\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication')):
            pass
            l_0_both_key_ids = []
            context.vars['both_key_ids'] = l_0_both_key_ids
            context.exported_vars.add('both_key_ids')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key_ids')):
                pass
                for l_1_auth_key in t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key_ids'), 'id'):
                    _loop_vars = {}
                    pass
                    if (((t_4(environment.getattr(l_1_auth_key, 'id')) and t_4(environment.getattr(l_1_auth_key, 'algorithm'))) and t_4(environment.getattr(l_1_auth_key, 'key_type'))) and t_4(environment.getattr(l_1_auth_key, 'key'))):
                        pass
                        context.call(environment.getattr((undefined(name='both_key_ids') if l_0_both_key_ids is missing else l_0_both_key_ids), 'append'), environment.getattr(l_1_auth_key, 'id'), _loop_vars=_loop_vars)
                        if t_4(environment.getattr(l_1_auth_key, 'rfc_5310'), True):
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' rfc-5310 key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield '\n'
                        else:
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield '\n'
                l_1_auth_key = missing
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key_ids')):
                pass
                for l_1_auth_key in environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key_ids'):
                    _loop_vars = {}
                    pass
                    if ((((t_4(environment.getattr(l_1_auth_key, 'id')) and (environment.getattr(l_1_auth_key, 'id') not in (undefined(name='both_key_ids') if l_0_both_key_ids is missing else l_0_both_key_ids))) and t_4(environment.getattr(l_1_auth_key, 'algorithm'))) and t_4(environment.getattr(l_1_auth_key, 'key_type'))) and t_4(environment.getattr(l_1_auth_key, 'key'))):
                        pass
                        if t_4(environment.getattr(l_1_auth_key, 'rfc_5310'), True):
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' rfc-5310 key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield ' level-1\n'
                        else:
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield ' level-1\n'
                l_1_auth_key = missing
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key_ids')):
                pass
                for l_1_auth_key in environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key_ids'):
                    _loop_vars = {}
                    pass
                    if ((((t_4(environment.getattr(l_1_auth_key, 'id')) and (environment.getattr(l_1_auth_key, 'id') not in (undefined(name='both_key_ids') if l_0_both_key_ids is missing else l_0_both_key_ids))) and t_4(environment.getattr(l_1_auth_key, 'algorithm'))) and t_4(environment.getattr(l_1_auth_key, 'key_type'))) and t_4(environment.getattr(l_1_auth_key, 'key'))):
                        pass
                        if t_4(environment.getattr(l_1_auth_key, 'rfc_5310'), True):
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' rfc-5310 key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield ' level-2\n'
                        else:
                            pass
                            yield '   authentication key-id '
                            yield str(environment.getattr(l_1_auth_key, 'id'))
                            yield ' algorithm '
                            yield str(environment.getattr(l_1_auth_key, 'algorithm'))
                            yield ' key '
                            yield str(environment.getattr(l_1_auth_key, 'key_type'))
                            yield ' '
                            yield str(environment.getattr(l_1_auth_key, 'key'))
                            yield ' level-2\n'
                l_1_auth_key = missing
            if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key_type')) and t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key'))):
                pass
                yield '   authentication key '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key_type'))
                yield ' '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'both'), 'key'))
                yield '\n'
            else:
                pass
                if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key_type')) and t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key'))):
                    pass
                    yield '   authentication key '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key_type'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_1'), 'key'))
                    yield ' level-1\n'
                if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key_type')) and t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key'))):
                    pass
                    yield '   authentication key '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key_type'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'authentication'), 'level_2'), 'key'))
                    yield ' level-2\n'
        yield '   !\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'enabled'), True):
            pass
            yield '   address-family ipv4 unicast\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'maximum_paths')):
                pass
                yield '      maximum-paths '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'maximum_paths'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'tunnel_source_labeled_unicast'), 'enabled'), True):
                pass
                l_0_lu_cli = 'tunnel source-protocol bgp ipv4 labeled-unicast'
                context.vars['lu_cli'] = l_0_lu_cli
                context.exported_vars.add('lu_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'tunnel_source_labeled_unicast'), 'rcf')):
                    pass
                    l_0_lu_cli = str_join(((undefined(name='lu_cli') if l_0_lu_cli is missing else l_0_lu_cli), ' rcf ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'tunnel_source_labeled_unicast'), 'rcf'), ))
                    context.vars['lu_cli'] = l_0_lu_cli
                    context.exported_vars.add('lu_cli')
                yield '      '
                yield str((undefined(name='lu_cli') if l_0_lu_cli is missing else l_0_lu_cli))
                yield '\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'bfd_all_interfaces'), True):
                pass
                yield '      bfd all-interfaces\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'mode')):
                pass
                l_0_ti_lfa_cli = str_join(('fast-reroute ti-lfa mode ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'mode'), ))
                context.vars['ti_lfa_cli'] = l_0_ti_lfa_cli
                context.exported_vars.add('ti_lfa_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'level')):
                    pass
                    l_0_ti_lfa_cli = str_join(((undefined(name='ti_lfa_cli') if l_0_ti_lfa_cli is missing else l_0_ti_lfa_cli), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'level'), ))
                    context.vars['ti_lfa_cli'] = l_0_ti_lfa_cli
                    context.exported_vars.add('ti_lfa_cli')
                yield '      '
                yield str((undefined(name='ti_lfa_cli') if l_0_ti_lfa_cli is missing else l_0_ti_lfa_cli))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'), True):
                pass
                l_0_ti_lfa_srlg_cli = 'fast-reroute ti-lfa srlg'
                context.vars['ti_lfa_srlg_cli'] = l_0_ti_lfa_srlg_cli
                context.exported_vars.add('ti_lfa_srlg_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'), True):
                    pass
                    l_0_ti_lfa_srlg_cli = str_join(((undefined(name='ti_lfa_srlg_cli') if l_0_ti_lfa_srlg_cli is missing else l_0_ti_lfa_srlg_cli), ' strict', ))
                    context.vars['ti_lfa_srlg_cli'] = l_0_ti_lfa_srlg_cli
                    context.exported_vars.add('ti_lfa_srlg_cli')
                yield '      '
                yield str((undefined(name='ti_lfa_srlg_cli') if l_0_ti_lfa_srlg_cli is missing else l_0_ti_lfa_srlg_cli))
                yield '\n'
            yield '   !\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'enabled'), True):
            pass
            yield '   address-family ipv6 unicast\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'bfd_all_interfaces'), True):
                pass
                yield '      bfd all-interfaces\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'maximum_paths')):
                pass
                yield '      maximum-paths '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'maximum_paths'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'mode')):
                pass
                l_0_ti_lfa_cli = str_join(('fast-reroute ti-lfa mode ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'mode'), ))
                context.vars['ti_lfa_cli'] = l_0_ti_lfa_cli
                context.exported_vars.add('ti_lfa_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'level')):
                    pass
                    l_0_ti_lfa_cli = str_join(((undefined(name='ti_lfa_cli') if l_0_ti_lfa_cli is missing else l_0_ti_lfa_cli), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'level'), ))
                    context.vars['ti_lfa_cli'] = l_0_ti_lfa_cli
                    context.exported_vars.add('ti_lfa_cli')
                yield '      '
                yield str((undefined(name='ti_lfa_cli') if l_0_ti_lfa_cli is missing else l_0_ti_lfa_cli))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'), True):
                pass
                l_0_ti_lfa_srlg_cli = 'fast-reroute ti-lfa srlg'
                context.vars['ti_lfa_srlg_cli'] = l_0_ti_lfa_srlg_cli
                context.exported_vars.add('ti_lfa_srlg_cli')
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'), True):
                    pass
                    l_0_ti_lfa_srlg_cli = str_join(((undefined(name='ti_lfa_srlg_cli') if l_0_ti_lfa_srlg_cli is missing else l_0_ti_lfa_srlg_cli), ' strict', ))
                    context.vars['ti_lfa_srlg_cli'] = l_0_ti_lfa_srlg_cli
                    context.exported_vars.add('ti_lfa_srlg_cli')
                yield '      '
                yield str((undefined(name='ti_lfa_srlg_cli') if l_0_ti_lfa_srlg_cli is missing else l_0_ti_lfa_srlg_cli))
                yield '\n'
            yield '   !\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls')):
            pass
            yield '   segment-routing mpls\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'enabled'), True):
                pass
                yield '      no shutdown\n'
            elif t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'enabled'), False):
                pass
                yield '      shutdown\n'
            for l_1_prefix_segment in t_2(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'prefix_segments'), 'prefix'):
                _loop_vars = {}
                pass
                if (t_4(environment.getattr(l_1_prefix_segment, 'prefix')) and t_4(environment.getattr(l_1_prefix_segment, 'index'))):
                    pass
                    yield '      prefix-segment '
                    yield str(environment.getattr(l_1_prefix_segment, 'prefix'))
                    yield ' index '
                    yield str(environment.getattr(l_1_prefix_segment, 'index'))
                    yield '\n'
            l_1_prefix_segment = missing
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'eos_cli')):
            pass
            yield '   '
            yield str(t_3(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'eos_cli'), 3, False))
            yield '\n'

blocks = {}
debug_info = '7=44&9=47&10=49&11=52&13=54&14=57&16=59&17=62&19=64&21=67&24=70&27=73&28=77&29=79&30=81&31=83&32=85&33=87&34=89&36=91&37=93&39=94&40=96&41=98&42=100&44=101&45=103&46=105&47=107&50=109&51=111&53=114&56=117&57=119&58=122&63=127&66=130&67=132&68=135&69=137&70=139&71=142&77=147&80=150&81=152&82=155&83=157&84=160&86=163&87=165&88=168&89=170&92=174&94=176&95=179&97=181&100=184&101=187&103=189&104=192&106=194&107=196&108=199&109=201&110=204&111=206&114=210&116=212&117=215&119=217&125=219&126=222&127=224&128=227&129=229&130=232&132=235&133=237&135=241&137=245&143=247&144=250&145=252&146=255&147=257&148=260&150=263&151=265&153=269&155=271&161=273&162=276&163=278&164=281&165=283&166=286&168=289&169=291&171=295&174=297&175=299&178=302&179=305&181=307&182=310&184=312&185=315&188=317&189=319&190=322&191=324&192=327&196=329&197=330&198=333&200=344&205=353&206=355&207=358&212=360&213=363&215=374&220=383&221=385&222=388&227=390&228=393&230=404&235=413&236=416&238=422&239=425&241=429&242=432&247=437&249=440&250=443&252=445&253=447&254=450&255=452&257=456&259=458&262=461&263=463&264=466&265=468&267=472&269=474&270=476&271=479&272=481&274=485&278=488&280=491&283=494&284=497&286=499&287=501&288=504&289=506&291=510&293=512&294=514&295=517&296=519&298=523&302=526&304=529&306=532&309=535&310=538&311=541&315=546&316=549'