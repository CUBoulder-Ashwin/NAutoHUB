from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dynamic-prefix-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dynamic_prefix_lists = resolve('dynamic_prefix_lists')
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
    if t_3((undefined(name='dynamic_prefix_lists') if l_0_dynamic_prefix_lists is missing else l_0_dynamic_prefix_lists)):
        pass
        yield '\n### Dynamic Prefix-lists\n\n#### Dynamic Prefix-lists Summary\n\n| Dynamic Prefix-List Name | Match Map | IPv4 Prefix-list | IPv6 Prefix-list |\n| ------------------------ | --------- | ---------------- | ---------------- |\n'
        def t_4(fiter):
            for l_1_dynamic_prefix_list in fiter:
                if (t_3(environment.getattr(l_1_dynamic_prefix_list, 'name')) and t_3(environment.getattr(l_1_dynamic_prefix_list, 'match_map'))):
                    yield l_1_dynamic_prefix_list
        for l_1_dynamic_prefix_list in t_4(t_2((undefined(name='dynamic_prefix_lists') if l_0_dynamic_prefix_lists is missing else l_0_dynamic_prefix_lists), 'name')):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_dynamic_prefix_list, 'name'))
            yield ' | '
            yield str(environment.getattr(l_1_dynamic_prefix_list, 'match_map'))
            yield ' | '
            yield str(t_1(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv4'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr(environment.getattr(l_1_dynamic_prefix_list, 'prefix_list'), 'ipv6'), '-'))
            yield ' |\n'
        l_1_dynamic_prefix_list = missing
        yield '\n#### Dynamic Prefix-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/dynamic-prefix-lists.j2', 'documentation/dynamic-prefix-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=41&22=51'