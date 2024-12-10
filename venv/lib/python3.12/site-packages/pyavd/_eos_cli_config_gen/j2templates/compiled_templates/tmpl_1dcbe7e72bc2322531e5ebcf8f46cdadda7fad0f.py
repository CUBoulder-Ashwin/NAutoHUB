from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-nat-part2.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_nat = resolve('ip_nat')
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
    if t_3((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat)):
        pass
        yield '!\n'
        for l_1_pool in t_2(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'pools'), 'name'):
            l_1_pool_type = missing
            _loop_vars = {}
            pass
            l_1_pool_type = t_1(environment.getattr(l_1_pool, 'type'), 'ip-port')
            _loop_vars['pool_type'] = l_1_pool_type
            if ((undefined(name='pool_type') if l_1_pool_type is missing else l_1_pool_type) == 'ip-port'):
                pass
                if (t_3(environment.getattr(l_1_pool, 'name')) and t_3(environment.getattr(l_1_pool, 'prefix_length'))):
                    pass
                    yield 'ip nat pool '
                    yield str(environment.getattr(l_1_pool, 'name'))
                    yield ' prefix-length '
                    yield str(environment.getattr(l_1_pool, 'prefix_length'))
                    yield '\n'
                    for l_2_range in t_1(environment.getattr(l_1_pool, 'ranges'), []):
                        l_2_range_cli = resolve('range_cli')
                        _loop_vars = {}
                        pass
                        if (t_3(environment.getattr(l_2_range, 'first_ip')) and t_3(environment.getattr(l_2_range, 'last_ip'))):
                            pass
                            l_2_range_cli = str_join(('range ', environment.getattr(l_2_range, 'first_ip'), ' ', environment.getattr(l_2_range, 'last_ip'), ))
                            _loop_vars['range_cli'] = l_2_range_cli
                            if (t_3(environment.getattr(l_2_range, 'first_port')) and t_3(environment.getattr(l_2_range, 'last_port'))):
                                pass
                                l_2_range_cli = str_join(((undefined(name='range_cli') if l_2_range_cli is missing else l_2_range_cli), ' ', environment.getattr(l_2_range, 'first_port'), ' ', environment.getattr(l_2_range, 'last_port'), ))
                                _loop_vars['range_cli'] = l_2_range_cli
                            yield '   '
                            yield str((undefined(name='range_cli') if l_2_range_cli is missing else l_2_range_cli))
                            yield '\n'
                    l_2_range = l_2_range_cli = missing
                    if t_3(environment.getattr(l_1_pool, 'utilization_log_threshold')):
                        pass
                        yield '   utilization threshold '
                        yield str(environment.getattr(l_1_pool, 'utilization_log_threshold'))
                        yield ' action log\n'
        l_1_pool = l_1_pool_type = missing
        for l_1_pool in t_2(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'pools'), 'name'):
            l_1_pool_type = missing
            _loop_vars = {}
            pass
            l_1_pool_type = t_1(environment.getattr(l_1_pool, 'type'), 'ip-port')
            _loop_vars['pool_type'] = l_1_pool_type
            if ((undefined(name='pool_type') if l_1_pool_type is missing else l_1_pool_type) == 'port-only'):
                pass
                if t_3(environment.getattr(l_1_pool, 'name')):
                    pass
                    yield 'ip nat pool '
                    yield str(environment.getattr(l_1_pool, 'name'))
                    yield ' port-only\n'
                    for l_2_range in t_1(environment.getattr(l_1_pool, 'ranges'), []):
                        l_2_range_cli = resolve('range_cli')
                        _loop_vars = {}
                        pass
                        if (t_3(environment.getattr(l_2_range, 'first_port')) and t_3(environment.getattr(l_2_range, 'last_port'))):
                            pass
                            l_2_range_cli = str_join(('port range ', environment.getattr(l_2_range, 'first_port'), ' ', environment.getattr(l_2_range, 'last_port'), ))
                            _loop_vars['range_cli'] = l_2_range_cli
                            yield '   '
                            yield str((undefined(name='range_cli') if l_2_range_cli is missing else l_2_range_cli))
                            yield '\n'
                    l_2_range = l_2_range_cli = missing
        l_1_pool = l_1_pool_type = missing
        if t_3(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization')):
            pass
            yield 'ip nat synchronization\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'description')):
                pass
                yield '   description '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'description'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'expiry_interval')):
                pass
                yield '   expiry-interval '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'expiry_interval'))
                yield '\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'shutdown'), False):
                pass
                yield '   shutdown\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'peer_address')):
                pass
                yield '   peer-address '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'peer_address'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'local_interface')):
                pass
                yield '   local-interface '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'local_interface'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range')):
                pass
                if (t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range'), 'first_port')) and t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range'), 'last_port'))):
                    pass
                    yield '   port-range '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range'), 'first_port'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range'), 'last_port'))
                    yield '\n'
                if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'synchronization'), 'port_range'), 'split_disabled'), False):
                    pass
                    yield '   port-range split disabled\n'

blocks = {}
debug_info = '7=30&9=33&10=37&11=39&12=41&13=44&14=48&15=52&16=54&17=56&18=58&20=61&23=64&24=67&29=70&30=74&31=76&32=78&33=81&34=83&35=87&36=89&37=92&43=96&45=99&46=102&48=104&49=107&51=109&54=112&55=115&57=117&58=120&60=122&61=124&63=127&65=131'