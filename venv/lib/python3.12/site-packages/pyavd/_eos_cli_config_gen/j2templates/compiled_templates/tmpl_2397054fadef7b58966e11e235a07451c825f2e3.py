from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/hostname.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_hostname = resolve('hostname')
    l_0_generate_default_config = resolve('generate_default_config')
    l_0_inventory_hostname = resolve('inventory_hostname')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_2((undefined(name='hostname') if l_0_hostname is missing else l_0_hostname)) or t_2((undefined(name='generate_default_config') if l_0_generate_default_config is missing else l_0_generate_default_config), True)):
        pass
        yield '!\nhostname '
        yield str(t_1((undefined(name='hostname') if l_0_hostname is missing else l_0_hostname), (undefined(name='inventory_hostname') if l_0_inventory_hostname is missing else l_0_inventory_hostname)))
        yield '\n'

blocks = {}
debug_info = '7=26&9=29'