from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mac-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_security = resolve('mac_security')
    try:
        t_1 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
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
    if t_3((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security)):
        pass
        yield '!\nmac security\n'
        if (t_3(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_name')) and t_3(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_key'))):
            pass
            yield '   license '
            yield str(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_name'))
            yield ' '
            yield str(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_key'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'fips_restrictions'), True):
            pass
            yield '   fips restrictions\n'
        for l_1_profile in t_2(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'profiles'), 'name'):
            l_1_traffic_unprotected_cli = resolve('traffic_unprotected_cli')
            _loop_vars = {}
            pass
            yield '   !\n   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_3(environment.getattr(l_1_profile, 'cipher')):
                pass
                yield '      cipher '
                yield str(environment.getattr(l_1_profile, 'cipher'))
                yield '\n'
            for l_2_connection_key in t_2(environment.getattr(l_1_profile, 'connection_keys'), 'id'):
                l_2_hide_passwords = resolve('hide_passwords')
                l_2_key_cli = resolve('key_cli')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_2_connection_key, 'encrypted_key')):
                    pass
                    l_2_key_cli = str_join(('key ', environment.getattr(l_2_connection_key, 'id'), ' 7 ', t_1(environment.getattr(l_2_connection_key, 'encrypted_key'), (undefined(name='hide_passwords') if l_2_hide_passwords is missing else l_2_hide_passwords)), ))
                    _loop_vars['key_cli'] = l_2_key_cli
                    if t_3(environment.getattr(l_2_connection_key, 'fallback'), True):
                        pass
                        l_2_key_cli = str_join(((undefined(name='key_cli') if l_2_key_cli is missing else l_2_key_cli), ' fallback', ))
                        _loop_vars['key_cli'] = l_2_key_cli
                    yield '      '
                    yield str((undefined(name='key_cli') if l_2_key_cli is missing else l_2_key_cli))
                    yield '\n'
            l_2_connection_key = l_2_hide_passwords = l_2_key_cli = missing
            if t_3(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'key_server_priority')):
                pass
                yield '      mka key-server priority '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'key_server_priority'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'session'), 'rekey_period')):
                pass
                yield '      mka session rekey-period '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'session'), 'rekey_period'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'action')):
                pass
                l_1_traffic_unprotected_cli = str_join(('traffic unprotected ', environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'action'), ))
                _loop_vars['traffic_unprotected_cli'] = l_1_traffic_unprotected_cli
                if ((environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'action') == 'allow') and t_3(environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'allow_active_sak'), True)):
                    pass
                    l_1_traffic_unprotected_cli = str_join(((undefined(name='traffic_unprotected_cli') if l_1_traffic_unprotected_cli is missing else l_1_traffic_unprotected_cli), ' active-sak', ))
                    _loop_vars['traffic_unprotected_cli'] = l_1_traffic_unprotected_cli
                yield '      '
                yield str((undefined(name='traffic_unprotected_cli') if l_1_traffic_unprotected_cli is missing else l_1_traffic_unprotected_cli))
                yield '\n'
            if t_3(environment.getattr(l_1_profile, 'sci'), True):
                pass
                yield '      sci\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control'), 'mode')):
                pass
                yield '      l2-protocol ethernet-flow-control '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control'), 'mode'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp'), 'mode')):
                pass
                yield '      l2-protocol lldp '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp'), 'mode'))
                yield '\n'
        l_1_profile = l_1_traffic_unprotected_cli = missing

blocks = {}
debug_info = '7=30&10=33&11=36&13=40&16=43&18=48&19=50&20=53&22=55&23=60&24=62&25=64&26=66&28=69&31=72&32=75&34=77&35=80&37=82&38=84&39=86&40=88&42=91&44=93&47=96&48=99&50=101&51=104'