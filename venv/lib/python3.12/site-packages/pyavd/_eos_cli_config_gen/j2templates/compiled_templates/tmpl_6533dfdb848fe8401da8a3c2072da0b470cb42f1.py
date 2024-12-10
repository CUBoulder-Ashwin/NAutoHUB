from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/vmtracer-sessions.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vmtracer_sessions = resolve('vmtracer_sessions')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='vmtracer_sessions') if l_0_vmtracer_sessions is missing else l_0_vmtracer_sessions)):
        pass
        yield '\n### VM Tracer Sessions\n\n#### VM Tracer Summary\n\n| Session | URL | Username | Autovlan | VRF | Source Interface |\n| ------- | --- | -------- | -------- | --- | ---------------- |\n'
        for l_1_session in t_2((undefined(name='vmtracer_sessions') if l_0_vmtracer_sessions is missing else l_0_vmtracer_sessions), 'name'):
            l_1_autovlan = resolve('autovlan')
            l_1_url = l_1_username = l_1_vrf = l_1_source_interface = missing
            _loop_vars = {}
            pass
            l_1_url = t_1(environment.getattr(l_1_session, 'url'), '-')
            _loop_vars['url'] = l_1_url
            l_1_username = t_1(environment.getattr(l_1_session, 'username'), '-')
            _loop_vars['username'] = l_1_username
            if t_3(environment.getattr(l_1_session, 'autovlan_disable'), True):
                pass
                l_1_autovlan = 'disabled'
                _loop_vars['autovlan'] = l_1_autovlan
            l_1_vrf = t_1(environment.getattr(l_1_session, 'vrf'), '-')
            _loop_vars['vrf'] = l_1_vrf
            l_1_source_interface = t_1(environment.getattr(l_1_session, 'source_interface'), '-')
            _loop_vars['source_interface'] = l_1_source_interface
            yield '| '
            yield str(environment.getattr(l_1_session, 'name'))
            yield ' | '
            yield str((undefined(name='url') if l_1_url is missing else l_1_url))
            yield ' | '
            yield str((undefined(name='username') if l_1_username is missing else l_1_username))
            yield ' | '
            yield str(t_1((undefined(name='autovlan') if l_1_autovlan is missing else l_1_autovlan), 'enabled'))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='source_interface') if l_1_source_interface is missing else l_1_source_interface))
            yield ' |\n'
        l_1_session = l_1_url = l_1_username = l_1_autovlan = l_1_vrf = l_1_source_interface = missing
        yield '\n#### VM Tracer Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/vmtracer-sessions.j2', 'documentation/vmtracer-sessions.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=38&17=40&18=42&19=44&21=46&22=48&23=51&29=65'