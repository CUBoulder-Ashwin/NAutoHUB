from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/policy-maps-qos.j2'

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
    if t_3(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'qos')):
        pass
        yield '\n### QOS Policy Maps\n\n#### QOS Policy Maps Summary\n'
        for l_1_policy_map in t_2(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'qos'), 'name'):
            _loop_vars = {}
            pass
            yield '\n##### '
            yield str(environment.getattr(l_1_policy_map, 'name'))
            yield '\n\n| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |\n| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |\n'
            for l_2_class in t_1(environment.getattr(l_1_policy_map, 'classes'), []):
                l_2_police_rate = resolve('police_rate')
                l_2_cos = l_2_dscp = l_2_traffic_class = l_2_drop_precedence = l_2_police = missing
                _loop_vars = {}
                pass
                l_2_cos = t_1(environment.getattr(environment.getattr(l_2_class, 'set'), 'cos'), '-')
                _loop_vars['cos'] = l_2_cos
                l_2_dscp = t_1(environment.getattr(environment.getattr(l_2_class, 'set'), 'dscp'), '-')
                _loop_vars['dscp'] = l_2_dscp
                l_2_traffic_class = t_1(environment.getattr(environment.getattr(l_2_class, 'set'), 'traffic_class'), '-')
                _loop_vars['traffic_class'] = l_2_traffic_class
                l_2_drop_precedence = t_1(environment.getattr(environment.getattr(l_2_class, 'set'), 'drop_precedence'), '-')
                _loop_vars['drop_precedence'] = l_2_drop_precedence
                if (t_3(environment.getattr(environment.getattr(l_2_class, 'police'), 'rate')) and t_3(environment.getattr(environment.getattr(l_2_class, 'police'), 'rate_burst_size'))):
                    pass
                    l_2_police_rate = str_join((environment.getattr(environment.getattr(l_2_class, 'police'), 'rate'), ' ', t_1(environment.getattr(environment.getattr(l_2_class, 'police'), 'rate_unit'), 'bps'), ' (', environment.getattr(environment.getattr(l_2_class, 'police'), 'rate_burst_size'), ' ', t_1(environment.getattr(environment.getattr(l_2_class, 'police'), 'rate_burst_size_unit'), 'bytes'), ')', ))
                    _loop_vars['police_rate'] = l_2_police_rate
                    l_2_police_rate = str_join(((undefined(name='police_rate') if l_2_police_rate is missing else l_2_police_rate), ' -> ', t_1(environment.getattr(environment.getattr(environment.getattr(l_2_class, 'police'), 'action'), 'type'), 'drop'), ))
                    _loop_vars['police_rate'] = l_2_police_rate
                    if (t_3(environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate')) and t_3(environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate_burst_size'))):
                        pass
                        l_2_police_rate = str_join(((undefined(name='police_rate') if l_2_police_rate is missing else l_2_police_rate), '<br> ', environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate'), ' ', t_1(environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate_unit'), 'bps'), '(', environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate_burst_size'), ' ', t_1(environment.getattr(environment.getattr(l_2_class, 'police'), 'higher_rate_burst_size_unit'), 'bytes'), ') -> drop', ))
                        _loop_vars['police_rate'] = l_2_police_rate
                l_2_police = t_1((undefined(name='police_rate') if l_2_police_rate is missing else l_2_police_rate), '-')
                _loop_vars['police'] = l_2_police
                yield '| '
                yield str(environment.getattr(l_2_class, 'name'))
                yield ' | '
                yield str((undefined(name='cos') if l_2_cos is missing else l_2_cos))
                yield ' | '
                yield str((undefined(name='dscp') if l_2_dscp is missing else l_2_dscp))
                yield ' | '
                yield str((undefined(name='traffic_class') if l_2_traffic_class is missing else l_2_traffic_class))
                yield ' | '
                yield str((undefined(name='drop_precedence') if l_2_drop_precedence is missing else l_2_drop_precedence))
                yield ' | '
                yield str((undefined(name='police') if l_2_police is missing else l_2_police))
                yield ' |\n'
            l_2_class = l_2_cos = l_2_dscp = l_2_traffic_class = l_2_drop_precedence = l_2_police_rate = l_2_police = missing
        l_1_policy_map = missing
        yield '\n#### QOS Policy Maps Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/policy-maps-qos.j2', 'documentation/policy-maps-qos.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&14=37&18=39&19=44&20=46&21=48&22=50&23=52&24=54&25=56&26=58&27=60&30=62&31=65&38=80'