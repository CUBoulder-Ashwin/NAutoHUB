from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-tech-support.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_tech_support = resolve('management_tech_support')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support)):
        pass
        yield '\n### Management Tech-Support\n'
        if t_3(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support')):
            pass
            yield '\n#### Policy\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'exclude_commands')):
                pass
                yield '\n##### Exclude Commands\n\n| Command | Type |\n| ------- | ---- |\n'
                if t_3(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'exclude_commands')):
                    pass
                    for l_1_exclude_command in environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'exclude_commands'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(t_2(context.eval_ctx, environment.getattr(l_1_exclude_command, 'command'), '|', '\\|'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_1_exclude_command, 'type'), 'text'))
                        yield ' |\n'
                    l_1_exclude_command = missing
            if t_3(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'include_commands')):
                pass
                yield '\n##### Include Commands\n\n| Command |\n| ------- |\n'
                if t_3(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'include_commands')):
                    pass
                    for l_1_include_command in environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'include_commands'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(t_2(context.eval_ctx, environment.getattr(l_1_include_command, 'command'), '|', '\\|'))
                        yield ' |\n'
                    l_1_include_command = missing
        yield '\n#### Policy Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-tech-support.j2', 'documentation/management-tech-support.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&10=33&13=36&19=39&20=41&21=45&25=50&31=53&32=55&33=59&42=63'