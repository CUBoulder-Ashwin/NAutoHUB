from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/hardware-speed-groups.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_hardware = resolve('hardware')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'speed_groups')):
        pass
        yield '!\n'
        for l_1_speed_group in environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'speed_groups'):
            _loop_vars = {}
            pass
            if t_1(environment.getattr(l_1_speed_group, 'serdes')):
                pass
                yield 'hardware speed-group '
                yield str(environment.getattr(l_1_speed_group, 'speed_group'))
                yield ' serdes '
                yield str(environment.getattr(l_1_speed_group, 'serdes'))
                yield '\n'
        l_1_speed_group = missing

blocks = {}
debug_info = '7=18&9=21&10=24&11=27'