from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-isis.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_isis = resolve('router_isis')
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    l_0_loopback_interfaces = resolve('loopback_interfaces')
    l_0_node_sid_loopbacks = resolve('node_sid_loopbacks')
    l_0_rcf = resolve('rcf')
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
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis)):
        pass
        yield '\n### Router ISIS\n\n#### Router ISIS Summary\n\n| Settings | Value |\n| -------- | ----- |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'instance')):
            pass
            yield '| Instance | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'instance'))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'net')):
            pass
            yield '| Net-ID | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'net'))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'is_type')):
            pass
            yield '| Type | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'is_type'))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'router_id')):
            pass
            yield '| Router-ID | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'router_id'))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'log_adjacency_changes')):
            pass
            yield '| Log Adjacency Changes | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'log_adjacency_changes'))
            yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'mpls_ldp_sync_default'), True):
            pass
            yield '| MPLS LDP Sync Default | '
            yield str(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'mpls_ldp_sync_default'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'advertise'), 'passive_only'), True):
            pass
            yield '| Advertise Passive-only | '
            yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'advertise'), 'passive_only'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'enabled')):
            pass
            yield '| SR MPLS Enabled | '
            yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'enabled'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval')):
            pass
            yield '| SPF Interval | '
            yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval'))
            yield ' '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'interval_unit'), 'seconds'))
            yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'wait_interval')):
                pass
                yield '| SPF Interval Wait Time| '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'wait_interval'))
                yield ' milliseconds |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'hold_interval')):
                    pass
                    yield '| SPF Interval Hold Time| '
                    yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'spf_interval'), 'hold_interval'))
                    yield ' milliseconds |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart')):
            pass
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'enabled'), True):
                pass
                yield '| Graceful-restart Enabled | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'enabled'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_1_wait_time')):
                pass
                yield '| Graceful-restart t2 Level-1 | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_1_wait_time'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_2_wait_time')):
                pass
                yield '| Graceful-restart t2 Level-2 | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 't2'), 'level_2_wait_time'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'restart_hold_time')):
                pass
                yield '| Graceful-restart Restart-hold-time | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'graceful_restart'), 'restart_hold_time'))
                yield ' |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers')):
            pass
            yield '\n#### ISIS Route Timers\n\n| Settings | Value |\n| -------- | ----- |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'local_convergence'), 'protected_prefixes'), True):
                pass
                yield '| Local Convergence Delay | '
                yield str(t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'local_convergence'), 'delay'), 10000))
                yield ' milliseconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'interval')):
                pass
                yield '| CSN Packet Transmission Interval | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'interval'))
                yield ' seconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'p2p_disabled')):
                pass
                yield '| CSN Packet P2P Links Disabled | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'csnp'), 'generation'), 'p2p_disabled'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'interval')):
                pass
                yield '| LSP Generation Maximum Interval | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'interval'))
                yield ' seconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'initial_wait_time')):
                pass
                yield '| LSP Generation Initial Wait-time | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'initial_wait_time'))
                yield ' milliseconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'wait_time')):
                pass
                yield '| LSP Generation Wait-time | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'generation'), 'wait_time'))
                yield ' milliseconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'out_delay')):
                pass
                yield '| LSP Out-delay | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'out_delay'))
                yield ' milliseconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'refresh_interval')):
                pass
                yield '| LSP Refresh Interval | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'refresh_interval'))
                yield ' seconds |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'min_remaining_lifetime')):
                pass
                yield '| LSP Minimum Remaining Lifetime | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'timers'), 'lsp'), 'min_remaining_lifetime'))
                yield ' seconds |\n'
        if t_4(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'redistribute_routes')):
            pass
            yield '\n#### ISIS Route Redistribution\n\n| Route Type | Route-Map | Include Leaked |\n| ---------- | --------- | -------------- |\n'
            for l_1_redistribute_route in t_2(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'redistribute_routes'), 'source_protocol'):
                l_1_include_leaked = resolve('include_leaked')
                l_1_src_protocol = l_1_route_map = missing
                _loop_vars = {}
                pass
                l_1_src_protocol = t_1(environment.getattr(l_1_redistribute_route, 'source_protocol'), '-')
                _loop_vars['src_protocol'] = l_1_src_protocol
                l_1_route_map = t_1(environment.getattr(l_1_redistribute_route, 'route_map'), '-')
                _loop_vars['route_map'] = l_1_route_map
                if ((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol) in ['static', 'connected', 'ospf']):
                    pass
                    l_1_include_leaked = t_1(environment.getattr(l_1_redistribute_route, 'include_leaked'), '-')
                    _loop_vars['include_leaked'] = l_1_include_leaked
                else:
                    pass
                    l_1_include_leaked = '-'
                    _loop_vars['include_leaked'] = l_1_include_leaked
                if ((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol) == 'isis'):
                    pass
                    l_1_src_protocol = str_join(((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol), ' instance', ))
                    _loop_vars['src_protocol'] = l_1_src_protocol
                if (((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol) in ['ospf', 'ospfv3']) and t_4(environment.getattr(l_1_redistribute_route, 'ospf_route_type'))):
                    pass
                    l_1_src_protocol = str_join(((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol), ' ', environment.getattr(l_1_redistribute_route, 'ospf_route_type'), ))
                    _loop_vars['src_protocol'] = l_1_src_protocol
                yield '| '
                yield str((undefined(name='src_protocol') if l_1_src_protocol is missing else l_1_src_protocol))
                yield ' | '
                yield str((undefined(name='route_map') if l_1_route_map is missing else l_1_route_map))
                yield ' | '
                yield str((undefined(name='include_leaked') if l_1_include_leaked is missing else l_1_include_leaked))
                yield ' |\n'
            l_1_redistribute_route = l_1_src_protocol = l_1_route_map = l_1_include_leaked = missing
        yield '\n#### ISIS Interfaces Summary\n\n| Interface | ISIS Instance | ISIS Metric | Interface Mode |\n| --------- | ------------- | ----------- | -------------- |\n'
        for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            l_1_row_isis_instance = resolve('row_isis_instance')
            l_1_row_isis_metric = resolve('row_isis_metric')
            l_1_row_intf_mode = resolve('row_intf_mode')
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_ethernet_interface, 'isis_enable')):
                pass
                l_1_row_isis_instance = environment.getattr(l_1_ethernet_interface, 'isis_enable')
                _loop_vars['row_isis_instance'] = l_1_row_isis_instance
                l_1_row_isis_metric = t_1(environment.getattr(l_1_ethernet_interface, 'isis_metric'), '-')
                _loop_vars['row_isis_metric'] = l_1_row_isis_metric
                if t_4(environment.getattr(l_1_ethernet_interface, 'isis_network_point_to_point'), True):
                    pass
                    l_1_row_intf_mode = 'point-to-point'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                elif t_4(environment.getattr(l_1_ethernet_interface, 'isis_passive'), True):
                    pass
                    l_1_row_intf_mode = 'passive'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                else:
                    pass
                    l_1_row_intf_mode = '-'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_isis_instance') if l_1_row_isis_instance is missing else l_1_row_isis_instance))
                yield ' | '
                yield str((undefined(name='row_isis_metric') if l_1_row_isis_metric is missing else l_1_row_isis_metric))
                yield ' | '
                yield str((undefined(name='row_intf_mode') if l_1_row_intf_mode is missing else l_1_row_intf_mode))
                yield ' |\n'
        l_1_ethernet_interface = l_1_row_isis_instance = l_1_row_isis_metric = l_1_row_intf_mode = missing
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            l_1_row_isis_instance = resolve('row_isis_instance')
            l_1_row_isis_metric = resolve('row_isis_metric')
            l_1_row_intf_mode = resolve('row_intf_mode')
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_vlan_interface, 'isis_enable')):
                pass
                l_1_row_isis_instance = environment.getattr(l_1_vlan_interface, 'isis_enable')
                _loop_vars['row_isis_instance'] = l_1_row_isis_instance
                l_1_row_isis_metric = t_1(environment.getattr(l_1_vlan_interface, 'isis_metric'), '-')
                _loop_vars['row_isis_metric'] = l_1_row_isis_metric
                if t_4(environment.getattr(l_1_vlan_interface, 'isis_network_point_to_point'), True):
                    pass
                    l_1_row_intf_mode = 'point-to-point'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                elif t_4(environment.getattr(l_1_vlan_interface, 'isis_passive'), True):
                    pass
                    l_1_row_intf_mode = 'passive'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                else:
                    pass
                    l_1_row_intf_mode = '-'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                yield '| '
                yield str(environment.getattr(l_1_vlan_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_isis_instance') if l_1_row_isis_instance is missing else l_1_row_isis_instance))
                yield ' | '
                yield str((undefined(name='row_isis_metric') if l_1_row_isis_metric is missing else l_1_row_isis_metric))
                yield ' | '
                yield str((undefined(name='row_intf_mode') if l_1_row_intf_mode is missing else l_1_row_intf_mode))
                yield ' |\n'
        l_1_vlan_interface = l_1_row_isis_instance = l_1_row_isis_metric = l_1_row_intf_mode = missing
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            l_1_row_isis_instance = resolve('row_isis_instance')
            l_1_row_isis_metric = resolve('row_isis_metric')
            l_1_row_intf_mode = resolve('row_intf_mode')
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_loopback_interface, 'isis_enable')):
                pass
                l_1_row_isis_instance = environment.getattr(l_1_loopback_interface, 'isis_enable')
                _loop_vars['row_isis_instance'] = l_1_row_isis_instance
                l_1_row_isis_metric = t_1(environment.getattr(l_1_loopback_interface, 'isis_metric'), '-')
                _loop_vars['row_isis_metric'] = l_1_row_isis_metric
                if t_4(environment.getattr(l_1_loopback_interface, 'isis_network_point_to_point'), True):
                    pass
                    l_1_row_intf_mode = 'point-to-point'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                elif t_4(environment.getattr(l_1_loopback_interface, 'isis_passive'), True):
                    pass
                    l_1_row_intf_mode = 'passive'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                else:
                    pass
                    l_1_row_intf_mode = '-'
                    _loop_vars['row_intf_mode'] = l_1_row_intf_mode
                yield '| '
                yield str(environment.getattr(l_1_loopback_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_isis_instance') if l_1_row_isis_instance is missing else l_1_row_isis_instance))
                yield ' | '
                yield str((undefined(name='row_isis_metric') if l_1_row_isis_metric is missing else l_1_row_isis_metric))
                yield ' | '
                yield str((undefined(name='row_intf_mode') if l_1_row_intf_mode is missing else l_1_row_intf_mode))
                yield ' |\n'
        l_1_loopback_interface = l_1_row_isis_instance = l_1_row_isis_metric = l_1_row_intf_mode = missing
        l_0_node_sid_loopbacks = []
        context.vars['node_sid_loopbacks'] = l_0_node_sid_loopbacks
        context.exported_vars.add('node_sid_loopbacks')
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_4(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv4_index')) or t_4(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv6_index'))):
                pass
                context.call(environment.getattr((undefined(name='node_sid_loopbacks') if l_0_node_sid_loopbacks is missing else l_0_node_sid_loopbacks), 'append'), l_1_loopback_interface, _loop_vars=_loop_vars)
        l_1_loopback_interface = missing
        if (t_3((undefined(name='node_sid_loopbacks') if l_0_node_sid_loopbacks is missing else l_0_node_sid_loopbacks)) > 0):
            pass
            yield '\n#### ISIS Segment-routing Node-SID\n\n| Loopback | IPv4 Index | IPv6 Index |\n| -------- | ---------- | ---------- |\n'
            for l_1_loopback_interface in t_2((undefined(name='node_sid_loopbacks') if l_0_node_sid_loopbacks is missing else l_0_node_sid_loopbacks)):
                l_1_row_ipv4_index = l_1_row_ipv6_index = missing
                _loop_vars = {}
                pass
                l_1_row_ipv4_index = t_1(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv4_index'), '-')
                _loop_vars['row_ipv4_index'] = l_1_row_ipv4_index
                l_1_row_ipv6_index = t_1(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv6_index'), '-')
                _loop_vars['row_ipv6_index'] = l_1_row_ipv6_index
                yield '| '
                yield str(environment.getattr(l_1_loopback_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_ipv4_index') if l_1_row_ipv4_index is missing else l_1_row_ipv4_index))
                yield ' | '
                yield str((undefined(name='row_ipv6_index') if l_1_row_ipv6_index is missing else l_1_row_ipv6_index))
                yield ' |\n'
            l_1_loopback_interface = l_1_row_ipv4_index = l_1_row_ipv6_index = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'prefix_segments')):
            pass
            yield '\n#### Prefix Segments\n\n| Prefix Segment | Index |\n| -------------- | ----- |\n'
            for l_1_prefix_segment in t_2(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'segment_routing_mpls'), 'prefix_segments'), 'prefix'):
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_prefix_segment, 'index')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_prefix_segment, 'prefix'))
                    yield ' | '
                    yield str(environment.getattr(l_1_prefix_segment, 'index'))
                    yield ' |\n'
            l_1_prefix_segment = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'enabled'), True):
            pass
            yield '\n#### ISIS IPv4 Address Family Summary\n\n| Settings | Value |\n| -------- | ----- |\n| IPv4 Address-family Enabled | True |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'maximum_paths')):
                pass
                yield '| Maximum-paths | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'maximum_paths'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'bfd_all_interfaces')):
                pass
                yield '| BFD All-interfaces | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'bfd_all_interfaces'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'mode')):
                pass
                yield '| TI-LFA Mode | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'mode'))
                yield ' |\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'level')):
                    pass
                    yield '| TI-LFA Level | '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'level'))
                    yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'), True):
                pass
                yield '| TI-LFA SRLG Enabled | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'))
                yield ' |\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'), True):
                    pass
                    yield '| TI-LFA SRLG Strict Mode | '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'))
                    yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'tunnel_source_labeled_unicast'), 'enabled'), True):
                pass
                yield '\n#### Tunnel Source\n\n| Source Protocol | RCF |\n| --------------- | --- |\n'
                l_0_rcf = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv4'), 'tunnel_source_labeled_unicast'), 'rcf'), '-')
                context.vars['rcf'] = l_0_rcf
                context.exported_vars.add('rcf')
                yield '| BGP Labeled-Unicast | '
                yield str((undefined(name='rcf') if l_0_rcf is missing else l_0_rcf))
                yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'enabled'), True):
            pass
            yield '\n#### ISIS IPv6 Address Family Summary\n\n| Settings | Value |\n| -------- | ----- |\n| IPv6 Address-family Enabled | True |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'maximum_paths')):
                pass
                yield '| Maximum-paths | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'maximum_paths'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'bfd_all_interfaces')):
                pass
                yield '| BFD All-interfaces | '
                yield str(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'bfd_all_interfaces'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'mode')):
                pass
                yield '| TI-LFA Mode | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'mode'))
                yield ' |\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'level')):
                    pass
                    yield '| TI-LFA Level | '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'level'))
                    yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'), True):
                pass
                yield '| TI-LFA SRLG Enabled | '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'enable'))
                yield ' |\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'), True):
                    pass
                    yield '| TI-LFA SRLG Strict Mode | '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis), 'address_family_ipv6'), 'fast_reroute_ti_lfa'), 'srlg'), 'strict'))
                    yield ' |\n'
        yield '\n#### Router ISIS Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-isis.j2', 'documentation/router-isis.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'node_sid_loopbacks': l_0_node_sid_loopbacks, 'rcf': l_0_rcf})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=41&15=44&16=47&18=49&19=52&21=54&22=57&24=59&25=62&27=64&28=67&30=69&31=72&33=74&34=77&36=79&37=82&39=84&40=87&41=91&42=94&43=96&44=99&48=101&49=103&50=106&52=108&53=111&55=113&56=116&58=118&59=121&62=123&68=126&69=129&71=131&72=134&74=136&75=139&77=141&78=144&80=146&81=149&83=151&84=154&86=156&87=159&89=161&90=164&92=166&93=169&96=171&102=174&103=179&104=181&105=183&106=185&108=189&110=191&111=193&113=195&114=197&116=200&126=208&127=214&128=216&129=218&130=220&131=222&132=224&133=226&135=230&137=233&143=242&144=248&145=250&146=252&147=254&148=256&149=258&150=260&152=264&154=267&160=276&161=282&162=284&163=286&164=288&165=290&166=292&167=294&169=298&171=301&175=310&176=313&177=316&178=318&181=320&187=323&188=327&189=329&190=332&193=339&199=342&200=345&201=348&205=353&212=356&213=359&215=361&216=364&218=366&219=369&220=371&221=374&224=376&225=379&226=381&227=384&230=386&236=389&237=393&240=395&247=398&248=401&250=403&251=406&253=408&254=411&255=413&256=416&259=418&260=421&261=423&262=426&270=429'