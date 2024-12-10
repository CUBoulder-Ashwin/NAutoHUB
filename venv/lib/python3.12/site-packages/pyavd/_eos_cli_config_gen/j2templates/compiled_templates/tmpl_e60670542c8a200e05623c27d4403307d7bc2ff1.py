from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-name-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_name_servers = resolve('ip_name_servers')
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
    if t_2((undefined(name='ip_name_servers') if l_0_ip_name_servers is missing else l_0_ip_name_servers)):
        pass
        yield '\n### IP Name Servers\n\n#### IP Name Servers Summary\n\n| Name Server | VRF | Priority |\n| ----------- | --- | -------- |\n'
        for l_1_name_server in t_1((undefined(name='ip_name_servers') if l_0_ip_name_servers is missing else l_0_ip_name_servers), []):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_name_server, 'ip_address'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_name_server, 'vrf'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_name_server, 'priority'), '-'))
            yield ' |\n'
        l_1_name_server = missing
        yield '\n#### IP Name Servers Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-name-servers.j2', 'documentation/ip-name-servers.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=31&22=39'