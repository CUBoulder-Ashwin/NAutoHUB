from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/interface-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_groups = resolve('interface_groups')
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
    if t_4((undefined(name='interface_groups') if l_0_interface_groups is missing else l_0_interface_groups)):
        pass
        yield '\n### Interface Groups\n\n#### Interface Groups Summary\n\n| Interface Group | Interfaces | Interface maintenance profile | BGP maintenance profiles |\n| --------------- | ---------- | ----------------------------- | ------------------------ |\n'
        for l_1_interface_group in t_2((undefined(name='interface_groups') if l_0_interface_groups is missing else l_0_interface_groups), 'name'):
            l_1_interface_profile = resolve('interface_profile')
            l_1_maintenance = resolve('maintenance')
            l_1_bgp_profile = resolve('bgp_profile')
            l_1_interfaces = missing
            _loop_vars = {}
            pass
            l_1_interfaces = t_3(context.eval_ctx, t_2(environment.getattr(l_1_interface_group, 'interfaces')), '<br>')
            _loop_vars['interfaces'] = l_1_interfaces
            if t_4(environment.getattr(l_1_interface_group, 'interface_maintenance_profiles')):
                pass
                l_1_interface_profile = t_3(context.eval_ctx, t_2(environment.getattr(l_1_interface_group, 'interface_maintenance_profiles')), '<br>')
                _loop_vars['interface_profile'] = l_1_interface_profile
            else:
                pass
                l_1_interface_profile = t_1(environment.getattr((undefined(name='maintenance') if l_1_maintenance is missing else l_1_maintenance), 'default_interface_profile'), 'Default')
                _loop_vars['interface_profile'] = l_1_interface_profile
            if t_4(environment.getattr(l_1_interface_group, 'bgp_maintenance_profiles')):
                pass
                l_1_bgp_profile = t_3(context.eval_ctx, t_2(environment.getattr(l_1_interface_group, 'bgp_maintenance_profiles')), '<br>')
                _loop_vars['bgp_profile'] = l_1_bgp_profile
            else:
                pass
                l_1_bgp_profile = t_1(environment.getattr((undefined(name='maintenance') if l_1_maintenance is missing else l_1_maintenance), 'default_bgp_profile'), 'Default')
                _loop_vars['bgp_profile'] = l_1_bgp_profile
            yield '| '
            yield str(environment.getattr(l_1_interface_group, 'name'))
            yield ' | '
            yield str((undefined(name='interfaces') if l_1_interfaces is missing else l_1_interfaces))
            yield ' | '
            yield str((undefined(name='interface_profile') if l_1_interface_profile is missing else l_1_interface_profile))
            yield ' | '
            yield str((undefined(name='bgp_profile') if l_1_bgp_profile is missing else l_1_bgp_profile))
            yield ' |\n'
        l_1_interface_group = l_1_interfaces = l_1_interface_profile = l_1_maintenance = l_1_bgp_profile = missing
        yield '\n#### Interface Groups Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/interface-groups.j2', 'documentation/interface-groups.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&15=39&16=46&17=48&18=50&20=54&22=56&23=58&25=62&27=65&33=75'