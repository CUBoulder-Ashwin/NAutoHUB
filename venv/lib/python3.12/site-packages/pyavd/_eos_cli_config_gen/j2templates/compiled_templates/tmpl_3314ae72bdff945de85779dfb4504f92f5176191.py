from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/service-routing-configuration-bgp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_service_routing_configuration_bgp = resolve('service_routing_configuration_bgp')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='service_routing_configuration_bgp') if l_0_service_routing_configuration_bgp is missing else l_0_service_routing_configuration_bgp)):
        pass
        yield '\n### Service Routing Configuration BGP\n\n'
        if t_1(environment.getattr((undefined(name='service_routing_configuration_bgp') if l_0_service_routing_configuration_bgp is missing else l_0_service_routing_configuration_bgp), 'no_equals_default'), True):
            pass
            yield 'BGP no equals default enabled\n'
        elif t_1(environment.getattr((undefined(name='service_routing_configuration_bgp') if l_0_service_routing_configuration_bgp is missing else l_0_service_routing_configuration_bgp), 'no_equals_default'), False):
            pass
            yield 'BGP no equals default disabled\n'
        yield '\n```eos\n'
        template = environment.get_template('eos/service-routing-configuration-bgp.j2', 'documentation/service-routing-configuration-bgp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&11=21&13=24&18=28'