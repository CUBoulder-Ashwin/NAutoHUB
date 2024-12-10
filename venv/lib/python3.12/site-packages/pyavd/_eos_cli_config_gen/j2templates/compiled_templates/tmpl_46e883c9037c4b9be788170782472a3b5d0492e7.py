from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/static-routes.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_static_routes = resolve('static_routes')
    l_0_with_vrf_non_default = resolve('with_vrf_non_default')
    l_0_without_vrf = resolve('without_vrf')
    l_0_with_vrf_default = resolve('with_vrf_default')
    l_0_sorted_static_routes = resolve('sorted_static_routes')
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
        t_3 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_4 = environment.filters['list']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'list' found.")
    try:
        t_5 = environment.filters['rejectattr']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'rejectattr' found.")
    try:
        t_6 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_7 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_7((undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes)):
        pass
        yield '!\n'
        if t_7((undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes)):
            pass
            l_0_with_vrf_non_default = t_2(t_2(t_5(context, t_6(context, (undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default')), 'vrf')
            context.vars['with_vrf_non_default'] = l_0_with_vrf_non_default
            context.exported_vars.add('with_vrf_non_default')
            l_0_without_vrf = t_2(t_5(context, (undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes), 'vrf', 'arista.avd.defined'))
            context.vars['without_vrf'] = l_0_without_vrf
            context.exported_vars.add('without_vrf')
            l_0_with_vrf_default = t_2(t_6(context, t_6(context, (undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes), 'vrf', 'arista.avd.defined'), 'vrf', 'equalto', 'default'))
            context.vars['with_vrf_default'] = l_0_with_vrf_default
            context.exported_vars.add('with_vrf_default')
            l_0_sorted_static_routes = ((t_4(context.eval_ctx, (undefined(name='without_vrf') if l_0_without_vrf is missing else l_0_without_vrf)) + t_4(context.eval_ctx, (undefined(name='with_vrf_default') if l_0_with_vrf_default is missing else l_0_with_vrf_default))) + t_4(context.eval_ctx, (undefined(name='with_vrf_non_default') if l_0_with_vrf_non_default is missing else l_0_with_vrf_non_default)))
            context.vars['sorted_static_routes'] = l_0_sorted_static_routes
            context.exported_vars.add('sorted_static_routes')
        for l_1_static_route in t_1((undefined(name='sorted_static_routes') if l_0_sorted_static_routes is missing else l_0_sorted_static_routes), []):
            l_1_static_route_cli = missing
            _loop_vars = {}
            pass
            l_1_static_route_cli = 'ip route'
            _loop_vars['static_route_cli'] = l_1_static_route_cli
            if (t_7(environment.getattr(l_1_static_route, 'vrf')) and (environment.getattr(l_1_static_route, 'vrf') != 'default')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' vrf ', environment.getattr(l_1_static_route, 'vrf'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'destination_address_prefix')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' ', environment.getattr(l_1_static_route, 'destination_address_prefix'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'interface')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' ', t_3(environment.getattr(l_1_static_route, 'interface')), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'gateway')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' ', environment.getattr(l_1_static_route, 'gateway'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
                if t_7(environment.getattr(l_1_static_route, 'track_bfd'), True):
                    pass
                    l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' track bfd', ))
                    _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'distance')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' ', environment.getattr(l_1_static_route, 'distance'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'tag')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' tag ', environment.getattr(l_1_static_route, 'tag'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'name')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' name ', environment.getattr(l_1_static_route, 'name'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            if t_7(environment.getattr(l_1_static_route, 'metric')):
                pass
                l_1_static_route_cli = str_join(((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli), ' metric ', environment.getattr(l_1_static_route, 'metric'), ))
                _loop_vars['static_route_cli'] = l_1_static_route_cli
            yield str((undefined(name='static_route_cli') if l_1_static_route_cli is missing else l_1_static_route_cli))
            yield '\n'
        l_1_static_route = l_1_static_route_cli = missing

blocks = {}
debug_info = '7=58&9=61&10=63&11=66&12=69&13=72&15=75&16=79&17=81&18=83&20=85&21=87&23=89&24=91&26=93&27=95&28=97&29=99&32=101&33=103&35=105&36=107&38=109&39=111&41=113&42=115&44=117'