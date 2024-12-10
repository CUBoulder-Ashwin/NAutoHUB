from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/logging-event-storm-control.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_logging = resolve('logging')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'event'), 'storm_control'), 'discards'), 'global'), True) or t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'event'), 'storm_control'), 'discards'), 'interval'))):
        pass
        yield '!\n'
    if t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'event'), 'storm_control'), 'discards'), 'global'), True):
        pass
        yield 'logging event storm-control discards global\n'
    if t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'event'), 'storm_control'), 'discards'), 'interval')):
        pass
        yield 'logging event storm-control discards interval '
        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'event'), 'storm_control'), 'discards'), 'interval'))
        yield '\n'

blocks = {}
debug_info = '7=18&10=21&13=24&14=27'