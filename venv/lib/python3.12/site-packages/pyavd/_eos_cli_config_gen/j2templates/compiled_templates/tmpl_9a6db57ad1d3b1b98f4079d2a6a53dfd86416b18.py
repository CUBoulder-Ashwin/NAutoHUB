from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/sync-e.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_sync_e = resolve('sync_e')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='sync_e') if l_0_sync_e is missing else l_0_sync_e), 'network_option')):
        pass
        yield '!\nsync-e\n   network option '
        yield str(environment.getattr((undefined(name='sync_e') if l_0_sync_e is missing else l_0_sync_e), 'network_option'))
        yield '\n'

blocks = {}
debug_info = '7=18&10=21'