from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-dhcp-snooping.j2'

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
    if t_1((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping)):
        pass
        yield '\n## IP DHCP Snooping\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'enabled'), True):
            pass
            yield '\nIP DHCP Snooping is enabled\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'bridging'), True):
            pass
            yield '\nIP DHCP Snooping Bridging is enabled\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'enabled'), True):
            pass
            yield '\nIP DHCP Snooping Insertion of Option 82 is enabled\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_type')):
            pass
            yield '\nIP DHCP Snooping Circuit-ID Suboption: '
            yield str(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_type'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_format')):
            pass
            yield '\nIP DHCP Snooping Circuit-ID Format: '
            yield str(environment.getattr(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'information_option'), 'circuit_id_format'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'vlan')):
            pass
            yield '\nIP DHCP Snooping enabled VLAN: '
            yield str(environment.getattr((undefined(name='ip_dhcp_snooping') if l_0_ip_dhcp_snooping is missing else l_0_ip_dhcp_snooping), 'vlan'))
            yield '\n'
        yield '\n### IP DHCP Snooping Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-dhcp-snooping.j2', 'documentation/ip-dhcp-snooping.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&10=21&14=24&18=27&22=30&24=33&26=35&28=38&30=40&32=43&38=46'