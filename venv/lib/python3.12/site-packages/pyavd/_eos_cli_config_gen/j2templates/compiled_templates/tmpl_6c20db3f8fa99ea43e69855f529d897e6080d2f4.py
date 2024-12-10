from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-defaults.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_defaults = resolve('management_defaults')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr(environment.getattr((undefined(name='management_defaults') if l_0_management_defaults is missing else l_0_management_defaults), 'secret'), 'hash')):
        pass
        yield '\n### Management defaults\n\nDefault secret hash is set to '
        yield str(environment.getattr(environment.getattr((undefined(name='management_defaults') if l_0_management_defaults is missing else l_0_management_defaults), 'secret'), 'hash'))
        yield '\n\n#### Management defaults Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-defaults.j2', 'documentation/management-defaults.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&11=21&16=23'