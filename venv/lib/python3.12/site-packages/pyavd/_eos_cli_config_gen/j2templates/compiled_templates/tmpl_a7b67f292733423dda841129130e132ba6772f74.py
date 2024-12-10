from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mac-address-table-notification.j2'

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
    if t_1(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap')):
        pass
        yield '!\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'logging'), False):
            pass
            yield 'no mac address-table notification host-flap logging\n'
        elif t_1(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'logging'), True):
            pass
            yield 'mac address-table notification host-flap logging\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'window')):
            pass
            yield 'mac address-table notification host-flap detection window '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'window'))
            yield '\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'moves')):
            pass
            yield 'mac address-table notification host-flap detection moves '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='mac_address_table') if l_0_mac_address_table is missing else l_0_mac_address_table), 'notification_host_flap'), 'detection'), 'moves'))
            yield '\n'

blocks = {}
debug_info = '7=18&9=21&11=24&14=27&15=30&17=32&18=35'