from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-msdp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_msdp = resolve('router_msdp')
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
    if t_3((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp)):
        pass
        yield '!\nrouter msdp\n'
        for l_1_group_limit in t_1(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'group_limits'), []):
            _loop_vars = {}
            pass
            yield '   group-limit '
            yield str(environment.getattr(l_1_group_limit, 'limit'))
            yield ' source '
            yield str(environment.getattr(l_1_group_limit, 'source_prefix'))
            yield '\n'
        l_1_group_limit = missing
        if t_3(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'originator_id_local_interface')):
            pass
            yield '   originator-id local-interface '
            yield str(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'originator_id_local_interface'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'rejected_limit')):
            pass
            yield '   rejected-limit '
            yield str(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'rejected_limit'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'forward_register_packets'), True):
            pass
            yield '   forward register-packets\n'
        if t_3(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'connection_retry_interval')):
            pass
            yield '   connection retry interval '
            yield str(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'connection_retry_interval'))
            yield '\n'
        for l_1_peer in t_2(t_1(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'peers'), []), 'ipv4_address'):
            l_1_default_peer_cli = resolve('default_peer_cli')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_peer, 'ipv4_address')):
                pass
                yield '   !\n   peer '
                yield str(environment.getattr(l_1_peer, 'ipv4_address'))
                yield '\n'
                if t_3(environment.getattr(environment.getattr(l_1_peer, 'default_peer'), 'enabled'), True):
                    pass
                    l_1_default_peer_cli = 'default-peer'
                    _loop_vars['default_peer_cli'] = l_1_default_peer_cli
                    if t_3(environment.getattr(environment.getattr(l_1_peer, 'default_peer'), 'prefix_list')):
                        pass
                        l_1_default_peer_cli = str_join(((undefined(name='default_peer_cli') if l_1_default_peer_cli is missing else l_1_default_peer_cli), ' prefix-list ', environment.getattr(environment.getattr(l_1_peer, 'default_peer'), 'prefix_list'), ))
                        _loop_vars['default_peer_cli'] = l_1_default_peer_cli
                    yield '      '
                    yield str((undefined(name='default_peer_cli') if l_1_default_peer_cli is missing else l_1_default_peer_cli))
                    yield '\n'
                for l_2_mesh_group in t_2(t_1(environment.getattr(l_1_peer, 'mesh_groups'), []), 'name'):
                    _loop_vars = {}
                    pass
                    if t_3(environment.getattr(l_2_mesh_group, 'name')):
                        pass
                        yield '      mesh-group '
                        yield str(environment.getattr(l_2_mesh_group, 'name'))
                        yield '\n'
                l_2_mesh_group = missing
                if t_3(environment.getattr(l_1_peer, 'local_interface')):
                    pass
                    yield '      local-interface '
                    yield str(environment.getattr(l_1_peer, 'local_interface'))
                    yield '\n'
                if (t_3(environment.getattr(environment.getattr(l_1_peer, 'keepalive'), 'keepalive_timer')) and t_3(environment.getattr(environment.getattr(l_1_peer, 'keepalive'), 'hold_timer'))):
                    pass
                    yield '      keepalive '
                    yield str(environment.getattr(environment.getattr(l_1_peer, 'keepalive'), 'keepalive_timer'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(l_1_peer, 'keepalive'), 'hold_timer'))
                    yield '\n'
                if t_3(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'in_list')):
                    pass
                    yield '      sa-filter in list '
                    yield str(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'in_list'))
                    yield '\n'
                if t_3(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'out_list')):
                    pass
                    yield '      sa-filter out list '
                    yield str(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'out_list'))
                    yield '\n'
                if t_3(environment.getattr(l_1_peer, 'description')):
                    pass
                    yield '      description '
                    yield str(environment.getattr(l_1_peer, 'description'))
                    yield '\n'
                if t_3(environment.getattr(l_1_peer, 'disabled'), True):
                    pass
                    yield '      disabled\n'
                if t_3(environment.getattr(l_1_peer, 'sa_limit')):
                    pass
                    yield '      sa-limit '
                    yield str(environment.getattr(l_1_peer, 'sa_limit'))
                    yield '\n'
        l_1_peer = l_1_default_peer_cli = missing
        for l_1_vrf in t_2(t_1(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'vrfs'), []), 'name'):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_1_vrf, 'name')) and (environment.getattr(l_1_vrf, 'name') != 'default')):
                pass
                yield '   !\n   vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield '\n'
                for l_2_group_limit in t_2(t_1(environment.getattr(l_1_vrf, 'group_limits'), []), 'source_prefix'):
                    _loop_vars = {}
                    pass
                    yield '      group-limit '
                    yield str(environment.getattr(l_2_group_limit, 'limit'))
                    yield ' source '
                    yield str(environment.getattr(l_2_group_limit, 'source_prefix'))
                    yield '\n'
                l_2_group_limit = missing
                if t_3(environment.getattr(l_1_vrf, 'originator_id_local_interface')):
                    pass
                    yield '      originator-id local-interface '
                    yield str(environment.getattr(l_1_vrf, 'originator_id_local_interface'))
                    yield '\n'
                if t_3(environment.getattr(l_1_vrf, 'rejected_limit')):
                    pass
                    yield '      rejected-limit '
                    yield str(environment.getattr(l_1_vrf, 'rejected_limit'))
                    yield '\n'
                if t_3(environment.getattr(l_1_vrf, 'forward_register_packets'), True):
                    pass
                    yield '      forward register-packets\n'
                if t_3(environment.getattr(l_1_vrf, 'connection_retry_interval')):
                    pass
                    yield '      connection retry interval '
                    yield str(environment.getattr(l_1_vrf, 'connection_retry_interval'))
                    yield '\n'
                for l_2_peer in t_2(t_1(environment.getattr(l_1_vrf, 'peers'), []), 'ipv4_address'):
                    l_2_default_peer_cli = resolve('default_peer_cli')
                    _loop_vars = {}
                    pass
                    yield '      !\n      peer '
                    yield str(environment.getattr(l_2_peer, 'ipv4_address'))
                    yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_peer, 'default_peer'), 'enabled'), True):
                        pass
                        l_2_default_peer_cli = 'default-peer'
                        _loop_vars['default_peer_cli'] = l_2_default_peer_cli
                        if t_3(environment.getattr(environment.getattr(l_2_peer, 'default_peer'), 'prefix_list')):
                            pass
                            l_2_default_peer_cli = str_join(((undefined(name='default_peer_cli') if l_2_default_peer_cli is missing else l_2_default_peer_cli), ' prefix-list ', environment.getattr(environment.getattr(l_2_peer, 'default_peer'), 'prefix_list'), ))
                            _loop_vars['default_peer_cli'] = l_2_default_peer_cli
                        yield '         '
                        yield str((undefined(name='default_peer_cli') if l_2_default_peer_cli is missing else l_2_default_peer_cli))
                        yield '\n'
                    for l_3_mesh_group in t_1(environment.getattr(l_2_peer, 'mesh_groups'), []):
                        _loop_vars = {}
                        pass
                        if t_3(environment.getattr(l_3_mesh_group, 'name')):
                            pass
                            yield '         mesh-group '
                            yield str(environment.getattr(l_3_mesh_group, 'name'))
                            yield '\n'
                    l_3_mesh_group = missing
                    if t_3(environment.getattr(l_2_peer, 'local_interface')):
                        pass
                        yield '         local-interface '
                        yield str(environment.getattr(l_2_peer, 'local_interface'))
                        yield '\n'
                    if (t_3(environment.getattr(environment.getattr(l_2_peer, 'keepalive'), 'keepalive_timer')) and t_3(environment.getattr(environment.getattr(l_2_peer, 'keepalive'), 'hold_timer'))):
                        pass
                        yield '         keepalive '
                        yield str(environment.getattr(environment.getattr(l_2_peer, 'keepalive'), 'keepalive_timer'))
                        yield ' '
                        yield str(environment.getattr(environment.getattr(l_2_peer, 'keepalive'), 'hold_timer'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_peer, 'sa_filter'), 'in_list')):
                        pass
                        yield '         sa-filter in list '
                        yield str(environment.getattr(environment.getattr(l_2_peer, 'sa_filter'), 'in_list'))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_peer, 'sa_filter'), 'out_list')):
                        pass
                        yield '         sa-filter out list '
                        yield str(environment.getattr(environment.getattr(l_2_peer, 'sa_filter'), 'out_list'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_peer, 'description')):
                        pass
                        yield '         description '
                        yield str(environment.getattr(l_2_peer, 'description'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_peer, 'disabled'), True):
                        pass
                        yield '         disabled\n'
                    if t_3(environment.getattr(l_2_peer, 'sa_limit')):
                        pass
                        yield '         sa-limit '
                        yield str(environment.getattr(l_2_peer, 'sa_limit'))
                        yield '\n'
                l_2_peer = l_2_default_peer_cli = missing
        l_1_vrf = missing

blocks = {}
debug_info = '7=30&10=33&11=37&13=42&14=45&16=47&17=50&19=52&22=55&23=58&25=60&26=64&28=67&29=69&30=71&31=73&32=75&34=78&36=80&37=83&38=86&41=89&42=92&44=94&45=97&47=101&48=104&50=106&51=109&53=111&54=114&56=116&59=119&60=122&64=125&65=128&67=131&68=133&69=137&71=142&72=145&74=147&75=150&77=152&80=155&81=158&83=160&85=165&86=167&87=169&88=171&89=173&91=176&93=178&94=181&95=184&98=187&99=190&101=192&102=195&104=199&105=202&107=204&108=207&110=209&111=212&113=214&116=217&117=220'