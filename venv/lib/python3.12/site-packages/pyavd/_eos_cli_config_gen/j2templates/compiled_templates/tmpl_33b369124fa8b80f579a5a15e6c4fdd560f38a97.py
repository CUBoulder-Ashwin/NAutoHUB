from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dynamic-prefix-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dynamic_prefix_lists = resolve('dynamic_prefix_lists')
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
    def t_3(fiter):
        for l_1_dynamic_prefix_list in fiter:
            if (t_2(environment.getattr(l_1_dynamic_prefix_list, 'name')) and t_2(environment.getattr(l_1_dynamic_prefix_list, 'match_map'))):
                yield l_1_dynamic_prefix_list
    for l_1_dynamic_prefix_list in t_3(t_1((undefined(name='dynamic_prefix_lists') if l_0_dynamic_prefix_lists is missing else l_0_dynamic_prefix_lists), 'name')):
        _loop_vars = {}
        pass
        yield '!\ndynamic prefix-list '
        yield str(environment.getattr(l_1_dynamic_prefix_list, 'name'))
        yield '\n   match-map '
        yield str(environment.getattr(l_1_dynamic_prefix_list, 'match_map'))
        yield '\n'
        if t_2(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv4')):
            pass
            yield '   prefix-list ipv4 '
            yield str(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv4'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv6')):
            pass
            yield '   prefix-list ipv6 '
            yield str(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv6'))
            yield '\n'
    l_1_dynamic_prefix_list = missing

blocks = {}
debug_info = '7=24&9=32&10=34&11=36&12=39&14=41&15=44'