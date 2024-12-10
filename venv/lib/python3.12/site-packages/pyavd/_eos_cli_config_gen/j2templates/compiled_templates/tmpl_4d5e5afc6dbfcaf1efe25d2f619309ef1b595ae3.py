from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-dhcp-relay.j2'

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
        yield '!\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'information_option'), True):
            pass
            yield 'ip dhcp relay information option\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'always_on'), True):
            pass
            yield 'ip dhcp relay always-on\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_relay') if l_0_ip_dhcp_relay is missing else l_0_ip_dhcp_relay), 'all_subnets'), True):
            pass
            yield 'ip dhcp relay all-subnets default\n'

blocks = {}
debug_info = '7=18&9=21&12=24&15=27'