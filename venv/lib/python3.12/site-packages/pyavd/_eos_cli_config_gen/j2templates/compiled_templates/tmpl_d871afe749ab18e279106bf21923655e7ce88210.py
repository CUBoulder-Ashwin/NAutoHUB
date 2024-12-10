from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dot1x.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dot1x = resolve('dot1x')
    l_0_aaa_config = resolve('aaa_config')
    l_0_actions = resolve('actions')
    l_0_captive_portal_cli = resolve('captive_portal_cli')
    l_0_av_pair_lldp = resolve('av_pair_lldp')
    l_0_av_pair_dhcp = resolve('av_pair_dhcp')
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
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x)):
        pass
        if (((((t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')) or t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'))) or t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'))) or t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'))) or t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'))) or t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair_username_format'))):
            pass
            yield 'dot1x\n'
            l_1_loop = missing
            for l_1_profile, l_1_loop in LoopContext(t_3(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'profiles'), 'name'), undefined):
                l_1_hide_passwords = resolve('hide_passwords')
                _loop_vars = {}
                pass
                yield '   supplicant profile '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '\n'
                if t_4(environment.getattr(l_1_profile, 'identity')):
                    pass
                    yield '      identity '
                    yield str(environment.getattr(l_1_profile, 'identity'))
                    yield '\n'
                if t_4(environment.getattr(l_1_profile, 'eap_method')):
                    pass
                    yield '      eap-method '
                    yield str(environment.getattr(l_1_profile, 'eap_method'))
                    yield '\n'
                if t_4(environment.getattr(l_1_profile, 'passphrase')):
                    pass
                    yield '      passphrase '
                    yield str(t_1(environment.getattr(l_1_profile, 'passphrase_type'), '7'))
                    yield ' '
                    yield str(t_2(environment.getattr(l_1_profile, 'passphrase'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                    yield '\n'
                if t_4(environment.getattr(l_1_profile, 'ssl_profile')):
                    pass
                    yield '      ssl profile '
                    yield str(environment.getattr(l_1_profile, 'ssl_profile'))
                    yield '\n'
                if (not environment.getattr(l_1_loop, 'last')):
                    pass
                    yield '   !\n'
            l_1_loop = l_1_profile = l_1_hide_passwords = missing
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive')):
                pass
                l_0_aaa_config = 'aaa unresponsive'
                context.vars['aaa_config'] = l_0_aaa_config
                context.exported_vars.add('aaa_config')
                if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'phone_action')) or t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'action'))):
                    pass
                    l_0_actions = [{'name': 'phone_action', 'config': str_join(((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config), ' phone action', ))}, {'name': 'action', 'config': str_join(((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config), ' action', ))}]
                    context.vars['actions'] = l_0_actions
                    context.exported_vars.add('actions')
                    for l_1_action in (undefined(name='actions') if l_0_actions is missing else l_0_actions):
                        l_1_aaa_action_config = resolve('aaa_action_config')
                        l_1_action_apply_config = resolve('action_apply_config')
                        l_1_traffic = resolve('traffic')
                        _loop_vars = {}
                        pass
                        if t_4(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name'))):
                            pass
                            l_1_aaa_action_config = environment.getattr(l_1_action, 'config')
                            _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                            if ((t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_cached_results'), True) or t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow'), True)) or t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan'))):
                                pass
                                if t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_cached_results'), True):
                                    pass
                                    l_1_action_apply_config = 'apply cached-results'
                                    _loop_vars['action_apply_config'] = l_1_action_apply_config
                                    if (t_4(environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration')) and t_4(environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration_unit'))):
                                        pass
                                        l_1_action_apply_config = str_join(((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ' timeout ', environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration'), ' ', environment.getattr(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'cached_results_timeout'), 'time_duration_unit'), ))
                                        _loop_vars['action_apply_config'] = l_1_action_apply_config
                                if t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow'), True):
                                    pass
                                    l_1_traffic = 'traffic allow'
                                    _loop_vars['traffic'] = l_1_traffic
                                elif t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan')):
                                    pass
                                    l_1_traffic = str_join(('traffic allow vlan ', environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'traffic_allow_vlan'), ))
                                    _loop_vars['traffic'] = l_1_traffic
                                if ((t_4(environment.getattr(environment.getitem(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), environment.getattr(l_1_action, 'name')), 'apply_alternate'), True) and t_4((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config))) and t_4((undefined(name='traffic') if l_1_traffic is missing else l_1_traffic))):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ' else ', (undefined(name='traffic') if l_1_traffic is missing else l_1_traffic), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                elif t_4((undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config)):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='action_apply_config') if l_1_action_apply_config is missing else l_1_action_apply_config), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                elif t_4((undefined(name='traffic') if l_1_traffic is missing else l_1_traffic)):
                                    pass
                                    l_1_aaa_action_config = str_join(((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config), ' ', (undefined(name='traffic') if l_1_traffic is missing else l_1_traffic), ))
                                    _loop_vars['aaa_action_config'] = l_1_aaa_action_config
                                yield '   '
                                yield str((undefined(name='aaa_action_config') if l_1_aaa_action_config is missing else l_1_aaa_action_config))
                                yield '\n'
                    l_1_action = l_1_aaa_action_config = l_1_action_apply_config = l_1_traffic = missing
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'eap_response')):
                    pass
                    yield '   '
                    yield str((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config))
                    yield ' eap response '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'eap_response'))
                    yield '\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'accounting_update_interval')):
                pass
                yield '   aaa accounting update interval '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'accounting_update_interval'))
                yield ' seconds\n'
            if t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')):
                pass
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay')):
                    pass
                    yield '   mac based authentication delay '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay'))
                    yield ' seconds\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period')):
                    pass
                    yield '   mac based authentication hold period '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period'))
                    yield ' seconds\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'service_type'), True):
                pass
                yield '   radius av-pair service-type\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu')):
                pass
                yield '   radius av-pair framed-mtu '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu'))
                yield '\n'
            if (t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair_username_format'), 'delimiter')) and t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair_username_format'), 'mac_string_case'))):
                pass
                yield '   mac-based-auth radius av-pair user-name delimiter '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair_username_format'), 'delimiter'))
                yield ' '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair_username_format'), 'mac_string_case'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'aaa'), 'unresponsive'), 'recovery_action_reauthenticate'), True):
                pass
                yield '   '
                yield str((undefined(name='aaa_config') if l_0_aaa_config is missing else l_0_aaa_config))
                yield ' recovery action reauthenticate\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'disconnect_cached_results_timeout')):
                pass
                yield '   supplicant disconnect cached-results timeout '
                yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'disconnect_cached_results_timeout'))
                yield ' seconds\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'enabled'), True):
                pass
                l_0_captive_portal_cli = 'captive-portal'
                context.vars['captive_portal_cli'] = l_0_captive_portal_cli
                context.exported_vars.add('captive_portal_cli')
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'url')):
                    pass
                    l_0_captive_portal_cli = str_join(((undefined(name='captive_portal_cli') if l_0_captive_portal_cli is missing else l_0_captive_portal_cli), ' url ', environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'url'), ))
                    context.vars['captive_portal_cli'] = l_0_captive_portal_cli
                    context.exported_vars.add('captive_portal_cli')
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'ssl_profile')):
                    pass
                    l_0_captive_portal_cli = str_join(((undefined(name='captive_portal_cli') if l_0_captive_portal_cli is missing else l_0_captive_portal_cli), ' ssl profile ', environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'ssl_profile'), ))
                    context.vars['captive_portal_cli'] = l_0_captive_portal_cli
                    context.exported_vars.add('captive_portal_cli')
                yield '   '
                yield str((undefined(name='captive_portal_cli') if l_0_captive_portal_cli is missing else l_0_captive_portal_cli))
                yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'access_list_ipv4')):
                    pass
                    yield '   captive-portal access-list ipv4 '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'access_list_ipv4'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'start_limit_infinite'), True):
                    pass
                    yield '   captive-portal start limit infinite\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'lldp')):
                pass
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'lldp'), 'system_name'), 'enabled'), True):
                    pass
                    l_0_av_pair_lldp = 'radius av-pair lldp system-name'
                    context.vars['av_pair_lldp'] = l_0_av_pair_lldp
                    context.exported_vars.add('av_pair_lldp')
                    if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'lldp'), 'system_name'), 'auth_only'), True):
                        pass
                        l_0_av_pair_lldp = str_join(((undefined(name='av_pair_lldp') if l_0_av_pair_lldp is missing else l_0_av_pair_lldp), ' auth-only', ))
                        context.vars['av_pair_lldp'] = l_0_av_pair_lldp
                        context.exported_vars.add('av_pair_lldp')
                    yield '   '
                    yield str((undefined(name='av_pair_lldp') if l_0_av_pair_lldp is missing else l_0_av_pair_lldp))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'lldp'), 'system_description'), 'enabled'), True):
                    pass
                    l_0_av_pair_lldp = 'radius av-pair lldp system-description'
                    context.vars['av_pair_lldp'] = l_0_av_pair_lldp
                    context.exported_vars.add('av_pair_lldp')
                    if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'lldp'), 'system_description'), 'auth_only'), True):
                        pass
                        l_0_av_pair_lldp = str_join(((undefined(name='av_pair_lldp') if l_0_av_pair_lldp is missing else l_0_av_pair_lldp), ' auth-only', ))
                        context.vars['av_pair_lldp'] = l_0_av_pair_lldp
                        context.exported_vars.add('av_pair_lldp')
                    yield '   '
                    yield str((undefined(name='av_pair_lldp') if l_0_av_pair_lldp is missing else l_0_av_pair_lldp))
                    yield '\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp')):
                pass
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'hostname'), 'enabled'), True):
                    pass
                    l_0_av_pair_dhcp = 'radius av-pair dhcp hostname'
                    context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                    context.exported_vars.add('av_pair_dhcp')
                    if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'hostname'), 'auth_only'), True):
                        pass
                        l_0_av_pair_dhcp = str_join(((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp), ' auth-only', ))
                        context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                        context.exported_vars.add('av_pair_dhcp')
                    yield '   '
                    yield str((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'parameter_request_list'), 'enabled'), True):
                    pass
                    l_0_av_pair_dhcp = 'radius av-pair dhcp parameter-request-list'
                    context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                    context.exported_vars.add('av_pair_dhcp')
                    if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'parameter_request_list'), 'auth_only'), True):
                        pass
                        l_0_av_pair_dhcp = str_join(((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp), ' auth-only', ))
                        context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                        context.exported_vars.add('av_pair_dhcp')
                    yield '   '
                    yield str((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'vendor_class_id'), 'enabled'), True):
                    pass
                    l_0_av_pair_dhcp = 'radius av-pair dhcp vendor-class-id'
                    context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                    context.exported_vars.add('av_pair_dhcp')
                    if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'dhcp'), 'vendor_class_id'), 'auth_only'), True):
                        pass
                        l_0_av_pair_dhcp = str_join(((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp), ' auth-only', ))
                        context.vars['av_pair_dhcp'] = l_0_av_pair_dhcp
                        context.exported_vars.add('av_pair_dhcp')
                    yield '   '
                    yield str((undefined(name='av_pair_dhcp') if l_0_av_pair_dhcp is missing else l_0_av_pair_dhcp))
                    yield '\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'logging'), True):
                pass
                yield '   supplicant logging\n'

blocks = {}
debug_info = '7=41&8=43&12=47&13=52&14=54&15=57&17=59&18=62&20=64&21=67&23=71&24=74&26=76&30=80&31=82&32=85&33=87&34=90&35=96&36=98&37=100&40=102&41=104&42=106&43=108&46=110&47=112&48=114&49=116&51=118&52=120&53=122&54=124&55=126&56=128&58=131&63=134&64=137&67=141&68=144&70=146&71=148&72=151&74=153&75=156&78=158&81=161&82=164&84=166&85=169&87=173&88=176&90=178&91=181&93=183&94=185&95=188&96=190&98=193&99=195&101=199&102=201&103=204&105=206&109=209&110=211&111=213&112=216&113=218&115=222&117=224&118=226&119=229&120=231&122=235&125=237&126=239&127=241&128=244&129=246&131=250&133=252&134=254&135=257&136=259&138=263&140=265&141=267&142=270&143=272&145=276&148=278'