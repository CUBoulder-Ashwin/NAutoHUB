from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/stun.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_stun = resolve('stun')
    l_0_bindings_timeout = resolve('bindings_timeout')
    l_0_ssl_profile = resolve('ssl_profile')
    l_0_stun_port = resolve('stun_port')
    l_0_lifetime = resolve('lifetime')
    l_0_interface_list = resolve('interface_list')
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='stun') if l_0_stun is missing else l_0_stun)):
        pass
        yield '\n## STUN\n'
        if t_4(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client')):
            pass
            yield '\n### STUN Client\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles')):
                pass
                yield '\n#### Server Profiles\n\n| Server Profile | IP address | SSL Profile | Port |\n| -------------- | ---------- | ----------- | ---- |\n'
                for l_1_server_profile in t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'client'), 'server_profiles'), 'name'):
                    l_1_ssl_profile = l_0_ssl_profile
                    l_1_stun_port = l_0_stun_port
                    _loop_vars = {}
                    pass
                    l_1_ssl_profile = t_1(environment.getattr(l_1_server_profile, 'ssl_profile'), '-')
                    _loop_vars['ssl_profile'] = l_1_ssl_profile
                    l_1_stun_port = t_1(environment.getattr(l_1_server_profile, 'port'), '3478')
                    _loop_vars['stun_port'] = l_1_stun_port
                    yield '| '
                    yield str(environment.getattr(l_1_server_profile, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_server_profile, 'ip_address'))
                    yield ' | '
                    yield str((undefined(name='ssl_profile') if l_1_ssl_profile is missing else l_1_ssl_profile))
                    yield ' | '
                    yield str((undefined(name='stun_port') if l_1_stun_port is missing else l_1_stun_port))
                    yield ' |\n'
                l_1_server_profile = l_1_ssl_profile = l_1_stun_port = missing
        if t_4(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server')):
            pass
            yield '\n### STUN Server\n\n| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |\n| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |\n'
            l_0_bindings_timeout = t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'bindings_timeout'), '-')
            context.vars['bindings_timeout'] = l_0_bindings_timeout
            context.exported_vars.add('bindings_timeout')
            l_0_ssl_profile = t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_profile'), '-')
            context.vars['ssl_profile'] = l_0_ssl_profile
            context.exported_vars.add('ssl_profile')
            l_0_stun_port = t_1(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'port'), '3478')
            context.vars['stun_port'] = l_0_stun_port
            context.exported_vars.add('stun_port')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'minutes')):
                pass
                l_0_lifetime = str_join((environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'minutes'), ' minutes', ))
                context.vars['lifetime'] = l_0_lifetime
                context.exported_vars.add('lifetime')
            elif t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'hours')):
                pass
                l_0_lifetime = str_join((environment.getattr(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'ssl_connection_lifetime'), 'hours'), ' hours', ))
                context.vars['lifetime'] = l_0_lifetime
                context.exported_vars.add('lifetime')
            else:
                pass
                l_0_lifetime = '-'
                context.vars['lifetime'] = l_0_lifetime
                context.exported_vars.add('lifetime')
            l_0_interface_list = t_2(environment.getattr(environment.getattr((undefined(name='stun') if l_0_stun is missing else l_0_stun), 'server'), 'local_interfaces'))
            context.vars['interface_list'] = l_0_interface_list
            context.exported_vars.add('interface_list')
            yield '| '
            yield str(t_3(context.eval_ctx, (undefined(name='interface_list') if l_0_interface_list is missing else l_0_interface_list), '<br>'))
            yield ' | '
            yield str((undefined(name='bindings_timeout') if l_0_bindings_timeout is missing else l_0_bindings_timeout))
            yield ' | '
            yield str((undefined(name='ssl_profile') if l_0_ssl_profile is missing else l_0_ssl_profile))
            yield ' | '
            yield str((undefined(name='lifetime') if l_0_lifetime is missing else l_0_lifetime))
            yield ' | '
            yield str((undefined(name='stun_port') if l_0_stun_port is missing else l_0_stun_port))
            yield ' |\n'
        yield '\n### STUN Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/stun.j2', 'documentation/stun.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'bindings_timeout': l_0_bindings_timeout, 'interface_list': l_0_interface_list, 'lifetime': l_0_lifetime, 'ssl_profile': l_0_ssl_profile, 'stun_port': l_0_stun_port})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=41&10=44&13=47&19=50&20=55&21=57&22=60&26=69&32=72&33=75&34=78&35=81&36=83&37=86&38=88&40=93&42=96&43=100&49=111'