from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/eos-cli.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_eos_cli = resolve('eos_cli')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='eos_cli') if l_0_eos_cli is missing else l_0_eos_cli)):
        pass
        yield '!\n'
        yield str((undefined(name='eos_cli') if l_0_eos_cli is missing else l_0_eos_cli))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'