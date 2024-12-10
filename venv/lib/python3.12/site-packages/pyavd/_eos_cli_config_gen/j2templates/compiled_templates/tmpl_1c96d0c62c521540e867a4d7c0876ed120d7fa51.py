from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-msdp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_msdp = resolve('router_msdp')
    l_0_namespace = resolve('namespace')
    l_0_msdp_info = resolve('msdp_info')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp)):
        pass
        yield '\n### Router MSDP\n'
        l_0_msdp_info = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), peers=[])
        context.vars['msdp_info'] = l_0_msdp_info
        context.exported_vars.add('msdp_info')
        for l_1_peer in t_1(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'peers'), []):
            _loop_vars = {}
            pass
            context.call(environment.getattr(environment.getattr((undefined(name='msdp_info') if l_0_msdp_info is missing else l_0_msdp_info), 'peers'), 'append'), l_1_peer, _loop_vars=_loop_vars)
        l_1_peer = missing
        for l_1_vrf in t_1(environment.getattr((undefined(name='router_msdp') if l_0_router_msdp is missing else l_0_router_msdp), 'vrfs'), []):
            _loop_vars = {}
            pass
            for l_2_peer in t_1(environment.getattr(l_1_vrf, 'peers'), []):
                _loop_vars = {}
                pass
                context.call(environment.getattr(l_2_peer, 'update'), {'vrf': environment.getattr(l_1_vrf, 'name')}, _loop_vars=_loop_vars)
                context.call(environment.getattr(environment.getattr((undefined(name='msdp_info') if l_0_msdp_info is missing else l_0_msdp_info), 'peers'), 'append'), l_2_peer, _loop_vars=_loop_vars)
            l_2_peer = missing
        l_1_vrf = missing
        if (t_3(environment.getattr((undefined(name='msdp_info') if l_0_msdp_info is missing else l_0_msdp_info), 'peers')) > 0):
            pass
            yield '\n#### Router MSDP Peers\n\n| Peer Address | Disabled | VRF | Default-peer | Default-peer Prefix List | Mesh Groups | Local Interface | Description | Inbound SA Filter | Outbound SA Filter |\n| ------------ | -------- | --- | ------------ | ------------------------ | ----------- | --------------- | ----------- | ----------------- | ------------------ |\n'
            for l_1_peer in environment.getattr((undefined(name='msdp_info') if l_0_msdp_info is missing else l_0_msdp_info), 'peers'):
                l_1_row_mesh_groups = resolve('row_mesh_groups')
                _loop_vars = {}
                pass
                if (t_3(t_1(environment.getattr(l_1_peer, 'mesh_groups'), [])) > 0):
                    pass
                    l_1_row_mesh_groups = []
                    _loop_vars['row_mesh_groups'] = l_1_row_mesh_groups
                    for l_2_mesh_group in environment.getattr(l_1_peer, 'mesh_groups'):
                        _loop_vars = {}
                        pass
                        context.call(environment.getattr((undefined(name='row_mesh_groups') if l_1_row_mesh_groups is missing else l_1_row_mesh_groups), 'append'), environment.getattr(l_2_mesh_group, 'name'), _loop_vars=_loop_vars)
                    l_2_mesh_group = missing
                    l_1_row_mesh_groups = t_2(context.eval_ctx, (undefined(name='row_mesh_groups') if l_1_row_mesh_groups is missing else l_1_row_mesh_groups), ', ')
                    _loop_vars['row_mesh_groups'] = l_1_row_mesh_groups
                yield '| '
                yield str(environment.getattr(l_1_peer, 'ipv4_address'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_peer, 'disabled'), False))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_peer, 'vrf'), 'default'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_peer, 'default_peer'), 'enabled'), False))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_peer, 'default_peer'), 'prefix_list'), '-'))
                yield ' | '
                yield str(t_1((undefined(name='row_mesh_groups') if l_1_row_mesh_groups is missing else l_1_row_mesh_groups), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_peer, 'local_interface'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_peer, 'description'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'in_list'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_peer, 'sa_filter'), 'out_list'), '-'))
                yield ' |\n'
            l_1_peer = l_1_row_mesh_groups = missing
        yield '\n#### Router MSDP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-msdp.j2', 'documentation/router-msdp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'msdp_info': l_0_msdp_info})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '6=38&9=41&10=44&11=47&13=49&14=52&15=55&16=56&19=59&25=62&26=66&27=68&28=70&29=73&31=75&33=78&40=100'