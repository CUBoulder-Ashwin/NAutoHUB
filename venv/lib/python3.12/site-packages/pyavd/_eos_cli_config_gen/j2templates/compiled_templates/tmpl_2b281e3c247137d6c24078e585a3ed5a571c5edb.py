from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/acl.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_standard_access_lists = resolve('standard_access_lists')
    l_0_access_lists = resolve('access_lists')
    l_0_ip_access_lists = resolve('ip_access_lists')
    l_0_ipv6_standard_access_lists = resolve('ipv6_standard_access_lists')
    l_0_ipv6_access_lists = resolve('ipv6_access_lists')
    l_0_mac_access_lists = resolve('mac_access_lists')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (((((t_1((undefined(name='standard_access_lists') if l_0_standard_access_lists is missing else l_0_standard_access_lists)) or t_1((undefined(name='access_lists') if l_0_access_lists is missing else l_0_access_lists))) or t_1((undefined(name='ip_access_lists') if l_0_ip_access_lists is missing else l_0_ip_access_lists))) or t_1((undefined(name='ipv6_standard_access_lists') if l_0_ipv6_standard_access_lists is missing else l_0_ipv6_standard_access_lists))) or t_1((undefined(name='ipv6_access_lists') if l_0_ipv6_access_lists is missing else l_0_ipv6_access_lists))) or t_1((undefined(name='mac_access_lists') if l_0_mac_access_lists is missing else l_0_mac_access_lists))):
        pass
        yield '\n## ACL\n'
        template = environment.get_template('documentation/standard-access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-standard-access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ipv6-access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/mac-access-lists.j2', 'documentation/acl.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '6=23&15=26&17=29&19=32&21=35&23=38&25=41'