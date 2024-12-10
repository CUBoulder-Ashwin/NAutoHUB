from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-multicast.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_multicast = resolve('router_multicast')
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
    if t_3((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast)):
        pass
        yield '\n### Router Multicast\n\n#### IP Router Multicast Summary\n\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'counters'), 'rate_period_decay')):
            pass
            yield '- Counters rate period decay is set for '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'counters'), 'rate_period_decay'))
            yield ' seconds\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'routing'), True):
            pass
            yield '- Routing for IPv4 multicast is enabled.\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath'), 'deterministic color'):
            pass
            yield '- Multipathing deterministically by selecting the same-colored upstream routers.\n'
        elif t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath'), 'deterministic router-id'):
            pass
            yield '- Multipathing deterministically by selecting the same upstream router.\n'
        elif t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath'), 'none'):
            pass
            yield '- Multipathing disabled.\n'
        elif t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath'), 'deterministic'):
            pass
            yield '- Multipathing via ECMP.\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'software_forwarding'), 'kernel'):
            pass
            yield '- Software forwarding by the Linux kernel\n'
        elif t_3(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'software_forwarding'), 'sfe'):
            pass
            yield '- Software forwarding by the Software Forwarding Engine (SFE)\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'rpf'), 'routes')):
            pass
            yield '\n#### IP Router Multicast RPF Routes\n\n| Source Prefix | Next Hop | Administrative Distance |\n| ------------- | -------- | ----------------------- |\n'
            def t_4(fiter):
                for l_1_rpf_route in fiter:
                    if t_3(environment.getattr(l_1_rpf_route, 'source_prefix')):
                        yield l_1_rpf_route
            for l_1_rpf_route in t_4(t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'rpf'), 'routes'), 'source_prefix')):
                _loop_vars = {}
                pass
                def t_5(fiter):
                    for l_2_destination in fiter:
                        if t_3(environment.getattr(l_2_destination, 'nexthop')):
                            yield l_2_destination
                for l_2_destination in t_5(t_2(environment.getattr(l_1_rpf_route, 'destinations'), 'nexthop')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_rpf_route, 'source_prefix'))
                    yield ' | '
                    yield str(environment.getattr(l_2_destination, 'nexthop'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_2_destination, 'distance'), '-'))
                    yield ' |\n'
                l_2_destination = missing
            l_1_rpf_route = missing
        if t_3(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'vrfs')):
            pass
            yield '\n#### IP Router Multicast VRFs\n\n| VRF Name | Multicast Routing |\n| -------- | ----------------- |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'vrfs'), 'name'):
                l_1_multicast_routing = resolve('multicast_routing')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(environment.getattr(l_1_vrf, 'ipv4'), 'routing'), True):
                    pass
                    l_1_multicast_routing = 'enabled'
                    _loop_vars['multicast_routing'] = l_1_multicast_routing
                else:
                    pass
                    l_1_multicast_routing = 'disabled'
                    _loop_vars['multicast_routing'] = l_1_multicast_routing
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str((undefined(name='multicast_routing') if l_1_multicast_routing is missing else l_1_multicast_routing))
                yield ' |\n'
            l_1_vrf = l_1_multicast_routing = missing
        yield '\n#### Router Multicast Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-multicast.j2', 'documentation/router-multicast.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&13=33&14=36&16=38&19=41&21=44&23=47&25=50&28=53&30=56&33=59&39=62&40=69&41=77&45=85&51=88&52=92&53=94&55=98&57=101&64=107'