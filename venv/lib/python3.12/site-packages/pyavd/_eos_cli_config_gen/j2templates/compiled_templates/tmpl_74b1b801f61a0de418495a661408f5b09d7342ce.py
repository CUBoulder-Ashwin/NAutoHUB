from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-server-groups-tacacs-plus.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_server_groups = resolve('aaa_server_groups')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    for l_1_aaa_server_group in t_1(t_1((undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups), 'name'), 'type'):
        _loop_vars = {}
        pass
        if (environment.getattr(l_1_aaa_server_group, 'type') == 'tacacs+'):
            pass
            yield '!\naaa group server '
            yield str(environment.getattr(l_1_aaa_server_group, 'type'))
            yield ' '
            yield str(environment.getattr(l_1_aaa_server_group, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_aaa_server_group, 'servers')):
                pass
                for l_2_server in environment.getattr(l_1_aaa_server_group, 'servers'):
                    l_2_server_cli = resolve('server_cli')
                    _loop_vars = {}
                    pass
                    if t_2(environment.getattr(l_2_server, 'server')):
                        pass
                        l_2_server_cli = str_join(('server ', environment.getattr(l_2_server, 'server'), ))
                        _loop_vars['server_cli'] = l_2_server_cli
                        if t_2(environment.getattr(l_2_server, 'vrf')):
                            pass
                            l_2_server_cli = str_join(((undefined(name='server_cli') if l_2_server_cli is missing else l_2_server_cli), ' vrf ', environment.getattr(l_2_server, 'vrf'), ))
                            _loop_vars['server_cli'] = l_2_server_cli
                        yield '   '
                        yield str((undefined(name='server_cli') if l_2_server_cli is missing else l_2_server_cli))
                        yield '\n'
                l_2_server = l_2_server_cli = missing
    l_1_aaa_server_group = missing

blocks = {}
debug_info = '7=24&8=27&10=30&11=34&12=36&13=40&14=42&15=44&16=46&18=49'