from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mac-access-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_access_lists = resolve('mac_access_lists')
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
    if t_3((undefined(name='mac_access_lists') if l_0_mac_access_lists is missing else l_0_mac_access_lists)):
        pass
        yield '\n### MAC Access-lists\n\n#### MAC Access-lists Summary\n'
        for l_1_mac_access_list in t_2((undefined(name='mac_access_lists') if l_0_mac_access_lists is missing else l_0_mac_access_lists), 'name'):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_mac_access_list, 'name')) and t_3(environment.getattr(l_1_mac_access_list, 'entries'))):
                pass
                yield '\n##### '
                yield str(environment.getattr(l_1_mac_access_list, 'name'))
                yield '\n'
                if t_3(environment.getattr(l_1_mac_access_list, 'counters_per_entry'), True):
                    pass
                    yield '\n- ACL has counting mode `counters per-entry` enabled!\n'
                yield '\n| Sequence | Action |\n| -------- | ------ |\n'
                for l_2_acl_entry in environment.getattr(l_1_mac_access_list, 'entries'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(t_1(environment.getattr(l_2_acl_entry, 'sequence'), '-'))
                    yield ' | '
                    yield str(environment.getattr(l_2_acl_entry, 'action'))
                    yield ' |\n'
                l_2_acl_entry = missing
        l_1_mac_access_list = missing
        yield '\n#### MAC Access-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mac-access-lists.j2', 'documentation/mac-access-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&13=36&15=39&16=41&23=45&24=49&32=56'