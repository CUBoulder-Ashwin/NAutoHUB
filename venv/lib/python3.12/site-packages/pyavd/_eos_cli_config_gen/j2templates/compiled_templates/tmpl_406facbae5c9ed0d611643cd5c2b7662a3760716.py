from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/flow-tracking.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_flow_tracking = resolve('flow_tracking')
    l_0_encapsulation = resolve('encapsulation')
    l_0_hardware_offload_protocols = resolve('hardware_offload_protocols')
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
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware')):
        pass
        yield '!\nflow tracking hardware\n'
        l_1_loop = missing
        for l_1_tracker, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'trackers')), undefined):
            _loop_vars = {}
            pass
            if (not environment.getattr(l_1_loop, 'first')):
                pass
                yield '   !\n'
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            l_2_loop = missing
            for l_2_exporter, l_2_loop in LoopContext(t_1(environment.getattr(l_1_tracker, 'exporters'), 'name'), undefined):
                l_2_collector_cli = resolve('collector_cli')
                _loop_vars = {}
                pass
                if (not environment.getattr(l_2_loop, 'first')):
                    pass
                    yield '      !\n'
                yield '      exporter '
                yield str(environment.getattr(l_2_exporter, 'name'))
                yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                    pass
                    l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                    _loop_vars['collector_cli'] = l_2_collector_cli
                    if t_4(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                        pass
                        l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                    yield '         '
                    yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                    pass
                    yield '         format ipfix version '
                    yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                    yield '\n'
                if t_4(environment.getattr(l_2_exporter, 'local_interface')):
                    pass
                    yield '         local interface '
                    yield str(environment.getattr(l_2_exporter, 'local_interface'))
                    yield '\n'
                if t_4(environment.getattr(l_2_exporter, 'template_interval')):
                    pass
                    yield '         template interval '
                    yield str(environment.getattr(l_2_exporter, 'template_interval'))
                    yield '\n'
            l_2_loop = l_2_exporter = l_2_collector_cli = missing
            if t_4(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
        l_1_loop = l_1_tracker = missing
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'record'), 'format_ipfix_standard_timestamps_counters'), True):
            pass
            yield '   record format ipfix standard timestamps counters\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
    if t_4(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled')):
        pass
        yield '!\nflow tracking sampled\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'encapsulation')):
            pass
            l_0_encapsulation = 'encapsulation'
            context.vars['encapsulation'] = l_0_encapsulation
            context.exported_vars.add('encapsulation')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'encapsulation'), 'ipv4_ipv6'), True):
                pass
                l_0_encapsulation = str_join(((undefined(name='encapsulation') if l_0_encapsulation is missing else l_0_encapsulation), ' ipv4 ipv6', ))
                context.vars['encapsulation'] = l_0_encapsulation
                context.exported_vars.add('encapsulation')
                if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'encapsulation'), 'mpls'), True):
                    pass
                    l_0_encapsulation = str_join(((undefined(name='encapsulation') if l_0_encapsulation is missing else l_0_encapsulation), ' mpls', ))
                    context.vars['encapsulation'] = l_0_encapsulation
                    context.exported_vars.add('encapsulation')
            yield '   '
            yield str((undefined(name='encapsulation') if l_0_encapsulation is missing else l_0_encapsulation))
            yield '\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample')):
            pass
            yield '   sample '
            yield str(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload')):
            pass
            l_0_hardware_offload_protocols = []
            context.vars['hardware_offload_protocols'] = l_0_hardware_offload_protocols
            context.exported_vars.add('hardware_offload_protocols')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'ipv4'), True):
                pass
                context.call(environment.getattr((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), 'append'), 'ipv4')
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'ipv6'), True):
                pass
                context.call(environment.getattr((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), 'append'), 'ipv6')
            if (t_3((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols)) > 0):
                pass
                yield '   hardware offload '
                yield str(t_2(context.eval_ctx, (undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), ' '))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'threshold_minimum')):
                pass
                yield '   hardware offload threshold minimum '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'threshold_minimum'))
                yield ' samples\n'
        l_1_loop = missing
        for l_1_tracker, l_1_loop in LoopContext(t_1(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'trackers')), undefined):
            _loop_vars = {}
            pass
            if (not environment.getattr(l_1_loop, 'first')):
                pass
                yield '   !\n'
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_4(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            l_2_loop = missing
            for l_2_exporter, l_2_loop in LoopContext(t_1(environment.getattr(l_1_tracker, 'exporters'), 'name'), undefined):
                l_2_collector_cli = resolve('collector_cli')
                _loop_vars = {}
                pass
                if (not environment.getattr(l_2_loop, 'first')):
                    pass
                    yield '      !\n'
                yield '      exporter '
                yield str(environment.getattr(l_2_exporter, 'name'))
                yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                    pass
                    l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                    _loop_vars['collector_cli'] = l_2_collector_cli
                    if t_4(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                        pass
                        l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                    yield '         '
                    yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                    pass
                    yield '         format ipfix version '
                    yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                    yield '\n'
                if t_4(environment.getattr(l_2_exporter, 'local_interface')):
                    pass
                    yield '         local interface '
                    yield str(environment.getattr(l_2_exporter, 'local_interface'))
                    yield '\n'
                if t_4(environment.getattr(l_2_exporter, 'template_interval')):
                    pass
                    yield '         template interval '
                    yield str(environment.getattr(l_2_exporter, 'template_interval'))
                    yield '\n'
            l_2_loop = l_2_exporter = l_2_collector_cli = missing
        l_1_loop = l_1_tracker = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'

blocks = {}
debug_info = '8=38&11=42&12=45&15=49&16=51&17=54&19=56&20=59&22=61&25=65&26=69&29=73&30=75&31=77&32=79&33=81&35=84&37=86&38=89&40=91&41=94&43=96&44=99&47=102&48=105&51=108&54=111&59=114&62=117&63=119&64=122&65=124&66=127&67=129&70=133&72=135&73=138&75=140&76=142&77=145&78=147&80=148&81=150&83=151&84=154&86=156&87=159&90=162&91=165&94=169&95=171&96=174&98=176&99=179&101=181&102=184&104=186&107=190&108=194&111=198&112=200&113=202&114=204&115=206&117=209&119=211&120=214&122=216&123=219&125=221&126=224&130=228'