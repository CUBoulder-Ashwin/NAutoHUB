from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-cvx.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_cvx = resolve('management_cvx')
    l_0_shut = resolve('shut')
    l_0_servers = resolve('servers')
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
    if t_3((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx)):
        pass
        yield '\n### Management CVX Summary\n\n| Shutdown | CVX Servers |\n| -------- | ----------- |\n'
        l_0_shut = t_1(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'shutdown'), '-')
        context.vars['shut'] = l_0_shut
        context.exported_vars.add('shut')
        l_0_servers = t_2(context.eval_ctx, t_1(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'server_hosts'), '-'), ', ')
        context.vars['servers'] = l_0_servers
        context.exported_vars.add('servers')
        yield '| '
        yield str((undefined(name='shut') if l_0_shut is missing else l_0_shut))
        yield ' | '
        yield str((undefined(name='servers') if l_0_servers is missing else l_0_servers))
        yield ' |\n'
        if t_3(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'source_interface')):
            pass
            yield '\n#### Management CVX Source Interface\n\n| Interface | VRF |\n| --------- | --- |\n| '
            yield str(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'source_interface'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'vrf'), '-'))
            yield ' |\n'
        yield '\n#### Management CVX Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-cvx.j2', 'documentation/management-cvx.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'servers': l_0_servers, 'shut': l_0_shut})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=32&13=35&14=38&15=42&16=46&22=49&28=54'