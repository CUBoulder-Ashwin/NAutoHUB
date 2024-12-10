from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/vxlan-interface.j2'

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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_vxlan_config = t_1(environment.getattr((undefined(name='vxlan_interface') if l_0_vxlan_interface is missing else l_0_vxlan_interface), 'vxlan1'), environment.getattr((undefined(name='vxlan_interface') if l_0_vxlan_interface is missing else l_0_vxlan_interface), 'Vxlan1'))
    context.vars['vxlan_config'] = l_0_vxlan_config
    context.exported_vars.add('vxlan_config')
    if t_4((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config)):
        pass
        yield '\n### VXLAN Interface\n\n#### VXLAN Interface Summary\n\n| Setting | Value |\n| ------- | ----- |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'source_interface')):
            pass
            yield '| Source Interface | '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'source_interface'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'controller_client'), 'enabled')):
            pass
            yield '| Controller Client | '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'controller_client'), 'enabled'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'mlag_source_interface')):
            pass
            yield '| MLAG Source Interface | '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'mlag_source_interface'))
            yield ' |\n'
        yield '| UDP port | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'udp_port'), '4789'))
        yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vtep_to_vtep_bridging'), True):
            pass
            yield '| Vtep-to-Vtep Bridging | '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vtep_to_vtep_bridging'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'virtual_router_encapsulation_mac_address')):
            pass
            yield '| EVPN MLAG Shared Router MAC | '
            yield str(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'virtual_router_encapsulation_mac_address'))
            yield ' |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vtep_learned_data_plane'), True):
            pass
            yield '| VXLAN flood-lists learning from data-plane | Enabled |\n'
        elif t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vtep_learned_data_plane'), False):
            pass
            yield '| VXLAN flood-lists learning from data-plane | Disabled |\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'dscp_propagation_encapsulation'), True):
            pass
            yield '| Qos dscp propagation encapsulation | Enabled |\n'
        elif t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'dscp_propagation_encapsulation'), False):
            pass
            yield '| Qos dscp propagation encapsulation | Disabled |\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'ecn_propagation'), True):
            pass
            yield '| Qos ECN propagation | Enabled |\n'
        elif t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'ecn_propagation'), False):
            pass
            yield '| Qos ECN propagation | Disabled |\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'map_dscp_to_traffic_class_decapsulation'), True):
            pass
            yield '| Qos map dscp to traffic-class decapsulation | Enabled |\n'
        elif t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'qos'), 'map_dscp_to_traffic_class_decapsulation'), False):
            pass
            yield '| Qos map dscp to traffic-class decapsulation | Disabled |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn')):
            pass
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'interval')):
                pass
                yield '| Remote VTEPs EVPN BFD transmission rate | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'interval'))
                yield 'ms |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'min_rx')):
                pass
                yield '| Remote VTEPs EVPN BFD expected minimum incoming rate (min-rx) | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'min_rx'))
                yield 'ms |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'multiplier')):
                pass
                yield '| Remote VTEPs EVPN BFD multiplier | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'multiplier'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'prefix_list')):
                pass
                yield '| Remote VTEPs EVPN BFD prefix-list | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'bfd_vtep_evpn'), 'prefix_list'))
                yield ' |\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'multicast'), 'headend_replication'), True):
            pass
            yield '| Multicast headend-replication | Enabled |\n'
        elif t_4(environment.getattr(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'multicast'), 'headend_replication'), False):
            pass
            yield '| Multicast headend-replication | Disabled |\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vlans')):
            pass
            yield '\n##### VLAN to VNI, Flood List and Multicast Group Mappings\n\n| VLAN | VNI | Flood List | Multicast Group |\n| ---- | --- | ---------- | --------------- |\n'
            for l_1_vlan in t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vlans'), 'id'):
                l_1_flood_list = resolve('flood_list')
                l_1_vlan_vni = l_1_multicast_group = missing
                _loop_vars = {}
                pass
                l_1_vlan_vni = t_1(environment.getattr(l_1_vlan, 'vni'), '-')
                _loop_vars['vlan_vni'] = l_1_vlan_vni
                l_1_multicast_group = t_1(environment.getattr(l_1_vlan, 'multicast_group'), '-')
                _loop_vars['multicast_group'] = l_1_multicast_group
                if t_4(environment.getattr(l_1_vlan, 'flood_vteps')):
                    pass
                    l_1_flood_list = t_3(context.eval_ctx, environment.getattr(l_1_vlan, 'flood_vteps'), '<br/>')
                    _loop_vars['flood_list'] = l_1_flood_list
                else:
                    pass
                    l_1_flood_list = '-'
                    _loop_vars['flood_list'] = l_1_flood_list
                yield '| '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' | '
                yield str((undefined(name='vlan_vni') if l_1_vlan_vni is missing else l_1_vlan_vni))
                yield ' | '
                yield str((undefined(name='flood_list') if l_1_flood_list is missing else l_1_flood_list))
                yield ' | '
                yield str((undefined(name='multicast_group') if l_1_multicast_group is missing else l_1_multicast_group))
                yield ' |\n'
            l_1_vlan = l_1_vlan_vni = l_1_multicast_group = l_1_flood_list = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vrfs')):
            pass
            yield '\n##### VRF to VNI and Multicast Group Mappings\n\n| VRF | VNI | Multicast Group |\n| ---- | --- | --------------- |\n'
            for l_1_vrf in t_2(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'vrfs'), 'name'):
                l_1_vrf_vni = l_1_multicast_group = missing
                _loop_vars = {}
                pass
                l_1_vrf_vni = t_1(environment.getattr(l_1_vrf, 'vni'), '-')
                _loop_vars['vrf_vni'] = l_1_vrf_vni
                l_1_multicast_group = t_1(environment.getattr(l_1_vrf, 'multicast_group'), '-')
                _loop_vars['multicast_group'] = l_1_multicast_group
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str((undefined(name='vrf_vni') if l_1_vrf_vni is missing else l_1_vrf_vni))
                yield ' | '
                yield str((undefined(name='multicast_group') if l_1_multicast_group is missing else l_1_multicast_group))
                yield ' |\n'
            l_1_vrf = l_1_vrf_vni = l_1_multicast_group = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vteps')):
            pass
            yield '\n##### Default Flood List\n\n| Default Flood List |\n| ------------------ |\n| '
            yield str(t_3(context.eval_ctx, environment.getattr(environment.getattr((undefined(name='vxlan_config') if l_0_vxlan_config is missing else l_0_vxlan_config), 'vxlan'), 'flood_vteps'), '<br/>'))
            yield ' |\n'
        yield '\n#### VXLAN Interface Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/vxlan-interface.j2', 'documentation/vxlan-interface.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'vxlan_config': l_0_vxlan_config})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '8=37&9=40&17=43&18=46&20=48&21=51&23=53&24=56&26=59&27=61&28=64&30=66&31=69&33=71&35=74&38=77&40=80&43=83&45=86&48=89&50=92&53=95&54=97&55=100&57=102&58=105&60=107&61=110&63=112&64=115&67=117&69=120&72=123&78=126&79=131&80=133&81=135&82=137&84=141&86=144&89=153&95=156&96=160&97=162&98=165&101=172&107=175&113=178'