from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitor-telemetry-influx.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_telemetry_influx = resolve('monitor_telemetry_influx')
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
    if t_3((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx)):
        pass
        yield '\n## InfluxDB Telemetry\n\n### InfluxDB Telemetry Summary\n'
        if t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_group_standard_disabled'), True):
            pass
            yield '\nSource Group Standard Disabled : '
            yield str(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_group_standard_disabled'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'destinations')):
            pass
            yield '\n#### InfluxDB Telemetry Destinations\n\n| Destination | Database | URL | VRF | Username |\n| ----------- | -------- | --- | --- | -------- |\n'
            for l_1_destination in t_2(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'destinations'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(t_1(environment.getattr(l_1_destination, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_destination, 'database'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_destination, 'url'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'vrf'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_destination, 'username'), '-'))
                yield ' |\n'
            l_1_destination = missing
        if t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_sockets')):
            pass
            yield '\n#### InfluxDB Telemetry Sources\n\n| Source Name | URL | Connection Limit |\n| ----------- | --- | ---------------- |\n'
            for l_1_source in t_2(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_sockets'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(t_1(environment.getattr(l_1_source, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_source, 'url'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_source, 'connection_limit'), '-'))
                yield ' |\n'
            l_1_source = missing
        if t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'tags')):
            pass
            yield '\n#### InfluxDB Telemetry Tags\n\n| Tag | Value |\n| --- | ----- |\n'
            for l_1_tag in environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'tags'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(t_1(environment.getattr(l_1_tag, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_tag, 'value'), '-'))
                yield ' |\n'
            l_1_tag = missing
        yield '\n### InfluxDB Telemetry Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/monitor-telemetry-influx.j2', 'documentation/monitor-telemetry-influx.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&14=36&16=38&22=41&23=45&26=56&32=59&33=63&36=70&42=73&43=77&50=83'