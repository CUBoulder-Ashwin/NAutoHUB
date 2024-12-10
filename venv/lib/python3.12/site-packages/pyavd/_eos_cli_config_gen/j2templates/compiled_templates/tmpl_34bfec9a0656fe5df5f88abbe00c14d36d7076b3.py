from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-server-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_server_groups = resolve('aaa_server_groups')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups)):
        pass
        for l_1_aaa_server_group in (undefined(name='aaa_server_groups') if l_0_aaa_server_groups is missing else l_0_aaa_server_groups):
            _loop_vars = {}
            pass
            if (t_1(environment.getattr(l_1_aaa_server_group, 'type')) and t_1(environment.getattr(l_1_aaa_server_group, 'name'))):
                pass
                yield '!\naaa group server '
                yield str(environment.getattr(l_1_aaa_server_group, 'type'))
                yield ' '
                yield str(environment.getattr(l_1_aaa_server_group, 'name'))
                yield '\n'
                if t_1(environment.getattr(l_1_aaa_server_group, 'servers')):
                    pass
                    for l_2_server in environment.getattr(l_1_aaa_server_group, 'servers'):
                        l_2_server_cli = resolve('server_cli')
                        _loop_vars = {}
                        pass
                        if t_1(environment.getattr(l_2_server, 'server')):
                            pass
                            l_2_server_cli = str_join(('server ', environment.getattr(l_2_server, 'server'), ))
                            _loop_vars['server_cli'] = l_2_server_cli
                            if t_1(environment.getattr(l_2_server, 'vrf')):
                                pass
                                l_2_server_cli = str_join(((undefined(name='server_cli') if l_2_server_cli is missing else l_2_server_cli), ' vrf ', environment.getattr(l_2_server, 'vrf'), ))
                                _loop_vars['server_cli'] = l_2_server_cli
                            yield '   '
                            yield str((undefined(name='server_cli') if l_2_server_cli is missing else l_2_server_cli))
                            yield '\n'
                    l_2_server = l_2_server_cli = missing
        l_1_aaa_server_group = missing

blocks = {}
debug_info = '7=18&8=20&9=23&11=26&12=30&13=32&14=36&15=38&16=40&17=42&19=45'