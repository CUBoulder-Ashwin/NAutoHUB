from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/service-routing-configuration-bgp.j2'

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
    if t_1(environment.getattr((undefined(name='service_routing_configuration_bgp') if l_0_service_routing_configuration_bgp is missing else l_0_service_routing_configuration_bgp), 'no_equals_default'), True):
        pass
        yield '!\nservice routing configuration bgp no-equals-default\n'

blocks = {}
debug_info = '7=18'