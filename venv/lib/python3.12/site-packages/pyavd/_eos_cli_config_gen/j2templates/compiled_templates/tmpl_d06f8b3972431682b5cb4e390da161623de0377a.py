from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_authentication = resolve('aaa_authentication')
    l_0_aaa_authorization = resolve('aaa_authorization')
    l_0_aaa_accounting = resolve('aaa_accounting')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((t_1((undefined(name='aaa_authentication') if l_0_aaa_authentication is missing else l_0_aaa_authentication)) or t_1((undefined(name='aaa_authorization') if l_0_aaa_authorization is missing else l_0_aaa_authorization))) or t_1((undefined(name='aaa_accounting') if l_0_aaa_accounting is missing else l_0_aaa_accounting))):
        pass
        yield '!\n'
    template = environment.get_template('eos/aaa-authentication.j2', 'eos/aaa.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/aaa-authorization.j2', 'eos/aaa.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/aaa-accounting.j2', 'eos/aaa.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event

blocks = {}
debug_info = '7=20&11=23&13=26&15=29'