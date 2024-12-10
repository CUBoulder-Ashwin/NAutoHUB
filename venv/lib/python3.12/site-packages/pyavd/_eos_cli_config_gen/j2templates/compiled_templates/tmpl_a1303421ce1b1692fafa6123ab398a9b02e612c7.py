from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/trackers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_trackers = resolve('trackers')
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
    if t_3((undefined(name='trackers') if l_0_trackers is missing else l_0_trackers)):
        pass
        yield '\n### Object Tracking\n\n#### Object Tracking Summary\n\n| Name | Interface | Tracked Property |\n| ---- | --------- | ---------------- |\n'
        for l_1_tracked_obj in t_2((undefined(name='trackers') if l_0_trackers is missing else l_0_trackers), 'name'):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_tracked_obj, 'name')) and t_3(environment.getattr(l_1_tracked_obj, 'interface'))):
                pass
                yield '| '
                yield str(environment.getattr(l_1_tracked_obj, 'name'))
                yield ' | '
                yield str(environment.getattr(l_1_tracked_obj, 'interface'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_tracked_obj, 'tracked_property'), 'line-protocol'))
                yield ' |\n'
        l_1_tracked_obj = missing
        yield '\n#### Object Tracking Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/trackers.j2', 'documentation/trackers.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=36&17=39&24=47'