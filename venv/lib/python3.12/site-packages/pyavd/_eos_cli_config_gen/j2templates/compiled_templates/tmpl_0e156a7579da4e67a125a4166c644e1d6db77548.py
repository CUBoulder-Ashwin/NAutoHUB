from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/monitor-layer1.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_layer1 = resolve('monitor_layer1')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'enabled'), True):
        pass
        yield '\n## Monitor Layer 1 Logging\n\n| Layer 1 Event | Logging |\n| ------------- | ------- |\n'
        if t_1(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_mac_fault')):
            pass
            yield '| MAC fault | '
            yield str(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_mac_fault'))
            yield ' |\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'enabled')):
            pass
            yield '| Logging Transceiver | '
            yield str(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'enabled'))
            yield ' |\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'dom')):
            pass
            yield '| Transceiver DOM | '
            yield str(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'dom'))
            yield ' |\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'communication')):
            pass
            yield '| Transceiver communication | '
            yield str(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'communication'))
            yield ' |\n'
        yield '\n### Monitor Layer 1 Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/monitor-layer1.j2', 'documentation/monitor-layer1.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&13=21&14=24&16=26&17=29&19=31&20=34&22=36&23=39&29=42'