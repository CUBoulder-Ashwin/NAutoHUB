from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitoring.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_port_channel_interfaces = resolve('port_channel_interfaces')
    l_0_daemon_terminattr = resolve('daemon_terminattr')
    l_0_daemons = resolve('daemons')
    l_0_logging = resolve('logging')
    l_0_mcs_client = resolve('mcs_client')
    l_0_snmp_server = resolve('snmp_server')
    l_0_monitor_sessions = resolve('monitor_sessions')
    l_0_monitor_session_default_encapsulation_gre = resolve('monitor_session_default_encapsulation_gre')
    l_0_tap_aggregation = resolve('tap_aggregation')
    l_0_sflow = resolve('sflow')
    l_0_hardware_counters = resolve('hardware_counters')
    l_0_hardware = resolve('hardware')
    l_0_vmtracer_sessions = resolve('vmtracer_sessions')
    l_0_event_handlers = resolve('event_handlers')
    l_0_flow_tracking = resolve('flow_tracking')
    l_0_trackers = resolve('trackers')
    l_0_monitor_telemetry_postcard_policy = resolve('monitor_telemetry_postcard_policy')
    l_0_monitor_server_radius = resolve('monitor_server_radius')
    l_0_sflow_interfaces = missing
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
    l_0_sflow_interfaces = []
    context.vars['sflow_interfaces'] = l_0_sflow_interfaces
    context.exported_vars.add('sflow_interfaces')
    for l_1_ethernet_interface in t_1((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_3(environment.getattr(l_1_ethernet_interface, 'sflow')):
            pass
            context.call(environment.getattr((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    for l_1_port_channel_interface in t_1((undefined(name='port_channel_interfaces') if l_0_port_channel_interfaces is missing else l_0_port_channel_interfaces), 'name'):
        _loop_vars = {}
        pass
        if t_3(environment.getattr(l_1_port_channel_interface, 'sflow')):
            pass
            context.call(environment.getattr((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces), 'append'), l_1_port_channel_interface, _loop_vars=_loop_vars)
    l_1_port_channel_interface = missing
    if (((((((((((((((((t_3((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr)) or t_3((undefined(name='daemons') if l_0_daemons is missing else l_0_daemons))) or t_3((undefined(name='logging') if l_0_logging is missing else l_0_logging))) or t_3((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client))) or t_3((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server))) or t_3((undefined(name='monitor_sessions') if l_0_monitor_sessions is missing else l_0_monitor_sessions))) or t_3((undefined(name='monitor_session_default_encapsulation_gre') if l_0_monitor_session_default_encapsulation_gre is missing else l_0_monitor_session_default_encapsulation_gre))) or t_3((undefined(name='tap_aggregation') if l_0_tap_aggregation is missing else l_0_tap_aggregation))) or t_3((undefined(name='sflow') if l_0_sflow is missing else l_0_sflow))) or t_3((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters))) or t_3((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware))) or t_3((undefined(name='vmtracer_sessions') if l_0_vmtracer_sessions is missing else l_0_vmtracer_sessions))) or t_3((undefined(name='event_handlers') if l_0_event_handlers is missing else l_0_event_handlers))) or t_3((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking))) or t_3((undefined(name='trackers') if l_0_trackers is missing else l_0_trackers))) or (t_2((undefined(name='sflow_interfaces') if l_0_sflow_interfaces is missing else l_0_sflow_interfaces)) > 0)) or t_3((undefined(name='monitor_telemetry_postcard_policy') if l_0_monitor_telemetry_postcard_policy is missing else l_0_monitor_telemetry_postcard_policy))) or t_3((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius))):
        pass
        yield '\n## Monitoring\n'
        template = environment.get_template('documentation/daemon-terminattr.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/daemons.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/logging.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/mcs-client.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/snmp-server.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/monitor-sessions.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/tap-aggregation.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/sflow.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/hardware.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/vmtracer-sessions.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/event-handlers.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/flow-tracking.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/trackers.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/monitor-telemetry-postcard-policy.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event
        template = environment.get_template('documentation/monitor-server-radius.j2', 'documentation/monitoring.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'sflow_interfaces': l_0_sflow_interfaces})):
            yield event

blocks = {}
debug_info = '7=49&8=52&9=55&10=57&13=59&14=62&15=64&18=66&39=69&41=72&43=75&45=78&47=81&49=84&51=87&53=90&55=93&57=96&59=99&61=102&63=105&65=108&67=111'