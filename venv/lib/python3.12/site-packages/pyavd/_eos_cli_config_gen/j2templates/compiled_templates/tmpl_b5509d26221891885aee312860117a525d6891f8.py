from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/loopback-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_loopback_interfaces = resolve('loopback_interfaces')
    l_0_namespace = resolve('namespace')
    l_0_loopback_interface_isis = resolve('loopback_interface_isis')
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
    if t_4((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces)):
        pass
        yield '\n### Loopback Interfaces\n\n#### Loopback Interfaces Summary\n\n##### IPv4\n\n| Interface | Description | VRF | IP Address |\n| --------- | ----------- | --- | ---------- |\n'
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            l_1_ip = resolve('ip')
            l_1_vrf = l_1_description = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_loopback_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            if t_4(environment.getattr(l_1_loopback_interface, 'ip_address')):
                pass
                l_1_ip = environment.getattr(l_1_loopback_interface, 'ip_address')
                _loop_vars['ip'] = l_1_ip
                if t_4(environment.getattr(l_1_loopback_interface, 'ip_address_secondaries')):
                    pass
                    l_1_ip = str_join((environment.getattr(l_1_loopback_interface, 'ip_address'), ' <br> ', t_3(context.eval_ctx, environment.getattr(l_1_loopback_interface, 'ip_address_secondaries'), ' secondary <br> '), ' secondary', ))
                    _loop_vars['ip'] = l_1_ip
            l_1_description = t_1(environment.getattr(l_1_loopback_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            yield '| '
            yield str(environment.getattr(l_1_loopback_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str(t_1((undefined(name='ip') if l_1_ip is missing else l_1_ip), '-'))
            yield ' |\n'
        l_1_loopback_interface = l_1_vrf = l_1_ip = l_1_description = missing
        yield '\n##### IPv6\n\n| Interface | Description | VRF | IPv6 Address |\n| --------- | ----------- | --- | ------------ |\n'
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            l_1_ip = l_1_ipv6 = l_1_description = missing
            _loop_vars = {}
            pass
            l_1_ip = t_1(environment.getattr(l_1_loopback_interface, 'vrf'), 'default')
            _loop_vars['ip'] = l_1_ip
            l_1_ipv6 = t_1(environment.getattr(l_1_loopback_interface, 'ipv6_address'), '-')
            _loop_vars['ipv6'] = l_1_ipv6
            l_1_description = t_1(environment.getattr(l_1_loopback_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            yield '| '
            yield str(environment.getattr(l_1_loopback_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='ip') if l_1_ip is missing else l_1_ip))
            yield ' | '
            yield str((undefined(name='ipv6') if l_1_ipv6 is missing else l_1_ipv6))
            yield ' |\n'
        l_1_loopback_interface = l_1_ip = l_1_ipv6 = l_1_description = missing
        l_0_loopback_interface_isis = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['loopback_interface_isis'] = l_0_loopback_interface_isis
        context.exported_vars.add('loopback_interface_isis')
        if not isinstance(l_0_loopback_interface_isis, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_loopback_interface_isis['configured'] = False
        for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_loopback_interface, 'isis_enable')):
                pass
                if not isinstance(l_0_loopback_interface_isis, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_loopback_interface_isis['configured'] = True
        l_1_loopback_interface = missing
        if (environment.getattr((undefined(name='loopback_interface_isis') if l_0_loopback_interface_isis is missing else l_0_loopback_interface_isis), 'configured') == True):
            pass
            yield '\n##### ISIS\n\n| Interface | ISIS instance | ISIS metric | Interface mode |\n| --------- | ------------- | ----------- | -------------- |\n'
            for l_1_loopback_interface in t_2((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
                l_1_mode = resolve('mode')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_loopback_interface, 'isis_enable')):
                    pass
                    if t_4(environment.getattr(l_1_loopback_interface, 'isis_network_point_to_point')):
                        pass
                        l_1_mode = 'point-to-point'
                        _loop_vars['mode'] = l_1_mode
                    elif t_4(environment.getattr(l_1_loopback_interface, 'isis_passive')):
                        pass
                        l_1_mode = 'passive'
                        _loop_vars['mode'] = l_1_mode
                    yield '| '
                    yield str(environment.getattr(l_1_loopback_interface, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_loopback_interface, 'isis_enable'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_loopback_interface, 'isis_metric'), '-'))
                    yield ' | '
                    yield str(t_1((undefined(name='mode') if l_1_mode is missing else l_1_mode), '-'))
                    yield ' |\n'
            l_1_loopback_interface = l_1_mode = missing
        yield '\n#### Loopback Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/loopback-interfaces.j2', 'documentation/loopback-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'loopback_interface_isis': l_0_loopback_interface_isis})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=38&17=41&18=46&19=48&20=50&21=52&22=54&25=56&26=59&33=69&34=73&35=75&36=77&37=80&39=89&40=92&41=95&42=98&43=100&46=104&52=107&53=111&54=113&55=115&56=117&57=119&59=122&67=132'