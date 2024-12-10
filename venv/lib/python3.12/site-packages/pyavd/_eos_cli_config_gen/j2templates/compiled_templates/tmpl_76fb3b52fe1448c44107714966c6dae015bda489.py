from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-l2-vpn.j2'

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
        yield '!\nrouter l2-vpn\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_learning_bridged'), True):
            pass
            yield '   arp learning bridged\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_proxy'), 'prefix_list')):
            pass
            yield '   arp proxy prefix-list '
            yield str(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_proxy'), 'prefix_list'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'arp_selective_install'), True):
            pass
            yield '   arp selective-install\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_learning_bridged'), True):
            pass
            yield '   nd learning bridged\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_proxy'), 'prefix_list')):
            pass
            yield '   nd proxy prefix-list '
            yield str(environment.getattr(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_proxy'), 'prefix_list'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'nd_rs_flooding_disabled'), True):
            pass
            yield '   nd rs flooding disabled\n'
        if t_1(environment.getattr((undefined(name='router_l2_vpn') if l_0_router_l2_vpn is missing else l_0_router_l2_vpn), 'virtual_router_nd_ra_flooding_disabled'), True):
            pass
            yield '   virtual-router neighbor advertisement flooding disabled\n'

blocks = {}
debug_info = '7=18&10=21&13=24&14=27&16=29&19=32&22=35&23=38&25=40&28=43'