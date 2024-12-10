from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-routing.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_routing_ipv6_interfaces = resolve('ip_routing_ipv6_interfaces')
    l_0_ip_routing = resolve('ip_routing')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='ip_routing_ipv6_interfaces') if l_0_ip_routing_ipv6_interfaces is missing else l_0_ip_routing_ipv6_interfaces), True):
        pass
        yield '!\nip routing ipv6 interfaces\n'
    elif t_1((undefined(name='ip_routing') if l_0_ip_routing is missing else l_0_ip_routing), True):
        pass
        yield '!\nip routing\n'
    elif t_1((undefined(name='ip_routing') if l_0_ip_routing is missing else l_0_ip_routing), False):
        pass
        yield '!\nno ip routing\n'

blocks = {}
debug_info = '8=19&11=22&14=25'