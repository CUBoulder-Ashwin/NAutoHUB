from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/as-path.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_as_path = resolve('as_path')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path)):
        pass
        yield '!\n'
        if t_3(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'regex_mode')):
            pass
            yield 'ip as-path regex-mode '
            yield str(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'regex_mode'))
            yield '\n'
        for l_1_as_path_access_list in t_2(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'access_lists'), 'name'):
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_as_path_access_list, 'entries')):
                pass
                for l_2_as_path_access_list_entry in environment.getattr(l_1_as_path_access_list, 'entries'):
                    _loop_vars = {}
                    pass
                    if (t_3(environment.getattr(l_2_as_path_access_list_entry, 'type')) and t_3(environment.getattr(l_2_as_path_access_list_entry, 'match'))):
                        pass
                        yield 'ip as-path access-list '
                        yield str(environment.getattr(l_1_as_path_access_list, 'name'))
                        yield ' '
                        yield str(environment.getattr(l_2_as_path_access_list_entry, 'type'))
                        yield ' '
                        yield str(environment.getattr(l_2_as_path_access_list_entry, 'match'))
                        yield ' '
                        yield str(t_1(environment.getattr(l_2_as_path_access_list_entry, 'origin'), 'any'))
                        yield '\n'
                l_2_as_path_access_list_entry = missing
        l_1_as_path_access_list = missing

blocks = {}
debug_info = '7=30&9=33&10=36&12=38&13=41&14=43&15=46&16=49'