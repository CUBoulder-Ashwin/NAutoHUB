from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dot1x.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_dot1x = resolve('dot1x')
    l_0_system_auth_control = resolve('system_auth_control')
    l_0_protocol_lldp_bypass = resolve('protocol_lldp_bypass')
    l_0_dynamic_authorization = resolve('dynamic_authorization')
    l_0_delay = resolve('delay')
    l_0_hold_period = resolve('hold_period')
    l_0_radius_av_pair_service = resolve('radius_av_pair_service')
    l_0_framed_mtu = resolve('framed_mtu')
    l_0_ethernet_interfaces_dot1x = missing
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
    l_0_ethernet_interfaces_dot1x = []
    context.vars['ethernet_interfaces_dot1x'] = l_0_ethernet_interfaces_dot1x
    context.exported_vars.add('ethernet_interfaces_dot1x')
    for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_4(environment.getattr(l_1_ethernet_interface, 'dot1x')):
            pass
            context.call(environment.getattr((undefined(name='ethernet_interfaces_dot1x') if l_0_ethernet_interfaces_dot1x is missing else l_0_ethernet_interfaces_dot1x), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    if (t_4((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x)) or (t_3((undefined(name='ethernet_interfaces_dot1x') if l_0_ethernet_interfaces_dot1x is missing else l_0_ethernet_interfaces_dot1x)) > 0)):
        pass
        yield '\n## 802.1X Port Security\n\n### 802.1X Summary\n'
        if t_4((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x)):
            pass
            yield '\n#### 802.1X Global\n\n| System Auth Control | Protocol LLDP Bypass | Dynamic Authorization |\n| ------------------- | -------------------- | ----------------------|\n'
            l_0_system_auth_control = t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'system_auth_control'), '-')
            context.vars['system_auth_control'] = l_0_system_auth_control
            context.exported_vars.add('system_auth_control')
            l_0_protocol_lldp_bypass = t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_lldp_bypass'), '-')
            context.vars['protocol_lldp_bypass'] = l_0_protocol_lldp_bypass
            context.exported_vars.add('protocol_lldp_bypass')
            l_0_dynamic_authorization = t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'dynamic_authorization'), '-')
            context.vars['dynamic_authorization'] = l_0_dynamic_authorization
            context.exported_vars.add('dynamic_authorization')
            yield '| '
            yield str((undefined(name='system_auth_control') if l_0_system_auth_control is missing else l_0_system_auth_control))
            yield ' | '
            yield str((undefined(name='protocol_lldp_bypass') if l_0_protocol_lldp_bypass is missing else l_0_protocol_lldp_bypass))
            yield ' | '
            yield str((undefined(name='dynamic_authorization') if l_0_dynamic_authorization is missing else l_0_dynamic_authorization))
            yield ' |\n'
            if t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')):
                pass
                yield '\n#### 802.1X MAC based authentication\n\n| Delay | Hold period |\n| ----- | ----------- |\n'
                l_0_delay = t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay'), '-')
                context.vars['delay'] = l_0_delay
                context.exported_vars.add('delay')
                l_0_hold_period = t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period'), '-')
                context.vars['hold_period'] = l_0_hold_period
                context.exported_vars.add('hold_period')
                yield '| '
                yield str((undefined(name='delay') if l_0_delay is missing else l_0_delay))
                yield ' | '
                yield str((undefined(name='hold_period') if l_0_hold_period is missing else l_0_hold_period))
                yield ' |\n'
            if t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair')):
                pass
                yield '\n#### 802.1X Radius AV pair\n\n| Service type | Framed MTU |\n| ------------ | ---------- |\n'
                l_0_radius_av_pair_service = t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'service_type'), '-')
                context.vars['radius_av_pair_service'] = l_0_radius_av_pair_service
                context.exported_vars.add('radius_av_pair_service')
                l_0_framed_mtu = t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu'), '-')
                context.vars['framed_mtu'] = l_0_framed_mtu
                context.exported_vars.add('framed_mtu')
                yield '| '
                yield str((undefined(name='radius_av_pair_service') if l_0_radius_av_pair_service is missing else l_0_radius_av_pair_service))
                yield ' | '
                yield str((undefined(name='framed_mtu') if l_0_framed_mtu is missing else l_0_framed_mtu))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'enabled'), True):
                pass
                yield '\n#### 802.1X Captive-portal authentication\n\n| Authentication Attribute | Value |\n| ------------------------ | ----- |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'url')):
                    pass
                    yield '| URL | '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'url'))
                    yield ' |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'ssl_profile')):
                    pass
                    yield '| SSL profile | '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'ssl_profile'))
                    yield ' |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'access_list_ipv4')):
                    pass
                    yield '| IPv4 Access-list | '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'access_list_ipv4'))
                    yield ' |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'captive_portal'), 'start_limit_infinite'), True):
                    pass
                    yield '| Start limit | Infinite |\n'
            if t_4(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant')):
                pass
                yield '\n#### 802.1X Supplicant\n\n| Attribute | Value |\n| --------- | ----- |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'logging')):
                    pass
                    yield '| Logging | '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'logging'))
                    yield ' |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'disconnect_cached_results_timeout')):
                    pass
                    yield '| Disconnect cached-results timeout | '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'disconnect_cached_results_timeout'))
                    yield ' seconds |\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'profiles')):
                    pass
                    yield '\n##### 802.1X Supplicant profiles\n\n| Profile | EAP Method | Identity | SSL Profile |\n| ------- | ---------- | -------- | ----------- |\n'
                    for l_1_profile in t_2(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'supplicant'), 'profiles'), 'name'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_profile, 'name'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_1_profile, 'eap_method'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_1_profile, 'identity'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_1_profile, 'ssl_profile'), '-'))
                        yield ' |\n'
                    l_1_profile = missing
        if (t_3((undefined(name='ethernet_interfaces_dot1x') if l_0_ethernet_interfaces_dot1x is missing else l_0_ethernet_interfaces_dot1x)) > 0):
            pass
            yield '\n#### 802.1X Interfaces\n\n| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |\n| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |\n'
            for l_1_ethernet_interface in (undefined(name='ethernet_interfaces_dot1x') if l_0_ethernet_interfaces_dot1x is missing else l_0_ethernet_interfaces_dot1x):
                l_1_pae_mode = l_1_auth_failure_action = l_1_state = l_1_phone_state = l_1_reauthentication = l_1_host_mode = l_1_mac_based_authentication_enabled = l_1_auth_failure_fallback_mba = missing
                _loop_vars = {}
                pass
                l_1_pae_mode = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'pae'), 'mode'), '-')
                _loop_vars['pae_mode'] = l_1_pae_mode
                l_1_auth_failure_action = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'action'), '-')
                _loop_vars['auth_failure_action'] = l_1_auth_failure_action
                if (((undefined(name='auth_failure_action') if l_1_auth_failure_action is missing else l_1_auth_failure_action) == 'allow') and t_4(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'))):
                    pass
                    l_1_auth_failure_action = str_join(((undefined(name='auth_failure_action') if l_1_auth_failure_action is missing else l_1_auth_failure_action), ' vlan ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'), ))
                    _loop_vars['auth_failure_action'] = l_1_auth_failure_action
                l_1_state = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control'), '-')
                _loop_vars['state'] = l_1_state
                l_1_phone_state = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control_force_authorized_phone'), '-')
                _loop_vars['phone_state'] = l_1_phone_state
                l_1_reauthentication = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthentication'), '-')
                _loop_vars['reauthentication'] = l_1_reauthentication
                l_1_host_mode = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'mode'), '-')
                _loop_vars['host_mode'] = l_1_host_mode
                l_1_mac_based_authentication_enabled = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'enabled'), '-')
                _loop_vars['mac_based_authentication_enabled'] = l_1_mac_based_authentication_enabled
                l_1_auth_failure_fallback_mba = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'enabled'), '-')
                _loop_vars['auth_failure_fallback_mba'] = l_1_auth_failure_fallback_mba
                yield '| '
                yield str(environment.getattr(l_1_ethernet_interface, 'name'))
                yield ' | '
                yield str((undefined(name='pae_mode') if l_1_pae_mode is missing else l_1_pae_mode))
                yield ' | '
                yield str((undefined(name='state') if l_1_state is missing else l_1_state))
                yield ' | '
                yield str((undefined(name='phone_state') if l_1_phone_state is missing else l_1_phone_state))
                yield ' | '
                yield str((undefined(name='reauthentication') if l_1_reauthentication is missing else l_1_reauthentication))
                yield ' | '
                yield str((undefined(name='auth_failure_action') if l_1_auth_failure_action is missing else l_1_auth_failure_action))
                yield ' | '
                yield str((undefined(name='host_mode') if l_1_host_mode is missing else l_1_host_mode))
                yield ' | '
                yield str((undefined(name='mac_based_authentication_enabled') if l_1_mac_based_authentication_enabled is missing else l_1_mac_based_authentication_enabled))
                yield ' | '
                yield str((undefined(name='auth_failure_fallback_mba') if l_1_auth_failure_fallback_mba is missing else l_1_auth_failure_fallback_mba))
                yield ' |\n'
            l_1_ethernet_interface = l_1_pae_mode = l_1_auth_failure_action = l_1_state = l_1_phone_state = l_1_reauthentication = l_1_host_mode = l_1_mac_based_authentication_enabled = l_1_auth_failure_fallback_mba = missing

blocks = {}
debug_info = '7=45&8=48&9=51&10=53&13=55&18=58&24=61&25=64&26=67&27=71&28=77&34=80&35=83&36=87&38=91&44=94&45=97&46=101&48=105&54=108&55=111&57=113&58=116&60=118&61=121&63=123&67=126&73=129&74=132&76=134&77=137&79=139&85=142&86=146&91=155&97=158&98=162&99=164&100=166&102=168&104=170&105=172&106=174&107=176&108=178&109=180&110=183'