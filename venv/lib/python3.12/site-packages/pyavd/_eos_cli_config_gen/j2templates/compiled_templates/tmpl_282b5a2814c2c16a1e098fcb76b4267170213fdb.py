from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/bgp-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_bgp_groups = resolve('bgp_groups')
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
    for l_1_bgp_group in t_1((undefined(name='bgp_groups') if l_0_bgp_groups is missing else l_0_bgp_groups), 'name'):
        _loop_vars = {}
        pass
        yield '!\ngroup bgp '
        yield str(environment.getattr(l_1_bgp_group, 'name'))
        yield '\n'
        if t_2(environment.getattr(l_1_bgp_group, 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_bgp_group, 'vrf'))
            yield '\n'
        for l_2_neighbor in t_1(environment.getattr(l_1_bgp_group, 'neighbors')):
            _loop_vars = {}
            pass
            yield '   neighbor '
            yield str(l_2_neighbor)
            yield '\n'
        l_2_neighbor = missing
        for l_2_bgp_profile in t_1(environment.getattr(l_1_bgp_group, 'bgp_maintenance_profiles')):
            _loop_vars = {}
            pass
            yield '   maintenance profile bgp '
            yield str(l_2_bgp_profile)
            yield '\n'
        l_2_bgp_profile = missing
    l_1_bgp_group = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33&13=35&14=39&16=42&17=46'