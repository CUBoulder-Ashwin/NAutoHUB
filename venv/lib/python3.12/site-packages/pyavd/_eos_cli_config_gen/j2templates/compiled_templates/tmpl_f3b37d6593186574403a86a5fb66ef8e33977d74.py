from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/aaa-server-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_server_groups = resolve('aaa_server_groups')
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
    if t_2((undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups)):
        pass
        yield '\n### AAA Server Groups\n\n#### AAA Server Groups Summary\n\n| Server Group Name | Type  | VRF | IP address |\n| ------------------| ----- | --- | ---------- |\n'
        for l_1_aaa_server_group in (undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups):
            _loop_vars = {}
            pass
            for l_2_server in environment.getattr(l_1_aaa_server_group, 'servers'):
                l_2_vrf = missing
                _loop_vars = {}
                pass
                l_2_vrf = t_1(environment.getattr(l_2_server, 'vrf'), 'default')
                _loop_vars['vrf'] = l_2_vrf
                yield '| '
                yield str(environment.getattr(l_1_aaa_server_group, 'name'))
                yield ' | '
                yield str(environment.getattr(l_1_aaa_server_group, 'type'))
                yield ' | '
                yield str((undefined(name='vrf') if l_2_vrf is missing else l_2_vrf))
                yield ' | '
                yield str(environment.getattr(l_2_server, 'server'))
                yield ' |\n'
            l_2_server = l_2_vrf = missing
        l_1_aaa_server_group = missing
        yield '\n#### AAA Server Groups Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/aaa-server-groups-ldap.j2', 'documentation/aaa-server-groups.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('eos/aaa-server-groups-radius.j2', 'documentation/aaa-server-groups.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('eos/aaa-server-groups-tacacs-plus.j2', 'documentation/aaa-server-groups.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=30&17=34&18=37&25=48&26=51&27=54'