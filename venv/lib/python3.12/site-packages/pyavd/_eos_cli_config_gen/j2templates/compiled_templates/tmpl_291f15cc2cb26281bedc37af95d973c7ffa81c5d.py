from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/interface-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_groups = resolve('interface_groups')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    pass
    for l_1_interface_group in t_1((undefined(name='interface_groups') if l_0_interface_groups is missing else l_0_interface_groups), 'name'):
        _loop_vars = {}
        pass
        yield '!\ngroup interface '
        yield str(environment.getattr(l_1_interface_group, 'name'))
        yield '\n'
        for l_2_interface in t_1(environment.getattr(l_1_interface_group, 'interfaces')):
            _loop_vars = {}
            pass
            yield '   interface '
            yield str(l_2_interface)
            yield '\n'
        l_2_interface = missing
        for l_2_bgp_profile in t_1(environment.getattr(l_1_interface_group, 'bgp_maintenance_profiles')):
            _loop_vars = {}
            pass
            yield '   maintenance profile bgp '
            yield str(l_2_bgp_profile)
            yield '\n'
        l_2_bgp_profile = missing
        for l_2_interface_profile in t_1(environment.getattr(l_1_interface_group, 'interface_maintenance_profiles')):
            _loop_vars = {}
            pass
            yield '   maintenance profile interface '
            yield str(l_2_interface_profile)
            yield '\n'
        l_2_interface_profile = missing
    l_1_interface_group = missing

blocks = {}
debug_info = '7=18&9=22&10=24&11=28&13=31&14=35&16=38&17=42'