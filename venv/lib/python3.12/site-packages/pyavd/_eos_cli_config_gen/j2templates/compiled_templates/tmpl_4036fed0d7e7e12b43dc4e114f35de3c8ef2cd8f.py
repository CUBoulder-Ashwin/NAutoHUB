from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-adaptive-virtual-topology.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_adaptive_virtual_topology = resolve('router_adaptive_virtual_topology')
    l_0_topology_role = resolve('topology_role')
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
    if t_2((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology)):
        pass
        yield '!\nrouter adaptive-virtual-topology\n'
        if t_2(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'topology_role')):
            pass
            l_0_topology_role = str_join(('topology role ', environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'topology_role'), ))
            context.vars['topology_role'] = l_0_topology_role
            context.exported_vars.add('topology_role')
            if (t_2(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'gateway_vxlan'), True) and (environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'topology_role') in ['edge', 'transit zone', 'transit region'])):
                pass
                l_0_topology_role = str_join(((undefined(name='topology_role') if l_0_topology_role is missing else l_0_topology_role), ' gateway vxlan', ))
                context.vars['topology_role'] = l_0_topology_role
                context.exported_vars.add('topology_role')
            yield '   '
            yield str((undefined(name='topology_role') if l_0_topology_role is missing else l_0_topology_role))
            yield '\n'
        if (t_2(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'region'), 'name')) and environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'region'), 'id')):
            pass
            yield '   region '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'region'), 'name'))
            yield ' id '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'region'), 'id'))
            yield '\n'
        if (t_2(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'zone'), 'name')) and environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'zone'), 'id')):
            pass
            yield '   zone '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'zone'), 'name'))
            yield ' id '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'zone'), 'id'))
            yield '\n'
        if (t_2(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'site'), 'name')) and environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'site'), 'id')):
            pass
            yield '   site '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'site'), 'name'))
            yield ' id '
            yield str(environment.getattr(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'site'), 'id'))
            yield '\n'
        for l_1_policy in t_1(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'policies'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   policy '
            yield str(environment.getattr(l_1_policy, 'name'))
            yield '\n'
            for l_2_match in environment.getattr(l_1_policy, 'matches'):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_2_match, 'application_profile')):
                    pass
                    yield '      !\n      match application-profile '
                    yield str(environment.getattr(l_2_match, 'application_profile'))
                    yield '\n'
                    if t_2(environment.getattr(l_2_match, 'avt_profile')):
                        pass
                        yield '         avt profile '
                        yield str(environment.getattr(l_2_match, 'avt_profile'))
                        yield '\n'
                    if t_2(environment.getattr(l_2_match, 'traffic_class')):
                        pass
                        yield '         traffic-class '
                        yield str(environment.getattr(l_2_match, 'traffic_class'))
                        yield '\n'
                    if t_2(environment.getattr(l_2_match, 'dscp')):
                        pass
                        yield '         dscp '
                        yield str(environment.getattr(l_2_match, 'dscp'))
                        yield '\n'
            l_2_match = missing
        l_1_policy = missing
        for l_1_profile in t_1(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_profile, 'internet_exit_policy')):
                pass
                yield '      internet-exit policy '
                yield str(environment.getattr(l_1_profile, 'internet_exit_policy'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'load_balance_policy')):
                pass
                yield '      path-selection load-balance '
                yield str(environment.getattr(l_1_profile, 'load_balance_policy'))
                yield '\n'
        l_1_profile = missing
        for l_1_vrf in t_1(environment.getattr((undefined(name='router_adaptive_virtual_topology') if l_0_router_adaptive_virtual_topology is missing else l_0_router_adaptive_virtual_topology), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_vrf, 'policy')):
                pass
                yield '      avt policy '
                yield str(environment.getattr(l_1_vrf, 'policy'))
                yield '\n'
            for l_2_profile in t_1(environment.getattr(l_1_vrf, 'profiles'), 'id'):
                _loop_vars = {}
                pass
                if (t_2(environment.getattr(l_2_profile, 'name')) and t_2(environment.getattr(l_2_profile, 'id'))):
                    pass
                    yield '      avt profile '
                    yield str(environment.getattr(l_2_profile, 'name'))
                    yield ' id '
                    yield str(environment.getattr(l_2_profile, 'id'))
                    yield '\n'
            l_2_profile = missing
        l_1_vrf = missing

blocks = {}
debug_info = '7=25&10=28&11=30&12=33&13=35&15=39&17=41&18=44&20=48&21=51&23=55&24=58&27=62&29=66&30=68&31=71&33=74&34=76&35=79&37=81&38=84&40=86&41=89&47=93&49=97&50=99&51=102&53=104&54=107&58=110&60=114&61=116&62=119&64=121&65=124&66=127'