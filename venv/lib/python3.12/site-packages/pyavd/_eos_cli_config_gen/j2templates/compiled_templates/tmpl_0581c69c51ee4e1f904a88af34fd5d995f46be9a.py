from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/end.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_config_end = resolve('config_end')
    l_0_generate_default_config = resolve('generate_default_config')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1((undefined(name='config_end') if l_0_config_end is missing else l_0_config_end), True) or t_1((undefined(name='generate_default_config') if l_0_generate_default_config is missing else l_0_generate_default_config), True)):
        pass
        yield '!\nend\n'

blocks = {}
debug_info = '7=19'