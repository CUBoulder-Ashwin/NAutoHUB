from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/aaa-accounting.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_accounting = resolve('aaa_accounting')
    l_0_aaa_accounting_logging = resolve('aaa_accounting_logging')
    l_0_aaa_accounting_group = resolve('aaa_accounting_group')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting)):
        pass
        yield '\n### AAA Accounting\n\n#### AAA Accounting Summary\n\n| Type | Commands | Record type | Group | Logging |\n| ---- | -------- | ----------- | ----- | ------- |\n'
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'type')):
            pass
            l_0_aaa_accounting_logging = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'logging'), '-')
            context.vars['aaa_accounting_logging'] = l_0_aaa_accounting_logging
            context.exported_vars.add('aaa_accounting_logging')
            l_0_aaa_accounting_group = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'group'), '-')
            context.vars['aaa_accounting_group'] = l_0_aaa_accounting_group
            context.exported_vars.add('aaa_accounting_group')
            yield '| Exec - Console | - | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'type'))
            yield ' | '
            yield str((undefined(name='aaa_accounting_group') if l_0_aaa_accounting_group is missing else l_0_aaa_accounting_group))
            yield ' | '
            yield str((undefined(name='aaa_accounting_logging') if l_0_aaa_accounting_logging is missing else l_0_aaa_accounting_logging))
            yield ' |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'console')):
            pass
            for l_1_command_console in environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'console'):
                l_1_group = resolve('group')
                l_1_logging = resolve('logging')
                _loop_vars = {}
                pass
                if (t_2(environment.getattr(l_1_command_console, 'commands')) and t_2(environment.getattr(l_1_command_console, 'type'))):
                    pass
                    l_1_group = t_1(environment.getattr(l_1_command_console, 'group'), ' - ')
                    _loop_vars['group'] = l_1_group
                    l_1_logging = t_1(environment.getattr(l_1_command_console, 'logging'), 'False')
                    _loop_vars['logging'] = l_1_logging
                    yield '| Commands - Console | '
                    yield str(environment.getattr(l_1_command_console, 'commands'))
                    yield ' | '
                    yield str(environment.getattr(l_1_command_console, 'type'))
                    yield ' | '
                    yield str((undefined(name='group') if l_1_group is missing else l_1_group))
                    yield ' | '
                    yield str((undefined(name='logging') if l_1_logging is missing else l_1_logging))
                    yield ' |\n'
            l_1_command_console = l_1_group = l_1_logging = missing
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'type')):
            pass
            l_0_aaa_accounting_logging = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'logging'), '-')
            context.vars['aaa_accounting_logging'] = l_0_aaa_accounting_logging
            context.exported_vars.add('aaa_accounting_logging')
            l_0_aaa_accounting_group = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'group'), '-')
            context.vars['aaa_accounting_group'] = l_0_aaa_accounting_group
            context.exported_vars.add('aaa_accounting_group')
            yield '| Exec - Default | - | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'type'))
            yield ' | '
            yield str((undefined(name='aaa_accounting_group') if l_0_aaa_accounting_group is missing else l_0_aaa_accounting_group))
            yield ' | '
            yield str((undefined(name='aaa_accounting_logging') if l_0_aaa_accounting_logging is missing else l_0_aaa_accounting_logging))
            yield ' |\n'
        if (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'type')) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'group'))):
            pass
            yield '| System - Default | - | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'type'))
            yield ' | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'group'))
            yield ' | - |\n'
        if (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'type')) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'group'))):
            pass
            yield '| Dot1x - Default  | - | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'type'))
            yield ' | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'group'))
            yield ' | - |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'default')):
            pass
            for l_1_command_default in environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'default'):
                l_1_logging = resolve('logging')
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_1_command_default, 'logging'), True):
                    pass
                    l_1_logging = 'True'
                    _loop_vars['logging'] = l_1_logging
                else:
                    pass
                    l_1_logging = 'False'
                    _loop_vars['logging'] = l_1_logging
                yield '| Commands - Default | '
                yield str(environment.getattr(l_1_command_default, 'commands'))
                yield ' | '
                yield str(environment.getattr(l_1_command_default, 'type'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_command_default, 'group'), '-'))
                yield ' | '
                yield str((undefined(name='logging') if l_1_logging is missing else l_1_logging))
                yield ' |\n'
            l_1_command_default = l_1_logging = missing
        yield '\n#### AAA Accounting Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/aaa-accounting.j2', 'documentation/aaa-accounting.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'aaa_accounting_group': l_0_aaa_accounting_group, 'aaa_accounting_logging': l_0_aaa_accounting_logging})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=26&15=29&16=31&17=34&18=38&20=44&21=46&22=51&23=53&24=55&25=58&29=67&30=69&31=72&32=76&34=82&35=85&37=89&38=92&40=96&41=98&42=102&43=104&45=108&47=111&54=121'