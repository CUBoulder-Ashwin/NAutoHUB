from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/system-l1.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_system = resolve('system')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1')):
        pass
        yield '!\nsystem l1\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_speed_action')):
            pass
            yield '   unsupported speed action '
            yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_speed_action'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_error_correction_action')):
            pass
            yield '   unsupported error-correction action '
            yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_error_correction_action'))
            yield '\n'

blocks = {}
debug_info = '7=18&10=21&11=24&13=26&14=29'