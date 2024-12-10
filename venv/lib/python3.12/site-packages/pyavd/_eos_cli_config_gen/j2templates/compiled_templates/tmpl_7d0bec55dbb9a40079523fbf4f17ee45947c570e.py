from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ethernet-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_POE_CLASS_MAP = missing
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
        t_4 = environment.filters['arista.avd.range_expand']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.range_expand' found.")
    try:
        t_5 = environment.filters['float']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'float' found.")
    try:
        t_6 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    try:
        t_7 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_8 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_9 = environment.filters['sort']
    except KeyError:
        @internalcode
        def t_9(*unused):
            raise TemplateRuntimeError("No filter named 'sort' found.")
    try:
        t_10 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_10(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_POE_CLASS_MAP = {0: '15.40', 1: '4.00', 2: '7.00', 3: '15.40', 4: '30.00', 5: '45.00', 6: '60.00', 7: '75.00', 8: '90.00'}
    context.vars['POE_CLASS_MAP'] = l_0_POE_CLASS_MAP
    context.exported_vars.add('POE_CLASS_MAP')
    for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        l_1_encapsulation_cli = resolve('encapsulation_cli')
        l_1_encapsulation_dot1q_cli = resolve('encapsulation_dot1q_cli')
        l_1_client_encapsulation = resolve('client_encapsulation')
        l_1_network_flag = resolve('network_flag')
        l_1_network_encapsulation = resolve('network_encapsulation')
        l_1_dfe_algo_cli = resolve('dfe_algo_cli')
        l_1_dfe_hold_time_cli = resolve('dfe_hold_time_cli')
        l_1_address_locking_cli = resolve('address_locking_cli')
        l_1_host_proxy_cli = resolve('host_proxy_cli')
        l_1_tcp_mss_ceiling_cli = resolve('tcp_mss_ceiling_cli')
        l_1_interface_ip_nat = resolve('interface_ip_nat')
        l_1_hide_passwords = resolve('hide_passwords')
        l_1_poe_link_down_action_cli = resolve('poe_link_down_action_cli')
        l_1_poe_limit_cli = resolve('poe_limit_cli')
        l_1_sorted_vlans_cli = resolve('sorted_vlans_cli')
        l_1_isis_auth_cli = resolve('isis_auth_cli')
        l_1_both_key_ids = resolve('both_key_ids')
        l_1_backup_link_cli = resolve('backup_link_cli')
        l_1_frequency_cli = resolve('frequency_cli')
        l_1_aaa_config = resolve('aaa_config')
        l_1_actions = resolve('actions')
        l_1_host_mode_cli = resolve('host_mode_cli')
        l_1_auth_cli = resolve('auth_cli')
        l_1_auth_failure_fallback_mba = resolve('auth_failure_fallback_mba')
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
        yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'profile')):
            pass
            yield '   profile '
            yield str(environment.getattr(l_1_ethernet_interface, 'profile'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'input')):
            pass
            yield '   traffic-policy input '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'input'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'output')):
            pass
            yield '   traffic-policy output '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'output'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_ethernet_interface, 'description'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'load_interval')):
            pass
            yield '   load-interval '
            yield str(environment.getattr(l_1_ethernet_interface, 'load_interval'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr(l_1_ethernet_interface, 'mtu'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'link_status'), True):
            pass
            yield '   logging event link-status\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'link_status'), False):
            pass
            yield '   no logging event link-status\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bgp'), 'session_tracker')):
            pass
            yield '   bgp session tracker '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bgp'), 'session_tracker'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'forwarding_profile')):
            pass
            yield '   l2-protocol forwarding profile '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'forwarding_profile'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flowcontrol'), 'received')):
            pass
            yield '   flowcontrol receive '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flowcontrol'), 'received'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'l2_mtu')):
            pass
            yield '   l2 mtu '
            yield str(environment.getattr(l_1_ethernet_interface, 'l2_mtu'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'l2_mru')):
            pass
            yield '   l2 mru '
            yield str(environment.getattr(l_1_ethernet_interface, 'l2_mru'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'congestion_drops'), True):
            pass
            yield '   logging event congestion-drops\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'congestion_drops'), False):
            pass
            yield '   no logging event congestion-drops\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'speed')):
            pass
            yield '   speed '
            yield str(environment.getattr(l_1_ethernet_interface, 'speed'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'enabled'), False):
            pass
            yield '   no error-correction encoding\n'
        else:
            pass
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'fire_code'), True):
                pass
                yield '   error-correction encoding fire-code\n'
            elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'fire_code'), False):
                pass
                yield '   no error-correction encoding fire-code\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'reed_solomon'), True):
                pass
                yield '   error-correction encoding reed-solomon\n'
            elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'reed_solomon'), False):
                pass
                yield '   no error-correction encoding reed-solomon\n'
        if (t_10(environment.getattr(l_1_ethernet_interface, 'mode'), 'access') or t_10(environment.getattr(l_1_ethernet_interface, 'mode'), 'dot1q-tunnel')):
            pass
            if t_10(environment.getattr(l_1_ethernet_interface, 'vlans')):
                pass
                yield '   switchport access vlan '
                yield str(environment.getattr(l_1_ethernet_interface, 'vlans'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan')):
            pass
            yield '   switchport access vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'access_vlan'))
            yield '\n'
        if (t_10(environment.getattr(l_1_ethernet_interface, 'mode')) and (environment.getattr(l_1_ethernet_interface, 'mode') in ['trunk', 'trunk phone'])):
            pass
            if t_10(environment.getattr(l_1_ethernet_interface, 'native_vlan_tag'), True):
                pass
                yield '   switchport trunk native vlan tag\n'
            elif t_10(environment.getattr(l_1_ethernet_interface, 'native_vlan')):
                pass
                yield '   switchport trunk native vlan '
                yield str(environment.getattr(l_1_ethernet_interface, 'native_vlan'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'vlan')):
            pass
            yield '   switchport phone vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'vlan'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'trunk')):
            pass
            yield '   switchport phone trunk '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'trunk'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan_tag'), True):
            pass
            yield '   switchport trunk native vlan tag\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan')):
            pass
            yield '   switchport trunk native vlan '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'native_vlan'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'phone'), 'vlan')):
            pass
            yield '   switchport phone vlan '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'phone'), 'vlan'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'phone'), 'trunk')):
            pass
            yield '   switchport phone trunk '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'phone'), 'trunk'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'in_required'), True):
            pass
            yield '   switchport vlan translation in required\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'out_required'), True):
            pass
            yield '   switchport vlan translation out required\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'dot1q'), 'vlan_tag')):
            pass
            yield '   switchport dot1q vlan tag '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'dot1q'), 'vlan_tag'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mode'), 'trunk'):
            pass
            if t_10(environment.getattr(l_1_ethernet_interface, 'vlans')):
                pass
                yield '   switchport trunk allowed vlan '
                yield str(environment.getattr(l_1_ethernet_interface, 'vlans'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan')):
            pass
            yield '   switchport trunk allowed vlan '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'allowed_vlan'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mode')):
            pass
            yield '   switchport mode '
            yield str(environment.getattr(l_1_ethernet_interface, 'mode'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'mode')):
            pass
            yield '   switchport mode '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'mode'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'dot1q'), 'ethertype')):
            pass
            yield '   switchport dot1q ethertype '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'dot1q'), 'ethertype'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_forwarding_accept_all'), True):
            pass
            yield '   switchport vlan forwarding accept all\n'
        for l_2_trunk_group in t_3(environment.getattr(l_1_ethernet_interface, 'trunk_groups')):
            _loop_vars = {}
            pass
            yield '   switchport trunk group '
            yield str(l_2_trunk_group)
            yield '\n'
        l_2_trunk_group = missing
        for l_2_trunk_group in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'groups')):
            _loop_vars = {}
            pass
            yield '   switchport trunk group '
            yield str(l_2_trunk_group)
            yield '\n'
        l_2_trunk_group = missing
        if t_10(environment.getattr(l_1_ethernet_interface, 'type'), 'routed'):
            pass
            yield '   no switchport\n'
        elif (t_1(environment.getattr(l_1_ethernet_interface, 'type')) in ['l3dot1q', 'l2dot1q']):
            pass
            if (t_10(environment.getattr(l_1_ethernet_interface, 'vlan_id')) and (environment.getattr(l_1_ethernet_interface, 'type') == 'l2dot1q')):
                pass
                yield '   vlan id '
                yield str(environment.getattr(l_1_ethernet_interface, 'vlan_id'))
                yield '\n'
            if t_10(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan')):
                pass
                yield '   encapsulation dot1q vlan '
                yield str(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan'))
                yield '\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'vlan')):
                pass
                l_1_encapsulation_cli = str_join(('client dot1q ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'vlan'), ))
                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'vlan')):
                    pass
                    l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network dot1q ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'vlan'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'client'), True):
                    pass
                    l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network client', ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
            elif (t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'inner')) and t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'outer'))):
                pass
                l_1_encapsulation_cli = str_join(('client dot1q outer ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'outer'), ' inner ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'inner'), ))
                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                if (t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'inner')) and t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'outer'))):
                    pass
                    l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network dot1q outer ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'outer'), ' inner ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'inner'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                elif t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'client'), True):
                    pass
                    l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network client', ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
            elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'unmatched'), True):
                pass
                l_1_encapsulation_cli = 'client unmatched'
                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
            if t_10((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli)):
                pass
                yield '   encapsulation vlan\n      '
                yield str((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli))
                yield '\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'type'), 'switched'):
            pass
            yield '   switchport\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'enabled'), True):
            pass
            yield '   switchport\n'
        elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'enabled'), False):
            pass
            yield '   no switchport\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'vlan')):
            pass
            l_1_encapsulation_dot1q_cli = str_join(('encapsulation dot1q vlan ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'vlan'), ))
            _loop_vars['encapsulation_dot1q_cli'] = l_1_encapsulation_dot1q_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'inner_vlan')):
                pass
                l_1_encapsulation_dot1q_cli = str_join(((undefined(name='encapsulation_dot1q_cli') if l_1_encapsulation_dot1q_cli is missing else l_1_encapsulation_dot1q_cli), ' inner ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'inner_vlan'), ))
                _loop_vars['encapsulation_dot1q_cli'] = l_1_encapsulation_dot1q_cli
            yield '   '
            yield str((undefined(name='encapsulation_dot1q_cli') if l_1_encapsulation_dot1q_cli is missing else l_1_encapsulation_dot1q_cli))
            yield '\n'
        if (t_10(environment.getattr(l_1_ethernet_interface, 'vlan_id')) and (t_1(environment.getattr(l_1_ethernet_interface, 'type')) != 'l2dot1q')):
            pass
            yield '   vlan id '
            yield str(environment.getattr(l_1_ethernet_interface, 'vlan_id'))
            yield '\n'
        if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'encapsulation')) and (not t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q'), 'vlan')))):
            pass
            l_1_client_encapsulation = environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'encapsulation')
            _loop_vars['client_encapsulation'] = l_1_client_encapsulation
            l_1_network_flag = False
            _loop_vars['network_flag'] = l_1_network_flag
            if ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) in ['dot1q', 'dot1ad']):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'vlan')):
                    pass
                    l_1_encapsulation_cli = str_join(('client ', (undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'vlan'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                elif (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'outer_vlan')) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_vlan'))):
                    pass
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_encapsulation')):
                        pass
                        l_1_encapsulation_cli = str_join(('client ', (undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation), ' outer ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'outer_vlan'), ' inner ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_encapsulation'), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_vlan'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    else:
                        pass
                        l_1_encapsulation_cli = str_join(('client ', (undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation), ' outer ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'outer_vlan'), ' inner ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'inner_vlan'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    if (t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'encapsulation')) == 'client inner'):
                        pass
                        l_1_network_flag = True
                        _loop_vars['network_flag'] = l_1_network_flag
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'encapsulation'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
            elif ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) in ['untagged', 'unmatched']):
                pass
                l_1_encapsulation_cli = str_join(('client ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'encapsulation'), ))
                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
            if t_10((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli)):
                pass
                if ((((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) in ['dot1q', 'dot1ad', 'untagged']) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'encapsulation'))) and (not (undefined(name='network_flag') if l_1_network_flag is missing else l_1_network_flag))):
                    pass
                    l_1_network_encapsulation = environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'encapsulation')
                    _loop_vars['network_encapsulation'] = l_1_network_encapsulation
                    if ((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation) in ['dot1q', 'dot1ad']):
                        pass
                        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'vlan')):
                            pass
                            l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network ', (undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'vlan'), ))
                            _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                        elif (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'outer_vlan')) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_vlan'))):
                            pass
                            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_encapsulation')):
                                pass
                                l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network ', (undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation), ' outer ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'outer_vlan'), ' inner ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_encapsulation'), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_vlan'), ))
                                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                            else:
                                pass
                                l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network ', (undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation), ' outer ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'outer_vlan'), ' inner ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'inner_vlan'), ))
                                _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    elif (((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation) == 'untagged') and ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) == 'untagged')):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network untagged', ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    elif (((undefined(name='network_encapsulation') if l_1_network_encapsulation is missing else l_1_network_encapsulation) == 'client') and ((undefined(name='client_encapsulation') if l_1_client_encapsulation is missing else l_1_client_encapsulation) != 'untagged')):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network client', ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                yield '   encapsulation vlan\n      '
                yield str((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'source_interface')):
            pass
            yield '   switchport source-interface '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'source_interface'))
            yield '\n'
        for l_2_vlan_translation in t_3(environment.getattr(l_1_ethernet_interface, 'vlan_translations')):
            l_2_vlan_translation_cli = resolve('vlan_translation_cli')
            _loop_vars = {}
            pass
            if (t_10(environment.getattr(l_2_vlan_translation, 'from')) and t_10(environment.getattr(l_2_vlan_translation, 'to'))):
                pass
                l_2_vlan_translation_cli = 'switchport vlan translation'
                _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                if (t_1(environment.getattr(l_2_vlan_translation, 'direction')) in ['in', 'out']):
                    pass
                    l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'direction'), ))
                    _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'from'), ))
                _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'to'), ))
                _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                yield '   '
                yield str((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli))
                yield '\n'
        l_2_vlan_translation = l_2_vlan_translation_cli = missing
        for l_2_vlan_translation in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_both'), 'from'):
            l_2_vlan_translation_both_cli = missing
            _loop_vars = {}
            pass
            l_2_vlan_translation_both_cli = str_join(('switchport vlan translation ', environment.getattr(l_2_vlan_translation, 'from'), ))
            _loop_vars['vlan_translation_both_cli'] = l_2_vlan_translation_both_cli
            if t_10(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel'), True):
                pass
                l_2_vlan_translation_both_cli = str_join(((undefined(name='vlan_translation_both_cli') if l_2_vlan_translation_both_cli is missing else l_2_vlan_translation_both_cli), ' dot1q-tunnel', ))
                _loop_vars['vlan_translation_both_cli'] = l_2_vlan_translation_both_cli
            elif t_10(environment.getattr(l_2_vlan_translation, 'inner_vlan_from')):
                pass
                l_2_vlan_translation_both_cli = str_join(((undefined(name='vlan_translation_both_cli') if l_2_vlan_translation_both_cli is missing else l_2_vlan_translation_both_cli), ' inner ', environment.getattr(l_2_vlan_translation, 'inner_vlan_from'), ))
                _loop_vars['vlan_translation_both_cli'] = l_2_vlan_translation_both_cli
                if t_10(environment.getattr(l_2_vlan_translation, 'network'), True):
                    pass
                    l_2_vlan_translation_both_cli = str_join(((undefined(name='vlan_translation_both_cli') if l_2_vlan_translation_both_cli is missing else l_2_vlan_translation_both_cli), ' network', ))
                    _loop_vars['vlan_translation_both_cli'] = l_2_vlan_translation_both_cli
            l_2_vlan_translation_both_cli = str_join(((undefined(name='vlan_translation_both_cli') if l_2_vlan_translation_both_cli is missing else l_2_vlan_translation_both_cli), ' ', environment.getattr(l_2_vlan_translation, 'to'), ))
            _loop_vars['vlan_translation_both_cli'] = l_2_vlan_translation_both_cli
            yield '   '
            yield str((undefined(name='vlan_translation_both_cli') if l_2_vlan_translation_both_cli is missing else l_2_vlan_translation_both_cli))
            yield '\n'
        l_2_vlan_translation = l_2_vlan_translation_both_cli = missing
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_in')):
            pass
            for l_2_vlan_translation in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_in'):
                l_2_vlan_translation_in_cli = missing
                _loop_vars = {}
                pass
                l_2_vlan_translation_in_cli = str_join(('switchport vlan translation in ', environment.getattr(l_2_vlan_translation, 'from'), ))
                _loop_vars['vlan_translation_in_cli'] = l_2_vlan_translation_in_cli
                if t_10(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel'), True):
                    pass
                    l_2_vlan_translation_in_cli = str_join(((undefined(name='vlan_translation_in_cli') if l_2_vlan_translation_in_cli is missing else l_2_vlan_translation_in_cli), ' dot1q-tunnel', ))
                    _loop_vars['vlan_translation_in_cli'] = l_2_vlan_translation_in_cli
                elif t_10(environment.getattr(l_2_vlan_translation, 'inner_vlan_from')):
                    pass
                    l_2_vlan_translation_in_cli = str_join(((undefined(name='vlan_translation_in_cli') if l_2_vlan_translation_in_cli is missing else l_2_vlan_translation_in_cli), ' inner ', environment.getattr(l_2_vlan_translation, 'inner_vlan_from'), ))
                    _loop_vars['vlan_translation_in_cli'] = l_2_vlan_translation_in_cli
                l_2_vlan_translation_in_cli = str_join(((undefined(name='vlan_translation_in_cli') if l_2_vlan_translation_in_cli is missing else l_2_vlan_translation_in_cli), ' ', environment.getattr(l_2_vlan_translation, 'to'), ))
                _loop_vars['vlan_translation_in_cli'] = l_2_vlan_translation_in_cli
                yield '   '
                yield str((undefined(name='vlan_translation_in_cli') if l_2_vlan_translation_in_cli is missing else l_2_vlan_translation_in_cli))
                yield '\n'
            l_2_vlan_translation = l_2_vlan_translation_in_cli = missing
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_out')):
            pass
            for l_2_vlan_translation in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'vlan_translations'), 'direction_out'):
                l_2_vlan_translation_out_cli = resolve('vlan_translation_out_cli')
                _loop_vars = {}
                pass
                if t_10(environment.getattr(l_2_vlan_translation, 'dot1q_tunnel_to')):
                    pass
                    l_2_vlan_translation_out_cli = str_join(('switchport vlan translation out ', environment.getattr(l_2_vlan_translation, 'from'), ' dot1q-tunnel ', environment.getattr(l_2_vlan_translation, 'dot1q_tunnel_to'), ))
                    _loop_vars['vlan_translation_out_cli'] = l_2_vlan_translation_out_cli
                elif t_10(environment.getattr(l_2_vlan_translation, 'to')):
                    pass
                    l_2_vlan_translation_out_cli = str_join(('switchport vlan translation out ', environment.getattr(l_2_vlan_translation, 'from'), ' ', environment.getattr(l_2_vlan_translation, 'to'), ))
                    _loop_vars['vlan_translation_out_cli'] = l_2_vlan_translation_out_cli
                    if t_10(environment.getattr(l_2_vlan_translation, 'inner_vlan_to')):
                        pass
                        l_2_vlan_translation_out_cli = str_join(((undefined(name='vlan_translation_out_cli') if l_2_vlan_translation_out_cli is missing else l_2_vlan_translation_out_cli), ' inner ', environment.getattr(l_2_vlan_translation, 'inner_vlan_to'), ))
                        _loop_vars['vlan_translation_out_cli'] = l_2_vlan_translation_out_cli
                if t_10((undefined(name='vlan_translation_out_cli') if l_2_vlan_translation_out_cli is missing else l_2_vlan_translation_out_cli)):
                    pass
                    yield '   '
                    yield str((undefined(name='vlan_translation_out_cli') if l_2_vlan_translation_out_cli is missing else l_2_vlan_translation_out_cli))
                    yield '\n'
            l_2_vlan_translation = l_2_vlan_translation_out_cli = missing
        if t_10(environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'), True):
            pass
            yield '   switchport trunk private-vlan secondary\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'), False):
            pass
            yield '   no switchport trunk private-vlan secondary\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'trunk'), 'private_vlan_secondary'), True):
            pass
            yield '   switchport trunk private-vlan secondary\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'pvlan_mapping')):
            pass
            yield '   switchport pvlan mapping '
            yield str(environment.getattr(l_1_ethernet_interface, 'pvlan_mapping'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'pvlan_mapping')):
            pass
            yield '   switchport pvlan mapping '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'pvlan_mapping'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'encapsulation_dot1q_vlan')):
            pass
            yield '   l2-protocol encapsulation dot1q vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'encapsulation_dot1q_vlan'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mac_timestamp')):
            pass
            yield '   mac timestamp '
            yield str(environment.getattr(l_1_ethernet_interface, 'mac_timestamp'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment')):
            pass
            yield '   !\n   evpn ethernet-segment\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'identifier')):
                pass
                yield '      identifier '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'identifier'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'redundancy')):
                pass
                yield '      redundancy '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'redundancy'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election')):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'algorithm'), 'modulus'):
                    pass
                    yield '      designated-forwarder election algorithm modulus\n'
                elif (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'algorithm'), 'preference') and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'preference_value'))):
                    pass
                    l_1_dfe_algo_cli = str_join(('designated-forwarder election algorithm preference ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'preference_value'), ))
                    _loop_vars['dfe_algo_cli'] = l_1_dfe_algo_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'dont_preempt'), True):
                        pass
                        l_1_dfe_algo_cli = str_join(((undefined(name='dfe_algo_cli') if l_1_dfe_algo_cli is missing else l_1_dfe_algo_cli), ' dont-preempt', ))
                        _loop_vars['dfe_algo_cli'] = l_1_dfe_algo_cli
                    yield '      '
                    yield str((undefined(name='dfe_algo_cli') if l_1_dfe_algo_cli is missing else l_1_dfe_algo_cli))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'hold_time')):
                    pass
                    l_1_dfe_hold_time_cli = str_join(('designated-forwarder election hold-time ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'hold_time'), ))
                    _loop_vars['dfe_hold_time_cli'] = l_1_dfe_hold_time_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'subsequent_hold_time')):
                        pass
                        l_1_dfe_hold_time_cli = str_join(((undefined(name='dfe_hold_time_cli') if l_1_dfe_hold_time_cli is missing else l_1_dfe_hold_time_cli), ' subsequent-hold-time ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'subsequent_hold_time'), ))
                        _loop_vars['dfe_hold_time_cli'] = l_1_dfe_hold_time_cli
                    yield '      '
                    yield str((undefined(name='dfe_hold_time_cli') if l_1_dfe_hold_time_cli is missing else l_1_dfe_hold_time_cli))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'candidate_reachability_required'), True):
                    pass
                    yield '      designated-forwarder election candidate reachability required\n'
                elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'candidate_reachability_required'), False):
                    pass
                    yield '      no designated-forwarder election candidate reachability required\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'tunnel_flood_filter_time')):
                pass
                yield '      mpls tunnel flood filter time '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'tunnel_flood_filter_time'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'shared_index')):
                pass
                yield '      mpls shared index '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'shared_index'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'route_target')):
                pass
                yield '      route-target import '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'route_target'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'hardware')):
            pass
            yield '   flow tracker hardware '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'hardware'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'sampled')):
            pass
            yield '   flow tracker sampled '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'sampled'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'snmp_trap_link_change'), False):
            pass
            yield '   no snmp trap link-change\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'snmp_trap_link_change'), True):
            pass
            yield '   snmp trap link-change\n'
        if (t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv4'), True) or t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv6'), True)):
            pass
            l_1_address_locking_cli = 'address locking'
            _loop_vars['address_locking_cli'] = l_1_address_locking_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv4'), True):
                pass
                l_1_address_locking_cli = ((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli) + ' ipv4')
                _loop_vars['address_locking_cli'] = l_1_address_locking_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv6'), True):
                pass
                l_1_address_locking_cli = ((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli) + ' ipv6')
                _loop_vars['address_locking_cli'] = l_1_address_locking_cli
            yield '   '
            yield str((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_ethernet_interface, 'vrf'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ip_proxy_arp'), True):
            pass
            yield '   ip proxy-arp\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_ethernet_interface, 'ip_address'))
            yield '\n'
            for l_2_ip_address_secondary in t_3(environment.getattr(l_1_ethernet_interface, 'ip_address_secondaries')):
                _loop_vars = {}
                pass
                yield '   ip address '
                yield str(l_2_ip_address_secondary)
                yield ' secondary\n'
            l_2_ip_address_secondary = missing
        if (t_10(environment.getattr(l_1_ethernet_interface, 'ip_address'), 'dhcp') and t_10(environment.getattr(l_1_ethernet_interface, 'dhcp_client_accept_default_route'), True)):
            pass
            yield '   dhcp client accept default-route\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ip_verify_unicast_source_reachable_via')):
            pass
            yield '   ip verify unicast source reachable-via '
            yield str(environment.getattr(l_1_ethernet_interface, 'ip_verify_unicast_source_reachable_via'))
            yield '\n'
        if ((t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval')) and t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))) and t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))):
            pass
            yield '   bfd interval '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval'))
            yield ' min-rx '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))
            yield ' multiplier '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'echo'), True):
            pass
            yield '   bfd echo\n'
        elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'echo'), False):
            pass
            yield '   no bfd echo\n'
        for l_2_ip_helper in t_3(environment.getattr(l_1_ethernet_interface, 'ip_helpers'), 'ip_helper'):
            l_2_ip_helper_cli = missing
            _loop_vars = {}
            pass
            l_2_ip_helper_cli = str_join(('ip helper-address ', environment.getattr(l_2_ip_helper, 'ip_helper'), ))
            _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            if t_10(environment.getattr(l_2_ip_helper, 'vrf')):
                pass
                l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' vrf ', environment.getattr(l_2_ip_helper, 'vrf'), ))
                _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            if t_10(environment.getattr(l_2_ip_helper, 'source_interface')):
                pass
                l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' source-interface ', environment.getattr(l_2_ip_helper, 'source_interface'), ))
                _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            yield '   '
            yield str((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli))
            yield '\n'
        l_2_ip_helper = l_2_ip_helper_cli = missing
        for l_2_destination in t_3(environment.getattr(l_1_ethernet_interface, 'ipv6_dhcp_relay_destinations'), 'address'):
            l_2_destination_cli = missing
            _loop_vars = {}
            pass
            l_2_destination_cli = str_join(('ipv6 dhcp relay destination ', environment.getattr(l_2_destination, 'address'), ))
            _loop_vars['destination_cli'] = l_2_destination_cli
            if t_10(environment.getattr(l_2_destination, 'vrf')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' vrf ', environment.getattr(l_2_destination, 'vrf'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_10(environment.getattr(l_2_destination, 'local_interface')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' local-interface ', environment.getattr(l_2_destination, 'local_interface'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            elif t_10(environment.getattr(l_2_destination, 'source_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' source-address ', environment.getattr(l_2_destination, 'source_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_10(environment.getattr(l_2_destination, 'link_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' link-address ', environment.getattr(l_2_destination, 'link_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            yield '   '
            yield str((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli))
            yield '\n'
        l_2_destination = l_2_destination_cli = missing
        if t_10(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv4'), True):
            pass
            yield '   dhcp server ipv4\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'dhcp_server_ipv6'), True):
            pass
            yield '   dhcp server ipv6\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'enabled'), True):
            pass
            l_1_host_proxy_cli = 'ip igmp host-proxy'
            _loop_vars['host_proxy_cli'] = l_1_host_proxy_cli
            yield '   '
            yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
            yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'groups')):
                pass
                for l_2_proxy_group in environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'groups'):
                    _loop_vars = {}
                    pass
                    if (t_10(environment.getattr(l_2_proxy_group, 'exclude')) or t_10(environment.getattr(l_2_proxy_group, 'include'))):
                        pass
                        if t_10(environment.getattr(l_2_proxy_group, 'include')):
                            pass
                            for l_3_include_source in environment.getattr(l_2_proxy_group, 'include'):
                                _loop_vars = {}
                                pass
                                yield '   '
                                yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                                yield ' '
                                yield str(environment.getattr(l_2_proxy_group, 'group'))
                                yield ' include '
                                yield str(environment.getattr(l_3_include_source, 'source'))
                                yield '\n'
                            l_3_include_source = missing
                        if t_10(environment.getattr(l_2_proxy_group, 'exclude')):
                            pass
                            for l_3_exclude_source in environment.getattr(l_2_proxy_group, 'exclude'):
                                _loop_vars = {}
                                pass
                                yield '   '
                                yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                                yield ' '
                                yield str(environment.getattr(l_2_proxy_group, 'group'))
                                yield ' exclude '
                                yield str(environment.getattr(l_3_exclude_source, 'source'))
                                yield '\n'
                            l_3_exclude_source = missing
                    elif t_10(environment.getattr(l_2_proxy_group, 'group')):
                        pass
                        yield '   '
                        yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                        yield ' '
                        yield str(environment.getattr(l_2_proxy_group, 'group'))
                        yield '\n'
                l_2_proxy_group = missing
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'access_lists')):
                pass
                for l_2_access_list in environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'access_lists'):
                    _loop_vars = {}
                    pass
                    yield '   '
                    yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                    yield ' access-list '
                    yield str(environment.getattr(l_2_access_list, 'name'))
                    yield '\n'
                l_2_access_list = missing
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'report_interval')):
                pass
                yield '   '
                yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                yield ' report-interval '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'report_interval'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'version')):
                pass
                yield '   '
                yield str((undefined(name='host_proxy_cli') if l_1_host_proxy_cli is missing else l_1_host_proxy_cli))
                yield ' version '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_igmp_host_proxy'), 'version'))
                yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_enable'), True):
            pass
            yield '   ipv6 enable\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_address')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_address'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_address_link_local')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_address_link_local'))
            yield ' link-local\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_ra_disabled'), True):
            pass
            yield '   ipv6 nd ra disabled\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_managed_config_flag'), True):
            pass
            yield '   ipv6 nd managed-config-flag\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_prefixes')):
            pass
            for l_2_prefix in environment.getattr(l_1_ethernet_interface, 'ipv6_nd_prefixes'):
                l_2_ipv6_nd_prefix_cli = missing
                _loop_vars = {}
                pass
                l_2_ipv6_nd_prefix_cli = str_join(('ipv6 nd prefix ', environment.getattr(l_2_prefix, 'ipv6_prefix'), ))
                _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                if t_10(environment.getattr(l_2_prefix, 'valid_lifetime')):
                    pass
                    l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'valid_lifetime'), ))
                    _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                    if t_10(environment.getattr(l_2_prefix, 'preferred_lifetime')):
                        pass
                        l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'preferred_lifetime'), ))
                        _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                if t_10(environment.getattr(l_2_prefix, 'no_autoconfig_flag'), True):
                    pass
                    l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' no-autoconfig', ))
                    _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                yield '   '
                yield str((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli))
                yield '\n'
            l_2_prefix = l_2_ipv6_nd_prefix_cli = missing
        if (t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv4_segment_size')) or t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv6_segment_size'))):
            pass
            l_1_tcp_mss_ceiling_cli = 'tcp mss ceiling'
            _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv4_segment_size')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv4 ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv4_segment_size'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv6_segment_size')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ipv6 ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'ipv6_segment_size'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'direction')):
                pass
                l_1_tcp_mss_ceiling_cli = str_join(((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli), ' ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'tcp_mss_ceiling'), 'direction'), ))
                _loop_vars['tcp_mss_ceiling_cli'] = l_1_tcp_mss_ceiling_cli
            yield '   '
            yield str((undefined(name='tcp_mss_ceiling_cli') if l_1_tcp_mss_ceiling_cli is missing else l_1_tcp_mss_ceiling_cli))
            yield '\n'
        if (t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')) and t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'mode'))):
            pass
            yield '   channel-group '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'))
            yield ' mode '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'mode'))
            yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'mode')):
                pass
                yield '   lacp timer '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'mode'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'multiplier')):
                pass
                yield '   lacp timer multiplier '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'multiplier'))
                yield '\n'
            if t_10(environment.getattr(l_1_ethernet_interface, 'lacp_port_priority')):
                pass
                yield '   lacp port-priority '
                yield str(environment.getattr(l_1_ethernet_interface, 'lacp_port_priority'))
                yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'access_group_in')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'access_group_in'))
            yield ' in\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'access_group_out')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'access_group_out'))
            yield ' out\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_in')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_in'))
            yield ' in\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_out')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_out'))
            yield ' out\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mac_access_group_in')):
            pass
            yield '   mac access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'mac_access_group_in'))
            yield ' in\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'mac_access_group_out')):
            pass
            yield '   mac access-group '
            yield str(environment.getattr(l_1_ethernet_interface, 'mac_access_group_out'))
            yield ' out\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'igp_sync'), True):
            pass
            yield '   mpls ldp igp sync\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'interface'), True):
            pass
            yield '   mpls ldp interface\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'interface'), False):
            pass
            yield '   no mpls ldp interface\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'transmit'), False):
            pass
            yield '   no lldp transmit\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'receive'), False):
            pass
            yield '   no lldp receive\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'ztp_vlan')):
            pass
            yield '   lldp tlv transmit ztp vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'ztp_vlan'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mac_security'), 'profile')):
            pass
            yield '   mac security profile '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mac_security'), 'profile'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'multicast')):
            pass
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'boundaries')):
                pass
                for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'boundaries'):
                    l_2_boundary_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_boundary_cli = str_join(('multicast ipv4 boundary ', environment.getattr(l_2_boundary, 'boundary'), ))
                    _loop_vars['boundary_cli'] = l_2_boundary_cli
                    if t_10(environment.getattr(l_2_boundary, 'out'), True):
                        pass
                        l_2_boundary_cli = str_join(((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli), ' out', ))
                        _loop_vars['boundary_cli'] = l_2_boundary_cli
                    yield '   '
                    yield str((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli))
                    yield '\n'
                l_2_boundary = l_2_boundary_cli = missing
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'boundaries')):
                pass
                for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'boundaries'):
                    _loop_vars = {}
                    pass
                    yield '   multicast ipv6 boundary '
                    yield str(environment.getattr(l_2_boundary, 'boundary'))
                    yield ' out\n'
                l_2_boundary = missing
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'static'), True):
                pass
                yield '   multicast ipv4 static\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'static'), True):
                pass
                yield '   multicast ipv6 static\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ip'), True):
            pass
            yield '   mpls ip\n'
        elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ip'), False):
            pass
            yield '   no mpls ip\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ip_nat')):
            pass
            l_1_interface_ip_nat = environment.getattr(l_1_ethernet_interface, 'ip_nat')
            _loop_vars['interface_ip_nat'] = l_1_interface_ip_nat
            template = environment.get_template('eos/interface-ip-nat.j2', 'eos/ethernet-interfaces.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'aaa_config': l_1_aaa_config, 'actions': l_1_actions, 'address_locking_cli': l_1_address_locking_cli, 'auth_cli': l_1_auth_cli, 'auth_failure_fallback_mba': l_1_auth_failure_fallback_mba, 'backup_link_cli': l_1_backup_link_cli, 'both_key_ids': l_1_both_key_ids, 'client_encapsulation': l_1_client_encapsulation, 'dfe_algo_cli': l_1_dfe_algo_cli, 'dfe_hold_time_cli': l_1_dfe_hold_time_cli, 'encapsulation_cli': l_1_encapsulation_cli, 'encapsulation_dot1q_cli': l_1_encapsulation_dot1q_cli, 'ethernet_interface': l_1_ethernet_interface, 'frequency_cli': l_1_frequency_cli, 'host_mode_cli': l_1_host_mode_cli, 'host_proxy_cli': l_1_host_proxy_cli, 'interface_ip_nat': l_1_interface_ip_nat, 'isis_auth_cli': l_1_isis_auth_cli, 'network_encapsulation': l_1_network_encapsulation, 'network_flag': l_1_network_flag, 'poe_limit_cli': l_1_poe_limit_cli, 'poe_link_down_action_cli': l_1_poe_link_down_action_cli, 'sorted_vlans_cli': l_1_sorted_vlans_cli, 'tcp_mss_ceiling_cli': l_1_tcp_mss_ceiling_cli, 'POE_CLASS_MAP': l_0_POE_CLASS_MAP})):
                yield event
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_nat'), 'service_profile')):
                pass
                yield '   ip nat service-profile '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ip_nat'), 'service_profile'))
                yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ospf_cost')):
            pass
            yield '   ip ospf cost '
            yield str(environment.getattr(l_1_ethernet_interface, 'ospf_cost'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ospf_network_point_to_point'), True):
            pass
            yield '   ip ospf network point-to-point\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ospf_authentication'), 'simple'):
            pass
            yield '   ip ospf authentication\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'ospf_authentication'), 'message-digest'):
            pass
            yield '   ip ospf authentication message-digest\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ospf_authentication_key')):
            pass
            yield '   ip ospf authentication-key 7 '
            yield str(t_2(environment.getattr(l_1_ethernet_interface, 'ospf_authentication_key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'ospf_area')):
            pass
            yield '   ip ospf area '
            yield str(environment.getattr(l_1_ethernet_interface, 'ospf_area'))
            yield '\n'
        for l_2_ospf_message_digest_key in t_3(environment.getattr(l_1_ethernet_interface, 'ospf_message_digest_keys'), 'id'):
            _loop_vars = {}
            pass
            if (t_10(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm')) and t_10(environment.getattr(l_2_ospf_message_digest_key, 'key'))):
                pass
                yield '   ip ospf message-digest-key '
                yield str(environment.getattr(l_2_ospf_message_digest_key, 'id'))
                yield ' '
                yield str(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm'))
                yield ' 7 '
                yield str(t_2(environment.getattr(l_2_ospf_message_digest_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
        l_2_ospf_message_digest_key = missing
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'pbr'), 'input')):
            pass
            yield '   service-policy type pbr input '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'pbr'), 'input'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
            pass
            yield '   pim ipv4 sparse-mode\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'bidirectional'), True):
            pass
            yield '   pim ipv4 bidirectional\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'border_router'), True):
            pass
            yield '   pim ipv4 border-router\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'hello'), 'interval')):
            pass
            yield '   pim ipv4 hello interval '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'hello'), 'interval'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'hello'), 'count')):
            pass
            yield '   pim ipv4 hello count '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'hello'), 'count'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'dr_priority')):
            pass
            yield '   pim ipv4 dr-priority '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'dr_priority'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'bfd'), True):
            pass
            yield '   pim ipv4 bfd\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'priority')):
            pass
            yield '   poe priority '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'priority'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'reboot'), 'action')):
            pass
            yield '   poe reboot action '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'reboot'), 'action'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'action')):
            pass
            l_1_poe_link_down_action_cli = str_join(('poe link down action ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'action'), ))
            _loop_vars['poe_link_down_action_cli'] = l_1_poe_link_down_action_cli
            if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'power_off_delay')) and (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'action') == 'power-off')):
                pass
                l_1_poe_link_down_action_cli = str_join(((undefined(name='poe_link_down_action_cli') if l_1_poe_link_down_action_cli is missing else l_1_poe_link_down_action_cli), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'power_off_delay'), ' seconds', ))
                _loop_vars['poe_link_down_action_cli'] = l_1_poe_link_down_action_cli
            yield '   '
            yield str((undefined(name='poe_link_down_action_cli') if l_1_poe_link_down_action_cli is missing else l_1_poe_link_down_action_cli))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'shutdown'), 'action')):
            pass
            yield '   poe shutdown action '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'shutdown'), 'action'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'disabled'), True):
            pass
            yield '   poe disabled\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit')):
            pass
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'class')):
                pass
                l_1_poe_limit_cli = str_join(('poe limit ', environment.getitem((undefined(name='POE_CLASS_MAP') if l_0_POE_CLASS_MAP is missing else l_0_POE_CLASS_MAP), environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'class')), ' watts', ))
                _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
            elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'watts')):
                pass
                l_1_poe_limit_cli = str_join(('poe limit ', t_6('%.2f', t_5(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'watts'))), ' watts', ))
                _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
            if (t_10((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli)) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'fixed'), True)):
                pass
                l_1_poe_limit_cli = str_join(((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli), ' fixed', ))
                _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
            yield '   '
            yield str((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'negotiation_lldp'), False):
            pass
            yield '   poe negotiation lldp disabled\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'legacy_detect'), True):
            pass
            yield '   poe legacy detect\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security')):
            pass
            if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'enabled'), True) or t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'violation'), 'mode'), 'shutdown')):
                pass
                yield '   switchport port-security\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'violation'), 'mode'), 'protect'):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'violation'), 'protect_log'), True):
                    pass
                    yield '   switchport port-security violation protect log\n'
                else:
                    pass
                    yield '   switchport port-security violation protect\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'mac_address_maximum'), 'disabled'), True):
                pass
                yield '   switchport port-security mac-address maximum disabled\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'mac_address_maximum'), 'disabled'), False):
                pass
                yield '   no switchport port-security mac-address maximum disabled\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'mac_address_maximum'), 'limit')):
                pass
                yield '   switchport port-security mac-address maximum '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'mac_address_maximum'), 'limit'))
                yield '\n'
            if (not t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'violation'), 'mode'), 'protect')):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'vlans')):
                    pass
                    l_1_sorted_vlans_cli = []
                    _loop_vars['sorted_vlans_cli'] = l_1_sorted_vlans_cli
                    for l_2_vlan in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'vlans'):
                        _loop_vars = {}
                        pass
                        if (t_10(environment.getattr(l_2_vlan, 'range')) and t_10(environment.getattr(l_2_vlan, 'mac_address_maximum'))):
                            pass
                            for l_3_id in t_4(environment.getattr(l_2_vlan, 'range')):
                                l_3_port_sec_cli = missing
                                _loop_vars = {}
                                pass
                                l_3_port_sec_cli = str_join(('switchport port-security vlan ', l_3_id, ' mac-address maximum ', environment.getattr(l_2_vlan, 'mac_address_maximum'), ))
                                _loop_vars['port_sec_cli'] = l_3_port_sec_cli
                                context.call(environment.getattr((undefined(name='sorted_vlans_cli') if l_1_sorted_vlans_cli is missing else l_1_sorted_vlans_cli), 'append'), (undefined(name='port_sec_cli') if l_3_port_sec_cli is missing else l_3_port_sec_cli), _loop_vars=_loop_vars)
                            l_3_id = l_3_port_sec_cli = missing
                    l_2_vlan = missing
                    for l_2_vlan_cli in t_3((undefined(name='sorted_vlans_cli') if l_1_sorted_vlans_cli is missing else l_1_sorted_vlans_cli)):
                        _loop_vars = {}
                        pass
                        yield '   '
                        yield str(l_2_vlan_cli)
                        yield '\n'
                    l_2_vlan_cli = missing
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'vlan_default_mac_address_maximum')):
                    pass
                    yield '   switchport port-security vlan default mac-address maximum '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'port_security'), 'vlan_default_mac_address_maximum'))
                    yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'enable'), True):
            pass
            yield '   ptp enable\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'interval')):
            pass
            yield '   ptp announce interval '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'interval'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'timeout')):
            pass
            yield '   ptp announce timeout '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'timeout'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_mechanism')):
            pass
            yield '   ptp delay-mechanism '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_mechanism'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_req')):
            pass
            yield '   ptp delay-req interval '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_req'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'profile'), 'g8275_1'), 'destination_mac_address')):
            pass
            yield '   ptp profile g8275.1 destination mac-address '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'profile'), 'g8275_1'), 'destination_mac_address'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'role')):
            pass
            yield '   ptp role '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'role'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'sync_message'), 'interval')):
            pass
            yield '   ptp sync-message interval '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'sync_message'), 'interval'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'transport')):
            pass
            yield '   ptp transport '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'transport'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'vlan')):
            pass
            yield '   ptp vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'vlan'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'qos'), 'input')):
            pass
            yield '   service-policy type qos input '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'qos'), 'input'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'service_profile')):
            pass
            yield '   service-profile '
            yield str(environment.getattr(l_1_ethernet_interface, 'service_profile'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust')):
            pass
            if (environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust') == 'disabled'):
                pass
                yield '   no qos trust\n'
            else:
                pass
                yield '   qos trust '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'cos')):
            pass
            yield '   qos cos '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'cos'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'dscp')):
            pass
            yield '   qos dscp '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'dscp'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'shape'), 'rate')):
            pass
            yield '   shape rate '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'shape'), 'rate'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'enabled'), True):
            pass
            yield '   priority-flow-control on\n'
        elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'enabled'), False):
            pass
            yield '   no priority-flow-control\n'
        for l_2_priority_block in t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'priorities')):
            _loop_vars = {}
            pass
            if t_10(environment.getattr(l_2_priority_block, 'priority')):
                pass
                if t_10(environment.getattr(l_2_priority_block, 'no_drop'), True):
                    pass
                    yield '   priority-flow-control priority '
                    yield str(environment.getattr(l_2_priority_block, 'priority'))
                    yield ' no-drop\n'
                elif t_10(environment.getattr(l_2_priority_block, 'no_drop'), False):
                    pass
                    yield '   priority-flow-control priority '
                    yield str(environment.getattr(l_2_priority_block, 'priority'))
                    yield ' drop\n'
        l_2_priority_block = missing
        for l_2_tx_queue in t_3(environment.getattr(l_1_ethernet_interface, 'tx_queues'), 'id'):
            _loop_vars = {}
            pass
            template = environment.get_template('eos/ethernet-interface-tx-queues.j2', 'eos/ethernet-interfaces.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'tx_queue': l_2_tx_queue, 'aaa_config': l_1_aaa_config, 'actions': l_1_actions, 'address_locking_cli': l_1_address_locking_cli, 'auth_cli': l_1_auth_cli, 'auth_failure_fallback_mba': l_1_auth_failure_fallback_mba, 'backup_link_cli': l_1_backup_link_cli, 'both_key_ids': l_1_both_key_ids, 'client_encapsulation': l_1_client_encapsulation, 'dfe_algo_cli': l_1_dfe_algo_cli, 'dfe_hold_time_cli': l_1_dfe_hold_time_cli, 'encapsulation_cli': l_1_encapsulation_cli, 'encapsulation_dot1q_cli': l_1_encapsulation_dot1q_cli, 'ethernet_interface': l_1_ethernet_interface, 'frequency_cli': l_1_frequency_cli, 'host_mode_cli': l_1_host_mode_cli, 'host_proxy_cli': l_1_host_proxy_cli, 'interface_ip_nat': l_1_interface_ip_nat, 'isis_auth_cli': l_1_isis_auth_cli, 'network_encapsulation': l_1_network_encapsulation, 'network_flag': l_1_network_flag, 'poe_limit_cli': l_1_poe_limit_cli, 'poe_link_down_action_cli': l_1_poe_link_down_action_cli, 'sorted_vlans_cli': l_1_sorted_vlans_cli, 'tcp_mss_ceiling_cli': l_1_tcp_mss_ceiling_cli, 'POE_CLASS_MAP': l_0_POE_CLASS_MAP})):
                yield event
        l_2_tx_queue = missing
        for l_2_uc_tx_queue in t_3(environment.getattr(l_1_ethernet_interface, 'uc_tx_queues'), 'id'):
            _loop_vars = {}
            pass
            template = environment.get_template('eos/ethernet-interface-uc-tx-queues.j2', 'eos/ethernet-interfaces.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'uc_tx_queue': l_2_uc_tx_queue, 'aaa_config': l_1_aaa_config, 'actions': l_1_actions, 'address_locking_cli': l_1_address_locking_cli, 'auth_cli': l_1_auth_cli, 'auth_failure_fallback_mba': l_1_auth_failure_fallback_mba, 'backup_link_cli': l_1_backup_link_cli, 'both_key_ids': l_1_both_key_ids, 'client_encapsulation': l_1_client_encapsulation, 'dfe_algo_cli': l_1_dfe_algo_cli, 'dfe_hold_time_cli': l_1_dfe_hold_time_cli, 'encapsulation_cli': l_1_encapsulation_cli, 'encapsulation_dot1q_cli': l_1_encapsulation_dot1q_cli, 'ethernet_interface': l_1_ethernet_interface, 'frequency_cli': l_1_frequency_cli, 'host_mode_cli': l_1_host_mode_cli, 'host_proxy_cli': l_1_host_proxy_cli, 'interface_ip_nat': l_1_interface_ip_nat, 'isis_auth_cli': l_1_isis_auth_cli, 'network_encapsulation': l_1_network_encapsulation, 'network_flag': l_1_network_flag, 'poe_limit_cli': l_1_poe_limit_cli, 'poe_link_down_action_cli': l_1_poe_link_down_action_cli, 'sorted_vlans_cli': l_1_sorted_vlans_cli, 'tcp_mss_ceiling_cli': l_1_tcp_mss_ceiling_cli, 'POE_CLASS_MAP': l_0_POE_CLASS_MAP})):
                yield event
        l_2_uc_tx_queue = missing
        if t_10(environment.getattr(l_1_ethernet_interface, 'sflow')):
            pass
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'enable'), True):
                pass
                yield '   sflow enable\n'
            elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'enable'), False):
                pass
                yield '   no sflow enable\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'enable'), True):
                pass
                yield '   sflow egress enable\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'enable'), False):
                pass
                yield '   no sflow egress enable\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'unmodified_enable'), True):
                pass
                yield '   sflow egress unmodified enable\n'
            elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'unmodified_enable'), False):
                pass
                yield '   no sflow egress unmodified enable\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_enable')):
            pass
            yield '   isis enable '
            yield str(environment.getattr(l_1_ethernet_interface, 'isis_enable'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_bfd'), True):
            pass
            yield '   isis bfd\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type')):
            pass
            yield '   isis circuit-type '
            yield str(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_metric')):
            pass
            yield '   isis metric '
            yield str(environment.getattr(l_1_ethernet_interface, 'isis_metric'))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_passive'), True):
            pass
            yield '   isis passive\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'), False):
            pass
            yield '   no isis hello padding\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'), True):
            pass
            yield '   isis hello padding\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_network_point_to_point'), True):
            pass
            yield '   isis network point-to-point\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'isis_authentication')):
            pass
            if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode') == 'sha') and t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'sha'), 'key_id')))) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode') == 'shared-secret') and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'shared_secret'))))):
                pass
                l_1_isis_auth_cli = str_join(('isis authentication mode ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode'), ))
                _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                if (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode') == 'sha'):
                    pass
                    l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'sha'), 'key_id'), ))
                    _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                elif (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'mode') == 'shared-secret'):
                    pass
                    l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'shared_secret'), 'profile'), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'shared_secret'), 'algorithm'), ))
                    _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'rx_disabled'), True):
                    pass
                    l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' rx-disabled', ))
                    _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                yield '   '
                yield str((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli))
                yield '\n'
            else:
                pass
                if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode') == 'sha') and t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'sha'), 'key_id')))) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode') == 'shared-secret') and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'shared_secret'))))):
                    pass
                    l_1_isis_auth_cli = str_join(('isis authentication mode ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode'), ))
                    _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    if (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode') == 'sha'):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'sha'), 'key_id'), ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    elif (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'mode') == 'shared-secret'):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'shared_secret'), 'profile'), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'shared_secret'), 'algorithm'), ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'rx_disabled'), True):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' rx-disabled', ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    yield '   '
                    yield str((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli))
                    yield ' level-1\n'
                if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode')) and (((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode') in ['md5', 'text']) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode') == 'sha') and t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'sha'), 'key_id')))) or ((environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode') == 'shared-secret') and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'shared_secret'))))):
                    pass
                    l_1_isis_auth_cli = str_join(('isis authentication mode ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode'), ))
                    _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    if (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode') == 'sha'):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' key-id ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'sha'), 'key_id'), ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    elif (environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'mode') == 'shared-secret'):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' profile ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'shared_secret'), 'profile'), ' algorithm ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'shared_secret'), 'algorithm'), ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'rx_disabled'), True):
                        pass
                        l_1_isis_auth_cli = str_join(((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli), ' rx-disabled', ))
                        _loop_vars['isis_auth_cli'] = l_1_isis_auth_cli
                    yield '   '
                    yield str((undefined(name='isis_auth_cli') if l_1_isis_auth_cli is missing else l_1_isis_auth_cli))
                    yield ' level-2\n'
            l_1_both_key_ids = []
            _loop_vars['both_key_ids'] = l_1_both_key_ids
            for l_2_auth_key in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'key_ids'), 'id'):
                _loop_vars = {}
                pass
                context.call(environment.getattr((undefined(name='both_key_ids') if l_1_both_key_ids is missing else l_1_both_key_ids), 'append'), environment.getattr(l_2_auth_key, 'id'), _loop_vars=_loop_vars)
                if t_10(environment.getattr(l_2_auth_key, 'rfc_5310'), True):
                    pass
                    yield '   isis authentication key-id '
                    yield str(environment.getattr(l_2_auth_key, 'id'))
                    yield ' algorithm '
                    yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                    yield ' rfc-5310 key '
                    yield str(environment.getattr(l_2_auth_key, 'key_type'))
                    yield ' '
                    yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                    yield '\n'
                else:
                    pass
                    yield '   isis authentication key-id '
                    yield str(environment.getattr(l_2_auth_key, 'id'))
                    yield ' algorithm '
                    yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                    yield ' key '
                    yield str(environment.getattr(l_2_auth_key, 'key_type'))
                    yield ' '
                    yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                    yield '\n'
            l_2_auth_key = missing
            for l_2_auth_key in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'key_ids'), 'id'):
                _loop_vars = {}
                pass
                if (environment.getattr(l_2_auth_key, 'id') not in (undefined(name='both_key_ids') if l_1_both_key_ids is missing else l_1_both_key_ids)):
                    pass
                    if t_10(environment.getattr(l_2_auth_key, 'rfc_5310'), True):
                        pass
                        yield '   isis authentication key-id '
                        yield str(environment.getattr(l_2_auth_key, 'id'))
                        yield ' algorithm '
                        yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                        yield ' rfc-5310 key '
                        yield str(environment.getattr(l_2_auth_key, 'key_type'))
                        yield ' '
                        yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                        yield ' level-1\n'
                    else:
                        pass
                        yield '   isis authentication key-id '
                        yield str(environment.getattr(l_2_auth_key, 'id'))
                        yield ' algorithm '
                        yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                        yield ' key '
                        yield str(environment.getattr(l_2_auth_key, 'key_type'))
                        yield ' '
                        yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                        yield ' level-1\n'
            l_2_auth_key = missing
            for l_2_auth_key in t_3(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'key_ids'), 'id'):
                _loop_vars = {}
                pass
                if (environment.getattr(l_2_auth_key, 'id') not in (undefined(name='both_key_ids') if l_1_both_key_ids is missing else l_1_both_key_ids)):
                    pass
                    if t_10(environment.getattr(l_2_auth_key, 'rfc_5310'), True):
                        pass
                        yield '   isis authentication key-id '
                        yield str(environment.getattr(l_2_auth_key, 'id'))
                        yield ' algorithm '
                        yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                        yield ' rfc-5310 key '
                        yield str(environment.getattr(l_2_auth_key, 'key_type'))
                        yield ' '
                        yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                        yield ' level-2\n'
                    else:
                        pass
                        yield '   isis authentication key-id '
                        yield str(environment.getattr(l_2_auth_key, 'id'))
                        yield ' algorithm '
                        yield str(environment.getattr(l_2_auth_key, 'algorithm'))
                        yield ' key '
                        yield str(environment.getattr(l_2_auth_key, 'key_type'))
                        yield ' '
                        yield str(t_2(environment.getattr(l_2_auth_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                        yield ' level-2\n'
            l_2_auth_key = missing
            if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'key_type')) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'key'))):
                pass
                yield '   isis authentication key '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'key_type'))
                yield ' '
                yield str(t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'both'), 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
            else:
                pass
                if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'key_type')) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'key'))):
                    pass
                    yield '   isis authentication key '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'key_type'))
                    yield ' '
                    yield str(t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_1'), 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                    yield ' level-1\n'
                if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'key_type')) and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'key'))):
                    pass
                    yield '   isis authentication key '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'key_type'))
                    yield ' '
                    yield str(t_2(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'isis_authentication'), 'level_2'), 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                    yield ' level-2\n'
        else:
            pass
            if (t_10(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode')) and (environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode') in ['text', 'md5'])):
                pass
                yield '   isis authentication mode '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode'))
                yield '\n'
            if t_10(environment.getattr(l_1_ethernet_interface, 'isis_authentication_key')):
                pass
                yield '   isis authentication key 7 '
                yield str(t_2(environment.getattr(l_1_ethernet_interface, 'isis_authentication_key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
        for l_2_section in t_3(environment.getattr(l_1_ethernet_interface, 'storm_control')):
            _loop_vars = {}
            pass
            if (t_10(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level')) and (l_2_section != 'all')):
                pass
                if t_10(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'unit'), 'pps'):
                    pass
                    yield '   storm-control '
                    yield str(t_8(context.eval_ctx, l_2_section, '_', '-'))
                    yield ' level pps '
                    yield str(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level'))
                    yield '\n'
                else:
                    pass
                    yield '   storm-control '
                    yield str(t_8(context.eval_ctx, l_2_section, '_', '-'))
                    yield ' level '
                    yield str(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level'))
                    yield '\n'
        l_2_section = missing
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'storm_control'), 'all'), 'level')):
            pass
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'storm_control'), 'all'), 'unit'), 'pps'):
                pass
                yield '   storm-control all level pps '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'storm_control'), 'all'), 'level'))
                yield '\n'
            else:
                pass
                yield '   storm-control all level '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'storm_control'), 'all'), 'level'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'storm_control_discards'), True):
            pass
            yield '   logging event storm-control discards\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'storm_control_discards'), False):
            pass
            yield '   no logging event storm-control discards\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_portfast'), 'edge'):
            pass
            yield '   spanning-tree portfast\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_portfast'), 'network'):
            pass
            yield '   spanning-tree portfast network\n'
        if (t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard')) and (environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard') in [True, 'True', 'enabled'])):
            pass
            yield '   spanning-tree bpduguard enable\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard'), 'disabled'):
            pass
            yield '   spanning-tree bpduguard disable\n'
        if (t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter')) and (environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter') in [True, 'True', 'enabled'])):
            pass
            yield '   spanning-tree bpdufilter enable\n'
        elif t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter'), 'disabled'):
            pass
            yield '   spanning-tree bpdufilter disable\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard')):
            pass
            if (environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard') == 'disabled'):
                pass
                yield '   spanning-tree guard none\n'
            else:
                pass
                yield '   spanning-tree guard '
                yield str(environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'spanning_tree'), True):
            pass
            yield '   logging event spanning-tree\n'
        elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'spanning_tree'), False):
            pass
            yield '   no logging event spanning-tree\n'
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup_link'), 'interface')):
            pass
            l_1_backup_link_cli = str_join(('switchport backup-link ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup_link'), 'interface'), ))
            _loop_vars['backup_link_cli'] = l_1_backup_link_cli
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup_link'), 'prefer_vlan')):
                pass
                l_1_backup_link_cli = str_join(((undefined(name='backup_link_cli') if l_1_backup_link_cli is missing else l_1_backup_link_cli), ' prefer vlan ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup_link'), 'prefer_vlan'), ))
                _loop_vars['backup_link_cli'] = l_1_backup_link_cli
            yield '   '
            yield str((undefined(name='backup_link_cli') if l_1_backup_link_cli is missing else l_1_backup_link_cli))
            yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'preemption_delay')):
                pass
                yield '   switchport backup preemption-delay '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'preemption_delay'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'mac_move_burst')):
                pass
                yield '   switchport backup mac-move-burst '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'mac_move_burst'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'mac_move_burst_interval')):
                pass
                yield '   switchport backup mac-move-burst-interval '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'mac_move_burst_interval'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'initial_mac_move_delay')):
                pass
                yield '   switchport backup initial-mac-move-delay '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'initial_mac_move_delay'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'dest_macaddr')):
                pass
                yield '   switchport backup dest-macaddr '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'switchport'), 'backup'), 'dest_macaddr'))
                yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sync_e'), 'enable'), True):
            pass
            yield '   !\n   sync-e\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sync_e'), 'priority')):
                pass
                yield '      priority '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sync_e'), 'priority'))
                yield '\n'
        for l_2_link_tracking_group in t_3(environment.getattr(l_1_ethernet_interface, 'link_tracking_groups')):
            _loop_vars = {}
            pass
            if (t_10(environment.getattr(l_2_link_tracking_group, 'name')) and t_10(environment.getattr(l_2_link_tracking_group, 'direction'))):
                pass
                yield '   link tracking group '
                yield str(environment.getattr(l_2_link_tracking_group, 'name'))
                yield ' '
                yield str(environment.getattr(l_2_link_tracking_group, 'direction'))
                yield '\n'
        l_2_link_tracking_group = missing
        if (t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'link_tracking'), 'direction')) and t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'link_tracking'), 'groups'))):
            pass
            for l_2_group_name in environment.getattr(environment.getattr(l_1_ethernet_interface, 'link_tracking'), 'groups'):
                _loop_vars = {}
                pass
                yield '   link tracking group '
                yield str(l_2_group_name)
                yield ' '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'link_tracking'), 'direction'))
                yield '\n'
            l_2_group_name = missing
        if t_10(environment.getattr(l_1_ethernet_interface, 'vmtracer'), True):
            pass
            yield '   vmtracer vmware-esx\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'vrrp_ids')):
            pass
            def t_11(fiter):
                for l_2_vrid in fiter:
                    if t_10(environment.getattr(l_2_vrid, 'id')):
                        yield l_2_vrid
            for l_2_vrid in t_11(t_3(environment.getattr(l_1_ethernet_interface, 'vrrp_ids'), 'id')):
                l_2_delay_cli = resolve('delay_cli')
                _loop_vars = {}
                pass
                if t_10(environment.getattr(l_2_vrid, 'priority_level')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' priority-level '
                    yield str(environment.getattr(l_2_vrid, 'priority_level'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' advertisement interval '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval'))
                    yield '\n'
                if (t_10(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), True) and (t_10(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum')) or t_10(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload')))):
                    pass
                    l_2_delay_cli = str_join(('vrrp ', environment.getattr(l_2_vrid, 'id'), ' preempt delay', ))
                    _loop_vars['delay_cli'] = l_2_delay_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum')):
                        pass
                        l_2_delay_cli = str_join(((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli), ' minimum ', environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum'), ))
                        _loop_vars['delay_cli'] = l_2_delay_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload')):
                        pass
                        l_2_delay_cli = str_join(((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli), ' reload ', environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload'), ))
                        _loop_vars['delay_cli'] = l_2_delay_cli
                    yield '   '
                    yield str((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli))
                    yield '\n'
                elif t_10(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), False):
                    pass
                    yield '   no vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' preempt\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'timers'), 'delay'), 'reload')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' timers delay reload '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'timers'), 'delay'), 'reload'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv4 '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv4 version '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv6 '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address'))
                    yield '\n'
                for l_3_tracked_obj in t_3(environment.getattr(l_2_vrid, 'tracked_object'), 'name'):
                    l_3_tracked_obj_cli = resolve('tracked_obj_cli')
                    _loop_vars = {}
                    pass
                    if t_10(environment.getattr(l_3_tracked_obj, 'name')):
                        pass
                        l_3_tracked_obj_cli = str_join(('vrrp ', environment.getattr(l_2_vrid, 'id'), ' tracked-object ', environment.getattr(l_3_tracked_obj, 'name'), ))
                        _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        if t_10(environment.getattr(l_3_tracked_obj, 'decrement')):
                            pass
                            l_3_tracked_obj_cli = str_join(((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli), ' decrement ', environment.getattr(l_3_tracked_obj, 'decrement'), ))
                            _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        elif t_10(environment.getattr(l_3_tracked_obj, 'shutdown'), True):
                            pass
                            l_3_tracked_obj_cli = str_join(((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli), ' shutdown', ))
                            _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        yield '   '
                        yield str((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli))
                        yield '\n'
                l_3_tracked_obj = l_3_tracked_obj_cli = missing
            l_2_vrid = l_2_delay_cli = missing
        if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'media'), 'override')):
            pass
            yield '   transceiver media override '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'media'), 'override'))
            yield '\n'
        if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'frequency')):
            pass
            l_1_frequency_cli = str_join(('transceiver frequency ', t_6('%.3f', t_5(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'frequency'))), ))
            _loop_vars['frequency_cli'] = l_1_frequency_cli
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'frequency_unit')):
                pass
                l_1_frequency_cli = str_join(((undefined(name='frequency_cli') if l_1_frequency_cli is missing else l_1_frequency_cli), ' ', environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'frequency_unit'), ))
                _loop_vars['frequency_cli'] = l_1_frequency_cli
            yield '   '
            yield str((undefined(name='frequency_cli') if l_1_frequency_cli is missing else l_1_frequency_cli))
            yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'dot1x')):
            pass
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'pae'), 'mode')):
                pass
                yield '   dot1x pae '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'pae'), 'mode'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure')):
                pass
                if (t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'action'), 'allow') and t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'))):
                    pass
                    yield '   dot1x authentication failure action traffic allow vlan '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'))
                    yield '\n'
                elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'action'), 'drop'):
                    pass
                    yield '   dot1x authentication failure action traffic drop\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'aaa'), 'unresponsive')):
                pass
                l_1_aaa_config = 'dot1x aaa unresponsive'
                _loop_vars['aaa_config'] = l_1_aaa_config
                l_1_actions = environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'aaa'), 'unresponsive')
                _loop_vars['actions'] = l_1_actions
                for l_2_action in t_9(environment, (undefined(name='actions') if l_1_actions is missing else l_1_actions), reverse=True):
                    l_2_aaa_action_config = resolve('aaa_action_config')
                    l_2_action_apply_config = resolve('action_apply_config')
                    _loop_vars = {}
                    pass
                    if (l_2_action == 'phone_action'):
                        pass
                        l_2_aaa_action_config = str_join(((undefined(name='aaa_config') if l_1_aaa_config is missing else l_1_aaa_config), ' phone action', ))
                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                    elif (l_2_action == 'action'):
                        pass
                        l_2_aaa_action_config = str_join(((undefined(name='aaa_config') if l_1_aaa_config is missing else l_1_aaa_config), ' action', ))
                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                    if t_10((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config)):
                        pass
                        if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'apply_cached_results'), True):
                            pass
                            l_2_action_apply_config = 'apply cached-results'
                            _loop_vars['action_apply_config'] = l_2_action_apply_config
                            if (t_10(environment.getattr(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'cached_results_timeout'), 'time_duration')) and t_10(environment.getattr(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'cached_results_timeout'), 'time_duration_unit'))):
                                pass
                                l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' ', (undefined(name='action_apply_config') if l_2_action_apply_config is missing else l_2_action_apply_config), ' timeout ', environment.getattr(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'cached_results_timeout'), 'time_duration'), ' ', environment.getattr(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'cached_results_timeout'), 'time_duration_unit'), ))
                                _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                        if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow'), True):
                            pass
                            if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'apply_alternate'), True):
                                pass
                                l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' else traffic allow', ))
                                _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                            else:
                                pass
                                l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' traffic allow', ))
                                _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                        else:
                            pass
                            if (t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan')) and t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list'))):
                                pass
                                if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'apply_alternate'), True):
                                    pass
                                    l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' else traffic allow vlan ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan'), ' access-list ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list'), ))
                                    _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                                else:
                                    pass
                                    l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' traffic allow vlan ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan'), ' access-list ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list'), ))
                                    _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                            else:
                                pass
                                if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan')):
                                    pass
                                    if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'apply_alternate'), True):
                                        pass
                                        l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' else traffic allow vlan ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan'), ))
                                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                                    else:
                                        pass
                                        l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' traffic allow vlan ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_vlan'), ))
                                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                                if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list')):
                                    pass
                                    if t_10(environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'apply_alternate'), True):
                                        pass
                                        l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' else traffic allow access list ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list'), ))
                                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                                    else:
                                        pass
                                        l_2_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config), ' traffic allow access list ', environment.getattr(environment.getitem((undefined(name='actions') if l_1_actions is missing else l_1_actions), l_2_action), 'traffic_allow_access_list'), ))
                                        _loop_vars['aaa_action_config'] = l_2_aaa_action_config
                        yield '   '
                        yield str((undefined(name='aaa_action_config') if l_2_aaa_action_config is missing else l_2_aaa_action_config))
                        yield '\n'
                l_2_action = l_2_aaa_action_config = l_2_action_apply_config = missing
            if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'aaa'), 'unresponsive'), 'eap_response')):
                pass
                yield '   '
                yield str((undefined(name='aaa_config') if l_1_aaa_config is missing else l_1_aaa_config))
                yield ' eap response '
                yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'aaa'), 'unresponsive'), 'eap_response'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthentication'), True):
                pass
                yield '   dot1x reauthentication\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control')):
                pass
                yield '   dot1x port-control '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control_force_authorized_phone'), True):
                pass
                yield '   dot1x port-control force-authorized phone\n'
            elif t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control_force_authorized_phone'), False):
                pass
                yield '   no dot1x port-control force-authorized phone\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode')):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'mode'), 'single-host'):
                    pass
                    yield '   dot1x host-mode single-host\n'
                elif t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'mode'), 'multi-host'):
                    pass
                    l_1_host_mode_cli = 'dot1x host-mode multi-host'
                    _loop_vars['host_mode_cli'] = l_1_host_mode_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'multi_host_authenticated'), True):
                        pass
                        l_1_host_mode_cli = str_join(((undefined(name='host_mode_cli') if l_1_host_mode_cli is missing else l_1_host_mode_cli), ' authenticated', ))
                        _loop_vars['host_mode_cli'] = l_1_host_mode_cli
                    yield '   '
                    yield str((undefined(name='host_mode_cli') if l_1_host_mode_cli is missing else l_1_host_mode_cli))
                    yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'disabled'), True):
                pass
                yield '   dot1x eapol disabled\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_access_list'), True):
                pass
                yield '   dot1x mac based access-list\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'enabled'), True):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'host_mode_common'), True):
                    pass
                    yield '   dot1x mac based authentication host-mode common\n'
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'always'), True):
                        pass
                        yield '   dot1x mac based authentication always\n'
                else:
                    pass
                    l_1_auth_cli = 'dot1x mac based authentication'
                    _loop_vars['auth_cli'] = l_1_auth_cli
                    if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'always'), True):
                        pass
                        l_1_auth_cli = str_join(((undefined(name='auth_cli') if l_1_auth_cli is missing else l_1_auth_cli), ' always', ))
                        _loop_vars['auth_cli'] = l_1_auth_cli
                    yield '   '
                    yield str((undefined(name='auth_cli') if l_1_auth_cli is missing else l_1_auth_cli))
                    yield '\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout')):
                pass
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'quiet_period')):
                    pass
                    yield '   dot1x timeout quiet-period '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'quiet_period'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_timeout_ignore'), True):
                    pass
                    yield '   dot1x timeout reauth-timeout-ignore always\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'tx_period')):
                    pass
                    yield '   dot1x timeout tx-period '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'tx_period'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_period')):
                    pass
                    yield '   dot1x timeout reauth-period '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_period'))
                    yield '\n'
                if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'idle_host')):
                    pass
                    yield '   dot1x timeout idle-host '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'idle_host'))
                    yield ' seconds\n'
            if t_10(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthorization_request_limit')):
                pass
                yield '   dot1x reauthorization request limit '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthorization_request_limit'))
                yield '\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'unauthorized'), 'access_vlan_membership_egress'), True):
                pass
                yield '   dot1x unauthorized access vlan membership egress\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'unauthorized'), 'native_vlan_membership_egress'), True):
                pass
                yield '   dot1x unauthorized native vlan membership egress\n'
            if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'enabled'), True):
                pass
                l_1_auth_failure_fallback_mba = 'dot1x eapol authentication failure fallback mba'
                _loop_vars['auth_failure_fallback_mba'] = l_1_auth_failure_fallback_mba
                if t_10(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'timeout')):
                    pass
                    l_1_auth_failure_fallback_mba = str_join(((undefined(name='auth_failure_fallback_mba') if l_1_auth_failure_fallback_mba is missing else l_1_auth_failure_fallback_mba), ' timeout ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'timeout'), ))
                    _loop_vars['auth_failure_fallback_mba'] = l_1_auth_failure_fallback_mba
                yield '   '
                yield str((undefined(name='auth_failure_fallback_mba') if l_1_auth_failure_fallback_mba is missing else l_1_auth_failure_fallback_mba))
                yield '\n'
        if t_10(environment.getattr(l_1_ethernet_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_7(environment.getattr(l_1_ethernet_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_ethernet_interface = l_1_encapsulation_cli = l_1_encapsulation_dot1q_cli = l_1_client_encapsulation = l_1_network_flag = l_1_network_encapsulation = l_1_dfe_algo_cli = l_1_dfe_hold_time_cli = l_1_address_locking_cli = l_1_host_proxy_cli = l_1_tcp_mss_ceiling_cli = l_1_interface_ip_nat = l_1_hide_passwords = l_1_poe_link_down_action_cli = l_1_poe_limit_cli = l_1_sorted_vlans_cli = l_1_isis_auth_cli = l_1_both_key_ids = l_1_backup_link_cli = l_1_frequency_cli = l_1_aaa_config = l_1_actions = l_1_host_mode_cli = l_1_auth_cli = l_1_auth_failure_fallback_mba = missing

blocks = {}
debug_info = '7=73&8=76&10=104&11=106&12=109&14=111&15=114&17=116&18=119&20=121&21=124&23=126&25=129&28=132&29=135&31=137&32=140&34=142&36=145&39=148&40=151&42=153&43=156&45=158&46=161&48=163&49=166&51=168&52=171&54=173&56=176&59=179&60=182&62=184&65=189&67=192&70=195&72=198&76=201&77=203&78=206&81=208&82=211&84=213&85=215&87=218&88=221&91=223&92=226&94=228&95=231&97=233&99=236&100=239&102=241&103=244&105=246&106=249&108=251&111=254&114=257&115=260&117=262&118=264&119=267&122=269&123=272&125=274&126=277&128=279&129=282&131=284&132=287&134=289&137=292&138=296&140=299&141=303&143=306&145=309&146=311&148=314&150=316&151=319&152=321&153=323&154=325&155=327&156=329&157=331&159=333&160=335&161=337&162=339&163=341&164=343&166=345&167=347&169=349&171=352&173=354&176=357&178=360&181=363&182=365&183=367&184=369&186=372&188=374&189=377&191=379&192=381&193=383&194=385&195=387&196=389&197=391&198=393&199=395&201=399&203=401&204=403&205=405&208=407&209=409&211=411&212=413&213=415&214=417&215=419&216=421&217=423&218=425&219=427&221=431&224=433&225=435&226=437&227=439&231=442&234=444&235=447&237=449&238=453&239=455&240=457&241=459&243=461&244=463&245=466&248=469&249=473&250=475&251=477&252=479&253=481&254=483&255=485&258=487&259=490&261=493&262=495&263=499&264=501&265=503&266=505&267=507&269=509&270=512&273=515&274=517&275=521&276=523&277=525&278=527&279=529&280=531&283=533&284=536&288=539&290=542&293=545&296=548&297=551&299=553&300=556&302=558&303=561&305=563&306=566&308=568&311=571&312=574&314=576&315=579&317=581&318=583&320=586&321=588&322=590&323=592&325=595&327=597&328=599&329=601&330=603&332=606&334=608&336=611&340=614&341=617&343=619&344=622&346=624&347=627&350=629&351=632&353=634&354=637&356=639&358=642&361=645&362=647&363=649&364=651&366=653&367=655&369=658&371=660&372=663&374=665&377=668&378=671&379=673&380=677&383=680&386=683&387=686&389=688&392=691&394=697&396=700&399=703&400=707&401=709&402=711&404=713&405=715&407=718&409=721&410=725&411=727&412=729&414=731&415=733&416=735&417=737&419=739&420=741&422=744&424=747&427=750&430=753&431=755&432=758&433=760&434=762&435=765&436=767&437=769&438=773&441=780&442=782&443=786&446=793&447=796&451=801&452=803&453=807&456=812&457=815&459=819&460=822&463=826&466=829&467=832&469=834&470=837&472=839&475=842&478=845&479=847&480=851&481=853&482=855&483=857&484=859&487=861&488=863&490=866&493=869&494=871&495=873&496=875&498=877&499=879&501=881&502=883&504=886&506=888&507=891&508=895&509=898&511=900&512=903&514=905&515=908&518=910&519=913&521=915&522=918&524=920&525=923&527=925&528=928&530=930&531=933&533=935&534=938&536=940&539=943&541=946&544=949&547=952&550=955&551=958&553=960&554=963&556=965&557=967&558=969&559=973&560=975&561=977&563=980&566=983&567=985&568=989&571=992&574=995&578=998&580=1001&583=1004&584=1006&585=1008&586=1011&587=1014&590=1016&591=1019&593=1021&596=1024&598=1027&601=1030&602=1033&604=1035&605=1038&607=1040&608=1043&609=1046&612=1053&613=1056&615=1058&618=1061&621=1064&624=1067&625=1070&627=1072&628=1075&630=1077&631=1080&633=1082&636=1085&637=1088&639=1090&640=1093&642=1095&643=1097&644=1099&645=1101&647=1104&649=1106&650=1109&652=1111&655=1114&656=1116&657=1118&658=1120&659=1122&661=1124&662=1126&664=1129&666=1131&669=1134&672=1137&673=1139&675=1142&676=1144&682=1150&684=1153&686=1156&687=1159&689=1161&690=1163&691=1165&692=1167&693=1170&694=1172&695=1176&696=1178&700=1181&701=1185&704=1188&705=1191&709=1193&712=1196&713=1199&715=1201&716=1204&718=1206&719=1209&721=1211&722=1214&724=1216&725=1219&727=1221&728=1224&730=1226&731=1229&733=1231&734=1234&736=1236&737=1239&739=1241&740=1244&742=1246&743=1249&745=1251&746=1253&749=1259&752=1261&753=1264&755=1266&756=1269&758=1271&759=1274&761=1276&763=1279&766=1282&767=1285&768=1287&769=1290&770=1292&771=1295&775=1298&776=1301&778=1305&779=1308&781=1312&782=1314&784=1317&787=1320&789=1323&792=1326&794=1329&798=1332&799=1335&801=1337&804=1340&805=1343&807=1345&808=1348&810=1350&813=1353&815=1356&818=1359&821=1362&822=1364&826=1366&827=1368&828=1370&829=1372&830=1374&832=1376&833=1378&835=1381&837=1385&842=1387&843=1389&844=1391&845=1393&846=1395&848=1397&849=1399&851=1402&853=1404&858=1406&859=1408&860=1410&861=1412&862=1414&864=1416&865=1418&867=1421&870=1423&871=1425&872=1428&873=1429&874=1432&876=1443&879=1452&880=1455&881=1457&882=1460&884=1471&888=1480&889=1483&890=1485&891=1488&893=1499&897=1508&898=1511&900=1517&901=1520&903=1524&904=1527&908=1533&910=1536&912=1538&913=1541&916=1543&917=1546&918=1548&919=1551&921=1558&925=1563&926=1565&927=1568&929=1573&932=1575&934=1578&937=1581&939=1584&942=1587&944=1590&947=1593&949=1596&952=1599&953=1601&956=1607&959=1609&961=1612&964=1615&965=1617&966=1619&967=1621&969=1624&970=1626&971=1629&973=1631&974=1634&976=1636&977=1639&979=1641&980=1644&982=1646&983=1649&986=1651&989=1654&990=1657&993=1659&994=1662&995=1665&998=1670&999=1672&1000=1676&1003=1681&1006=1684&1007=1686&1008=1694&1009=1697&1011=1701&1012=1704&1014=1708&1017=1710&1018=1712&1019=1714&1021=1716&1022=1718&1024=1721&1025=1723&1026=1726&1028=1728&1029=1731&1031=1735&1032=1738&1034=1742&1035=1745&1037=1749&1038=1752&1040=1756&1041=1760&1042=1762&1043=1764&1044=1766&1045=1768&1046=1770&1048=1773&1053=1777&1054=1780&1056=1782&1057=1784&1058=1786&1059=1788&1061=1791&1063=1793&1064=1795&1065=1798&1067=1800&1068=1802&1070=1805&1071=1807&1075=1810&1076=1812&1077=1814&1078=1816&1079=1821&1080=1823&1081=1825&1082=1827&1084=1829&1085=1831&1086=1833&1087=1835&1088=1837&1091=1839&1092=1841&1093=1843&1095=1847&1098=1851&1099=1853&1100=1855&1102=1859&1105=1863&1106=1865&1107=1867&1109=1871&1112=1873&1113=1875&1114=1877&1116=1881&1121=1884&1125=1887&1126=1890&1128=1894&1131=1897&1132=1900&1134=1902&1136=1905&1139=1908&1140=1910&1142=1913&1143=1915&1144=1917&1145=1919&1147=1922&1150=1924&1153=1927&1156=1930&1157=1932&1159=1935&1163=1940&1164=1942&1165=1944&1167=1947&1170=1949&1171=1951&1172=1954&1174=1956&1177=1959&1178=1962&1180=1964&1181=1967&1183=1969&1184=1972&1187=1974&1188=1977&1190=1979&1193=1982&1196=1985&1197=1987&1198=1989&1199=1991&1201=1994&1204=1996&1205=1999'