from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/interface-defaults.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_defaults = resolve('interface_defaults')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults)):
        pass
        yield '!\ninterface defaults\n'
        if t_1(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'mtu'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'ethernet')):
            pass
            yield '   ethernet\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'ethernet'), 'shutdown'), True):
                pass
                yield '      shutdown\n'
            elif t_1(environment.getattr(environment.getattr((undefined(name='interface_defaults') if l_0_interface_defaults is missing else l_0_interface_defaults), 'ethernet'), 'shutdown'), False):
                pass
                yield '      no shutdown\n'

blocks = {}
debug_info = '7=18&10=21&11=24&13=26&15=29&17=32'