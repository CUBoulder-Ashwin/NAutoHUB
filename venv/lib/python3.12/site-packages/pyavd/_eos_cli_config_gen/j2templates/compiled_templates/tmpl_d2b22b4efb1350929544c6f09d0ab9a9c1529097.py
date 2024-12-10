from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/clock.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_clock = resolve('clock')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='clock') if l_0_clock is missing else l_0_clock)):
        pass
        yield '\n### Clock Settings\n'
        if t_1(environment.getattr((undefined(name='clock') if l_0_clock is missing else l_0_clock), 'timezone')):
            pass
            yield '\n#### Clock Timezone Settings\n\nClock Timezone is set to **'
            yield str(environment.getattr((undefined(name='clock') if l_0_clock is missing else l_0_clock), 'timezone'))
            yield '**.\n'
        yield '\n#### Clock Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/clock.j2', 'documentation/clock.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&10=21&14=24&20=27'