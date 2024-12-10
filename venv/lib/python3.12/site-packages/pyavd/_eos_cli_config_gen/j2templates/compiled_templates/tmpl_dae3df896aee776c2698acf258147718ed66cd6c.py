from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/routing.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_service_routing_configuration_bgp = resolve('service_routing_configuration_bgp')
    l_0_service_routing_protocols_model = resolve('service_routing_protocols_model')
    l_0_ip_virtual_router_mac_address = resolve('ip_virtual_router_mac_address')
    l_0_ip_routing = resolve('ip_routing')
    l_0_vrfs = resolve('vrfs')
    l_0_ipv6_unicast_routing = resolve('ipv6_unicast_routing')
    l_0_static_routes = resolve('static_routes')
    l_0_ipv6_static_routes = resolve('ipv6_static_routes')
    l_0_ipv6_neighbor = resolve('ipv6_neighbor')
    l_0_arp = resolve('arp')
    l_0_router_general = resolve('router_general')
    l_0_router_service_insertion = resolve('router_service_insertion')
    l_0_router_traffic_engineering = resolve('router_traffic_engineering')
    l_0_router_adaptive_virtual_topology = resolve('router_adaptive_virtual_topology')
    l_0_router_ospf = resolve('router_ospf')
    l_0_router_isis = resolve('router_isis')
    l_0_router_bgp = resolve('router_bgp')
    l_0_policy_maps = resolve('policy_maps')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (((((((((((((((((t_1((undefined(name='service_routing_configuration_bgp') if l_0_service_routing_configuration_bgp is missing else l_0_service_routing_configuration_bgp)) or t_1((undefined(name='service_routing_protocols_model') if l_0_service_routing_protocols_model is missing else l_0_service_routing_protocols_model))) or t_1((undefined(name='ip_virtual_router_mac_address') if l_0_ip_virtual_router_mac_address is missing else l_0_ip_virtual_router_mac_address))) or t_1((undefined(name='ip_routing') if l_0_ip_routing is missing else l_0_ip_routing))) or t_1((undefined(name='vrfs') if l_0_vrfs is missing else l_0_vrfs))) or t_1((undefined(name='ipv6_unicast_routing') if l_0_ipv6_unicast_routing is missing else l_0_ipv6_unicast_routing))) or t_1((undefined(name='static_routes') if l_0_static_routes is missing else l_0_static_routes))) or t_1((undefined(name='ipv6_static_routes') if l_0_ipv6_static_routes is missing else l_0_ipv6_static_routes))) or t_1((undefined(name='ipv6_neighbor') if l_0_ipv6_neighbor is missing else l_0_ipv6_neighbor))) or t_1((undefined(name='arp') if l_0_arp is missing else l_0_arp))) or t_1((undefined(name='router_general') if l_0_router_general is missing else l_0_router_general))) or t_1((undefined(name='router_service_insertion') if l_0_router_service_insertion is missing else l_0_router_service_insertion))) or t_1((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering))) or t_1((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology))) or t_1((undefined(name='router_ospf') if l_0_router_ospf is missing else l_0_router_ospf))) or t_1((undefined(name='router_isis') if l_0_router_isis is missing else l_0_router_isis))) or t_1((undefined(name='router_bgp') if l_0_router_bgp is missing else l_0_router_bgp))) or t_1(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'pbr'))):
        pass
        yield '\n## Routing\n'
        template = environment.get_template('documentation/service-routing-configuration-bgp.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/service-routing-protocols-model.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-virtual-router-mac-address.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-routing.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-unicast-routing.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/static-routes.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-static-routes.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-neighbors.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/arp.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-adaptive-virtual-topology.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-general.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-service-insertion.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-traffic-engineering.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-ospf.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-isis.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/router-bgp.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/policy-maps-pbr.j2', 'documentation/routing.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '6=35&27=38&29=41&31=44&33=47&35=50&37=53&39=56&41=59&43=62&45=65&47=68&49=71&51=74&53=77&55=80&57=83&59=86'