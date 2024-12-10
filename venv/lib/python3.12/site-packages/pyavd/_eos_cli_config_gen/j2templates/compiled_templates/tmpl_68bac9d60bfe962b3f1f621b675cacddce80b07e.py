from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ipv6-dhcp-relay.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_dhcp_relay = resolve('ipv6_dhcp_relay')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay)):
        pass
        yield '\n## IPv6 DHCP Relay\n\n### IPv6 DHCP Relay Summary\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'always_on'), True):
            pass
            yield '\nDhcpRelay Agent is in always-on mode.\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'all_subnets'), True):
            pass
            yield '\nForwarding requests with additional IPv6 addresses in the "giaddr" field is allowed.\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option')):
            pass
            if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'link_layer_address'), True):
                pass
                yield '\nAdd Option 79 - Link Layer Address Option.\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format')):
                pass
                if (environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format') == '%m:%i'):
                    pass
                    yield '\nAdd RemoteID option 37 in format MAC address and interface ID.\n'
                elif (environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format') == '%m:%p'):
                    pass
                    yield '\nAdd RemoteID option 37 in format MAC address and interface name.\n'
        yield '\n### IPv6 DHCP Relay Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ipv6-dhcp-relay.j2', 'documentation/ipv6-dhcp-relay.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&12=21&16=24&20=27&21=29&25=32&26=34&29=37&39=41'