from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-bgp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_bgp = resolve('router_bgp')
    l_0_timers_bgp_cli = resolve('timers_bgp_cli')
    l_0_distance_cli = resolve('distance_cli')
    l_0_rr_preserve_attributes_cli = resolve('rr_preserve_attributes_cli')
    l_0_paths_cli = resolve('paths_cli')
    l_0_redistribute_var = resolve('redistribute_var')
    l_0_redistribute_conn = resolve('redistribute_conn')
    l_0_redistribute_isis = resolve('redistribute_isis')
    l_0_redistribute_ospf = resolve('redistribute_ospf')
    l_0_redistribute_ospf_match = resolve('redistribute_ospf_match')
    l_0_redistribute_ospfv3 = resolve('redistribute_ospfv3')
    l_0_redistribute_ospfv3_match = resolve('redistribute_ospfv3_match')
    l_0_redistribute_static = resolve('redistribute_static')
    l_0_redistribute_rip = resolve('redistribute_rip')
    l_0_redistribute_host = resolve('redistribute_host')
    l_0_redistribute_dynamic = resolve('redistribute_dynamic')
    l_0_redistribute_bgp = resolve('redistribute_bgp')
    l_0_redistribute_user = resolve('redistribute_user')
    l_0_evpn_neighbor_default_encap_cli = resolve('evpn_neighbor_default_encap_cli')
    l_0_evpn_mpls_resolution_ribs = resolve('evpn_mpls_resolution_ribs')
    l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli = resolve('evpn_neighbor_default_nhs_received_evpn_routes_cli')
    l_0_hostflap_detection_cli = resolve('hostflap_detection_cli')
    l_0_layer2_cli = resolve('layer2_cli')
    l_0_v4_bgp_lu_resolution_ribs = resolve('v4_bgp_lu_resolution_ribs')
    l_0_redistribute_dhcp = resolve('redistribute_dhcp')
    l_0_path_selection_roles = resolve('path_selection_roles')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_5 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
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
    try:
        t_8 = environment.tests['number']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No test named 'number' found.")
    pass
    if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'as')):
        pass
        yield '!\nrouter bgp '
        yield str(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'as'))
        yield '\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'as_notation')):
            pass
            yield '   bgp asn notation '
            yield str(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'as_notation'))
            yield '\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'router_id')):
            pass
            yield '   router-id '
            yield str(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'router_id'))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'updates'), 'wait_for_convergence'), True):
            pass
            yield '   update wait-for-convergence\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'updates'), 'wait_install'), True):
            pass
            yield '   update wait-install\n'
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'default'), 'ipv4_unicast'), True):
            pass
            yield '   bgp default ipv4-unicast\n'
        elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'default'), 'ipv4_unicast'), False):
            pass
            yield '   no bgp default ipv4-unicast\n'
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'default'), 'ipv4_unicast_transport_ipv6'), True):
            pass
            yield '   bgp default ipv4-unicast transport ipv6\n'
        elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'default'), 'ipv4_unicast_transport_ipv6'), False):
            pass
            yield '   no bgp default ipv4-unicast transport ipv6\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers')):
            pass
            l_0_timers_bgp_cli = 'timers bgp'
            context.vars['timers_bgp_cli'] = l_0_timers_bgp_cli
            context.exported_vars.add('timers_bgp_cli')
            if (t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'keepalive_time')) and t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'hold_time'))):
                pass
                l_0_timers_bgp_cli = str_join(((undefined(name='timers_bgp_cli') if l_0_timers_bgp_cli is missing else l_0_timers_bgp_cli), ' ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'keepalive_time'), ' ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'hold_time'), ))
                context.vars['timers_bgp_cli'] = l_0_timers_bgp_cli
                context.exported_vars.add('timers_bgp_cli')
            if (t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'min_hold_time')) or t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'send_failure_hold_time'))):
                pass
                if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'min_hold_time')):
                    pass
                    l_0_timers_bgp_cli = str_join(((undefined(name='timers_bgp_cli') if l_0_timers_bgp_cli is missing else l_0_timers_bgp_cli), ' min-hold-time ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'min_hold_time'), ))
                    context.vars['timers_bgp_cli'] = l_0_timers_bgp_cli
                    context.exported_vars.add('timers_bgp_cli')
                if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'send_failure_hold_time')):
                    pass
                    l_0_timers_bgp_cli = str_join(((undefined(name='timers_bgp_cli') if l_0_timers_bgp_cli is missing else l_0_timers_bgp_cli), ' send-failure hold-time ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'timers'), 'send_failure_hold_time'), ))
                    context.vars['timers_bgp_cli'] = l_0_timers_bgp_cli
                    context.exported_vars.add('timers_bgp_cli')
            yield '   '
            yield str((undefined(name='timers_bgp_cli') if l_0_timers_bgp_cli is missing else l_0_timers_bgp_cli))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'external_routes')):
            pass
            l_0_distance_cli = str_join(('distance bgp ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'external_routes'), ))
            context.vars['distance_cli'] = l_0_distance_cli
            context.exported_vars.add('distance_cli')
            if (t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'internal_routes')) and t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'local_routes'))):
                pass
                l_0_distance_cli = str_join(((undefined(name='distance_cli') if l_0_distance_cli is missing else l_0_distance_cli), ' ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'internal_routes'), ' ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'distance'), 'local_routes'), ))
                context.vars['distance_cli'] = l_0_distance_cli
                context.exported_vars.add('distance_cli')
            yield '   '
            yield str((undefined(name='distance_cli') if l_0_distance_cli is missing else l_0_distance_cli))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart'), 'enabled'), True):
            pass
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart'), 'restart_time')):
                pass
                yield '   graceful-restart restart-time '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart'), 'restart_time'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart'), 'stalepath_time')):
                pass
                yield '   graceful-restart stalepath-time '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart'), 'stalepath_time'))
                yield '\n'
            yield '   graceful-restart\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp_cluster_id')):
            pass
            yield '   bgp cluster-id '
            yield str(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp_cluster_id'))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart_helper'), 'enabled'), False):
            pass
            yield '   no graceful-restart-helper\n'
        elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart_helper'), 'enabled'), True):
            pass
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart_helper'), 'restart_time')):
                pass
                yield '   graceful-restart-helper restart-time '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart_helper'), 'restart_time'))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'graceful_restart_helper'), 'long_lived'), True):
                pass
                yield '   graceful-restart-helper long-lived\n'
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'route_reflector_preserve_attributes'), 'enabled'), True):
            pass
            l_0_rr_preserve_attributes_cli = 'bgp route-reflector preserve-attributes'
            context.vars['rr_preserve_attributes_cli'] = l_0_rr_preserve_attributes_cli
            context.exported_vars.add('rr_preserve_attributes_cli')
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'route_reflector_preserve_attributes'), 'always'), True):
                pass
                l_0_rr_preserve_attributes_cli = str_join(((undefined(name='rr_preserve_attributes_cli') if l_0_rr_preserve_attributes_cli is missing else l_0_rr_preserve_attributes_cli), ' always', ))
                context.vars['rr_preserve_attributes_cli'] = l_0_rr_preserve_attributes_cli
                context.exported_vars.add('rr_preserve_attributes_cli')
            yield '   '
            yield str((undefined(name='rr_preserve_attributes_cli') if l_0_rr_preserve_attributes_cli is missing else l_0_rr_preserve_attributes_cli))
            yield '\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'maximum_paths'), 'paths')):
            pass
            l_0_paths_cli = str_join(('maximum-paths ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'maximum_paths'), 'paths'), ))
            context.vars['paths_cli'] = l_0_paths_cli
            context.exported_vars.add('paths_cli')
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'maximum_paths'), 'ecmp')):
                pass
                l_0_paths_cli = str_join(((undefined(name='paths_cli') if l_0_paths_cli is missing else l_0_paths_cli), ' ecmp ', environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'maximum_paths'), 'ecmp'), ))
                context.vars['paths_cli'] = l_0_paths_cli
                context.exported_vars.add('paths_cli')
            yield '   '
            yield str((undefined(name='paths_cli') if l_0_paths_cli is missing else l_0_paths_cli))
            yield '\n'
        for l_1_bgp_default in t_1(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp_defaults'), []):
            _loop_vars = {}
            pass
            yield '   '
            yield str(l_1_bgp_default)
            yield '\n'
        l_1_bgp_default = missing
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'receive'), True):
            pass
            yield '   bgp additional-paths receive\n'
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'receive'), False):
            pass
            yield '   no bgp additional-paths receive\n'
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send')):
            pass
            if (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                pass
                yield '   no bgp additional-paths send\n'
            elif (t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                pass
                yield '   bgp additional-paths send ecmp limit '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send_limit'))
                yield '\n'
            elif (environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                pass
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send_limit')):
                    pass
                    yield '   bgp additional-paths send limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
            else:
                pass
                yield '   bgp additional-paths send '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'additional_paths'), 'send'))
                yield '\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'listen_ranges')):
            pass
            def t_9(fiter):
                for l_1_listen_range in fiter:
                    if ((t_6(environment.getattr(l_1_listen_range, 'peer_group')) and t_6(environment.getattr(l_1_listen_range, 'prefix'))) and (t_6(environment.getattr(l_1_listen_range, 'peer_filter')) or t_6(environment.getattr(l_1_listen_range, 'remote_as')))):
                        yield l_1_listen_range
            for l_1_listen_range in t_9(t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'listen_ranges'), 'peer_group')):
                l_1_listen_range_cli = missing
                _loop_vars = {}
                pass
                l_1_listen_range_cli = str_join(('bgp listen range ', environment.getattr(l_1_listen_range, 'prefix'), ))
                _loop_vars['listen_range_cli'] = l_1_listen_range_cli
                if t_6(environment.getattr(l_1_listen_range, 'peer_id_include_router_id'), True):
                    pass
                    l_1_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_1_listen_range_cli is missing else l_1_listen_range_cli), ' peer-id include router-id', ))
                    _loop_vars['listen_range_cli'] = l_1_listen_range_cli
                l_1_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_1_listen_range_cli is missing else l_1_listen_range_cli), ' peer-group ', environment.getattr(l_1_listen_range, 'peer_group'), ))
                _loop_vars['listen_range_cli'] = l_1_listen_range_cli
                if t_6(environment.getattr(l_1_listen_range, 'peer_filter')):
                    pass
                    l_1_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_1_listen_range_cli is missing else l_1_listen_range_cli), ' peer-filter ', environment.getattr(l_1_listen_range, 'peer_filter'), ))
                    _loop_vars['listen_range_cli'] = l_1_listen_range_cli
                elif t_6(environment.getattr(l_1_listen_range, 'remote_as')):
                    pass
                    l_1_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_1_listen_range_cli is missing else l_1_listen_range_cli), ' remote-as ', environment.getattr(l_1_listen_range, 'remote_as'), ))
                    _loop_vars['listen_range_cli'] = l_1_listen_range_cli
                yield '   '
                yield str((undefined(name='listen_range_cli') if l_1_listen_range_cli is missing else l_1_listen_range_cli))
                yield '\n'
            l_1_listen_range = l_1_listen_range_cli = missing
        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'bestpath'), 'd_path'), True):
            pass
            yield '   bgp bestpath d-path\n'
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'neighbor_default'), 'send_community'), 'all'):
            pass
            yield '   neighbor default send-community\n'
        elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'neighbor_default'), 'send_community')):
            pass
            yield '   neighbor default send-community '
            yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'neighbor_default'), 'send_community'))
            yield '\n'
        for l_1_peer_group in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'peer_groups'), 'name'):
            l_1_remove_private_as_cli = resolve('remove_private_as_cli')
            l_1_allowas_in_cli = resolve('allowas_in_cli')
            l_1_neighbor_rib_in_pre_policy_retain_cli = resolve('neighbor_rib_in_pre_policy_retain_cli')
            l_1_hide_passwords = resolve('hide_passwords')
            l_1_default_originate_cli = resolve('default_originate_cli')
            l_1_maximum_routes_cli = resolve('maximum_routes_cli')
            l_1_link_bandwidth_cli = resolve('link_bandwidth_cli')
            l_1_remove_private_as_ingress_cli = resolve('remove_private_as_ingress_cli')
            _loop_vars = {}
            pass
            yield '   neighbor '
            yield str(environment.getattr(l_1_peer_group, 'name'))
            yield ' peer group\n'
            if t_6(environment.getattr(l_1_peer_group, 'remote_as')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' remote-as '
                yield str(environment.getattr(l_1_peer_group, 'remote_as'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'next_hop_self'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' next-hop-self\n'
            if t_6(environment.getattr(l_1_peer_group, 'next_hop_unchanged'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' next-hop-unchanged\n'
            if t_6(environment.getattr(l_1_peer_group, 'shutdown'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' shutdown\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as'), 'enabled'), True):
                pass
                l_1_remove_private_as_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' remove-private-as', ))
                _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as'), 'all'), True):
                    pass
                    l_1_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli), ' all', ))
                    _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as'), 'replace_as'), True):
                        pass
                        l_1_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli), ' replace-as', ))
                        _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                yield '   '
                yield str((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as'), 'enabled'), False):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' remove-private-as\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'as_path'), 'prepend_own_disabled'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' as-path prepend-own disabled\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'as_path'), 'remote_as_replace_out'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' as-path remote-as replace out\n'
            if t_6(environment.getattr(l_1_peer_group, 'local_as')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' local-as '
                yield str(environment.getattr(l_1_peer_group, 'local_as'))
                yield ' no-prepend replace-as\n'
            if t_6(environment.getattr(l_1_peer_group, 'weight')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' weight '
                yield str(environment.getattr(l_1_peer_group, 'weight'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'passive'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' passive\n'
            if t_6(environment.getattr(l_1_peer_group, 'update_source')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' update-source '
                yield str(environment.getattr(l_1_peer_group, 'update_source'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'bfd'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' bfd\n'
                if ((t_6(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'interval')) and t_6(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'min_rx'))) and t_6(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'multiplier'))):
                    pass
                    yield '   neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' bfd interval '
                    yield str(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'interval'))
                    yield ' min-rx '
                    yield str(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'min_rx'))
                    yield ' multiplier '
                    yield str(environment.getattr(environment.getattr(l_1_peer_group, 'bfd_timers'), 'multiplier'))
                    yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'description')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' description '
                yield str(environment.getattr(l_1_peer_group, 'description'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'allowas_in'), 'enabled'), True):
                pass
                l_1_allowas_in_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' allowas-in', ))
                _loop_vars['allowas_in_cli'] = l_1_allowas_in_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'allowas_in'), 'times')):
                    pass
                    l_1_allowas_in_cli = str_join(((undefined(name='allowas_in_cli') if l_1_allowas_in_cli is missing else l_1_allowas_in_cli), ' ', environment.getattr(environment.getattr(l_1_peer_group, 'allowas_in'), 'times'), ))
                    _loop_vars['allowas_in_cli'] = l_1_allowas_in_cli
                yield '   '
                yield str((undefined(name='allowas_in_cli') if l_1_allowas_in_cli is missing else l_1_allowas_in_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'rib_in_pre_policy_retain'), 'enabled'), True):
                pass
                l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' rib-in pre-policy retain', ))
                _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'rib_in_pre_policy_retain'), 'all'), True):
                    pass
                    l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli), ' all', ))
                    _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                yield '   '
                yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'rib_in_pre_policy_retain'), 'enabled'), False):
                pass
                l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(('no neighbor ', environment.getattr(l_1_peer_group, 'name'), ' rib-in pre-policy retain', ))
                _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                yield '   '
                yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'ebgp_multihop')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' ebgp-multihop '
                yield str(environment.getattr(l_1_peer_group, 'ebgp_multihop'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'ttl_maximum_hops')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' ttl maximum-hops '
                yield str(environment.getattr(l_1_peer_group, 'ttl_maximum_hops'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'route_reflector_client'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' route-reflector-client\n'
            if t_6(environment.getattr(l_1_peer_group, 'session_tracker')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' session tracker '
                yield str(environment.getattr(l_1_peer_group, 'session_tracker'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'timers')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' timers '
                yield str(environment.getattr(l_1_peer_group, 'timers'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' route-map '
                yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                yield ' in\n'
            if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' route-map '
                yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                yield ' out\n'
            if t_6(environment.getattr(l_1_peer_group, 'password')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' password 7 '
                yield str(t_2(environment.getattr(l_1_peer_group, 'password'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
            if (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'shared_secret'), 'profile')) and t_6(environment.getattr(environment.getattr(l_1_peer_group, 'shared_secret'), 'hash_algorithm'))):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' password shared-secret profile '
                yield str(environment.getattr(environment.getattr(l_1_peer_group, 'shared_secret'), 'profile'))
                yield ' algorithm '
                yield str(environment.getattr(environment.getattr(l_1_peer_group, 'shared_secret'), 'hash_algorithm'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'enabled'), True):
                pass
                l_1_default_originate_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' default-originate', ))
                _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'route_map')):
                    pass
                    l_1_default_originate_cli = str_join(((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli), ' route-map ', environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'route_map'), ))
                    _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'always'), True):
                    pass
                    l_1_default_originate_cli = str_join(((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli), ' always', ))
                    _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                yield '   '
                yield str((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'send_community'), 'all'):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' send-community\n'
            elif t_6(environment.getattr(l_1_peer_group, 'send_community')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' send-community '
                yield str(environment.getattr(l_1_peer_group, 'send_community'))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'maximum_routes')):
                pass
                l_1_maximum_routes_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' maximum-routes ', environment.getattr(l_1_peer_group, 'maximum_routes'), ))
                _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                if t_6(environment.getattr(l_1_peer_group, 'maximum_routes_warning_limit')):
                    pass
                    l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-limit ', environment.getattr(l_1_peer_group, 'maximum_routes_warning_limit'), ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                if t_6(environment.getattr(l_1_peer_group, 'maximum_routes_warning_only'), True):
                    pass
                    l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-only', ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                yield '   '
                yield str((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_peer_group, 'missing_policy')):
                pass
                for l_2_direction in ['in', 'out']:
                    l_2_missing_policy_cli = resolve('missing_policy_cli')
                    l_2_dir = l_2_policy = missing
                    _loop_vars = {}
                    pass
                    l_2_dir = str_join(('direction_', l_2_direction, ))
                    _loop_vars['dir'] = l_2_dir
                    l_2_policy = environment.getitem(environment.getattr(l_1_peer_group, 'missing_policy'), (undefined(name='dir') if l_2_dir is missing else l_2_dir))
                    _loop_vars['policy'] = l_2_policy
                    if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action')):
                        pass
                        l_2_missing_policy_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' missing-policy address-family all', ))
                        _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        if ((t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True)) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True)):
                            pass
                            l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' include', ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' community-list', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' prefix-list', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' sub-route-map', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' direction ', l_2_direction, ' action ', environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action'), ))
                        _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        yield '   '
                        yield str((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli))
                        yield '\n'
                l_2_direction = l_2_dir = l_2_policy = l_2_missing_policy_cli = missing
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'link_bandwidth'), 'enabled'), True):
                pass
                l_1_link_bandwidth_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' link-bandwidth', ))
                _loop_vars['link_bandwidth_cli'] = l_1_link_bandwidth_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'link_bandwidth'), 'default')):
                    pass
                    l_1_link_bandwidth_cli = str_join(((undefined(name='link_bandwidth_cli') if l_1_link_bandwidth_cli is missing else l_1_link_bandwidth_cli), ' default ', environment.getattr(environment.getattr(l_1_peer_group, 'link_bandwidth'), 'default'), ))
                    _loop_vars['link_bandwidth_cli'] = l_1_link_bandwidth_cli
                yield '   '
                yield str((undefined(name='link_bandwidth_cli') if l_1_link_bandwidth_cli is missing else l_1_link_bandwidth_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as_ingress'), 'enabled'), True):
                pass
                l_1_remove_private_as_ingress_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' remove-private-as ingress', ))
                _loop_vars['remove_private_as_ingress_cli'] = l_1_remove_private_as_ingress_cli
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as_ingress'), 'replace_as'), True):
                    pass
                    l_1_remove_private_as_ingress_cli = str_join(((undefined(name='remove_private_as_ingress_cli') if l_1_remove_private_as_ingress_cli is missing else l_1_remove_private_as_ingress_cli), ' replace-as', ))
                    _loop_vars['remove_private_as_ingress_cli'] = l_1_remove_private_as_ingress_cli
                yield '   '
                yield str((undefined(name='remove_private_as_ingress_cli') if l_1_remove_private_as_ingress_cli is missing else l_1_remove_private_as_ingress_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'remove_private_as_ingress'), 'enabled'), False):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_peer_group, 'name'))
                yield ' remove-private-as ingress\n'
        l_1_peer_group = l_1_remove_private_as_cli = l_1_allowas_in_cli = l_1_neighbor_rib_in_pre_policy_retain_cli = l_1_hide_passwords = l_1_default_originate_cli = l_1_maximum_routes_cli = l_1_link_bandwidth_cli = l_1_remove_private_as_ingress_cli = missing
        for l_1_neighbor in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'neighbors'), 'ip_address'):
            l_1_remove_private_as_cli = resolve('remove_private_as_cli')
            l_1_allowas_in_cli = resolve('allowas_in_cli')
            l_1_neighbor_rib_in_pre_policy_retain_cli = resolve('neighbor_rib_in_pre_policy_retain_cli')
            l_1_hide_passwords = resolve('hide_passwords')
            l_1_default_originate_cli = resolve('default_originate_cli')
            l_1_maximum_routes_cli = resolve('maximum_routes_cli')
            l_1_link_bandwidth_cli = resolve('link_bandwidth_cli')
            l_1_remove_private_as_ingress_cli = resolve('remove_private_as_ingress_cli')
            _loop_vars = {}
            pass
            if t_6(environment.getattr(l_1_neighbor, 'peer_group')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' peer group '
                yield str(environment.getattr(l_1_neighbor, 'peer_group'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'remote_as')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' remote-as '
                yield str(environment.getattr(l_1_neighbor, 'remote_as'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'next_hop_self'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' next-hop-self\n'
            if t_6(environment.getattr(l_1_neighbor, 'shutdown'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' shutdown\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as'), 'enabled'), True):
                pass
                l_1_remove_private_as_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' remove-private-as', ))
                _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as'), 'all'), True):
                    pass
                    l_1_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli), ' all', ))
                    _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as'), 'replace_as'), True):
                        pass
                        l_1_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli), ' replace-as', ))
                        _loop_vars['remove_private_as_cli'] = l_1_remove_private_as_cli
                yield '   '
                yield str((undefined(name='remove_private_as_cli') if l_1_remove_private_as_cli is missing else l_1_remove_private_as_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as'), 'enabled'), False):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' remove-private-as\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'as_path'), 'prepend_own_disabled'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' as-path prepend-own disabled\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'as_path'), 'remote_as_replace_out'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' as-path remote-as replace out\n'
            if t_6(environment.getattr(l_1_neighbor, 'local_as')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' local-as '
                yield str(environment.getattr(l_1_neighbor, 'local_as'))
                yield ' no-prepend replace-as\n'
            if t_6(environment.getattr(l_1_neighbor, 'weight')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' weight '
                yield str(environment.getattr(l_1_neighbor, 'weight'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'passive'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' passive\n'
            if t_6(environment.getattr(l_1_neighbor, 'update_source')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' update-source '
                yield str(environment.getattr(l_1_neighbor, 'update_source'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'bfd'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' bfd\n'
                if ((t_6(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'interval')) and t_6(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'min_rx'))) and t_6(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'multiplier'))):
                    pass
                    yield '   neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' bfd interval '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'interval'))
                    yield ' min-rx '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'min_rx'))
                    yield ' multiplier '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'bfd_timers'), 'multiplier'))
                    yield '\n'
            elif (t_6(environment.getattr(l_1_neighbor, 'bfd'), False) and t_6(environment.getattr(l_1_neighbor, 'peer_group'))):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' bfd\n'
            if t_6(environment.getattr(l_1_neighbor, 'description')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' description '
                yield str(environment.getattr(l_1_neighbor, 'description'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'allowas_in'), 'enabled'), True):
                pass
                l_1_allowas_in_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' allowas-in', ))
                _loop_vars['allowas_in_cli'] = l_1_allowas_in_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'allowas_in'), 'times')):
                    pass
                    l_1_allowas_in_cli = str_join(((undefined(name='allowas_in_cli') if l_1_allowas_in_cli is missing else l_1_allowas_in_cli), ' ', environment.getattr(environment.getattr(l_1_neighbor, 'allowas_in'), 'times'), ))
                    _loop_vars['allowas_in_cli'] = l_1_allowas_in_cli
                yield '   '
                yield str((undefined(name='allowas_in_cli') if l_1_allowas_in_cli is missing else l_1_allowas_in_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'rib_in_pre_policy_retain'), 'enabled'), True):
                pass
                l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' rib-in pre-policy retain', ))
                _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'rib_in_pre_policy_retain'), 'all'), True):
                    pass
                    l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli), ' all', ))
                    _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                yield '   '
                yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'rib_in_pre_policy_retain'), 'enabled'), False):
                pass
                l_1_neighbor_rib_in_pre_policy_retain_cli = str_join(('no neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' rib-in pre-policy retain', ))
                _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_1_neighbor_rib_in_pre_policy_retain_cli
                yield '   '
                yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_1_neighbor_rib_in_pre_policy_retain_cli is missing else l_1_neighbor_rib_in_pre_policy_retain_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'ebgp_multihop')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' ebgp-multihop '
                yield str(environment.getattr(l_1_neighbor, 'ebgp_multihop'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'ttl_maximum_hops')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' ttl maximum-hops '
                yield str(environment.getattr(l_1_neighbor, 'ttl_maximum_hops'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'route_reflector_client'), True):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' route-reflector-client\n'
            elif t_6(environment.getattr(l_1_neighbor, 'route_reflector_client'), False):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' route-reflector-client\n'
            if t_6(environment.getattr(l_1_neighbor, 'session_tracker')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' session tracker '
                yield str(environment.getattr(l_1_neighbor, 'session_tracker'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'timers')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' timers '
                yield str(environment.getattr(l_1_neighbor, 'timers'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' route-map '
                yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                yield ' in\n'
            if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' route-map '
                yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                yield ' out\n'
            if (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'shared_secret'), 'profile')) and t_6(environment.getattr(environment.getattr(l_1_neighbor, 'shared_secret'), 'hash_algorithm'))):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' password shared-secret profile '
                yield str(environment.getattr(environment.getattr(l_1_neighbor, 'shared_secret'), 'profile'))
                yield ' algorithm '
                yield str(environment.getattr(environment.getattr(l_1_neighbor, 'shared_secret'), 'hash_algorithm'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'password')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' password 7 '
                yield str(t_2(environment.getattr(l_1_neighbor, 'password'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'enabled'), True):
                pass
                l_1_default_originate_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' default-originate', ))
                _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'route_map')):
                    pass
                    l_1_default_originate_cli = str_join(((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli), ' route-map ', environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'route_map'), ))
                    _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'always'), True):
                    pass
                    l_1_default_originate_cli = str_join(((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli), ' always', ))
                    _loop_vars['default_originate_cli'] = l_1_default_originate_cli
                yield '   '
                yield str((undefined(name='default_originate_cli') if l_1_default_originate_cli is missing else l_1_default_originate_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'send_community'), 'all'):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' send-community\n'
            elif t_6(environment.getattr(l_1_neighbor, 'send_community')):
                pass
                yield '   neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' send-community '
                yield str(environment.getattr(l_1_neighbor, 'send_community'))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'maximum_routes')):
                pass
                l_1_maximum_routes_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' maximum-routes ', environment.getattr(l_1_neighbor, 'maximum_routes'), ))
                _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                if t_6(environment.getattr(l_1_neighbor, 'maximum_routes_warning_limit')):
                    pass
                    l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-limit ', environment.getattr(l_1_neighbor, 'maximum_routes_warning_limit'), ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                if t_6(environment.getattr(l_1_neighbor, 'maximum_routes_warning_only'), True):
                    pass
                    l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-only', ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                yield '   '
                yield str((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli))
                yield '\n'
            if t_6(environment.getattr(l_1_neighbor, 'missing_policy')):
                pass
                for l_2_direction in ['in', 'out']:
                    l_2_missing_policy_cli = resolve('missing_policy_cli')
                    l_2_dir = l_2_policy = missing
                    _loop_vars = {}
                    pass
                    l_2_dir = str_join(('direction_', l_2_direction, ))
                    _loop_vars['dir'] = l_2_dir
                    l_2_policy = environment.getitem(environment.getattr(l_1_neighbor, 'missing_policy'), (undefined(name='dir') if l_2_dir is missing else l_2_dir))
                    _loop_vars['policy'] = l_2_policy
                    if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action')):
                        pass
                        l_2_missing_policy_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' missing-policy address-family all', ))
                        _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        if ((t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True)) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True)):
                            pass
                            l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' include', ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' community-list', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' prefix-list', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' sub-route-map', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' direction ', l_2_direction, ' action ', environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action'), ))
                        _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                        yield '   '
                        yield str((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli))
                        yield '\n'
                l_2_direction = l_2_dir = l_2_policy = l_2_missing_policy_cli = missing
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'link_bandwidth'), 'enabled'), True):
                pass
                l_1_link_bandwidth_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' link-bandwidth', ))
                _loop_vars['link_bandwidth_cli'] = l_1_link_bandwidth_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'link_bandwidth'), 'default')):
                    pass
                    l_1_link_bandwidth_cli = str_join(((undefined(name='link_bandwidth_cli') if l_1_link_bandwidth_cli is missing else l_1_link_bandwidth_cli), ' default ', environment.getattr(environment.getattr(l_1_neighbor, 'link_bandwidth'), 'default'), ))
                    _loop_vars['link_bandwidth_cli'] = l_1_link_bandwidth_cli
                yield '   '
                yield str((undefined(name='link_bandwidth_cli') if l_1_link_bandwidth_cli is missing else l_1_link_bandwidth_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as_ingress'), 'enabled'), True):
                pass
                l_1_remove_private_as_ingress_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' remove-private-as ingress', ))
                _loop_vars['remove_private_as_ingress_cli'] = l_1_remove_private_as_ingress_cli
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as_ingress'), 'replace_as'), True):
                    pass
                    l_1_remove_private_as_ingress_cli = str_join(((undefined(name='remove_private_as_ingress_cli') if l_1_remove_private_as_ingress_cli is missing else l_1_remove_private_as_ingress_cli), ' replace-as', ))
                    _loop_vars['remove_private_as_ingress_cli'] = l_1_remove_private_as_ingress_cli
                yield '   '
                yield str((undefined(name='remove_private_as_ingress_cli') if l_1_remove_private_as_ingress_cli is missing else l_1_remove_private_as_ingress_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'remove_private_as_ingress'), 'enabled'), False):
                pass
                yield '   no neighbor '
                yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                yield ' remove-private-as ingress\n'
        l_1_neighbor = l_1_remove_private_as_cli = l_1_allowas_in_cli = l_1_neighbor_rib_in_pre_policy_retain_cli = l_1_hide_passwords = l_1_default_originate_cli = l_1_maximum_routes_cli = l_1_link_bandwidth_cli = l_1_remove_private_as_ingress_cli = missing
        if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'redistribute_internal'), True):
            pass
            yield '   bgp redistribute-internal\n'
        elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'bgp'), 'redistribute_internal'), False):
            pass
            yield '   no bgp redistribute-internal\n'
        for l_1_aggregate_address in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'aggregate_addresses'), 'prefix'):
            l_1_aggregate_address_cli = missing
            _loop_vars = {}
            pass
            l_1_aggregate_address_cli = str_join(('aggregate-address ', environment.getattr(l_1_aggregate_address, 'prefix'), ))
            _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            if t_6(environment.getattr(l_1_aggregate_address, 'as_set'), True):
                pass
                l_1_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli), ' as-set', ))
                _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            if t_6(environment.getattr(l_1_aggregate_address, 'summary_only'), True):
                pass
                l_1_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli), ' summary-only', ))
                _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            if t_6(environment.getattr(l_1_aggregate_address, 'attribute_map')):
                pass
                l_1_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli), ' attribute-map ', environment.getattr(l_1_aggregate_address, 'attribute_map'), ))
                _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            if t_6(environment.getattr(l_1_aggregate_address, 'match_map')):
                pass
                l_1_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli), ' match-map ', environment.getattr(l_1_aggregate_address, 'match_map'), ))
                _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            if t_6(environment.getattr(l_1_aggregate_address, 'advertise_only'), True):
                pass
                l_1_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli), ' advertise-only', ))
                _loop_vars['aggregate_address_cli'] = l_1_aggregate_address_cli
            yield '   '
            yield str((undefined(name='aggregate_address_cli') if l_1_aggregate_address_cli is missing else l_1_aggregate_address_cli))
            yield '\n'
        l_1_aggregate_address = l_1_aggregate_address_cli = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'redistribute')):
            pass
            l_0_redistribute_var = environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'redistribute')
            context.vars['redistribute_var'] = l_0_redistribute_var
            context.exported_vars.add('redistribute_var')
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'enabled'), True):
                pass
                l_0_redistribute_conn = 'redistribute connected'
                context.vars['redistribute_conn'] = l_0_redistribute_conn
                context.exported_vars.add('redistribute_conn')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' include leaked', ))
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map')):
                    pass
                    l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map'), ))
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf')):
                    pass
                    l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf'), ))
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                yield '   '
                yield str((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'enabled'), True):
                pass
                l_0_redistribute_isis = 'redistribute isis'
                context.vars['redistribute_isis'] = l_0_redistribute_isis
                context.exported_vars.add('redistribute_isis')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level')):
                    pass
                    l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level'), ))
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' include leaked', ))
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map')):
                    pass
                    l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map'), ))
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf')):
                    pass
                    l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf'), ))
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                yield '   '
                yield str((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'enabled'), True):
                pass
                l_0_redistribute_ospf = 'redistribute ospf'
                context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                context.exported_vars.add('redistribute_ospf')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' include leaked', ))
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map')):
                    pass
                    l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map'), ))
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                yield '   '
                yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                pass
                l_0_redistribute_ospf = 'redistribute ospf match internal'
                context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                context.exported_vars.add('redistribute_ospf')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' include leaked', ))
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                    pass
                    l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                yield '   '
                yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                pass
                l_0_redistribute_ospf_match = 'redistribute ospf match external'
                context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                context.exported_vars.add('redistribute_ospf_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' include leaked', ))
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                    pass
                    l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                yield '   '
                yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                pass
                l_0_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                context.exported_vars.add('redistribute_ospf_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                    pass
                    l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' include leaked', ))
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                    pass
                    l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                yield '   '
                yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'enabled'), True):
                pass
                l_0_redistribute_ospfv3 = 'redistribute ospfv3'
                context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                context.exported_vars.add('redistribute_ospfv3')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map')):
                    pass
                    l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map'), ))
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                yield '   '
                yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                pass
                l_0_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                context.exported_vars.add('redistribute_ospfv3')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                    pass
                    l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                yield '   '
                yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                pass
                l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                context.exported_vars.add('redistribute_ospfv3_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                    pass
                    l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                yield '   '
                yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                pass
                l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                context.exported_vars.add('redistribute_ospfv3_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                    pass
                    l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                    pass
                    l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                yield '   '
                yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'enabled'), True):
                pass
                l_0_redistribute_static = 'redistribute static'
                context.vars['redistribute_static'] = l_0_redistribute_static
                context.exported_vars.add('redistribute_static')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'include_leaked'), True):
                    pass
                    l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' include leaked', ))
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map')):
                    pass
                    l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map'), ))
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf')):
                    pass
                    l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf'), ))
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                yield '   '
                yield str((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'enabled'), True):
                pass
                l_0_redistribute_rip = 'redistribute rip'
                context.vars['redistribute_rip'] = l_0_redistribute_rip
                context.exported_vars.add('redistribute_rip')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'route_map')):
                    pass
                    l_0_redistribute_rip = str_join(((undefined(name='redistribute_rip') if l_0_redistribute_rip is missing else l_0_redistribute_rip), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'route_map'), ))
                    context.vars['redistribute_rip'] = l_0_redistribute_rip
                    context.exported_vars.add('redistribute_rip')
                yield '   '
                yield str((undefined(name='redistribute_rip') if l_0_redistribute_rip is missing else l_0_redistribute_rip))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'enabled'), True):
                pass
                l_0_redistribute_host = 'redistribute attached-host'
                context.vars['redistribute_host'] = l_0_redistribute_host
                context.exported_vars.add('redistribute_host')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map')):
                    pass
                    l_0_redistribute_host = str_join(((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map'), ))
                    context.vars['redistribute_host'] = l_0_redistribute_host
                    context.exported_vars.add('redistribute_host')
                yield '   '
                yield str((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'enabled'), True):
                pass
                l_0_redistribute_dynamic = 'redistribute dynamic'
                context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                context.exported_vars.add('redistribute_dynamic')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map')):
                    pass
                    l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map'), ))
                    context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                    context.exported_vars.add('redistribute_dynamic')
                elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf')):
                    pass
                    l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf'), ))
                    context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                    context.exported_vars.add('redistribute_dynamic')
                yield '   '
                yield str((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'enabled'), True):
                pass
                l_0_redistribute_bgp = 'redistribute bgp leaked'
                context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                context.exported_vars.add('redistribute_bgp')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map')):
                    pass
                    l_0_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map'), ))
                    context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                    context.exported_vars.add('redistribute_bgp')
                yield '   '
                yield str((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'enabled'), True):
                pass
                l_0_redistribute_user = 'redistribute user'
                context.vars['redistribute_user'] = l_0_redistribute_user
                context.exported_vars.add('redistribute_user')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf')):
                    pass
                    l_0_redistribute_user = str_join(((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf'), ))
                    context.vars['redistribute_user'] = l_0_redistribute_user
                    context.exported_vars.add('redistribute_user')
                yield '   '
                yield str((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user))
                yield '\n'
        elif t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'redistribute_routes')):
            pass
            for l_1_redistribute_route in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'redistribute_routes'), 'source_protocol'):
                l_1_redistribute_route_cli = missing
                _loop_vars = {}
                pass
                l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                if (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                    pass
                    if t_6(environment.getattr(l_1_redistribute_route, 'ospf_route_type')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                if (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'bgp'):
                    pass
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' leaked', ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                elif t_6(environment.getattr(l_1_redistribute_route, 'include_leaked'), True):
                    pass
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                if t_6(environment.getattr(l_1_redistribute_route, 'route_map')):
                    pass
                    l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                elif (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                    pass
                    if t_6(environment.getattr(l_1_redistribute_route, 'rcf')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' rcf ', environment.getattr(l_1_redistribute_route, 'rcf'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                yield '   '
                yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                yield '\n'
            l_1_redistribute_route = l_1_redistribute_route_cli = missing
        for l_1_neighbor_interface in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'neighbor_interfaces'), 'name'):
            _loop_vars = {}
            pass
            if (t_6(environment.getattr(l_1_neighbor_interface, 'peer_group')) and t_6(environment.getattr(l_1_neighbor_interface, 'remote_as'))):
                pass
                yield '   neighbor interface '
                yield str(environment.getattr(l_1_neighbor_interface, 'name'))
                yield ' peer-group '
                yield str(environment.getattr(l_1_neighbor_interface, 'peer_group'))
                yield ' remote-as '
                yield str(environment.getattr(l_1_neighbor_interface, 'remote_as'))
                yield '\n'
            elif (t_6(environment.getattr(l_1_neighbor_interface, 'peer_group')) and t_6(environment.getattr(l_1_neighbor_interface, 'peer_filter'))):
                pass
                yield '   neighbor interface '
                yield str(environment.getattr(l_1_neighbor_interface, 'name'))
                yield ' peer-group '
                yield str(environment.getattr(l_1_neighbor_interface, 'peer_group'))
                yield ' peer-filter '
                yield str(environment.getattr(l_1_neighbor_interface, 'peer_filter'))
                yield '\n'
        l_1_neighbor_interface = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vlans')):
            pass
            for l_1_vlan in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vlans')):
                _loop_vars = {}
                pass
                yield '   !\n   vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield '\n'
                if t_6(environment.getattr(l_1_vlan, 'rd')):
                    pass
                    yield '      rd '
                    yield str(environment.getattr(l_1_vlan, 'rd'))
                    yield '\n'
                if (t_6(environment.getattr(environment.getattr(l_1_vlan, 'rd_evpn_domain'), 'domain')) and t_6(environment.getattr(environment.getattr(l_1_vlan, 'rd_evpn_domain'), 'rd'))):
                    pass
                    yield '      rd evpn domain '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'rd_evpn_domain'), 'domain'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'rd_evpn_domain'), 'rd'))
                    yield '\n'
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'both')):
                    _loop_vars = {}
                    pass
                    yield '      route-target both '
                    yield str(l_2_route_target)
                    yield '\n'
                l_2_route_target = missing
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'import')):
                    _loop_vars = {}
                    pass
                    yield '      route-target import '
                    yield str(l_2_route_target)
                    yield '\n'
                l_2_route_target = missing
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'export')):
                    _loop_vars = {}
                    pass
                    yield '      route-target export '
                    yield str(l_2_route_target)
                    yield '\n'
                l_2_route_target = missing
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'import_evpn_domains')):
                    _loop_vars = {}
                    pass
                    yield '      route-target import evpn domain '
                    yield str(environment.getattr(l_2_route_target, 'domain'))
                    yield ' '
                    yield str(environment.getattr(l_2_route_target, 'route_target'))
                    yield '\n'
                l_2_route_target = missing
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'export_evpn_domains')):
                    _loop_vars = {}
                    pass
                    yield '      route-target export evpn domain '
                    yield str(environment.getattr(l_2_route_target, 'domain'))
                    yield ' '
                    yield str(environment.getattr(l_2_route_target, 'route_target'))
                    yield '\n'
                l_2_route_target = missing
                for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan, 'route_targets'), 'import_export_evpn_domains')):
                    _loop_vars = {}
                    pass
                    yield '      route-target import export evpn domain '
                    yield str(environment.getattr(l_2_route_target, 'domain'))
                    yield ' '
                    yield str(environment.getattr(l_2_route_target, 'route_target'))
                    yield '\n'
                l_2_route_target = missing
                for l_2_redistribute_route in t_3(environment.getattr(l_1_vlan, 'redistribute_routes')):
                    _loop_vars = {}
                    pass
                    yield '      redistribute '
                    yield str(l_2_redistribute_route)
                    yield '\n'
                l_2_redistribute_route = missing
                for l_2_no_redistribute_route in t_3(environment.getattr(l_1_vlan, 'no_redistribute_routes')):
                    _loop_vars = {}
                    pass
                    yield '      no redistribute '
                    yield str(l_2_no_redistribute_route)
                    yield '\n'
                l_2_no_redistribute_route = missing
                if t_6(environment.getattr(l_1_vlan, 'eos_cli')):
                    pass
                    yield '      !\n      '
                    yield str(t_4(environment.getattr(l_1_vlan, 'eos_cli'), 6, False))
                    yield '\n'
            l_1_vlan = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vpws')):
            pass
            for l_1_vpws_service in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vpws'), 'name'):
                _loop_vars = {}
                pass
                yield '   !\n'
                if t_6(environment.getattr(l_1_vpws_service, 'name')):
                    pass
                    yield '   vpws '
                    yield str(environment.getattr(l_1_vpws_service, 'name'))
                    yield '\n'
                    if t_6(environment.getattr(l_1_vpws_service, 'rd')):
                        pass
                        yield '      rd '
                        yield str(environment.getattr(l_1_vpws_service, 'rd'))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(l_1_vpws_service, 'route_targets'), 'import_export')):
                        pass
                        yield '      route-target import export evpn '
                        yield str(environment.getattr(environment.getattr(l_1_vpws_service, 'route_targets'), 'import_export'))
                        yield '\n'
                    if t_6(environment.getattr(l_1_vpws_service, 'mpls_control_word'), True):
                        pass
                        yield '      mpls control-word\n'
                    if t_6(environment.getattr(l_1_vpws_service, 'label_flow'), True):
                        pass
                        yield '      label flow\n'
                    if t_6(environment.getattr(l_1_vpws_service, 'mtu')):
                        pass
                        yield '      mtu '
                        yield str(environment.getattr(l_1_vpws_service, 'mtu'))
                        yield '\n'
                    for l_2_pw in t_3(environment.getattr(l_1_vpws_service, 'pseudowires'), 'name'):
                        _loop_vars = {}
                        pass
                        if ((t_6(environment.getattr(l_2_pw, 'name')) and t_6(environment.getattr(l_2_pw, 'id_local'))) and t_6(environment.getattr(l_2_pw, 'id_remote'))):
                            pass
                            yield '      !\n      pseudowire '
                            yield str(environment.getattr(l_2_pw, 'name'))
                            yield '\n         evpn vpws id local '
                            yield str(environment.getattr(l_2_pw, 'id_local'))
                            yield ' remote '
                            yield str(environment.getattr(l_2_pw, 'id_remote'))
                            yield '\n'
                    l_2_pw = missing
            l_1_vpws_service = missing
        for l_1_vlan_aware_bundle in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vlan_aware_bundles'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   vlan-aware-bundle '
            yield str(environment.getattr(l_1_vlan_aware_bundle, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_vlan_aware_bundle, 'rd')):
                pass
                yield '      rd '
                yield str(environment.getattr(l_1_vlan_aware_bundle, 'rd'))
                yield '\n'
            if (t_6(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'rd_evpn_domain'), 'domain')) and t_6(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'rd_evpn_domain'), 'rd'))):
                pass
                yield '      rd evpn domain '
                yield str(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'rd_evpn_domain'), 'domain'))
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'rd_evpn_domain'), 'rd'))
                yield '\n'
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'both')):
                _loop_vars = {}
                pass
                yield '      route-target both '
                yield str(l_2_route_target)
                yield '\n'
            l_2_route_target = missing
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'import')):
                _loop_vars = {}
                pass
                yield '      route-target import '
                yield str(l_2_route_target)
                yield '\n'
            l_2_route_target = missing
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'export')):
                _loop_vars = {}
                pass
                yield '      route-target export '
                yield str(l_2_route_target)
                yield '\n'
            l_2_route_target = missing
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'import_evpn_domains')):
                _loop_vars = {}
                pass
                yield '      route-target import evpn domain '
                yield str(environment.getattr(l_2_route_target, 'domain'))
                yield ' '
                yield str(environment.getattr(l_2_route_target, 'route_target'))
                yield '\n'
            l_2_route_target = missing
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'export_evpn_domains')):
                _loop_vars = {}
                pass
                yield '      route-target export evpn domain '
                yield str(environment.getattr(l_2_route_target, 'domain'))
                yield ' '
                yield str(environment.getattr(l_2_route_target, 'route_target'))
                yield '\n'
            l_2_route_target = missing
            for l_2_route_target in t_3(environment.getattr(environment.getattr(l_1_vlan_aware_bundle, 'route_targets'), 'import_export_evpn_domains')):
                _loop_vars = {}
                pass
                yield '      route-target import export evpn domain '
                yield str(environment.getattr(l_2_route_target, 'domain'))
                yield ' '
                yield str(environment.getattr(l_2_route_target, 'route_target'))
                yield '\n'
            l_2_route_target = missing
            for l_2_redistribute_route in t_3(environment.getattr(l_1_vlan_aware_bundle, 'redistribute_routes')):
                _loop_vars = {}
                pass
                yield '      redistribute '
                yield str(l_2_redistribute_route)
                yield '\n'
            l_2_redistribute_route = missing
            for l_2_no_redistribute_route in t_3(environment.getattr(l_1_vlan_aware_bundle, 'no_redistribute_routes')):
                _loop_vars = {}
                pass
                yield '      no redistribute '
                yield str(l_2_no_redistribute_route)
                yield '\n'
            l_2_no_redistribute_route = missing
            yield '      vlan '
            yield str(environment.getattr(l_1_vlan_aware_bundle, 'vlan'))
            yield '\n'
            if t_6(environment.getattr(l_1_vlan_aware_bundle, 'eos_cli')):
                pass
                yield '      !\n      '
                yield str(t_4(environment.getattr(l_1_vlan_aware_bundle, 'eos_cli'), 6, False))
                yield '\n'
        l_1_vlan_aware_bundle = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn')):
            pass
            yield '   !\n   address-family evpn\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'route'), 'export_ethernet_segment_ip_mass_withdraw'), True):
                pass
                yield '      route export ethernet-segment ip mass-withdraw\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'route'), 'import_ethernet_segment_ip_mass_withdraw'), True):
                pass
                yield '      route import ethernet-segment ip mass-withdraw\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'any'), True):
                pass
                yield '      bgp additional-paths send any\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'backup'), True):
                pass
                yield '      bgp additional-paths send backup\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'ecmp'), True):
                pass
                yield '      bgp additional-paths send ecmp\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'limit')):
                pass
                yield '      bgp additional-paths send ecmp limit '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'limit'))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'limit')):
                pass
                yield '      bgp additional-paths send limit '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'bgp_additional_paths'), 'send'), 'limit'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'next_hop_unchanged'), True):
                pass
                yield '      bgp next-hop-unchanged\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'encapsulation'), 'mpls'):
                pass
                l_0_evpn_neighbor_default_encap_cli = 'neighbor default encapsulation mpls'
                context.vars['evpn_neighbor_default_encap_cli'] = l_0_evpn_neighbor_default_encap_cli
                context.exported_vars.add('evpn_neighbor_default_encap_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'next_hop_self_source_interface')):
                    pass
                    l_0_evpn_neighbor_default_encap_cli = str_join(((undefined(name='evpn_neighbor_default_encap_cli') if l_0_evpn_neighbor_default_encap_cli is missing else l_0_evpn_neighbor_default_encap_cli), ' next-hop-self source-interface ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'next_hop_self_source_interface'), ))
                    context.vars['evpn_neighbor_default_encap_cli'] = l_0_evpn_neighbor_default_encap_cli
                    context.exported_vars.add('evpn_neighbor_default_encap_cli')
                yield '      '
                yield str((undefined(name='evpn_neighbor_default_encap_cli') if l_0_evpn_neighbor_default_encap_cli is missing else l_0_evpn_neighbor_default_encap_cli))
                yield '\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'encapsulation'), 'path-selection'):
                pass
                yield '      neighbor default encapsulation path-selection\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'next_hop_mpls_resolution_ribs')):
                pass
                l_0_evpn_mpls_resolution_ribs = []
                context.vars['evpn_mpls_resolution_ribs'] = l_0_evpn_mpls_resolution_ribs
                context.exported_vars.add('evpn_mpls_resolution_ribs')
                for l_1_rib in environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'next_hop_mpls_resolution_ribs'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_1_rib, 'rib_type'), 'tunnel-rib-colored'):
                        pass
                        context.call(environment.getattr((undefined(name='evpn_mpls_resolution_ribs') if l_0_evpn_mpls_resolution_ribs is missing else l_0_evpn_mpls_resolution_ribs), 'append'), 'tunnel-rib colored system-colored-tunnel-rib', _loop_vars=_loop_vars)
                    elif (t_6(environment.getattr(l_1_rib, 'rib_type'), 'tunnel-rib') and t_6(environment.getattr(l_1_rib, 'rib_name'))):
                        pass
                        context.call(environment.getattr((undefined(name='evpn_mpls_resolution_ribs') if l_0_evpn_mpls_resolution_ribs is missing else l_0_evpn_mpls_resolution_ribs), 'append'), str_join(('tunnel-rib ', environment.getattr(l_1_rib, 'rib_name'), )), _loop_vars=_loop_vars)
                    elif t_6(environment.getattr(l_1_rib, 'rib_type')):
                        pass
                        context.call(environment.getattr((undefined(name='evpn_mpls_resolution_ribs') if l_0_evpn_mpls_resolution_ribs is missing else l_0_evpn_mpls_resolution_ribs), 'append'), environment.getattr(l_1_rib, 'rib_type'), _loop_vars=_loop_vars)
                l_1_rib = missing
                if (undefined(name='evpn_mpls_resolution_ribs') if l_0_evpn_mpls_resolution_ribs is missing else l_0_evpn_mpls_resolution_ribs):
                    pass
                    yield '      next-hop mpls resolution ribs '
                    yield str(t_5(context.eval_ctx, (undefined(name='evpn_mpls_resolution_ribs') if l_0_evpn_mpls_resolution_ribs is missing else l_0_evpn_mpls_resolution_ribs), ' '))
                    yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'peer_groups'), 'name'):
                l_1_peer_group_default_route_cli = resolve('peer_group_default_route_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'enabled'), True):
                    pass
                    l_1_peer_group_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' default-route', ))
                    _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    yield '      '
                    yield str((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_peer_group, 'name'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send'))
                        yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'encapsulation')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' encapsulation '
                    yield str(environment.getattr(l_1_peer_group, 'encapsulation'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'domain_remote'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' domain remote\n'
            l_1_peer_group = l_1_peer_group_default_route_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbors'), 'ip_address'):
                l_1_neighbor_default_route_cli = resolve('neighbor_default_route_cli')
                l_1_encapsulation_cli = resolve('encapsulation_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'enabled'), True):
                    pass
                    l_1_neighbor_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' default-route', ))
                    _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send'))
                        yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'encapsulation')):
                    pass
                    l_1_encapsulation_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' encapsulation ', environment.getattr(l_1_neighbor, 'encapsulation'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    if ((environment.getattr(l_1_neighbor, 'encapsulation') == 'mpls') and t_6(environment.getattr(l_1_neighbor, 'next_hop_self_source_interface'))):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' next-hop-self source-interface ', environment.getattr(l_1_neighbor, 'next_hop_self_source_interface'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    yield '      '
                    yield str((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli))
                    yield '\n'
            l_1_neighbor = l_1_neighbor_default_route_cli = l_1_encapsulation_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'domain_identifier')):
                pass
                yield '      domain identifier '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'domain_identifier'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'domain_identifier_remote')):
                pass
                yield '      domain identifier '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'domain_identifier_remote'))
                yield ' remote\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'next_hop'), 'resolution_disabled'), True):
                pass
                yield '      next-hop resolution disabled\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'route'), 'import_match_failure_action'), 'discard'):
                pass
                yield '      route import match-failure action discard\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'next_hop_self_received_evpn_routes'), 'enable'), True):
                pass
                l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli = 'neighbor default next-hop-self received-evpn-routes route-type ip-prefix'
                context.vars['evpn_neighbor_default_nhs_received_evpn_routes_cli'] = l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli
                context.exported_vars.add('evpn_neighbor_default_nhs_received_evpn_routes_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'neighbor_default'), 'next_hop_self_received_evpn_routes'), 'inter_domain'), True):
                    pass
                    l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli = str_join(((undefined(name='evpn_neighbor_default_nhs_received_evpn_routes_cli') if l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli is missing else l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli), ' inter-domain', ))
                    context.vars['evpn_neighbor_default_nhs_received_evpn_routes_cli'] = l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli
                    context.exported_vars.add('evpn_neighbor_default_nhs_received_evpn_routes_cli')
                yield '      '
                yield str((undefined(name='evpn_neighbor_default_nhs_received_evpn_routes_cli') if l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli is missing else l_0_evpn_neighbor_default_nhs_received_evpn_routes_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'enabled'), False):
                pass
                yield '      no host-flap detection\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'enabled'), True):
                pass
                l_0_hostflap_detection_cli = ''
                context.vars['hostflap_detection_cli'] = l_0_hostflap_detection_cli
                context.exported_vars.add('hostflap_detection_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'window')):
                    pass
                    l_0_hostflap_detection_cli = str_join(((undefined(name='hostflap_detection_cli') if l_0_hostflap_detection_cli is missing else l_0_hostflap_detection_cli), ' window ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'window'), ))
                    context.vars['hostflap_detection_cli'] = l_0_hostflap_detection_cli
                    context.exported_vars.add('hostflap_detection_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'threshold')):
                    pass
                    l_0_hostflap_detection_cli = str_join(((undefined(name='hostflap_detection_cli') if l_0_hostflap_detection_cli is missing else l_0_hostflap_detection_cli), ' threshold ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'threshold'), ))
                    context.vars['hostflap_detection_cli'] = l_0_hostflap_detection_cli
                    context.exported_vars.add('hostflap_detection_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'expiry_timeout')):
                    pass
                    l_0_hostflap_detection_cli = str_join(((undefined(name='hostflap_detection_cli') if l_0_hostflap_detection_cli is missing else l_0_hostflap_detection_cli), ' expiry timeout ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_hostflap_detection'), 'expiry_timeout'), ' seconds', ))
                    context.vars['hostflap_detection_cli'] = l_0_hostflap_detection_cli
                    context.exported_vars.add('hostflap_detection_cli')
                if ((undefined(name='hostflap_detection_cli') if l_0_hostflap_detection_cli is missing else l_0_hostflap_detection_cli) != ''):
                    pass
                    yield '      host-flap detection'
                    yield str((undefined(name='hostflap_detection_cli') if l_0_hostflap_detection_cli is missing else l_0_hostflap_detection_cli))
                    yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'layer_2_fec_in_place_update'), 'enabled'), True):
                pass
                l_0_layer2_cli = 'layer-2 fec in-place update'
                context.vars['layer2_cli'] = l_0_layer2_cli
                context.exported_vars.add('layer2_cli')
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'layer_2_fec_in_place_update'), 'timeout')):
                    pass
                    l_0_layer2_cli = str_join(((undefined(name='layer2_cli') if l_0_layer2_cli is missing else l_0_layer2_cli), ' timeout ', environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'layer_2_fec_in_place_update'), 'timeout'), ' seconds', ))
                    context.vars['layer2_cli'] = l_0_layer2_cli
                    context.exported_vars.add('layer2_cli')
                yield '      '
                yield str((undefined(name='layer2_cli') if l_0_layer2_cli is missing else l_0_layer2_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'route'), 'import_overlay_index_gateway'), True):
                pass
                yield '      route import overlay-index gateway\n'
            for l_1_segment in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_evpn'), 'evpn_ethernet_segment'), 'domain'):
                _loop_vars = {}
                pass
                yield '      !\n      evpn ethernet-segment domain '
                yield str(environment.getattr(l_1_segment, 'domain'))
                yield '\n'
                if t_6(environment.getattr(l_1_segment, 'identifier')):
                    pass
                    yield '         identifier '
                    yield str(environment.getattr(l_1_segment, 'identifier'))
                    yield '\n'
                if t_6(environment.getattr(l_1_segment, 'route_target_import')):
                    pass
                    yield '         route-target import '
                    yield str(environment.getattr(l_1_segment, 'route_target_import'))
                    yield '\n'
            l_1_segment = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4')):
            pass
            yield '   !\n   address-family flow-spec ipv4\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                pass
                yield '      bgp missing-policy direction in action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                pass
                yield '      bgp missing-policy direction out action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv4'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
            l_1_neighbor = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6')):
            pass
            yield '   !\n   address-family flow-spec ipv6\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                pass
                yield '      bgp missing-policy direction in action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                pass
                yield '      bgp missing-policy direction out action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_flow_spec_ipv6'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
            l_1_neighbor = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4')):
            pass
            yield '   !\n   address-family ipv4\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'install'), True):
                pass
                yield '      bgp additional-paths install\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'install_ecmp_primary'), True):
                pass
                yield '      bgp additional-paths install ecmp-primary\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'peer_groups'), 'name'):
                l_1_neighbor_default_originate_cli = resolve('neighbor_default_originate_cli')
                l_1_add_path_cli = resolve('add_path_cli')
                l_1_nexthop_v6_cli = resolve('nexthop_v6_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'prefix_list_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_peer_group, 'prefix_list_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'prefix_list_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_peer_group, 'prefix_list_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'default_originate')):
                    pass
                    l_1_neighbor_default_originate_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' default-originate', ))
                    _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'route_map')):
                        pass
                        l_1_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli), ' route-map ', environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'route_map'), ))
                        _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_originate'), 'always'), True):
                        pass
                        l_1_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli), ' always', ))
                        _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send\n'
                    else:
                        pass
                        if (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send ecmp limit ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        elif (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')):
                                pass
                                l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send limit ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'), ))
                                _loop_vars['add_path_cli'] = l_1_add_path_cli
                        else:
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'prefix_list')) and t_6((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli))):
                            pass
                            l_1_add_path_cli = str_join(((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli), ' prefix-list ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'prefix_list'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli)):
                            pass
                            yield '      '
                            yield str((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli))
                            yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_peer_group, 'next_hop'), 'address_family_ipv6'), 'enabled'), True):
                    pass
                    l_1_nexthop_v6_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' next-hop address-family ipv6', ))
                    _loop_vars['nexthop_v6_cli'] = l_1_nexthop_v6_cli
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_peer_group, 'next_hop'), 'address_family_ipv6'), 'originate'), True):
                        pass
                        l_1_nexthop_v6_cli = str_join(((undefined(name='nexthop_v6_cli') if l_1_nexthop_v6_cli is missing else l_1_nexthop_v6_cli), ' originate', ))
                        _loop_vars['nexthop_v6_cli'] = l_1_nexthop_v6_cli
                    yield '      '
                    yield str((undefined(name='nexthop_v6_cli') if l_1_nexthop_v6_cli is missing else l_1_nexthop_v6_cli))
                    yield '\n'
            l_1_peer_group = l_1_neighbor_default_originate_cli = l_1_add_path_cli = l_1_nexthop_v6_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'neighbors'), 'ip_address'):
                l_1_neighbor_default_originate_cli = resolve('neighbor_default_originate_cli')
                l_1_add_path_cli = resolve('add_path_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'prefix_list_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_neighbor, 'prefix_list_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'prefix_list_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_neighbor, 'prefix_list_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'default_originate')):
                    pass
                    l_1_neighbor_default_originate_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' default-originate', ))
                    _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'route_map')):
                        pass
                        l_1_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli), ' route-map ', environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'route_map'), ))
                        _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_originate'), 'always'), True):
                        pass
                        l_1_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli), ' always', ))
                        _loop_vars['neighbor_default_originate_cli'] = l_1_neighbor_default_originate_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_originate_cli') if l_1_neighbor_default_originate_cli is missing else l_1_neighbor_default_originate_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    else:
                        pass
                        if (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send ecmp limit ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        elif (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')):
                                pass
                                l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send limit ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'), ))
                                _loop_vars['add_path_cli'] = l_1_add_path_cli
                        else:
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'prefix_list')):
                            pass
                            l_1_add_path_cli = str_join(((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli), ' prefix-list ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'prefix_list'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli)):
                            pass
                            yield '      '
                            yield str((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli))
                            yield '\n'
            l_1_neighbor = l_1_neighbor_default_originate_cli = l_1_add_path_cli = missing
            for l_1_network in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'networks'), 'prefix'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_network, 'route_map')):
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_1_network, 'prefix'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_network, 'route_map'))
                    yield '\n'
                else:
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_1_network, 'prefix'))
                    yield '\n'
            l_1_network = missing
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'redistribute_internal'), True):
                pass
                yield '      bgp redistribute-internal\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'bgp'), 'redistribute_internal'), False):
                pass
                yield '      no bgp redistribute-internal\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'redistribute')):
                pass
                l_0_redistribute_var = environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'redistribute')
                context.vars['redistribute_var'] = l_0_redistribute_var
                context.exported_vars.add('redistribute_var')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'enabled'), True):
                    pass
                    l_0_redistribute_host = 'redistribute attached-host'
                    context.vars['redistribute_host'] = l_0_redistribute_host
                    context.exported_vars.add('redistribute_host')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map')):
                        pass
                        l_0_redistribute_host = str_join(((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map'), ))
                        context.vars['redistribute_host'] = l_0_redistribute_host
                        context.exported_vars.add('redistribute_host')
                    yield '      '
                    yield str((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'enabled'), True):
                    pass
                    l_0_redistribute_bgp = 'redistribute bgp leaked'
                    context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                    context.exported_vars.add('redistribute_bgp')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map')):
                        pass
                        l_0_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map'), ))
                        context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                        context.exported_vars.add('redistribute_bgp')
                    yield '      '
                    yield str((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'enabled'), True):
                    pass
                    l_0_redistribute_conn = 'redistribute connected'
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' include leaked', ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    yield '      '
                    yield str((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'enabled'), True):
                    pass
                    l_0_redistribute_dynamic = 'redistribute dynamic'
                    context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                    context.exported_vars.add('redistribute_dynamic')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map')):
                        pass
                        l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map'), ))
                        context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                        context.exported_vars.add('redistribute_dynamic')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf')):
                        pass
                        l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf'), ))
                        context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                        context.exported_vars.add('redistribute_dynamic')
                    yield '      '
                    yield str((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'enabled'), True):
                    pass
                    l_0_redistribute_user = 'redistribute user'
                    context.vars['redistribute_user'] = l_0_redistribute_user
                    context.exported_vars.add('redistribute_user')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf')):
                        pass
                        l_0_redistribute_user = str_join(((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf'), ))
                        context.vars['redistribute_user'] = l_0_redistribute_user
                        context.exported_vars.add('redistribute_user')
                    yield '      '
                    yield str((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'enabled'), True):
                    pass
                    l_0_redistribute_isis = 'redistribute isis'
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' include leaked', ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    yield '      '
                    yield str((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' include leaked', ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf match internal'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' include leaked', ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' include leaked', ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' include leaked', ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'enabled'), True):
                    pass
                    l_0_redistribute_rip = 'redistribute rip'
                    context.vars['redistribute_rip'] = l_0_redistribute_rip
                    context.exported_vars.add('redistribute_rip')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'route_map')):
                        pass
                        l_0_redistribute_rip = str_join(((undefined(name='redistribute_rip') if l_0_redistribute_rip is missing else l_0_redistribute_rip), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'rip'), 'route_map'), ))
                        context.vars['redistribute_rip'] = l_0_redistribute_rip
                        context.exported_vars.add('redistribute_rip')
                    yield '      '
                    yield str((undefined(name='redistribute_rip') if l_0_redistribute_rip is missing else l_0_redistribute_rip))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'enabled'), True):
                    pass
                    l_0_redistribute_static = 'redistribute static'
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' include leaked', ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    yield '      '
                    yield str((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static))
                    yield '\n'
            elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'redistribute_routes')):
                pass
                for l_1_redistribute_route in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4'), 'redistribute_routes'), 'source_protocol'):
                    l_1_redistribute_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'ospf_route_type')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'bgp'):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif (t_6(environment.getattr(l_1_redistribute_route, 'include_leaked'), True) and (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'ospf', 'ospfv3'])):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if t_6(environment.getattr(l_1_redistribute_route, 'route_map')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'rcf')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' rcf ', environment.getattr(l_1_redistribute_route, 'rcf'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    yield '      '
                    yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                    yield '\n'
                l_1_redistribute_route = l_1_redistribute_route_cli = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast')):
            pass
            yield '   !\n   address-family ipv4 labeled-unicast\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'update_wait_for_convergence'), True):
                pass
                yield '      update wait-for-convergence\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'missing_policy')):
                pass
                for l_1_direction in ['in', 'out']:
                    l_1_missing_policy_cli = resolve('missing_policy_cli')
                    l_1_dir = l_1_policy = missing
                    _loop_vars = {}
                    pass
                    l_1_dir = str_join(('direction_', l_1_direction, ))
                    _loop_vars['dir'] = l_1_dir
                    l_1_policy = environment.getitem(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'missing_policy'), (undefined(name='dir') if l_1_dir is missing else l_1_dir))
                    _loop_vars['policy'] = l_1_policy
                    if t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'action')):
                        pass
                        l_1_missing_policy_cli = 'bgp missing-policy'
                        _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                        if ((t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_community_list'), True) or t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_prefix_list'), True)) or t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_sub_route_map'), True)):
                            pass
                            l_1_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli), ' include', ))
                            _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_community_list'), True):
                                pass
                                l_1_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli), ' community-list', ))
                                _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_prefix_list'), True):
                                pass
                                l_1_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli), ' prefix-list', ))
                                _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                            if t_6(environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'include_sub_route_map'), True):
                                pass
                                l_1_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli), ' sub-route-map', ))
                                _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                        l_1_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli), ' direction ', l_1_direction, ' action ', environment.getattr((undefined(name='policy') if l_1_policy is missing else l_1_policy), 'action'), ))
                        _loop_vars['missing_policy_cli'] = l_1_missing_policy_cli
                        yield '      '
                        yield str((undefined(name='missing_policy_cli') if l_1_missing_policy_cli is missing else l_1_missing_policy_cli))
                        yield '\n'
                l_1_direction = l_1_dir = l_1_policy = l_1_missing_policy_cli = missing
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'bgp'), 'next_hop_unchanged'), True):
                pass
                yield '      bgp next-hop-unchanged\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'neighbor_default'), 'next_hop_self'), True):
                pass
                yield '      neighbor default next-hop-self\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'next_hop_resolution_ribs')):
                pass
                l_0_v4_bgp_lu_resolution_ribs = []
                context.vars['v4_bgp_lu_resolution_ribs'] = l_0_v4_bgp_lu_resolution_ribs
                context.exported_vars.add('v4_bgp_lu_resolution_ribs')
                for l_1_rib in environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'next_hop_resolution_ribs'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_1_rib, 'rib_type'), 'tunnel-rib-colored'):
                        pass
                        context.call(environment.getattr((undefined(name='v4_bgp_lu_resolution_ribs') if l_0_v4_bgp_lu_resolution_ribs is missing else l_0_v4_bgp_lu_resolution_ribs), 'append'), 'tunnel-rib colored system-colored-tunnel-rib', _loop_vars=_loop_vars)
                    elif t_6(environment.getattr(l_1_rib, 'rib_type'), 'tunnel-rib'):
                        pass
                        if t_6(environment.getattr(l_1_rib, 'rib_name')):
                            pass
                            context.call(environment.getattr((undefined(name='v4_bgp_lu_resolution_ribs') if l_0_v4_bgp_lu_resolution_ribs is missing else l_0_v4_bgp_lu_resolution_ribs), 'append'), str_join(('tunnel-rib ', environment.getattr(l_1_rib, 'rib_name'), )), _loop_vars=_loop_vars)
                    elif t_6(environment.getattr(l_1_rib, 'rib_type')):
                        pass
                        context.call(environment.getattr((undefined(name='v4_bgp_lu_resolution_ribs') if l_0_v4_bgp_lu_resolution_ribs is missing else l_0_v4_bgp_lu_resolution_ribs), 'append'), environment.getattr(l_1_rib, 'rib_type'), _loop_vars=_loop_vars)
                l_1_rib = missing
                if (undefined(name='v4_bgp_lu_resolution_ribs') if l_0_v4_bgp_lu_resolution_ribs is missing else l_0_v4_bgp_lu_resolution_ribs):
                    pass
                    yield '      next-hop resolution ribs '
                    yield str(t_5(context.eval_ctx, (undefined(name='v4_bgp_lu_resolution_ribs') if l_0_v4_bgp_lu_resolution_ribs is missing else l_0_v4_bgp_lu_resolution_ribs), ' '))
                    yield '\n'
            for l_1_peer in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'peer_groups'), 'name'):
                l_1_maximum_routes_cli = resolve('maximum_routes_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' activate\n'
                else:
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_peer, 'graceful_restart'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' graceful-restart\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer, 'graceful_restart_helper'), 'stale_route_map')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' graceful-restart-helper stale-route route-map '
                    yield str(environment.getattr(environment.getattr(l_1_peer, 'graceful_restart_helper'), 'stale_route_map'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_peer, 'name'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer, 'name'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_peer, 'name'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer, 'name'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_peer, 'additional_paths'), 'send'))
                        yield '\n'
                if t_6(environment.getattr(l_1_peer, 'next_hop_unchanged'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' next-hop-unchanged\n'
                if t_6(environment.getattr(l_1_peer, 'next_hop_self'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' next-hop-self\n'
                if t_6(environment.getattr(l_1_peer, 'next_hop_self_v4_mapped_v6_source_interface')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' next-hop-self v4-mapped-v6 source-interface '
                    yield str(environment.getattr(l_1_peer, 'next_hop_self_v4_mapped_v6_source_interface'))
                    yield '\n'
                elif t_6(environment.getattr(l_1_peer, 'next_hop_self_source_interface')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' next-hop-self source-interface '
                    yield str(environment.getattr(l_1_peer, 'next_hop_self_source_interface'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer, 'maximum_advertised_routes')):
                    pass
                    l_1_maximum_routes_cli = str_join(('neighbor ', environment.getattr(l_1_peer, 'name'), ' maximum-advertised-routes ', environment.getattr(l_1_peer, 'maximum_advertised_routes'), ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                    if t_6(environment.getattr(l_1_peer, 'maximum_advertised_routes_warning_limit')):
                        pass
                        l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-limit ', environment.getattr(l_1_peer, 'maximum_advertised_routes_warning_limit'), ))
                        _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                    yield '      '
                    yield str((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer, 'missing_policy')):
                    pass
                    for l_2_direction in ['in', 'out']:
                        l_2_missing_policy_cli = resolve('missing_policy_cli')
                        l_2_dir = l_2_policy = missing
                        _loop_vars = {}
                        pass
                        l_2_dir = str_join(('direction_', l_2_direction, ))
                        _loop_vars['dir'] = l_2_dir
                        l_2_policy = environment.getitem(environment.getattr(l_1_peer, 'missing_policy'), (undefined(name='dir') if l_2_dir is missing else l_2_dir))
                        _loop_vars['policy'] = l_2_policy
                        if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action')):
                            pass
                            l_2_missing_policy_cli = str_join(('neighbor ', environment.getattr(l_1_peer, 'name'), ' missing-policy', ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if ((t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True)) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True)):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' include', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' community-list', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' prefix-list', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' sub-route-map', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' direction ', l_2_direction, ' action ', environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action'), ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            yield '      '
                            yield str((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli))
                            yield '\n'
                    l_2_direction = l_2_dir = l_2_policy = l_2_missing_policy_cli = missing
                if t_6(environment.getattr(l_1_peer, 'aigp_session'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' aigp-session\n'
                if t_6(environment.getattr(l_1_peer, 'multi_path'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer, 'name'))
                    yield ' multi-path\n'
            l_1_peer = l_1_maximum_routes_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'neighbors'), 'ip_address'):
                l_1_maximum_routes_cli = resolve('maximum_routes_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                else:
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'graceful_restart'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' graceful-restart\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'graceful_restart_helper'), 'stale_route_map')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' graceful-restart-helper stale-route route-map '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'graceful_restart_helper'), 'stale_route_map'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send'))
                        yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'next_hop_unchanged'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' next-hop-unchanged\n'
                if t_6(environment.getattr(l_1_neighbor, 'next_hop_self'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' next-hop-self\n'
                if t_6(environment.getattr(l_1_neighbor, 'next_hop_self_v4_mapped_v6_source_interface')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' next-hop-self v4-mapped-v6 source-interface '
                    yield str(environment.getattr(l_1_neighbor, 'next_hop_self_v4_mapped_v6_source_interface'))
                    yield '\n'
                elif t_6(environment.getattr(l_1_neighbor, 'next_hop_self_source_interface')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' next-hop-self source-interface '
                    yield str(environment.getattr(l_1_neighbor, 'next_hop_self_source_interface'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'maximum_advertised_routes')):
                    pass
                    l_1_maximum_routes_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' maximum-advertised-routes ', environment.getattr(l_1_neighbor, 'maximum_advertised_routes'), ))
                    _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                    if t_6(environment.getattr(l_1_neighbor, 'maximum_advertised_routes_warning_limit')):
                        pass
                        l_1_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli), ' warning-limit ', environment.getattr(l_1_neighbor, 'maximum_advertised_routes_warning_limit'), ))
                        _loop_vars['maximum_routes_cli'] = l_1_maximum_routes_cli
                    yield '      '
                    yield str((undefined(name='maximum_routes_cli') if l_1_maximum_routes_cli is missing else l_1_maximum_routes_cli))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'missing_policy')):
                    pass
                    for l_2_direction in ['in', 'out']:
                        l_2_missing_policy_cli = resolve('missing_policy_cli')
                        l_2_dir = l_2_policy = missing
                        _loop_vars = {}
                        pass
                        l_2_dir = str_join(('direction_', l_2_direction, ))
                        _loop_vars['dir'] = l_2_dir
                        l_2_policy = environment.getitem(environment.getattr(l_1_neighbor, 'missing_policy'), (undefined(name='dir') if l_2_dir is missing else l_2_dir))
                        _loop_vars['policy'] = l_2_policy
                        if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action')):
                            pass
                            l_2_missing_policy_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' missing-policy ', ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            if ((t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True)) or t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True)):
                                pass
                                l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' include', ))
                                _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_community_list'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' community-list', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_prefix_list'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' prefix-list', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                                if t_6(environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'include_sub_route_map'), True):
                                    pass
                                    l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' sub-route-map', ))
                                    _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            l_2_missing_policy_cli = str_join(((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli), ' direction ', l_2_direction, ' action ', environment.getattr((undefined(name='policy') if l_2_policy is missing else l_2_policy), 'action'), ))
                            _loop_vars['missing_policy_cli'] = l_2_missing_policy_cli
                            yield '      '
                            yield str((undefined(name='missing_policy_cli') if l_2_missing_policy_cli is missing else l_2_missing_policy_cli))
                            yield '\n'
                    l_2_direction = l_2_dir = l_2_policy = l_2_missing_policy_cli = missing
                if t_6(environment.getattr(l_1_neighbor, 'aigp_session'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' aigp-session\n'
                if t_6(environment.getattr(l_1_neighbor, 'multi_path'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' multi-path\n'
            l_1_neighbor = l_1_maximum_routes_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'networks')):
                pass
                for l_1_network in environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'networks'):
                    l_1_network_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_network_cli = str_join(('network ', environment.getattr(l_1_network, 'prefix'), ))
                    _loop_vars['network_cli'] = l_1_network_cli
                    if t_6(environment.getattr(l_1_network, 'route_map')):
                        pass
                        l_1_network_cli = str_join(((undefined(name='network_cli') if l_1_network_cli is missing else l_1_network_cli), ' route-map ', environment.getattr(l_1_network, 'route_map'), ))
                        _loop_vars['network_cli'] = l_1_network_cli
                    yield '      '
                    yield str((undefined(name='network_cli') if l_1_network_cli is missing else l_1_network_cli))
                    yield '\n'
                l_1_network = l_1_network_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'next_hops')):
                pass
                for l_1_next_hop in environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'next_hops'):
                    l_1_next_hop_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_next_hop_cli = str_join(('next-hop ', environment.getattr(l_1_next_hop, 'ip_address'), ' originate', ))
                    _loop_vars['next_hop_cli'] = l_1_next_hop_cli
                    if t_6(environment.getattr(l_1_next_hop, 'lfib_backup_ip_forwarding'), True):
                        pass
                        l_1_next_hop_cli = str_join(((undefined(name='next_hop_cli') if l_1_next_hop_cli is missing else l_1_next_hop_cli), ' lfib-backup ip-forwarding', ))
                        _loop_vars['next_hop_cli'] = l_1_next_hop_cli
                    yield '      '
                    yield str((undefined(name='next_hop_cli') if l_1_next_hop_cli is missing else l_1_next_hop_cli))
                    yield '\n'
                l_1_next_hop = l_1_next_hop_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'lfib_entry_installation_skipped'), True):
                pass
                yield '      lfib entry installation skipped\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'label_local_termination')):
                pass
                yield '      label local-termination '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'label_local_termination'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'graceful_restart'), True):
                pass
                yield '      graceful-restart\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'tunnel_source_protocols')):
                pass
                for l_1_tunnel_source_protocol in environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'tunnel_source_protocols'):
                    l_1_tunnel_source_protocol_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_tunnel_source_protocol_cli = str_join(('tunnel source-protocol ', environment.getattr(l_1_tunnel_source_protocol, 'protocol'), ))
                    _loop_vars['tunnel_source_protocol_cli'] = l_1_tunnel_source_protocol_cli
                    if t_6(environment.getattr(l_1_tunnel_source_protocol, 'rcf')):
                        pass
                        l_1_tunnel_source_protocol_cli = str_join(((undefined(name='tunnel_source_protocol_cli') if l_1_tunnel_source_protocol_cli is missing else l_1_tunnel_source_protocol_cli), ' rcf ', environment.getattr(l_1_tunnel_source_protocol, 'rcf'), ))
                        _loop_vars['tunnel_source_protocol_cli'] = l_1_tunnel_source_protocol_cli
                    yield '      '
                    yield str((undefined(name='tunnel_source_protocol_cli') if l_1_tunnel_source_protocol_cli is missing else l_1_tunnel_source_protocol_cli))
                    yield '\n'
                l_1_tunnel_source_protocol = l_1_tunnel_source_protocol_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'aigp_session')):
                pass
                for l_1_aigp_session_type in ['ibgp', 'confederation', 'ebgp']:
                    _loop_vars = {}
                    pass
                    if t_6(environment.getitem(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_labeled_unicast'), 'aigp_session'), l_1_aigp_session_type), True):
                        pass
                        yield '      aigp-session '
                        yield str(l_1_aigp_session_type)
                        yield '\n'
                l_1_aigp_session_type = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast')):
            pass
            yield '   !\n   address-family ipv4 multicast\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
            l_1_neighbor = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'redistribute')):
                pass
                l_0_redistribute_var = environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'redistribute')
                context.vars['redistribute_var'] = l_0_redistribute_var
                context.exported_vars.add('redistribute_var')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'enabled'), True):
                    pass
                    l_0_redistribute_host = 'redistribute attached-host'
                    context.vars['redistribute_host'] = l_0_redistribute_host
                    context.exported_vars.add('redistribute_host')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map')):
                        pass
                        l_0_redistribute_host = str_join(((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map'), ))
                        context.vars['redistribute_host'] = l_0_redistribute_host
                        context.exported_vars.add('redistribute_host')
                    yield '      '
                    yield str((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'enabled'), True):
                    pass
                    l_0_redistribute_conn = 'redistribute connected'
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    yield '      '
                    yield str((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'enabled'), True):
                    pass
                    l_0_redistribute_isis = 'redistribute isis'
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' include leaked', ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    yield '      '
                    yield str((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf match internal'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'enabled'), True):
                    pass
                    l_0_redistribute_static = 'redistribute static'
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    yield '      '
                    yield str((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static))
                    yield '\n'
            elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'redistribute_routes')):
                pass
                for l_1_redistribute_route in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_multicast'), 'redistribute_routes'), 'source_protocol'):
                    l_1_redistribute_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'ospf_route_type')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (t_6(environment.getattr(l_1_redistribute_route, 'include_leaked'), True) and (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'isis')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if t_6(environment.getattr(l_1_redistribute_route, 'route_map')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif ((environment.getattr(l_1_redistribute_route, 'source_protocol') == 'isis') and t_6(environment.getattr(l_1_redistribute_route, 'rcf'))):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' rcf ', environment.getattr(l_1_redistribute_route, 'rcf'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    yield '      '
                    yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                    yield '\n'
                l_1_redistribute_route = l_1_redistribute_route_cli = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_sr_te')):
            pass
            yield '   !\n   address-family ipv4 sr-te\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_sr_te'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv4_sr_te'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
            l_1_neighbor = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6')):
            pass
            yield '   !\n   address-family ipv6\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'install'), True):
                pass
                yield '      bgp additional-paths install\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'install_ecmp_primary'), True):
                pass
                yield '      bgp additional-paths install ecmp-primary\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'peer_groups'), 'name'):
                l_1_add_path_cli = resolve('add_path_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'prefix_list_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_peer_group, 'prefix_list_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'prefix_list_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_peer_group, 'prefix_list_out'))
                    yield ' out\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send\n'
                    else:
                        pass
                        if (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send ecmp limit ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        elif (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')):
                                pass
                                l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send limit ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'), ))
                                _loop_vars['add_path_cli'] = l_1_add_path_cli
                        else:
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' additional-paths send ', environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'prefix_list')):
                            pass
                            l_1_add_path_cli = str_join(((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli), ' prefix-list ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'prefix_list'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli)):
                            pass
                            yield '      '
                            yield str((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli))
                            yield '\n'
            l_1_peer_group = l_1_add_path_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'neighbors'), 'ip_address'):
                l_1_add_path_cli = resolve('add_path_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'prefix_list_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_neighbor, 'prefix_list_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'prefix_list_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' prefix-list '
                    yield str(environment.getattr(l_1_neighbor, 'prefix_list_out'))
                    yield ' out\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    else:
                        pass
                        if (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send ecmp limit ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        elif (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')):
                                pass
                                l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send limit ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'), ))
                                _loop_vars['add_path_cli'] = l_1_add_path_cli
                        else:
                            pass
                            l_1_add_path_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' additional-paths send ', environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'prefix_list')):
                            pass
                            l_1_add_path_cli = str_join(((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli), ' prefix-list ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'prefix_list'), ))
                            _loop_vars['add_path_cli'] = l_1_add_path_cli
                        if t_6((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli)):
                            pass
                            yield '      '
                            yield str((undefined(name='add_path_cli') if l_1_add_path_cli is missing else l_1_add_path_cli))
                            yield '\n'
            l_1_neighbor = l_1_add_path_cli = missing
            for l_1_network in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'networks'), 'prefix'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_network, 'route_map')):
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_1_network, 'prefix'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_network, 'route_map'))
                    yield '\n'
                else:
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_1_network, 'prefix'))
                    yield '\n'
            l_1_network = missing
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'redistribute_internal'), True):
                pass
                yield '      bgp redistribute-internal\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'bgp'), 'redistribute_internal'), False):
                pass
                yield '      no bgp redistribute-internal\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'redistribute')):
                pass
                l_0_redistribute_var = environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'redistribute')
                context.vars['redistribute_var'] = l_0_redistribute_var
                context.exported_vars.add('redistribute_var')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'enabled'), True):
                    pass
                    l_0_redistribute_host = 'redistribute attached-host'
                    context.vars['redistribute_host'] = l_0_redistribute_host
                    context.exported_vars.add('redistribute_host')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map')):
                        pass
                        l_0_redistribute_host = str_join(((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'attached_host'), 'route_map'), ))
                        context.vars['redistribute_host'] = l_0_redistribute_host
                        context.exported_vars.add('redistribute_host')
                    yield '      '
                    yield str((undefined(name='redistribute_host') if l_0_redistribute_host is missing else l_0_redistribute_host))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'enabled'), True):
                    pass
                    l_0_redistribute_bgp = 'redistribute bgp leaked'
                    context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                    context.exported_vars.add('redistribute_bgp')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map')):
                        pass
                        l_0_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'bgp'), 'route_map'), ))
                        context.vars['redistribute_bgp'] = l_0_redistribute_bgp
                        context.exported_vars.add('redistribute_bgp')
                    yield '      '
                    yield str((undefined(name='redistribute_bgp') if l_0_redistribute_bgp is missing else l_0_redistribute_bgp))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dhcp'), 'enabled'), True):
                    pass
                    l_0_redistribute_dhcp = 'redistribute dhcp'
                    context.vars['redistribute_dhcp'] = l_0_redistribute_dhcp
                    context.exported_vars.add('redistribute_dhcp')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dhcp'), 'route_map')):
                        pass
                        l_0_redistribute_dhcp = str_join(((undefined(name='redistribute_dhcp') if l_0_redistribute_dhcp is missing else l_0_redistribute_dhcp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dhcp'), 'route_map'), ))
                        context.vars['redistribute_dhcp'] = l_0_redistribute_dhcp
                        context.exported_vars.add('redistribute_dhcp')
                    yield '      '
                    yield str((undefined(name='redistribute_dhcp') if l_0_redistribute_dhcp is missing else l_0_redistribute_dhcp))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'enabled'), True):
                    pass
                    l_0_redistribute_conn = 'redistribute connected'
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' include leaked', ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'rcf'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    yield '      '
                    yield str((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'enabled'), True):
                    pass
                    l_0_redistribute_dynamic = 'redistribute dynamic'
                    context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                    context.exported_vars.add('redistribute_dynamic')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map')):
                        pass
                        l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'route_map'), ))
                        context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                        context.exported_vars.add('redistribute_dynamic')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf')):
                        pass
                        l_0_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'dynamic'), 'rcf'), ))
                        context.vars['redistribute_dynamic'] = l_0_redistribute_dynamic
                        context.exported_vars.add('redistribute_dynamic')
                    yield '      '
                    yield str((undefined(name='redistribute_dynamic') if l_0_redistribute_dynamic is missing else l_0_redistribute_dynamic))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'enabled'), True):
                    pass
                    l_0_redistribute_user = 'redistribute user'
                    context.vars['redistribute_user'] = l_0_redistribute_user
                    context.exported_vars.add('redistribute_user')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf')):
                        pass
                        l_0_redistribute_user = str_join(((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'user'), 'rcf'), ))
                        context.vars['redistribute_user'] = l_0_redistribute_user
                        context.exported_vars.add('redistribute_user')
                    yield '      '
                    yield str((undefined(name='redistribute_user') if l_0_redistribute_user is missing else l_0_redistribute_user))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'enabled'), True):
                    pass
                    l_0_redistribute_isis = 'redistribute isis'
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' include leaked', ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    yield '      '
                    yield str((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' include leaked', ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' include leaked', ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'enabled'), True):
                    pass
                    l_0_redistribute_static = 'redistribute static'
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' include leaked', ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'rcf'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    yield '      '
                    yield str((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static))
                    yield '\n'
            elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'redistribute_routes')):
                pass
                for l_1_redistribute_route in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6'), 'redistribute_routes'), 'source_protocol'):
                    l_1_redistribute_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'ospfv3'):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'ospf_route_type')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') == 'bgp'):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif t_6(environment.getattr(l_1_redistribute_route, 'include_leaked'), True):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if t_6(environment.getattr(l_1_redistribute_route, 'route_map')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'rcf')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' rcf ', environment.getattr(l_1_redistribute_route, 'rcf'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    yield '      '
                    yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                    yield '\n'
                l_1_redistribute_route = l_1_redistribute_route_cli = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast')):
            pass
            yield '   !\n   address-family ipv6 multicast\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                pass
                yield '      bgp missing-policy direction in action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                pass
                yield '      bgp missing-policy direction out action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
            l_1_neighbor = missing
            for l_1_network in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'networks'), 'prefix'):
                l_1_network_cli = missing
                _loop_vars = {}
                pass
                l_1_network_cli = str_join(('network ', environment.getattr(l_1_network, 'prefix'), ))
                _loop_vars['network_cli'] = l_1_network_cli
                if t_6(environment.getattr(l_1_network, 'route_map')):
                    pass
                    l_1_network_cli = str_join(((undefined(name='network_cli') if l_1_network_cli is missing else l_1_network_cli), ' route-map ', environment.getattr(l_1_network, 'route_map'), ))
                    _loop_vars['network_cli'] = l_1_network_cli
                yield '      '
                yield str((undefined(name='network_cli') if l_1_network_cli is missing else l_1_network_cli))
                yield '\n'
            l_1_network = l_1_network_cli = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'redistribute')):
                pass
                l_0_redistribute_var = environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'redistribute')
                context.vars['redistribute_var'] = l_0_redistribute_var
                context.exported_vars.add('redistribute_var')
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'enabled'), True):
                    pass
                    l_0_redistribute_conn = 'redistribute connected'
                    context.vars['redistribute_conn'] = l_0_redistribute_conn
                    context.exported_vars.add('redistribute_conn')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map')):
                        pass
                        l_0_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'connected'), 'route_map'), ))
                        context.vars['redistribute_conn'] = l_0_redistribute_conn
                        context.exported_vars.add('redistribute_conn')
                    yield '      '
                    yield str((undefined(name='redistribute_conn') if l_0_redistribute_conn is missing else l_0_redistribute_conn))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'enabled'), True):
                    pass
                    l_0_redistribute_isis = 'redistribute isis'
                    context.vars['redistribute_isis'] = l_0_redistribute_isis
                    context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'isis_level'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'include_leaked'), True):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' include leaked', ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'route_map'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf')):
                        pass
                        l_0_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'isis'), 'rcf'), ))
                        context.vars['redistribute_isis'] = l_0_redistribute_isis
                        context.exported_vars.add('redistribute_isis')
                    yield '      '
                    yield str((undefined(name='redistribute_isis') if l_0_redistribute_isis is missing else l_0_redistribute_isis))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf = 'redistribute ospf match internal'
                    context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                    context.exported_vars.add('redistribute_ospf')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospf'] = l_0_redistribute_ospf
                        context.exported_vars.add('redistribute_ospf')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_0_redistribute_ospf is missing else l_0_redistribute_ospf))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                    context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                    context.exported_vars.add('redistribute_ospfv3')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                        context.vars['redistribute_ospfv3'] = l_0_redistribute_ospfv3
                        context.exported_vars.add('redistribute_ospfv3')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_0_redistribute_ospfv3 is missing else l_0_redistribute_ospfv3))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                    context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                    context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospfv3_match'] = l_0_redistribute_ospfv3_match
                        context.exported_vars.add('redistribute_ospfv3_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_0_redistribute_ospfv3_match is missing else l_0_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_0_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                    context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                    context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_0_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                        context.vars['redistribute_ospf_match'] = l_0_redistribute_ospf_match
                        context.exported_vars.add('redistribute_ospf_match')
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_0_redistribute_ospf_match is missing else l_0_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'enabled'), True):
                    pass
                    l_0_redistribute_static = 'redistribute static'
                    context.vars['redistribute_static'] = l_0_redistribute_static
                    context.exported_vars.add('redistribute_static')
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map')):
                        pass
                        l_0_redistribute_static = str_join(((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_0_redistribute_var is missing else l_0_redistribute_var), 'static'), 'route_map'), ))
                        context.vars['redistribute_static'] = l_0_redistribute_static
                        context.exported_vars.add('redistribute_static')
                    yield '      '
                    yield str((undefined(name='redistribute_static') if l_0_redistribute_static is missing else l_0_redistribute_static))
                    yield '\n'
            elif t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'redistribute_routes')):
                pass
                for l_1_redistribute_route in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_multicast'), 'redistribute_routes'), 'source_protocol'):
                    l_1_redistribute_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_1_redistribute_route, 'source_protocol'), ))
                    _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if (environment.getattr(l_1_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                        pass
                        if t_6(environment.getattr(l_1_redistribute_route, 'ospf_route_type')):
                            pass
                            l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' match ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                            _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if t_6(environment.getattr(l_1_redistribute_route, 'include_leaked'), True):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    if t_6(environment.getattr(l_1_redistribute_route, 'route_map')):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' route-map ', environment.getattr(l_1_redistribute_route, 'route_map'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    elif ((environment.getattr(l_1_redistribute_route, 'source_protocol') == 'isis') and t_6(environment.getattr(l_1_redistribute_route, 'rcf'))):
                        pass
                        l_1_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli), ' rcf ', environment.getattr(l_1_redistribute_route, 'rcf'), ))
                        _loop_vars['redistribute_route_cli'] = l_1_redistribute_route_cli
                    yield '      '
                    yield str((undefined(name='redistribute_route_cli') if l_1_redistribute_route_cli is missing else l_1_redistribute_route_cli))
                    yield '\n'
                l_1_redistribute_route = l_1_redistribute_route_cli = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_sr_te')):
            pass
            yield '   !\n   address-family ipv6 sr-te\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_sr_te'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_ipv6_sr_te'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
            l_1_neighbor = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state')):
            pass
            yield '   !\n   address-family link-state\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                pass
                yield '      bgp missing-policy direction in action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                pass
                yield '      bgp missing-policy direction out action '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(l_1_peer_group, 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(l_1_peer_group, 'missing_policy'), 'direction_out_action'))
                    yield '\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(l_1_neighbor, 'missing_policy'), 'direction_out_action'))
                    yield '\n'
            l_1_neighbor = missing
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection')):
                pass
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection'), 'roles'), 'producer'), True):
                    pass
                    yield '      path-selection\n'
                if (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection'), 'roles'), 'consumer'), True) or t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection'), 'roles'), 'propagator'), True)):
                    pass
                    l_0_path_selection_roles = 'path-selection role'
                    context.vars['path_selection_roles'] = l_0_path_selection_roles
                    context.exported_vars.add('path_selection_roles')
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection'), 'roles'), 'consumer'), True):
                        pass
                        l_0_path_selection_roles = str_join(((undefined(name='path_selection_roles') if l_0_path_selection_roles is missing else l_0_path_selection_roles), ' consumer', ))
                        context.vars['path_selection_roles'] = l_0_path_selection_roles
                        context.exported_vars.add('path_selection_roles')
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_link_state'), 'path_selection'), 'roles'), 'propagator'), True):
                        pass
                        l_0_path_selection_roles = str_join(((undefined(name='path_selection_roles') if l_0_path_selection_roles is missing else l_0_path_selection_roles), ' propagator', ))
                        context.vars['path_selection_roles'] = l_0_path_selection_roles
                        context.exported_vars.add('path_selection_roles')
                    yield '      '
                    yield str((undefined(name='path_selection_roles') if l_0_path_selection_roles is missing else l_0_path_selection_roles))
                    yield '\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection')):
            pass
            yield '   !\n   address-family path-selection\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_peer_group, 'name'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_peer_group, 'additional_paths'), 'send'))
                        yield '\n'
            l_1_peer_group = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_path_selection'), 'neighbors'), 'ip_address'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_1_neighbor, 'additional_paths'), 'send'))
                        yield '\n'
            l_1_neighbor = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_rtc')):
            pass
            yield '   !\n   address-family rt-membership\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_rtc'), 'peer_groups'), 'name'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_7(environment.getattr(l_1_peer_group, 'default_route_target')):
                    pass
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route_target'), 'only'), True):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' default-route-target only\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_1_peer_group, 'name'))
                        yield ' default-route-target\n'
                if t_7(environment.getattr(environment.getattr(l_1_peer_group, 'default_route_target'), 'encoding_origin_as_omit')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' default-route-target encoding origin-as omit\n'
            l_1_peer_group = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4')):
            pass
            yield '   !\n   address-family vpn-ipv4\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'peer_groups'), 'name'):
                l_1_peer_group_default_route_cli = resolve('peer_group_default_route_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'enabled'), True):
                    pass
                    l_1_peer_group_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' default-route', ))
                    _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    yield '      '
                    yield str((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli))
                    yield '\n'
            l_1_peer_group = l_1_peer_group_default_route_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'neighbors'), 'ip_address'):
                l_1_neighbor_default_route_cli = resolve('neighbor_default_route_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'enabled'), True):
                    pass
                    l_1_neighbor_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' default-route', ))
                    _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli))
                    yield '\n'
            l_1_neighbor = l_1_neighbor_default_route_cli = missing
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'neighbor_default_encapsulation_mpls_next_hop_self'), 'source_interface')):
                pass
                yield '      neighbor default encapsulation mpls next-hop-self source-interface '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'neighbor_default_encapsulation_mpls_next_hop_self'), 'source_interface'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'domain_identifier')):
                pass
                yield '      domain identifier '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'domain_identifier'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv4'), 'route'), 'import_match_failure_action'), 'discard'):
                pass
                yield '      route import match-failure action discard\n'
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6')):
            pass
            yield '   !\n   address-family vpn-ipv6\n'
            for l_1_peer_group in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'peer_groups'), 'name'):
                l_1_peer_group_default_route_cli = resolve('peer_group_default_route_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_peer_group, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_peer_group, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_peer_group, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_peer_group, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_peer_group, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_peer_group, 'name'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_peer_group, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'enabled'), True):
                    pass
                    l_1_peer_group_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_peer_group, 'name'), ' default-route', ))
                    _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'rcf'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map')):
                        pass
                        l_1_peer_group_default_route_cli = str_join(((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_peer_group, 'default_route'), 'route_map'), ))
                        _loop_vars['peer_group_default_route_cli'] = l_1_peer_group_default_route_cli
                    yield '      '
                    yield str((undefined(name='peer_group_default_route_cli') if l_1_peer_group_default_route_cli is missing else l_1_peer_group_default_route_cli))
                    yield '\n'
            l_1_peer_group = l_1_peer_group_default_route_cli = missing
            for l_1_neighbor in t_3(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'neighbors'), 'ip_address'):
                l_1_neighbor_default_route_cli = resolve('neighbor_default_route_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_1_neighbor, 'activate'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                elif t_6(environment.getattr(l_1_neighbor, 'activate'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' activate\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(l_1_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_1_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf in '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_in'))
                    yield '\n'
                if t_6(environment.getattr(l_1_neighbor, 'rcf_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_1_neighbor, 'ip_address'))
                    yield ' rcf out '
                    yield str(environment.getattr(l_1_neighbor, 'rcf_out'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'enabled'), True):
                    pass
                    l_1_neighbor_default_route_cli = str_join(('neighbor ', environment.getattr(l_1_neighbor, 'ip_address'), ' default-route', ))
                    _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    if t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' rcf ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'rcf'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    elif t_6(environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map')):
                        pass
                        l_1_neighbor_default_route_cli = str_join(((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli), ' route-map ', environment.getattr(environment.getattr(l_1_neighbor, 'default_route'), 'route_map'), ))
                        _loop_vars['neighbor_default_route_cli'] = l_1_neighbor_default_route_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_route_cli') if l_1_neighbor_default_route_cli is missing else l_1_neighbor_default_route_cli))
                    yield '\n'
            l_1_neighbor = l_1_neighbor_default_route_cli = missing
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'neighbor_default_encapsulation_mpls_next_hop_self'), 'source_interface')):
                pass
                yield '      neighbor default encapsulation mpls next-hop-self source-interface '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'neighbor_default_encapsulation_mpls_next_hop_self'), 'source_interface'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'domain_identifier')):
                pass
                yield '      domain identifier '
                yield str(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'domain_identifier'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'address_family_vpn_ipv6'), 'route'), 'import_match_failure_action'), 'discard'):
                pass
                yield '      route import match-failure action discard\n'
        for l_1_vrf in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'vrfs'), 'name'):
            l_1_paths_cli = l_0_paths_cli
            l_1_redistribute_var = l_0_redistribute_var
            l_1_redistribute_conn = l_0_redistribute_conn
            l_1_redistribute_isis = l_0_redistribute_isis
            l_1_redistribute_ospf = l_0_redistribute_ospf
            l_1_redistribute_ospf_match = l_0_redistribute_ospf_match
            l_1_redistribute_ospfv3 = l_0_redistribute_ospfv3
            l_1_redistribute_ospfv3_match = l_0_redistribute_ospfv3_match
            l_1_redistribute_static = l_0_redistribute_static
            l_1_redistribute_rip = l_0_redistribute_rip
            l_1_redistribute_host = l_0_redistribute_host
            l_1_redistribute_dynamic = l_0_redistribute_dynamic
            l_1_redistribute_bgp = l_0_redistribute_bgp
            l_1_redistribute_user = l_0_redistribute_user
            l_1_redistribute_dhcp = l_0_redistribute_dhcp
            _loop_vars = {}
            pass
            yield '   !\n   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_vrf, 'rd')):
                pass
                yield '      rd '
                yield str(environment.getattr(l_1_vrf, 'rd'))
                yield '\n'
            if t_6(environment.getattr(l_1_vrf, 'default_route_exports')):
                pass
                for l_2_default_route_export in t_3(environment.getattr(l_1_vrf, 'default_route_exports'), 'address_family'):
                    l_2_vrf_default_route_export_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_vrf_default_route_export_cli = str_join(('default-route export ', environment.getattr(l_2_default_route_export, 'address_family'), ))
                    _loop_vars['vrf_default_route_export_cli'] = l_2_vrf_default_route_export_cli
                    if t_6(environment.getattr(l_2_default_route_export, 'always'), True):
                        pass
                        l_2_vrf_default_route_export_cli = str_join(((undefined(name='vrf_default_route_export_cli') if l_2_vrf_default_route_export_cli is missing else l_2_vrf_default_route_export_cli), ' always', ))
                        _loop_vars['vrf_default_route_export_cli'] = l_2_vrf_default_route_export_cli
                    if t_6(environment.getattr(l_2_default_route_export, 'rcf')):
                        pass
                        l_2_vrf_default_route_export_cli = str_join(((undefined(name='vrf_default_route_export_cli') if l_2_vrf_default_route_export_cli is missing else l_2_vrf_default_route_export_cli), ' rcf ', environment.getattr(l_2_default_route_export, 'rcf'), ))
                        _loop_vars['vrf_default_route_export_cli'] = l_2_vrf_default_route_export_cli
                    elif t_6(environment.getattr(l_2_default_route_export, 'route_map')):
                        pass
                        l_2_vrf_default_route_export_cli = str_join(((undefined(name='vrf_default_route_export_cli') if l_2_vrf_default_route_export_cli is missing else l_2_vrf_default_route_export_cli), ' route-map ', environment.getattr(l_2_default_route_export, 'route_map'), ))
                        _loop_vars['vrf_default_route_export_cli'] = l_2_vrf_default_route_export_cli
                    yield '      '
                    yield str((undefined(name='vrf_default_route_export_cli') if l_2_vrf_default_route_export_cli is missing else l_2_vrf_default_route_export_cli))
                    yield '\n'
                l_2_default_route_export = l_2_vrf_default_route_export_cli = missing
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'route_targets'), 'import')):
                pass
                for l_2_address_family in environment.getattr(environment.getattr(l_1_vrf, 'route_targets'), 'import'):
                    _loop_vars = {}
                    pass
                    for l_3_route_target in environment.getattr(l_2_address_family, 'route_targets'):
                        _loop_vars = {}
                        pass
                        yield '      route-target import '
                        yield str(environment.getattr(l_2_address_family, 'address_family'))
                        yield ' '
                        yield str(l_3_route_target)
                        yield '\n'
                    l_3_route_target = missing
                    if (environment.getattr(l_2_address_family, 'address_family') in ['evpn', 'vpn-ipv4', 'vpn-ipv6']):
                        pass
                        if t_6(environment.getattr(l_2_address_family, 'rcf')):
                            pass
                            if (t_6(environment.getattr(l_2_address_family, 'vpn_route_filter_rcf')) and (environment.getattr(l_2_address_family, 'address_family') in ['vpn-ipv4', 'vpn-ipv6'])):
                                pass
                                yield '      route-target import '
                                yield str(environment.getattr(l_2_address_family, 'address_family'))
                                yield ' rcf '
                                yield str(environment.getattr(l_2_address_family, 'rcf'))
                                yield ' vpn-route filter-rcf '
                                yield str(environment.getattr(l_2_address_family, 'vpn_route_filter_rcf'))
                                yield '\n'
                            else:
                                pass
                                yield '      route-target import '
                                yield str(environment.getattr(l_2_address_family, 'address_family'))
                                yield ' rcf '
                                yield str(environment.getattr(l_2_address_family, 'rcf'))
                                yield '\n'
                        if t_6(environment.getattr(l_2_address_family, 'route_map')):
                            pass
                            yield '      route-target import '
                            yield str(environment.getattr(l_2_address_family, 'address_family'))
                            yield ' route-map '
                            yield str(environment.getattr(l_2_address_family, 'route_map'))
                            yield '\n'
                l_2_address_family = missing
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'route_targets'), 'export')):
                pass
                for l_2_address_family in environment.getattr(environment.getattr(l_1_vrf, 'route_targets'), 'export'):
                    _loop_vars = {}
                    pass
                    for l_3_route_target in environment.getattr(l_2_address_family, 'route_targets'):
                        _loop_vars = {}
                        pass
                        yield '      route-target export '
                        yield str(environment.getattr(l_2_address_family, 'address_family'))
                        yield ' '
                        yield str(l_3_route_target)
                        yield '\n'
                    l_3_route_target = missing
                    if (environment.getattr(l_2_address_family, 'address_family') in ['evpn', 'vpn-ipv4', 'vpn-ipv6']):
                        pass
                        if t_6(environment.getattr(l_2_address_family, 'rcf')):
                            pass
                            if (t_6(environment.getattr(l_2_address_family, 'vpn_route_filter_rcf')) and (environment.getattr(l_2_address_family, 'address_family') in ['vpn-ipv4', 'vpn-ipv6'])):
                                pass
                                yield '      route-target export '
                                yield str(environment.getattr(l_2_address_family, 'address_family'))
                                yield ' rcf '
                                yield str(environment.getattr(l_2_address_family, 'rcf'))
                                yield ' vpn-route filter-rcf '
                                yield str(environment.getattr(l_2_address_family, 'vpn_route_filter_rcf'))
                                yield '\n'
                            else:
                                pass
                                yield '      route-target export '
                                yield str(environment.getattr(l_2_address_family, 'address_family'))
                                yield ' rcf '
                                yield str(environment.getattr(l_2_address_family, 'rcf'))
                                yield '\n'
                        if t_6(environment.getattr(l_2_address_family, 'route_map')):
                            pass
                            yield '      route-target export '
                            yield str(environment.getattr(l_2_address_family, 'address_family'))
                            yield ' route-map '
                            yield str(environment.getattr(l_2_address_family, 'route_map'))
                            yield '\n'
                l_2_address_family = missing
            if t_6(environment.getattr(l_1_vrf, 'router_id')):
                pass
                yield '      router-id '
                yield str(environment.getattr(l_1_vrf, 'router_id'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'updates'), 'wait_for_convergence'), True):
                pass
                yield '      update wait-for-convergence\n'
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'updates'), 'wait_install'), True):
                pass
                yield '      update wait-install\n'
            if t_6(environment.getattr(l_1_vrf, 'timers')):
                pass
                yield '      timers bgp '
                yield str(environment.getattr(l_1_vrf, 'timers'))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'maximum_paths'), 'paths')):
                pass
                l_1_paths_cli = str_join(('maximum-paths ', environment.getattr(environment.getattr(l_1_vrf, 'maximum_paths'), 'paths'), ))
                _loop_vars['paths_cli'] = l_1_paths_cli
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'maximum_paths'), 'ecmp')):
                    pass
                    l_1_paths_cli = str_join(((undefined(name='paths_cli') if l_1_paths_cli is missing else l_1_paths_cli), ' ecmp ', environment.getattr(environment.getattr(l_1_vrf, 'maximum_paths'), 'ecmp'), ))
                    _loop_vars['paths_cli'] = l_1_paths_cli
                yield '      '
                yield str((undefined(name='paths_cli') if l_1_paths_cli is missing else l_1_paths_cli))
                yield '\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'install'), True):
                pass
                yield '      bgp additional-paths install\n'
            elif t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'install_ecmp_primary'), True):
                pass
                yield '      bgp additional-paths install ecmp-primary\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'receive'), True):
                pass
                yield '      bgp additional-paths receive\n'
            if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send')):
                pass
                if (environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                    pass
                    yield '      no bgp additional-paths send\n'
                elif (t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                    pass
                    yield '      bgp additional-paths send ecmp limit '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send_limit'))
                    yield '\n'
                elif (environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send') == 'limit'):
                    pass
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send_limit')):
                        pass
                        yield '      bgp additional-paths send limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                else:
                    pass
                    yield '      bgp additional-paths send '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'additional_paths'), 'send'))
                    yield '\n'
            if t_6(environment.getattr(l_1_vrf, 'listen_ranges')):
                pass
                def t_10(fiter):
                    for l_2_listen_range in fiter:
                        if ((t_6(environment.getattr(l_2_listen_range, 'peer_group')) and t_6(environment.getattr(l_2_listen_range, 'prefix'))) and (t_6(environment.getattr(l_2_listen_range, 'peer_filter')) or t_6(environment.getattr(l_2_listen_range, 'remote_as')))):
                            yield l_2_listen_range
                for l_2_listen_range in t_10(t_3(environment.getattr(l_1_vrf, 'listen_ranges'), 'peer_group')):
                    l_2_listen_range_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_listen_range_cli = str_join(('bgp listen range ', environment.getattr(l_2_listen_range, 'prefix'), ))
                    _loop_vars['listen_range_cli'] = l_2_listen_range_cli
                    if t_6(environment.getattr(l_2_listen_range, 'peer_id_include_router_id'), True):
                        pass
                        l_2_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_2_listen_range_cli is missing else l_2_listen_range_cli), ' peer-id include router-id', ))
                        _loop_vars['listen_range_cli'] = l_2_listen_range_cli
                    l_2_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_2_listen_range_cli is missing else l_2_listen_range_cli), ' peer-group ', environment.getattr(l_2_listen_range, 'peer_group'), ))
                    _loop_vars['listen_range_cli'] = l_2_listen_range_cli
                    if t_6(environment.getattr(l_2_listen_range, 'peer_filter')):
                        pass
                        l_2_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_2_listen_range_cli is missing else l_2_listen_range_cli), ' peer-filter ', environment.getattr(l_2_listen_range, 'peer_filter'), ))
                        _loop_vars['listen_range_cli'] = l_2_listen_range_cli
                    elif t_6(environment.getattr(l_2_listen_range, 'remote_as')):
                        pass
                        l_2_listen_range_cli = str_join(((undefined(name='listen_range_cli') if l_2_listen_range_cli is missing else l_2_listen_range_cli), ' remote-as ', environment.getattr(l_2_listen_range, 'remote_as'), ))
                        _loop_vars['listen_range_cli'] = l_2_listen_range_cli
                    yield '      '
                    yield str((undefined(name='listen_range_cli') if l_2_listen_range_cli is missing else l_2_listen_range_cli))
                    yield '\n'
                l_2_listen_range = l_2_listen_range_cli = missing
            for l_2_neighbor in t_3(environment.getattr(l_1_vrf, 'neighbors'), 'ip_address'):
                l_2_remove_private_as_cli = resolve('remove_private_as_cli')
                l_2_allowas_in_cli = resolve('allowas_in_cli')
                l_2_neighbor_rib_in_pre_policy_retain_cli = resolve('neighbor_rib_in_pre_policy_retain_cli')
                l_2_neighbor_ebgp_multihop_cli = resolve('neighbor_ebgp_multihop_cli')
                l_2_hide_passwords = resolve('hide_passwords')
                l_2_neighbor_default_originate_cli = resolve('neighbor_default_originate_cli')
                l_2_maximum_routes_cli = resolve('maximum_routes_cli')
                l_2_remove_private_as_ingress_cli = resolve('remove_private_as_ingress_cli')
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_2_neighbor, 'peer_group')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' peer group '
                    yield str(environment.getattr(l_2_neighbor, 'peer_group'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'remote_as')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' remote-as '
                    yield str(environment.getattr(l_2_neighbor, 'remote_as'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'next_hop_self'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' next-hop-self\n'
                if t_6(environment.getattr(l_2_neighbor, 'shutdown'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' shutdown\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as'), 'enabled'), True):
                    pass
                    l_2_remove_private_as_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' remove-private-as', ))
                    _loop_vars['remove_private_as_cli'] = l_2_remove_private_as_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as'), 'all'), True):
                        pass
                        l_2_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_2_remove_private_as_cli is missing else l_2_remove_private_as_cli), ' all', ))
                        _loop_vars['remove_private_as_cli'] = l_2_remove_private_as_cli
                        if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as'), 'replace_as'), True):
                            pass
                            l_2_remove_private_as_cli = str_join(((undefined(name='remove_private_as_cli') if l_2_remove_private_as_cli is missing else l_2_remove_private_as_cli), ' replace-as', ))
                            _loop_vars['remove_private_as_cli'] = l_2_remove_private_as_cli
                    yield '      '
                    yield str((undefined(name='remove_private_as_cli') if l_2_remove_private_as_cli is missing else l_2_remove_private_as_cli))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as'), 'enabled'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' remove-private-as\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'as_path'), 'prepend_own_disabled'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' as-path prepend-own disabled\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'as_path'), 'remote_as_replace_out'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' as-path remote-as replace out\n'
                if t_6(environment.getattr(l_2_neighbor, 'local_as')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' local-as '
                    yield str(environment.getattr(l_2_neighbor, 'local_as'))
                    yield ' no-prepend replace-as\n'
                if t_6(environment.getattr(l_2_neighbor, 'weight')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' weight '
                    yield str(environment.getattr(l_2_neighbor, 'weight'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'passive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' passive\n'
                if t_6(environment.getattr(l_2_neighbor, 'update_source')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' update-source '
                    yield str(environment.getattr(l_2_neighbor, 'update_source'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'bfd'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' bfd\n'
                    if ((t_6(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'interval')) and t_6(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'min_rx'))) and t_6(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'multiplier'))):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' bfd interval '
                        yield str(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'interval'))
                        yield ' min-rx '
                        yield str(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'min_rx'))
                        yield ' multiplier '
                        yield str(environment.getattr(environment.getattr(l_2_neighbor, 'bfd_timers'), 'multiplier'))
                        yield '\n'
                elif (t_6(environment.getattr(l_2_neighbor, 'bfd'), False) and t_6(environment.getattr(l_2_neighbor, 'peer_group'))):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' bfd\n'
                if t_6(environment.getattr(l_2_neighbor, 'description')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' description '
                    yield str(environment.getattr(l_2_neighbor, 'description'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'allowas_in'), 'enabled'), True):
                    pass
                    l_2_allowas_in_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' allowas-in', ))
                    _loop_vars['allowas_in_cli'] = l_2_allowas_in_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'allowas_in'), 'times')):
                        pass
                        l_2_allowas_in_cli = str_join(((undefined(name='allowas_in_cli') if l_2_allowas_in_cli is missing else l_2_allowas_in_cli), ' ', environment.getattr(environment.getattr(l_2_neighbor, 'allowas_in'), 'times'), ))
                        _loop_vars['allowas_in_cli'] = l_2_allowas_in_cli
                    yield '      '
                    yield str((undefined(name='allowas_in_cli') if l_2_allowas_in_cli is missing else l_2_allowas_in_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'rib_in_pre_policy_retain'), 'enabled'), True):
                    pass
                    l_2_neighbor_rib_in_pre_policy_retain_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' rib-in pre-policy retain', ))
                    _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_2_neighbor_rib_in_pre_policy_retain_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'rib_in_pre_policy_retain'), 'all'), True):
                        pass
                        l_2_neighbor_rib_in_pre_policy_retain_cli = str_join(((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_2_neighbor_rib_in_pre_policy_retain_cli is missing else l_2_neighbor_rib_in_pre_policy_retain_cli), ' all', ))
                        _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_2_neighbor_rib_in_pre_policy_retain_cli
                    yield '      '
                    yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_2_neighbor_rib_in_pre_policy_retain_cli is missing else l_2_neighbor_rib_in_pre_policy_retain_cli))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_2_neighbor, 'rib_in_pre_policy_retain'), 'enabled'), False):
                    pass
                    l_2_neighbor_rib_in_pre_policy_retain_cli = str_join(('no neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' rib-in pre-policy retain', ))
                    _loop_vars['neighbor_rib_in_pre_policy_retain_cli'] = l_2_neighbor_rib_in_pre_policy_retain_cli
                    yield '      '
                    yield str((undefined(name='neighbor_rib_in_pre_policy_retain_cli') if l_2_neighbor_rib_in_pre_policy_retain_cli is missing else l_2_neighbor_rib_in_pre_policy_retain_cli))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'ebgp_multihop')):
                    pass
                    l_2_neighbor_ebgp_multihop_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' ebgp-multihop', ))
                    _loop_vars['neighbor_ebgp_multihop_cli'] = l_2_neighbor_ebgp_multihop_cli
                    if t_8(environment.getattr(l_2_neighbor, 'ebgp_multihop')):
                        pass
                        l_2_neighbor_ebgp_multihop_cli = str_join(((undefined(name='neighbor_ebgp_multihop_cli') if l_2_neighbor_ebgp_multihop_cli is missing else l_2_neighbor_ebgp_multihop_cli), ' ', environment.getattr(l_2_neighbor, 'ebgp_multihop'), ))
                        _loop_vars['neighbor_ebgp_multihop_cli'] = l_2_neighbor_ebgp_multihop_cli
                    yield '      '
                    yield str((undefined(name='neighbor_ebgp_multihop_cli') if l_2_neighbor_ebgp_multihop_cli is missing else l_2_neighbor_ebgp_multihop_cli))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'route_reflector_client'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' route-reflector-client\n'
                elif t_6(environment.getattr(l_2_neighbor, 'route_reflector_client'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' route-reflector-client\n'
                if t_6(environment.getattr(l_2_neighbor, 'timers')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' timers '
                    yield str(environment.getattr(l_2_neighbor, 'timers'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'route_map_in')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_2_neighbor, 'route_map_in'))
                    yield ' in\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'receive'), True):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' additional-paths receive\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '      no neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')):
                            pass
                            yield '      neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '      neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths send '
                        yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send'))
                        yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'route_map_out')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' route-map '
                    yield str(environment.getattr(l_2_neighbor, 'route_map_out'))
                    yield ' out\n'
                if t_6(environment.getattr(l_2_neighbor, 'password')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' password 7 '
                    yield str(t_2(environment.getattr(l_2_neighbor, 'password'), (undefined(name='hide_passwords') if l_2_hide_passwords is missing else l_2_hide_passwords)))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'default_originate')):
                    pass
                    l_2_neighbor_default_originate_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' default-originate', ))
                    _loop_vars['neighbor_default_originate_cli'] = l_2_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'default_originate'), 'route_map')):
                        pass
                        l_2_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_2_neighbor_default_originate_cli is missing else l_2_neighbor_default_originate_cli), ' route-map ', environment.getattr(environment.getattr(l_2_neighbor, 'default_originate'), 'route_map'), ))
                        _loop_vars['neighbor_default_originate_cli'] = l_2_neighbor_default_originate_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'default_originate'), 'always'), True):
                        pass
                        l_2_neighbor_default_originate_cli = str_join(((undefined(name='neighbor_default_originate_cli') if l_2_neighbor_default_originate_cli is missing else l_2_neighbor_default_originate_cli), ' always', ))
                        _loop_vars['neighbor_default_originate_cli'] = l_2_neighbor_default_originate_cli
                    yield '      '
                    yield str((undefined(name='neighbor_default_originate_cli') if l_2_neighbor_default_originate_cli is missing else l_2_neighbor_default_originate_cli))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'send_community'), 'all'):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' send-community\n'
                elif t_6(environment.getattr(l_2_neighbor, 'send_community')):
                    pass
                    yield '      neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' send-community '
                    yield str(environment.getattr(l_2_neighbor, 'send_community'))
                    yield '\n'
                if t_6(environment.getattr(l_2_neighbor, 'maximum_routes')):
                    pass
                    l_2_maximum_routes_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' maximum-routes ', environment.getattr(l_2_neighbor, 'maximum_routes'), ))
                    _loop_vars['maximum_routes_cli'] = l_2_maximum_routes_cli
                    if t_6(environment.getattr(l_2_neighbor, 'maximum_routes_warning_limit')):
                        pass
                        l_2_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_2_maximum_routes_cli is missing else l_2_maximum_routes_cli), ' warning-limit ', environment.getattr(l_2_neighbor, 'maximum_routes_warning_limit'), ))
                        _loop_vars['maximum_routes_cli'] = l_2_maximum_routes_cli
                    if t_6(environment.getattr(l_2_neighbor, 'maximum_routes_warning_only'), True):
                        pass
                        l_2_maximum_routes_cli = str_join(((undefined(name='maximum_routes_cli') if l_2_maximum_routes_cli is missing else l_2_maximum_routes_cli), ' warning-only', ))
                        _loop_vars['maximum_routes_cli'] = l_2_maximum_routes_cli
                    yield '      '
                    yield str((undefined(name='maximum_routes_cli') if l_2_maximum_routes_cli is missing else l_2_maximum_routes_cli))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as_ingress'), 'enabled'), True):
                    pass
                    l_2_remove_private_as_ingress_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' remove-private-as ingress', ))
                    _loop_vars['remove_private_as_ingress_cli'] = l_2_remove_private_as_ingress_cli
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as_ingress'), 'replace_as'), True):
                        pass
                        l_2_remove_private_as_ingress_cli = str_join(((undefined(name='remove_private_as_ingress_cli') if l_2_remove_private_as_ingress_cli is missing else l_2_remove_private_as_ingress_cli), ' replace-as', ))
                        _loop_vars['remove_private_as_ingress_cli'] = l_2_remove_private_as_ingress_cli
                    yield '      '
                    yield str((undefined(name='remove_private_as_ingress_cli') if l_2_remove_private_as_ingress_cli is missing else l_2_remove_private_as_ingress_cli))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_2_neighbor, 'remove_private_as_ingress'), 'enabled'), False):
                    pass
                    yield '      no neighbor '
                    yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                    yield ' remove-private-as ingress\n'
            l_2_neighbor = l_2_remove_private_as_cli = l_2_allowas_in_cli = l_2_neighbor_rib_in_pre_policy_retain_cli = l_2_neighbor_ebgp_multihop_cli = l_2_hide_passwords = l_2_neighbor_default_originate_cli = l_2_maximum_routes_cli = l_2_remove_private_as_ingress_cli = missing
            for l_2_network in t_3(environment.getattr(l_1_vrf, 'networks'), 'prefix'):
                _loop_vars = {}
                pass
                if t_6(environment.getattr(l_2_network, 'route_map')):
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_2_network, 'prefix'))
                    yield ' route-map '
                    yield str(environment.getattr(l_2_network, 'route_map'))
                    yield '\n'
                else:
                    pass
                    yield '      network '
                    yield str(environment.getattr(l_2_network, 'prefix'))
                    yield '\n'
            l_2_network = missing
            if t_6(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'redistribute_internal'), True):
                pass
                yield '      bgp redistribute-internal\n'
            elif t_6(environment.getattr(environment.getattr(l_1_vrf, 'bgp'), 'redistribute_internal'), False):
                pass
                yield '      no bgp redistribute-internal\n'
            for l_2_aggregate_address in t_3(environment.getattr(l_1_vrf, 'aggregate_addresses'), 'prefix'):
                l_2_aggregate_address_cli = missing
                _loop_vars = {}
                pass
                l_2_aggregate_address_cli = str_join(('aggregate-address ', environment.getattr(l_2_aggregate_address, 'prefix'), ))
                _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                if t_6(environment.getattr(l_2_aggregate_address, 'as_set'), True):
                    pass
                    l_2_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli), ' as-set', ))
                    _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                if t_6(environment.getattr(l_2_aggregate_address, 'summary_only'), True):
                    pass
                    l_2_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli), ' summary-only', ))
                    _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                if t_6(environment.getattr(l_2_aggregate_address, 'attribute_map')):
                    pass
                    l_2_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli), ' attribute-map ', environment.getattr(l_2_aggregate_address, 'attribute_map'), ))
                    _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                if t_6(environment.getattr(l_2_aggregate_address, 'match_map')):
                    pass
                    l_2_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli), ' match-map ', environment.getattr(l_2_aggregate_address, 'match_map'), ))
                    _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                if t_6(environment.getattr(l_2_aggregate_address, 'advertise_only'), True):
                    pass
                    l_2_aggregate_address_cli = str_join(((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli), ' advertise-only', ))
                    _loop_vars['aggregate_address_cli'] = l_2_aggregate_address_cli
                yield '      '
                yield str((undefined(name='aggregate_address_cli') if l_2_aggregate_address_cli is missing else l_2_aggregate_address_cli))
                yield '\n'
            l_2_aggregate_address = l_2_aggregate_address_cli = missing
            if t_6(environment.getattr(l_1_vrf, 'redistribute')):
                pass
                l_1_redistribute_var = environment.getattr(l_1_vrf, 'redistribute')
                _loop_vars['redistribute_var'] = l_1_redistribute_var
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'enabled'), True):
                    pass
                    l_1_redistribute_conn = 'redistribute connected'
                    _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' include leaked', ))
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map')):
                        pass
                        l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map'), ))
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf')):
                        pass
                        l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf'), ))
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                    yield '      '
                    yield str((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'enabled'), True):
                    pass
                    l_1_redistribute_isis = 'redistribute isis'
                    _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level')):
                        pass
                        l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level'), ))
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' include leaked', ))
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map')):
                        pass
                        l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map'), ))
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf')):
                        pass
                        l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf'), ))
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                    yield '      '
                    yield str((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospf = 'redistribute ospf'
                    _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' include leaked', ))
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map')):
                        pass
                        l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map'), ))
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospf = 'redistribute ospf match internal'
                    _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' include leaked', ))
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                        pass
                        l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                    yield '      '
                    yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospf_match = 'redistribute ospf match external'
                    _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' include leaked', ))
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                        pass
                        l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                    _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' include leaked', ))
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                    yield '      '
                    yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospfv3 = 'redistribute ospfv3'
                    _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map')):
                        pass
                        l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map'), ))
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                    yield '\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                    _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                        pass
                        l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                    _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                        pass
                        l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                    pass
                    l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                    _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                        pass
                        l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                        pass
                        l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                    yield '      '
                    yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'enabled'), True):
                    pass
                    l_1_redistribute_static = 'redistribute static'
                    _loop_vars['redistribute_static'] = l_1_redistribute_static
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'include_leaked'), True):
                        pass
                        l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' include leaked', ))
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map')):
                        pass
                        l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map'), ))
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf')):
                        pass
                        l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf'), ))
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                    yield '      '
                    yield str((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'enabled'), True):
                    pass
                    l_1_redistribute_rip = 'redistribute rip'
                    _loop_vars['redistribute_rip'] = l_1_redistribute_rip
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'route_map')):
                        pass
                        l_1_redistribute_rip = str_join(((undefined(name='redistribute_rip') if l_1_redistribute_rip is missing else l_1_redistribute_rip), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'route_map'), ))
                        _loop_vars['redistribute_rip'] = l_1_redistribute_rip
                    yield '      '
                    yield str((undefined(name='redistribute_rip') if l_1_redistribute_rip is missing else l_1_redistribute_rip))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'enabled'), True):
                    pass
                    l_1_redistribute_host = 'redistribute attached-host'
                    _loop_vars['redistribute_host'] = l_1_redistribute_host
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map')):
                        pass
                        l_1_redistribute_host = str_join(((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map'), ))
                        _loop_vars['redistribute_host'] = l_1_redistribute_host
                    yield '      '
                    yield str((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'enabled'), True):
                    pass
                    l_1_redistribute_dynamic = 'redistribute dynamic'
                    _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map')):
                        pass
                        l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map'), ))
                        _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                    elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf')):
                        pass
                        l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf'), ))
                        _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                    yield '      '
                    yield str((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'enabled'), True):
                    pass
                    l_1_redistribute_bgp = 'redistribute bgp leaked'
                    _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map')):
                        pass
                        l_1_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map'), ))
                        _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                    yield '      '
                    yield str((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'enabled'), True):
                    pass
                    l_1_redistribute_user = 'redistribute user'
                    _loop_vars['redistribute_user'] = l_1_redistribute_user
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf')):
                        pass
                        l_1_redistribute_user = str_join(((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf'), ))
                        _loop_vars['redistribute_user'] = l_1_redistribute_user
                    yield '      '
                    yield str((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user))
                    yield '\n'
            elif t_6(environment.getattr(l_1_vrf, 'redistribute_routes')):
                pass
                for l_2_redistribute_route in t_3(environment.getattr(l_1_vrf, 'redistribute_routes'), 'source_protocol'):
                    l_2_redistribute_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_2_redistribute_route, 'source_protocol'), ))
                    _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    if (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                        pass
                        if t_6(environment.getattr(l_2_redistribute_route, 'ospf_route_type')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' match ', environment.getattr(l_2_redistribute_route, 'ospf_route_type'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    if (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'bgp'):
                        pass
                        l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    elif t_6(environment.getattr(l_2_redistribute_route, 'include_leaked'), True):
                        pass
                        l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' include leaked', ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    if t_6(environment.getattr(l_2_redistribute_route, 'route_map')):
                        pass
                        l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' route-map ', environment.getattr(l_2_redistribute_route, 'route_map'), ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    elif (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                        pass
                        if t_6(environment.getattr(l_2_redistribute_route, 'rcf')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' rcf ', environment.getattr(l_2_redistribute_route, 'rcf'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                    yield '      '
                    yield str((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli))
                    yield '\n'
                l_2_redistribute_route = l_2_redistribute_route_cli = missing
            for l_2_neighbor_interface in t_3(environment.getattr(l_1_vrf, 'neighbor_interfaces'), 'name'):
                _loop_vars = {}
                pass
                if (t_6(environment.getattr(l_2_neighbor_interface, 'peer_group')) and t_6(environment.getattr(l_2_neighbor_interface, 'remote_as'))):
                    pass
                    yield '      neighbor interface '
                    yield str(environment.getattr(l_2_neighbor_interface, 'name'))
                    yield ' peer-group '
                    yield str(environment.getattr(l_2_neighbor_interface, 'peer_group'))
                    yield ' remote-as '
                    yield str(environment.getattr(l_2_neighbor_interface, 'remote_as'))
                    yield '\n'
                elif (t_6(environment.getattr(l_2_neighbor_interface, 'peer_group')) and t_6(environment.getattr(l_2_neighbor_interface, 'peer_filter'))):
                    pass
                    yield '      neighbor interface '
                    yield str(environment.getattr(l_2_neighbor_interface, 'name'))
                    yield ' peer-group '
                    yield str(environment.getattr(l_2_neighbor_interface, 'peer_group'))
                    yield ' peer-filter '
                    yield str(environment.getattr(l_2_neighbor_interface, 'peer_filter'))
                    yield '\n'
            l_2_neighbor_interface = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4')):
                pass
                yield '      !\n      address-family flow-spec ipv4\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv4'), 'neighbors'), 'ip_address'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                l_2_neighbor = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6')):
                pass
                yield '      !\n      address-family flow-spec ipv6\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_flow_spec_ipv6'), 'neighbors'), 'ip_address'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                l_2_neighbor = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_ipv4')):
                pass
                yield '      !\n      address-family ipv4\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'install'), True):
                    pass
                    yield '         bgp additional-paths install\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'install_ecmp_primary'), True):
                    pass
                    yield '         bgp additional-paths install ecmp-primary\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'receive'), True):
                    pass
                    yield '         bgp additional-paths receive\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '         no bgp additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '         bgp additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit')):
                            pass
                            yield '         bgp additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '         bgp additional-paths send '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'additional_paths'), 'send'))
                        yield '\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'neighbors'), 'ip_address'):
                    l_2_ipv6_originate_cli = resolve('ipv6_originate_cli')
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'receive'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths receive\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_out'))
                        yield ' out\n'
                    if t_6(environment.getattr(l_2_neighbor, 'rcf_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' rcf in '
                        yield str(environment.getattr(l_2_neighbor, 'rcf_in'))
                        yield '\n'
                    if t_6(environment.getattr(l_2_neighbor, 'rcf_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' rcf out '
                        yield str(environment.getattr(l_2_neighbor, 'rcf_out'))
                        yield '\n'
                    if t_6(environment.getattr(l_2_neighbor, 'prefix_list_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' prefix-list '
                        yield str(environment.getattr(l_2_neighbor, 'prefix_list_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'prefix_list_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' prefix-list '
                        yield str(environment.getattr(l_2_neighbor, 'prefix_list_out'))
                        yield ' out\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send')):
                        pass
                        if (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'disabled'):
                            pass
                            yield '         no neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send\n'
                        elif (t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            yield '         neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send ecmp limit '
                            yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                        elif (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')):
                                pass
                                yield '         neighbor '
                                yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                                yield ' additional-paths send limit '
                                yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                                yield '\n'
                        else:
                            pass
                            yield '         neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send '
                            yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send'))
                            yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_2_neighbor, 'next_hop'), 'address_family_ipv6'), 'enabled')):
                        pass
                        if t_6(environment.getattr(environment.getattr(environment.getattr(l_2_neighbor, 'next_hop'), 'address_family_ipv6'), 'enabled'), True):
                            pass
                            l_2_ipv6_originate_cli = str_join(('neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' next-hop address-family ipv6', ))
                            _loop_vars['ipv6_originate_cli'] = l_2_ipv6_originate_cli
                            if t_6(environment.getattr(environment.getattr(environment.getattr(l_2_neighbor, 'next_hop'), 'address_family_ipv6'), 'originate'), True):
                                pass
                                l_2_ipv6_originate_cli = str_join(((undefined(name='ipv6_originate_cli') if l_2_ipv6_originate_cli is missing else l_2_ipv6_originate_cli), ' originate', ))
                                _loop_vars['ipv6_originate_cli'] = l_2_ipv6_originate_cli
                        elif t_6(environment.getattr(environment.getattr(environment.getattr(l_2_neighbor, 'next_hop'), 'address_family_ipv6'), 'enabled'), False):
                            pass
                            l_2_ipv6_originate_cli = str_join(('no neighbor ', environment.getattr(l_2_neighbor, 'ip_address'), ' next-hop address-family ipv6', ))
                            _loop_vars['ipv6_originate_cli'] = l_2_ipv6_originate_cli
                        yield '         '
                        yield str((undefined(name='ipv6_originate_cli') if l_2_ipv6_originate_cli is missing else l_2_ipv6_originate_cli))
                        yield '\n'
                l_2_neighbor = l_2_ipv6_originate_cli = missing
                for l_2_network in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'networks'), 'prefix'):
                    l_2_network_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_network_cli = str_join(('network ', environment.getattr(l_2_network, 'prefix'), ))
                    _loop_vars['network_cli'] = l_2_network_cli
                    if t_6(environment.getattr(l_2_network, 'route_map')):
                        pass
                        l_2_network_cli = str_join(((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli), ' route-map ', environment.getattr(l_2_network, 'route_map'), ))
                        _loop_vars['network_cli'] = l_2_network_cli
                    yield '         '
                    yield str((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli))
                    yield '\n'
                l_2_network = l_2_network_cli = missing
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'redistribute_internal'), True):
                    pass
                    yield '         bgp redistribute-internal\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'bgp'), 'redistribute_internal'), False):
                    pass
                    yield '         no bgp redistribute-internal\n'
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'redistribute')):
                    pass
                    l_1_redistribute_var = environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'redistribute')
                    _loop_vars['redistribute_var'] = l_1_redistribute_var
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'enabled'), True):
                        pass
                        l_1_redistribute_host = 'redistribute attached-host'
                        _loop_vars['redistribute_host'] = l_1_redistribute_host
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map')):
                            pass
                            l_1_redistribute_host = str_join(((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map'), ))
                            _loop_vars['redistribute_host'] = l_1_redistribute_host
                        yield '         '
                        yield str((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'enabled'), True):
                        pass
                        l_1_redistribute_bgp = 'redistribute bgp leaked'
                        _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map')):
                            pass
                            l_1_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map'), ))
                            _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                        yield '         '
                        yield str((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'enabled'), True):
                        pass
                        l_1_redistribute_conn = 'redistribute connected'
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' include leaked', ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        yield '         '
                        yield str((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'enabled'), True):
                        pass
                        l_1_redistribute_dynamic = 'redistribute dynamic'
                        _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map')):
                            pass
                            l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map'), ))
                            _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf')):
                            pass
                            l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf'), ))
                            _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        yield '         '
                        yield str((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'enabled'), True):
                        pass
                        l_1_redistribute_user = 'redistribute user'
                        _loop_vars['redistribute_user'] = l_1_redistribute_user
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf')):
                            pass
                            l_1_redistribute_user = str_join(((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf'), ))
                            _loop_vars['redistribute_user'] = l_1_redistribute_user
                        yield '         '
                        yield str((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'enabled'), True):
                        pass
                        l_1_redistribute_isis = 'redistribute isis'
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' include leaked', ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        yield '         '
                        yield str((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' include leaked', ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf match internal'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' include leaked', ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' include leaked', ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' include leaked', ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'enabled'), True):
                        pass
                        l_1_redistribute_rip = 'redistribute rip'
                        _loop_vars['redistribute_rip'] = l_1_redistribute_rip
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'route_map')):
                            pass
                            l_1_redistribute_rip = str_join(((undefined(name='redistribute_rip') if l_1_redistribute_rip is missing else l_1_redistribute_rip), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'rip'), 'route_map'), ))
                            _loop_vars['redistribute_rip'] = l_1_redistribute_rip
                        yield '         '
                        yield str((undefined(name='redistribute_rip') if l_1_redistribute_rip is missing else l_1_redistribute_rip))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'enabled'), True):
                        pass
                        l_1_redistribute_static = 'redistribute static'
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' include leaked', ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        yield '         '
                        yield str((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static))
                        yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'redistribute_routes')):
                    pass
                    for l_2_redistribute_route in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4'), 'redistribute_routes'), 'source_protocol'):
                        l_2_redistribute_route_cli = missing
                        _loop_vars = {}
                        pass
                        l_2_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_2_redistribute_route, 'source_protocol'), ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'ospf_route_type')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' match ', environment.getattr(l_2_redistribute_route, 'ospf_route_type'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'bgp'):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (t_6(environment.getattr(l_2_redistribute_route, 'include_leaked'), True) and (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['connected', 'isis', 'ospf', 'ospfv3', 'static'])):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' include leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'route_map')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' route-map ', environment.getattr(l_2_redistribute_route, 'route_map'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'rcf')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' rcf ', environment.getattr(l_2_redistribute_route, 'rcf'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        yield '         '
                        yield str((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli))
                        yield '\n'
                    l_2_redistribute_route = l_2_redistribute_route_cli = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast')):
                pass
                yield '      !\n      address-family ipv4 multicast\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'bgp'), 'additional_paths'), 'receive'), True):
                    pass
                    yield '         bgp additional-paths receive\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'neighbors'), 'ip_address'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'receive'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths receive\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_out'))
                        yield ' out\n'
                l_2_neighbor = missing
                for l_2_network in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'networks'), 'prefix'):
                    l_2_network_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_network_cli = str_join(('network ', environment.getattr(l_2_network, 'prefix'), ))
                    _loop_vars['network_cli'] = l_2_network_cli
                    if t_6(environment.getattr(l_2_network, 'route_map')):
                        pass
                        l_2_network_cli = str_join(((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli), ' route-map ', environment.getattr(l_2_network, 'route_map'), ))
                        _loop_vars['network_cli'] = l_2_network_cli
                    yield '         '
                    yield str((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli))
                    yield '\n'
                l_2_network = l_2_network_cli = missing
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'redistribute')):
                    pass
                    l_1_redistribute_var = environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'redistribute')
                    _loop_vars['redistribute_var'] = l_1_redistribute_var
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'enabled'), True):
                        pass
                        l_1_redistribute_host = 'redistribute attached-host'
                        _loop_vars['redistribute_host'] = l_1_redistribute_host
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map')):
                            pass
                            l_1_redistribute_host = str_join(((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map'), ))
                            _loop_vars['redistribute_host'] = l_1_redistribute_host
                        yield '         '
                        yield str((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'enabled'), True):
                        pass
                        l_1_redistribute_conn = 'redistribute connected'
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        yield '         '
                        yield str((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'enabled'), True):
                        pass
                        l_1_redistribute_isis = 'redistribute isis'
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' include leaked', ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        yield '         '
                        yield str((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf match internal'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'enabled'), True):
                        pass
                        l_1_redistribute_static = 'redistribute static'
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        yield '         '
                        yield str((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static))
                        yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'redistribute_routes')):
                    pass
                    for l_2_redistribute_route in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv4_multicast'), 'redistribute_routes'), 'source_protocol'):
                        l_2_redistribute_route_cli = missing
                        _loop_vars = {}
                        pass
                        l_2_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_2_redistribute_route, 'source_protocol'), ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'ospf_route_type')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' match ', environment.getattr(l_2_redistribute_route, 'ospf_route_type'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'include_leaked'), True):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' include leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'route_map')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' route-map ', environment.getattr(l_2_redistribute_route, 'route_map'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'isis'):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'rcf')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' rcf ', environment.getattr(l_2_redistribute_route, 'rcf'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        yield '         '
                        yield str((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli))
                        yield '\n'
                    l_2_redistribute_route = l_2_redistribute_route_cli = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_ipv6')):
                pass
                yield '      !\n      address-family ipv6\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'install'), True):
                    pass
                    yield '         bgp additional-paths install\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'install_ecmp_primary'), True):
                    pass
                    yield '         bgp additional-paths install ecmp-primary\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'receive'), True):
                    pass
                    yield '         bgp additional-paths receive\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send')):
                    pass
                    if (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'disabled'):
                        pass
                        yield '         no bgp additional-paths send\n'
                    elif (t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'ecmp')):
                        pass
                        yield '         bgp additional-paths send ecmp limit '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit'))
                        yield '\n'
                    elif (environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send') == 'limit'):
                        pass
                        if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit')):
                            pass
                            yield '         bgp additional-paths send limit '
                            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send_limit'))
                            yield '\n'
                    else:
                        pass
                        yield '         bgp additional-paths send '
                        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'additional_paths'), 'send'))
                        yield '\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'neighbors'), 'ip_address'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'receive'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths receive\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_out'))
                        yield ' out\n'
                    if t_6(environment.getattr(l_2_neighbor, 'rcf_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' rcf in '
                        yield str(environment.getattr(l_2_neighbor, 'rcf_in'))
                        yield '\n'
                    if t_6(environment.getattr(l_2_neighbor, 'rcf_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' rcf out '
                        yield str(environment.getattr(l_2_neighbor, 'rcf_out'))
                        yield '\n'
                    if t_6(environment.getattr(l_2_neighbor, 'prefix_list_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' prefix-list '
                        yield str(environment.getattr(l_2_neighbor, 'prefix_list_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'prefix_list_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' prefix-list '
                        yield str(environment.getattr(l_2_neighbor, 'prefix_list_out'))
                        yield ' out\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send')):
                        pass
                        if (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'disabled'):
                            pass
                            yield '         no neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send\n'
                        elif (t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')) and (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'ecmp')):
                            pass
                            yield '         neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send ecmp limit '
                            yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                            yield '\n'
                        elif (environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send') == 'limit'):
                            pass
                            if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit')):
                                pass
                                yield '         neighbor '
                                yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                                yield ' additional-paths send limit '
                                yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send_limit'))
                                yield '\n'
                        else:
                            pass
                            yield '         neighbor '
                            yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                            yield ' additional-paths send '
                            yield str(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'send'))
                            yield '\n'
                l_2_neighbor = missing
                for l_2_network in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'networks'), 'prefix'):
                    l_2_network_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_network_cli = str_join(('network ', environment.getattr(l_2_network, 'prefix'), ))
                    _loop_vars['network_cli'] = l_2_network_cli
                    if t_6(environment.getattr(l_2_network, 'route_map')):
                        pass
                        l_2_network_cli = str_join(((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli), ' route-map ', environment.getattr(l_2_network, 'route_map'), ))
                        _loop_vars['network_cli'] = l_2_network_cli
                    yield '         '
                    yield str((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli))
                    yield '\n'
                l_2_network = l_2_network_cli = missing
                if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'redistribute_internal'), True):
                    pass
                    yield '         bgp redistribute-internal\n'
                elif t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'bgp'), 'redistribute_internal'), False):
                    pass
                    yield '         no bgp redistribute-internal\n'
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'redistribute')):
                    pass
                    l_1_redistribute_var = environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'redistribute')
                    _loop_vars['redistribute_var'] = l_1_redistribute_var
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'enabled'), True):
                        pass
                        l_1_redistribute_host = 'redistribute attached-host'
                        _loop_vars['redistribute_host'] = l_1_redistribute_host
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map')):
                            pass
                            l_1_redistribute_host = str_join(((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'attached_host'), 'route_map'), ))
                            _loop_vars['redistribute_host'] = l_1_redistribute_host
                        yield '         '
                        yield str((undefined(name='redistribute_host') if l_1_redistribute_host is missing else l_1_redistribute_host))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'enabled'), True):
                        pass
                        l_1_redistribute_bgp = 'redistribute bgp leaked'
                        _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map')):
                            pass
                            l_1_redistribute_bgp = str_join(((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'bgp'), 'route_map'), ))
                            _loop_vars['redistribute_bgp'] = l_1_redistribute_bgp
                        yield '         '
                        yield str((undefined(name='redistribute_bgp') if l_1_redistribute_bgp is missing else l_1_redistribute_bgp))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dhcp'), 'enabled'), True):
                        pass
                        l_1_redistribute_dhcp = 'redistribute dhcp'
                        _loop_vars['redistribute_dhcp'] = l_1_redistribute_dhcp
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dhcp'), 'route_map')):
                            pass
                            l_1_redistribute_dhcp = str_join(((undefined(name='redistribute_dhcp') if l_1_redistribute_dhcp is missing else l_1_redistribute_dhcp), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dhcp'), 'route_map'), ))
                            _loop_vars['redistribute_dhcp'] = l_1_redistribute_dhcp
                        yield '         '
                        yield str((undefined(name='redistribute_dhcp') if l_1_redistribute_dhcp is missing else l_1_redistribute_dhcp))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'enabled'), True):
                        pass
                        l_1_redistribute_conn = 'redistribute connected'
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' include leaked', ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'rcf'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        yield '         '
                        yield str((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'enabled'), True):
                        pass
                        l_1_redistribute_dynamic = 'redistribute dynamic'
                        _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map')):
                            pass
                            l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'route_map'), ))
                            _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf')):
                            pass
                            l_1_redistribute_dynamic = str_join(((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'dynamic'), 'rcf'), ))
                            _loop_vars['redistribute_dynamic'] = l_1_redistribute_dynamic
                        yield '         '
                        yield str((undefined(name='redistribute_dynamic') if l_1_redistribute_dynamic is missing else l_1_redistribute_dynamic))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'enabled'), True):
                        pass
                        l_1_redistribute_user = 'redistribute user'
                        _loop_vars['redistribute_user'] = l_1_redistribute_user
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf')):
                            pass
                            l_1_redistribute_user = str_join(((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'user'), 'rcf'), ))
                            _loop_vars['redistribute_user'] = l_1_redistribute_user
                        yield '         '
                        yield str((undefined(name='redistribute_user') if l_1_redistribute_user is missing else l_1_redistribute_user))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'enabled'), True):
                        pass
                        l_1_redistribute_isis = 'redistribute isis'
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' include leaked', ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        yield '         '
                        yield str((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' include leaked', ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'enabled'), True):
                        pass
                        l_1_redistribute_static = 'redistribute static'
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' include leaked', ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'rcf'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        yield '         '
                        yield str((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static))
                        yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'redistribute_routes')):
                    pass
                    for l_2_redistribute_route in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6'), 'redistribute_routes'), 'source_protocol'):
                        l_2_redistribute_route_cli = missing
                        _loop_vars = {}
                        pass
                        l_2_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_2_redistribute_route, 'source_protocol'), ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'ospfv3'):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'ospf_route_type')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' match ', environment.getattr(l_2_redistribute_route, 'ospf_route_type'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'bgp'):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (t_6(environment.getattr(l_2_redistribute_route, 'include_leaked'), True) and (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['connected', 'isis', 'ospfv3', 'static'])):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' include leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'route_map')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' route-map ', environment.getattr(l_2_redistribute_route, 'route_map'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['connected', 'static', 'isis', 'user', 'dynamic']):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'rcf')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' rcf ', environment.getattr(l_2_redistribute_route, 'rcf'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        yield '         '
                        yield str((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli))
                        yield '\n'
                    l_2_redistribute_route = l_2_redistribute_route_cli = missing
            if t_6(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast')):
                pass
                yield '      !\n      address-family ipv6 multicast\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action')):
                    pass
                    yield '         bgp missing-policy direction in action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_in_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action')):
                    pass
                    yield '         bgp missing-policy direction out action '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'bgp'), 'missing_policy'), 'direction_out_action'))
                    yield '\n'
                if t_6(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'bgp'), 'additional_paths'), 'receive'), True):
                    pass
                    yield '         bgp additional-paths receive\n'
                for l_2_neighbor in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'neighbors'), 'ip_address'):
                    _loop_vars = {}
                    pass
                    if t_6(environment.getattr(l_2_neighbor, 'activate'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' activate\n'
                    if t_6(environment.getattr(environment.getattr(l_2_neighbor, 'additional_paths'), 'receive'), True):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' additional-paths receive\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_in')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_in'))
                        yield ' in\n'
                    if t_6(environment.getattr(l_2_neighbor, 'route_map_out')):
                        pass
                        yield '         neighbor '
                        yield str(environment.getattr(l_2_neighbor, 'ip_address'))
                        yield ' route-map '
                        yield str(environment.getattr(l_2_neighbor, 'route_map_out'))
                        yield ' out\n'
                l_2_neighbor = missing
                for l_2_network in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'networks'), 'prefix'):
                    l_2_network_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_network_cli = str_join(('network ', environment.getattr(l_2_network, 'prefix'), ))
                    _loop_vars['network_cli'] = l_2_network_cli
                    if t_6(environment.getattr(l_2_network, 'route_map')):
                        pass
                        l_2_network_cli = str_join(((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli), ' route-map ', environment.getattr(l_2_network, 'route_map'), ))
                        _loop_vars['network_cli'] = l_2_network_cli
                    yield '         '
                    yield str((undefined(name='network_cli') if l_2_network_cli is missing else l_2_network_cli))
                    yield '\n'
                l_2_network = l_2_network_cli = missing
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'redistribute')):
                    pass
                    l_1_redistribute_var = environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'redistribute')
                    _loop_vars['redistribute_var'] = l_1_redistribute_var
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'enabled'), True):
                        pass
                        l_1_redistribute_conn = 'redistribute connected'
                        _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map')):
                            pass
                            l_1_redistribute_conn = str_join(((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'connected'), 'route_map'), ))
                            _loop_vars['redistribute_conn'] = l_1_redistribute_conn
                        yield '         '
                        yield str((undefined(name='redistribute_conn') if l_1_redistribute_conn is missing else l_1_redistribute_conn))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'enabled'), True):
                        pass
                        l_1_redistribute_isis = 'redistribute isis'
                        _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'isis_level'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'include_leaked'), True):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' include leaked', ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'route_map'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        elif t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf')):
                            pass
                            l_1_redistribute_isis = str_join(((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis), ' rcf ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'isis'), 'rcf'), ))
                            _loop_vars['redistribute_isis'] = l_1_redistribute_isis
                        yield '         '
                        yield str((undefined(name='redistribute_isis') if l_1_redistribute_isis is missing else l_1_redistribute_isis))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf = 'redistribute ospf match internal'
                        _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospf = str_join(((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospf'] = l_1_redistribute_ospf
                        yield '         '
                        yield str((undefined(name='redistribute_ospf') if l_1_redistribute_ospf is missing else l_1_redistribute_ospf))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    elif t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3 = 'redistribute ospfv3 match internal'
                        _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3 = str_join(((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_internal'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3'] = l_1_redistribute_ospfv3
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3') if l_1_redistribute_ospfv3 is missing else l_1_redistribute_ospfv3))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospfv3_match = 'redistribute ospfv3 match nssa-external'
                        _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospfv3_match = str_join(((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospfv3'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospfv3_match'] = l_1_redistribute_ospfv3_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospfv3_match') if l_1_redistribute_ospfv3_match is missing else l_1_redistribute_ospfv3_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'enabled'), True):
                        pass
                        l_1_redistribute_ospf_match = 'redistribute ospf match nssa-external'
                        _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'nssa_type'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        if t_6(environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map')):
                            pass
                            l_1_redistribute_ospf_match = str_join(((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match), ' route-map ', environment.getattr(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'ospf'), 'match_nssa_external'), 'route_map'), ))
                            _loop_vars['redistribute_ospf_match'] = l_1_redistribute_ospf_match
                        yield '         '
                        yield str((undefined(name='redistribute_ospf_match') if l_1_redistribute_ospf_match is missing else l_1_redistribute_ospf_match))
                        yield '\n'
                    if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'enabled'), True):
                        pass
                        l_1_redistribute_static = 'redistribute static'
                        _loop_vars['redistribute_static'] = l_1_redistribute_static
                        if t_6(environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map')):
                            pass
                            l_1_redistribute_static = str_join(((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static), ' route-map ', environment.getattr(environment.getattr((undefined(name='redistribute_var') if l_1_redistribute_var is missing else l_1_redistribute_var), 'static'), 'route_map'), ))
                            _loop_vars['redistribute_static'] = l_1_redistribute_static
                        yield '         '
                        yield str((undefined(name='redistribute_static') if l_1_redistribute_static is missing else l_1_redistribute_static))
                        yield '\n'
                elif t_6(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'redistribute_routes')):
                    pass
                    for l_2_redistribute_route in t_3(environment.getattr(environment.getattr(l_1_vrf, 'address_family_ipv6_multicast'), 'redistribute_routes'), 'source_protocol'):
                        l_2_redistribute_route_cli = missing
                        _loop_vars = {}
                        pass
                        l_2_redistribute_route_cli = str_join(('redistribute ', environment.getattr(l_2_redistribute_route, 'source_protocol'), ))
                        _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if (environment.getattr(l_2_redistribute_route, 'source_protocol') in ['ospf', 'ospfv3']):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'ospf_route_type')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' match ', environment.getattr(l_2_redistribute_route, 'ospf_route_type'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'include_leaked'), True):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' include leaked', ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        if t_6(environment.getattr(l_2_redistribute_route, 'route_map')):
                            pass
                            l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' route-map ', environment.getattr(l_2_redistribute_route, 'route_map'), ))
                            _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        elif (environment.getattr(l_2_redistribute_route, 'source_protocol') == 'isis'):
                            pass
                            if t_6(environment.getattr(l_2_redistribute_route, 'rcf')):
                                pass
                                l_2_redistribute_route_cli = str_join(((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli), ' rcf ', environment.getattr(l_2_redistribute_route, 'rcf'), ))
                                _loop_vars['redistribute_route_cli'] = l_2_redistribute_route_cli
                        yield '         '
                        yield str((undefined(name='redistribute_route_cli') if l_2_redistribute_route_cli is missing else l_2_redistribute_route_cli))
                        yield '\n'
                    l_2_redistribute_route = l_2_redistribute_route_cli = missing
            if t_6(environment.getattr(l_1_vrf, 'evpn_multicast'), True):
                pass
                yield '      evpn multicast\n'
                if t_6(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_gateway_dr_election'), 'algorithm')):
                    pass
                    if (environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_gateway_dr_election'), 'algorithm') == 'preference'):
                        pass
                        if t_6(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_gateway_dr_election'), 'preference_value')):
                            pass
                            yield '         gateway dr election algorithm preference '
                            yield str(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_gateway_dr_election'), 'preference_value'))
                            yield '\n'
                    else:
                        pass
                        yield '         gateway dr election algorithm '
                        yield str(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_gateway_dr_election'), 'algorithm'))
                        yield '\n'
                if (t_6(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_address_family'), 'ipv4')) and t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_address_family'), 'ipv4'), 'transit'), True)):
                    pass
                    yield '         address-family ipv4\n'
                    if t_6(environment.getattr(environment.getattr(environment.getattr(l_1_vrf, 'evpn_multicast_address_family'), 'ipv4'), 'transit'), True):
                        pass
                        yield '            transit\n'
            if t_6(environment.getattr(l_1_vrf, 'eos_cli')):
                pass
                yield '      !\n      '
                yield str(t_4(environment.getattr(l_1_vrf, 'eos_cli'), 6, False))
                yield '\n'
        l_1_vrf = l_1_paths_cli = l_1_redistribute_var = l_1_redistribute_conn = l_1_redistribute_isis = l_1_redistribute_ospf = l_1_redistribute_ospf_match = l_1_redistribute_ospfv3 = l_1_redistribute_ospfv3_match = l_1_redistribute_static = l_1_redistribute_rip = l_1_redistribute_host = l_1_redistribute_dynamic = l_1_redistribute_bgp = l_1_redistribute_user = l_1_redistribute_dhcp = missing
        for l_1_session_tracker in t_3(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'session_trackers'), 'name'):
            _loop_vars = {}
            pass
            yield '   session tracker '
            yield str(environment.getattr(l_1_session_tracker, 'name'))
            yield '\n'
            if t_6(environment.getattr(l_1_session_tracker, 'recovery_delay')):
                pass
                yield '      recovery delay '
                yield str(environment.getattr(l_1_session_tracker, 'recovery_delay'))
                yield ' seconds\n'
        l_1_session_tracker = missing
        if t_6(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'eos_cli')):
            pass
            yield '   !\n   '
            yield str(t_4(environment.getattr((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp), 'eos_cli'), 3, False))
            yield '\n'

blocks = {}
debug_info = '7=85&9=88&10=90&11=93&13=95&14=98&16=100&19=103&22=106&24=109&27=112&29=115&32=118&33=120&34=123&35=125&37=128&38=130&39=132&41=135&42=137&45=141&47=143&48=145&49=148&50=150&52=154&54=156&55=158&56=161&58=163&59=166&63=169&64=172&66=174&68=177&69=179&70=182&71=184&75=187&76=189&77=192&78=194&80=198&82=200&83=202&84=205&85=207&87=211&89=213&90=217&92=220&95=223&98=226&99=228&101=231&102=234&103=236&104=238&105=241&108=246&111=248&113=250&112=254&114=258&115=260&116=262&118=264&119=266&120=268&121=270&122=272&124=275&127=278&130=281&132=284&133=287&135=289&136=301&137=303&138=306&140=310&141=313&143=315&144=318&146=320&147=323&149=325&150=327&151=329&152=331&153=333&154=335&157=338&158=340&159=343&161=345&162=348&164=350&165=353&167=355&168=358&170=362&171=365&173=369&174=372&176=374&177=377&179=381&180=384&181=386&184=389&187=397&188=400&190=404&191=406&192=408&193=410&195=413&197=415&198=417&199=419&200=421&202=424&203=426&204=428&205=431&207=433&208=436&210=440&211=443&213=447&214=450&216=452&217=455&219=459&220=462&222=466&223=469&225=473&226=476&228=480&229=483&231=487&232=490&234=496&235=498&236=500&237=502&239=504&240=506&242=509&244=511&245=514&246=516&247=519&249=523&250=525&251=527&252=529&254=531&255=533&257=536&259=538&260=540&261=545&262=547&263=549&264=551&265=553&266=555&267=557&268=559&270=561&271=563&273=565&274=567&277=569&278=572&282=575&283=577&284=579&285=581&287=584&289=586&290=588&291=590&292=592&294=595&295=597&296=600&299=603&300=614&301=617&303=621&304=624&306=628&307=631&309=633&310=636&312=638&313=640&314=642&315=644&316=646&317=648&320=651&321=653&322=656&324=658&325=661&327=663&328=666&330=668&331=671&333=675&334=678&336=682&337=685&339=687&340=690&342=694&343=697&344=699&347=702&349=710&350=713&352=715&353=718&355=722&356=724&357=726&358=728&360=731&362=733&363=735&364=737&365=739&367=742&368=744&369=746&370=749&372=751&373=754&375=758&376=761&378=765&379=768&380=770&381=773&383=775&384=778&386=782&387=785&389=789&390=792&392=796&393=799&395=803&396=806&398=812&399=815&401=819&402=821&403=823&404=825&406=827&407=829&409=832&411=834&412=837&413=839&414=842&416=846&417=848&418=850&419=852&421=854&422=856&424=859&426=861&427=863&428=868&429=870&430=872&431=874&432=876&433=878&434=880&435=882&437=884&438=886&440=888&441=890&444=892&445=895&449=898&450=900&451=902&452=904&454=907&456=909&457=911&458=913&459=915&461=918&462=920&463=923&466=926&468=929&471=932&472=936&473=938&474=940&476=942&477=944&479=946&480=948&482=950&483=952&485=954&486=956&488=959&490=962&491=964&492=967&493=969&494=972&495=974&497=977&498=979&499=982&500=984&502=988&504=990&505=992&506=995&507=997&509=1000&510=1002&512=1005&513=1007&514=1010&515=1012&517=1016&519=1018&520=1020&521=1023&522=1025&524=1028&525=1030&527=1034&528=1036&529=1038&530=1041&531=1043&533=1046&534=1048&536=1052&538=1054&539=1056&540=1059&541=1061&543=1064&544=1066&546=1070&548=1072&549=1074&550=1077&551=1079&553=1082&554=1084&556=1087&557=1089&559=1093&561=1095&562=1097&563=1100&564=1102&566=1105&567=1107&569=1111&570=1113&571=1115&572=1118&573=1120&575=1123&576=1125&578=1129&580=1131&581=1133&582=1136&583=1138&585=1141&586=1143&588=1147&590=1149&591=1151&592=1154&593=1156&595=1159&596=1161&598=1164&599=1166&601=1170&603=1172&604=1174&605=1177&606=1179&608=1182&609=1184&610=1187&611=1189&613=1193&615=1195&616=1197&617=1200&618=1202&620=1206&622=1208&623=1210&624=1213&625=1215&627=1219&629=1221&630=1223&631=1226&632=1228&633=1231&634=1233&636=1237&638=1239&639=1241&640=1244&641=1246&643=1250&645=1252&646=1254&647=1257&648=1259&650=1263&652=1265&653=1267&654=1271&655=1273&656=1275&657=1277&660=1279&661=1281&662=1283&663=1285&665=1287&666=1289&667=1291&668=1293&669=1295&672=1298&675=1301&676=1304&677=1307&678=1313&679=1316&683=1323&684=1325&686=1329&687=1331&688=1334&690=1336&691=1339&693=1343&694=1347&696=1350&697=1354&699=1357&700=1361&702=1364&703=1368&705=1373&706=1377&708=1382&709=1386&711=1391&712=1395&714=1398&715=1402&717=1405&719=1408&724=1411&725=1413&727=1417&728=1420&729=1422&730=1425&732=1427&733=1430&735=1432&738=1435&741=1438&742=1441&744=1443&745=1446&747=1449&748=1451&755=1457&757=1461&758=1463&759=1466&761=1468&762=1471&764=1475&765=1479&767=1482&768=1486&770=1489&771=1493&773=1496&774=1500&776=1505&777=1509&779=1514&780=1518&782=1523&783=1527&785=1530&786=1534&788=1538&789=1540&791=1543&796=1546&799=1549&802=1552&805=1555&807=1558&810=1561&811=1563&813=1566&814=1569&815=1571&816=1573&817=1576&820=1581&822=1583&824=1586&826=1589&828=1592&829=1595&830=1597&831=1600&833=1602&836=1605&837=1607&838=1610&839=1612&841=1616&842=1618&845=1621&846=1623&847=1626&848=1629&849=1631&850=1632&851=1634&852=1635&853=1637&856=1639&857=1642&860=1644&861=1648&862=1651&863=1653&864=1656&866=1658&867=1661&869=1663&870=1666&872=1670&873=1673&875=1677&876=1680&878=1684&879=1687&881=1691&882=1693&883=1695&884=1697&885=1699&886=1701&888=1704&890=1706&891=1708&892=1711&893=1713&894=1716&895=1720&896=1722&897=1725&900=1732&903=1736&904=1739&906=1743&907=1746&910=1749&911=1754&912=1757&913=1759&914=1762&916=1764&917=1767&919=1769&920=1772&922=1776&923=1779&925=1783&926=1786&928=1790&929=1793&931=1797&932=1799&933=1801&934=1803&935=1805&936=1807&938=1810&940=1812&941=1814&942=1817&943=1819&944=1822&945=1826&946=1828&947=1831&950=1838&953=1842&954=1844&955=1846&956=1848&958=1851&961=1854&962=1857&964=1859&965=1862&967=1864&970=1867&973=1870&974=1872&975=1875&976=1877&978=1881&980=1883&982=1886&983=1888&984=1891&985=1893&987=1896&988=1898&990=1901&991=1903&993=1906&994=1909&997=1911&998=1913&999=1916&1000=1918&1002=1922&1004=1924&1007=1927&1009=1931&1010=1933&1011=1936&1013=1938&1014=1941&1019=1944&1022=1947&1023=1950&1025=1952&1026=1955&1028=1957&1029=1960&1030=1963&1031=1965&1032=1968&1035=1971&1036=1974&1037=1977&1042=1980&1045=1983&1046=1986&1048=1988&1049=1991&1051=1993&1052=1996&1053=1999&1054=2001&1055=2004&1058=2007&1059=2010&1060=2013&1065=2016&1068=2019&1070=2022&1073=2025&1076=2028&1077=2030&1079=2033&1080=2036&1081=2038&1082=2040&1083=2043&1086=2048&1089=2050&1090=2056&1091=2059&1092=2061&1093=2064&1095=2066&1096=2069&1098=2071&1099=2074&1101=2078&1102=2081&1104=2085&1105=2088&1107=2092&1108=2095&1110=2099&1111=2102&1113=2106&1114=2109&1116=2113&1117=2115&1118=2117&1119=2119&1121=2121&1122=2123&1124=2126&1126=2128&1127=2130&1128=2133&1130=2137&1131=2139&1132=2141&1133=2143&1134=2145&1137=2149&1139=2151&1140=2153&1142=2155&1143=2158&1147=2160&1148=2162&1149=2164&1150=2166&1152=2169&1155=2172&1156=2177&1157=2180&1158=2182&1159=2185&1161=2187&1162=2190&1164=2192&1165=2195&1167=2199&1168=2202&1170=2206&1171=2209&1173=2213&1174=2216&1176=2220&1177=2223&1179=2227&1180=2230&1182=2234&1183=2236&1184=2238&1185=2240&1187=2242&1188=2244&1190=2247&1192=2249&1193=2251&1194=2254&1196=2258&1197=2260&1198=2262&1199=2264&1200=2266&1203=2270&1205=2272&1206=2274&1208=2276&1209=2279&1214=2282&1215=2285&1216=2288&1218=2295&1221=2298&1223=2301&1226=2304&1227=2306&1228=2309&1229=2311&1230=2314&1231=2316&1233=2320&1235=2322&1236=2324&1237=2327&1238=2329&1240=2333&1242=2335&1243=2337&1244=2340&1245=2342&1247=2345&1248=2347&1249=2350&1250=2352&1252=2356&1254=2358&1255=2360&1256=2363&1257=2365&1258=2368&1259=2370&1261=2374&1263=2376&1264=2378&1265=2381&1266=2383&1268=2387&1270=2389&1271=2391&1272=2394&1273=2396&1275=2399&1276=2401&1278=2404&1279=2406&1280=2409&1281=2411&1283=2415&1285=2417&1286=2419&1287=2422&1288=2424&1290=2427&1291=2429&1293=2433&1294=2435&1295=2437&1296=2440&1297=2442&1299=2445&1300=2447&1302=2451&1304=2453&1305=2455&1306=2458&1307=2460&1309=2463&1310=2465&1312=2469&1313=2471&1314=2473&1315=2476&1316=2478&1318=2481&1319=2483&1321=2487&1323=2489&1324=2491&1325=2494&1326=2496&1328=2499&1329=2501&1331=2505&1333=2507&1334=2509&1335=2512&1336=2514&1338=2517&1339=2519&1341=2522&1342=2524&1344=2528&1346=2530&1347=2532&1348=2535&1349=2537&1351=2540&1352=2542&1354=2546&1356=2548&1357=2550&1358=2553&1359=2555&1361=2558&1362=2560&1364=2563&1365=2565&1367=2569&1369=2571&1370=2573&1371=2576&1372=2578&1374=2582&1376=2584&1377=2586&1378=2589&1379=2591&1381=2594&1382=2596&1383=2599&1384=2601&1386=2605&1388=2607&1389=2609&1390=2613&1391=2615&1392=2617&1393=2619&1396=2621&1397=2623&1398=2625&1399=2627&1401=2629&1402=2631&1403=2633&1404=2635&1405=2637&1408=2640&1413=2643&1416=2646&1419=2649&1420=2651&1421=2656&1422=2658&1423=2660&1424=2662&1425=2664&1426=2666&1427=2668&1428=2670&1430=2672&1431=2674&1433=2676&1434=2678&1437=2680&1438=2683&1442=2686&1445=2689&1446=2691&1448=2694&1449=2697&1450=2699&1451=2701&1452=2704&1455=2709&1458=2711&1461=2714&1464=2717&1465=2719&1466=2722&1467=2725&1468=2727&1469=2728&1470=2730&1471=2732&1473=2733&1474=2735&1477=2737&1478=2740&1481=2742&1482=2746&1483=2749&1485=2754&1487=2756&1488=2759&1490=2761&1491=2764&1493=2766&1494=2769&1496=2773&1497=2776&1499=2780&1500=2783&1502=2787&1503=2790&1505=2794&1506=2797&1508=2801&1509=2803&1510=2806&1511=2808&1512=2811&1513=2815&1514=2817&1515=2820&1518=2827&1521=2831&1522=2834&1524=2836&1525=2839&1527=2841&1528=2844&1529=2848&1530=2851&1532=2855&1533=2857&1534=2859&1535=2861&1537=2864&1539=2866&1540=2868&1541=2873&1542=2875&1543=2877&1544=2879&1545=2881&1546=2883&1547=2885&1548=2887&1550=2889&1551=2891&1553=2893&1554=2895&1557=2897&1558=2900&1562=2903&1563=2906&1565=2908&1566=2911&1569=2914&1570=2918&1571=2921&1573=2926&1575=2928&1576=2931&1578=2933&1579=2936&1581=2938&1582=2941&1584=2945&1585=2948&1587=2952&1588=2955&1590=2959&1591=2962&1593=2966&1594=2969&1596=2973&1597=2975&1598=2978&1599=2980&1600=2983&1601=2987&1602=2989&1603=2992&1606=2999&1609=3003&1610=3006&1612=3008&1613=3011&1615=3013&1616=3016&1617=3020&1618=3023&1620=3027&1621=3029&1622=3031&1623=3033&1625=3036&1627=3038&1628=3040&1629=3045&1630=3047&1631=3049&1632=3051&1633=3053&1634=3055&1635=3057&1636=3059&1638=3061&1639=3063&1641=3065&1642=3067&1645=3069&1646=3072&1650=3075&1651=3078&1653=3080&1654=3083&1657=3086&1658=3088&1659=3092&1660=3094&1661=3096&1663=3099&1666=3102&1667=3104&1668=3108&1669=3110&1670=3112&1672=3115&1675=3118&1678=3121&1679=3124&1681=3126&1684=3129&1685=3131&1686=3135&1687=3137&1688=3139&1690=3142&1693=3145&1694=3147&1695=3150&1696=3153&1702=3156&1705=3159&1708=3162&1709=3165&1710=3168&1711=3170&1712=3173&1714=3175&1715=3178&1717=3180&1718=3183&1720=3187&1721=3190&1724=3195&1725=3198&1726=3201&1727=3203&1728=3206&1730=3208&1731=3211&1733=3213&1734=3216&1736=3220&1737=3223&1740=3228&1741=3230&1742=3233&1743=3235&1744=3238&1745=3240&1747=3244&1749=3246&1750=3248&1751=3251&1752=3253&1754=3257&1756=3259&1757=3261&1758=3264&1759=3266&1761=3269&1762=3271&1764=3274&1765=3276&1766=3279&1767=3281&1769=3285&1771=3287&1772=3289&1773=3292&1774=3294&1776=3298&1777=3300&1778=3302&1779=3305&1780=3307&1782=3311&1784=3313&1785=3315&1786=3318&1787=3320&1789=3324&1790=3326&1791=3328&1792=3331&1793=3333&1795=3337&1797=3339&1798=3341&1799=3344&1800=3346&1802=3350&1804=3352&1805=3354&1806=3357&1807=3359&1809=3362&1810=3364&1812=3368&1814=3370&1815=3372&1816=3375&1817=3377&1819=3381&1821=3383&1822=3385&1823=3388&1824=3390&1826=3393&1827=3395&1829=3399&1831=3401&1832=3403&1833=3406&1834=3408&1836=3412&1838=3414&1839=3416&1840=3420&1841=3422&1842=3424&1843=3426&1846=3428&1847=3430&1849=3432&1850=3434&1851=3436&1852=3438&1854=3441&1859=3444&1862=3447&1863=3450&1864=3453&1865=3455&1866=3458&1868=3460&1869=3463&1871=3467&1872=3470&1875=3475&1876=3478&1877=3481&1878=3483&1879=3486&1881=3488&1882=3491&1884=3495&1885=3498&1890=3503&1893=3506&1895=3509&1898=3512&1901=3515&1902=3517&1904=3520&1905=3523&1906=3525&1907=3527&1908=3530&1911=3535&1914=3537&1915=3541&1916=3544&1917=3546&1918=3549&1920=3551&1921=3554&1923=3556&1924=3559&1926=3563&1927=3566&1929=3570&1930=3573&1932=3577&1933=3580&1935=3584&1936=3587&1938=3591&1939=3594&1941=3598&1942=3600&1943=3603&1945=3607&1946=3609&1947=3611&1948=3613&1949=3615&1952=3619&1954=3621&1955=3623&1957=3625&1958=3628&1963=3631&1964=3635&1965=3638&1966=3640&1967=3643&1969=3645&1970=3648&1972=3650&1973=3653&1975=3657&1976=3660&1978=3664&1979=3667&1981=3671&1982=3674&1984=3678&1985=3681&1987=3685&1988=3688&1990=3692&1991=3694&1992=3697&1994=3701&1995=3703&1996=3705&1997=3707&1998=3709&2001=3713&2003=3715&2004=3717&2006=3719&2007=3722&2012=3725&2013=3728&2014=3731&2016=3738&2019=3741&2021=3744&2024=3747&2025=3749&2026=3752&2027=3754&2028=3757&2029=3759&2031=3763&2033=3765&2034=3767&2035=3770&2036=3772&2038=3776&2040=3778&2041=3780&2042=3783&2043=3785&2045=3789&2047=3791&2048=3793&2049=3796&2050=3798&2052=3801&2053=3803&2054=3806&2055=3808&2057=3812&2059=3814&2060=3816&2061=3819&2062=3821&2063=3824&2064=3826&2066=3830&2068=3832&2069=3834&2070=3837&2071=3839&2073=3843&2075=3845&2076=3847&2077=3850&2078=3852&2080=3855&2081=3857&2083=3860&2084=3862&2085=3865&2086=3867&2088=3871&2090=3873&2091=3875&2092=3878&2093=3880&2095=3883&2096=3885&2098=3889&2099=3891&2100=3893&2101=3896&2102=3898&2104=3901&2105=3903&2107=3907&2109=3909&2110=3911&2111=3914&2112=3916&2114=3919&2115=3921&2117=3925&2119=3927&2120=3929&2121=3932&2122=3934&2124=3937&2125=3939&2127=3942&2128=3944&2130=3948&2132=3950&2133=3952&2134=3955&2135=3957&2137=3960&2138=3962&2139=3965&2140=3967&2142=3971&2144=3973&2145=3975&2146=3979&2147=3981&2148=3983&2149=3985&2152=3987&2153=3989&2154=3991&2155=3993&2157=3995&2158=3997&2159=3999&2160=4001&2161=4003&2164=4006&2169=4009&2172=4012&2173=4015&2175=4017&2176=4020&2178=4022&2181=4025&2182=4028&2183=4031&2184=4033&2185=4036&2187=4038&2188=4041&2191=4044&2192=4047&2193=4050&2195=4052&2196=4055&2198=4057&2199=4060&2201=4064&2202=4067&2205=4072&2206=4076&2207=4078&2208=4080&2210=4083&2212=4086&2213=4088&2214=4091&2215=4093&2216=4096&2217=4098&2219=4102&2221=4104&2222=4106&2223=4109&2224=4111&2226=4114&2227=4116&2229=4119&2230=4121&2231=4124&2232=4126&2234=4130&2236=4132&2237=4134&2238=4137&2239=4139&2241=4143&2242=4145&2243=4147&2244=4150&2245=4152&2247=4156&2249=4158&2250=4160&2251=4163&2252=4165&2254=4169&2255=4171&2256=4173&2257=4176&2258=4178&2260=4182&2262=4184&2263=4186&2264=4189&2265=4191&2267=4195&2269=4197&2270=4199&2271=4202&2272=4204&2274=4207&2275=4209&2277=4213&2279=4215&2280=4217&2281=4220&2282=4222&2284=4226&2286=4228&2287=4230&2288=4233&2289=4235&2291=4238&2292=4240&2294=4244&2296=4246&2297=4248&2298=4251&2299=4253&2301=4257&2303=4259&2304=4261&2305=4265&2306=4267&2307=4269&2308=4271&2311=4273&2312=4275&2314=4277&2315=4279&2316=4281&2317=4283&2319=4286&2324=4289&2327=4292&2328=4295&2329=4298&2330=4300&2331=4303&2333=4305&2334=4308&2336=4312&2337=4315&2340=4320&2341=4323&2342=4326&2343=4328&2344=4331&2346=4333&2347=4336&2349=4340&2350=4343&2355=4348&2358=4351&2359=4354&2361=4356&2362=4359&2364=4361&2365=4364&2366=4367&2367=4369&2368=4372&2370=4374&2371=4377&2373=4381&2374=4384&2377=4389&2378=4392&2379=4395&2381=4397&2382=4400&2384=4404&2385=4407&2388=4412&2389=4414&2392=4417&2393=4419&2394=4422&2395=4424&2397=4427&2398=4429&2400=4433&2405=4435&2408=4438&2411=4441&2412=4443&2414=4446&2415=4449&2416=4451&2417=4453&2418=4456&2421=4461&2424=4463&2425=4466&2426=4469&2427=4471&2428=4474&2430=4476&2431=4479&2433=4481&2434=4483&2435=4486&2436=4488&2437=4491&2438=4495&2439=4497&2440=4500&2443=4507&2447=4512&2448=4515&2449=4518&2450=4520&2451=4523&2453=4525&2454=4528&2456=4530&2457=4532&2458=4535&2459=4537&2460=4540&2461=4544&2462=4546&2463=4549&2466=4556&2472=4561&2475=4564&2476=4567&2477=4570&2478=4572&2479=4575&2481=4577&2482=4579&2483=4582&2485=4587&2488=4589&2489=4592&2494=4595&2497=4598&2498=4602&2499=4605&2500=4607&2501=4610&2503=4612&2504=4615&2506=4619&2507=4622&2509=4626&2510=4629&2512=4633&2513=4636&2515=4640&2516=4642&2517=4644&2518=4646&2519=4648&2520=4650&2522=4653&2525=4656&2526=4660&2527=4663&2528=4665&2529=4668&2531=4670&2532=4673&2534=4677&2535=4680&2537=4684&2538=4687&2540=4691&2541=4694&2543=4698&2544=4700&2545=4702&2546=4704&2547=4706&2548=4708&2550=4711&2553=4714&2554=4717&2556=4719&2557=4722&2559=4724&2564=4727&2567=4730&2568=4734&2569=4737&2570=4739&2571=4742&2573=4744&2574=4747&2576=4751&2577=4754&2579=4758&2580=4761&2582=4765&2583=4768&2585=4772&2586=4774&2587=4776&2588=4778&2589=4780&2590=4782&2592=4785&2595=4788&2596=4792&2597=4795&2598=4797&2599=4800&2601=4802&2602=4805&2604=4809&2605=4812&2607=4816&2608=4819&2610=4823&2611=4826&2613=4830&2614=4832&2615=4834&2616=4836&2617=4838&2618=4840&2620=4843&2623=4846&2624=4849&2626=4851&2627=4854&2629=4856&2634=4859&2636=4878&2637=4880&2638=4883&2640=4885&2641=4887&2642=4891&2643=4893&2644=4895&2646=4897&2647=4899&2648=4901&2649=4903&2651=4906&2654=4909&2655=4911&2656=4914&2657=4918&2659=4923&2660=4925&2661=4927&2662=4930&2664=4939&2667=4943&2668=4946&2673=4951&2674=4953&2675=4956&2676=4960&2678=4965&2679=4967&2680=4969&2681=4972&2683=4981&2686=4985&2687=4988&2692=4993&2693=4996&2695=4998&2698=5001&2701=5004&2702=5007&2704=5009&2705=5011&2706=5013&2707=5015&2709=5018&2711=5020&2713=5023&2716=5026&2719=5029&2720=5031&2722=5034&2723=5037&2724=5039&2725=5041&2726=5044&2729=5049&2732=5051&2734=5053&2733=5057&2735=5061&2736=5063&2737=5065&2739=5067&2740=5069&2741=5071&2742=5073&2743=5075&2745=5078&2748=5081&2749=5092&2750=5095&2752=5099&2753=5102&2755=5106&2756=5109&2758=5111&2759=5114&2761=5116&2762=5118&2763=5120&2764=5122&2765=5124&2766=5126&2769=5129&2770=5131&2771=5134&2773=5136&2774=5139&2776=5141&2777=5144&2779=5146&2780=5149&2782=5153&2783=5156&2785=5160&2786=5163&2788=5165&2789=5168&2791=5172&2792=5175&2793=5177&2796=5180&2798=5188&2799=5191&2801=5193&2802=5196&2804=5200&2805=5202&2806=5204&2807=5206&2809=5209&2811=5211&2812=5213&2813=5215&2814=5217&2816=5220&2817=5222&2818=5224&2819=5227&2821=5229&2822=5231&2823=5233&2824=5235&2826=5238&2828=5240&2829=5243&2830=5245&2831=5248&2833=5250&2834=5253&2836=5257&2837=5260&2839=5264&2840=5267&2842=5269&2843=5271&2844=5274&2845=5276&2846=5279&2847=5283&2848=5285&2849=5288&2852=5295&2855=5299&2856=5302&2858=5306&2859=5309&2861=5313&2862=5315&2863=5317&2864=5319&2866=5321&2867=5323&2869=5326&2871=5328&2872=5331&2873=5333&2874=5336&2876=5340&2877=5342&2878=5344&2879=5346&2881=5348&2882=5350&2884=5353&2886=5355&2887=5357&2888=5359&2889=5361&2891=5364&2892=5366&2893=5369&2896=5372&2897=5375&2898=5378&2900=5385&2903=5388&2905=5391&2908=5394&2909=5398&2910=5400&2911=5402&2913=5404&2914=5406&2916=5408&2917=5410&2919=5412&2920=5414&2922=5416&2923=5418&2925=5421&2927=5424&2928=5426&2929=5428&2930=5430&2931=5432&2932=5434&2934=5436&2935=5438&2936=5440&2937=5442&2939=5445&2941=5447&2942=5449&2943=5451&2944=5453&2946=5455&2947=5457&2949=5459&2950=5461&2951=5463&2952=5465&2954=5468&2956=5470&2957=5472&2958=5474&2959=5476&2961=5478&2962=5480&2964=5483&2965=5485&2966=5487&2967=5489&2968=5491&2970=5493&2971=5495&2973=5498&2975=5500&2976=5502&2977=5504&2978=5506&2980=5508&2981=5510&2983=5513&2985=5515&2986=5517&2987=5519&2988=5521&2990=5523&2991=5525&2993=5527&2994=5529&2996=5532&2998=5534&2999=5536&3000=5538&3001=5540&3003=5542&3004=5544&3006=5547&3007=5549&3008=5551&3009=5553&3010=5555&3012=5557&3013=5559&3015=5562&3017=5564&3018=5566&3019=5568&3020=5570&3022=5572&3023=5574&3025=5577&3027=5579&3028=5581&3029=5583&3030=5585&3032=5587&3033=5589&3035=5591&3036=5593&3038=5596&3040=5598&3041=5600&3042=5602&3043=5604&3045=5606&3046=5608&3047=5610&3048=5612&3050=5615&3052=5617&3053=5619&3054=5621&3055=5623&3057=5626&3059=5628&3060=5630&3061=5632&3062=5634&3064=5637&3066=5639&3067=5641&3068=5643&3069=5645&3070=5647&3071=5649&3073=5652&3075=5654&3076=5656&3077=5658&3078=5660&3080=5663&3082=5665&3083=5667&3084=5669&3085=5671&3087=5674&3089=5676&3090=5678&3091=5682&3092=5684&3093=5686&3094=5688&3097=5690&3098=5692&3099=5694&3100=5696&3102=5698&3103=5700&3104=5702&3105=5704&3106=5706&3109=5709&3112=5712&3113=5715&3114=5718&3115=5724&3116=5727&3119=5734&3122=5737&3123=5740&3125=5742&3126=5745&3128=5747&3129=5750&3130=5753&3134=5756&3137=5759&3138=5762&3140=5764&3141=5767&3143=5769&3144=5772&3145=5775&3149=5778&3152=5781&3154=5784&3157=5787&3158=5790&3160=5792&3161=5795&3163=5797&3166=5800&3167=5802&3169=5805&3170=5808&3171=5810&3172=5812&3173=5815&3176=5820&3179=5822&3180=5826&3181=5829&3183=5831&3184=5834&3186=5836&3187=5839&3189=5843&3190=5846&3192=5850&3193=5853&3195=5857&3196=5860&3198=5864&3199=5867&3201=5871&3202=5874&3204=5878&3205=5880&3206=5883&3207=5885&3208=5888&3209=5892&3210=5894&3211=5897&3214=5904&3217=5908&3218=5910&3219=5912&3220=5914&3221=5916&3223=5918&3224=5920&3226=5923&3229=5926&3230=5930&3231=5932&3232=5934&3234=5937&3236=5940&3238=5943&3241=5946&3242=5948&3243=5950&3244=5952&3245=5954&3246=5956&3248=5959&3250=5961&3251=5963&3252=5965&3253=5967&3255=5970&3257=5972&3258=5974&3259=5976&3260=5978&3262=5980&3263=5982&3264=5984&3265=5986&3267=5989&3269=5991&3270=5993&3271=5995&3272=5997&3273=5999&3274=6001&3276=6004&3278=6006&3279=6008&3280=6010&3281=6012&3283=6015&3285=6017&3286=6019&3287=6021&3288=6023&3290=6025&3291=6027&3293=6029&3294=6031&3295=6033&3296=6035&3298=6038&3300=6040&3301=6042&3302=6044&3303=6046&3305=6048&3306=6050&3308=6053&3309=6055&3310=6057&3311=6059&3312=6061&3314=6063&3315=6065&3317=6068&3319=6070&3320=6072&3321=6074&3322=6076&3324=6078&3325=6080&3327=6083&3328=6085&3329=6087&3330=6089&3331=6091&3333=6093&3334=6095&3336=6098&3338=6100&3339=6102&3340=6104&3341=6106&3343=6108&3344=6110&3346=6113&3348=6115&3349=6117&3350=6119&3351=6121&3353=6123&3354=6125&3356=6127&3357=6129&3359=6132&3361=6134&3362=6136&3363=6138&3364=6140&3366=6142&3367=6144&3369=6147&3371=6149&3372=6151&3373=6153&3374=6155&3376=6157&3377=6159&3379=6161&3380=6163&3382=6166&3384=6168&3385=6170&3386=6172&3387=6174&3389=6177&3391=6179&3392=6181&3393=6183&3394=6185&3396=6187&3397=6189&3398=6191&3399=6193&3401=6196&3403=6198&3404=6200&3405=6204&3406=6206&3407=6208&3408=6210&3411=6212&3412=6214&3413=6216&3414=6218&3416=6220&3417=6222&3418=6224&3419=6226&3420=6228&3423=6231&3427=6234&3430=6237&3431=6240&3433=6242&3434=6245&3436=6247&3439=6250&3440=6253&3441=6256&3443=6258&3444=6261&3446=6263&3447=6266&3449=6270&3450=6273&3453=6278&3454=6282&3455=6284&3456=6286&3458=6289&3460=6292&3461=6294&3462=6296&3463=6298&3464=6300&3465=6302&3467=6305&3469=6307&3470=6309&3471=6311&3472=6313&3474=6316&3476=6318&3477=6320&3478=6322&3479=6324&3481=6326&3482=6328&3484=6330&3485=6332&3486=6334&3487=6336&3489=6339&3491=6341&3492=6343&3493=6345&3494=6347&3496=6350&3497=6352&3498=6354&3499=6356&3500=6358&3502=6361&3504=6363&3505=6365&3506=6367&3507=6369&3509=6372&3510=6374&3511=6376&3512=6378&3513=6380&3515=6383&3517=6385&3518=6387&3519=6389&3520=6391&3522=6394&3524=6396&3525=6398&3526=6400&3527=6402&3529=6404&3530=6406&3532=6409&3534=6411&3535=6413&3536=6415&3537=6417&3539=6420&3541=6422&3542=6424&3543=6426&3544=6428&3546=6430&3547=6432&3549=6435&3551=6437&3552=6439&3553=6441&3554=6443&3556=6446&3558=6448&3559=6450&3560=6454&3561=6456&3562=6458&3563=6460&3566=6462&3567=6464&3569=6466&3570=6468&3571=6470&3572=6472&3573=6474&3576=6477&3580=6480&3583=6483&3585=6486&3588=6489&3589=6492&3591=6494&3592=6497&3594=6499&3597=6502&3598=6504&3600=6507&3601=6510&3602=6512&3603=6514&3604=6517&3607=6522&3610=6524&3611=6527&3612=6530&3614=6532&3615=6535&3617=6537&3618=6540&3620=6544&3621=6547&3623=6551&3624=6554&3626=6558&3627=6561&3629=6565&3630=6568&3632=6572&3633=6575&3635=6579&3636=6581&3637=6584&3638=6586&3639=6589&3640=6593&3641=6595&3642=6598&3645=6605&3649=6610&3650=6614&3651=6616&3652=6618&3654=6621&3656=6624&3658=6627&3661=6630&3662=6632&3663=6634&3664=6636&3665=6638&3666=6640&3668=6643&3670=6645&3671=6647&3672=6649&3673=6651&3675=6654&3677=6656&3678=6658&3679=6660&3680=6662&3682=6665&3684=6667&3685=6669&3686=6671&3687=6673&3689=6675&3690=6677&3691=6679&3692=6681&3694=6684&3696=6686&3697=6688&3698=6690&3699=6692&3700=6694&3701=6696&3703=6699&3705=6701&3706=6703&3707=6705&3708=6707&3710=6710&3712=6712&3713=6714&3714=6716&3715=6718&3717=6720&3718=6722&3720=6724&3721=6726&3722=6728&3723=6730&3725=6733&3727=6735&3728=6737&3729=6739&3730=6741&3732=6743&3733=6745&3735=6748&3736=6750&3737=6752&3738=6754&3739=6756&3741=6758&3742=6760&3744=6763&3746=6765&3747=6767&3748=6769&3749=6771&3751=6773&3752=6775&3754=6778&3756=6780&3757=6782&3758=6784&3759=6786&3761=6788&3762=6790&3764=6792&3765=6794&3767=6797&3769=6799&3770=6801&3771=6803&3772=6805&3774=6807&3775=6809&3776=6811&3777=6813&3779=6816&3781=6818&3782=6820&3783=6824&3784=6826&3785=6828&3786=6830&3789=6832&3790=6834&3791=6836&3792=6838&3794=6840&3795=6842&3796=6844&3797=6846&3798=6848&3801=6851&3805=6854&3808=6857&3809=6860&3811=6862&3812=6865&3814=6867&3817=6870&3818=6873&3819=6876&3821=6878&3822=6881&3824=6883&3825=6886&3827=6890&3828=6893&3831=6898&3832=6902&3833=6904&3834=6906&3836=6909&3838=6912&3839=6914&3840=6916&3841=6918&3842=6920&3843=6922&3845=6925&3847=6927&3848=6929&3849=6931&3850=6933&3852=6935&3853=6937&3855=6939&3856=6941&3857=6943&3858=6945&3860=6948&3862=6950&3863=6952&3864=6954&3865=6956&3867=6959&3868=6961&3869=6963&3870=6965&3871=6967&3873=6970&3875=6972&3876=6974&3877=6976&3878=6978&3880=6981&3881=6983&3882=6985&3883=6987&3884=6989&3886=6992&3888=6994&3889=6996&3890=6998&3891=7000&3893=7003&3895=7005&3896=7007&3897=7009&3898=7011&3900=7013&3901=7015&3903=7018&3905=7020&3906=7022&3907=7024&3908=7026&3910=7029&3912=7031&3913=7033&3914=7035&3915=7037&3917=7039&3918=7041&3920=7044&3922=7046&3923=7048&3924=7050&3925=7052&3927=7055&3929=7057&3930=7059&3931=7063&3932=7065&3933=7067&3934=7069&3937=7071&3938=7073&3940=7075&3941=7077&3942=7079&3943=7081&3944=7083&3947=7086&3951=7089&3953=7092&3954=7094&3955=7096&3956=7099&3959=7104&3962=7106&3965=7109&3970=7112&3972=7115&3976=7118&3977=7122&3978=7124&3979=7127&3982=7130&3984=7133'