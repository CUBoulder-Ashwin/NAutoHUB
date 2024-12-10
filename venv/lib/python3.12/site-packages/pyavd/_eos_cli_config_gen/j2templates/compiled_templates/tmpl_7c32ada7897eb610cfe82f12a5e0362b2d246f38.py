from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-tacacs-source-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_tacacs_source_interfaces = resolve('ip_tacacs_source_interfaces')
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
    if t_2((undefined(name='ip_tacacs_source_interfaces') if l_0_ip_tacacs_source_interfaces is missing else l_0_ip_tacacs_source_interfaces)):
        pass
        yield '\n### IP TACACS Source Interfaces\n\n#### IP TACACS Source Interfaces\n\n| VRF | Source Interface Name |\n| --- | --------------- |\n'
        for l_1_ip_tacacs_source_interface in (undefined(name='ip_tacacs_source_interfaces') if l_0_ip_tacacs_source_interfaces is missing else l_0_ip_tacacs_source_interfaces):
            l_1_vrf = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_ip_tacacs_source_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            yield '| '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str(environment.getattr(l_1_ip_tacacs_source_interface, 'name'))
            yield ' |\n'
        l_1_ip_tacacs_source_interface = l_1_vrf = missing
        yield '\n#### IP TACACS Source Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-tacacs-source-interfaces.j2', 'documentation/ip-tacacs-source-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=31&17=34&23=40'