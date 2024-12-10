from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/community-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_community_lists = resolve('community_lists')
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
    if t_2((undefined(name='community_lists') if l_0_community_lists is missing else l_0_community_lists)):
        pass
        yield '\n### Community-lists\n\n#### Community-lists Summary\n\n| Name | Action |\n| -------- | ------ |\n'
        for l_1_community_list in t_1((undefined(name='community_lists') if l_0_community_lists is missing else l_0_community_lists), 'name'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_community_list, 'name'))
            yield ' | '
            yield str(environment.getattr(l_1_community_list, 'action'))
            yield ' |\n'
        l_1_community_list = missing
        yield '\n#### Community-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/community-lists.j2', 'documentation/community-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=31&22=37'