from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vmtracer-sessions.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vmtracer_sessions = resolve('vmtracer_sessions')
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
    for l_1_session in t_1((undefined(name='vmtracer_sessions') if l_0_vmtracer_sessions is missing else l_0_vmtracer_sessions), 'name'):
        _loop_vars = {}
        pass
        yield '!\nvmtracer session '
        yield str(environment.getattr(l_1_session, 'name'))
        yield '\n'
        if t_2(environment.getattr(l_1_session, 'url')):
            pass
            yield '   url '
            yield str(environment.getattr(l_1_session, 'url'))
            yield '\n'
        if t_2(environment.getattr(l_1_session, 'username')):
            pass
            yield '   username '
            yield str(environment.getattr(l_1_session, 'username'))
            yield '\n'
        if t_2(environment.getattr(l_1_session, 'password')):
            pass
            yield '   password 7 '
            yield str(environment.getattr(l_1_session, 'password'))
            yield '\n'
        if t_2(environment.getattr(l_1_session, 'autovlan_disable'), True):
            pass
            yield '   autovlan disable\n'
        if t_2(environment.getattr(l_1_session, 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_session, 'vrf'))
            yield '\n'
        if t_2(environment.getattr(l_1_session, 'source_interface')):
            pass
            yield '   source-interface '
            yield str(environment.getattr(l_1_session, 'source_interface'))
            yield '\n'
    l_1_session = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33&13=35&14=38&16=40&17=43&19=45&22=48&23=51&25=53&26=56'