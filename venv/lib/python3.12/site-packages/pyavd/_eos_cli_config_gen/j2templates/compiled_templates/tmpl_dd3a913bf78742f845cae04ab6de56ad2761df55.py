from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/aaa-authorization.j2'

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
        yield '\n### AAA Authorization\n\n#### AAA Authorization Summary\n\n| Type | User Stores |\n| ---- | ----------- |\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'exec'), 'default')):
            pass
            yield '| Exec | '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'exec'), 'default'))
            yield ' |\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'policy'), 'local_default_role')):
            pass
            yield '| Default Role | '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'policy'), 'local_default_role'))
            yield ' |\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'dynamic'), 'dot1x_additional_groups')):
            pass
            yield '| Additional Dynamic Authorization Groups | '
            yield str(t_2(context.eval_ctx, environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'dynamic'), 'dot1x_additional_groups'), ', '))
            yield ' |\n'
        if t_3(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'config_commands'), True):
            pass
            yield '\nAuthorization for configuration commands is enabled.\n'
        else:
            pass
            yield '\nAuthorization for configuration commands is disabled.\n'
        if t_3(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'serial_console'), True):
            pass
            yield '\nAuthorization for serial console is enabled.\n'
        if (t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'privilege')) or t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'all_default'))):
            pass
            yield '\n#### AAA Authorization Privilege Levels Summary\n\n| Privilege Level | User Stores |\n| --------------- | ----------- |\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'all_default')):
                pass
                yield '| all | '
                yield str(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'all_default'))
                yield ' |\n'
            for l_1_command_level in t_1(environment.getattr(environment.getattr((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization), 'commands'), 'privilege')):
                _loop_vars = {}
                pass
                if (t_3(environment.getattr(l_1_command_level, 'level')) and t_3(environment.getattr(l_1_command_level, 'default'))):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_command_level, 'level'))
                    yield ' | '
                    yield str(environment.getattr(l_1_command_level, 'default'))
                    yield ' |\n'
            l_1_command_level = missing
        yield '\n#### AAA Authorization Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/aaa-authorization.j2', 'documentation/aaa-authorization.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '!\n```\n'

blocks = {}
debug_info = '7=30&15=33&16=36&18=38&19=41&21=43&22=46&24=48&31=54&35=57&41=60&42=63&44=65&45=68&46=71&54=77'