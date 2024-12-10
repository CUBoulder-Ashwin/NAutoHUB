from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/qos-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces_qos = resolve('ethernet_interfaces_qos')
    l_0_port_channel_interfaces_qos = resolve('port_channel_interfaces_qos')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    pass
    if ((t_2((undefined(name='ethernet_interfaces_qos') if l_0_ethernet_interfaces_qos is missing else l_0_ethernet_interfaces_qos)) > 0) or (t_2((undefined(name='port_channel_interfaces_qos') if l_0_port_channel_interfaces_qos is missing else l_0_port_channel_interfaces_qos)) > 0)):
        pass
        yield '\n### QOS Interfaces\n\n| Interface | Trust | Default DSCP | Default COS | Shape rate |\n| --------- | ----- | ------------ | ----------- | ---------- |\n'
        for l_1_ethernet_interface in (undefined(name='ethernet_interfaces_qos') if l_0_ethernet_interfaces_qos is missing else l_0_ethernet_interfaces_qos):
            l_1_qos_trust = l_1_qos_dscp = l_1_qos_cos = l_1_shape_rate = missing
            _loop_vars = {}
            pass
            l_1_qos_trust = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust'), '-')
            _loop_vars['qos_trust'] = l_1_qos_trust
            l_1_qos_dscp = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'dscp'), '-')
            _loop_vars['qos_dscp'] = l_1_qos_dscp
            l_1_qos_cos = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'cos'), '-')
            _loop_vars['qos_cos'] = l_1_qos_cos
            l_1_shape_rate = t_1(environment.getattr(environment.getattr(l_1_ethernet_interface, 'shape'), 'rate'), '-')
            _loop_vars['shape_rate'] = l_1_shape_rate
            yield '| '
            yield str(environment.getattr(l_1_ethernet_interface, 'name'))
            yield ' | '
            yield str((undefined(name='qos_trust') if l_1_qos_trust is missing else l_1_qos_trust))
            yield ' | '
            yield str((undefined(name='qos_dscp') if l_1_qos_dscp is missing else l_1_qos_dscp))
            yield ' | '
            yield str((undefined(name='qos_cos') if l_1_qos_cos is missing else l_1_qos_cos))
            yield ' | '
            yield str((undefined(name='shape_rate') if l_1_shape_rate is missing else l_1_shape_rate))
            yield ' |\n'
        l_1_ethernet_interface = l_1_qos_trust = l_1_qos_dscp = l_1_qos_cos = l_1_shape_rate = missing
        for l_1_port_channel_interface in (undefined(name='port_channel_interfaces_qos') if l_0_port_channel_interfaces_qos is missing else l_0_port_channel_interfaces_qos):
            l_1_qos_trust = l_1_qos_dscp = l_1_qos_cos = l_1_shape_rate = missing
            _loop_vars = {}
            pass
            l_1_qos_trust = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'qos'), 'trust'), '-')
            _loop_vars['qos_trust'] = l_1_qos_trust
            l_1_qos_dscp = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'qos'), 'dscp'), '-')
            _loop_vars['qos_dscp'] = l_1_qos_dscp
            l_1_qos_cos = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'qos'), 'cos'), '-')
            _loop_vars['qos_cos'] = l_1_qos_cos
            l_1_shape_rate = t_1(environment.getattr(environment.getattr(l_1_port_channel_interface, 'shape'), 'rate'), '-')
            _loop_vars['shape_rate'] = l_1_shape_rate
            yield '| '
            yield str(environment.getattr(l_1_port_channel_interface, 'name'))
            yield ' | '
            yield str((undefined(name='qos_trust') if l_1_qos_trust is missing else l_1_qos_trust))
            yield ' | '
            yield str((undefined(name='qos_dscp') if l_1_qos_dscp is missing else l_1_qos_dscp))
            yield ' | '
            yield str((undefined(name='qos_cos') if l_1_qos_cos is missing else l_1_qos_cos))
            yield ' | '
            yield str((undefined(name='shape_rate') if l_1_shape_rate is missing else l_1_shape_rate))
            yield ' |\n'
        l_1_port_channel_interface = l_1_qos_trust = l_1_qos_dscp = l_1_qos_cos = l_1_shape_rate = missing

blocks = {}
debug_info = '7=25&13=28&14=32&15=34&16=36&17=38&18=41&20=52&21=56&22=58&23=60&24=62&25=65'