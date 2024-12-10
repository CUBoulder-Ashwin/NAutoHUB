from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dhcp-relay.j2'

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
        yield '!\ndhcp relay\n'
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'tunnel_requests_disabled'), True):
            pass
            yield '   tunnel requests disabled\n'
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'mlag_peerlink_requests_disabled'), True):
            pass
            yield '   mlag peer-link requests disabled\n'
        for l_1_server in t_1(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'servers')):
            _loop_vars = {}
            pass
            yield '   server '
            yield str(l_1_server)
            yield '\n'
        l_1_server = missing

blocks = {}
debug_info = '7=24&10=27&13=30&16=33&17=37'