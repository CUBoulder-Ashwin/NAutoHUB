from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-telemetry-influx.j2'

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
        t_2 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx)):
        pass
        yield '!\nmonitor telemetry influx\n'
        l_1_loop = missing
        for l_1_destination, l_1_loop in LoopContext(t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'destinations'), 'name'), undefined):
            l_1_hide_passwords = resolve('hide_passwords')
            _loop_vars = {}
            pass
            yield '   destination influxdb '
            yield str(environment.getattr(l_1_destination, 'name'))
            yield '\n'
            if t_4(environment.getattr(l_1_destination, 'url')):
                pass
                yield '      url '
                yield str(environment.getattr(l_1_destination, 'url'))
                yield '\n'
            if t_4(environment.getattr(l_1_destination, 'database')):
                pass
                yield '      database name '
                yield str(environment.getattr(l_1_destination, 'database'))
                yield '\n'
            if t_4(environment.getattr(l_1_destination, 'data_retention_policy')):
                pass
                yield '      retention policy '
                yield str(environment.getattr(l_1_destination, 'data_retention_policy'))
                yield '\n'
            if t_4(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'vrf')):
                pass
                yield '      vrf '
                yield str(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'vrf'))
                yield '\n'
            if (t_4(environment.getattr(l_1_destination, 'username')) and t_4(environment.getattr(l_1_destination, 'password'))):
                pass
                yield '      username '
                yield str(environment.getattr(l_1_destination, 'username'))
                yield ' password '
                yield str(t_1(environment.getattr(l_1_destination, 'password_type'), '7'))
                yield ' '
                yield str(t_2(environment.getattr(l_1_destination, 'password'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
            if ((not environment.getattr(l_1_loop, 'last')) or t_4(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_sockets'))):
                pass
                yield '   !\n'
        l_1_loop = l_1_destination = l_1_hide_passwords = missing
        l_1_loop = missing
        for l_1_socket, l_1_loop in LoopContext(t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_sockets'), 'name'), undefined):
            _loop_vars = {}
            pass
            yield '   source socket '
            yield str(environment.getattr(l_1_socket, 'name'))
            yield '\n'
            if t_4(environment.getattr(l_1_socket, 'url')):
                pass
                yield '      url '
                yield str(environment.getattr(l_1_socket, 'url'))
                yield '\n'
            if t_4(environment.getattr(l_1_socket, 'connection_limit')):
                pass
                yield '      connection limit '
                yield str(environment.getattr(l_1_socket, 'connection_limit'))
                yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_socket = missing
        for l_1_tag in t_3(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'tags'), 'name'):
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_tag, 'value')):
                pass
                yield '   tag global '
                yield str(environment.getattr(l_1_tag, 'name'))
                yield ' '
                yield str(environment.getattr(l_1_tag, 'value'))
                yield '\n'
        l_1_tag = missing
        if t_4(environment.getattr((undefined(name='monitor_telemetry_influx') if l_0_monitor_telemetry_influx is missing else l_0_monitor_telemetry_influx), 'source_group_standard_disabled'), True):
            pass
            yield '   source group standard disabled\n'

blocks = {}
debug_info = '7=36&10=40&11=45&12=47&13=50&15=52&16=55&18=57&19=60&21=62&22=65&24=67&25=70&27=76&31=81&32=85&33=87&34=90&36=92&37=95&39=97&43=101&44=104&45=107&48=112'