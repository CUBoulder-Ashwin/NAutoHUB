from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/tacacs-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tacacs_servers = resolve('tacacs_servers')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['default']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'default' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'hosts')):
        pass
        yield '\n### TACACS Servers\n\n#### TACACS Servers\n\n| VRF | TACACS Servers | Single-Connection | Timeout |\n| --- | -------------- | ----------------- | ------- |\n'
        for l_1_host in environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'hosts'):
            l_1_vrf = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_host, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            yield '| '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str(environment.getattr(l_1_host, 'host'))
            yield ' | '
            yield str(t_2(environment.getattr(l_1_host, 'single_connection'), False))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_host, 'timeout'), '-'))
            yield ' |\n'
        l_1_host = l_1_vrf = missing
        yield '\n'
        if (t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'policy_unknown_mandatory_attribute_ignore')) and (environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'policy_unknown_mandatory_attribute_ignore') == True)):
            pass
            yield 'Policy unknown-mandatory-attribute ignore is configured\n\n'
        if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'timeout')):
            pass
            yield 'Global timeout: '
            yield str(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'timeout'))
            yield ' seconds\n\n'
        yield '#### TACACS Servers Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/tacacs-servers.j2', 'documentation/tacacs-servers.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=37&17=40&20=50&24=53&25=56&31=59'