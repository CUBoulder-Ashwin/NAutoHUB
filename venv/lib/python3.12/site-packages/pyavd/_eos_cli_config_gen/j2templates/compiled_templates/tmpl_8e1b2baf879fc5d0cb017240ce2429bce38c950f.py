from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-access-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_access_lists = resolve('ip_access_lists')
    l_0_namespace = resolve('namespace')
    l_0_counter = resolve('counter')
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
        t_3 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_4 = environment.filters['mandatory']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'mandatory' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='ip_access_lists') if l_0_ip_access_lists is missing else l_0_ip_access_lists)):
        pass
        l_0_counter = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['counter'] = l_0_counter
        context.exported_vars.add('counter')
        if not isinstance(l_0_counter, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_counter['acle_number'] = 0
        for l_1_acl in t_2((undefined(name='ip_access_lists') if l_0_ip_access_lists is missing else l_0_ip_access_lists), 'name'):
            _loop_vars = {}
            pass
            if ((not t_5(environment.getattr(l_1_acl, 'name'))) or (not t_5(environment.getattr(l_1_acl, 'entries')))):
                pass
                continue
            yield '!\nip access-list '
            yield str(environment.getattr(l_1_acl, 'name'))
            yield '\n'
            if t_5(environment.getattr(l_1_acl, 'counters_per_entry'), True):
                pass
                yield '   counters per-entry\n'
            for l_2_acle in environment.getattr(l_1_acl, 'entries'):
                l_2_ip_access_lists_max_entries = resolve('ip_access_lists_max_entries')
                l_2_a_non_existing_var = resolve('a_non_existing_var')
                l_2_acl_entry = missing
                _loop_vars = {}
                pass
                l_2_acl_entry = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), string='', _loop_vars=_loop_vars)
                _loop_vars['acl_entry'] = l_2_acl_entry
                if t_5(environment.getattr(l_2_acle, 'remark')):
                    pass
                    if not isinstance(l_2_acl_entry, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), 'remark ', environment.getattr(l_2_acle, 'remark'), ))
                elif (((t_5(environment.getattr(l_2_acle, 'action')) and t_5(environment.getattr(l_2_acle, 'protocol'))) and t_5(environment.getattr(l_2_acle, 'source'))) and t_5(environment.getattr(l_2_acle, 'destination'))):
                    pass
                    if not isinstance(l_2_acl_entry, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), environment.getattr(l_2_acle, 'action'), ))
                    if (t_5(environment.getattr(l_2_acle, 'vlan_number')) and t_5(environment.getattr(l_2_acle, 'vlan_mask'))):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' vlan', ))
                        if t_5(environment.getattr(l_2_acle, 'vlan_inner'), True):
                            pass
                            if not isinstance(l_2_acl_entry, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' inner', ))
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'vlan_number'), ' ', environment.getattr(l_2_acle, 'vlan_mask'), ))
                    if not isinstance(l_2_acl_entry, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'protocol'), ))
                    if (('/' not in environment.getattr(l_2_acle, 'source')) and (environment.getattr(l_2_acle, 'source') != 'any')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' host', ))
                    if not isinstance(l_2_acl_entry, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'source'), ))
                    if (t_3(environment.getattr(l_2_acle, 'protocol')) in ['tcp', 'udp']):
                        pass
                        if t_5(environment.getattr(l_2_acle, 'source_ports')):
                            pass
                            if not isinstance(l_2_acl_entry, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', t_1(environment.getattr(l_2_acle, 'source_ports_match'), 'eq'), ))
                            for l_3_a_port in environment.getattr(l_2_acle, 'source_ports'):
                                _loop_vars = {}
                                pass
                                if not isinstance(l_2_acl_entry, Namespace):
                                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                                l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', l_3_a_port, ))
                            l_3_a_port = missing
                    if (('/' not in environment.getattr(l_2_acle, 'destination')) and (environment.getattr(l_2_acle, 'destination') != 'any')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' host', ))
                    if not isinstance(l_2_acl_entry, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'destination'), ))
                    if (t_3(environment.getattr(l_2_acle, 'protocol')) in ['tcp', 'udp']):
                        pass
                        if t_5(environment.getattr(l_2_acle, 'destination_ports')):
                            pass
                            if not isinstance(l_2_acl_entry, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', t_1(environment.getattr(l_2_acle, 'destination_ports_match'), 'eq'), ))
                            for l_3_a_port in environment.getattr(l_2_acle, 'destination_ports'):
                                _loop_vars = {}
                                pass
                                if not isinstance(l_2_acl_entry, Namespace):
                                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                                l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', l_3_a_port, ))
                            l_3_a_port = missing
                    if (t_3(environment.getattr(l_2_acle, 'protocol')) == 'tcp'):
                        pass
                        if t_5(environment.getattr(l_2_acle, 'tcp_flags')):
                            pass
                            for l_3_a_flag in environment.getattr(l_2_acle, 'tcp_flags'):
                                _loop_vars = {}
                                pass
                                if not isinstance(l_2_acl_entry, Namespace):
                                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                                l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', l_3_a_flag, ))
                            l_3_a_flag = missing
                    if (t_3(environment.getattr(l_2_acle, 'protocol')) == 'icmp'):
                        pass
                        if t_5(environment.getattr(l_2_acle, 'icmp_type')):
                            pass
                            if not isinstance(l_2_acl_entry, Namespace):
                                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                            l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'icmp_type'), ))
                            if t_5(environment.getattr(l_2_acle, 'icmp_code')):
                                pass
                                if not isinstance(l_2_acl_entry, Namespace):
                                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                                l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'icmp_code'), ))
                    if t_5(environment.getattr(l_2_acle, 'nexthop_group')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' nexthop-group ', environment.getattr(l_2_acle, 'nexthop_group'), ))
                    if t_5(environment.getattr(l_2_acle, 'fragments'), True):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' fragments', ))
                    if t_5(environment.getattr(l_2_acle, 'tracked'), True):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' tracked', ))
                    if t_5(environment.getattr(l_2_acle, 'ttl')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ttl ', t_1(environment.getattr(l_2_acle, 'ttl_match'), 'eq'), ))
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' ', environment.getattr(l_2_acle, 'ttl'), ))
                    if t_5(environment.getattr(l_2_acle, 'dscp')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' dscp ', t_3(environment.getattr(l_2_acle, 'dscp')), ))
                    if t_5(environment.getattr(l_2_acle, 'log'), True):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ' log', ))
                    if t_5((undefined(name='ip_access_lists_max_entries') if l_2_ip_access_lists_max_entries is missing else l_2_ip_access_lists_max_entries)):
                        pass
                        if not isinstance(l_0_counter, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_0_counter['acle_number'] = (environment.getattr((undefined(name='counter') if l_0_counter is missing else l_0_counter), 'acle_number') + 1)
                        if (environment.getattr((undefined(name='counter') if l_0_counter is missing else l_0_counter), 'acle_number') > (undefined(name='ip_access_lists_max_entries') if l_2_ip_access_lists_max_entries is missing else l_2_ip_access_lists_max_entries)):
                            pass
                            yield '   '
                            yield str(t_4((undefined(name='a_non_existing_var') if l_2_a_non_existing_var is missing else l_2_a_non_existing_var), 'The number of ACL entries is above defined maximum!'))
                            yield '\n'
                if (environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string') != ''):
                    pass
                    if t_5(environment.getattr(l_2_acle, 'sequence')):
                        pass
                        if not isinstance(l_2_acl_entry, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_2_acl_entry['string'] = str_join((environment.getattr(l_2_acle, 'sequence'), ' ', environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'), ))
                    yield '   '
                    yield str(environment.getattr((undefined(name='acl_entry') if l_2_acl_entry is missing else l_2_acl_entry), 'string'))
                    yield '\n'
            l_2_acle = l_2_acl_entry = l_2_ip_access_lists_max_entries = l_2_a_non_existing_var = missing
            if t_5(environment.getattr(l_1_acl, 'permit_response_traffic')):
                pass
                yield '   permit response traffic '
                yield str(environment.getattr(l_1_acl, 'permit_response_traffic'))
                yield '\n'
        l_1_acl = missing

blocks = {}
debug_info = '7=44&9=46&10=49&12=52&13=55&16=57&19=59&20=61&24=64&27=70&30=72&31=74&34=77&39=79&41=82&42=84&43=87&44=89&46=92&49=95&51=98&52=100&54=103&56=106&57=108&58=110&59=113&60=116&65=120&66=122&68=125&70=128&71=130&72=132&73=135&74=138&79=142&80=144&81=146&82=149&87=153&88=155&89=157&90=160&91=162&96=165&97=167&100=170&101=172&104=175&105=177&108=180&109=182&110=185&113=188&114=190&117=193&118=195&121=198&122=200&123=203&125=206&130=208&132=210&133=212&135=216&139=219&140=222'