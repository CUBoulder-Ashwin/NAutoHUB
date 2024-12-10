from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitor-telemetry-postcard-policy.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_telemetry_postcard_policy = resolve('monitor_telemetry_postcard_policy')
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
    if t_4((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy)):
        pass
        yield '\n### Monitor Telemetry Postcard Policy\n'
        if t_4(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'sample_policies')):
            pass
            yield '\n#### Sample Policy Summary\n'
            for l_1_policy in t_2(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'sample_policies'), 'name'):
                _loop_vars = {}
                pass
                yield '\n##### '
                yield str(environment.getattr(l_1_policy, 'name'))
                yield '\n'
                if t_4(environment.getattr(l_1_policy, 'match_rules')):
                    pass
                    yield '\n###### Match rules\n\n| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |\n| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |\n'
                    for l_2_rule in t_2(environment.getattr(l_1_policy, 'match_rules'), 'name'):
                        l_2_protocols_list = l_2_destination_ports = l_2_source_ports = missing
                        _loop_vars = {}
                        pass
                        l_2_protocols_list = []
                        _loop_vars['protocols_list'] = l_2_protocols_list
                        l_2_destination_ports = []
                        _loop_vars['destination_ports'] = l_2_destination_ports
                        l_2_source_ports = []
                        _loop_vars['source_ports'] = l_2_source_ports
                        for l_3_protocol in t_2(environment.getattr(l_2_rule, 'protocols'), 'protocol'):
                            _loop_vars = {}
                            pass
                            context.call(environment.getattr((undefined(name='protocols_list') if l_2_protocols_list is missing else l_2_protocols_list), 'append'), environment.getattr(l_3_protocol, 'protocol'), _loop_vars=_loop_vars)
                            if t_4(environment.getattr(l_3_protocol, 'source_ports')):
                                pass
                                context.call(environment.getattr((undefined(name='source_ports') if l_2_source_ports is missing else l_2_source_ports), 'append'), t_3(context.eval_ctx, environment.getattr(l_3_protocol, 'source_ports'), ', '), _loop_vars=_loop_vars)
                            else:
                                pass
                                context.call(environment.getattr((undefined(name='source_ports') if l_2_source_ports is missing else l_2_source_ports), 'append'), '-', _loop_vars=_loop_vars)
                            if t_4(environment.getattr(l_3_protocol, 'destination_ports')):
                                pass
                                context.call(environment.getattr((undefined(name='destination_ports') if l_2_destination_ports is missing else l_2_destination_ports), 'append'), t_3(context.eval_ctx, environment.getattr(l_3_protocol, 'destination_ports'), ', '), _loop_vars=_loop_vars)
                            else:
                                pass
                                context.call(environment.getattr((undefined(name='destination_ports') if l_2_destination_ports is missing else l_2_destination_ports), 'append'), '-', _loop_vars=_loop_vars)
                        l_3_protocol = missing
                        if ((undefined(name='protocols_list') if l_2_protocols_list is missing else l_2_protocols_list) == []):
                            pass
                            context.call(environment.getattr((undefined(name='protocols_list') if l_2_protocols_list is missing else l_2_protocols_list), 'append'), '-', _loop_vars=_loop_vars)
                            context.call(environment.getattr((undefined(name='source_ports') if l_2_source_ports is missing else l_2_source_ports), 'append'), '-', _loop_vars=_loop_vars)
                            context.call(environment.getattr((undefined(name='destination_ports') if l_2_destination_ports is missing else l_2_destination_ports), 'append'), '-', _loop_vars=_loop_vars)
                        yield '| '
                        yield str(environment.getattr(l_2_rule, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_rule, 'type'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_rule, 'source_prefix'), '-'))
                        yield ' | '
                        yield str(t_1(environment.getattr(l_2_rule, 'destination_prefix'), '-'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, (undefined(name='protocols_list') if l_2_protocols_list is missing else l_2_protocols_list), '<br>'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, (undefined(name='source_ports') if l_2_source_ports is missing else l_2_source_ports), '<br>'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, (undefined(name='destination_ports') if l_2_destination_ports is missing else l_2_destination_ports), '<br>'))
                        yield ' |\n'
                    l_2_rule = l_2_protocols_list = l_2_destination_ports = l_2_source_ports = missing
            l_1_policy = missing
        if t_4(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'profiles')):
            pass
            yield '\n#### Telemetry Postcard Policy Profiles\n\n| Profile Name | Ingress Sample Policy |\n| ------------ | --------------------- |\n'
            for l_1_profile in t_2(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'profiles'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_profile, 'ingress_sample_policy'), '-'))
                yield ' |\n'
            l_1_profile = missing
        yield '\n#### Monitor Telemetry Postcard Policy Configuration\n\n```eos\n'
        template = environment.get_template('eos/monitor-telemetry-postcard-policy.j2', 'documentation/monitor-telemetry-postcard-policy.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&10=39&13=42&15=46&16=48&22=51&23=55&24=57&25=59&26=61&27=64&28=65&29=67&31=70&33=71&34=73&36=76&39=78&40=80&41=81&42=82&44=84&49=100&55=103&56=107&63=113'