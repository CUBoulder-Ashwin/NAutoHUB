from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mcs-client.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mcs_client = resolve('mcs_client')
    l_0_secondary = resolve('secondary')
    l_0_servers = resolve('servers')
    l_0_enabled = resolve('enabled')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
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
    if t_3((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client)):
        pass
        yield '\n### MCS Client Summary\n'
        if t_3(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'shutdown'), True):
            pass
            yield '\nMCS client is shutdown\n'
        elif t_3(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'shutdown'), False):
            pass
            yield '\nMCS client is enabled\n'
        if t_3(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary')):
            pass
            yield '\n| Secondary CVX cluster | Server Hosts | Enabled |\n| --------------------- | ------------ | ------- |\n'
            l_0_secondary = environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'name')
            context.vars['secondary'] = l_0_secondary
            context.exported_vars.add('secondary')
            l_0_servers = t_2(context.eval_ctx, t_1(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'server_hosts'), '-'), ', ')
            context.vars['servers'] = l_0_servers
            context.exported_vars.add('servers')
            if t_3(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'shutdown')):
                pass
                l_0_enabled = (not environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'shutdown'))
                context.vars['enabled'] = l_0_enabled
                context.exported_vars.add('enabled')
            else:
                pass
                l_0_enabled = '-'
                context.vars['enabled'] = l_0_enabled
                context.exported_vars.add('enabled')
            yield '| '
            yield str((undefined(name='secondary') if l_0_secondary is missing else l_0_secondary))
            yield ' | '
            yield str((undefined(name='servers') if l_0_servers is missing else l_0_servers))
            yield ' | '
            yield str((undefined(name='enabled') if l_0_enabled is missing else l_0_enabled))
            yield ' |\n'
        yield '\n#### MCS Client Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mcs-client.j2', 'documentation/mcs-client.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'enabled': l_0_enabled, 'secondary': l_0_secondary, 'servers': l_0_servers})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=33&10=36&13=39&17=42&21=45&22=48&23=51&24=53&26=58&28=62&34=69'