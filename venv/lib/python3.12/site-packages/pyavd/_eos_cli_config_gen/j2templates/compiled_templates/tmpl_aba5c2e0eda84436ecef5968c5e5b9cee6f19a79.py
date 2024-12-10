from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/aaa-authentication.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_authentication = resolve('aaa_authentication')
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
    try:
        t_3 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_2((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication)):
        pass
        yield '\n### AAA Authentication\n\n#### AAA Authentication Summary\n\n| Type | Sub-type | User Stores |\n| ---- | -------- | ---------- |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'default')):
            pass
            yield '| Login | default | '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'default'))
            yield ' |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'console')):
            pass
            yield '| Login | console | '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'login'), 'console'))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'on_failure_log'), True):
                pass
                yield '\nAAA Authentication on-failure log has been enabled\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'on_success_log'), True):
                pass
                yield '\nAAA Authentication on-success log has been enabled\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'local')):
                pass
                if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'local'), 'allow_nopassword'), True):
                    pass
                    yield '\nPolicy local allow-nopassword-remote-login has been enabled.\n'
            if (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'failure')) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'duration'))):
                pass
                yield '\nPolicy lockout has been enabled. After **'
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'failure'))
                yield '** failed login attempts within **'
                yield str(t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'window'), '1440'))
                yield "** minutes, you'll be locked out for **"
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication), 'policies'), 'lockout'), 'duration'))
                yield '** minutes.\n'
        yield '\n#### AAA Authentication Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/aaa-authentication.j2', 'documentation/aaa-authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '!\n```\n'

blocks = {}
debug_info = '7=30&15=33&16=36&18=38&19=41&21=43&22=45&26=48&30=51&31=53&36=56&38=59&45=66'