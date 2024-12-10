from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/sflow.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_sflow = resolve('sflow')
    l_0_sample_cli = resolve('sample_cli')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow)):
        pass
        yield '!\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample')):
            pass
            l_0_sample_cli = 'sflow sample '
            context.vars['sample_cli'] = l_0_sample_cli
            context.exported_vars.add('sample_cli')
            if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'dangerous'), True):
                pass
                l_0_sample_cli = str_join(((undefined(name='sample_cli') if l_0_sample_cli is missing else l_0_sample_cli), 'dangerous ', ))
                context.vars['sample_cli'] = l_0_sample_cli
                context.exported_vars.add('sample_cli')
            l_0_sample_cli = str_join(((undefined(name='sample_cli') if l_0_sample_cli is missing else l_0_sample_cli), environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample'), ))
            context.vars['sample_cli'] = l_0_sample_cli
            context.exported_vars.add('sample_cli')
            yield str((undefined(name='sample_cli') if l_0_sample_cli is missing else l_0_sample_cli))
            yield '\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'polling_interval')):
            pass
            yield 'sflow polling-interval '
            yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'polling_interval'))
            yield '\n'
        for l_1_vrf in t_1(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            for l_2_destination in t_1(environment.getattr(l_1_vrf, 'destinations'), 'destination'):
                l_2_vrf_cli = missing
                _loop_vars = {}
                pass
                l_2_vrf_cli = str_join(('sflow vrf ', environment.getattr(l_1_vrf, 'name'), ' destination ', environment.getattr(l_2_destination, 'destination'), ))
                _loop_vars['vrf_cli'] = l_2_vrf_cli
                if t_2(environment.getattr(l_2_destination, 'port')):
                    pass
                    l_2_vrf_cli = str_join(((undefined(name='vrf_cli') if l_2_vrf_cli is missing else l_2_vrf_cli), ' ', environment.getattr(l_2_destination, 'port'), ))
                    _loop_vars['vrf_cli'] = l_2_vrf_cli
                yield str((undefined(name='vrf_cli') if l_2_vrf_cli is missing else l_2_vrf_cli))
                yield '\n'
            l_2_destination = l_2_vrf_cli = missing
            if t_2(environment.getattr(l_1_vrf, 'source_interface')):
                pass
                yield 'sflow vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' source-interface '
                yield str(environment.getattr(l_1_vrf, 'source_interface'))
                yield '\n'
            elif t_2(environment.getattr(l_1_vrf, 'source')):
                pass
                yield 'sflow vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' source '
                yield str(environment.getattr(l_1_vrf, 'source'))
                yield '\n'
        l_1_vrf = missing
        for l_1_destination in t_1(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'destinations'), 'destination'):
            l_1_destination_cli = missing
            _loop_vars = {}
            pass
            l_1_destination_cli = str_join(('sflow destination ', environment.getattr(l_1_destination, 'destination'), ))
            _loop_vars['destination_cli'] = l_1_destination_cli
            if t_2(environment.getattr(l_1_destination, 'port')):
                pass
                l_1_destination_cli = str_join(((undefined(name='destination_cli') if l_1_destination_cli is missing else l_1_destination_cli), ' ', environment.getattr(l_1_destination, 'port'), ))
                _loop_vars['destination_cli'] = l_1_destination_cli
            yield str((undefined(name='destination_cli') if l_1_destination_cli is missing else l_1_destination_cli))
            yield '\n'
        l_1_destination = l_1_destination_cli = missing
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source_interface')):
            pass
            yield 'sflow source-interface '
            yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source_interface'))
            yield '\n'
        elif t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source')):
            pass
            yield 'sflow source '
            yield str(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'source'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample_input_subinterface'), True):
            pass
            yield 'sflow sample input subinterface\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'sample_output_subinterface'), True):
            pass
            yield 'sflow sample output subinterface\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'extensions')):
            pass
            def t_3(fiter):
                for l_1_extension in fiter:
                    if (t_2(environment.getattr(l_1_extension, 'name')) and t_2(environment.getattr(l_1_extension, 'enabled'))):
                        yield l_1_extension
            for l_1_extension in t_3(t_1(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'extensions'), 'name')):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_1_extension, 'enabled'), True):
                    pass
                    yield 'sflow extension '
                    yield str(environment.getattr(l_1_extension, 'name'))
                    yield '\n'
                else:
                    pass
                    yield 'no sflow extension '
                    yield str(environment.getattr(l_1_extension, 'name'))
                    yield '\n'
            l_1_extension = missing
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'disable'), 'default'), True):
            pass
            yield 'sflow interface disable default\n'
        if (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'enable_default'), True) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'unmodified'), False)):
            pass
            yield 'sflow interface egress enable default\n'
        elif (t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'enable_default'), True) and t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'interface'), 'egress'), 'unmodified'), True)):
            pass
            yield 'sflow interface egress unmodified enable default\n'
        if t_2(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'run'), True):
            pass
            yield 'sflow run\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'enabled'), True):
            pass
            yield 'sflow hardware acceleration\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'sample')):
            pass
            yield 'sflow hardware acceleration sample '
            yield str(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'sample'))
            yield '\n'
        for l_1_module in t_1(environment.getattr(environment.getattr((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow), 'hardware_acceleration'), 'modules'), 'name'):
            l_1_module_cli = resolve('module_cli')
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_module, 'name')):
                pass
                if t_2(environment.getattr(l_1_module, 'enabled'), False):
                    pass
                    l_1_module_cli = str_join(('no sflow hardware acceleration module ', environment.getattr(l_1_module, 'name'), ))
                    _loop_vars['module_cli'] = l_1_module_cli
                else:
                    pass
                    l_1_module_cli = str_join(('sflow hardware acceleration module ', environment.getattr(l_1_module, 'name'), ))
                    _loop_vars['module_cli'] = l_1_module_cli
                yield str((undefined(name='module_cli') if l_1_module_cli is missing else l_1_module_cli))
                yield '\n'
        l_1_module = l_1_module_cli = missing

blocks = {}
debug_info = '7=25&9=28&10=30&11=33&12=35&14=38&15=41&17=43&18=46&20=48&21=51&22=55&23=57&24=59&26=61&28=64&29=67&30=71&31=74&34=79&35=83&36=85&37=87&39=89&41=92&42=95&43=97&44=100&46=102&49=105&52=108&53=110&54=117&55=120&57=125&61=128&64=131&66=134&69=137&72=140&75=143&76=146&78=148&79=152&80=154&81=156&83=160&85=162'