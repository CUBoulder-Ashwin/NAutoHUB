from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/redundancy.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_redundancy = resolve('redundancy')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='redundancy') if l_0_redundancy is missing else l_0_redundancy)):
        pass
        yield '!\nredundancy\n'
        if t_1(environment.getattr((undefined(name='redundancy') if l_0_redundancy is missing else l_0_redundancy), 'protocol')):
            pass
            yield '   protocol '
            yield str(environment.getattr((undefined(name='redundancy') if l_0_redundancy is missing else l_0_redundancy), 'protocol'))
            yield '\n'

blocks = {}
debug_info = '7=18&10=21&11=24'