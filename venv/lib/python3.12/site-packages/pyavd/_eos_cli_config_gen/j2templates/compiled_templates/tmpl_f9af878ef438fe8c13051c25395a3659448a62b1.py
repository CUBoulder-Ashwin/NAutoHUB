from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ipv6-static-routes.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_static_routes = resolve('ipv6_static_routes')
    try:
        t_1 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='ipv6_static_routes') if l_0_ipv6_static_routes is missing else l_0_ipv6_static_routes)):
        pass
        yield '!\n'
        for l_1_ipv6_static_route in (undefined(name='ipv6_static_routes') if l_0_ipv6_static_routes is missing else l_0_ipv6_static_routes):
            l_1_ipv6_static_route_cli = missing
            _loop_vars = {}
            pass
            l_1_ipv6_static_route_cli = 'ipv6 route'
            _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'vrf')):
                pass
                if (environment.getattr(l_1_ipv6_static_route, 'vrf') != 'default'):
                    pass
                    l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' vrf ', environment.getattr(l_1_ipv6_static_route, 'vrf'), ))
                    _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'destination_address_prefix')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' ', environment.getattr(l_1_ipv6_static_route, 'destination_address_prefix'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'interface')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' ', t_1(environment.getattr(l_1_ipv6_static_route, 'interface')), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'gateway')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' ', environment.getattr(l_1_ipv6_static_route, 'gateway'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
                if t_2(environment.getattr(l_1_ipv6_static_route, 'track_bfd'), True):
                    pass
                    l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' track bfd', ))
                    _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'distance')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' ', environment.getattr(l_1_ipv6_static_route, 'distance'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'tag')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' tag ', environment.getattr(l_1_ipv6_static_route, 'tag'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'name')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' name ', environment.getattr(l_1_ipv6_static_route, 'name'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            if t_2(environment.getattr(l_1_ipv6_static_route, 'metric')):
                pass
                l_1_ipv6_static_route_cli = str_join(((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli), ' metric ', environment.getattr(l_1_ipv6_static_route, 'metric'), ))
                _loop_vars['ipv6_static_route_cli'] = l_1_ipv6_static_route_cli
            yield str((undefined(name='ipv6_static_route_cli') if l_1_ipv6_static_route_cli is missing else l_1_ipv6_static_route_cli))
            yield '\n'
        l_1_ipv6_static_route = l_1_ipv6_static_route_cli = missing

blocks = {}
debug_info = '7=24&9=27&10=31&11=33&12=35&13=37&16=39&17=41&19=43&20=45&22=47&23=49&24=51&25=53&28=55&29=57&31=59&32=61&34=63&35=65&37=67&38=69&40=71'