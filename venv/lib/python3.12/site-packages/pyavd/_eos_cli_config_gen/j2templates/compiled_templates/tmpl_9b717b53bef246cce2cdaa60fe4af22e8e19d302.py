from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vxlan-interface.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vxlan_interface = resolve('vxlan_interface')
    l_0_vxlan_config = missing
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
        t_3 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_4 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_vxlan_config = t_1(environment.getattr((undefined(name='vxlan_interface') if l_0_vxlan_interface is missing else l_0_vxlan_interface), 'vxlan1'), environment.getattr((undefined(name='vxlan_interface') if l_0_vxlan_interface is missing else l_0_vxlan_interface), 'Vxlan1'))
    context.vars['vxlan_config'] = l_0_vxlan_config
    context.exported_vars.add('vxlan_config')
    if t_5((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config)):
        pass
        yield '!\ninterface Vxlan1\n'
        if t_5(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'description')):
            pass
            yield '   description '
            yield str(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'description'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'source_interface')):
            pass
            yield '   vxlan source-interface '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'source_interface'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'controller_client'), 'enabled'), True):
            pass
            yield '   vxlan controller-client\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'virtual_router_encapsulation_mac_address')):
            pass
            yield '   vxlan virtual-router encapsulation mac-address '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'virtual_router_encapsulation_mac_address'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'udp_port')):
            pass
            yield '   vxlan udp-port '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'udp_port'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vtep_to_vtep_bridging'), True):
            pass
            yield '   vxlan bridging vtep-to-vtep\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vtep_learned_data_plane'), True):
            pass
            yield '   vxlan flood vtep learned data-plane\n'
        for l_1_vlan in t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vlans'), 'id'):
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_vlan, 'vni')):
                pass
                yield '   vxlan vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' vni '
                yield str(environment.getattr(l_1_vlan, 'vni'))
                yield '\n'
        l_1_vlan = missing
        for l_1_vrf in t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_vrf, 'vni')):
                pass
                yield '   vxlan vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' vni '
                yield str(environment.getattr(l_1_vrf, 'vni'))
                yield '\n'
        l_1_vrf = missing
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'mlag_source_interface')):
            pass
            yield '   vxlan mlag source-interface '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'mlag_source_interface'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn')):
            pass
            if ((t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'interval')) and t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'min_rx'))) and t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'multiplier'))):
                pass
                yield '   bfd vtep evpn interval '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'interval'))
                yield ' min-rx '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'min_rx'))
                yield ' multiplier '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'multiplier'))
                yield '\n'
            if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'prefix_list')):
                pass
                yield '   bfd vtep evpn prefix-list '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'prefix_list'))
                yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vteps')):
            pass
            yield '   vxlan flood vtep '
            yield str(t_4(context.eval_ctx, environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vteps'), ' '))
            yield '\n'
        for l_1_vlan in t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vlans'), 'id'):
            _loop_vars = {}
            pass
            if t_5(environment.getattr(l_1_vlan, 'flood_vteps')):
                pass
                yield '   vxlan vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' flood vtep '
                yield str(t_4(context.eval_ctx, environment.getattr(l_1_vlan, 'flood_vteps'), ' '))
                yield '\n'
        l_1_vlan = missing
        def t_6(fiter):
            for l_1_vlan in fiter:
                if t_5(environment.getattr(l_1_vlan, 'multicast_group')):
                    yield l_1_vlan
        for l_1_vlan in t_6(t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vlans'), 'id')):
            _loop_vars = {}
            pass
            yield '   vxlan vlan '
            yield str(environment.getattr(l_1_vlan, 'id'))
            yield ' multicast group '
            yield str(environment.getattr(l_1_vlan, 'multicast_group'))
            yield '\n'
        l_1_vlan = missing
        def t_7(fiter):
            for l_1_vrf in fiter:
                if t_5(environment.getattr(l_1_vrf, 'multicast_group')):
                    yield l_1_vrf
        for l_1_vrf in t_7(t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vrfs'), 'name')):
            _loop_vars = {}
            pass
            yield '   vxlan vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield ' multicast group '
            yield str(environment.getattr(l_1_vrf, 'multicast_group'))
            yield '\n'
        l_1_vrf = missing
        if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'multicast'), 'headend_replication'), True):
            pass
            yield '   vxlan multicast headend-replication\n'
        if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'ecn_propagation'), True):
            pass
            yield '   vxlan qos ecn propagation\n'
        elif t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'ecn_propagation'), False):
            pass
            yield '   no vxlan qos ecn propagation\n'
        if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'dscp_propagation_encapsulation'), True):
            pass
            yield '   vxlan qos dscp propagation encapsulation\n'
        elif t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'dscp_propagation_encapsulation'), False):
            pass
            yield '   no vxlan qos dscp propagation encapsulation\n'
        if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'map_dscp_to_traffic_class_decapsulation'), True):
            pass
            yield '   vxlan qos map dscp to traffic-class decapsulation\n'
        elif t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'map_dscp_to_traffic_class_decapsulation'), False):
            pass
            yield '   no vxlan qos map dscp to traffic-class decapsulation\n'
        if t_5(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'eos_cli')):
            pass
            yield '   '
            yield str(t_3(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'eos_cli'), 3, False))
            yield '\n'

blocks = {}
debug_info = '8=43&9=46&12=49&13=52&15=54&16=57&18=59&21=62&22=65&24=67&25=70&27=72&30=75&33=78&34=81&35=84&38=89&39=92&40=95&43=100&44=103&46=105&47=107&50=110&52=116&53=119&56=121&57=124&59=126&60=129&61=132&64=137&65=145&67=150&68=158&70=163&73=166&75=169&78=172&80=175&83=178&85=181&88=184&89=187'