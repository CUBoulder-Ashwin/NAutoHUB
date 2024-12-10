from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/radius-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_radius_servers = resolve('radius_servers')
    try:
        t_1 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='radius_servers') if l_0_radius_servers is missing else l_0_radius_servers)):
        pass
        yield '!\n'
        for l_1_radius_server in (undefined(name='radius_servers') if l_0_radius_servers is missing else l_0_radius_servers):
            l_1_radius_cli = resolve('radius_cli')
            l_1_hide_passwords = resolve('hide_passwords')
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_radius_server, 'host')):
                pass
                l_1_radius_cli = str_join(('radius-server host ', environment.getattr(l_1_radius_server, 'host'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if (t_2(environment.getattr(l_1_radius_server, 'vrf')) and (environment.getattr(l_1_radius_server, 'vrf') != 'default')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' vrf ', environment.getattr(l_1_radius_server, 'vrf'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_2(environment.getattr(l_1_radius_server, 'key')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' key 7 ', t_1(environment.getattr(l_1_radius_server, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            yield str((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli))
            yield '\n'
        l_1_radius_server = l_1_radius_cli = l_1_hide_passwords = missing

blocks = {}
debug_info = '7=24&9=27&10=32&11=34&13=36&14=38&16=40&17=42&19=44'