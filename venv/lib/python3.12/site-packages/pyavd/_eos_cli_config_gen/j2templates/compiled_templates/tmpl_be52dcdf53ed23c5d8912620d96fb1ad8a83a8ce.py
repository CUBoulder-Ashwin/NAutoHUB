from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ipv6-dhcp-relay.j2'

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
        yield '!\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'always_on'), True):
            pass
            yield 'ipv6 dhcp relay always-on\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'all_subnets'), True):
            pass
            yield 'ipv6 dhcp relay all-subnets default\n'
        if t_1(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option')):
            pass
            if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'link_layer_address'), True):
                pass
                yield 'ipv6 dhcp relay option link-layer address\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format')):
                pass
                if (environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format') == '%m:%i'):
                    pass
                    yield 'ipv6 dhcp relay option remote-id format %m:%i\n'
                elif (environment.getattr(environment.getattr((undefined(name='ipv6_dhcp_relay') if l_0_ipv6_dhcp_relay is missing else l_0_ipv6_dhcp_relay), 'option'), 'remote_id_format') == '%m:%p'):
                    pass
                    yield 'ipv6 dhcp relay option remote-id format %m:%p\n'

blocks = {}
debug_info = '7=18&9=21&12=24&15=27&16=29&19=32&20=34&22=37'