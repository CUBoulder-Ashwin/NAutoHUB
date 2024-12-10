from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/tcam-profile.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tcam_profile = resolve('tcam_profile')
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
    if t_2((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile)):
        pass
        yield '\n## Hardware TCAM Profile\n\nTCAM profile **`'
        yield str(t_1(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'system'), 'default'))
        yield '`** is active\n'
        if t_2(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'profiles')):
            pass
            yield '\n### Custom TCAM Profiles\n\nFollowing TCAM profiles are configured on device:\n\n'
            for l_1_profile in environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'profiles'):
                _loop_vars = {}
                pass
                yield '- Profile Name: `'
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '`\n'
            l_1_profile = missing
        yield '\n### Hardware TCAM Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/tcam-profile.j2', 'documentation/tcam-profile.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&11=27&12=29&18=32&19=36&26=40'