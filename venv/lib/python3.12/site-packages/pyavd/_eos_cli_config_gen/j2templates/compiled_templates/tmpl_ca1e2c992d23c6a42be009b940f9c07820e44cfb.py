from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/address-locking.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_address_locking = resolve('address_locking')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking)):
        pass
        yield '!\naddress locking\n'
        if t_2(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'disabled'), True):
            pass
            yield '   disabled\n'
        if t_2(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'local_interface')):
            pass
            yield '   local-interface '
            yield str(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'local_interface'))
            yield '\n'
        for l_1_ip in t_1(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'dhcp_servers_ipv4')):
            _loop_vars = {}
            pass
            yield '   dhcp server ipv4 '
            yield str(l_1_ip)
            yield '\n'
        l_1_ip = missing
        for l_1_lease in t_1(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'leases'), 'ip'):
            _loop_vars = {}
            pass
            yield '   lease '
            yield str(environment.getattr(l_1_lease, 'ip'))
            yield ' mac '
            yield str(environment.getattr(l_1_lease, 'mac'))
            yield '\n'
        l_1_lease = missing
        if t_2(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'expiration_mac_disabled'), True):
            pass
            yield '   locked-address expiration mac disabled\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'ipv4_enforcement_disabled'), True):
            pass
            yield '   locked-address ipv4 enforcement disabled\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'ipv6_enforcement_disabled'), True):
            pass
            yield '   locked-address ipv6 enforcement disabled\n'

blocks = {}
debug_info = '7=24&10=27&13=30&14=33&16=35&17=39&19=42&20=46&22=51&25=54&28=57'