from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dps-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dps_interfaces = resolve('dps_interfaces')
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
    if t_4((undefined(name='dps_interfaces') if l_0_dps_interfaces is missing else l_0_dps_interfaces)):
        pass
        yield '\n### DPS Interfaces\n\n#### DPS Interfaces Summary\n\n| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |\n| --------- | ---------- | -------- | --- | --------------- | --------------- |\n'
        for l_1_dps_interface in t_2((undefined(name='dps_interfaces') if l_0_dps_interfaces is missing else l_0_dps_interfaces), 'name'):
            l_1_mtu = l_1_ip_address = l_1_flow_trackers = l_1_shutdown = l_1_tcp_mss_settings = missing
            _loop_vars = {}
            pass
            l_1_mtu = t_1(environment.getattr(l_1_dps_interface, 'mtu'), '-')
            _loop_vars['mtu'] = l_1_mtu
            l_1_ip_address = t_1(environment.getattr(l_1_dps_interface, 'ip_address'), '-')
            _loop_vars['ip_address'] = l_1_ip_address
            l_1_flow_trackers = []
            _loop_vars['flow_trackers'] = l_1_flow_trackers
            if t_4(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'hardware')):
                pass
                context.call(environment.getattr((undefined(name='flow_trackers') if l_1_flow_trackers is missing else l_1_flow_trackers), 'append'), str_join(('Hardware: ', environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'hardware'), )), _loop_vars=_loop_vars)
            l_1_shutdown = t_1(environment.getattr(l_1_dps_interface, 'shutdown'), '-')
            _loop_vars['shutdown'] = l_1_shutdown
            if t_4(environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'sampled')):
                pass
                context.call(environment.getattr((undefined(name='flow_trackers') if l_1_flow_trackers is missing else l_1_flow_trackers), 'append'), str_join(('Sampled: ', environment.getattr(environment.getattr(l_1_dps_interface, 'flow_tracker'), 'sampled'), )), _loop_vars=_loop_vars)
            l_1_tcp_mss_settings = []
            _loop_vars['tcp_mss_settings'] = l_1_tcp_mss_settings
            if t_4(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv4')):
                pass
                context.call(environment.getattr((undefined(name='tcp_mss_settings') if l_1_tcp_mss_settings is missing else l_1_tcp_mss_settings), 'append'), str_join(('IPv4: ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv4'), )), _loop_vars=_loop_vars)
            if t_4(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv6')):
                pass
                context.call(environment.getattr((undefined(name='tcp_mss_settings') if l_1_tcp_mss_settings is missing else l_1_tcp_mss_settings), 'append'), str_join(('IPv6: ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'ipv6'), )), _loop_vars=_loop_vars)
            if t_4(environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'direction')):
                pass
                context.call(environment.getattr((undefined(name='tcp_mss_settings') if l_1_tcp_mss_settings is missing else l_1_tcp_mss_settings), 'append'), str_join(('Direction: ', environment.getattr(environment.getattr(l_1_dps_interface, 'tcp_mss_ceiling'), 'direction'), )), _loop_vars=_loop_vars)
            yield '| '
            yield str(environment.getattr(l_1_dps_interface, 'name'))
            yield ' | '
            yield str((undefined(name='ip_address') if l_1_ip_address is missing else l_1_ip_address))
            yield ' | '
            yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
            yield ' | '
            yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
            yield ' | '
            yield str(t_3(context.eval_ctx, (undefined(name='flow_trackers') if l_1_flow_trackers is missing else l_1_flow_trackers), '<br>'))
            yield ' | '
            yield str(t_3(context.eval_ctx, (undefined(name='tcp_mss_settings') if l_1_tcp_mss_settings is missing else l_1_tcp_mss_settings), '<br>'))
            yield ' |\n'
        l_1_dps_interface = l_1_mtu = l_1_ip_address = l_1_flow_trackers = l_1_shutdown = l_1_tcp_mss_settings = missing
        yield '\n#### DPS Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/dps-interfaces.j2', 'documentation/dps-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&15=39&16=43&17=45&18=47&19=49&20=51&22=52&23=54&24=56&26=57&27=59&28=61&30=62&31=64&33=65&34=67&36=69&42=83'