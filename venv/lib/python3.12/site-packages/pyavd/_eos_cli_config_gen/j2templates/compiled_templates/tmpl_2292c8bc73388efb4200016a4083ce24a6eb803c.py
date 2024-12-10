from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/switchport-default.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_switchport_default = resolve('switchport_default')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default)):
        pass
        yield '\n### Switchport Default\n\n#### Switchport Defaults Summary\n\n'
        if t_1(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'mode')):
            pass
            yield '- Default Switchport Mode: '
            yield str(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'mode'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'cos')):
            pass
            yield '- Default Switchport Phone COS: '
            yield str(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'cos'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'trunk')):
            pass
            yield '- Default Switchport Phone Trunk: '
            yield str(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'trunk'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'vlan')):
            pass
            yield '- Default Switchport Phone VLAN: '
            yield str(environment.getattr(environment.getattr((undefined(name='switchport_default') if l_0_switchport_default is missing else l_0_switchport_default), 'phone'), 'vlan'))
            yield '\n'
        yield '\n#### Switchport Default Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/switchport-default.j2', 'documentation/switchport-default.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&13=21&14=24&16=26&17=29&19=31&20=34&22=36&23=39&29=42'