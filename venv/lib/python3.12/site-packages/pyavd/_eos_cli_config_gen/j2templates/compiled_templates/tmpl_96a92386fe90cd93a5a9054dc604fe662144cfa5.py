from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mcs-client.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mcs_client = resolve('mcs_client')
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
    if t_2((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client)):
        pass
        yield '!\nmcs client\n'
        if t_2(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_2(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'name')):
            pass
            yield '   !\n   cvx secondary '
            yield str(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'shutdown'), False):
                pass
                yield '      no shutdown\n'
            elif t_2(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'shutdown'), True):
                pass
                yield '      shutdown\n'
            for l_1_server_host in t_1(environment.getattr(environment.getattr((undefined(name='mcs_client') if l_0_mcs_client is missing else l_0_mcs_client), 'cvx_secondary'), 'server_hosts')):
                _loop_vars = {}
                pass
                yield '      server host '
                yield str(l_1_server_host)
                yield '\n'
            l_1_server_host = missing

blocks = {}
debug_info = '7=24&10=27&12=30&15=33&17=36&18=38&20=41&23=44&24=48'