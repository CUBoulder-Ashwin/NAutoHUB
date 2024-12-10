from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/sync-e.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_sync_e = resolve('sync_e')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='sync_e') if l_0_sync_e is missing else l_0_sync_e), 'network_option')):
        pass
        yield '\n### Synchronous Ethernet (SyncE) Settings\n\nSynchronous Ethernet Network Option: '
        yield str(environment.getattr((undefined(name='sync_e') if l_0_sync_e is missing else l_0_sync_e), 'network_option'))
        yield '\n\n#### Synchronous Ethernet Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/sync-e.j2', 'documentation/sync-e.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&11=21&16=23'