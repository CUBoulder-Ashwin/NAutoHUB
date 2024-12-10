from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ipv6-unicast-routing-vrfs.j2'

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
    l_1_loop = missing
    for l_1_vrf, l_1_loop in LoopContext(t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs), 'name'), undefined):
        _loop_vars = {}
        pass
        if (t_2(environment.getattr(l_1_vrf, 'ipv6_routing'), True) and (environment.getattr(l_1_vrf, 'name') != 'default')):
            pass
            if environment.getattr(l_1_loop, 'first'):
                pass
                yield '!\n'
            yield 'ipv6 unicast-routing vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
    l_1_loop = l_1_vrf = missing

blocks = {}
debug_info = '7=25&8=28&9=30&12=34'