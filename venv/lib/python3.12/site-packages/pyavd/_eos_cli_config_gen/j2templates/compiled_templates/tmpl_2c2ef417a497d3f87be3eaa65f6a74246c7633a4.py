from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/service-routing-protocols-model.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_service_routing_protocols_model = resolve('service_routing_protocols_model')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='service_routing_protocols_model') if l_0_service_routing_protocols_model is missing else l_0_service_routing_protocols_model)):
        pass
        yield '\n### Service Routing Protocols Model\n\n'
        if t_1((undefined(name='service_routing_protocols_model') if l_0_service_routing_protocols_model is missing else l_0_service_routing_protocols_model), 'multi-agent'):
            pass
            yield 'Multi agent routing protocol model enabled\n'
        elif t_1((undefined(name='service_routing_protocols_model') if l_0_service_routing_protocols_model is missing else l_0_service_routing_protocols_model), 'ribd'):
            pass
            yield 'Single agent routing protocol model enabled\n'
        yield '\n```eos\n'
        template = environment.get_template('eos/service-routing-protocols-model.j2', 'documentation/service-routing-protocols-model.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&11=21&13=24&18=28'