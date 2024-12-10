from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-client-source-interfaces.j2'

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
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((((t_3((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)) or t_3((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces))) or t_3((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces))) or t_3((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces))) or t_3((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces))):
        pass
        yield '!\n'
        if t_3((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)):
            pass
            for l_1_ip_ftp_client_source_interface in t_1((undefined(name='ip_ftp_client_source_interfaces') if l_0_ip_ftp_client_source_interfaces is missing else l_0_ip_ftp_client_source_interfaces)):
                l_1_ip_ftp_client_cli = resolve('ip_ftp_client_cli')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_ip_ftp_client_source_interface, 'name')):
                    pass
                    l_1_ip_ftp_client_cli = str_join(('ip ftp client source-interface ', t_2(environment.getattr(l_1_ip_ftp_client_source_interface, 'name')), ))
                    _loop_vars['ip_ftp_client_cli'] = l_1_ip_ftp_client_cli
                    if t_3(environment.getattr(l_1_ip_ftp_client_source_interface, 'vrf')):
                        pass
                        l_1_ip_ftp_client_cli = str_join(((undefined(name='ip_ftp_client_cli') if l_1_ip_ftp_client_cli is missing else l_1_ip_ftp_client_cli), ' vrf ', environment.getattr(l_1_ip_ftp_client_source_interface, 'vrf'), ))
                        _loop_vars['ip_ftp_client_cli'] = l_1_ip_ftp_client_cli
                    yield str((undefined(name='ip_ftp_client_cli') if l_1_ip_ftp_client_cli is missing else l_1_ip_ftp_client_cli))
                    yield '\n'
            l_1_ip_ftp_client_source_interface = l_1_ip_ftp_client_cli = missing
        for l_1_ip_http_client_source_interface in t_1((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces)):
            l_1_ip_http_client_cli = missing
            _loop_vars = {}
            pass
            l_1_ip_http_client_cli = 'ip http client'
            _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
            if t_3(environment.getattr(l_1_ip_http_client_source_interface, 'name')):
                pass
                l_1_ip_http_client_cli = str_join(((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli), ' local-interface ', environment.getattr(l_1_ip_http_client_source_interface, 'name'), ))
                _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
                if t_3(environment.getattr(l_1_ip_http_client_source_interface, 'vrf')):
                    pass
                    l_1_ip_http_client_cli = str_join(((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli), ' vrf ', environment.getattr(l_1_ip_http_client_source_interface, 'vrf'), ))
                    _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
                yield str((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli))
                yield '\n'
        l_1_ip_http_client_source_interface = l_1_ip_http_client_cli = missing
        if t_3((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces)):
            pass
            for l_1_ip_ssh_client_source_interface in t_1((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces)):
                l_1_ip_ssh_client_cli = resolve('ip_ssh_client_cli')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_ip_ssh_client_source_interface, 'name')):
                    pass
                    l_1_ip_ssh_client_cli = str_join(('ip ssh client source-interface ', t_2(environment.getattr(l_1_ip_ssh_client_source_interface, 'name')), ))
                    _loop_vars['ip_ssh_client_cli'] = l_1_ip_ssh_client_cli
                    if t_3(environment.getattr(l_1_ip_ssh_client_source_interface, 'vrf')):
                        pass
                        l_1_ip_ssh_client_cli = str_join(((undefined(name='ip_ssh_client_cli') if l_1_ip_ssh_client_cli is missing else l_1_ip_ssh_client_cli), ' vrf ', environment.getattr(l_1_ip_ssh_client_source_interface, 'vrf'), ))
                        _loop_vars['ip_ssh_client_cli'] = l_1_ip_ssh_client_cli
                    yield str((undefined(name='ip_ssh_client_cli') if l_1_ip_ssh_client_cli is missing else l_1_ip_ssh_client_cli))
                    yield '\n'
            l_1_ip_ssh_client_source_interface = l_1_ip_ssh_client_cli = missing
        if t_3((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces)):
            pass
            for l_1_ip_telnet_client_source_interface in t_1((undefined(name='ip_telnet_client_source_interfaces') if l_0_ip_telnet_client_source_interfaces is missing else l_0_ip_telnet_client_source_interfaces)):
                l_1_ip_telnet_client_cli = resolve('ip_telnet_client_cli')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_ip_telnet_client_source_interface, 'name')):
                    pass
                    l_1_ip_telnet_client_cli = str_join(('ip telnet client source-interface ', t_2(environment.getattr(l_1_ip_telnet_client_source_interface, 'name')), ))
                    _loop_vars['ip_telnet_client_cli'] = l_1_ip_telnet_client_cli
                    if t_3(environment.getattr(l_1_ip_telnet_client_source_interface, 'vrf')):
                        pass
                        l_1_ip_telnet_client_cli = str_join(((undefined(name='ip_telnet_client_cli') if l_1_ip_telnet_client_cli is missing else l_1_ip_telnet_client_cli), ' vrf ', environment.getattr(l_1_ip_telnet_client_source_interface, 'vrf'), ))
                        _loop_vars['ip_telnet_client_cli'] = l_1_ip_telnet_client_cli
                    yield str((undefined(name='ip_telnet_client_cli') if l_1_ip_telnet_client_cli is missing else l_1_ip_telnet_client_cli))
                    yield '\n'
            l_1_ip_telnet_client_source_interface = l_1_ip_telnet_client_cli = missing
        if t_3((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces)):
            pass
            for l_1_ip_tftp_client_source_interface in t_1((undefined(name='ip_tftp_client_source_interfaces') if l_0_ip_tftp_client_source_interfaces is missing else l_0_ip_tftp_client_source_interfaces)):
                l_1_ip_tftp_client_cli = resolve('ip_tftp_client_cli')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_ip_tftp_client_source_interface, 'name')):
                    pass
                    l_1_ip_tftp_client_cli = str_join(('ip tftp client source-interface ', t_2(environment.getattr(l_1_ip_tftp_client_source_interface, 'name')), ))
                    _loop_vars['ip_tftp_client_cli'] = l_1_ip_tftp_client_cli
                    if t_3(environment.getattr(l_1_ip_tftp_client_source_interface, 'vrf')):
                        pass
                        l_1_ip_tftp_client_cli = str_join(((undefined(name='ip_tftp_client_cli') if l_1_ip_tftp_client_cli is missing else l_1_ip_tftp_client_cli), ' vrf ', environment.getattr(l_1_ip_tftp_client_source_interface, 'vrf'), ))
                        _loop_vars['ip_tftp_client_cli'] = l_1_ip_tftp_client_cli
                    yield str((undefined(name='ip_tftp_client_cli') if l_1_ip_tftp_client_cli is missing else l_1_ip_tftp_client_cli))
                    yield '\n'
            l_1_ip_tftp_client_source_interface = l_1_ip_tftp_client_cli = missing

blocks = {}
debug_info = '7=34&13=37&14=39&15=43&16=45&17=47&18=49&20=51&24=54&25=58&26=60&27=62&28=64&29=66&31=68&34=71&35=73&36=77&37=79&38=81&39=83&41=85&45=88&46=90&47=94&48=96&49=98&50=100&52=102&56=105&57=107&58=111&59=113&60=115&61=117&63=119'