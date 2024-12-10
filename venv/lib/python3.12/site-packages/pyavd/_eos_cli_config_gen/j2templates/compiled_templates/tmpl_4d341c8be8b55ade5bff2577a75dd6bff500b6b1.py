from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/event-handlers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_event_handlers = resolve('event_handlers')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers)):
        pass
        for l_1_handler in t_1((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers), 'name'):
            l_1_trigger_cli = resolve('trigger_cli')
            l_1_on_maintenance_cli = resolve('on_maintenance_cli')
            l_1_trigger_on_intf_cli = resolve('trigger_on_intf_cli')
            l_1_bash_command = resolve('bash_command')
            _loop_vars = {}
            pass
            yield '!\nevent-handler '
            yield str(environment.getattr(l_1_handler, 'name'))
            yield '\n'
            if ((t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'log'), True) and (not t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')))) and (environment.getattr(l_1_handler, 'trigger') != 'on-boot')):
                pass
                yield '   action log\n'
            if (t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric')) and (environment.getattr(l_1_handler, 'trigger') != 'on-boot')):
                pass
                yield '   action increment device-health metric '
                yield str(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric'))
                yield '\n'
            if t_3(environment.getattr(l_1_handler, 'trigger')):
                pass
                if ((t_3(environment.getattr(l_1_handler, 'trigger'), 'on-maintenance') and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'))) and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))):
                    pass
                    l_1_trigger_cli = str_join(('trigger ', environment.getattr(l_1_handler, 'trigger'), ' ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'operation'), ))
                    _loop_vars['trigger_cli'] = l_1_trigger_cli
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer')):
                        pass
                        l_1_on_maintenance_cli = str_join(('bgp ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'bgp_peer'), ))
                        _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf')):
                            pass
                            l_1_on_maintenance_cli = str_join(((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli), ' vrf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'vrf'), ))
                            _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface')):
                        pass
                        l_1_on_maintenance_cli = str_join(('interface ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'interface'), ))
                        _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                    elif t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit')):
                        pass
                        l_1_on_maintenance_cli = str_join(('unit ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'unit'), ))
                        _loop_vars['on_maintenance_cli'] = l_1_on_maintenance_cli
                    if t_3((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli)):
                        pass
                        if ((environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action') in ['after', 'before']) and t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'))):
                            pass
                            yield '   '
                            yield str((undefined(name='trigger_cli') if l_1_trigger_cli is missing else l_1_trigger_cli))
                            yield ' '
                            yield str((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli))
                            yield ' '
                            yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))
                            yield ' stage '
                            yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'stage'))
                            yield '\n'
                        elif (environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action') in ['all', 'begin', 'end']):
                            pass
                            yield '   '
                            yield str((undefined(name='trigger_cli') if l_1_trigger_cli is missing else l_1_trigger_cli))
                            yield ' '
                            yield str((undefined(name='on_maintenance_cli') if l_1_on_maintenance_cli is missing else l_1_on_maintenance_cli))
                            yield ' '
                            yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_maintenance'), 'action'))
                            yield '\n'
                elif t_3(environment.getattr(l_1_handler, 'trigger'), 'on-counters'):
                    pass
                    yield '   trigger on-counters\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval')):
                        pass
                        yield '      poll interval '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'poll_interval'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition')):
                        pass
                        yield '      condition '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'condition'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_counters'), 'granularity_per_source'), True):
                        pass
                        yield '      granularity per-source\n'
                elif t_3(environment.getattr(l_1_handler, 'trigger'), 'on-logging'):
                    pass
                    yield '   trigger on-logging\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval')):
                        pass
                        yield '      poll interval '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'poll_interval'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex')):
                        pass
                        yield '      regex '
                        yield str(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_logging'), 'regex'))
                        yield '\n'
                elif t_3(environment.getattr(l_1_handler, 'trigger'), 'on-intf'):
                    pass
                    if (t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface')) and ((t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True) or t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True)) or t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True))):
                        pass
                        l_1_trigger_on_intf_cli = str_join(('trigger on-intf ', environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'interface'), ))
                        _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'operstatus'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' operstatus', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ip'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' ip', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        if t_3(environment.getattr(environment.getattr(l_1_handler, 'trigger_on_intf'), 'ipv6'), True):
                            pass
                            l_1_trigger_on_intf_cli = str_join(((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli), ' ip6', ))
                            _loop_vars['trigger_on_intf_cli'] = l_1_trigger_on_intf_cli
                        yield '   '
                        yield str((undefined(name='trigger_on_intf_cli') if l_1_trigger_on_intf_cli is missing else l_1_trigger_on_intf_cli))
                        yield '\n'
                else:
                    pass
                    yield '   trigger '
                    yield str(environment.getattr(l_1_handler, 'trigger'))
                    yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')):
                pass
                l_1_bash_command = environment.getattr(environment.getattr(l_1_handler, 'actions'), 'bash_command')
                _loop_vars['bash_command'] = l_1_bash_command
                if (context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'count'), '\n', _loop_vars=_loop_vars) > 0):
                    pass
                    if (not context.call(environment.getattr(context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'rstrip'), _loop_vars=_loop_vars), 'endswith'), '\nEOF', _loop_vars=_loop_vars)):
                        pass
                        l_1_bash_command = str_join((context.call(environment.getattr((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), 'rstrip'), _loop_vars=_loop_vars), '\nEOF', ))
                        _loop_vars['bash_command'] = l_1_bash_command
                    yield '   action bash\n      '
                    yield str(t_2((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command), width=6, first=False))
                    yield '\n'
                else:
                    pass
                    yield '   action bash '
                    yield str((undefined(name='bash_command') if l_1_bash_command is missing else l_1_bash_command))
                    yield '\n'
            if (t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'log'), True) and (environment.getattr(l_1_handler, 'trigger') == 'on-boot')):
                pass
                yield '   action log\n'
            if (t_3(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric')) and (environment.getattr(l_1_handler, 'trigger') == 'on-boot')):
                pass
                yield '   action increment device-health metric '
                yield str(environment.getattr(environment.getattr(l_1_handler, 'actions'), 'increment_device_health_metric'))
                yield '\n'
            if t_3(environment.getattr(l_1_handler, 'delay')):
                pass
                yield '   delay '
                yield str(environment.getattr(l_1_handler, 'delay'))
                yield '\n'
            if t_3(environment.getattr(l_1_handler, 'asynchronous'), True):
                pass
                yield '   asynchronous\n'
        l_1_handler = l_1_trigger_cli = l_1_on_maintenance_cli = l_1_trigger_on_intf_cli = l_1_bash_command = missing

blocks = {}
debug_info = '7=30&8=32&10=40&11=42&14=45&15=48&17=50&18=52&21=54&22=56&23=58&24=60&25=62&27=64&28=66&29=68&30=70&32=72&33=74&34=77&35=85&36=88&39=94&41=97&42=100&44=102&45=105&47=107&50=110&52=113&53=116&55=118&56=121&58=123&59=125&63=127&64=129&65=131&67=133&68=135&70=137&71=139&73=142&76=147&79=149&80=151&81=153&82=155&83=157&86=160&88=165&91=167&94=170&95=173&97=175&98=178&100=180'