from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitor-server-radius.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_server_radius = resolve('monitor_server_radius')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius)):
        pass
        yield '\n### Monitor Server Radius Summary\n'
        if t_1(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'service_dot1x'), True):
            pass
            yield '\nMonitor servers are used for 802.1x authentication.\n'
        if t_1(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe')):
            pass
            yield '\n#### Server Probe Settings\n\n| Setting | Value |\n| ------- | ----- |\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'interval')):
                pass
                yield '| Probe interval | '
                yield str(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'interval'))
                yield ' |\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'threshold_failure')):
                pass
                yield '| Threshold failure | '
                yield str(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'threshold_failure'))
                yield ' |\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'method')):
                pass
                yield '| Probe method | '
                yield str(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'method'))
                yield ' |\n'
        yield '\n#### Monitor Server Radius Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/monitor-server-radius.j2', 'documentation/monitor-server-radius.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&10=21&14=24&20=27&21=30&23=32&24=35&26=37&27=40&34=43'