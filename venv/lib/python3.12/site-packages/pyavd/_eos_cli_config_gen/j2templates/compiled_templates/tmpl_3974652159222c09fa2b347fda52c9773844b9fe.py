from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mac-address-table-aging-time.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_address_table = resolve('mac_address_table')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'aging_time')):
        pass
        yield '!\nmac address-table aging-time '
        yield str(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'aging_time'))
        yield '\n'

blocks = {}
debug_info = '7=18&9=21'