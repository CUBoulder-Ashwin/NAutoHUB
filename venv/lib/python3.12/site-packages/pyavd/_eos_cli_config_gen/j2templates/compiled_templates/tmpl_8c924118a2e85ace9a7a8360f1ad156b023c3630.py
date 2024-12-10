from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ethernet-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_encapsulation_dot1q_interfaces = resolve('encapsulation_dot1q_interfaces')
    l_0_flexencap_interfaces = resolve('flexencap_interfaces')
    l_0_namespace = resolve('namespace')
    l_0_ethernet_interface_pvlan = resolve('ethernet_interface_pvlan')
    l_0_ethernet_interface_vlan_xlate = resolve('ethernet_interface_vlan_xlate')
    l_0_tcp_mss_clampings = resolve('tcp_mss_clampings')
    l_0_transceiver_settings = resolve('transceiver_settings')
    l_0_link_tracking_interfaces = resolve('link_tracking_interfaces')
    l_0_phone_interfaces = resolve('phone_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_multicast_interfaces = resolve('multicast_interfaces')
    l_0_ethernet_interface_ipv4 = resolve('ethernet_interface_ipv4')
    l_0_port_channel_interface_ipv4 = resolve('port_channel_interface_ipv4')
    l_0_ip_nat_interfaces = resolve('ip_nat_interfaces')
    l_0_ethernet_interface_ipv6 = resolve('ethernet_interface_ipv6')
    l_0_port_channel_interface_ipv6 = resolve('port_channel_interface_ipv6')
    l_0_ethernet_interfaces_isis = resolve('ethernet_interfaces_isis')
    l_0_port_channel_interfaces_isis = resolve('port_channel_interfaces_isis')
    l_0_ethernet_interfaces_vrrp_details = resolve('ethernet_interfaces_vrrp_details')
    l_0_evpn_es_ethernet_interfaces = resolve('evpn_es_ethernet_interfaces')
    l_0_evpn_dfe_ethernet_interfaces = resolve('evpn_dfe_ethernet_interfaces')
    l_0_evpn_mpls_ethernet_interfaces = resolve('evpn_mpls_ethernet_interfaces')
    l_0_err_cor_enc_intfs = resolve('err_cor_enc_intfs')
    l_0_priority_intfs = resolve('priority_intfs')
    l_0_sync_e_interfaces = resolve('sync_e_interfaces')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.list_compress']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.list_compress' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.filters['arista.avd.range_expand']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.range_expand' found.")
    try:
        t_5 = environment.filters['first']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'first' found.")
    try:
        t_6 = environment.filters['float']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'float' found.")
    try:
        t_7 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    try:
        t_8 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_9 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_9(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_10 = environment.filters['map']
    except KeyError:
        @internalcode
        def t_10(*unused):
            raise TemplateRuntimeError("No filter named 'map' found.")
    try:
        t_11 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_11(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_12 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_12(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_12((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces)):
        pass
        yield '\n### Ethernet Interfaces\n\n#### Ethernet Interfaces Summary\n\n##### L2\n\n| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |\n| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |\n'
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            l_1_port_channel_interface_name = resolve('port_channel_interface_name')
            l_1_port_channel_interface = resolve('port_channel_interface')
            l_1_description = resolve('description')
            l_1_mode = resolve('mode')
            l_1_switchport_vlans = resolve('switchport_vlans')
            l_1_native_vlan = resolve('native_vlan')
            l_1_channel_group = resolve('channel_group')
            l_1_trunk_groups = resolve('trunk_groups')
            _loop_vars = {}
            pass
            if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')):
                pass
                l_1_port_channel_interface_name = str_join(('Port-Channel', environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), ))
                _loop_vars['port_channel_interface_name'] = l_1_port_channel_interface_name
                l_1_port_channel_interface = t_5(environment, t_11(context, t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), []), 'name', 'arista.avd.defined', (undefined(name='port_channel_interface_name') if l_1_port_channel_interface_name is missing else l_1_port_channel_interface_name)))
                _loop_vars['port_channel_interface'] = l_1_port_channel_interface
                if (((((((t_12(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'mode')) or t_12(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'access_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'allowed_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'native_vlan_tag'), True)) or t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'native_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'groups'))) or t_12(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'enabled'), True)) and ((not t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'type'))) or (t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'type')) and (environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'type') not in ['switched', 'routed'])))):
                    pass
                    l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                    _loop_vars['description'] = l_1_description
                    l_1_mode = t_1(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'mode'), '-')
                    _loop_vars['mode'] = l_1_mode
                    if (t_12(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'access_vlan')) or t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'allowed_vlan'))):
                        pass
                        l_1_switchport_vlans = []
                        _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                        if t_12(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'access_vlan')):
                            pass
                            context.call(environment.getattr((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), 'append'), environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'access_vlan'), _loop_vars=_loop_vars)
                        if t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'allowed_vlan')):
                            pass
                            context.call(environment.getattr((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), 'extend'), t_10(context, t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'allowed_vlan')), 'int'), _loop_vars=_loop_vars)
                        if (undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans):
                            pass
                            l_1_switchport_vlans = t_2((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans))
                            _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                        else:
                            pass
                            l_1_switchport_vlans = environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'allowed_vlan')
                            _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                    if t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'native_vlan_tag'), True):
                        pass
                        l_1_native_vlan = 'tag'
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    else:
                        pass
                        l_1_native_vlan = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'native_vlan'), '-')
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    l_1_channel_group = environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')
                    _loop_vars['channel_group'] = l_1_channel_group
                    l_1_trunk_groups = t_8(context.eval_ctx, t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'switchport'), 'trunk'), 'groups'), ['-']), ', ')
                    _loop_vars['trunk_groups'] = l_1_trunk_groups
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                    yield ' | *'
                    yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                    yield ' | *'
                    yield str(t_1((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), '-'))
                    yield ' | *'
                    yield str((undefined(name='native_vlan') if l_1_native_vlan is missing else l_1_native_vlan))
                    yield ' | *'
                    yield str((undefined(name='trunk_groups') if l_1_trunk_groups is missing else l_1_trunk_groups))
                    yield ' | '
                    yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                    yield ' |\n'
                elif t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'type'), 'switched'):
                    pass
                    l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                    _loop_vars['description'] = l_1_description
                    l_1_mode = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'mode'), '-')
                    _loop_vars['mode'] = l_1_mode
                    l_1_switchport_vlans = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'vlans'), '-')
                    _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                    if t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'native_vlan_tag'), True):
                        pass
                        l_1_native_vlan = 'tag'
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    else:
                        pass
                        l_1_native_vlan = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'native_vlan'), '-')
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    l_1_channel_group = environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')
                    _loop_vars['channel_group'] = l_1_channel_group
                    l_1_trunk_groups = t_8(context.eval_ctx, t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'trunk_groups'), ['-']), ', ')
                    _loop_vars['trunk_groups'] = l_1_trunk_groups
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                    yield ' | *'
                    yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                    yield ' | *'
                    yield str((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans))
                    yield ' | *'
                    yield str((undefined(name='native_vlan') if l_1_native_vlan is missing else l_1_native_vlan))
                    yield ' | *'
                    yield str((undefined(name='trunk_groups') if l_1_trunk_groups is missing else l_1_trunk_groups))
                    yield ' | '
                    yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                    yield ' |\n'
            else:
                pass
                if (((((((t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'mode')) or t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan_tag'), True)) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'groups'))) or t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'enabled'), True)) and ((not t_12(environment.getattr(l_1_ethernet_interface, 'type'))) or (t_12(environment.getattr(l_1_ethernet_interface, 'type')) and (environment.getattr(l_1_ethernet_interface, 'type') not in ['switched', 'routed'])))):
                    pass
                    l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                    _loop_vars['description'] = l_1_description
                    l_1_mode = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'mode'), '-')
                    _loop_vars['mode'] = l_1_mode
                    if (t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan')) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan'))):
                        pass
                        l_1_switchport_vlans = []
                        _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                        if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan')):
                            pass
                            context.call(environment.getattr((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), 'append'), environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan'), _loop_vars=_loop_vars)
                        if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan')):
                            pass
                            context.call(environment.getattr((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), 'extend'), t_10(context, t_4(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan')), 'int'), _loop_vars=_loop_vars)
                        if (undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans):
                            pass
                            l_1_switchport_vlans = t_2((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans))
                            _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                        elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan'), 'none'):
                            pass
                            l_1_switchport_vlans = environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan')
                            _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                    if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan_tag'), True):
                        pass
                        l_1_native_vlan = 'tag'
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    else:
                        pass
                        l_1_native_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan'), '-')
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    l_1_trunk_groups = t_8(context.eval_ctx, t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'groups'), ['-']), ', ')
                    _loop_vars['trunk_groups'] = l_1_trunk_groups
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                    yield ' | '
                    yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                    yield ' | '
                    yield str(t_1((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans), '-'))
                    yield ' | '
                    yield str((undefined(name='native_vlan') if l_1_native_vlan is missing else l_1_native_vlan))
                    yield ' | '
                    yield str((undefined(name='trunk_groups') if l_1_trunk_groups is missing else l_1_trunk_groups))
                    yield ' | - |\n'
                elif t_12(environment.getattr(l_1_ethernet_interface, 'type'), 'switched'):
                    pass
                    l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                    _loop_vars['description'] = l_1_description
                    l_1_mode = t_1(environment.getattr(l_1_ethernet_interface, 'mode'), '-')
                    _loop_vars['mode'] = l_1_mode
                    l_1_switchport_vlans = t_1(environment.getattr(l_1_ethernet_interface, 'vlans'), '-')
                    _loop_vars['switchport_vlans'] = l_1_switchport_vlans
                    if t_12(environment.getattr(l_1_ethernet_interface, 'native_vlan_tag'), True):
                        pass
                        l_1_native_vlan = 'tag'
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    else:
                        pass
                        l_1_native_vlan = t_1(environment.getattr(l_1_ethernet_interface, 'native_vlan'), '-')
                        _loop_vars['native_vlan'] = l_1_native_vlan
                    l_1_trunk_groups = t_8(context.eval_ctx, t_1(environment.getattr(l_1_ethernet_interface, 'trunk_groups'), ['-']), ', ')
                    _loop_vars['trunk_groups'] = l_1_trunk_groups
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                    yield ' | '
                    yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                    yield ' | '
                    yield str((undefined(name='switchport_vlans') if l_1_switchport_vlans is missing else l_1_switchport_vlans))
                    yield ' | '
                    yield str((undefined(name='native_vlan') if l_1_native_vlan is missing else l_1_native_vlan))
                    yield ' | '
                    yield str((undefined(name='trunk_groups') if l_1_trunk_groups is missing else l_1_trunk_groups))
                    yield ' | - |\n'
        l_1_ethernet_interface = l_1_port_channel_interface_name = l_1_port_channel_interface = l_1_description = l_1_mode = l_1_switchport_vlans = l_1_native_vlan = l_1_channel_group = l_1_trunk_groups = missing
        yield '\n*Inherited from Port-Channel Interface\n'
        l_0_encapsulation_dot1q_interfaces = []
        context.vars['encapsulation_dot1q_interfaces'] = l_0_encapsulation_dot1q_interfaces
        context.exported_vars.add('encapsulation_dot1q_interfaces')
        l_0_flexencap_interfaces = []
        context.vars['flexencap_interfaces'] = l_0_flexencap_interfaces
        context.exported_vars.add('flexencap_interfaces')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'vlan')):
                pass
                context.call(environment.getattr((undefined(name='encapsulation_dot1q_interfaces') if l_0_encapsulation_dot1q_interfaces is missing else l_0_encapsulation_dot1q_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
            elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'encapsulation')):
                pass
                context.call(environment.getattr((undefined(name='flexencap_interfaces') if l_0_flexencap_interfaces is missing else l_0_flexencap_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
            elif (t_1(environment.getattr(l_1_ethernet_interface, 'type')) in ['l3dot1q', 'l2dot1q']):
                pass
                if t_12(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan')):
                    pass
                    context.call(environment.getattr((undefined(name='encapsulation_dot1q_interfaces') if l_0_encapsulation_dot1q_interfaces is missing else l_0_encapsulation_dot1q_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
                elif t_12(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan')):
                    pass
                    context.call(environment.getattr((undefined(name='flexencap_interfaces') if l_0_flexencap_interfaces is missing else l_0_flexencap_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='encapsulation_dot1q_interfaces') if l_0_encapsulation_dot1q_interfaces is missing else l_0_encapsulation_dot1q_interfaces)) > 0):
            pass
            yield '\n##### Encapsulation Dot1q Interfaces\n\n| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |\n| --------- | ----------- | ------- | -------------- | -------------------- |\n'
            for l_1_ethernet_interface in (undefined(name='encapsulation_dot1q_interfaces') if l_0_encapsulation_dot1q_interfaces is missing else l_0_encapsulation_dot1q_interfaces):
                l_1_description = l_1_vlan_id = l_1_encapsulation_dot1q_vlan = l_1_encapsulation_dot1q_inner_vlan = missing
                _loop_vars = {}
                pass
                l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                _loop_vars['description'] = l_1_description
                l_1_vlan_id = t_1(environment.getattr(l_1_ethernet_interface, 'vlan_id'), '-')
                _loop_vars['vlan_id'] = l_1_vlan_id
                l_1_encapsulation_dot1q_vlan = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'vlan'), environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan'), '-')
                _loop_vars['encapsulation_dot1q_vlan'] = l_1_encapsulation_dot1q_vlan
                l_1_encapsulation_dot1q_inner_vlan = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'inner_vlan'), '-')
                _loop_vars['encapsulation_dot1q_inner_vlan'] = l_1_encapsulation_dot1q_inner_vlan
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                yield ' | '
                yield str((undefined(name='vlan_id') if l_1_vlan_id is missing else l_1_vlan_id))
                yield ' | '
                yield str((undefined(name='encapsulation_dot1q_vlan') if l_1_encapsulation_dot1q_vlan is missing else l_1_encapsulation_dot1q_vlan))
                yield ' | '
                yield str((undefined(name='encapsulation_dot1q_inner_vlan') if l_1_encapsulation_dot1q_inner_vlan is missing else l_1_encapsulation_dot1q_inner_vlan))
                yield ' |\n'
            l_1_ethernet_interface = l_1_description = l_1_vlan_id = l_1_encapsulation_dot1q_vlan = l_1_encapsulation_dot1q_inner_vlan = missing
        if (t_9((undefined(name='flexencap_interfaces') if l_0_flexencap_interfaces is missing else l_0_flexencap_interfaces)) > 0):
            pass
            yield '\n##### Flexible Encapsulation Interfaces\n\n| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |\n| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- |------------ | ---------------------- | ---------------------- |\n'
            for l_1_ethernet_interface in (undefined(name='flexencap_interfaces') if l_0_flexencap_interfaces is missing else l_0_flexencap_interfaces):
                l_1_client_inner_encapsulation = resolve('client_inner_encapsulation')
                l_1_client_vlan = resolve('client_vlan')
                l_1_client_outer_vlan = resolve('client_outer_vlan')
                l_1_client_inner_vlan = resolve('client_inner_vlan')
                l_1_network_inner_encapsulation = resolve('network_inner_encapsulation')
                l_1_network_vlan = resolve('network_vlan')
                l_1_network_outer_vlan = resolve('network_outer_vlan')
                l_1_network_inner_vlan = resolve('network_inner_vlan')
                l_1_description = l_1_vlan_id = l_1_client_encapsulation = l_1_network_encapsulation = missing
                _loop_vars = {}
                pass
                l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                _loop_vars['description'] = l_1_description
                l_1_vlan_id = t_1(environment.getattr(l_1_ethernet_interface, 'vlan_id'), '-')
                _loop_vars['vlan_id'] = l_1_vlan_id
                l_1_client_encapsulation = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'encapsulation'), '-')
                _loop_vars['client_encapsulation'] = l_1_client_encapsulation
                if ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) == '-'):
                    pass
                    if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q')):
                        pass
                        l_1_client_encapsulation = 'dot1q'
                        _loop_vars['client_encapsulation'] = l_1_client_encapsulation
                    elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'unmatched'), True):
                        pass
                        l_1_client_encapsulation = 'unmatched'
                        _loop_vars['client_encapsulation'] = l_1_client_encapsulation
                if ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) in ['dot1q', 'dot1ad']):
                    pass
                    l_1_client_inner_encapsulation = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_encapsulation'), '-')
                    _loop_vars['client_inner_encapsulation'] = l_1_client_inner_encapsulation
                    l_1_client_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'vlan'))
                    _loop_vars['client_vlan'] = l_1_client_vlan
                    l_1_client_outer_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'outer_vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'outer'))
                    _loop_vars['client_outer_vlan'] = l_1_client_outer_vlan
                    l_1_client_inner_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'inner'))
                    _loop_vars['client_inner_vlan'] = l_1_client_inner_vlan
                l_1_network_encapsulation = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'encapsulation'), '-')
                _loop_vars['network_encapsulation'] = l_1_network_encapsulation
                if ((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation) == '-'):
                    pass
                    if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q')):
                        pass
                        l_1_network_encapsulation = 'dot1q'
                        _loop_vars['network_encapsulation'] = l_1_network_encapsulation
                    elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'client'), True):
                        pass
                        l_1_network_encapsulation = 'client'
                        _loop_vars['network_encapsulation'] = l_1_network_encapsulation
                if ((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation) in ['dot1q', 'dot1ad']):
                    pass
                    l_1_network_inner_encapsulation = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_encapsulation'), '-')
                    _loop_vars['network_inner_encapsulation'] = l_1_network_inner_encapsulation
                    l_1_network_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'vlan'))
                    _loop_vars['network_vlan'] = l_1_network_vlan
                    l_1_network_outer_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'outer_vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'outer'))
                    _loop_vars['network_outer_vlan'] = l_1_network_outer_vlan
                    l_1_network_inner_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_vlan'), environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'inner'))
                    _loop_vars['network_inner_vlan'] = l_1_network_inner_vlan
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                yield ' | '
                yield str((undefined(name='vlan_id') if l_1_vlan_id is missing else l_1_vlan_id))
                yield ' | '
                yield str((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation))
                yield ' | '
                yield str(t_1((undefined(name='client_inner_encapsulation') if l_1_client_inner_encapsulation is missing else l_1_client_inner_encapsulation), '-'))
                yield ' | '
                yield str(t_1((undefined(name='client_vlan') if l_1_client_vlan is missing else l_1_client_vlan), '-'))
                yield ' | '
                yield str(t_1((undefined(name='client_outer_vlan') if l_1_client_outer_vlan is missing else l_1_client_outer_vlan), '-'))
                yield ' | '
                yield str(t_1((undefined(name='client_inner_vlan') if l_1_client_inner_vlan is missing else l_1_client_inner_vlan), '-'))
                yield ' | '
                yield str((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation))
                yield ' | '
                yield str(t_1((undefined(name='network_inner_encapsulation') if l_1_network_inner_encapsulation is missing else l_1_network_inner_encapsulation), '-'))
                yield ' | '
                yield str(t_1((undefined(name='network_vlan') if l_1_network_vlan is missing else l_1_network_vlan), '-'))
                yield ' | '
                yield str(t_1((undefined(name='network_outer_vlan') if l_1_network_outer_vlan is missing else l_1_network_outer_vlan), '-'))
                yield ' | '
                yield str(t_1((undefined(name='network_inner_vlan') if l_1_network_inner_vlan is missing else l_1_network_inner_vlan), '-'))
                yield ' |\n'
            l_1_ethernet_interface = l_1_description = l_1_vlan_id = l_1_client_encapsulation = l_1_client_inner_encapsulation = l_1_client_vlan = l_1_client_outer_vlan = l_1_client_inner_vlan = l_1_network_encapsulation = l_1_network_inner_encapsulation = l_1_network_vlan = l_1_network_outer_vlan = l_1_network_inner_vlan = missing
        l_0_ethernet_interface_pvlan = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['ethernet_interface_pvlan'] = l_0_ethernet_interface_pvlan
        context.exported_vars.add('ethernet_interface_pvlan')
        if not isinstance(l_0_ethernet_interface_pvlan, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_ethernet_interface_pvlan['configured'] = False
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (((t_12(environment.getattr(l_1_ethernet_interface, 'pvlan_mapping')) or t_12(environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'))) or t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'pvlan_mapping'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'private_vlan_secondary'))):
                pass
                if not isinstance(l_0_ethernet_interface_pvlan, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_ethernet_interface_pvlan['configured'] = True
                break
        l_1_ethernet_interface = missing
        if (environment.getattr((undefined(name='ethernet_interface_pvlan') if l_0_ethernet_interface_pvlan is missing else l_0_ethernet_interface_pvlan), 'configured') == True):
            pass
            yield '\n##### Private VLAN\n\n| Interface | PVLAN Mapping | Secondary Trunk |\n| --------- | ------------- | ----------------|\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                l_1_row_pvlan_mapping = l_1_row_trunk_private_vlan_secondary = missing
                _loop_vars = {}
                pass
                l_1_row_pvlan_mapping = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'pvlan_mapping'), environment.getattr(l_1_ethernet_interface, 'pvlan_mapping'), '-')
                _loop_vars['row_pvlan_mapping'] = l_1_row_pvlan_mapping
                l_1_row_trunk_private_vlan_secondary = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'private_vlan_secondary'), environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'), '-')
                _loop_vars['row_trunk_private_vlan_secondary'] = l_1_row_trunk_private_vlan_secondary
                if (((undefined(name='row_pvlan_mapping') if l_1_row_pvlan_mapping is missing else l_1_row_pvlan_mapping) != '-') or ((undefined(name='row_trunk_private_vlan_secondary') if l_1_row_trunk_private_vlan_secondary is missing else l_1_row_trunk_private_vlan_secondary) != '-')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='row_pvlan_mapping') if l_1_row_pvlan_mapping is missing else l_1_row_pvlan_mapping))
                    yield ' | '
                    yield str((undefined(name='row_trunk_private_vlan_secondary') if l_1_row_trunk_private_vlan_secondary is missing else l_1_row_trunk_private_vlan_secondary))
                    yield ' |\n'
            l_1_ethernet_interface = l_1_row_pvlan_mapping = l_1_row_trunk_private_vlan_secondary = missing
        l_0_ethernet_interface_vlan_xlate = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['ethernet_interface_vlan_xlate'] = l_0_ethernet_interface_vlan_xlate
        context.exported_vars.add('ethernet_interface_vlan_xlate')
        if not isinstance(l_0_ethernet_interface_vlan_xlate, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_ethernet_interface_vlan_xlate['configured'] = False
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations')) or t_12(environment.getattr(l_1_ethernet_interface, 'vlan_translations'))):
                pass
                if not isinstance(l_0_ethernet_interface_vlan_xlate, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_ethernet_interface_vlan_xlate['configured'] = True
                break
        l_1_ethernet_interface = missing
        if (environment.getattr((undefined(name='ethernet_interface_vlan_xlate') if l_0_ethernet_interface_vlan_xlate is missing else l_0_ethernet_interface_vlan_xlate), 'configured') == True):
            pass
            yield '\n##### VLAN Translations\n\n| Interface | Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |\n| --------- | --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations')):
                    pass
                    for l_2_vlan_translation in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_both'), 'from'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | both | '
                        yield str(environment.getattr(l_2_vlan_translation, 'from'))
                        yield ' | '
                        yield str(environment.getattr(l_2_vlan_translation, 'to'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'inner_vlan_from'), '-'))
                        yield ' | - | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'network'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel'), '-'))
                        yield ' |\n'
                    l_2_vlan_translation = missing
                    for l_2_vlan_translation in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_in'), 'from'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | in | '
                        yield str(environment.getattr(l_2_vlan_translation, 'from'))
                        yield ' | '
                        yield str(environment.getattr(l_2_vlan_translation, 'to'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'inner_vlan_from'), '-'))
                        yield ' | - | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'network'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel'), '-'))
                        yield ' |\n'
                    l_2_vlan_translation = missing
                    for l_2_vlan_translation in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_out'), 'from'):
                        l_2_dot1q_tunnel = resolve('dot1q_tunnel')
                        l_2_to_vlan_id = resolve('to_vlan_id')
                        _loop_vars = {}
                        pass
                        if t_12(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel_to')):
                            pass
                            l_2_dot1q_tunnel = 'True'
                            _loop_vars['dot1q_tunnel'] = l_2_dot1q_tunnel
                            l_2_to_vlan_id = environment.getattr(l_2_vlan_translation, 'dot1q_tunnel_to')
                            _loop_vars['to_vlan_id'] = l_2_to_vlan_id
                        else:
                            pass
                            l_2_to_vlan_id = t_1(environment.getattr(l_2_vlan_translation, 'to'), '-')
                            _loop_vars['to_vlan_id'] = l_2_to_vlan_id
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | out | '
                        yield str(environment.getattr(l_2_vlan_translation, 'from'))
                        yield ' | '
                        yield str((undefined(name='to_vlan_id') if l_2_to_vlan_id is missing else l_2_to_vlan_id))
                        yield ' | - | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'inner_vlan_to'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_vlan_translation, 'network'), '-'))
                        yield ' | '
                        yield str(t_1((undefined(name='dot1q_tunnel') if l_2_dot1q_tunnel is missing else l_2_dot1q_tunnel), '-'))
                        yield ' |\n'
                    l_2_vlan_translation = l_2_dot1q_tunnel = l_2_to_vlan_id = missing
                elif t_12(environment.getattr(l_1_ethernet_interface, 'vlan_translations')):
                    pass
                    for l_2_vlan_translation in t_3(environment.getattr(l_1_ethernet_interface, 'vlan_translations')):
                        l_2_row_direction = resolve('row_direction')
                        _loop_vars = {}
                        pass
                        if (t_12(environment.getattr(l_2_vlan_translation, 'from')) and t_12(environment.getattr(l_2_vlan_translation, 'to'))):
                            pass
                            l_2_row_direction = t_1(environment.getattr(l_2_vlan_translation, 'direction'), 'both')
                            _loop_vars['row_direction'] = l_2_row_direction
                            yield '| '
                            yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                            yield ' | '
                            yield str((undefined(name='row_direction') if l_2_row_direction is missing else l_2_row_direction))
                            yield ' | '
                            yield str(environment.getattr(l_2_vlan_translation, 'from'))
                            yield ' | '
                            yield str(environment.getattr(l_2_vlan_translation, 'to'))
                            yield ' | - | - | - | - |\n'
                    l_2_vlan_translation = l_2_row_direction = missing
            l_1_ethernet_interface = missing
        l_0_tcp_mss_clampings = []
        context.vars['tcp_mss_clampings'] = l_0_tcp_mss_clampings
        context.exported_vars.add('tcp_mss_clampings')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling')):
                pass
                context.call(environment.getattr((undefined(name='tcp_mss_clampings') if l_0_tcp_mss_clampings is missing else l_0_tcp_mss_clampings), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='tcp_mss_clampings') if l_0_tcp_mss_clampings is missing else l_0_tcp_mss_clampings)) > 0):
            pass
            yield '\n##### TCP MSS Clamping\n\n| Interface | Ipv4 Segment Size | Ipv6 Segment Size | Direction |\n| --------- | ----------------- | ----------------- | --------- |\n'
            for l_1_tcp_mss_clamping in t_3((undefined(name='tcp_mss_clampings') if l_0_tcp_mss_clampings is missing else l_0_tcp_mss_clampings), 'name'):
                l_1_ipv4_segment_size = resolve('ipv4_segment_size')
                l_1_ipv6_segment_size = resolve('ipv6_segment_size')
                l_1_interface = missing
                _loop_vars = {}
                pass
                l_1_interface = environment.getattr(l_1_tcp_mss_clamping, 'name')
                _loop_vars['interface'] = l_1_interface
                if t_12(environment.getattr(environment.getattr(l_1_tcp_mss_clamping, 'tcp_mss_ceiling'), 'ipv4_segment_size')):
                    pass
                    l_1_ipv4_segment_size = environment.getattr(environment.getattr(l_1_tcp_mss_clamping, 'tcp_mss_ceiling'), 'ipv4_segment_size')
                    _loop_vars['ipv4_segment_size'] = l_1_ipv4_segment_size
                if t_12(environment.getattr(environment.getattr(l_1_tcp_mss_clamping, 'tcp_mss_ceiling'), 'ipv6_segment_size')):
                    pass
                    l_1_ipv6_segment_size = environment.getattr(environment.getattr(l_1_tcp_mss_clamping, 'tcp_mss_ceiling'), 'ipv6_segment_size')
                    _loop_vars['ipv6_segment_size'] = l_1_ipv6_segment_size
                yield '| '
                yield str((undefined(name='interface') if l_1_interface is missing else l_1_interface))
                yield ' | '
                yield str(t_1((undefined(name='ipv4_segment_size') if l_1_ipv4_segment_size is missing else l_1_ipv4_segment_size), '-'))
                yield ' | '
                yield str(t_1((undefined(name='ipv6_segment_size') if l_1_ipv6_segment_size is missing else l_1_ipv6_segment_size), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_tcp_mss_clamping, 'tcp_mss_ceiling'), 'direction'), '-'))
                yield ' |\n'
            l_1_tcp_mss_clamping = l_1_interface = l_1_ipv4_segment_size = l_1_ipv6_segment_size = missing
        l_0_transceiver_settings = []
        context.vars['transceiver_settings'] = l_0_transceiver_settings
        context.exported_vars.add('transceiver_settings')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'transceiver')):
                pass
                context.call(environment.getattr((undefined(name='transceiver_settings') if l_0_transceiver_settings is missing else l_0_transceiver_settings), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='transceiver_settings') if l_0_transceiver_settings is missing else l_0_transceiver_settings)) > 0):
            pass
            yield '\n##### Transceiver Settings\n\n| Interface | Transceiver Frequency | Media Override |\n| --------- | --------------------- | -------------- |\n'
            for l_1_transceiver_setting in t_3((undefined(name='transceiver_settings') if l_0_transceiver_settings is missing else l_0_transceiver_settings), 'name'):
                l_1_frequency = resolve('frequency')
                l_1_interface = l_1_m_override = missing
                _loop_vars = {}
                pass
                l_1_interface = environment.getattr(l_1_transceiver_setting, 'name')
                _loop_vars['interface'] = l_1_interface
                if t_12(environment.getattr(environment.getattr(l_1_transceiver_setting, 'transceiver'), 'frequency')):
                    pass
                    l_1_frequency = t_7('%.3f', t_6(environment.getattr(environment.getattr(l_1_transceiver_setting, 'transceiver'), 'frequency')))
                    _loop_vars['frequency'] = l_1_frequency
                    if t_12(environment.getattr(environment.getattr(l_1_transceiver_setting, 'transceiver'), 'frequency_unit')):
                        pass
                        l_1_frequency = str_join(((undefined(name='frequency') if l_1_frequency is missing else l_1_frequency), ' ', environment.getattr(environment.getattr(l_1_transceiver_setting, 'transceiver'), 'frequency_unit'), ))
                        _loop_vars['frequency'] = l_1_frequency
                else:
                    pass
                    l_1_frequency = '-'
                    _loop_vars['frequency'] = l_1_frequency
                l_1_m_override = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_transceiver_setting, 'transceiver'), 'media'), 'override'), '-')
                _loop_vars['m_override'] = l_1_m_override
                yield '| '
                yield str((undefined(name='interface') if l_1_interface is missing else l_1_interface))
                yield ' | '
                yield str((undefined(name='frequency') if l_1_frequency is missing else l_1_frequency))
                yield ' | '
                yield str((undefined(name='m_override') if l_1_m_override is missing else l_1_m_override))
                yield ' |\n'
            l_1_transceiver_setting = l_1_interface = l_1_frequency = l_1_m_override = missing
        l_0_link_tracking_interfaces = []
        context.vars['link_tracking_interfaces'] = l_0_link_tracking_interfaces
        context.exported_vars.add('link_tracking_interfaces')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'link_tracking_groups')):
                pass
                context.call(environment.getattr((undefined(name='link_tracking_interfaces') if l_0_link_tracking_interfaces is missing else l_0_link_tracking_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='link_tracking_interfaces') if l_0_link_tracking_interfaces is missing else l_0_link_tracking_interfaces)) > 0):
            pass
            yield '\n##### Link Tracking Groups\n\n| Interface | Group Name | Direction |\n| --------- | ---------- | --------- |\n'
            for l_1_link_tracking_interface in (undefined(name='link_tracking_interfaces') if l_0_link_tracking_interfaces is missing else l_0_link_tracking_interfaces):
                _loop_vars = {}
                pass
                for l_2_link_tracking_group in t_3(environment.getattr(l_1_link_tracking_interface, 'link_tracking_groups'), 'name'):
                    _loop_vars = {}
                    pass
                    if (t_12(environment.getattr(l_2_link_tracking_group, 'name')) and t_12(environment.getattr(l_2_link_tracking_group, 'direction'))):
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_link_tracking_interface, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_link_tracking_group, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_link_tracking_group, 'direction'))
                        yield ' |\n'
                l_2_link_tracking_group = missing
                if (t_12(environment.getattr(environment.getattr(l_1_link_tracking_interface, 'link_tracking'), 'direction')) and t_12(environment.getattr(environment.getattr(l_1_link_tracking_interface, 'link_tracking'), 'groups'))):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_link_tracking_interface, 'name'))
                    yield ' | '
                    yield str(t_8(context.eval_ctx, environment.getattr(environment.getattr(l_1_link_tracking_interface, 'link_tracking'), 'groups'), ', '))
                    yield ' | '
                    yield str(environment.getattr(environment.getattr(l_1_link_tracking_interface, 'link_tracking'), 'direction'))
                    yield ' |\n'
            l_1_link_tracking_interface = missing
        l_0_phone_interfaces = []
        context.vars['phone_interfaces'] = l_0_phone_interfaces
        context.exported_vars.add('phone_interfaces')
        for l_1_interface in (t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name') + t_3((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name')):
            _loop_vars = {}
            pass
            if (t_12(environment.getattr(environment.getattr(l_1_interface, 'switchport'), 'phone')) or t_12(environment.getattr(l_1_interface, 'phone'))):
                pass
                context.call(environment.getattr((undefined(name='phone_interfaces') if l_0_phone_interfaces is missing else l_0_phone_interfaces), 'append'), l_1_interface, _loop_vars=_loop_vars)
        l_1_interface = missing
        if (t_9((undefined(name='phone_interfaces') if l_0_phone_interfaces is missing else l_0_phone_interfaces)) > 0):
            pass
            yield '\n##### Phone Interfaces\n\n| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |\n| --------- | ---- | ----------- | ---------- | --------------- |\n'
            for l_1_phone_interface in (undefined(name='phone_interfaces') if l_0_phone_interfaces is missing else l_0_phone_interfaces):
                l_1_mode = l_1_native_vlan = l_1_phone_vlan = l_1_phone_vlan_mode = missing
                _loop_vars = {}
                pass
                l_1_mode = t_1(environment.getattr(environment.getattr(l_1_phone_interface, 'switchport'), 'mode'), environment.getattr(l_1_phone_interface, 'mode'), '-')
                _loop_vars['mode'] = l_1_mode
                l_1_native_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_phone_interface, 'switchport'), 'trunk'), 'native_vlan'), environment.getattr(l_1_phone_interface, 'native_vlan'), '-')
                _loop_vars['native_vlan'] = l_1_native_vlan
                l_1_phone_vlan = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_phone_interface, 'switchport'), 'phone'), 'vlan'), environment.getattr(environment.getattr(l_1_phone_interface, 'phone'), 'vlan'), '-')
                _loop_vars['phone_vlan'] = l_1_phone_vlan
                l_1_phone_vlan_mode = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_phone_interface, 'switchport'), 'phone'), 'trunk'), environment.getattr(environment.getattr(l_1_phone_interface, 'phone'), 'trunk'), '-')
                _loop_vars['phone_vlan_mode'] = l_1_phone_vlan_mode
                yield '| '
                yield str(environment.getattr(l_1_phone_interface, 'name'))
                yield ' | '
                yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                yield ' | '
                yield str((undefined(name='native_vlan') if l_1_native_vlan is missing else l_1_native_vlan))
                yield ' | '
                yield str((undefined(name='phone_vlan') if l_1_phone_vlan is missing else l_1_phone_vlan))
                yield ' | '
                yield str((undefined(name='phone_vlan_mode') if l_1_phone_vlan_mode is missing else l_1_phone_vlan_mode))
                yield ' |\n'
            l_1_phone_interface = l_1_mode = l_1_native_vlan = l_1_phone_vlan = l_1_phone_vlan_mode = missing
        l_0_multicast_interfaces = []
        context.vars['multicast_interfaces'] = l_0_multicast_interfaces
        context.exported_vars.add('multicast_interfaces')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'multicast')):
                pass
                context.call(environment.getattr((undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces)) > 0):
            pass
            yield '\n##### Multicast Routing\n\n| Interface | IP Version | Static Routes Allowed | Multicast Boundaries |\n| --------- | ---------- | --------------------- | -------------------- |\n'
            for l_1_multicast_interface in (undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces):
                l_1_static = resolve('static')
                l_1_boundaries = resolve('boundaries')
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4')):
                    pass
                    l_1_static = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'static'), '-')
                    _loop_vars['static'] = l_1_static
                    if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'boundaries')):
                        pass
                        l_1_boundaries = t_8(context.eval_ctx, t_10(context, t_11(context, environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'boundaries'), 'boundary', 'arista.avd.defined'), attribute='boundary'), ', ')
                        _loop_vars['boundaries'] = l_1_boundaries
                    else:
                        pass
                        l_1_boundaries = '-'
                        _loop_vars['boundaries'] = l_1_boundaries
                    yield '| '
                    yield str(environment.getattr(l_1_multicast_interface, 'name'))
                    yield ' | IPv4 | '
                    yield str((undefined(name='static') if l_1_static is missing else l_1_static))
                    yield ' | '
                    yield str((undefined(name='boundaries') if l_1_boundaries is missing else l_1_boundaries))
                    yield ' |\n'
                if t_12(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6')):
                    pass
                    l_1_static = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'static'), '-')
                    _loop_vars['static'] = l_1_static
                    if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'boundaries')):
                        pass
                        l_1_boundaries = t_8(context.eval_ctx, t_10(context, t_11(context, environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'boundaries'), 'boundary', 'arista.avd.defined'), attribute='boundary'), ', ')
                        _loop_vars['boundaries'] = l_1_boundaries
                    else:
                        pass
                        l_1_boundaries = '-'
                        _loop_vars['boundaries'] = l_1_boundaries
                    yield '| '
                    yield str(environment.getattr(l_1_multicast_interface, 'name'))
                    yield ' | IPv6 | '
                    yield str((undefined(name='static') if l_1_static is missing else l_1_static))
                    yield ' | '
                    yield str((undefined(name='boundaries') if l_1_boundaries is missing else l_1_boundaries))
                    yield ' |\n'
            l_1_multicast_interface = l_1_static = l_1_boundaries = missing
        l_0_ethernet_interface_ipv4 = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['ethernet_interface_ipv4'] = l_0_ethernet_interface_ipv4
        context.exported_vars.add('ethernet_interface_ipv4')
        if not isinstance(l_0_ethernet_interface_ipv4, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_ethernet_interface_ipv4['configured'] = False
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'ip_address')):
                pass
                if not isinstance(l_0_ethernet_interface_ipv4, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_ethernet_interface_ipv4['configured'] = True
                break
        l_1_ethernet_interface = missing
        l_0_port_channel_interface_ipv4 = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['port_channel_interface_ipv4'] = l_0_port_channel_interface_ipv4
        context.exported_vars.add('port_channel_interface_ipv4')
        if not isinstance(l_0_port_channel_interface_ipv4, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_port_channel_interface_ipv4['configured'] = False
        for l_1_port_channel_interface in t_3((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_port_channel_interface, 'ip_address')):
                pass
                if not isinstance(l_0_port_channel_interface_ipv4, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_port_channel_interface_ipv4['configured'] = True
                break
        l_1_port_channel_interface = missing
        if ((environment.getattr((undefined(name='ethernet_interface_ipv4') if l_0_ethernet_interface_ipv4 is missing else l_0_ethernet_interface_ipv4), 'configured') == True) or (environment.getattr((undefined(name='port_channel_interface_ipv4') if l_0_port_channel_interface_ipv4 is missing else l_0_port_channel_interface_ipv4), 'configured') == True)):
            pass
            yield '\n##### IPv4\n\n| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |\n| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                l_1_port_channel_interface_name = resolve('port_channel_interface_name')
                l_1_port_channel_interface = resolve('port_channel_interface')
                l_1_description = resolve('description')
                l_1_channel_group = resolve('channel_group')
                l_1_ip_address = resolve('ip_address')
                l_1_vrf = resolve('vrf')
                l_1_mtu = resolve('mtu')
                l_1_shutdown = resolve('shutdown')
                l_1_acl_in = resolve('acl_in')
                l_1_acl_out = resolve('acl_out')
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')):
                    pass
                    l_1_port_channel_interface_name = str_join(('Port-Channel', environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), ))
                    _loop_vars['port_channel_interface_name'] = l_1_port_channel_interface_name
                    l_1_port_channel_interface = t_5(environment, t_11(context, t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), []), 'name', 'arista.avd.defined', (undefined(name='port_channel_interface_name') if l_1_port_channel_interface_name is missing else l_1_port_channel_interface_name)))
                    _loop_vars['port_channel_interface'] = l_1_port_channel_interface
                    if t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ip_address')):
                        pass
                        l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                        _loop_vars['description'] = l_1_description
                        l_1_channel_group = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), '-')
                        _loop_vars['channel_group'] = l_1_channel_group
                        l_1_ip_address = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ip_address'), '-')
                        _loop_vars['ip_address'] = l_1_ip_address
                        l_1_vrf = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'vrf'), '*default')
                        _loop_vars['vrf'] = l_1_vrf
                        l_1_mtu = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'mtu'), '*-')
                        _loop_vars['mtu'] = l_1_mtu
                        l_1_shutdown = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'shutdown'), '*-')
                        _loop_vars['shutdown'] = l_1_shutdown
                        l_1_acl_in = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'access_group_in'), '*-')
                        _loop_vars['acl_in'] = l_1_acl_in
                        l_1_acl_out = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'access_group_out'), '*-')
                        _loop_vars['acl_out'] = l_1_acl_out
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                        yield ' | '
                        yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                        yield ' | *'
                        yield str((undefined(name='ip_address') if l_1_ip_address is missing else l_1_ip_address))
                        yield ' | *'
                        yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
                        yield ' | *'
                        yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
                        yield ' | *'
                        yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
                        yield ' | *'
                        yield str((undefined(name='acl_in') if l_1_acl_in is missing else l_1_acl_in))
                        yield ' | *'
                        yield str((undefined(name='acl_out') if l_1_acl_out is missing else l_1_acl_out))
                        yield ' |\n'
                else:
                    pass
                    if t_12(environment.getattr(l_1_ethernet_interface, 'ip_address')):
                        pass
                        l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                        _loop_vars['description'] = l_1_description
                        l_1_ip_address = t_1(environment.getattr(l_1_ethernet_interface, 'ip_address'), '-')
                        _loop_vars['ip_address'] = l_1_ip_address
                        l_1_vrf = t_1(environment.getattr(l_1_ethernet_interface, 'vrf'), 'default')
                        _loop_vars['vrf'] = l_1_vrf
                        l_1_mtu = t_1(environment.getattr(l_1_ethernet_interface, 'mtu'), '-')
                        _loop_vars['mtu'] = l_1_mtu
                        l_1_shutdown = t_1(environment.getattr(l_1_ethernet_interface, 'shutdown'), '-')
                        _loop_vars['shutdown'] = l_1_shutdown
                        l_1_acl_in = t_1(environment.getattr(l_1_ethernet_interface, 'access_group_in'), '-')
                        _loop_vars['acl_in'] = l_1_acl_in
                        l_1_acl_out = t_1(environment.getattr(l_1_ethernet_interface, 'access_group_out'), '-')
                        _loop_vars['acl_out'] = l_1_acl_out
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                        yield ' | - | '
                        yield str((undefined(name='ip_address') if l_1_ip_address is missing else l_1_ip_address))
                        yield ' | '
                        yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
                        yield ' | '
                        yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
                        yield ' | '
                        yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
                        yield ' | '
                        yield str((undefined(name='acl_in') if l_1_acl_in is missing else l_1_acl_in))
                        yield ' | '
                        yield str((undefined(name='acl_out') if l_1_acl_out is missing else l_1_acl_out))
                        yield ' |\n'
            l_1_ethernet_interface = l_1_port_channel_interface_name = l_1_port_channel_interface = l_1_description = l_1_channel_group = l_1_ip_address = l_1_vrf = l_1_mtu = l_1_shutdown = l_1_acl_in = l_1_acl_out = missing
        if (environment.getattr((undefined(name='port_channel_interface_ipv4') if l_0_port_channel_interface_ipv4 is missing else l_0_port_channel_interface_ipv4), 'configured') == True):
            pass
            yield '\n*Inherited from Port-Channel Interface\n'
        l_0_ip_nat_interfaces = (undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces)
        context.vars['ip_nat_interfaces'] = l_0_ip_nat_interfaces
        context.exported_vars.add('ip_nat_interfaces')
        template = environment.get_template('documentation/interfaces-ip-nat.j2', 'documentation/ethernet-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'encapsulation_dot1q_interfaces': l_0_encapsulation_dot1q_interfaces, 'err_cor_enc_intfs': l_0_err_cor_enc_intfs, 'ethernet_interface_ipv4': l_0_ethernet_interface_ipv4, 'ethernet_interface_ipv6': l_0_ethernet_interface_ipv6, 'ethernet_interface_pvlan': l_0_ethernet_interface_pvlan, 'ethernet_interface_vlan_xlate': l_0_ethernet_interface_vlan_xlate, 'ethernet_interfaces_isis': l_0_ethernet_interfaces_isis, 'ethernet_interfaces_vrrp_details': l_0_ethernet_interfaces_vrrp_details, 'evpn_dfe_ethernet_interfaces': l_0_evpn_dfe_ethernet_interfaces, 'evpn_es_ethernet_interfaces': l_0_evpn_es_ethernet_interfaces, 'evpn_mpls_ethernet_interfaces': l_0_evpn_mpls_ethernet_interfaces, 'flexencap_interfaces': l_0_flexencap_interfaces, 'ip_nat_interfaces': l_0_ip_nat_interfaces, 'link_tracking_interfaces': l_0_link_tracking_interfaces, 'multicast_interfaces': l_0_multicast_interfaces, 'phone_interfaces': l_0_phone_interfaces, 'port_channel_interface_ipv4': l_0_port_channel_interface_ipv4, 'port_channel_interface_ipv6': l_0_port_channel_interface_ipv6, 'port_channel_interfaces_isis': l_0_port_channel_interfaces_isis, 'priority_intfs': l_0_priority_intfs, 'sync_e_interfaces': l_0_sync_e_interfaces, 'tcp_mss_clampings': l_0_tcp_mss_clampings, 'transceiver_settings': l_0_transceiver_settings})):
            yield event
        l_0_ethernet_interface_ipv6 = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['ethernet_interface_ipv6'] = l_0_ethernet_interface_ipv6
        context.exported_vars.add('ethernet_interface_ipv6')
        if not isinstance(l_0_ethernet_interface_ipv6, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_ethernet_interface_ipv6['configured'] = False
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_12(environment.getattr(l_1_ethernet_interface, 'ipv6_address')) or t_12(environment.getattr(l_1_ethernet_interface, 'ipv6_enable'), True)):
                pass
                if not isinstance(l_0_ethernet_interface_ipv6, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_ethernet_interface_ipv6['configured'] = True
                break
        l_1_ethernet_interface = missing
        l_0_port_channel_interface_ipv6 = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['port_channel_interface_ipv6'] = l_0_port_channel_interface_ipv6
        context.exported_vars.add('port_channel_interface_ipv6')
        if not isinstance(l_0_port_channel_interface_ipv6, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_port_channel_interface_ipv6['configured'] = False
        for l_1_port_channel_interface in t_3((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
            _loop_vars = {}
            pass
            if (t_12(environment.getattr(l_1_port_channel_interface, 'ipv6_address')) or t_12(environment.getattr(l_1_port_channel_interface, 'ipv6_enable'), True)):
                pass
                if not isinstance(l_0_port_channel_interface_ipv6, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_port_channel_interface_ipv6['configured'] = True
                break
        l_1_port_channel_interface = missing
        if ((environment.getattr((undefined(name='ethernet_interface_ipv6') if l_0_ethernet_interface_ipv6 is missing else l_0_ethernet_interface_ipv6), 'configured') == True) or (environment.getattr((undefined(name='port_channel_interface_ipv6') if l_0_port_channel_interface_ipv6 is missing else l_0_port_channel_interface_ipv6), 'configured') == True)):
            pass
            yield '\n##### IPv6\n\n| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |\n| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                l_1_port_channel_interface_name = resolve('port_channel_interface_name')
                l_1_port_channel_interface = resolve('port_channel_interface')
                l_1_description = resolve('description')
                l_1_channel_group = resolve('channel_group')
                l_1_ipv6_address = resolve('ipv6_address')
                l_1_vrf = resolve('vrf')
                l_1_mtu = resolve('mtu')
                l_1_shutdown = resolve('shutdown')
                l_1_nd_ra_disabled = resolve('nd_ra_disabled')
                l_1_managed_config_flag = resolve('managed_config_flag')
                l_1_ipv6_acl_in = resolve('ipv6_acl_in')
                l_1_ipv6_acl_out = resolve('ipv6_acl_out')
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')):
                    pass
                    l_1_port_channel_interface_name = str_join(('Port-Channel', environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), ))
                    _loop_vars['port_channel_interface_name'] = l_1_port_channel_interface_name
                    l_1_port_channel_interface = t_5(environment, t_11(context, t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), []), 'name', 'arista.avd.defined', (undefined(name='port_channel_interface_name') if l_1_port_channel_interface_name is missing else l_1_port_channel_interface_name)))
                    _loop_vars['port_channel_interface'] = l_1_port_channel_interface
                    if (t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_address')) or t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_enable'), True)):
                        pass
                        l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                        _loop_vars['description'] = l_1_description
                        l_1_channel_group = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), '-')
                        _loop_vars['channel_group'] = l_1_channel_group
                        l_1_ipv6_address = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_address'), '-')
                        _loop_vars['ipv6_address'] = l_1_ipv6_address
                        l_1_vrf = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'vrf'), 'default')
                        _loop_vars['vrf'] = l_1_vrf
                        l_1_mtu = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'mtu'), '-')
                        _loop_vars['mtu'] = l_1_mtu
                        l_1_shutdown = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'shutdown'), '-')
                        _loop_vars['shutdown'] = l_1_shutdown
                        l_1_nd_ra_disabled = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_nd_ra_disabled'), '-')
                        _loop_vars['nd_ra_disabled'] = l_1_nd_ra_disabled
                        l_1_managed_config_flag = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_nd_managed_config_flag'), '-')
                        _loop_vars['managed_config_flag'] = l_1_managed_config_flag
                        l_1_ipv6_acl_in = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_access_group_in'), '-')
                        _loop_vars['ipv6_acl_in'] = l_1_ipv6_acl_in
                        l_1_ipv6_acl_out = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'ipv6_access_group_out'), '-')
                        _loop_vars['ipv6_acl_out'] = l_1_ipv6_acl_out
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                        yield ' | '
                        yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                        yield ' | *'
                        yield str((undefined(name='ipv6_address') if l_1_ipv6_address is missing else l_1_ipv6_address))
                        yield ' | *'
                        yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
                        yield ' | *'
                        yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
                        yield ' | *'
                        yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
                        yield ' | *'
                        yield str((undefined(name='nd_ra_disabled') if l_1_nd_ra_disabled is missing else l_1_nd_ra_disabled))
                        yield ' | *'
                        yield str((undefined(name='managed_config_flag') if l_1_managed_config_flag is missing else l_1_managed_config_flag))
                        yield ' | *'
                        yield str((undefined(name='ipv6_acl_in') if l_1_ipv6_acl_in is missing else l_1_ipv6_acl_in))
                        yield ' | *'
                        yield str((undefined(name='ipv6_acl_out') if l_1_ipv6_acl_out is missing else l_1_ipv6_acl_out))
                        yield ' |\n'
                else:
                    pass
                    if (t_12(environment.getattr(l_1_ethernet_interface, 'ipv6_address')) or t_12(environment.getattr(l_1_ethernet_interface, 'ipv6_enable'), True)):
                        pass
                        l_1_description = t_1(environment.getattr(l_1_ethernet_interface, 'description'), '-')
                        _loop_vars['description'] = l_1_description
                        l_1_ipv6_address = t_1(environment.getattr(l_1_ethernet_interface, 'ipv6_address'), '-')
                        _loop_vars['ipv6_address'] = l_1_ipv6_address
                        l_1_vrf = t_1(environment.getattr(l_1_ethernet_interface, 'vrf'), 'default')
                        _loop_vars['vrf'] = l_1_vrf
                        l_1_mtu = t_1(environment.getattr(l_1_ethernet_interface, 'mtu'), '-')
                        _loop_vars['mtu'] = l_1_mtu
                        l_1_shutdown = t_1(environment.getattr(l_1_ethernet_interface, 'shutdown'), '-')
                        _loop_vars['shutdown'] = l_1_shutdown
                        l_1_nd_ra_disabled = t_1(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_ra_disabled'), '-')
                        _loop_vars['nd_ra_disabled'] = l_1_nd_ra_disabled
                        l_1_managed_config_flag = t_1(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_managed_config_flag'), '-')
                        _loop_vars['managed_config_flag'] = l_1_managed_config_flag
                        l_1_ipv6_acl_in = t_1(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_in'), '-')
                        _loop_vars['ipv6_acl_in'] = l_1_ipv6_acl_in
                        l_1_ipv6_acl_out = t_1(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_out'), '-')
                        _loop_vars['ipv6_acl_out'] = l_1_ipv6_acl_out
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='description') if l_1_description is missing else l_1_description))
                        yield ' | - | '
                        yield str((undefined(name='ipv6_address') if l_1_ipv6_address is missing else l_1_ipv6_address))
                        yield ' | '
                        yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
                        yield ' | '
                        yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
                        yield ' | '
                        yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
                        yield ' | '
                        yield str((undefined(name='nd_ra_disabled') if l_1_nd_ra_disabled is missing else l_1_nd_ra_disabled))
                        yield ' | '
                        yield str((undefined(name='managed_config_flag') if l_1_managed_config_flag is missing else l_1_managed_config_flag))
                        yield ' | '
                        yield str((undefined(name='ipv6_acl_in') if l_1_ipv6_acl_in is missing else l_1_ipv6_acl_in))
                        yield ' | '
                        yield str((undefined(name='ipv6_acl_out') if l_1_ipv6_acl_out is missing else l_1_ipv6_acl_out))
                        yield ' |\n'
            l_1_ethernet_interface = l_1_port_channel_interface_name = l_1_port_channel_interface = l_1_description = l_1_channel_group = l_1_ipv6_address = l_1_vrf = l_1_mtu = l_1_shutdown = l_1_nd_ra_disabled = l_1_managed_config_flag = l_1_ipv6_acl_in = l_1_ipv6_acl_out = missing
        if (environment.getattr((undefined(name='port_channel_interface_ipv6') if l_0_port_channel_interface_ipv6 is missing else l_0_port_channel_interface_ipv6), 'configured') == True):
            pass
            yield '\n*Inherited from Port-Channel Interface\n'
        l_0_ethernet_interfaces_isis = []
        context.vars['ethernet_interfaces_isis'] = l_0_ethernet_interfaces_isis
        context.exported_vars.add('ethernet_interfaces_isis')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if ((((((((((t_12(environment.getattr(l_1_ethernet_interface, 'isis_enable')) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_bfd'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_metric'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_network_point_to_point'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_passive'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'))) or t_12(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode'))):
                pass
                context.call(environment.getattr((undefined(name='ethernet_interfaces_isis') if l_0_ethernet_interfaces_isis is missing else l_0_ethernet_interfaces_isis), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        l_0_port_channel_interfaces_isis = []
        context.vars['port_channel_interfaces_isis'] = l_0_port_channel_interfaces_isis
        context.exported_vars.add('port_channel_interfaces_isis')
        for l_1_port_channel_interface in t_3((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
            _loop_vars = {}
            pass
            if ((((((((((t_12(environment.getattr(l_1_port_channel_interface, 'isis_enable')) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_bfd'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_metric'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_circuit_type'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_network_point_to_point'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_passive'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_hello_padding'))) or t_12(environment.getattr(l_1_port_channel_interface, 'isis_authentication_mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'isis_authentication'), 'both'), 'mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'isis_authentication'), 'level_1'), 'mode'))) or t_12(environment.getattr(environment.getattr(environment.getattr(l_1_port_channel_interface, 'isis_authentication'), 'level_2'), 'mode'))):
                pass
                context.call(environment.getattr((undefined(name='port_channel_interfaces_isis') if l_0_port_channel_interfaces_isis is missing else l_0_port_channel_interfaces_isis), 'append'), l_1_port_channel_interface, _loop_vars=_loop_vars)
        l_1_port_channel_interface = missing
        l_0_ethernet_interfaces_vrrp_details = []
        context.vars['ethernet_interfaces_vrrp_details'] = l_0_ethernet_interfaces_vrrp_details
        context.exported_vars.add('ethernet_interfaces_vrrp_details')
        for l_1_ethernet_interface in t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), []):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'vrrp_ids')):
                pass
                context.call(environment.getattr((undefined(name='ethernet_interfaces_vrrp_details') if l_0_ethernet_interfaces_vrrp_details is missing else l_0_ethernet_interfaces_vrrp_details), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='ethernet_interfaces_vrrp_details') if l_0_ethernet_interfaces_vrrp_details is missing else l_0_ethernet_interfaces_vrrp_details)) > 0):
            pass
            yield '\n##### VRRP Details\n\n| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |\n| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces_vrrp_details') if l_0_ethernet_interfaces_vrrp_details is missing else l_0_ethernet_interfaces_vrrp_details), 'name'):
                _loop_vars = {}
                pass
                def t_13(fiter):
                    for l_2_vrid in fiter:
                        if t_12(environment.getattr(l_2_vrid, 'id')):
                            yield l_2_vrid
                for l_2_vrid in t_13(environment.getattr(l_1_ethernet_interface, 'vrrp_ids')):
                    l_2_row_tracked_object_name = resolve('row_tracked_object_name')
                    l_2_row_tracked_object_action = resolve('row_tracked_object_action')
                    l_2_row_id = l_2_row_prio_level = l_2_row_ad_interval = l_2_row_preempt = l_2_row_ipv4_virt = l_2_row_ipv4_vers = l_2_row_ipv6_virt = missing
                    _loop_vars = {}
                    pass
                    l_2_row_id = environment.getattr(l_2_vrid, 'id')
                    _loop_vars['row_id'] = l_2_row_id
                    l_2_row_prio_level = t_1(environment.getattr(l_2_vrid, 'priority_level'), '-')
                    _loop_vars['row_prio_level'] = l_2_row_prio_level
                    l_2_row_ad_interval = t_1(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval'), '-')
                    _loop_vars['row_ad_interval'] = l_2_row_ad_interval
                    l_2_row_preempt = 'Enabled'
                    _loop_vars['row_preempt'] = l_2_row_preempt
                    if t_12(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), False):
                        pass
                        l_2_row_preempt = 'Disabled'
                        _loop_vars['row_preempt'] = l_2_row_preempt
                    if t_12(environment.getattr(l_2_vrid, 'tracked_object')):
                        pass
                        l_2_row_tracked_object_name = []
                        _loop_vars['row_tracked_object_name'] = l_2_row_tracked_object_name
                        l_2_row_tracked_object_action = []
                        _loop_vars['row_tracked_object_action'] = l_2_row_tracked_object_action
                        for l_3_tracked_obj in t_3(environment.getattr(l_2_vrid, 'tracked_object'), 'name'):
                            _loop_vars = {}
                            pass
                            context.call(environment.getattr((undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), 'append'), environment.getattr(l_3_tracked_obj, 'name'), _loop_vars=_loop_vars)
                            if t_12(environment.getattr(l_3_tracked_obj, 'shutdown'), True):
                                pass
                                context.call(environment.getattr((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), 'append'), 'Shutdown', _loop_vars=_loop_vars)
                            elif t_12(environment.getattr(l_3_tracked_obj, 'decrement')):
                                pass
                                context.call(environment.getattr((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), 'append'), str_join(('Decrement ', environment.getattr(l_3_tracked_obj, 'decrement'), )), _loop_vars=_loop_vars)
                        l_3_tracked_obj = missing
                        l_2_row_tracked_object_name = t_8(context.eval_ctx, (undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), ', ')
                        _loop_vars['row_tracked_object_name'] = l_2_row_tracked_object_name
                        l_2_row_tracked_object_action = t_8(context.eval_ctx, (undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), ', ')
                        _loop_vars['row_tracked_object_action'] = l_2_row_tracked_object_action
                    l_2_row_ipv4_virt = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address'), '-')
                    _loop_vars['row_ipv4_virt'] = l_2_row_ipv4_virt
                    l_2_row_ipv4_vers = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version'), '2')
                    _loop_vars['row_ipv4_vers'] = l_2_row_ipv4_vers
                    l_2_row_ipv6_virt = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address'), '-')
                    _loop_vars['row_ipv6_virt'] = l_2_row_ipv6_virt
                    yield '| '
                    yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='row_id') if l_2_row_id is missing else l_2_row_id))
                    yield ' | '
                    yield str((undefined(name='row_prio_level') if l_2_row_prio_level is missing else l_2_row_prio_level))
                    yield ' | '
                    yield str((undefined(name='row_ad_interval') if l_2_row_ad_interval is missing else l_2_row_ad_interval))
                    yield ' | '
                    yield str((undefined(name='row_preempt') if l_2_row_preempt is missing else l_2_row_preempt))
                    yield ' | '
                    yield str(t_1((undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), '-'))
                    yield ' | '
                    yield str(t_1((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), '-'))
                    yield ' | '
                    yield str((undefined(name='row_ipv4_virt') if l_2_row_ipv4_virt is missing else l_2_row_ipv4_virt))
                    yield ' | '
                    yield str((undefined(name='row_ipv4_vers') if l_2_row_ipv4_vers is missing else l_2_row_ipv4_vers))
                    yield ' | '
                    yield str((undefined(name='row_ipv6_virt') if l_2_row_ipv6_virt is missing else l_2_row_ipv6_virt))
                    yield ' |\n'
                l_2_vrid = l_2_row_id = l_2_row_prio_level = l_2_row_ad_interval = l_2_row_preempt = l_2_row_tracked_object_name = l_2_row_tracked_object_action = l_2_row_ipv4_virt = l_2_row_ipv4_vers = l_2_row_ipv6_virt = missing
            l_1_ethernet_interface = missing
        if ((t_9((undefined(name='ethernet_interfaces_isis') if l_0_ethernet_interfaces_isis is missing else l_0_ethernet_interfaces_isis)) > 0) or (t_9((undefined(name='port_channel_interfaces_isis') if l_0_port_channel_interfaces_isis is missing else l_0_port_channel_interfaces_isis)) > 0)):
            pass
            yield '\n##### ISIS\n\n| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |\n| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |\n'
            for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
                l_1_port_channel_interface_name = resolve('port_channel_interface_name')
                l_1_port_channel_interface = resolve('port_channel_interface')
                l_1_channel_group = resolve('channel_group')
                l_1_isis_instance = resolve('isis_instance')
                l_1_isis_bfd = resolve('isis_bfd')
                l_1_isis_metric = resolve('isis_metric')
                l_1_isis_circuit_type = resolve('isis_circuit_type')
                l_1_isis_hello_padding = resolve('isis_hello_padding')
                l_1_isis_authentication_mode = resolve('isis_authentication_mode')
                l_1_mode = resolve('mode')
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')):
                    pass
                    l_1_port_channel_interface_name = str_join(('Port-Channel', environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), ))
                    _loop_vars['port_channel_interface_name'] = l_1_port_channel_interface_name
                    l_1_port_channel_interface = t_5(environment, t_11(context, (undefined(name='port_channel_interfaces_isis') if l_0_port_channel_interfaces_isis is missing else l_0_port_channel_interfaces_isis), 'name', 'arista.avd.defined', (undefined(name='port_channel_interface_name') if l_1_port_channel_interface_name is missing else l_1_port_channel_interface_name)))
                    _loop_vars['port_channel_interface'] = l_1_port_channel_interface
                    if t_12((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface)):
                        pass
                        l_1_channel_group = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), '-')
                        _loop_vars['channel_group'] = l_1_channel_group
                        l_1_isis_instance = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_enable'), '-')
                        _loop_vars['isis_instance'] = l_1_isis_instance
                        l_1_isis_bfd = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_bfd'), '-')
                        _loop_vars['isis_bfd'] = l_1_isis_bfd
                        l_1_isis_metric = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_metric'), '-')
                        _loop_vars['isis_metric'] = l_1_isis_metric
                        l_1_isis_circuit_type = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_circuit_type'), '-')
                        _loop_vars['isis_circuit_type'] = l_1_isis_circuit_type
                        l_1_isis_hello_padding = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_hello_padding'), '-')
                        _loop_vars['isis_hello_padding'] = l_1_isis_hello_padding
                        if t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'both'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'both'), 'mode')
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif (t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_1'), 'mode')) and t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_2'), 'mode'))):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-1: ', environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_1'), 'mode'), '<br>', 'Level-2: ', environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_2'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_1'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-1: ', environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_1'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif t_12(environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_2'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-2: ', environment.getattr(environment.getattr(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication'), 'level_2'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        else:
                            pass
                            l_1_isis_authentication_mode = t_1(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_authentication_mode'), '-')
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        if t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_network_point_to_point'), True):
                            pass
                            l_1_mode = 'point-to-point'
                            _loop_vars['mode'] = l_1_mode
                        elif t_12(environment.getattr((undefined(name='port_channel_interface') if l_1_port_channel_interface is missing else l_1_port_channel_interface), 'isis_passive'), True):
                            pass
                            l_1_mode = 'passive'
                            _loop_vars['mode'] = l_1_mode
                        else:
                            pass
                            l_1_mode = '-'
                            _loop_vars['mode'] = l_1_mode
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                        yield ' | *'
                        yield str((undefined(name='isis_instance') if l_1_isis_instance is missing else l_1_isis_instance))
                        yield ' | '
                        yield str((undefined(name='isis_bfd') if l_1_isis_bfd is missing else l_1_isis_bfd))
                        yield ' | *'
                        yield str((undefined(name='isis_metric') if l_1_isis_metric is missing else l_1_isis_metric))
                        yield ' | *'
                        yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                        yield ' | *'
                        yield str((undefined(name='isis_circuit_type') if l_1_isis_circuit_type is missing else l_1_isis_circuit_type))
                        yield ' | *'
                        yield str((undefined(name='isis_hello_padding') if l_1_isis_hello_padding is missing else l_1_isis_hello_padding))
                        yield ' | *'
                        yield str((undefined(name='isis_authentication_mode') if l_1_isis_authentication_mode is missing else l_1_isis_authentication_mode))
                        yield ' |\n'
                else:
                    pass
                    if (l_1_ethernet_interface in (undefined(name='ethernet_interfaces_isis') if l_0_ethernet_interfaces_isis is missing else l_0_ethernet_interfaces_isis)):
                        pass
                        l_1_channel_group = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), '-')
                        _loop_vars['channel_group'] = l_1_channel_group
                        l_1_isis_instance = t_1(environment.getattr(l_1_ethernet_interface, 'isis_enable'), '-')
                        _loop_vars['isis_instance'] = l_1_isis_instance
                        l_1_isis_bfd = t_1(environment.getattr(l_1_ethernet_interface, 'isis_bfd'), '-')
                        _loop_vars['isis_bfd'] = l_1_isis_bfd
                        l_1_isis_metric = t_1(environment.getattr(l_1_ethernet_interface, 'isis_metric'), '-')
                        _loop_vars['isis_metric'] = l_1_isis_metric
                        l_1_isis_circuit_type = t_1(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type'), '-')
                        _loop_vars['isis_circuit_type'] = l_1_isis_circuit_type
                        l_1_isis_hello_padding = t_1(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'), '-')
                        _loop_vars['isis_hello_padding'] = l_1_isis_hello_padding
                        if t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode')
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif (t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode')) and t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode'))):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-1: ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode'), '<br>', 'Level-2: ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-1: ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        elif t_12(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode')):
                            pass
                            l_1_isis_authentication_mode = str_join(('Level-2: ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode'), ))
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        else:
                            pass
                            l_1_isis_authentication_mode = t_1(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode'), '-')
                            _loop_vars['isis_authentication_mode'] = l_1_isis_authentication_mode
                        if t_12(environment.getattr(l_1_ethernet_interface, 'isis_network_point_to_point'), True):
                            pass
                            l_1_mode = 'point-to-point'
                            _loop_vars['mode'] = l_1_mode
                        elif t_12(environment.getattr(l_1_ethernet_interface, 'isis_passive'), True):
                            pass
                            l_1_mode = 'passive'
                            _loop_vars['mode'] = l_1_mode
                        else:
                            pass
                            l_1_mode = '-'
                            _loop_vars['mode'] = l_1_mode
                        yield '| '
                        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                        yield ' | '
                        yield str((undefined(name='channel_group') if l_1_channel_group is missing else l_1_channel_group))
                        yield ' | '
                        yield str((undefined(name='isis_instance') if l_1_isis_instance is missing else l_1_isis_instance))
                        yield ' | '
                        yield str((undefined(name='isis_bfd') if l_1_isis_bfd is missing else l_1_isis_bfd))
                        yield ' | '
                        yield str((undefined(name='isis_metric') if l_1_isis_metric is missing else l_1_isis_metric))
                        yield ' | '
                        yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                        yield ' | '
                        yield str((undefined(name='isis_circuit_type') if l_1_isis_circuit_type is missing else l_1_isis_circuit_type))
                        yield ' | '
                        yield str((undefined(name='isis_hello_padding') if l_1_isis_hello_padding is missing else l_1_isis_hello_padding))
                        yield ' | '
                        yield str((undefined(name='isis_authentication_mode') if l_1_isis_authentication_mode is missing else l_1_isis_authentication_mode))
                        yield ' |\n'
            l_1_ethernet_interface = l_1_port_channel_interface_name = l_1_port_channel_interface = l_1_channel_group = l_1_isis_instance = l_1_isis_bfd = l_1_isis_metric = l_1_isis_circuit_type = l_1_isis_hello_padding = l_1_isis_authentication_mode = l_1_mode = missing
        if (t_9((undefined(name='port_channel_interfaces_isis') if l_0_port_channel_interfaces_isis is missing else l_0_port_channel_interfaces_isis)) > 0):
            pass
            yield '\n*Inherited from Port-Channel Interface\n'
        l_0_evpn_es_ethernet_interfaces = []
        context.vars['evpn_es_ethernet_interfaces'] = l_0_evpn_es_ethernet_interfaces
        context.exported_vars.add('evpn_es_ethernet_interfaces')
        l_0_evpn_dfe_ethernet_interfaces = []
        context.vars['evpn_dfe_ethernet_interfaces'] = l_0_evpn_dfe_ethernet_interfaces
        context.exported_vars.add('evpn_dfe_ethernet_interfaces')
        l_0_evpn_mpls_ethernet_interfaces = []
        context.vars['evpn_mpls_ethernet_interfaces'] = l_0_evpn_mpls_ethernet_interfaces
        context.exported_vars.add('evpn_mpls_ethernet_interfaces')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment')):
                pass
                context.call(environment.getattr((undefined(name='evpn_es_ethernet_interfaces') if l_0_evpn_es_ethernet_interfaces is missing else l_0_evpn_es_ethernet_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election')):
                    pass
                    context.call(environment.getattr((undefined(name='evpn_dfe_ethernet_interfaces') if l_0_evpn_dfe_ethernet_interfaces is missing else l_0_evpn_dfe_ethernet_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls')):
                    pass
                    context.call(environment.getattr((undefined(name='evpn_mpls_ethernet_interfaces') if l_0_evpn_mpls_ethernet_interfaces is missing else l_0_evpn_mpls_ethernet_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='evpn_es_ethernet_interfaces') if l_0_evpn_es_ethernet_interfaces is missing else l_0_evpn_es_ethernet_interfaces)) > 0):
            pass
            yield '\n##### EVPN Multihoming\n\n####### EVPN Multihoming Summary\n\n| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |\n| --------- | --------------------------- | --------------------------- | ------------ |\n'
            for l_1_evpn_es_ethernet_interface in (undefined(name='evpn_es_ethernet_interfaces') if l_0_evpn_es_ethernet_interfaces is missing else l_0_evpn_es_ethernet_interfaces):
                l_1_esi = l_1_redundancy = l_1_rt = missing
                _loop_vars = {}
                pass
                l_1_esi = t_1(environment.getattr(environment.getattr(l_1_evpn_es_ethernet_interface, 'evpn_ethernet_segment'), 'identifier'), '-')
                _loop_vars['esi'] = l_1_esi
                l_1_redundancy = t_1(environment.getattr(environment.getattr(l_1_evpn_es_ethernet_interface, 'evpn_ethernet_segment'), 'redundancy'), 'all-active')
                _loop_vars['redundancy'] = l_1_redundancy
                l_1_rt = t_1(environment.getattr(environment.getattr(l_1_evpn_es_ethernet_interface, 'evpn_ethernet_segment'), 'route_target'), '-')
                _loop_vars['rt'] = l_1_rt
                yield '| '
                yield str(environment.getattr(l_1_evpn_es_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='esi') if l_1_esi is missing else l_1_esi))
                yield ' | '
                yield str((undefined(name='redundancy') if l_1_redundancy is missing else l_1_redundancy))
                yield ' | '
                yield str((undefined(name='rt') if l_1_rt is missing else l_1_rt))
                yield ' |\n'
            l_1_evpn_es_ethernet_interface = l_1_esi = l_1_redundancy = l_1_rt = missing
            if (t_9((undefined(name='evpn_dfe_ethernet_interfaces') if l_0_evpn_dfe_ethernet_interfaces is missing else l_0_evpn_dfe_ethernet_interfaces)) > 0):
                pass
                yield '\n####### Designated Forwarder Election Summary\n\n| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |\n| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |\n'
                for l_1_evpn_dfe_ethernet_interface in (undefined(name='evpn_dfe_ethernet_interfaces') if l_0_evpn_dfe_ethernet_interfaces is missing else l_0_evpn_dfe_ethernet_interfaces):
                    l_1_df_eth_settings = l_1_algorithm = l_1_pref_value = l_1_dont_preempt = l_1_hold_time = l_1_subsequent_hold_time = l_1_candidate_reachability = missing
                    _loop_vars = {}
                    pass
                    l_1_df_eth_settings = environment.getattr(environment.getattr(l_1_evpn_dfe_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election')
                    _loop_vars['df_eth_settings'] = l_1_df_eth_settings
                    l_1_algorithm = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'algorithm'), 'modulus')
                    _loop_vars['algorithm'] = l_1_algorithm
                    l_1_pref_value = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'preference_value'), '-')
                    _loop_vars['pref_value'] = l_1_pref_value
                    l_1_dont_preempt = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'dont_preempt'), False)
                    _loop_vars['dont_preempt'] = l_1_dont_preempt
                    l_1_hold_time = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'hold_time'), '-')
                    _loop_vars['hold_time'] = l_1_hold_time
                    l_1_subsequent_hold_time = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'subsequent_hold_time'), '-')
                    _loop_vars['subsequent_hold_time'] = l_1_subsequent_hold_time
                    l_1_candidate_reachability = t_1(environment.getattr((undefined(name='df_eth_settings') if l_1_df_eth_settings is missing else l_1_df_eth_settings), 'candidate_reachability_required'), False)
                    _loop_vars['candidate_reachability'] = l_1_candidate_reachability
                    yield '| '
                    yield str(environment.getattr(l_1_evpn_dfe_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='algorithm') if l_1_algorithm is missing else l_1_algorithm))
                    yield ' | '
                    yield str((undefined(name='pref_value') if l_1_pref_value is missing else l_1_pref_value))
                    yield ' | '
                    yield str((undefined(name='dont_preempt') if l_1_dont_preempt is missing else l_1_dont_preempt))
                    yield ' | '
                    yield str((undefined(name='hold_time') if l_1_hold_time is missing else l_1_hold_time))
                    yield ' | '
                    yield str((undefined(name='subsequent_hold_time') if l_1_subsequent_hold_time is missing else l_1_subsequent_hold_time))
                    yield ' | '
                    yield str((undefined(name='candidate_reachability') if l_1_candidate_reachability is missing else l_1_candidate_reachability))
                    yield ' |\n'
                l_1_evpn_dfe_ethernet_interface = l_1_df_eth_settings = l_1_algorithm = l_1_pref_value = l_1_dont_preempt = l_1_hold_time = l_1_subsequent_hold_time = l_1_candidate_reachability = missing
            if (t_9((undefined(name='evpn_mpls_ethernet_interfaces') if l_0_evpn_mpls_ethernet_interfaces is missing else l_0_evpn_mpls_ethernet_interfaces)) > 0):
                pass
                yield '\n####### EVPN-MPLS summary\n\n| Interface | Shared Index | Tunnel Flood Filter Time |\n| --------- | ------------ | ------------------------ |\n'
                for l_1_evpn_mpls_ethernet_interface in (undefined(name='evpn_mpls_ethernet_interfaces') if l_0_evpn_mpls_ethernet_interfaces is missing else l_0_evpn_mpls_ethernet_interfaces):
                    l_1_shared_index = l_1_tff_time = missing
                    _loop_vars = {}
                    pass
                    l_1_shared_index = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_evpn_mpls_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'shared_index'), '-')
                    _loop_vars['shared_index'] = l_1_shared_index
                    l_1_tff_time = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_evpn_mpls_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'tunnel_flood_filter_time'), '-')
                    _loop_vars['tff_time'] = l_1_tff_time
                    yield '| '
                    yield str(environment.getattr(l_1_evpn_mpls_ethernet_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='shared_index') if l_1_shared_index is missing else l_1_shared_index))
                    yield ' | '
                    yield str((undefined(name='tff_time') if l_1_tff_time is missing else l_1_tff_time))
                    yield ' |\n'
                l_1_evpn_mpls_ethernet_interface = l_1_shared_index = l_1_tff_time = missing
        l_0_err_cor_enc_intfs = []
        context.vars['err_cor_enc_intfs'] = l_0_err_cor_enc_intfs
        context.exported_vars.add('err_cor_enc_intfs')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding')):
                pass
                context.call(environment.getattr((undefined(name='err_cor_enc_intfs') if l_0_err_cor_enc_intfs is missing else l_0_err_cor_enc_intfs), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='err_cor_enc_intfs') if l_0_err_cor_enc_intfs is missing else l_0_err_cor_enc_intfs)) > 0):
            pass
            yield '\n##### Error Correction Encoding Interfaces\n\n| Interface | Enabled |\n| --------- | ------- |\n'
            for l_1_ethernet_interface in (undefined(name='err_cor_enc_intfs') if l_0_err_cor_enc_intfs is missing else l_0_err_cor_enc_intfs):
                l_1_enabled = resolve('enabled')
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'enabled'), False):
                    pass
                    l_1_enabled = ['Disabled']
                    _loop_vars['enabled'] = l_1_enabled
                else:
                    pass
                    l_1_enabled = []
                    _loop_vars['enabled'] = l_1_enabled
                    if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'fire_code'), True):
                        pass
                        context.call(environment.getattr((undefined(name='enabled') if l_1_enabled is missing else l_1_enabled), 'append'), 'fire-code', _loop_vars=_loop_vars)
                    if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'reed_solomon'), True):
                        pass
                        context.call(environment.getattr((undefined(name='enabled') if l_1_enabled is missing else l_1_enabled), 'append'), 'reed-solomon', _loop_vars=_loop_vars)
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str(t_8(context.eval_ctx, (undefined(name='enabled') if l_1_enabled is missing else l_1_enabled), '<br>'))
                yield ' |\n'
            l_1_ethernet_interface = l_1_enabled = missing
        l_0_priority_intfs = []
        context.vars['priority_intfs'] = l_0_priority_intfs
        context.exported_vars.add('priority_intfs')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'enabled')):
                pass
                context.call(environment.getattr((undefined(name='priority_intfs') if l_0_priority_intfs is missing else l_0_priority_intfs), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='priority_intfs') if l_0_priority_intfs is missing else l_0_priority_intfs)) > 0):
            pass
            yield '\n#### Priority Flow Control\n\n| Interface | PFC | Priority | Drop/No_drop |\n'
            for l_1_priority_intf in (undefined(name='priority_intfs') if l_0_priority_intfs is missing else l_0_priority_intfs):
                _loop_vars = {}
                pass
                if t_12(environment.getattr(environment.getattr(l_1_priority_intf, 'priority_flow_control'), 'priorities')):
                    pass
                    for l_2_priority_block in t_3(environment.getattr(environment.getattr(l_1_priority_intf, 'priority_flow_control'), 'priorities')):
                        l_2_priority = l_2_drop_no_drop = missing
                        _loop_vars = {}
                        pass
                        l_2_priority = t_1(environment.getattr(l_2_priority_block, 'priority'), '-')
                        _loop_vars['priority'] = l_2_priority
                        l_2_drop_no_drop = t_1(environment.getattr(l_2_priority_block, 'no_drop'), '-')
                        _loop_vars['drop_no_drop'] = l_2_drop_no_drop
                        yield '| '
                        yield str(environment.getattr(l_1_priority_intf, 'name'))
                        yield ' | '
                        yield str(environment.getattr(environment.getattr(l_1_priority_intf, 'priority_flow_control'), 'enabled'))
                        yield ' | '
                        yield str((undefined(name='priority') if l_2_priority is missing else l_2_priority))
                        yield ' | '
                        yield str((undefined(name='drop_no_drop') if l_2_drop_no_drop is missing else l_2_drop_no_drop))
                        yield ' |\n'
                    l_2_priority_block = l_2_priority = l_2_drop_no_drop = missing
                else:
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_priority_intf, 'name'))
                    yield ' | '
                    yield str(environment.getattr(environment.getattr(l_1_priority_intf, 'priority_flow_control'), 'enabled'))
                    yield ' | - | - |\n'
            l_1_priority_intf = missing
        l_0_sync_e_interfaces = []
        context.vars['sync_e_interfaces'] = l_0_sync_e_interfaces
        context.exported_vars.add('sync_e_interfaces')
        for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_12(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sync_e'), 'enable'), True):
                pass
                context.call(environment.getattr((undefined(name='sync_e_interfaces') if l_0_sync_e_interfaces is missing else l_0_sync_e_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
        l_1_ethernet_interface = missing
        if (t_9((undefined(name='sync_e_interfaces') if l_0_sync_e_interfaces is missing else l_0_sync_e_interfaces)) > 0):
            pass
            yield '\n#### Synchronous Ethernet\n\n| Interface | Priority |\n| --------- | -------- |\n'
            for l_1_sync_e_interface in (undefined(name='sync_e_interfaces') if l_0_sync_e_interfaces is missing else l_0_sync_e_interfaces):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_sync_e_interface, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_sync_e_interface, 'sync_e'), 'priority'), '127'))
                yield ' |\n'
            l_1_sync_e_interface = missing
        yield '\n#### Ethernet Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ethernet-interfaces.j2', 'documentation/ethernet-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'encapsulation_dot1q_interfaces': l_0_encapsulation_dot1q_interfaces, 'err_cor_enc_intfs': l_0_err_cor_enc_intfs, 'ethernet_interface_ipv4': l_0_ethernet_interface_ipv4, 'ethernet_interface_ipv6': l_0_ethernet_interface_ipv6, 'ethernet_interface_pvlan': l_0_ethernet_interface_pvlan, 'ethernet_interface_vlan_xlate': l_0_ethernet_interface_vlan_xlate, 'ethernet_interfaces_isis': l_0_ethernet_interfaces_isis, 'ethernet_interfaces_vrrp_details': l_0_ethernet_interfaces_vrrp_details, 'evpn_dfe_ethernet_interfaces': l_0_evpn_dfe_ethernet_interfaces, 'evpn_es_ethernet_interfaces': l_0_evpn_es_ethernet_interfaces, 'evpn_mpls_ethernet_interfaces': l_0_evpn_mpls_ethernet_interfaces, 'flexencap_interfaces': l_0_flexencap_interfaces, 'ip_nat_interfaces': l_0_ip_nat_interfaces, 'link_tracking_interfaces': l_0_link_tracking_interfaces, 'multicast_interfaces': l_0_multicast_interfaces, 'phone_interfaces': l_0_phone_interfaces, 'port_channel_interface_ipv4': l_0_port_channel_interface_ipv4, 'port_channel_interface_ipv6': l_0_port_channel_interface_ipv6, 'port_channel_interfaces_isis': l_0_port_channel_interfaces_isis, 'priority_intfs': l_0_priority_intfs, 'sync_e_interfaces': l_0_sync_e_interfaces, 'tcp_mss_clampings': l_0_tcp_mss_clampings, 'transceiver_settings': l_0_transceiver_settings})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=109&17=112&18=123&19=125&20=127&25=129&33=131&34=133&35=135&37=137&38=139&39=141&41=142&42=144&44=145&45=147&47=151&50=153&51=155&53=159&55=161&56=163&57=166&59=180&60=182&61=184&62=186&63=188&64=190&66=194&68=196&69=198&70=201&75=217&83=219&84=221&85=223&87=225&88=227&89=229&91=230&92=232&94=233&95=235&96=237&97=239&100=241&101=243&103=247&105=249&106=252&108=264&109=266&110=268&111=270&112=272&113=274&115=278&117=280&118=283&125=297&126=300&127=303&128=306&129=308&130=309&131=311&132=312&133=314&134=316&135=317&136=319&140=321&146=324&147=328&148=330&149=332&150=334&151=337&154=348&160=351&161=363&162=365&163=367&166=369&167=371&168=373&169=375&170=377&173=379&174=381&175=383&176=385&177=387&179=389&182=391&183=393&184=395&185=397&186=399&189=401&190=403&191=405&192=407&193=409&195=412&199=439&200=442&201=445&202=448&206=450&207=453&210=455&216=458&217=462&218=464&219=466&220=469&225=476&226=479&227=482&228=485&230=487&231=490&234=492&240=495&241=498&242=500&243=504&245=517&246=521&248=534&249=539&250=541&251=543&253=547&255=550&257=563&258=565&259=569&260=571&261=574&268=584&269=587&270=590&271=592&274=594&280=597&281=603&282=605&283=607&285=609&286=611&288=614&292=623&293=626&294=629&295=631&298=633&304=636&305=641&306=643&307=645&308=647&309=649&312=653&314=655&315=658&319=665&320=668&321=671&322=673&325=675&331=678&332=681&333=684&334=687&337=694&338=697&343=704&344=707&345=710&346=712&349=714&355=717&356=721&357=723&358=725&359=727&360=730&364=741&365=744&366=747&367=749&370=751&376=754&377=759&378=761&379=763&380=765&384=769&386=772&388=778&389=780&390=782&391=784&395=788&397=791&402=798&403=801&404=804&405=807&406=809&407=812&410=814&411=817&412=820&413=823&414=825&415=828&418=830&424=833&425=846&426=848&427=850&430=852&431=854&432=856&433=858&434=860&435=862&436=864&437=866&438=868&439=871&442=891&443=893&444=895&445=897&446=899&447=901&448=903&449=905&450=908&455=925&460=928&461=931&463=934&464=937&465=940&466=943&467=945&468=948&471=950&472=953&473=956&474=959&475=961&476=964&479=966&485=969&486=984&487=986&488=988&491=990&492=992&493=994&494=996&495=998&496=1000&497=1002&498=1004&499=1006&500=1008&501=1010&502=1013&505=1037&506=1039&507=1041&508=1043&509=1045&510=1047&511=1049&512=1051&513=1053&514=1055&515=1058&520=1079&525=1082&526=1085&527=1088&538=1090&541=1092&542=1095&543=1098&554=1100&558=1102&559=1105&560=1108&561=1110&564=1112&570=1115&571=1118&572=1128&573=1130&574=1132&575=1134&576=1136&577=1138&579=1140&580=1142&581=1144&582=1146&583=1149&584=1150&585=1152&586=1153&587=1155&590=1157&591=1159&593=1161&594=1163&595=1165&596=1168&600=1190&606=1193&607=1206&608=1208&609=1210&611=1212&612=1214&613=1216&614=1218&615=1220&616=1222&617=1224&618=1226&619=1228&620=1230&621=1232&622=1234&623=1236&624=1238&625=1240&627=1244&629=1246&630=1248&631=1250&632=1252&634=1256&636=1259&639=1279&640=1281&641=1283&642=1285&643=1287&644=1289&645=1291&646=1293&647=1295&648=1297&649=1299&650=1301&651=1303&652=1305&653=1307&655=1311&657=1313&658=1315&659=1317&660=1319&662=1323&664=1326&669=1345&674=1348&675=1351&676=1354&677=1357&678=1360&679=1362&680=1363&681=1365&683=1366&684=1368&688=1370&696=1373&697=1377&698=1379&699=1381&700=1384&702=1393&708=1396&709=1400&710=1402&711=1404&712=1406&713=1408&714=1410&715=1412&716=1415&719=1430&725=1433&726=1437&727=1439&728=1442&732=1449&733=1452&734=1455&735=1457&738=1459&744=1462&745=1466&746=1468&748=1472&749=1474&750=1476&752=1477&753=1479&756=1481&759=1486&760=1489&761=1492&762=1494&765=1496&770=1499&771=1502&772=1504&773=1508&774=1510&775=1513&778=1525&782=1530&783=1533&784=1536&785=1538&788=1540&794=1543&795=1547&802=1553'