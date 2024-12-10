from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/quality-of-service.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_qos = resolve('qos')
    l_0_class_maps = resolve('class_maps')
    l_0_policy_maps = resolve('policy_maps')
    l_0_qos_profiles = resolve('qos_profiles')
    l_0_ethernet_interfaces_qos = l_0_port_channel_interfaces_qos = missing
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_ethernet_interfaces_qos = []
    context.vars['ethernet_interfaces_qos'] = l_0_ethernet_interfaces_qos
    context.exported_vars.add('ethernet_interfaces_qos')
    l_0_port_channel_interfaces_qos = []
    context.vars['port_channel_interfaces_qos'] = l_0_port_channel_interfaces_qos
    context.exported_vars.add('port_channel_interfaces_qos')
    for l_1_ethernet_interface in t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if (t_3(environment.getattr(l_1_ethernet_interface, 'shape')) or t_3(environment.getattr(l_1_ethernet_interface, 'qos'))):
            pass
            context.call(environment.getattr((undefined(name='ethernet_interfaces_qos') if l_0_ethernet_interfaces_qos is missing else l_0_ethernet_interfaces_qos), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    for l_1_port_channel_interface in t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
        _loop_vars = {}
        pass
        if (t_3(environment.getattr(l_1_port_channel_interface, 'shape')) or t_3(environment.getattr(l_1_port_channel_interface, 'qos'))):
            pass
            context.call(environment.getattr((undefined(name='port_channel_interfaces_qos') if l_0_port_channel_interfaces_qos is missing else l_0_port_channel_interfaces_qos), 'append'), l_1_port_channel_interface, _loop_vars=_loop_vars)
    l_1_port_channel_interface = missing
    if ((((((t_3((undefined(name='qos') if l_0_qos is missing else l_0_qos)) or t_3(environment.getattr((undefined(name='class_maps') if l_0_class_maps is missing else l_0_class_maps), 'qos'))) or t_3(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'qos'))) or t_3((undefined(name='qos_profiles') if l_0_qos_profiles is missing else l_0_qos_profiles))) or (t_2((undefined(name='ethernet_interfaces_qos') if l_0_ethernet_interfaces_qos is missing else l_0_ethernet_interfaces_qos)) > True)) or (t_2((undefined(name='port_channel_interfaces_qos') if l_0_port_channel_interfaces_qos is missing else l_0_port_channel_interfaces_qos)) > 0)) or t_3(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy'))):
        pass
        yield '\n## Quality Of Service\n'
        template = environment.get_template('documentation/qos.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event
        template = environment.get_template('documentation/class-maps.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event
        template = environment.get_template('documentation/policy-maps-qos.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event
        template = environment.get_template('documentation/qos-profiles.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event
        template = environment.get_template('documentation/qos-interfaces.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event
        template = environment.get_template('documentation/policy-maps-copp.j2', 'documentation/quality-of-service.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_interfaces_qos': l_0_ethernet_interfaces_qos, 'port_channel_interfaces_qos': l_0_port_channel_interfaces_qos})):
            yield event

blocks = {}
debug_info = '6=36&7=39&8=42&9=45&11=47&14=49&15=52&17=54&20=56&30=59&32=62&34=65&36=68&38=71&40=74'