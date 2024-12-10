from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-console.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_console = resolve('management_console')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='management_console') if l_0_management_console is missing else l_0_management_console)):
        pass
        yield '\n### Management Console\n'
        if t_1(environment.getattr((undefined(name='management_console') if l_0_management_console is missing else l_0_management_console), 'idle_timeout')):
            pass
            yield '\n#### Management Console Timeout\n\nManagement Console Timeout is set to **'
            yield str(environment.getattr((undefined(name='management_console') if l_0_management_console is missing else l_0_management_console), 'idle_timeout'))
            yield '** minutes.\n'
        yield '\n#### Management Console Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-console.j2', 'documentation/management-console.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&10=21&14=24&20=27'