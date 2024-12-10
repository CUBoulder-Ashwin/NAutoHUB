from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-nat-part1.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_nat = resolve('ip_nat')
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
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat)):
        pass
        yield '!\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'address_selection'), 'hash_field_source_ip'), False):
            pass
            yield 'ip nat translation address selection hash field source-ip\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'address_selection'), 'any'), False):
            pass
            yield 'ip nat translation address selection any\n'
        for l_1_timeout in t_2(t_1(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'timeouts'), [])):
            _loop_vars = {}
            pass
            yield 'ip nat translation '
            yield str(environment.getattr(l_1_timeout, 'protocol'))
            yield '-timeout '
            yield str(environment.getattr(l_1_timeout, 'timeout'))
            yield '\n'
        l_1_timeout = missing
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'max_entries'), 'limit')):
            pass
            yield 'ip nat translation max-entries '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'max_entries'), 'limit'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'low_mark'), 'percentage')):
            pass
            yield 'ip nat translation low-mark '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'low_mark'), 'percentage'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'max_entries'), 'host_limit')):
            pass
            yield 'ip nat translation max-entries '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'max_entries'), 'host_limit'))
            yield ' host\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'low_mark'), 'host_percentage')):
            pass
            yield 'ip nat translation low-mark '
            yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'low_mark'), 'host_percentage'))
            yield ' host\n'
        for l_1_ip_limit in t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'translation'), 'max_entries'), 'ip_limits'), []):
            _loop_vars = {}
            pass
            yield 'ip nat translation max-entries '
            yield str(environment.getattr(l_1_ip_limit, 'limit'))
            yield ' '
            yield str(environment.getattr(l_1_ip_limit, 'ip'))
            yield '\n'
        l_1_ip_limit = missing
        if t_3(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'kernel_buffer_size')):
            pass
            yield 'ip nat kernel buffer size '
            yield str(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'kernel_buffer_size'))
            yield '\n'
        for l_1_profile in t_2(environment.getattr((undefined(name='ip_nat') if l_0_ip_nat is missing else l_0_ip_nat), 'profiles'), 'name'):
            l_1_nat_profile_def = l_1_interface_ip_nat = missing
            _loop_vars = {}
            pass
            yield '!\n'
            l_1_nat_profile_def = str_join(('ip nat profile ', environment.getattr(l_1_profile, 'name'), ))
            _loop_vars['nat_profile_def'] = l_1_nat_profile_def
            if t_3(environment.getattr(l_1_profile, 'vrf')):
                pass
                l_1_nat_profile_def = str_join(((undefined(name='nat_profile_def') if l_1_nat_profile_def is missing else l_1_nat_profile_def), ' vrf ', environment.getattr(l_1_profile, 'vrf'), ))
                _loop_vars['nat_profile_def'] = l_1_nat_profile_def
            yield str((undefined(name='nat_profile_def') if l_1_nat_profile_def is missing else l_1_nat_profile_def))
            yield '\n'
            l_1_interface_ip_nat = l_1_profile
            _loop_vars['interface_ip_nat'] = l_1_interface_ip_nat
            template = environment.get_template('eos/interface-ip-nat.j2', 'eos/ip-nat-part1.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'interface_ip_nat': l_1_interface_ip_nat, 'nat_profile_def': l_1_nat_profile_def, 'profile': l_1_profile})):
                yield event
        l_1_profile = l_1_nat_profile_def = l_1_interface_ip_nat = missing

blocks = {}
debug_info = '7=30&9=33&12=36&15=39&16=43&18=48&19=51&21=53&22=56&24=58&25=61&27=63&28=66&30=68&31=72&33=77&34=80&36=82&38=87&39=89&40=91&42=93&43=95&44=97'