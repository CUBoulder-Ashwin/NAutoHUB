from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/system-l1.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_system = resolve('system')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1')):
        pass
        yield '\n## System L1\n'
        if (t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_speed_action')) or t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_error_correction_action'))):
            pass
            yield '\n### Unsupported Interface Configurations\n\n| Unsupported Configuration | action |\n| ---------------- | -------|\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_speed_action')):
                pass
                yield '| Speed | '
                yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_speed_action'))
                yield ' |\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_error_correction_action')):
                pass
                yield '| Error correction | '
                yield str(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'l1'), 'unsupported_error_correction_action'))
                yield ' |\n'
        yield '\n### System L1 Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/system-l1.j2', 'documentation/system-l1.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&10=21&16=24&17=27&19=29&20=32&27=35'