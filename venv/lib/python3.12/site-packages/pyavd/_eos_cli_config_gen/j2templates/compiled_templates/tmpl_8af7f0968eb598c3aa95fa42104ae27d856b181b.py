from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/authentication.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_local_users = resolve('local_users')
    l_0_roles = resolve('roles')
    l_0_enable_password = resolve('enable_password')
    l_0_management_defaults = resolve('management_defaults')
    l_0_tacacs_servers = resolve('tacacs_servers')
    l_0_ip_tacacs_source_interfaces = resolve('ip_tacacs_source_interfaces')
    l_0_radius_server = resolve('radius_server')
    l_0_ip_radius_source_interfaces = resolve('ip_radius_source_interfaces')
    l_0_aaa_server_groups = resolve('aaa_server_groups')
    l_0_aaa_authentication = resolve('aaa_authentication')
    l_0_aaa_authorization = resolve('aaa_authorization')
    l_0_aaa_accounting = resolve('aaa_accounting')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (((((((((((t_1((undefined(name='local_users') if l_0_local_users is missing else l_0_local_users)) or t_1((undefined(name='roles') if l_0_roles is missing else l_0_roles))) or t_1((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password))) or t_1((undefined(name='management_defaults') if l_0_management_defaults is missing else l_0_management_defaults))) or t_1((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers))) or t_1((undefined(name='ip_tacacs_source_interfaces') if l_0_ip_tacacs_source_interfaces is missing else l_0_ip_tacacs_source_interfaces))) or t_1((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server))) or t_1((undefined(name='ip_radius_source_interfaces') if l_0_ip_radius_source_interfaces is missing else l_0_ip_radius_source_interfaces))) or t_1((undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups))) or t_1((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication))) or t_1((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization))) or t_1((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting))):
        pass
        yield '\n## Authentication\n'
        template = environment.get_template('documentation/local-users.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/roles.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/enable-password.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-defaults.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/tacacs-servers.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-tacacs-source-interfaces.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/radius-server.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-radius-source-interfaces.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/aaa-server-groups.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/aaa-authentication.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/aaa-authorization.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/aaa-accounting.j2', 'documentation/authentication.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '6=29&21=32&23=35&25=38&27=41&29=44&31=47&33=50&35=53&37=56&39=59&41=62&43=65'