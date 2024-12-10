from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/hardware.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_hardware = resolve('hardware')
    l_0_hardware_counters = resolve('hardware_counters')
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
    if t_2(environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'port_groups')):
        pass
        yield '!\n'
        for l_1_port_group in environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'port_groups'):
            _loop_vars = {}
            pass
            if t_2(environment.getattr(l_1_port_group, 'select')):
                pass
                yield 'hardware port-group '
                yield str(environment.getattr(l_1_port_group, 'port_group'))
                yield ' select '
                yield str(environment.getattr(l_1_port_group, 'select'))
                yield '\n'
        l_1_port_group = missing
    if t_2(environment.getattr((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters), 'features')):
        pass
        yield '!\n'
        for l_1_feature in t_1(environment.getattr((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters), 'features'), 'name'):
            l_1_hardware_counters_cli = missing
            _loop_vars = {}
            pass
            l_1_hardware_counters_cli = str_join(('hardware counter feature ', environment.getattr(l_1_feature, 'name'), ))
            _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'direction')):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' ', environment.getattr(l_1_feature, 'direction'), ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'address_type')):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' ', environment.getattr(l_1_feature, 'address_type'), ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'layer3'), True):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' layer3', ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'vrf')):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' vrf ', environment.getattr(l_1_feature, 'vrf'), ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'prefix')):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' ', environment.getattr(l_1_feature, 'prefix'), ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            if t_2(environment.getattr(l_1_feature, 'units_packets'), True):
                pass
                l_1_hardware_counters_cli = str_join(((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli), ' units packets', ))
                _loop_vars['hardware_counters_cli'] = l_1_hardware_counters_cli
            yield str((undefined(name='hardware_counters_cli') if l_1_hardware_counters_cli is missing else l_1_hardware_counters_cli))
            yield '\n'
        l_1_feature = l_1_hardware_counters_cli = missing
    if t_2(environment.getattr(environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'access_list'), 'mechanism')):
        pass
        yield '!\nhardware access-list mechanism '
        yield str(environment.getattr(environment.getattr((undefined(name='hardware') if l_0_hardware is missing else l_0_hardware), 'access_list'), 'mechanism'))
        yield '\n'

blocks = {}
debug_info = '7=25&9=28&10=31&11=34&15=39&17=42&18=46&19=48&20=50&22=52&23=54&25=56&26=58&28=60&29=62&31=64&32=66&34=68&35=70&37=72&40=75&42=78'