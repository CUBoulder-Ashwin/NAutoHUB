from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/poe.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_poe = resolve('poe')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'reboot'), 'action'), 'maintain') or t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'interface_shutdown'), 'action'), 'power-off')):
        pass
        yield '!\npoe\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'reboot'), 'action'), 'maintain'):
            pass
            yield '   reboot action '
            yield str(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'reboot'), 'action'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'interface_shutdown'), 'action'), 'power-off'):
            pass
            yield '   interface shutdown action '
            yield str(environment.getattr(environment.getattr((undefined(name='poe') if l_0_poe is missing else l_0_poe), 'interface_shutdown'), 'action'))
            yield '\n'

blocks = {}
debug_info = '7=18&10=21&11=24&13=26&14=29'