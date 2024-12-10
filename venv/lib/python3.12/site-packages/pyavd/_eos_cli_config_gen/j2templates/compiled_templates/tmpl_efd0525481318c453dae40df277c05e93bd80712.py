from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-authorization.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_authorization = resolve('aaa_authorization')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization)):
        pass
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'policy'), 'local_default_role')):
            pass
            yield 'aaa authorization policy local default-role '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'policy'), 'local_default_role'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'serial_console'), True):
            pass
            yield 'aaa authorization serial-console\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'dynamic'), 'dot1x_additional_groups')):
            pass
            yield 'aaa authorization dynamic dot1x additional-groups group '
            yield str(t_2(context.eval_ctx, environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'dynamic'), 'dot1x_additional_groups'), ' group '))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'exec'), 'default')):
            pass
            yield 'aaa authorization exec default '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'exec'), 'default'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'config_commands'), False):
            pass
            yield 'no aaa authorization config-commands\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'all_default')):
            pass
            yield 'aaa authorization commands all default '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'all_default'))
            yield '\n'
        for l_1_command_level in t_1(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'privilege')):
            l_1_commands_privilege_cli = resolve('commands_privilege_cli')
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_command_level, 'level')) and t_3(environment.getattr(l_1_command_level, 'default'))):
                pass
                l_1_commands_privilege_cli = str_join(('aaa authorization commands ', environment.getattr(l_1_command_level, 'level'), ' default ', environment.getattr(l_1_command_level, 'default'), ))
                _loop_vars['commands_privilege_cli'] = l_1_commands_privilege_cli
                yield str((undefined(name='commands_privilege_cli') if l_1_commands_privilege_cli is missing else l_1_commands_privilege_cli))
                yield '\n'
        l_1_command_level = l_1_commands_privilege_cli = missing

blocks = {}
debug_info = '7=30&8=32&9=35&11=37&14=40&15=43&17=45&18=48&20=50&23=53&24=56&26=58&27=62&28=64&29=66'