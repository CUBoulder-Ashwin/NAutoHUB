from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-virtual-router-mac-address.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_virtual_router_mac_address = resolve('ip_virtual_router_mac_address')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='ip_virtual_router_mac_address') if l_0_ip_virtual_router_mac_address is missing else l_0_ip_virtual_router_mac_address)):
        pass
        yield '!\nip virtual-router mac-address '
        yield str((undefined(name='ip_virtual_router_mac_address') if l_0_ip_virtual_router_mac_address is missing else l_0_ip_virtual_router_mac_address))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'