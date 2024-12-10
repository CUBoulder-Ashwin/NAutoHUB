from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/platform-apply.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_platform = resolve('platform')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'mmu'), 'active_profile')):
        pass
        yield '!\nplatform trident mmu queue profile '
        yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='platform') if l_0_platform is missing else l_0_platform), 'trident'), 'mmu'), 'active_profile'))
        yield ' apply\n'

blocks = {}
debug_info = '7=18&9=21'