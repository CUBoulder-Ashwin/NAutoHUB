from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/lacp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_lacp = resolve('lacp')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp)):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'system_priority')):
            pass
            yield 'lacp system-priority '
            yield str(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'system_priority'))
            yield '\n'
        if (t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'begin')) and t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'end'))):
            pass
            yield 'lacp port-id range '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'begin'))
            yield ' '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'port_id'), 'range'), 'end'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'rate_limit'), 'default'), True):
            pass
            yield 'lacp rate-limit default\n'
        elif t_1(environment.getattr(environment.getattr((undefined(name='lacp') if l_0_lacp is missing else l_0_lacp), 'rate_limit'), 'default'), False):
            pass
            yield 'no lacp rate-limit default\n'

blocks = {}
debug_info = '7=18&9=21&10=24&12=26&13=29&15=33&17=36'