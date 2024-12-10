from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/sflow.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_sflow = resolve('sflow')
    l_0_sflow_interfaces = resolve('sflow_interfaces')
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
    try:
        t_5 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if (t_4((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow)) or (t_3((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces)) > 0)):
        pass
        yield '\n### SFlow\n\n#### SFlow Summary\n'
        if ((t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'vrfs')) or t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'destinations'))) or t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source_interface'))):
            pass
            yield '\n| VRF | SFlow Source | SFlow Destination | Port |\n| --- | ------------ | ----------------- | ---- |\n'
            if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'vrfs')):
                pass
                for l_1_vrf in t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'vrfs'), 'name'):
                    _loop_vars = {}
                    pass
                    if t_4(environment.getattr(l_1_vrf, 'destinations')):
                        pass
                        for l_2_destination in t_2(environment.getattr(l_1_vrf, 'destinations'), 'destination'):
                            l_2_port = missing
                            _loop_vars = {}
                            pass
                            l_2_port = t_1(environment.getattr(l_2_destination, 'port'), '6343')
                            _loop_vars['port'] = l_2_port
                            yield '| '
                            yield str(environment.getattr(l_1_vrf, 'name'))
                            yield ' | - | '
                            yield str(environment.getattr(l_2_destination, 'destination'))
                            yield ' | '
                            yield str((undefined(name='port') if l_2_port is missing else l_2_port))
                            yield ' |\n'
                        l_2_destination = l_2_port = missing
                    if t_4(environment.getattr(l_1_vrf, 'source_interface')):
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_vrf, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_1_vrf, 'source_interface'))
                        yield ' | - | - |\n'
                    elif t_4(environment.getattr(l_1_vrf, 'source')):
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_vrf, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_1_vrf, 'source'))
                        yield ' | - | - |\n'
                l_1_vrf = missing
            if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'destinations')):
                pass
                for l_1_destination in environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'destinations'):
                    l_1_port = missing
                    _loop_vars = {}
                    pass
                    l_1_port = t_1(environment.getattr(l_1_destination, 'port'), '6343')
                    _loop_vars['port'] = l_1_port
                    yield '| default | - | '
                    yield str(environment.getattr(l_1_destination, 'destination'))
                    yield ' | '
                    yield str((undefined(name='port') if l_1_port is missing else l_1_port))
                    yield ' |\n'
                l_1_destination = l_1_port = missing
            if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source_interface')):
                pass
                yield '| default | '
                yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source_interface'))
                yield ' | - | - |\n'
            elif t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source')):
                pass
                yield '| default | '
                yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source'))
                yield ' | - | - |\n'
        if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample')):
            pass
            yield '\nsFlow Sample Rate: '
            yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample_input_subinterface'), True):
            pass
            yield '\nsFlow Sample Input Subinterface is enabled.\n'
        if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample_output_subinterface'), True):
            pass
            yield '\nsFlow Sample Output Subinterface is enabled.\n'
        if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'polling_interval')):
            pass
            yield '\nsFlow Polling Interval: '
            yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'polling_interval'))
            yield '\n'
        if (t_5(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'run')) and (environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'run') == True)):
            pass
            yield '\nsFlow is enabled.\n'
        else:
            pass
            yield '\nsFlow is disabled.\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'disable'), 'default'), True):
            pass
            yield '\nsFlow is disabled on all interfaces by default.\n'
        if (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'enable_default'), True) and t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'unmodified'), False)):
            pass
            yield '\nEgress sFlow is enabled on all interfaces by default.\n'
        elif (t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'enable_default'), True) and t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'unmodified'), True)):
            pass
            yield '\nUnmodified egress sFlow is enabled on all interfaces by default.\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'enabled'), True):
            pass
            yield '\nsFlow hardware acceleration is enabled.\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'sample')):
            pass
            yield '\nsFlow hardware accelerated Sample Rate: '
            yield str(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'sample'))
            yield '\n'
        if (t_4(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'modules')) and (t_3(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'modules')) > 0)):
            pass
            yield '\n#### SFlow Hardware Accelerated Modules\n\n| Module | Acceleration Enabled |\n| ------ | -------------------- |\n'
            for l_1_module in environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'modules'):
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_module, 'name')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_module, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_module, 'enabled'), True))
                    yield ' |\n'
            l_1_module = missing
        if t_4(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'extensions')):
            pass
            yield '\n#### SFlow Extensions\n\n| Extension | Enabled |\n| --------- | ------- |\n'
            def t_6(fiter):
                for l_1_extension in fiter:
                    if (t_4(environment.getattr(l_1_extension, 'name')) and t_4(environment.getattr(l_1_extension, 'enabled'))):
                        yield l_1_extension
            for l_1_extension in t_6(t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'extensions'), 'name')):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_extension, 'name'))
                yield ' | '
                yield str(environment.getattr(l_1_extension, 'enabled'))
                yield ' |\n'
            l_1_extension = missing
        if (t_3((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces)) > 0):
            pass
            yield '\n#### SFlow Interfaces\n\n| Interface | Ingress Enabled | Egress Enabled |\n| --------- | --------------- | -------------- |\n'
            for l_1_sflow_interface in t_2((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces), 'name'):
                l_1_sflow_egress_enable = resolve('sflow_egress_enable')
                l_1_sflow_ingress_enable = missing
                _loop_vars = {}
                pass
                l_1_sflow_ingress_enable = t_1(environment.getattr(environment.getattr(l_1_sflow_interface, 'sflow'), 'enable'), '-')
                _loop_vars['sflow_ingress_enable'] = l_1_sflow_ingress_enable
                if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_sflow_interface, 'sflow'), 'egress'), 'enable')):
                    pass
                    l_1_sflow_egress_enable = environment.getattr(environment.getattr(environment.getattr(l_1_sflow_interface, 'sflow'), 'egress'), 'enable')
                    _loop_vars['sflow_egress_enable'] = l_1_sflow_egress_enable
                elif t_4(environment.getattr(environment.getattr(environment.getattr(l_1_sflow_interface, 'sflow'), 'egress'), 'unmodified_enable')):
                    pass
                    l_1_sflow_egress_enable = str_join((environment.getattr(environment.getattr(environment.getattr(l_1_sflow_interface, 'sflow'), 'egress'), 'unmodified_enable'), ' (unmodified)', ))
                    _loop_vars['sflow_egress_enable'] = l_1_sflow_egress_enable
                yield '| '
                yield str(environment.getattr(l_1_sflow_interface, 'name'))
                yield ' | '
                yield str((undefined(name='sflow_ingress_enable') if l_1_sflow_ingress_enable is missing else l_1_sflow_ingress_enable))
                yield ' | '
                yield str(t_1((undefined(name='sflow_egress_enable') if l_1_sflow_egress_enable is missing else l_1_sflow_egress_enable), '-'))
                yield ' |\n'
            l_1_sflow_interface = l_1_sflow_ingress_enable = l_1_sflow_egress_enable = missing
        if t_4((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow)):
            pass
            yield '\n#### SFlow Device Configuration\n\n```eos\n'
            template = environment.get_template('eos/sflow.j2', 'documentation/sflow.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
                yield event
            yield '```\n'

blocks = {}
debug_info = '7=43&12=46&16=49&17=51&18=54&19=56&20=60&21=63&24=70&25=73&26=77&27=80&31=85&32=87&33=91&34=94&37=99&38=102&39=104&40=107&43=109&45=112&47=114&51=117&55=120&57=123&59=125&66=131&70=134&73=137&77=140&81=143&83=146&85=148&91=151&92=154&93=157&97=162&103=165&104=173&107=178&113=181&114=186&115=188&116=190&117=192&118=194&120=197&123=204&128=207'