from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/policy-maps-pbr.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_policy_maps = resolve('policy_maps')
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
    if t_3(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'pbr')):
        pass
        yield '\n### PBR Policy Maps\n\n#### PBR Policy Maps Summary\n'
        for l_1_policy_map in t_2(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'pbr'), 'name'):
            _loop_vars = {}
            pass
            yield '\n##### '
            yield str(environment.getattr(l_1_policy_map, 'name'))
            yield '\n'
            if t_3(environment.getattr(l_1_policy_map, 'classes')):
                pass
                yield '\n| Class | Index | Drop | Nexthop | Recursive |\n| ----- | ----- | ---- | ------- | --------- |\n'
                for l_2_class in environment.getattr(l_1_policy_map, 'classes'):
                    l_2_index = l_2_drop = l_2_nexthop = l_2_recur = missing
                    _loop_vars = {}
                    pass
                    l_2_index = t_1(environment.getattr(l_2_class, 'index'), '-')
                    _loop_vars['index'] = l_2_index
                    l_2_drop = t_1(environment.getattr(l_2_class, 'drop'), '-')
                    _loop_vars['drop'] = l_2_drop
                    l_2_nexthop = t_1(environment.getattr(environment.getattr(environment.getattr(l_2_class, 'set'), 'nexthop'), 'ip_address'), '-')
                    _loop_vars['nexthop'] = l_2_nexthop
                    l_2_recur = t_1(environment.getattr(environment.getattr(environment.getattr(l_2_class, 'set'), 'nexthop'), 'recursive'), '-')
                    _loop_vars['recur'] = l_2_recur
                    yield '| '
                    yield str(environment.getattr(l_2_class, 'name'))
                    yield ' | '
                    yield str((undefined(name='index') if l_2_index is missing else l_2_index))
                    yield ' | '
                    yield str((undefined(name='drop') if l_2_drop is missing else l_2_drop))
                    yield ' | '
                    yield str((undefined(name='nexthop') if l_2_nexthop is missing else l_2_nexthop))
                    yield ' | '
                    yield str((undefined(name='recur') if l_2_recur is missing else l_2_recur))
                    yield ' |\n'
                l_2_class = l_2_index = l_2_drop = l_2_nexthop = l_2_recur = missing
        l_1_policy_map = missing
        yield '\n#### PBR Policy Maps Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/policy-maps-pbr.j2', 'documentation/policy-maps-pbr.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&14=37&15=39&19=42&20=46&21=48&22=50&23=52&24=55&32=68'