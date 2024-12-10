from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-service-insertion.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_service_insertion = resolve('router_service_insertion')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2(environment.getattr((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion), 'enabled'), True):
        pass
        yield '!\nrouter service-insertion\n'
        for l_1_connection in t_1(environment.getattr((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion), 'connections'), 'name'):
            _loop_vars = {}
            pass
            yield '   connection '
            yield str(environment.getattr(l_1_connection, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_connection, 'ethernet_interface')):
                pass
                if (t_2(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'name')) and t_2(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'next_hop'))):
                    pass
                    yield '      interface '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'name'))
                    yield ' next-hop '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'ethernet_interface'), 'next_hop'))
                    yield '\n'
            elif t_2(environment.getattr(l_1_connection, 'tunnel_interface')):
                pass
                if t_2(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'primary')):
                    pass
                    yield '      interface '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'primary'))
                    yield ' primary\n'
                if t_2(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'secondary')):
                    pass
                    yield '      interface '
                    yield str(environment.getattr(environment.getattr(l_1_connection, 'tunnel_interface'), 'secondary'))
                    yield ' secondary\n'
            if t_2(environment.getattr(l_1_connection, 'monitor_connectivity_host')):
                pass
                yield '      monitor connectivity host '
                yield str(environment.getattr(l_1_connection, 'monitor_connectivity_host'))
                yield '\n'
        l_1_connection = missing

blocks = {}
debug_info = '7=24&10=27&11=31&12=33&13=35&14=38&16=42&17=44&18=47&20=49&21=52&24=54&25=57'