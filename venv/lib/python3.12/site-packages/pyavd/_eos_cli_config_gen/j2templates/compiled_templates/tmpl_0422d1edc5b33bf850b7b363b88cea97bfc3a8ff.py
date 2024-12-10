from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/tacacs-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tacacs_servers = resolve('tacacs_servers')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers)):
        pass
        yield '!\n'
        if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'timeout')):
            pass
            yield 'tacacs-server timeout '
            yield str(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'timeout'))
            yield '\n'
        if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'policy_unknown_mandatory_attribute_ignore'), True):
            pass
            yield 'tacacs-server policy unknown-mandatory-attribute ignore\n'
        if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'hosts')):
            pass
            for l_1_host in environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'hosts'):
                l_1_host_cli = resolve('host_cli')
                l_1_hide_passwords = resolve('hide_passwords')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_host, 'host')):
                    pass
                    l_1_host_cli = str_join(('tacacs-server host ', environment.getattr(l_1_host, 'host'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                if t_3(environment.getattr(l_1_host, 'single_connection'), True):
                    pass
                    l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' single-connection', ))
                    _loop_vars['host_cli'] = l_1_host_cli
                if (t_3(environment.getattr(l_1_host, 'vrf')) and (environment.getattr(l_1_host, 'vrf') != 'default')):
                    pass
                    l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' vrf ', environment.getattr(l_1_host, 'vrf'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                if t_3(environment.getattr(l_1_host, 'timeout')):
                    pass
                    l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' timeout ', environment.getattr(l_1_host, 'timeout'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                if t_3(environment.getattr(l_1_host, 'key')):
                    pass
                    l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' key ', t_1(environment.getattr(l_1_host, 'key_type'), '7'), ' ', t_2(environment.getattr(l_1_host, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
                yield '\n'
            l_1_host = l_1_host_cli = l_1_hide_passwords = missing

blocks = {}
debug_info = '7=30&9=33&10=36&12=38&15=41&16=43&17=48&18=50&20=52&21=54&23=56&24=58&26=60&27=62&29=64&30=66&32=68'