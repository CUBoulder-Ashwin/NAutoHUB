from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-routing-vrfs.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vrfs = resolve('vrfs')
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
    for l_1_vrf in t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), 'name'):
        _loop_vars = {}
        pass
        if (t_2(environment.getattr(l_1_vrf, 'ip_routing_ipv6_interfaces'), True) and (environment.getattr(l_1_vrf, 'name') != 'default')):
            pass
            yield 'ip routing ipv6 interfaces vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
        elif (t_2(environment.getattr(l_1_vrf, 'ip_routing'), True) and (environment.getattr(l_1_vrf, 'name') != 'default')):
            pass
            yield 'ip routing vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
        elif (t_2(environment.getattr(l_1_vrf, 'ip_routing'), False) and (environment.getattr(l_1_vrf, 'name') != 'default')):
            pass
            yield 'no ip routing vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
    l_1_vrf = missing

blocks = {}
debug_info = '7=24&8=27&9=30&10=32&11=35&12=37&13=40'