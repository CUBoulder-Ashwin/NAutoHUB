from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/link-tracking-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_link_tracking_groups = resolve('link_tracking_groups')
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
    if t_3((undefined(name='link_tracking_groups') if l_0_link_tracking_groups is missing else l_0_link_tracking_groups)):
        pass
        yield '\n### Link Tracking\n\n#### Link Tracking Groups Summary\n\n| Group Name | Minimum Links | Recovery Delay |\n| ---------- | ------------- | -------------- |\n'
        for l_1_link_tracking_group in t_2((undefined(name='link_tracking_groups') if l_0_link_tracking_groups is missing else l_0_link_tracking_groups), 'name'):
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_link_tracking_group, 'name')):
                pass
                yield '| '
                yield str(environment.getattr(l_1_link_tracking_group, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_link_tracking_group, 'links_minimum'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_link_tracking_group, 'recovery_delay'), '-'))
                yield ' |\n'
        l_1_link_tracking_group = missing
        yield '\n#### Link Tracking Groups Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/link-tracking-groups.j2', 'documentation/link-tracking-groups.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=36&17=39&24=47'