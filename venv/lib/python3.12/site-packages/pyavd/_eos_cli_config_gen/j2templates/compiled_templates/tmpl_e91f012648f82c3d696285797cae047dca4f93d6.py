from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_interfaces = resolve('management_interfaces')
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
    if t_3((undefined(name='management_interfaces') if l_0_management_interfaces is missing else l_0_management_interfaces)):
        pass
        yield '\n### Management Interfaces\n\n#### Management Interfaces Summary\n\n##### IPv4\n\n| Management Interface | Description | Type | VRF | IP Address | Gateway |\n| -------------------- | ----------- | ---- | --- | ---------- | ------- |\n'
        for l_1_management_interface in t_2((undefined(name='management_interfaces') if l_0_management_interfaces is missing else l_0_management_interfaces), 'name'):
            l_1_vrf = l_1_description = l_1_ip = l_1_ip_gateway = l_1_int_type = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_management_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            l_1_description = t_1(environment.getattr(l_1_management_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            l_1_ip = t_1(environment.getattr(l_1_management_interface, 'ip_address'), '-')
            _loop_vars['ip'] = l_1_ip
            l_1_ip_gateway = t_1(environment.getattr(l_1_management_interface, 'gateway'), '-')
            _loop_vars['ip_gateway'] = l_1_ip_gateway
            l_1_int_type = t_1(environment.getattr(l_1_management_interface, 'type'), 'oob')
            _loop_vars['int_type'] = l_1_int_type
            yield '| '
            yield str(environment.getattr(l_1_management_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='int_type') if l_1_int_type is missing else l_1_int_type))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='ip') if l_1_ip is missing else l_1_ip))
            yield ' | '
            yield str((undefined(name='ip_gateway') if l_1_ip_gateway is missing else l_1_ip_gateway))
            yield ' |\n'
        l_1_management_interface = l_1_vrf = l_1_description = l_1_ip = l_1_ip_gateway = l_1_int_type = missing
        yield '\n##### IPv6\n\n| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |\n| -------------------- | ----------- | ---- | --- | ------------ | ------------ |\n'
        for l_1_management_interface in t_2((undefined(name='management_interfaces') if l_0_management_interfaces is missing else l_0_management_interfaces), 'name'):
            l_1_description = l_1_vrf = l_1_ipv6 = l_1_ipv6_gateway = l_1_int_type = missing
            _loop_vars = {}
            pass
            l_1_description = t_1(environment.getattr(l_1_management_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            l_1_vrf = t_1(environment.getattr(l_1_management_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            l_1_ipv6 = t_1(environment.getattr(l_1_management_interface, 'ipv6_address'), '-')
            _loop_vars['ipv6'] = l_1_ipv6
            l_1_ipv6_gateway = t_1(environment.getattr(l_1_management_interface, 'ipv6_gateway'), '-')
            _loop_vars['ipv6_gateway'] = l_1_ipv6_gateway
            l_1_int_type = t_1(environment.getattr(l_1_management_interface, 'type'), 'oob')
            _loop_vars['int_type'] = l_1_int_type
            yield '| '
            yield str(environment.getattr(l_1_management_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='int_type') if l_1_int_type is missing else l_1_int_type))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='ipv6') if l_1_ipv6 is missing else l_1_ipv6))
            yield ' | '
            yield str((undefined(name='ipv6_gateway') if l_1_ipv6_gateway is missing else l_1_ipv6_gateway))
            yield ' |\n'
        l_1_management_interface = l_1_description = l_1_vrf = l_1_ipv6 = l_1_ipv6_gateway = l_1_int_type = missing
        yield '\n#### Management Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-interfaces.j2', 'documentation/management-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&17=33&18=37&19=39&20=41&21=43&22=45&23=48&30=62&31=66&32=68&33=70&34=72&35=74&36=77&42=91'