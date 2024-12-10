from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-service-insertion.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_service_insertion = resolve('router_service_insertion')
    l_0_ethernet_connections = resolve('ethernet_connections')
    l_0_tunnel_connections = resolve('tunnel_connections')
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
    if t_3(environment.getattr((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion), 'enabled'), True):
        pass
        yield '\n## Router Service Insertion\n\nRouter service-insertion is enabled.\n'
        if t_3(environment.getattr((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion), 'connections')):
            pass
            yield '\n### Connections\n'
            l_0_ethernet_connections = []
            context.vars['ethernet_connections'] = l_0_ethernet_connections
            context.exported_vars.add('ethernet_connections')
            l_0_tunnel_connections = []
            context.vars['tunnel_connections'] = l_0_tunnel_connections
            context.exported_vars.add('tunnel_connections')
            for l_1_connection in t_2(environment.getattr((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion), 'connections'), 'name'):
                _loop_vars = {}
                pass
                if (t_3(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'name')) and t_3(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'next_hop'))):
                    pass
                    context.call(environment.getattr((undefined(name='ethernet_connections') if l_0_ethernet_connections is missing else l_0_ethernet_connections), 'append'), l_1_connection, _loop_vars=_loop_vars)
                elif (t_3(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'primary')) or t_3(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'secondary'))):
                    pass
                    context.call(environment.getattr((undefined(name='tunnel_connections') if l_0_tunnel_connections is missing else l_0_tunnel_connections), 'append'), l_1_connection, _loop_vars=_loop_vars)
            l_1_connection = missing
            if (undefined(name='ethernet_connections') if l_0_ethernet_connections is missing else l_0_ethernet_connections):
                pass
                yield '\n#### Connections Through Ethernet Interface\n\n| Name | Interface | Next Hop | Monitor Connectivity Host |\n| ---- | --------- | -------- | ------------------------- |\n'
                for l_1_connection in (undefined(name='ethernet_connections') if l_0_ethernet_connections is missing else l_0_ethernet_connections):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_connection, 'name'))
                    yield ' | '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'name'))
                    yield ' | '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'next_hop'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_connection, 'monitor_connectivity_host'), '-'))
                    yield ' |\n'
                l_1_connection = missing
            if (undefined(name='tunnel_connections') if l_0_tunnel_connections is missing else l_0_tunnel_connections):
                pass
                yield '\n#### Connections Through Tunnel Interface\n\n| Name | Primary Interface | Secondary Interface | Monitor Connectivity Host |\n| ---- | ----------------- | ------------------- | ------------------------- |\n'
                for l_1_connection in (undefined(name='tunnel_connections') if l_0_tunnel_connections is missing else l_0_tunnel_connections):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_connection, 'name'))
                    yield ' | '
                    yield str(t_1(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'primary'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'secondary'), '-'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_connection, 'monitor_connectivity_host'), '-'))
                    yield ' |\n'
                l_1_connection = missing
        yield '\n### Router Service Insertion Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-service-insertion.j2', 'documentation/router-service-insertion.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ethernet_connections': l_0_ethernet_connections, 'tunnel_connections': l_0_tunnel_connections})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=32&12=35&15=38&16=41&17=44&18=47&19=49&20=50&21=52&24=54&30=57&31=61&34=70&40=73&41=77&49=87'