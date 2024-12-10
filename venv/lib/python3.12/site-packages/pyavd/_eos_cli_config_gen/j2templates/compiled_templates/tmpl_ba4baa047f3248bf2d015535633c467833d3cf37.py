from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-igmp-snooping.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_igmp_snooping = resolve('ip_igmp_snooping')
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
    if t_2((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping)):
        pass
        if ((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping) != {'globally_enabled': True}):
            pass
            yield '!\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'globally_enabled'), False):
            pass
            yield 'no ip igmp snooping\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'robustness_variable')):
            pass
            yield 'ip igmp snooping robustness-variable '
            yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'robustness_variable'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'restart_query_interval')):
            pass
            yield 'ip igmp snooping restart query-interval '
            yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'restart_query_interval'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'interface_restart_query')):
            pass
            yield 'ip igmp snooping interface-restart-query '
            yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'interface_restart_query'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'fast_leave'), False):
            pass
            yield 'no ip igmp snooping fast-leave\n'
        elif t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'fast_leave'), True):
            pass
            yield 'ip igmp snooping fast-leave\n'
        for l_1_vlan in t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans'), 'id'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_vlan, 'enabled'), False):
                pass
                yield 'no ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield '\n'
            elif t_2(environment.getattr(l_1_vlan, 'enabled'), True):
                pass
                yield 'ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield '\n'
            if t_2(environment.getattr(l_1_vlan, 'querier')):
                pass
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'enabled'), True):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier\n'
                elif t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'enabled'), False):
                    pass
                    yield 'no ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'address')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier address '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'address'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'query_interval')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier query-interval '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'query_interval'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'max_response_time')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier max-response-time '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'max_response_time'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_interval')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier last-member-query-interval '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_interval'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_count')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier last-member-query-count '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_count'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_interval')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier startup-query-interval '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_interval'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_count')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier startup-query-count '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_count'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'version')):
                    pass
                    yield 'ip igmp snooping vlan '
                    yield str(environment.getattr(l_1_vlan, 'id'))
                    yield ' querier version '
                    yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'version'))
                    yield '\n'
            if t_2(environment.getattr(l_1_vlan, 'max_groups')):
                pass
                yield 'ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' max-groups '
                yield str(environment.getattr(l_1_vlan, 'max_groups'))
                yield '\n'
            if t_2(environment.getattr(l_1_vlan, 'fast_leave'), True):
                pass
                yield 'ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' fast-leave\n'
            elif t_2(environment.getattr(l_1_vlan, 'fast_leave'), False):
                pass
                yield 'no ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' fast-leave\n'
        l_1_vlan = missing
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'enabled'), True):
                pass
                yield 'ip igmp snooping querier\n'
            elif t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'enabled'), False):
                pass
                yield 'no ip igmp snooping querier\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'address')):
                pass
                yield 'ip igmp snooping querier address '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'address'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'query_interval')):
                pass
                yield 'ip igmp snooping querier query-interval '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'query_interval'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'max_response_time')):
                pass
                yield 'ip igmp snooping querier max-response-time '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'max_response_time'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_interval')):
                pass
                yield 'ip igmp snooping querier last-member-query-interval '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_interval'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_count')):
                pass
                yield 'ip igmp snooping querier last-member-query-count '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_count'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_interval')):
                pass
                yield 'ip igmp snooping querier startup-query-interval '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_interval'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_count')):
                pass
                yield 'ip igmp snooping querier startup-query-count '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_count'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'version')):
                pass
                yield 'ip igmp snooping querier version '
                yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'version'))
                yield '\n'
        if t_2(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'proxy'), True):
            pass
            yield '!\nip igmp snooping proxy\n'
        for l_1_vlan in t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans'), 'id'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_vlan, 'proxy'), True):
                pass
                yield 'ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' proxy\n'
            elif t_2(environment.getattr(l_1_vlan, 'proxy'), False):
                pass
                yield 'no ip igmp snooping vlan '
                yield str(environment.getattr(l_1_vlan, 'id'))
                yield ' proxy\n'
        l_1_vlan = missing

blocks = {}
debug_info = '7=24&8=26&12=29&15=32&16=35&18=37&19=40&21=42&22=45&24=47&26=50&29=53&30=56&31=59&32=61&33=64&35=66&36=68&37=71&38=73&39=76&41=78&42=81&44=85&45=88&47=92&48=95&50=99&51=102&53=106&54=109&56=113&57=116&59=120&60=123&62=127&63=130&66=134&67=137&69=141&70=144&71=146&72=149&75=152&76=154&78=157&81=160&82=163&84=165&85=168&87=170&88=173&90=175&91=178&93=180&94=183&96=185&97=188&99=190&100=193&102=195&103=198&106=200&110=203&111=206&112=209&113=211&114=214'