from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/event-handlers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_event_handlers = resolve('event_handlers')
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
        t_4 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers)):
        pass
        yield '\n### Event Handler\n\n#### Event Handler Summary\n\n| Handler | Actions | Trigger | Trigger Config |\n| ------- | ------- | ------- | -------------- |\n'
        for l_1_handler in t_2((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers), 'name'):
            l_1_actions = resolve('actions')
            l_1_bash_command = resolve('bash_command')
            l_1_metric = resolve('metric')
            l_1_trigger_cli = resolve('trigger_cli')
            l_1_on_maintenance_cli = resolve('on_maintenance_cli')
            l_1_trigger_config = resolve('trigger_config')
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_handler, 'actions')):
                pass
                l_1_actions = []
                _loop_vars['actions'] = l_1_actions
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')):
                    pass
                    l_1_bash_command = t_4(context.eval_ctx, t_4(context.eval_ctx, environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command'), '\n', '\\n'), '|', '\\|')
                    _loop_vars['bash_command'] = l_1_bash_command
                    l_1_bash_command = str_join(('<code>', (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), '</code>', ))
                    _loop_vars['bash_command'] = l_1_bash_command
                    l_1_bash_command = str_join(('bash ', (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), ))
                    _loop_vars['bash_command'] = l_1_bash_command
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), (undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), _loop_vars=_loop_vars)
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'log')):
                    pass
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), 'log', _loop_vars=_loop_vars)
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric')):
                    pass
                    l_1_metric = str_join(('increment device health metric ', environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric'), ))
                    _loop_vars['metric'] = l_1_metric
                    context.call(environment.getattr((undefined(name='actions') if l_1_actions is missing else l_1_actions), 'append'), (undefined(name='metric') if l_1_metric is missing else l_1_metric), _loop_vars=_loop_vars)
                l_1_actions = t_3(context.eval_ctx, (undefined(name='actions') if l_1_actions is missing else l_1_actions), '<br>')
                _loop_vars['actions'] = l_1_actions
            if ((t_5(environment.getattr(l_1_handler, 'trigger'), 'on-maintenance') and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'))) and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))):
                pass
                l_1_trigger_cli = str_join(('trigger ', environment.getattr(l_1_handler, 'trigger'), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'), ))
                _loop_vars['trigger_cli'] = l_1_trigger_cli
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer')):
                    pass
                    l_1_on_maintenance_cli = str_join(('bgp ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer'), ))
                    _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf')):
                        pass
                        l_1_on_maintenance_cli = str_join(((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli), ' vrf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf'), ))
                        _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface')):
                    pass
                    l_1_on_maintenance_cli = str_join(('interface ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface'), ))
                    _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                elif t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit')):
                    pass
                    l_1_on_maintenance_cli = str_join(('unit ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit'), ))
                    _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                if t_5((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli)):
                    pass
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action')):
                        pass
                        if ((environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action') in ['after', 'before']) and t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'))):
                            pass
                            l_1_trigger_config = str_join(((undefined(name='trigger_cli') if l_1_trigger_cli is missing else l_1_trigger_cli), ' ', (undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), ' stage ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'), ))
                            _loop_vars['trigger_config'] = l_1_trigger_config
                        elif (environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action') in ['all', 'begin', 'end']):
                            pass
                            l_1_trigger_config = str_join(((undefined(name='trigger_cli') if l_1_trigger_cli is missing else l_1_trigger_cli), ' ', (undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'), ))
                            _loop_vars['trigger_config'] = l_1_trigger_config
            elif (t_5(environment.getattr(l_1_handler, 'trigger'), 'on-counters') and t_5(environment.getattr(l_1_handler, 'trigger_on_counters'))):
                pass
                l_1_trigger_config = []
                _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval')):
                    pass
                    context.call(environment.getattr((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), 'append'), str_join(('poll interval ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval'), )), _loop_vars=_loop_vars)
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition')):
                    pass
                    context.call(environment.getattr((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), 'append'), str_join(('condition ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition'), )), _loop_vars=_loop_vars)
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'granularity_per_source'), True):
                    pass
                    context.call(environment.getattr((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), 'append'), 'granularity per-source', _loop_vars=_loop_vars)
                l_1_trigger_config = t_3(context.eval_ctx, (undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '<br>')
                _loop_vars['trigger_config'] = l_1_trigger_config
            elif (t_5(environment.getattr(l_1_handler, 'trigger'), 'on-logging') and t_5(environment.getattr(l_1_handler, 'trigger_on_logging'))):
                pass
                l_1_trigger_config = []
                _loop_vars['trigger_config'] = l_1_trigger_config
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval')):
                    pass
                    context.call(environment.getattr((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), 'append'), str_join(('poll interval ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval'), )), _loop_vars=_loop_vars)
                if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex')):
                    pass
                    context.call(environment.getattr((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), 'append'), str_join(('regex ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex'), )), _loop_vars=_loop_vars)
                l_1_trigger_config = t_3(context.eval_ctx, (undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '<br>')
                _loop_vars['trigger_config'] = l_1_trigger_config
            elif t_5(environment.getattr(l_1_handler, 'trigger'), 'on-intf'):
                pass
                if (t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface')) and ((t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True) or t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True)) or t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True))):
                    pass
                    l_1_trigger_config = str_join(('trigger on-intf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'), ))
                    _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' operstatus', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' ip', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
                    if t_5(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True):
                        pass
                        l_1_trigger_config = str_join(((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), ' ip6', ))
                        _loop_vars['trigger_config'] = l_1_trigger_config
            yield '| '
            yield str(environment.getattr(l_1_handler, 'name'))
            yield ' | '
            yield str(t_1((undefined(name='actions') if l_1_actions is missing else l_1_actions), '-'))
            yield ' | '
            yield str(t_1(environment.getattr(l_1_handler, 'trigger'), '-'))
            yield ' | '
            yield str(t_1((undefined(name='trigger_config') if l_1_trigger_config is missing else l_1_trigger_config), '-'))
            yield ' |\n'
        l_1_handler = l_1_actions = l_1_bash_command = l_1_metric = l_1_trigger_cli = l_1_on_maintenance_cli = l_1_trigger_config = missing
        yield '\n#### Event Handler Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/event-handlers.j2', 'documentation/event-handlers.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=42&15=45&16=54&17=56&18=58&19=60&20=62&21=64&22=66&23=67&24=69&26=70&27=72&28=74&30=75&32=77&35=79&36=81&37=83&38=85&39=87&41=89&42=91&43=93&44=95&46=97&47=99&48=101&49=103&50=105&51=107&55=109&56=111&57=113&58=115&60=116&61=118&63=119&64=121&66=122&67=124&68=126&69=128&70=130&72=131&73=133&75=134&76=136&77=138&81=140&82=142&83=144&85=146&86=148&88=150&89=152&93=155&99=165'