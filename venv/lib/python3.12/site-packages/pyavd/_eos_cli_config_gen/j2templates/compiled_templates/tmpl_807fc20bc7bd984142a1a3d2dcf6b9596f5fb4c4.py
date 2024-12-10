from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-igmp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_igmp = resolve('router_igmp')
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
    if t_2((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp)):
        pass
        yield '!\nrouter igmp\n'
        if t_2(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'host_proxy_match_mroute')):
            pass
            yield '   host-proxy match mroute '
            yield str(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'host_proxy_match_mroute'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'ssm_aware'), True):
            pass
            yield '   ssm aware\n'
        if t_2(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'vrfs')):
            pass
            for l_1_vrf in t_1(environment.getattr((undefined(name='router_igmp') if l_0_router_igmp is missing else l_0_router_igmp), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                if (environment.getattr(l_1_vrf, 'name') != 'default'):
                    pass
                    yield '   !\n   vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield '\n'
                    if t_2(environment.getattr(l_1_vrf, 'host_proxy_match_mroute')):
                        pass
                        yield '     host-proxy match mroute '
                        yield str(environment.getattr(l_1_vrf, 'host_proxy_match_mroute'))
                        yield '\n'
            l_1_vrf = missing

blocks = {}
debug_info = '7=24&10=27&11=30&13=32&16=35&17=37&18=40&20=43&21=45&22=48'