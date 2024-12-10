from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/interface-ip-nat.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_ip_nat = resolve('interface_ip_nat')
    l_0_unsorted_nat_entries = missing
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_unsorted_nat_entries = []
    context.vars['unsorted_nat_entries'] = l_0_unsorted_nat_entries
    context.exported_vars.add('unsorted_nat_entries')
    for l_1_nat in t_1(environment.getattr(environment.getattr((undefined(name='interface_ip_nat') if l_0_interface_ip_nat is missing else l_0_interface_ip_nat), 'source'), 'static'), []):
        l_1_nat_cli = resolve('nat_cli')
        l_1_sort_key = resolve('sort_key')
        _loop_vars = {}
        pass
        if ((not (t_4(environment.getattr(l_1_nat, 'access_list')) and t_4(environment.getattr(l_1_nat, 'group')))) and (not ((not t_4(environment.getattr(l_1_nat, 'original_port'))) and t_4(environment.getattr(l_1_nat, 'translated_port'))))):
            pass
            l_1_nat_cli = 'ip nat source'
            _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_sort_key = str_join(('a_', environment.getattr(l_1_nat, 'original_ip'), ))
            _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'direction')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'direction'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' static ', environment.getattr(l_1_nat, 'original_ip'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'original_port')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'original_port'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
                l_1_sort_key = str_join(((undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), '_', environment.getattr(l_1_nat, 'original_port'), ))
                _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'access_list')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' access-list ', environment.getattr(l_1_nat, 'access_list'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'translated_ip'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'translated_port')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'translated_port'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'protocol')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' protocol ', environment.getattr(l_1_nat, 'protocol'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'group')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' group ', environment.getattr(l_1_nat, 'group'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
                l_1_sort_key = str_join(('c_', environment.getattr(l_1_nat, 'group'), ))
                _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'comment')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' comment ', environment.getattr(l_1_nat, 'comment'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            context.call(environment.getattr((undefined(name='unsorted_nat_entries') if l_0_unsorted_nat_entries is missing else l_0_unsorted_nat_entries), 'append'), {'sort_key': (undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), 'cli': (undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli)}, _loop_vars=_loop_vars)
    l_1_nat = l_1_nat_cli = l_1_sort_key = missing
    for l_1_nat in t_1(environment.getattr(environment.getattr((undefined(name='interface_ip_nat') if l_0_interface_ip_nat is missing else l_0_interface_ip_nat), 'destination'), 'static'), []):
        l_1_nat_cli = resolve('nat_cli')
        l_1_sort_key = resolve('sort_key')
        _loop_vars = {}
        pass
        if ((not (t_4(environment.getattr(l_1_nat, 'access_list')) and t_4(environment.getattr(l_1_nat, 'group')))) and (not ((not t_4(environment.getattr(l_1_nat, 'original_port'))) and t_4(environment.getattr(l_1_nat, 'translated_port'))))):
            pass
            l_1_nat_cli = 'ip nat destination'
            _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_sort_key = str_join(('a_', environment.getattr(l_1_nat, 'original_ip'), ))
            _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'direction')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'direction'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' static ', environment.getattr(l_1_nat, 'original_ip'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'original_port')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'original_port'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
                l_1_sort_key = str_join(((undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), '_', environment.getattr(l_1_nat, 'original_port'), ))
                _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'access_list')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' access-list ', environment.getattr(l_1_nat, 'access_list'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'translated_ip'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'translated_port')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' ', environment.getattr(l_1_nat, 'translated_port'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'protocol')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' protocol ', environment.getattr(l_1_nat, 'protocol'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'group')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' group ', environment.getattr(l_1_nat, 'group'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
                l_1_sort_key = str_join(('c_', environment.getattr(l_1_nat, 'group'), ))
                _loop_vars['sort_key'] = l_1_sort_key
            if t_4(environment.getattr(l_1_nat, 'comment')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' comment ', environment.getattr(l_1_nat, 'comment'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            context.call(environment.getattr((undefined(name='unsorted_nat_entries') if l_0_unsorted_nat_entries is missing else l_0_unsorted_nat_entries), 'append'), {'sort_key': (undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), 'cli': (undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli)}, _loop_vars=_loop_vars)
    l_1_nat = l_1_nat_cli = l_1_sort_key = missing
    for l_1_nat in t_1(environment.getattr(environment.getattr((undefined(name='interface_ip_nat') if l_0_interface_ip_nat is missing else l_0_interface_ip_nat), 'source'), 'dynamic'), []):
        l_1_valid = l_1_nat_cli = l_1_sort_key = missing
        _loop_vars = {}
        pass
        l_1_valid = False
        _loop_vars['valid'] = l_1_valid
        l_1_nat_cli = str_join(('ip nat source dynamic access-list ', environment.getattr(l_1_nat, 'access_list'), ))
        _loop_vars['nat_cli'] = l_1_nat_cli
        l_1_sort_key = str_join(('d_', t_3(context.eval_ctx, environment.getattr(l_1_nat, 'access_list'), '.'), ))
        _loop_vars['sort_key'] = l_1_sort_key
        if (environment.getattr(l_1_nat, 'nat_type') == 'overload'):
            pass
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' overload', ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_valid = True
            _loop_vars['valid'] = l_1_valid
        elif t_4(environment.getattr(l_1_nat, 'pool_name')):
            pass
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' pool ', environment.getattr(l_1_nat, 'pool_name'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
            l_1_valid = True
            _loop_vars['valid'] = l_1_valid
            if (environment.getattr(l_1_nat, 'nat_type') == 'pool-address-only'):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' address-only', ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            elif (environment.getattr(l_1_nat, 'nat_type') == 'pool-full-cone'):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' full-cone', ))
                _loop_vars['nat_cli'] = l_1_nat_cli
        if (undefined(name='valid') if l_1_valid is missing else l_1_valid):
            pass
            if (t_1(environment.getattr(l_1_nat, 'priority'), 0) > 0):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' priority ', environment.getattr(l_1_nat, 'priority'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            if t_4(environment.getattr(l_1_nat, 'comment')):
                pass
                l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' comment ', environment.getattr(l_1_nat, 'comment'), ))
                _loop_vars['nat_cli'] = l_1_nat_cli
            context.call(environment.getattr((undefined(name='unsorted_nat_entries') if l_0_unsorted_nat_entries is missing else l_0_unsorted_nat_entries), 'append'), {'sort_key': (undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), 'cli': (undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli)}, _loop_vars=_loop_vars)
    l_1_nat = l_1_valid = l_1_nat_cli = l_1_sort_key = missing
    for l_1_nat in t_1(environment.getattr(environment.getattr((undefined(name='interface_ip_nat') if l_0_interface_ip_nat is missing else l_0_interface_ip_nat), 'destination'), 'dynamic'), []):
        l_1_nat_cli = l_1_sort_key = missing
        _loop_vars = {}
        pass
        l_1_nat_cli = str_join(('ip nat destination dynamic access-list ', environment.getattr(l_1_nat, 'access_list'), ' pool ', environment.getattr(l_1_nat, 'pool_name'), ))
        _loop_vars['nat_cli'] = l_1_nat_cli
        l_1_sort_key = str_join(('d_', t_3(context.eval_ctx, environment.getattr(l_1_nat, 'access_list'), '.'), ))
        _loop_vars['sort_key'] = l_1_sort_key
        if (t_1(environment.getattr(l_1_nat, 'priority'), 0) > 0):
            pass
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' priority ', environment.getattr(l_1_nat, 'priority'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
        if t_4(environment.getattr(l_1_nat, 'comment')):
            pass
            l_1_nat_cli = str_join(((undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli), ' comment ', environment.getattr(l_1_nat, 'comment'), ))
            _loop_vars['nat_cli'] = l_1_nat_cli
        context.call(environment.getattr((undefined(name='unsorted_nat_entries') if l_0_unsorted_nat_entries is missing else l_0_unsorted_nat_entries), 'append'), {'sort_key': (undefined(name='sort_key') if l_1_sort_key is missing else l_1_sort_key), 'cli': (undefined(name='nat_cli') if l_1_nat_cli is missing else l_1_nat_cli)}, _loop_vars=_loop_vars)
    l_1_nat = l_1_nat_cli = l_1_sort_key = missing
    for l_1_nat_entry in t_2((undefined(name='unsorted_nat_entries') if l_0_unsorted_nat_entries is missing else l_0_unsorted_nat_entries), 'sort_key'):
        _loop_vars = {}
        pass
        yield '   '
        yield str(environment.getattr(l_1_nat_entry, 'cli'))
        yield '\n'
    l_1_nat_entry = missing

blocks = {}
debug_info = '9=37&11=40&12=45&14=47&15=49&16=51&17=53&19=55&20=57&21=59&22=61&24=63&25=65&27=67&28=69&29=71&31=73&32=75&34=77&35=79&36=81&38=83&39=85&41=87&45=89&46=94&48=96&49=98&50=100&51=102&53=104&54=106&55=108&56=110&58=112&59=114&61=116&62=118&63=120&65=122&66=124&68=126&69=128&70=130&72=132&73=134&75=136&79=138&80=142&81=144&83=146&84=148&85=150&86=152&87=154&88=156&89=158&90=160&91=162&92=164&93=166&96=168&97=170&98=172&100=174&101=176&103=178&107=180&108=184&110=186&111=188&112=190&114=192&115=194&117=196&119=198&120=202'