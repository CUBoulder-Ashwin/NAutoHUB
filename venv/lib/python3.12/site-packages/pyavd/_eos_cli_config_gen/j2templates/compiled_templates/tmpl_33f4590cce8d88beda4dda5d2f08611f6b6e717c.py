from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-traffic-engineering.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_traffic_engineering = resolve('router_traffic_engineering')
    l_0_namespace = resolve('namespace')
    l_0_ns = resolve('ns')
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
    if t_2(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'enabled'), True):
        pass
        yield '!\nrouter traffic-engineering\n'
        if t_2(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing')):
            pass
            l_0_ns = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), delimiter=False)
            context.vars['ns'] = l_0_ns
            context.exported_vars.add('ns')
            yield '   segment-routing\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'colored_tunnel_rib'), True):
                pass
                if not isinstance(l_0_ns, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_ns['delimiter'] = True
                yield '      rib system-colored-tunnel-rib\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'policy_endpoints')):
                pass
                for l_1_endpoint in t_1(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'policy_endpoints'), 'address'):
                    _loop_vars = {}
                    pass
                    for l_2_color in t_1(environment.getattr(l_1_endpoint, 'colors'), 'value'):
                        _loop_vars = {}
                        pass
                        if t_2(environment.getattr((undefined(name='ns') if l_0_ns is missing else l_0_ns), 'delimiter'), True):
                            pass
                            yield '      !\n'
                        if not isinstance(l_0_ns, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_0_ns['delimiter'] = True
                        yield '      policy endpoint '
                        yield str(environment.getattr(l_1_endpoint, 'address'))
                        yield ' color '
                        yield str(environment.getattr(l_2_color, 'value'))
                        yield '\n'
                        if t_2(environment.getattr(l_2_color, 'binding_sid')):
                            pass
                            yield '         binding-sid '
                            yield str(environment.getattr(l_2_color, 'binding_sid'))
                            yield '\n'
                        if t_2(environment.getattr(l_2_color, 'name')):
                            pass
                            yield '         name '
                            yield str(environment.getattr(l_2_color, 'name'))
                            yield '\n'
                        if t_2(environment.getattr(l_2_color, 'description')):
                            pass
                            yield '         description '
                            yield str(environment.getattr(l_2_color, 'description'))
                            yield '\n'
                        if t_2(environment.getattr(l_2_color, 'sbfd_remote_discriminator')):
                            pass
                            yield '         sbfd remote-discriminator '
                            yield str(environment.getattr(l_2_color, 'sbfd_remote_discriminator'))
                            yield '\n'
                        for l_3_pathgroup in t_1(environment.getattr(l_2_color, 'path_group'), 'preference'):
                            _loop_vars = {}
                            pass
                            yield '         !\n         path-group preference '
                            yield str(environment.getattr(l_3_pathgroup, 'preference'))
                            yield '\n'
                            if t_2(environment.getattr(l_3_pathgroup, 'explicit_null')):
                                pass
                                yield '            explicit-null '
                                yield str(environment.getattr(l_3_pathgroup, 'explicit_null'))
                                yield '\n'
                            for l_4_labelstack in t_1(environment.getattr(l_3_pathgroup, 'segment_list'), 'label_stack'):
                                l_4_stack = missing
                                _loop_vars = {}
                                pass
                                l_4_stack = environment.getattr(l_4_labelstack, 'label_stack')
                                _loop_vars['stack'] = l_4_stack
                                if t_2(environment.getattr(l_4_labelstack, 'weight')):
                                    pass
                                    l_4_stack = str_join(((undefined(name='stack') if l_4_stack is missing else l_4_stack), ' weight ', environment.getattr(l_4_labelstack, 'weight'), ))
                                    _loop_vars['stack'] = l_4_stack
                                if t_2(environment.getattr(l_4_labelstack, 'index')):
                                    pass
                                    l_4_stack = str_join(((undefined(name='stack') if l_4_stack is missing else l_4_stack), ' index ', environment.getattr(l_4_labelstack, 'index'), ))
                                    _loop_vars['stack'] = l_4_stack
                                yield '            segment-list label-stack '
                                yield str((undefined(name='stack') if l_4_stack is missing else l_4_stack))
                                yield '\n'
                            l_4_labelstack = l_4_stack = missing
                        l_3_pathgroup = missing
                    l_2_color = missing
                l_1_endpoint = missing
        if t_2(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'router_id'), 'ipv4')):
            pass
            yield '   router-id ipv4 '
            yield str(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'router_id'), 'ipv4'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'router_id'), 'ipv6')):
            pass
            yield '   router-id ipv6 '
            yield str(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'router_id'), 'ipv6'))
            yield '\n'

blocks = {}
debug_info = '7=26&10=29&11=31&13=35&14=37&17=41&18=43&19=46&20=49&23=52&24=56&25=60&26=63&28=65&29=68&31=70&32=73&34=75&35=78&37=80&39=84&40=86&41=89&43=91&44=95&45=97&46=99&48=101&49=103&51=106&58=112&59=115&61=117&62=120'