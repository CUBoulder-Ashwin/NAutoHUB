from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/filters.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_community_lists = resolve('community_lists')
    l_0_ip_community_lists = resolve('ip_community_lists')
    l_0_peer_filters = resolve('peer_filters')
    l_0_dynamic_prefix_lists = resolve('dynamic_prefix_lists')
    l_0_prefix_lists = resolve('prefix_lists')
    l_0_ipv6_prefix_lists = resolve('ipv6_prefix_lists')
    l_0_route_maps = resolve('route_maps')
    l_0_ip_extcommunity_lists = resolve('ip_extcommunity_lists')
    l_0_ip_extcommunity_lists_regexp = resolve('ip_extcommunity_lists_regexp')
    l_0_match_list_input = resolve('match_list_input')
    l_0_as_path = resolve('as_path')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((((((((((t_1((undefined(name='community_lists') if l_0_community_lists is missing else l_0_community_lists)) or t_1((undefined(name='ip_community_lists') if l_0_ip_community_lists is missing else l_0_ip_community_lists))) or t_1((undefined(name='peer_filters') if l_0_peer_filters is missing else l_0_peer_filters))) or t_1((undefined(name='dynamic_prefix_lists') if l_0_dynamic_prefix_lists is missing else l_0_dynamic_prefix_lists))) or t_1((undefined(name='prefix_lists') if l_0_prefix_lists is missing else l_0_prefix_lists))) or t_1((undefined(name='ipv6_prefix_lists') if l_0_ipv6_prefix_lists is missing else l_0_ipv6_prefix_lists))) or t_1((undefined(name='route_maps') if l_0_route_maps is missing else l_0_route_maps))) or t_1((undefined(name='ip_extcommunity_lists') if l_0_ip_extcommunity_lists is missing else l_0_ip_extcommunity_lists))) or t_1((undefined(name='ip_extcommunity_lists_regexp') if l_0_ip_extcommunity_lists_regexp is missing else l_0_ip_extcommunity_lists_regexp))) or t_1((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input))) or t_1((undefined(name='as_path') if l_0_as_path is missing else l_0_as_path))):
        pass
        yield '\n## Filters\n'
        template = environment.get_template('documentation/community-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-community-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/peer-filters.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/dynamic-prefix-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/prefix-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-prefix-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/route-maps.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-extcommunity-lists.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-extcommunity-lists-regexp.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/match-list-input.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/as-path.j2', 'documentation/filters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '6=28&20=31&22=34&24=37&26=40&28=43&30=46&32=49&34=52&36=55&38=58&40=61'