from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/platform.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_platform = resolve('platform')
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
    if t_2((undefined(name='platform') if l_0_platform is missing else l_0_platform)):
        pass
        yield '!\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'l3')):
            pass
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'l3'), 'routing_mac_address_per_vlan'), True):
                pass
                yield 'platform trident l3 routing mac-address per-vlan\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'forwarding_table_partition')):
            pass
            yield 'platform trident forwarding-table partition '
            yield str(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'forwarding_table_partition'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'forwarding_mode')):
                pass
                yield 'platform sand forwarding mode '
                yield str(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'forwarding_mode'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'lag'), 'mode')):
                pass
                yield 'platform sand lag mode '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'lag'), 'mode'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'lag'), 'hardware_only'), True):
                pass
                yield 'platform sand lag hardware-only\n'
            for l_1_qos_map in t_1(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'qos_maps'), 'traffic_class'):
                _loop_vars = {}
                pass
                if (t_2(environment.getattr(l_1_qos_map, 'traffic_class')) and t_2(environment.getattr(l_1_qos_map, 'to_network_qos'))):
                    pass
                    yield 'platform sand qos map traffic-class '
                    yield str(environment.getattr(l_1_qos_map, 'traffic_class'))
                    yield ' to network-qos '
                    yield str(environment.getattr(l_1_qos_map, 'to_network_qos'))
                    yield '\n'
            l_1_qos_map = missing
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'multicast_replication'), 'default')):
                pass
                yield 'platform sand multicast replication default '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'multicast_replication'), 'default'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'mdb_profile')):
                pass
                yield 'platform sand mdb profile '
                yield str(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sand'), 'mdb_profile'))
                yield '\n'
        if t_2(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sfe')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sfe'), 'data_plane_cpu_allocation_max')):
                pass
                yield 'platform sfe data-plane cpu allocation maximum '
                yield str(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'sfe'), 'data_plane_cpu_allocation_max'))
                yield '\n'

blocks = {}
debug_info = '7=24&9=27&10=29&14=32&15=35&17=37&18=39&19=42&21=44&22=47&24=49&27=52&28=55&29=58&32=63&33=66&35=68&36=71&39=73&40=75&41=78'