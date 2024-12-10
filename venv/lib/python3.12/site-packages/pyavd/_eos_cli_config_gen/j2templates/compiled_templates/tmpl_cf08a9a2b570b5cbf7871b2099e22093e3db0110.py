from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/class-maps-pbr.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_class_maps = resolve('class_maps')
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
    for l_1_class_map in t_1(environment.getattr((undefined(name='class_maps') if l_0_class_maps is missing else l_0_class_maps), 'pbr'), 'name'):
        _loop_vars = {}
        pass
        yield '!\nclass-map type pbr match-any '
        yield str(environment.getattr(l_1_class_map, 'name'))
        yield '\n'
        if t_2(environment.getattr(environment.getattr(l_1_class_map, 'ip'), 'access_group')):
            pass
            yield '   match ip access-group '
            yield str(environment.getattr(environment.getattr(l_1_class_map, 'ip'), 'access_group'))
            yield '\n'
    l_1_class_map = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33'