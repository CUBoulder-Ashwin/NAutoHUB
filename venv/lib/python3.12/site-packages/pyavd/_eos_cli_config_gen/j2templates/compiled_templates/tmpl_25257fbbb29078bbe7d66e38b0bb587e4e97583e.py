from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-l2-vpn.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_l2_vpn = resolve('router_l2_vpn')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn)):
        pass
        yield '\n## Router L2 VPN\n\n### Router L2 VPN Summary\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_learning_bridged'), True):
            pass
            yield '\n- ARP learning bridged is enabled.\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_proxy'), 'prefix_list')):
            pass
            yield '\n- VXLAN ARP Proxying is disabled for IPv4 addresses defined in the prefix-list '
            yield str(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_proxy'), 'prefix_list'))
            yield '.\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_selective_install'), True):
            pass
            yield '\n- Selective ARP is enabled.\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_learning_bridged'), True):
            pass
            yield '\n- ND learning bridged is enabled.\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_proxy'), 'prefix_list')):
            pass
            yield '\n- VXLAN ND Proxying is disabled for IPv6 addresses defined in the prefix-list '
            yield str(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_proxy'), 'prefix_list'))
            yield '.\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_rs_flooding_disabled'), True):
            pass
            yield '\n- Neighbor discovery router solicitation VTEP flooding is disabled.\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'virtual_router_nd_ra_flooding_disabled'), True):
            pass
            yield '\n- Virtual router neighbor advertisement VTEP flooding is disabled.\n'
        yield '\n### Router L2 VPN Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-l2-vpn.j2', 'documentation/router-l2-vpn.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&12=21&16=24&18=27&20=29&24=32&28=35&30=38&32=40&36=43&44=47'