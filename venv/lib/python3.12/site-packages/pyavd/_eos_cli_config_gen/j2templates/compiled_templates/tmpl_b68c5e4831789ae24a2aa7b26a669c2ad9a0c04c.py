from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-dhcp-snooping.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_dhcp_snooping = resolve('ip_dhcp_snooping')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'enabled'), True):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'bridging'), True):
            pass
            yield 'ip dhcp snooping bridging\n'
        else:
            pass
            yield 'ip dhcp snooping\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'enabled'), True):
            pass
            yield 'ip dhcp snooping information option\n'
            if (t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_type')) and t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_format'))):
                pass
                yield 'ip dhcp snooping information option circuit-id type '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_type'))
                yield ' format '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_format'))
                yield '\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'vlan')):
            pass
            yield 'ip dhcp snooping vlan '
            yield str(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'vlan'))
            yield '\n'

blocks = {}
debug_info = '7=18&9=21&14=27&16=30&17=33&20=37&21=40'