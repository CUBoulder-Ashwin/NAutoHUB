from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'connected_endpoints_documentation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_all_connected_endpoints = resolve('all_connected_endpoints')
    l_0_all_connected_endpoints_keys = resolve('all_connected_endpoints_keys')
    l_0_all_port_profiles = resolve('all_port_profiles')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    pass
    yield '## Connected Endpoints\n'
    if (t_3((undefined(name='all_connected_endpoints') if l_0_all_connected_endpoints is missing else l_0_all_connected_endpoints)) == 0):
        pass
        yield '\nNo connected endpoint configured!\n'
    else:
        pass
        yield '\n### Connected Endpoint Keys\n\n| Key | Type | Description |\n| --- | ---- | ----------- |\n'
        for l_1_connected_endpoints_key in (undefined(name='all_connected_endpoints_keys') if l_0_all_connected_endpoints_keys is missing else l_0_all_connected_endpoints_keys):
            l_1_key = l_1_type = l_1_description = missing
            _loop_vars = {}
            pass
            l_1_key = environment.getattr(l_1_connected_endpoints_key, 'key')
            _loop_vars['key'] = l_1_key
            l_1_type = environment.getattr(l_1_connected_endpoints_key, 'type')
            _loop_vars['type'] = l_1_type
            l_1_description = t_1(environment.getattr(l_1_connected_endpoints_key, 'description'), '-')
            _loop_vars['description'] = l_1_description
            yield '| '
            yield str((undefined(name='key') if l_1_key is missing else l_1_key))
            yield ' | '
            yield str((undefined(name='type') if l_1_type is missing else l_1_type))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' |\n'
        l_1_connected_endpoints_key = l_1_key = l_1_type = l_1_description = missing
        for l_1_key in (undefined(name='all_connected_endpoints') if l_0_all_connected_endpoints is missing else l_0_all_connected_endpoints):
            _loop_vars = {}
            pass
            yield '\n### '
            yield str(t_2(t_4(context.eval_ctx, l_1_key, '_', ' ')))
            yield '\n\n| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Mode | Access VLAN | Trunk Allowed VLANs | Profile |\n| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ----------- | ------------------- | ------- |\n'
            for l_2_connected_endpoint in environment.getitem((undefined(name='all_connected_endpoints') if l_0_all_connected_endpoints is missing else l_0_all_connected_endpoints), l_1_key):
                l_2_port = l_2_fabric_port = l_2_profile = l_2_description = l_2_shutdown = l_2_mode = l_2_access_vlan = l_2_trunk_allowed_vlan = missing
                _loop_vars = {}
                pass
                l_2_port = environment.getattr(l_2_connected_endpoint, 'peer_interface')
                _loop_vars['port'] = l_2_port
                l_2_fabric_port = environment.getattr(l_2_connected_endpoint, 'fabric_port')
                _loop_vars['fabric_port'] = l_2_fabric_port
                l_2_profile = t_1(environment.getattr(l_2_connected_endpoint, 'profile'), '-')
                _loop_vars['profile'] = l_2_profile
                l_2_description = t_1(environment.getattr(l_2_connected_endpoint, 'description'), '-')
                _loop_vars['description'] = l_2_description
                l_2_shutdown = t_1(environment.getattr(l_2_connected_endpoint, 'shutdown'), '-')
                _loop_vars['shutdown'] = l_2_shutdown
                l_2_mode = t_1(environment.getattr(l_2_connected_endpoint, 'mode'), '-')
                _loop_vars['mode'] = l_2_mode
                l_2_access_vlan = t_1(environment.getattr(l_2_connected_endpoint, 'access_vlan'), '-')
                _loop_vars['access_vlan'] = l_2_access_vlan
                l_2_trunk_allowed_vlan = t_1(environment.getattr(l_2_connected_endpoint, 'trunk_allowed_vlan'), '-')
                _loop_vars['trunk_allowed_vlan'] = l_2_trunk_allowed_vlan
                yield '| '
                yield str(environment.getattr(l_2_connected_endpoint, 'peer'))
                yield ' | '
                yield str((undefined(name='port') if l_2_port is missing else l_2_port))
                yield ' | '
                yield str(environment.getattr(l_2_connected_endpoint, 'fabric_switch'))
                yield ' | '
                yield str((undefined(name='fabric_port') if l_2_fabric_port is missing else l_2_fabric_port))
                yield ' | '
                yield str((undefined(name='description') if l_2_description is missing else l_2_description))
                yield ' | '
                yield str((undefined(name='shutdown') if l_2_shutdown is missing else l_2_shutdown))
                yield ' | '
                yield str((undefined(name='mode') if l_2_mode is missing else l_2_mode))
                yield ' | '
                yield str((undefined(name='access_vlan') if l_2_access_vlan is missing else l_2_access_vlan))
                yield ' | '
                yield str((undefined(name='trunk_allowed_vlan') if l_2_trunk_allowed_vlan is missing else l_2_trunk_allowed_vlan))
                yield ' | '
                yield str((undefined(name='profile') if l_2_profile is missing else l_2_profile))
                yield ' |\n'
            l_2_connected_endpoint = l_2_port = l_2_fabric_port = l_2_profile = l_2_description = l_2_shutdown = l_2_mode = l_2_access_vlan = l_2_trunk_allowed_vlan = missing
        l_1_key = missing
    if (t_3((undefined(name='all_port_profiles') if l_0_all_port_profiles is missing else l_0_all_port_profiles)) > 0):
        pass
        yield '\n### Port Profiles\n\n| Profile Name | Parent Profile |\n| ------------ | -------------- |\n'
        for l_1_profile in (undefined(name='all_port_profiles') if l_0_all_port_profiles is missing else l_0_all_port_profiles):
            l_1_parent = missing
            _loop_vars = {}
            pass
            l_1_parent = t_1(environment.getattr(l_1_profile, 'parent_profile'), '-')
            _loop_vars['parent'] = l_1_parent
            yield '| '
            yield str(environment.getattr(l_1_profile, 'profile'))
            yield ' | '
            yield str((undefined(name='parent') if l_1_parent is missing else l_1_parent))
            yield ' |\n'
        l_1_profile = l_1_parent = missing

blocks = {}
debug_info = '7=39&16=45&17=49&18=51&19=53&20=56&22=63&24=67&28=69&29=73&30=75&31=77&32=79&33=81&34=83&35=85&36=87&37=90&41=112&47=115&48=119&49=122'