from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mac-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_security = resolve('mac_security')
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
    if t_4((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security)):
        pass
        yield '\n## MACsec\n\n### MACsec Summary\n\n'
        if t_4(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license')):
            pass
            yield 'License is installed.\n'
        else:
            pass
            yield 'License is not installed.\n'
        yield '\n'
        if t_4(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'fips_restrictions'), True):
            pass
            yield 'FIPS restrictions enabled.\n'
        if t_4(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'profiles')):
            pass
            yield '\n#### MACsec Profiles Summary\n'
            for l_1_profile in t_2(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'profiles'), 'name'):
                l_1_cipher = l_1_key_server_priority = l_1_rekey_period = l_1_sci = l_1_traffic_unprotected = missing
                _loop_vars = {}
                pass
                yield '\n##### Profile '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '\n\n###### Settings\n\n| Cipher | Key-Server Priority | Rekey-Period | SCI | Traffic Unprotected Fallback |\n| ------ | ------------------- | ------------ | --- | ---------------------------- |\n'
                l_1_cipher = t_1(environment.getattr(l_1_profile, 'cipher'), '-')
                _loop_vars['cipher'] = l_1_cipher
                l_1_key_server_priority = t_1(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'key_server_priority'), '-')
                _loop_vars['key_server_priority'] = l_1_key_server_priority
                l_1_rekey_period = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'session'), 'rekey_period'), '-')
                _loop_vars['rekey_period'] = l_1_rekey_period
                l_1_sci = t_1(environment.getattr(l_1_profile, 'sci'), '-')
                _loop_vars['sci'] = l_1_sci
                l_1_traffic_unprotected = t_1(environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'action'), '-')
                _loop_vars['traffic_unprotected'] = l_1_traffic_unprotected
                if (((undefined(name='traffic_unprotected') if l_1_traffic_unprotected is missing else l_1_traffic_unprotected) == 'allow') and t_4(environment.getattr(environment.getattr(l_1_profile, 'traffic_unprotected'), 'allow_active_sak'), True)):
                    pass
                    l_1_traffic_unprotected = str_join(((undefined(name='traffic_unprotected') if l_1_traffic_unprotected is missing else l_1_traffic_unprotected), ' active-sak', ))
                    _loop_vars['traffic_unprotected'] = l_1_traffic_unprotected
                yield '| '
                yield str((undefined(name='cipher') if l_1_cipher is missing else l_1_cipher))
                yield ' | '
                yield str((undefined(name='key_server_priority') if l_1_key_server_priority is missing else l_1_key_server_priority))
                yield ' | '
                yield str((undefined(name='rekey_period') if l_1_rekey_period is missing else l_1_rekey_period))
                yield ' | '
                yield str((undefined(name='sci') if l_1_sci is missing else l_1_sci))
                yield ' | '
                yield str((undefined(name='traffic_unprotected') if l_1_traffic_unprotected is missing else l_1_traffic_unprotected))
                yield ' |\n'
                if t_4(environment.getattr(l_1_profile, 'connection_keys')):
                    pass
                    yield '\n###### Keys\n\n| Key ID | Fallback |\n| ------ | -------- |\n'
                    for l_2_connection_key in t_2(environment.getattr(l_1_profile, 'connection_keys'), 'id'):
                        l_2_fallback = resolve('fallback')
                        _loop_vars = {}
                        pass
                        if t_4(environment.getattr(l_2_connection_key, 'encrypted_key')):
                            pass
                            l_2_fallback = t_1(environment.getattr(l_2_connection_key, 'fallback'), '-')
                            _loop_vars['fallback'] = l_2_fallback
                            yield '| '
                            yield str(environment.getattr(l_2_connection_key, 'id'))
                            yield ' | '
                            yield str((undefined(name='fallback') if l_2_fallback is missing else l_2_fallback))
                            yield ' |\n'
                    l_2_connection_key = l_2_fallback = missing
                if (t_3(t_1(environment.getattr(l_1_profile, 'l2_protocols'), [])) > 0):
                    pass
                    yield '\n###### L2 Protocols\n\n| L2 Protocol | Mode |\n| ----------- | ---- |\n'
                    if t_4(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control')):
                        pass
                        yield '| ethernet-flow-control | '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control'), 'mode'))
                        yield ' |\n'
                    if t_4(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp')):
                        pass
                        yield '| lldp | '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp'), 'mode'))
                        yield ' |\n'
            l_1_profile = l_1_cipher = l_1_key_server_priority = l_1_rekey_period = l_1_sci = l_1_traffic_unprotected = missing
        yield '\n### MACsec Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mac-security.j2', 'documentation/mac-security.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&13=39&19=46&22=49&25=52&27=57&33=59&34=61&35=63&36=65&37=67&38=69&39=71&41=74&42=84&48=87&49=91&50=93&51=96&55=101&61=104&62=107&64=109&65=112&74=116'