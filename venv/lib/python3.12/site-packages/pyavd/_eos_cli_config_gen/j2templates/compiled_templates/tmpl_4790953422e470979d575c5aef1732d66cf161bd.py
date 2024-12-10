from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dhcp-relay.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dhcp_relay = resolve('dhcp_relay')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay)):
        pass
        yield '\n## DHCP Relay\n\n### DHCP Relay Summary\n'
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'tunnel_requests_disabled'), True):
            pass
            yield '\n- DHCP Relay is disabled for tunnelled requests\n'
        else:
            pass
            yield '\n- DHCP Relay is enabled for tunnelled requests\n'
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'mlag_peerlink_requests_disabled'), True):
            pass
            yield '- DHCP Relay is disabled for MLAG peer-link requests\n'
        else:
            pass
            yield '- DHCP Relay is enabled for MLAG peer-link requests\n'
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'servers')):
            pass
            yield '\n| DHCP Relay Servers |\n| ------------------ |\n'
            for l_1_server in t_1(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'servers')):
                _loop_vars = {}
                pass
                yield '| '
                yield str(l_1_server)
                yield ' |\n'
            l_1_server = missing
        yield '\n### DHCP Relay Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/dhcp-relay.j2', 'documentation/dhcp-relay.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&12=27&19=33&24=39&28=42&29=46&36=50'