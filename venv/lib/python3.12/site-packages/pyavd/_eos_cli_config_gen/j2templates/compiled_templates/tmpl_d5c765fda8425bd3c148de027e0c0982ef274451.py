from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-server-radius.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_server_radius = resolve('monitor_server_radius')
    l_0_access_request = resolve('access_request')
    l_0_hide_passwords = resolve('hide_passwords')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius)):
        pass
        yield '!\nmonitor server radius\n'
        if t_3(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'service_dot1x'), True):
            pass
            yield '   service dot1x\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'interval')):
            pass
            yield '   probe interval '
            yield str(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'interval'))
            yield ' seconds\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'threshold_failure')):
            pass
            yield '   probe threshold failure '
            yield str(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'threshold_failure'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'method'), 'status-server'):
            pass
            yield '   probe method status-server\n'
        elif t_3(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'method'), 'access-request'):
            pass
            if (t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'access_request'), 'username')) and t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'access_request'), 'password'))):
                pass
                l_0_access_request = environment.getattr(environment.getattr((undefined(name='monitor_server_radius') if l_0_monitor_server_radius is missing else l_0_monitor_server_radius), 'probe'), 'access_request')
                context.vars['access_request'] = l_0_access_request
                context.exported_vars.add('access_request')
                yield '   probe method access-request username '
                yield str(environment.getattr((undefined(name='access_request') if l_0_access_request is missing else l_0_access_request), 'username'))
                yield ' password '
                yield str(t_1(environment.getattr((undefined(name='access_request') if l_0_access_request is missing else l_0_access_request), 'password_type'), '7'))
                yield ' '
                yield str(t_2(environment.getattr((undefined(name='access_request') if l_0_access_request is missing else l_0_access_request), 'password'), (undefined(name='hide_passwords') if l_0_hide_passwords is missing else l_0_hide_passwords)))
                yield '\n'

blocks = {}
debug_info = '7=32&10=35&13=38&14=41&16=43&17=46&19=48&21=51&22=53&24=55&25=59'