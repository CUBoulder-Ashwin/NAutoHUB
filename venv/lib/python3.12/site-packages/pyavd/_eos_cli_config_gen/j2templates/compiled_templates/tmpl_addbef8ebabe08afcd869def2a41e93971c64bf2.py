from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/service-unsupported-transceiver.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_service_unsupported_transceiver = resolve('service_unsupported_transceiver')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1(environment.getattr((undefined(name='service_unsupported_transceiver') if l_0_service_unsupported_transceiver is missing else l_0_service_unsupported_transceiver), 'license_name')) and t_1(environment.getattr((undefined(name='service_unsupported_transceiver') if l_0_service_unsupported_transceiver is missing else l_0_service_unsupported_transceiver), 'license_key'))):
        pass
        yield '!\nservice unsupported-transceiver '
        yield str(environment.getattr((undefined(name='service_unsupported_transceiver') if l_0_service_unsupported_transceiver is missing else l_0_service_unsupported_transceiver), 'license_name'))
        yield ' '
        yield str(environment.getattr((undefined(name='service_unsupported_transceiver') if l_0_service_unsupported_transceiver is missing else l_0_service_unsupported_transceiver), 'license_key'))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'