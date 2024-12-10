from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/as-path.j2'

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
        t_3 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'access_lists')):
        pass
        yield '\n### AS Path Lists\n\n#### AS Path Lists Summary\n'
        if t_4(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'regex_mode')):
            pass
            yield '\nAS Path Regex Mode is **'
            yield str(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'regex_mode'))
            yield '**.\n'
        yield '\n| List Name | Type | Match | Origin |\n| --------- | ---- | ----- | ------ |\n'
        for l_1_as_path_access_list in t_2(environment.getattr((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path), 'access_lists'), 'name'):
            _loop_vars = {}
            pass
            if (t_4(environment.getattr(l_1_as_path_access_list, 'name')) and t_4(environment.getattr(l_1_as_path_access_list, 'entries'))):
                pass
                for l_2_as_path_access_list_entry in environment.getattr(l_1_as_path_access_list, 'entries'):
                    _loop_vars = {}
                    pass
                    if (t_4(environment.getattr(l_2_as_path_access_list_entry, 'type')) and t_4(environment.getattr(l_2_as_path_access_list_entry, 'match'))):
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_as_path_access_list, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_as_path_access_list_entry, 'type'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, environment.getattr(l_2_as_path_access_list_entry, 'match'), '|', '\\|'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_as_path_access_list_entry, 'origin'), 'any'))
                        yield ' |\n'
                l_2_as_path_access_list_entry = missing
        l_1_as_path_access_list = missing
        yield '\n#### AS Path Lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/as-path.j2', 'documentation/as-path.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&12=39&14=42&19=45&20=48&21=50&22=53&23=56&32=67'