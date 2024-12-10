from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-api-models.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_models = resolve('management_api_models')
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
        t_3 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models)):
        pass
        yield '\n### Management API Models\n\n#### Management API Models Summary\n\n| Provider | Path | Disabled |\n| -------- | ---- | ------- |\n'
        if t_4(environment.getattr((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models), 'providers')):
            pass
            for l_1_provider in t_2(environment.getattr((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models), 'providers'), 'name'):
                _loop_vars = {}
                pass
                if (t_4(environment.getattr(l_1_provider, 'paths')) and (t_3(environment.getattr(l_1_provider, 'name')) in ['smash', 'sysdb'])):
                    pass
                    for l_2_path in t_2(environment.getattr(l_1_provider, 'paths'), 'path'):
                        l_2_disabled = missing
                        _loop_vars = {}
                        pass
                        l_2_disabled = t_1(environment.getattr(l_2_path, 'disabled'), False)
                        _loop_vars['disabled'] = l_2_disabled
                        yield '| '
                        yield str(environment.getattr(l_1_provider, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_path, 'path'))
                        yield ' | '
                        yield str((undefined(name='disabled') if l_2_disabled is missing else l_2_disabled))
                        yield ' |\n'
                    l_2_path = l_2_disabled = missing
            l_1_provider = missing
        yield '\n#### Management API Models Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-api-models.j2', 'documentation/management-api-models.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&15=39&16=41&17=44&18=46&19=50&20=53&29=62'