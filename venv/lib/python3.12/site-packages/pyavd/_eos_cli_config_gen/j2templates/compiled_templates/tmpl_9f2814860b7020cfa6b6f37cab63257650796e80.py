from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/daemons.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_daemons = resolve('daemons')
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
    for l_1_daemon in t_1((undefined(name='daemons') if l_0_daemons is missing else l_0_daemons), 'name'):
        _loop_vars = {}
        pass
        yield '!\ndaemon '
        yield str(environment.getattr(l_1_daemon, 'name'))
        yield '\n'
        if t_2(environment.getattr(l_1_daemon, 'exec')):
            pass
            yield '   exec '
            yield str(environment.getattr(l_1_daemon, 'exec'))
            yield '\n'
        if t_2(environment.getattr(l_1_daemon, 'enabled'), False):
            pass
            yield '   shutdown\n'
        else:
            pass
            yield '   no shutdown\n'
    l_1_daemon = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33&13=35'