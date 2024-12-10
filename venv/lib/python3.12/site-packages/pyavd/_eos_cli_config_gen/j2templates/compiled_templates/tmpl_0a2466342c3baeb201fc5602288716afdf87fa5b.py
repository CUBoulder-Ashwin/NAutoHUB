from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-api-http.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_http = resolve('management_api_http')
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
    if t_3((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http)):
        pass
        yield '\n### Management API HTTP\n\n#### Management API HTTP Summary\n\n| HTTP | HTTPS | Default Services |\n| ---- | ----- | ---------------- |\n| '
        yield str(t_1(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_http'), False))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_https'), True))
        yield ' | '
        yield str(t_1(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'default_services'), '-'))
        yield ' |\n'
        if (t_3(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_https'), True) and t_3(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'https_ssl_profile'))):
            pass
            yield '\nManagement HTTPS is using the SSL profile '
            yield str(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'https_ssl_profile'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_vrfs')):
            pass
            yield '\n#### Management API VRF Access\n\n| VRF Name | IPv4 ACL | IPv6 ACL |\n| -------- | -------- | -------- |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_vrfs'), 'name'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_vrf, 'access_group'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_vrf, 'ipv6_access_group'), '-'))
                yield ' |\n'
            l_1_vrf = missing
        if (t_3(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'certificate')) and t_3(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'private_key'))):
            pass
            yield '\nHTTPS certificate and private key are configured.\n'
        yield '\n#### Management API HTTP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-api-http.j2', 'documentation/management-api-http.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=39&18=42&20=44&26=47&27=51&30=58&38=62'