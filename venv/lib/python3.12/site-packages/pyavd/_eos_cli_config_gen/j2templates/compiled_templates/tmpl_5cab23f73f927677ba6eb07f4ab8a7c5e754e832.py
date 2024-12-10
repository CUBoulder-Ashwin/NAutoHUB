from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/interfaces-ip-nat.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_namespace = resolve('namespace')
    l_0_ip_nat_interfaces = resolve('ip_nat_interfaces')
    l_0_ip_nat = missing
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
        t_3 = environment.filters['upper']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'upper' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_ip_nat = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), dst_dyn=[], src_dyn=[], dst_static=[], src_static=[], profile=[])
    context.vars['ip_nat'] = l_0_ip_nat
    context.exported_vars.add('ip_nat')
    for l_1__intf in t_2((undefined(name='ip_nat_interfaces') if l_0_ip_nat_interfaces is missing else l_0_ip_nat_interfaces), 'name'):
        _loop_vars = {}
        pass
        for l_2_dst_dyn in t_2(t_1(environment.getattr(environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'destination'), 'dynamic'), []), 'access_list'):
            _loop_vars = {}
            pass
            context.call(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_dyn'), 'append'), {'if_name': environment.getattr(l_1__intf, 'name'), 'acl': environment.getattr(l_2_dst_dyn, 'access_list'), 'pool': environment.getattr(l_2_dst_dyn, 'pool_name'), 'comment': t_1(environment.getattr(l_2_dst_dyn, 'comment'), '-'), 'priority': t_1(environment.getattr(l_2_dst_dyn, 'priority'), 0)}, _loop_vars=_loop_vars)
        l_2_dst_dyn = missing
        for l_2_src_dyn in t_2(t_1(environment.getattr(environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'source'), 'dynamic'), []), 'access_list'):
            l_2_pool = resolve('pool')
            l_2_valid = missing
            _loop_vars = {}
            pass
            l_2_valid = False
            _loop_vars['valid'] = l_2_valid
            if (environment.getattr(l_2_src_dyn, 'nat_type') == 'overload'):
                pass
                l_2_pool = '-'
                _loop_vars['pool'] = l_2_pool
                l_2_valid = True
                _loop_vars['valid'] = l_2_valid
            elif t_4(environment.getattr(l_2_src_dyn, 'pool_name')):
                pass
                l_2_pool = environment.getattr(l_2_src_dyn, 'pool_name')
                _loop_vars['pool'] = l_2_pool
                l_2_valid = True
                _loop_vars['valid'] = l_2_valid
            if (undefined(name='valid') if l_2_valid is missing else l_2_valid):
                pass
                context.call(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_dyn'), 'append'), {'if_name': environment.getattr(l_1__intf, 'name'), 'acl': environment.getattr(l_2_src_dyn, 'access_list'), 'type': environment.getattr(l_2_src_dyn, 'nat_type'), 'pool': (undefined(name='pool') if l_2_pool is missing else l_2_pool), 'comment': t_1(environment.getattr(l_2_src_dyn, 'comment'), '-'), 'priority': t_1(environment.getattr(l_2_src_dyn, 'priority'), 0)}, _loop_vars=_loop_vars)
        l_2_src_dyn = l_2_valid = l_2_pool = missing
        for l_2_dst_static in t_2(t_1(environment.getattr(environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'destination'), 'static'), []), 'original_ip'):
            _loop_vars = {}
            pass
            if ((not (t_4(environment.getattr(l_2_dst_static, 'access_list')) and t_4(environment.getattr(l_2_dst_static, 'group')))) and (not ((not t_4(environment.getattr(l_2_dst_static, 'original_port'))) and t_4(environment.getattr(l_2_dst_static, 'translated_port'))))):
                pass
                context.call(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_static'), 'append'), {'if_name': environment.getattr(l_1__intf, 'name'), 'direction': t_1(environment.getattr(l_2_dst_static, 'direction'), '-'), 'o_ip': environment.getattr(l_2_dst_static, 'original_ip'), 'o_port': t_1(environment.getattr(l_2_dst_static, 'original_port'), '-'), 'acl': t_1(environment.getattr(l_2_dst_static, 'access_list'), '-'), 't_ip': environment.getattr(l_2_dst_static, 'translated_ip'), 't_port': t_1(environment.getattr(l_2_dst_static, 'translated_port'), '-'), 'proto': t_1(environment.getattr(l_2_dst_static, 'protocol'), '-'), 'group': t_1(environment.getattr(l_2_dst_static, 'group'), '-'), 'priority': t_1(environment.getattr(l_2_dst_static, 'priority'), 0), 'comment': t_1(environment.getattr(l_2_dst_static, 'comment'), '-')}, _loop_vars=_loop_vars)
        l_2_dst_static = missing
        for l_2_src_static in t_2(t_1(environment.getattr(environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'source'), 'static'), []), 'original_ip'):
            _loop_vars = {}
            pass
            if ((not (t_4(environment.getattr(l_2_src_static, 'access_list')) and t_4(environment.getattr(l_2_src_static, 'group')))) and (not ((not t_4(environment.getattr(l_2_src_static, 'original_port'))) and t_4(environment.getattr(l_2_src_static, 'translated_port'))))):
                pass
                context.call(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_static'), 'append'), {'if_name': environment.getattr(l_1__intf, 'name'), 'direction': t_1(environment.getattr(l_2_src_static, 'direction'), '-'), 'o_ip': environment.getattr(l_2_src_static, 'original_ip'), 'o_port': t_1(environment.getattr(l_2_src_static, 'original_port'), '-'), 'acl': t_1(environment.getattr(l_2_src_static, 'access_list'), '-'), 't_ip': environment.getattr(l_2_src_static, 'translated_ip'), 't_port': t_1(environment.getattr(l_2_src_static, 'translated_port'), '-'), 'proto': t_3(t_1(environment.getattr(l_2_src_static, 'protocol'), '-')), 'group': t_1(environment.getattr(l_2_src_static, 'group'), '-'), 'priority': t_1(environment.getattr(l_2_src_static, 'priority'), 0), 'comment': t_1(environment.getattr(l_2_src_static, 'comment'), '-')}, _loop_vars=_loop_vars)
        l_2_src_static = missing
        if t_4(environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'service_profile')):
            pass
            context.call(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'profile'), 'append'), {'if_name': environment.getattr(l_1__intf, 'name'), 'profile': environment.getattr(environment.getattr(l_1__intf, 'ip_nat'), 'service_profile')}, _loop_vars=_loop_vars)
    l_1__intf = missing
    if environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_static'):
        pass
        yield '\n##### IP NAT: Source Static\n\n| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |\n| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |\n'
        for l_1_row in environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_static'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_row, 'if_name'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'direction'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'o_ip'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'o_port'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'acl'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 't_ip'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 't_port'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'proto'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'group'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'priority'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'comment'))
            yield ' |\n'
        l_1_row = missing
    if environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_dyn'):
        pass
        yield '\n##### IP NAT: Source Dynamic\n\n| Interface | Access List | NAT Type | Pool Name | Priority | Comment |\n| --------- | ----------- | -------- | --------- | -------- | ------- |\n'
        for l_1_row in environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'src_dyn'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_row, 'if_name'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'acl'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'type'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'pool'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'priority'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'comment'))
            yield ' |\n'
        l_1_row = missing
    if environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_static'):
        pass
        yield '\n##### IP NAT: Destination Static\n\n| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |\n| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |\n'
        for l_1_row in environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_static'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_row, 'if_name'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'direction'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'o_ip'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'o_port'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'acl'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 't_ip'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 't_port'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'proto'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'group'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'priority'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'comment'))
            yield ' |\n'
        l_1_row = missing
    if environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_dyn'):
        pass
        yield '\n##### IP NAT: Destination Dynamic\n\n| Interface | Access List | Pool Name | Priority | Comment |\n| --------- | ----------- | --------- | -------- | ------- |\n'
        for l_1_row in environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'dst_dyn'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_row, 'if_name'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'acl'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'pool'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'priority'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'comment'))
            yield ' |\n'
        l_1_row = missing
    if environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'profile'):
        pass
        yield '\n##### IP NAT: Interfaces configured via profile\n\n| Interface | Profile |\n| --------- |-------- |\n'
        for l_1_row in environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'profile'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_row, 'if_name'))
            yield ' | '
            yield str(environment.getattr(l_1_row, 'profile'))
            yield ' |\n'
        l_1_row = missing

blocks = {}
debug_info = '7=38&8=41&10=44&11=47&19=49&20=54&21=56&22=58&23=60&24=62&25=64&26=66&28=68&29=70&39=72&40=75&42=77&57=79&58=82&60=84&75=86&76=88&81=90&87=93&88=97&91=120&97=123&98=127&101=140&107=143&108=147&111=170&117=173&118=177&121=188&127=191&128=195'