from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/interface-defaults.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_defaults = resolve('interface_defaults')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults)):
        pass
        yield '\n### Interface Defaults\n\n#### Interface Defaults Summary\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'ethernet'), 'shutdown')):
            pass
            yield '\n- Default Ethernet Interface Shutdown: '
            yield str(environment.getattr(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'ethernet'), 'shutdown'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'mtu')):
            pass
            yield '\n- Default Routed Interface MTU: '
            yield str(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'mtu'))
            yield '\n'
        yield '\n#### Interface Defaults Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/interface-defaults.j2', 'documentation/interface-defaults.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&12=21&14=24&16=26&18=29&24=32'