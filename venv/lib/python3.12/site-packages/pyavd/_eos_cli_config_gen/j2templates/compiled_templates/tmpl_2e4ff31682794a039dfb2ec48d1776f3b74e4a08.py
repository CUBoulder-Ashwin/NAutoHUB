from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-traffic-engineering.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_traffic_engineering = resolve('router_traffic_engineering')
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
    if t_3(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'enabled'), True):
        pass
        yield '\n### Router Traffic-Engineering\n\n- Traffic Engineering is enabled.\n'
        if t_3(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing')):
            pass
            yield '\n#### Segment Routing Summary\n\n- SRTE is enabled.\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'colored_tunnel_rib'), True):
                pass
                yield '\n- system-colored-tunnel-rib is enabled\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'policy_endpoints')):
                pass
                yield '\n##### SRTE Policies\n\n| Endpoint | Color | Preference | Name | Description | SBFD Remote Discriminator | Label Stack | Index  | Weight | Explicit Null |\n| -------- | ----- | ---------- | ---- | ----------- | ------------------------- | ----------- | ------ | ------ | ------------- |\n'
                for l_1_endpoint in t_2(environment.getattr(environment.getattr((undefined(name='router_traffic_engineering') if l_0_router_traffic_engineering is missing else l_0_router_traffic_engineering), 'segment_routing'), 'policy_endpoints'), 'address'):
                    _loop_vars = {}
                    pass
                    for l_2_color in t_2(environment.getattr(l_1_endpoint, 'colors'), 'value'):
                        l_2_name = l_2_description = l_2_sbfd_remote = missing
                        _loop_vars = {}
                        pass
                        l_2_name = t_1(environment.getattr(l_2_color, 'name'), '-')
                        _loop_vars['name'] = l_2_name
                        l_2_description = t_1(environment.getattr(l_2_color, 'description'), '-')
                        _loop_vars['description'] = l_2_description
                        l_2_sbfd_remote = t_1(environment.getattr(l_2_color, 'sbfd_remote_discriminator'), '-')
                        _loop_vars['sbfd_remote'] = l_2_sbfd_remote
                        for l_3_pathgroup in t_2(environment.getattr(l_2_color, 'path_group'), 'preference'):
                            l_3_pathgroup_preference = l_3_expnull = missing
                            _loop_vars = {}
                            pass
                            l_3_pathgroup_preference = t_1(environment.getattr(l_3_pathgroup, 'preference'), '-')
                            _loop_vars['pathgroup_preference'] = l_3_pathgroup_preference
                            l_3_expnull = t_1(environment.getattr(l_3_pathgroup, 'explicit_null'), '-')
                            _loop_vars['expnull'] = l_3_expnull
                            for l_4_labelstack in t_2(environment.getattr(l_3_pathgroup, 'segment_list'), 'label_stack'):
                                l_4_stack = l_4_index = l_4_weight = missing
                                _loop_vars = {}
                                pass
                                l_4_stack = environment.getattr(l_4_labelstack, 'label_stack')
                                _loop_vars['stack'] = l_4_stack
                                l_4_index = t_1(environment.getattr(l_4_labelstack, 'index'), '-')
                                _loop_vars['index'] = l_4_index
                                l_4_weight = t_1(environment.getattr(l_4_labelstack, 'weight'), '-')
                                _loop_vars['weight'] = l_4_weight
                                yield '| '
                                yield str(environment.getattr(l_1_endpoint, 'address'))
                                yield ' | '
                                yield str(environment.getattr(l_2_color, 'value'))
                                yield ' | '
                                yield str((undefined(name='pathgroup_preference') if l_3_pathgroup_preference is missing else l_3_pathgroup_preference))
                                yield ' | '
                                yield str((undefined(name='name') if l_2_name is missing else l_2_name))
                                yield ' | '
                                yield str((undefined(name='description') if l_2_description is missing else l_2_description))
                                yield ' | '
                                yield str((undefined(name='sbfd_remote') if l_2_sbfd_remote is missing else l_2_sbfd_remote))
                                yield ' | '
                                yield str((undefined(name='stack') if l_4_stack is missing else l_4_stack))
                                yield ' | '
                                yield str((undefined(name='index') if l_4_index is missing else l_4_index))
                                yield ' | '
                                yield str((undefined(name='weight') if l_4_weight is missing else l_4_weight))
                                yield ' | '
                                yield str((undefined(name='expnull') if l_3_expnull is missing else l_3_expnull))
                                yield ' |\n'
                            l_4_labelstack = l_4_stack = l_4_index = l_4_weight = missing
                        l_3_pathgroup = l_3_pathgroup_preference = l_3_expnull = missing
                    l_2_color = l_2_name = l_2_description = l_2_sbfd_remote = missing
                l_1_endpoint = missing
        yield '\n#### Router Traffic Engineering Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-traffic-engineering.j2', 'documentation/router-traffic-engineering.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&17=36&21=39&27=42&28=45&29=49&30=51&31=53&32=55&33=59&34=61&35=63&36=67&37=69&38=71&39=74&50=99'