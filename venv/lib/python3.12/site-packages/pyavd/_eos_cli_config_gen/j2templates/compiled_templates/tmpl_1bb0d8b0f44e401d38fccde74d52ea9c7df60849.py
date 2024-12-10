from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/address-locking.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_address_locking = resolve('address_locking')
    l_0_address_locking_intfs = missing
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_address_locking_intfs = []
    context.vars['address_locking_intfs'] = l_0_address_locking_intfs
    context.exported_vars.add('address_locking_intfs')
    for l_1_ethernet_interface in t_2((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        _loop_vars = {}
        pass
        if (t_4(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv4'), True) or t_4(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv6'), True)):
            pass
            context.call(environment.getattr((undefined(name='address_locking_intfs') if l_0_address_locking_intfs is missing else l_0_address_locking_intfs), 'append'), l_1_ethernet_interface, _loop_vars=_loop_vars)
    l_1_ethernet_interface = missing
    if (t_4((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking)) or (t_3((undefined(name='address_locking_intfs') if l_0_address_locking_intfs is missing else l_0_address_locking_intfs)) > 0)):
        pass
        yield '\n## Address Locking\n'
        if t_4((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking)):
            pass
            yield '\n### Address Locking Summary\n\n| Setting | Value |\n| -------- | ----- |\n| Disable IP locking on configured ports | '
            yield str(t_1(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'disabled'), False))
            yield ' |\n'
            if t_4(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'local_interface')):
                pass
                yield '| Local Interface | '
                yield str(t_1(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'local_interface'), '-'))
                yield ' |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'expiration_mac_disabled'), True):
                pass
                yield '| Disable deauthorizing locked addresses upon MAC aging out | True |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'ipv4_enforcement_disabled'), True):
                pass
                yield '| Disable enforcement for locked ipv4 addresses | True |\n'
            if t_4(environment.getattr(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'locked_address'), 'ipv6_enforcement_disabled'), True):
                pass
                yield '| Disable enforcement for locked ipv6 addresses | True |\n'
            if t_4(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'dhcp_servers_ipv4')):
                pass
                yield '\n### DHCP Servers\n\n| Server IP |\n| --------- |\n'
                for l_1_ip in t_2(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'dhcp_servers_ipv4')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(l_1_ip)
                    yield ' |\n'
                l_1_ip = missing
            if t_4(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'leases')):
                pass
                yield '\n### Leases\n\n| Lease IP Address | Lease MAC Address |\n| ---------------- | ----------------- |\n'
                for l_1_lease in t_2(environment.getattr((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking), 'leases'), 'ip'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_lease, 'ip'))
                    yield ' | '
                    yield str(environment.getattr(l_1_lease, 'mac'))
                    yield ' |\n'
                l_1_lease = missing
        if (t_3((undefined(name='address_locking_intfs') if l_0_address_locking_intfs is missing else l_0_address_locking_intfs)) > 0):
            pass
            yield '\n## Address Locking Interfaces\n\n| Interface | IPv4 Address Locking | IPv6 Address Locking |\n| --------- | -------------------- | -------------------- |\n'
            for l_1_locking_intf in (undefined(name='address_locking_intfs') if l_0_address_locking_intfs is missing else l_0_address_locking_intfs):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_locking_intf, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_locking_intf, 'address_locking'), 'ipv4'), False))
                yield ' | '
                yield str(t_1(environment.getattr(environment.getattr(l_1_locking_intf, 'address_locking'), 'ipv6'), False))
                yield ' |\n'
            l_1_locking_intf = missing
        if t_4((undefined(name='address_locking') if l_0_address_locking is missing else l_0_address_locking)):
            pass
            yield '\n### Address Locking Device Configuration\n\n```eos\n'
            template = environment.get_template('eos/address-locking.j2', 'documentation/address-locking.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'address_locking_intfs': l_0_address_locking_intfs})):
                yield event
            yield '```\n'

blocks = {}
debug_info = '7=38&8=41&9=44&10=46&13=48&16=51&22=54&23=56&24=59&26=61&29=64&32=67&35=70&41=73&42=77&45=80&51=83&52=87&56=92&62=95&63=99&66=106&71=109'