from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-accounting.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_accounting = resolve('aaa_accounting')
    l_0_aaa_accounting_exec_console_cli = resolve('aaa_accounting_exec_console_cli')
    l_0_aaa_accounting_exec_default_cli = resolve('aaa_accounting_exec_default_cli')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting)):
        pass
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'type')):
            pass
            l_0_aaa_accounting_exec_console_cli = 'aaa accounting exec console'
            context.vars['aaa_accounting_exec_console_cli'] = l_0_aaa_accounting_exec_console_cli
            context.exported_vars.add('aaa_accounting_exec_console_cli')
            if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'type'), 'none'):
                pass
                l_0_aaa_accounting_exec_console_cli = str_join(((undefined(name='aaa_accounting_exec_console_cli') if l_0_aaa_accounting_exec_console_cli is missing else l_0_aaa_accounting_exec_console_cli), ' none', ))
                context.vars['aaa_accounting_exec_console_cli'] = l_0_aaa_accounting_exec_console_cli
                context.exported_vars.add('aaa_accounting_exec_console_cli')
            else:
                pass
                l_0_aaa_accounting_exec_console_cli = str_join(((undefined(name='aaa_accounting_exec_console_cli') if l_0_aaa_accounting_exec_console_cli is missing else l_0_aaa_accounting_exec_console_cli), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'type'), ))
                context.vars['aaa_accounting_exec_console_cli'] = l_0_aaa_accounting_exec_console_cli
                context.exported_vars.add('aaa_accounting_exec_console_cli')
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'group')):
                    pass
                    l_0_aaa_accounting_exec_console_cli = str_join(((undefined(name='aaa_accounting_exec_console_cli') if l_0_aaa_accounting_exec_console_cli is missing else l_0_aaa_accounting_exec_console_cli), ' group ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'group'), ))
                    context.vars['aaa_accounting_exec_console_cli'] = l_0_aaa_accounting_exec_console_cli
                    context.exported_vars.add('aaa_accounting_exec_console_cli')
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'console'), 'logging'), True):
                    pass
                    l_0_aaa_accounting_exec_console_cli = str_join(((undefined(name='aaa_accounting_exec_console_cli') if l_0_aaa_accounting_exec_console_cli is missing else l_0_aaa_accounting_exec_console_cli), ' logging', ))
                    context.vars['aaa_accounting_exec_console_cli'] = l_0_aaa_accounting_exec_console_cli
                    context.exported_vars.add('aaa_accounting_exec_console_cli')
            yield str((undefined(name='aaa_accounting_exec_console_cli') if l_0_aaa_accounting_exec_console_cli is missing else l_0_aaa_accounting_exec_console_cli))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'console')):
            pass
            for l_1_command_default in environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'console'):
                l_1_aaa_accounting_commands_commands_console_cli = resolve('aaa_accounting_commands_commands_console_cli')
                _loop_vars = {}
                pass
                if (t_1(environment.getattr(l_1_command_default, 'commands')) and t_1(environment.getattr(l_1_command_default, 'type'))):
                    pass
                    l_1_aaa_accounting_commands_commands_console_cli = str_join(('aaa accounting commands ', environment.getattr(l_1_command_default, 'commands'), ' console ', environment.getattr(l_1_command_default, 'type'), ))
                    _loop_vars['aaa_accounting_commands_commands_console_cli'] = l_1_aaa_accounting_commands_commands_console_cli
                    if t_1(environment.getattr(l_1_command_default, 'group')):
                        pass
                        l_1_aaa_accounting_commands_commands_console_cli = str_join(((undefined(name='aaa_accounting_commands_commands_console_cli') if l_1_aaa_accounting_commands_commands_console_cli is missing else l_1_aaa_accounting_commands_commands_console_cli), ' group ', environment.getattr(l_1_command_default, 'group'), ))
                        _loop_vars['aaa_accounting_commands_commands_console_cli'] = l_1_aaa_accounting_commands_commands_console_cli
                    if t_1(environment.getattr(l_1_command_default, 'logging'), True):
                        pass
                        l_1_aaa_accounting_commands_commands_console_cli = str_join(((undefined(name='aaa_accounting_commands_commands_console_cli') if l_1_aaa_accounting_commands_commands_console_cli is missing else l_1_aaa_accounting_commands_commands_console_cli), ' logging', ))
                        _loop_vars['aaa_accounting_commands_commands_console_cli'] = l_1_aaa_accounting_commands_commands_console_cli
                yield str((undefined(name='aaa_accounting_commands_commands_console_cli') if l_1_aaa_accounting_commands_commands_console_cli is missing else l_1_aaa_accounting_commands_commands_console_cli))
                yield '\n'
            l_1_command_default = l_1_aaa_accounting_commands_commands_console_cli = missing
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'type')):
            pass
            l_0_aaa_accounting_exec_default_cli = 'aaa accounting exec default'
            context.vars['aaa_accounting_exec_default_cli'] = l_0_aaa_accounting_exec_default_cli
            context.exported_vars.add('aaa_accounting_exec_default_cli')
            if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'type'), 'none'):
                pass
                l_0_aaa_accounting_exec_default_cli = str_join(((undefined(name='aaa_accounting_exec_default_cli') if l_0_aaa_accounting_exec_default_cli is missing else l_0_aaa_accounting_exec_default_cli), ' none', ))
                context.vars['aaa_accounting_exec_default_cli'] = l_0_aaa_accounting_exec_default_cli
                context.exported_vars.add('aaa_accounting_exec_default_cli')
            else:
                pass
                l_0_aaa_accounting_exec_default_cli = str_join(((undefined(name='aaa_accounting_exec_default_cli') if l_0_aaa_accounting_exec_default_cli is missing else l_0_aaa_accounting_exec_default_cli), ' ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'type'), ))
                context.vars['aaa_accounting_exec_default_cli'] = l_0_aaa_accounting_exec_default_cli
                context.exported_vars.add('aaa_accounting_exec_default_cli')
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'group')):
                    pass
                    l_0_aaa_accounting_exec_default_cli = str_join(((undefined(name='aaa_accounting_exec_default_cli') if l_0_aaa_accounting_exec_default_cli is missing else l_0_aaa_accounting_exec_default_cli), ' group ', environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'group'), ))
                    context.vars['aaa_accounting_exec_default_cli'] = l_0_aaa_accounting_exec_default_cli
                    context.exported_vars.add('aaa_accounting_exec_default_cli')
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'exec'), 'default'), 'logging'), True):
                    pass
                    l_0_aaa_accounting_exec_default_cli = str_join(((undefined(name='aaa_accounting_exec_default_cli') if l_0_aaa_accounting_exec_default_cli is missing else l_0_aaa_accounting_exec_default_cli), ' logging', ))
                    context.vars['aaa_accounting_exec_default_cli'] = l_0_aaa_accounting_exec_default_cli
                    context.exported_vars.add('aaa_accounting_exec_default_cli')
            yield str((undefined(name='aaa_accounting_exec_default_cli') if l_0_aaa_accounting_exec_default_cli is missing else l_0_aaa_accounting_exec_default_cli))
            yield '\n'
        if (t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'type')) and t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'group'))):
            pass
            yield 'aaa accounting system default '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'type'))
            yield ' group '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'system'), 'default'), 'group'))
            yield '\n'
        if (t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'type')) and t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'group'))):
            pass
            yield 'aaa accounting dot1x default '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'type'))
            yield ' group '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'dot1x'), 'default'), 'group'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'default')):
            pass
            for l_1_command_default in environment.getattr(environment.getattr((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting), 'commands'), 'default'):
                l_1_aaa_accounting_commands_commands_default_cli = resolve('aaa_accounting_commands_commands_default_cli')
                _loop_vars = {}
                pass
                if (t_1(environment.getattr(l_1_command_default, 'commands')) and t_1(environment.getattr(l_1_command_default, 'type'))):
                    pass
                    l_1_aaa_accounting_commands_commands_default_cli = str_join(('aaa accounting commands ', environment.getattr(l_1_command_default, 'commands'), ' default ', environment.getattr(l_1_command_default, 'type'), ))
                    _loop_vars['aaa_accounting_commands_commands_default_cli'] = l_1_aaa_accounting_commands_commands_default_cli
                    if t_1(environment.getattr(l_1_command_default, 'group')):
                        pass
                        l_1_aaa_accounting_commands_commands_default_cli = str_join(((undefined(name='aaa_accounting_commands_commands_default_cli') if l_1_aaa_accounting_commands_commands_default_cli is missing else l_1_aaa_accounting_commands_commands_default_cli), ' group ', environment.getattr(l_1_command_default, 'group'), ))
                        _loop_vars['aaa_accounting_commands_commands_default_cli'] = l_1_aaa_accounting_commands_commands_default_cli
                    if t_1(environment.getattr(l_1_command_default, 'logging'), True):
                        pass
                        l_1_aaa_accounting_commands_commands_default_cli = str_join(((undefined(name='aaa_accounting_commands_commands_default_cli') if l_1_aaa_accounting_commands_commands_default_cli is missing else l_1_aaa_accounting_commands_commands_default_cli), ' logging', ))
                        _loop_vars['aaa_accounting_commands_commands_default_cli'] = l_1_aaa_accounting_commands_commands_default_cli
                yield str((undefined(name='aaa_accounting_commands_commands_default_cli') if l_1_aaa_accounting_commands_commands_default_cli is missing else l_1_aaa_accounting_commands_commands_default_cli))
                yield '\n'
            l_1_command_default = l_1_aaa_accounting_commands_commands_default_cli = missing

blocks = {}
debug_info = '7=20&8=22&9=24&10=27&11=29&13=34&14=37&15=39&17=42&18=44&21=47&23=49&24=51&25=55&26=57&27=59&28=61&30=63&31=65&34=67&37=70&38=72&39=75&40=77&42=82&43=85&44=87&46=90&47=92&50=95&52=97&53=100&55=104&56=107&58=111&59=113&60=117&61=119&62=121&63=123&65=125&66=127&69=129'