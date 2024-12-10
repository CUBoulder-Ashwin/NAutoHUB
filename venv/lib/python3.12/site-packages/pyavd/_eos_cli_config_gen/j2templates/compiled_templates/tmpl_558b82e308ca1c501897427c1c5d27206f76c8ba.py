from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/service-routing-protocols-model.j2'

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
        yield '!\nservice routing protocols model '
        yield str((undefined(name='service_routing_protocols_model') if l_0_service_routing_protocols_model is missing else l_0_service_routing_protocols_model))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'