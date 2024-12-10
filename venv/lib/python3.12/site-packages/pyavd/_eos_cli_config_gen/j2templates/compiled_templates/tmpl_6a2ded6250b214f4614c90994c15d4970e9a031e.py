from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-client-source-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_ftp_client_source_interfaces = resolve('ip_ftp_client_source_interfaces')
    l_0_ip_http_client_source_interfaces = resolve('ip_http_client_source_interfaces')
    l_0_ip_ssh_client_source_interfaces = resolve('ip_ssh_client_source_interfaces')
    l_0_ip_telnet_client_source_interfaces = resolve('ip_telnet_client_source_interfaces')
    l_0_ip_tftp_client_source_interfaces = resolve('ip_tftp_client_source_interfaces')
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
        t_3 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((((t_4((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)) or t_4((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces))) or t_4((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces))) or t_4((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces))) or t_4((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces))):
        pass
        yield '\n### IP Client Source Interfaces\n\n| IP Client | VRF | Source Interface Name |\n| --------- | --- | --------------------- |\n'
        if t_4((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)):
            pass
            for l_1_ip_ftp_client_source_interface in t_2((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)):
                _loop_vars = {}
                pass
                yield '| FTP | '
                yield str(t_1(environment.getattr(l_1_ip_ftp_client_source_interface, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_ip_ftp_client_source_interface, 'name'))
                yield ' |\n'
            l_1_ip_ftp_client_source_interface = missing
        if t_4((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces)):
            pass
            for l_1_ip_http_client_source_interface in t_2((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces)):
                _loop_vars = {}
                pass
                yield '| HTTP | '
                yield str(t_1(environment.getattr(l_1_ip_http_client_source_interface, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_ip_http_client_source_interface, 'name'))
                yield ' |\n'
            l_1_ip_http_client_source_interface = missing
        if t_4((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces)):
            pass
            for l_1_ip_ssh_client_source_interface in t_2((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces)):
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_ip_ssh_client_source_interface, 'name')):
                    pass
                    yield '| SSH | '
                    yield str(t_1(environment.getattr(l_1_ip_ssh_client_source_interface, 'vrf'), 'default'))
                    yield ' | '
                    yield str(t_3(environment.getattr(l_1_ip_ssh_client_source_interface, 'name')))
                    yield ' |\n'
            l_1_ip_ssh_client_source_interface = missing
        if t_4((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces)):
            pass
            for l_1_ip_telnet_client_source_interface in t_2((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces)):
                _loop_vars = {}
                pass
                yield '| Telnet | '
                yield str(t_1(environment.getattr(l_1_ip_telnet_client_source_interface, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_ip_telnet_client_source_interface, 'name'))
                yield ' |\n'
            l_1_ip_telnet_client_source_interface = missing
        if t_4((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces)):
            pass
            for l_1_ip_tftp_client_source_interface in t_2((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces)):
                _loop_vars = {}
                pass
                yield '| TFTP | '
                yield str(t_1(environment.getattr(l_1_ip_tftp_client_source_interface, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_ip_tftp_client_source_interface, 'name'))
                yield ' |\n'
            l_1_ip_tftp_client_source_interface = missing
        yield '\n#### IP Client Source Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-client-source-interfaces.j2', 'documentation/ip-client-source-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield ' ```\n'

blocks = {}
debug_info = '7=40&13=43&14=45&15=49&18=54&19=56&20=60&23=65&24=67&25=70&26=73&30=78&31=80&32=84&35=89&36=91&37=95&44=101'