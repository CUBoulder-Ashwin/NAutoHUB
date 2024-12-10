from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-connectivity.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_connectivity = resolve('monitor_connectivity')
    l_0_local_interfaces_cli = resolve('local_interfaces_cli')
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
    if t_3((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity)):
        pass
        yield '!\nmonitor connectivity\n'
        l_1_loop = missing
        for l_1_vrf, l_1_loop in LoopContext(t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'vrfs'), 'name'), undefined):
            l_1_local_interfaces_cli = l_0_local_interfaces_cli
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_vrf, 'name')):
                pass
                if (not environment.getattr(l_1_loop, 'first')):
                    pass
                    yield '   !\n'
                yield '   vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield '\n'
                for l_2_interface_set in t_2(environment.getattr(l_1_vrf, 'interface_sets'), 'name'):
                    _loop_vars = {}
                    pass
                    if (t_3(environment.getattr(l_2_interface_set, 'name')) and t_3(environment.getattr(l_2_interface_set, 'interfaces'))):
                        pass
                        yield '      interface set '
                        yield str(environment.getattr(l_2_interface_set, 'name'))
                        yield ' '
                        yield str(environment.getattr(l_2_interface_set, 'interfaces'))
                        yield '\n'
                l_2_interface_set = missing
                if t_3(environment.getattr(l_1_vrf, 'description')):
                    pass
                    yield '      description\n      '
                    yield str(environment.getattr(l_1_vrf, 'description'))
                    yield '\n'
                if t_3(environment.getattr(l_1_vrf, 'local_interfaces')):
                    pass
                    l_1_local_interfaces_cli = str_join(('local-interfaces ', environment.getattr(l_1_vrf, 'local_interfaces'), ))
                    _loop_vars['local_interfaces_cli'] = l_1_local_interfaces_cli
                    if t_1(environment.getattr(l_1_vrf, 'address_only'), True):
                        pass
                        l_1_local_interfaces_cli = str_join(((undefined(name='local_interfaces_cli') if l_1_local_interfaces_cli is missing else l_1_local_interfaces_cli), ' address-only', ))
                        _loop_vars['local_interfaces_cli'] = l_1_local_interfaces_cli
                    yield '      '
                    yield str((undefined(name='local_interfaces_cli') if l_1_local_interfaces_cli is missing else l_1_local_interfaces_cli))
                    yield ' default\n'
                for l_2_host in t_2(environment.getattr(l_1_vrf, 'hosts'), 'name'):
                    l_2_local_interfaces_cli = l_1_local_interfaces_cli
                    _loop_vars = {}
                    pass
                    if t_3(environment.getattr(l_2_host, 'name')):
                        pass
                        yield '      !\n      host '
                        yield str(environment.getattr(l_2_host, 'name'))
                        yield '\n'
                        if t_3(environment.getattr(l_2_host, 'description')):
                            pass
                            yield '         description\n         '
                            yield str(environment.getattr(l_2_host, 'description'))
                            yield '\n'
                        if t_3(environment.getattr(l_2_host, 'local_interfaces')):
                            pass
                            l_2_local_interfaces_cli = str_join(('local-interfaces ', environment.getattr(l_2_host, 'local_interfaces'), ))
                            _loop_vars['local_interfaces_cli'] = l_2_local_interfaces_cli
                            if t_1(environment.getattr(l_2_host, 'address_only'), True):
                                pass
                                l_2_local_interfaces_cli = str_join(((undefined(name='local_interfaces_cli') if l_2_local_interfaces_cli is missing else l_2_local_interfaces_cli), ' address-only', ))
                                _loop_vars['local_interfaces_cli'] = l_2_local_interfaces_cli
                            yield '         '
                            yield str((undefined(name='local_interfaces_cli') if l_2_local_interfaces_cli is missing else l_2_local_interfaces_cli))
                            yield '\n'
                        if t_3(environment.getattr(l_2_host, 'ip')):
                            pass
                            yield '         ip '
                            yield str(environment.getattr(l_2_host, 'ip'))
                            yield '\n'
                        if t_3(environment.getattr(l_2_host, 'url')):
                            pass
                            yield '         url '
                            yield str(environment.getattr(l_2_host, 'url'))
                            yield '\n'
                l_2_host = l_2_local_interfaces_cli = missing
        l_1_loop = l_1_vrf = l_1_local_interfaces_cli = missing
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interval')):
            pass
            yield '   interval '
            yield str(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interval'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        elif t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'shutdown'), True):
            pass
            yield '   shutdown\n'
        for l_1_interface_set in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'interface_sets'), 'name'):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_interface_set, 'name')) and t_3(environment.getattr(l_1_interface_set, 'interfaces'))):
                pass
                yield '   interface set '
                yield str(environment.getattr(l_1_interface_set, 'name'))
                yield ' '
                yield str(environment.getattr(l_1_interface_set, 'interfaces'))
                yield '\n'
        l_1_interface_set = missing
        if t_3(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'local_interfaces')):
            pass
            l_0_local_interfaces_cli = str_join(('local-interfaces ', environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'local_interfaces'), ))
            context.vars['local_interfaces_cli'] = l_0_local_interfaces_cli
            context.exported_vars.add('local_interfaces_cli')
            if t_1(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'address_only'), True):
                pass
                l_0_local_interfaces_cli = str_join(((undefined(name='local_interfaces_cli') if l_0_local_interfaces_cli is missing else l_0_local_interfaces_cli), ' address-only', ))
                context.vars['local_interfaces_cli'] = l_0_local_interfaces_cli
                context.exported_vars.add('local_interfaces_cli')
            yield '   '
            yield str((undefined(name='local_interfaces_cli') if l_0_local_interfaces_cli is missing else l_0_local_interfaces_cli))
            yield ' default\n'
        for l_1_host in t_2(environment.getattr((undefined(name='monitor_connectivity') if l_0_monitor_connectivity is missing else l_0_monitor_connectivity), 'hosts'), 'name'):
            l_1_local_interfaces_cli = l_0_local_interfaces_cli
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_host, 'name')):
                pass
                yield '   !\n   host '
                yield str(environment.getattr(l_1_host, 'name'))
                yield '\n'
                if t_3(environment.getattr(l_1_host, 'description')):
                    pass
                    yield '      description\n      '
                    yield str(environment.getattr(l_1_host, 'description'))
                    yield '\n'
                if t_3(environment.getattr(l_1_host, 'local_interfaces')):
                    pass
                    l_1_local_interfaces_cli = str_join(('local-interfaces ', environment.getattr(l_1_host, 'local_interfaces'), ))
                    _loop_vars['local_interfaces_cli'] = l_1_local_interfaces_cli
                    if t_1(environment.getattr(l_1_host, 'address_only'), True):
                        pass
                        l_1_local_interfaces_cli = str_join(((undefined(name='local_interfaces_cli') if l_1_local_interfaces_cli is missing else l_1_local_interfaces_cli), ' address-only', ))
                        _loop_vars['local_interfaces_cli'] = l_1_local_interfaces_cli
                    yield '      '
                    yield str((undefined(name='local_interfaces_cli') if l_1_local_interfaces_cli is missing else l_1_local_interfaces_cli))
                    yield '\n'
                if t_3(environment.getattr(l_1_host, 'ip')):
                    pass
                    yield '      ip '
                    yield str(environment.getattr(l_1_host, 'ip'))
                    yield '\n'
                if t_3(environment.getattr(l_1_host, 'url')):
                    pass
                    yield '      url '
                    yield str(environment.getattr(l_1_host, 'url'))
                    yield '\n'
        l_1_host = l_1_local_interfaces_cli = missing

blocks = {}
debug_info = '7=31&10=35&11=39&12=41&15=45&16=47&17=50&18=53&21=58&23=61&25=63&26=65&27=67&28=69&30=72&32=74&33=78&35=81&36=83&38=86&40=88&41=90&42=92&43=94&45=97&47=99&48=102&50=104&51=107&57=111&58=114&60=116&62=119&65=122&66=125&67=128&70=133&71=135&72=138&73=140&75=144&77=146&78=150&80=153&81=155&83=158&85=160&86=162&87=164&88=166&90=169&92=171&93=174&95=176&96=179'