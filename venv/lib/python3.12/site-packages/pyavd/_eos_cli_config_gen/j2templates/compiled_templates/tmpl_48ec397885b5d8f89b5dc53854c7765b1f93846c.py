from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-telemetry-postcard-policy.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_telemetry_postcard_policy = resolve('monitor_telemetry_postcard_policy')
    l_0_marker_cli = resolve('marker_cli')
    l_0_ingress_cli = resolve('ingress_cli')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy)):
        pass
        yield '!\nmonitor telemetry postcard policy\n'
        if t_3(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'disabled'), False):
            pass
            yield '   no disabled\n'
        elif t_3(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'disabled'), True):
            pass
            yield '   disabled\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'rate')):
            pass
            yield '   ingress sample rate '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'rate'))
            yield '\n'
        elif (t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'tcp_udp_checksum'), 'value')) and t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'tcp_udp_checksum'), 'mask'))):
            pass
            yield '   ingress sample tcp-udp-checksum value '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'tcp_udp_checksum'), 'value'))
            yield ' mask '
            yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'sample'), 'tcp_udp_checksum'), 'mask'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'marker_vxlan'), 'enabled'), True):
            pass
            l_0_marker_cli = 'marker vxlan'
            context.vars['marker_cli'] = l_0_marker_cli
            context.exported_vars.add('marker_cli')
            if t_3(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'marker_vxlan'), 'header_word_zero_bit')):
                pass
                l_0_marker_cli = str_join(((undefined(name='marker_cli') if l_0_marker_cli is missing else l_0_marker_cli), ' header word 0 bit ', environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'marker_vxlan'), 'header_word_zero_bit'), ))
                context.vars['marker_cli'] = l_0_marker_cli
                context.exported_vars.add('marker_cli')
            yield '   '
            yield str((undefined(name='marker_cli') if l_0_marker_cli is missing else l_0_marker_cli))
            yield '\n'
        if (t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'source')) and t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'destination'))):
            pass
            l_0_ingress_cli = str_join(('ingress collection gre source ', environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'source'), ' destination ', environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'destination'), ))
            context.vars['ingress_cli'] = l_0_ingress_cli
            context.exported_vars.add('ingress_cli')
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'version')):
                pass
                l_0_ingress_cli = str_join(((undefined(name='ingress_cli') if l_0_ingress_cli is missing else l_0_ingress_cli), ' version ', environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'ingress'), 'collection'), 'version'), ))
                context.vars['ingress_cli'] = l_0_ingress_cli
                context.exported_vars.add('ingress_cli')
            yield '   '
            yield str((undefined(name='ingress_cli') if l_0_ingress_cli is missing else l_0_ingress_cli))
            yield '\n'
        l_1_loop = missing
        for l_1_policy, l_1_loop in LoopContext(t_1(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'sample_policies'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   !\n   sample policy '
            yield str(environment.getattr(l_1_policy, 'name'))
            yield '\n'
            l_2_loop = missing
            for l_2_rule, l_2_loop in LoopContext(t_1(environment.getattr(l_1_policy, 'match_rules'), 'name'), undefined):
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_2_rule, 'type')):
                    pass
                    yield '      match '
                    yield str(environment.getattr(l_2_rule, 'name'))
                    yield ' '
                    yield str(environment.getattr(l_2_rule, 'type'))
                    yield '\n'
                    if t_3(environment.getattr(l_2_rule, 'source_prefix')):
                        pass
                        yield '         source prefix '
                        yield str(environment.getattr(l_2_rule, 'source_prefix'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_rule, 'destination_prefix')):
                        pass
                        yield '         destination prefix '
                        yield str(environment.getattr(l_2_rule, 'destination_prefix'))
                        yield '\n'
                    for l_3_protocol in t_1(environment.getattr(l_2_rule, 'protocols'), 'protocol'):
                        l_3_protocol_cli = resolve('protocol_cli')
                        _loop_vars = {}
                        pass
                        if t_3(environment.getattr(l_3_protocol, 'protocol')):
                            pass
                            l_3_protocol_cli = str_join(('protocol ', environment.getattr(l_3_protocol, 'protocol'), ))
                            _loop_vars['protocol_cli'] = l_3_protocol_cli
                            if t_3(environment.getattr(l_3_protocol, 'source_ports')):
                                pass
                                l_3_protocol_cli = str_join(((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli), ' source port ', t_2(context.eval_ctx, environment.getattr(l_3_protocol, 'source_ports'), ', '), ))
                                _loop_vars['protocol_cli'] = l_3_protocol_cli
                            if t_3(environment.getattr(l_3_protocol, 'destination_ports')):
                                pass
                                l_3_protocol_cli = str_join(((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli), ' destination port ', t_2(context.eval_ctx, environment.getattr(l_3_protocol, 'destination_ports'), ', '), ))
                                _loop_vars['protocol_cli'] = l_3_protocol_cli
                            yield '         '
                            yield str((undefined(name='protocol_cli') if l_3_protocol_cli is missing else l_3_protocol_cli))
                            yield '\n'
                    l_3_protocol = l_3_protocol_cli = missing
                if (not environment.getattr(l_2_loop, 'last')):
                    pass
                    yield '      !\n'
            l_2_loop = l_2_rule = missing
        l_1_loop = l_1_policy = missing
        for l_1_profile in t_1(environment.getattr((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy), 'profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_3(environment.getattr(l_1_profile, 'ingress_sample_policy')):
                pass
                yield '      ingress sample policy '
                yield str(environment.getattr(l_1_profile, 'ingress_sample_policy'))
                yield '\n'
        l_1_profile = missing

blocks = {}
debug_info = '7=32&10=35&12=38&15=41&16=44&17=46&18=49&20=53&21=55&22=58&23=60&25=64&27=66&28=68&29=71&30=73&32=77&34=80&36=84&37=87&38=90&39=93&40=97&41=100&43=102&44=105&46=107&47=111&48=113&49=115&50=117&52=119&53=121&55=124&59=127&64=132&66=136&67=138&68=141'