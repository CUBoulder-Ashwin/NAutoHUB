from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-dhcp-relay.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_dhcp_relay = resolve('ip_dhcp_relay')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay)):
        pass
        yield '\n## IP DHCP Relay\n\n### IP DHCP Relay Summary\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'information_option'), True):
            pass
            yield '\nIP DHCP Relay Option 82 is enabled.\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'always_on'), True):
            pass
            yield '\nDhcpRelay Agent is in always-on mode.\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'all_subnets'), True):
            pass
            yield '\nForwarding requests with secondary IP addresses in the "giaddr" field is allowed.\n'
        yield '\n### IP DHCP Relay Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-dhcp-relay.j2', 'documentation/ip-dhcp-relay.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&12=21&16=24&20=27&28=31'