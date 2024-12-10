from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-layer1.j2'

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
        yield '!\nmonitor layer1\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'enabled'), True):
            pass
            yield '   logging transceiver\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'dom'), True):
            pass
            yield '   logging transceiver dom\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_transceiver'), 'communication'), True):
            pass
            yield '   logging transceiver communication\n'
        if t_1(environment.getattr((undefined(name='monitor_layer1') if l_0_monitor_layer1 is missing else l_0_monitor_layer1), 'logging_mac_fault'), True):
            pass
            yield '   logging mac fault\n'

blocks = {}
debug_info = '7=18&10=21&13=24&16=27&19=30'