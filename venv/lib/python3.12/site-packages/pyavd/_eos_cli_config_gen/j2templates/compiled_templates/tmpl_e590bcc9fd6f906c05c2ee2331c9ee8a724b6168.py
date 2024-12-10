from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-cvx.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_cvx = resolve('management_cvx')
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
    if t_2((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx)):
        pass
        yield '!\nmanagement cvx\n'
        if t_2(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_2(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        for l_1_server_host in t_1(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'server_hosts')):
            _loop_vars = {}
            pass
            yield '   server host '
            yield str(l_1_server_host)
            yield '\n'
        l_1_server_host = missing
        if t_2(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'source_interface')):
            pass
            yield '   source-interface '
            yield str(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'source_interface'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx), 'vrf'))
            yield '\n'

blocks = {}
debug_info = '7=24&10=27&12=30&15=33&16=37&18=40&19=43&21=45&22=48'