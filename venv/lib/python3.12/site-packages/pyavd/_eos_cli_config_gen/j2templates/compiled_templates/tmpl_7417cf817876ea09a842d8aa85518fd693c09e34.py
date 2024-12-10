from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/qos.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_qos = resolve('qos')
    l_0_ecn_command = resolve('ecn_command')
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
    if t_2((undefined(name='qos') if l_0_qos is missing else l_0_qos)):
        pass
        yield '!\n'
        if t_2(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'rewrite_dscp'), True):
            pass
            yield 'qos rewrite dscp\n'
        for l_1_cos_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'cos')):
            _loop_vars = {}
            pass
            yield 'qos map cos '
            yield str(l_1_cos_map)
            yield '\n'
        l_1_cos_map = missing
        for l_1_dscp_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'dscp')):
            _loop_vars = {}
            pass
            yield 'qos map dscp '
            yield str(l_1_dscp_map)
            yield '\n'
        l_1_dscp_map = missing
        for l_1_tc_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'traffic_class')):
            _loop_vars = {}
            pass
            yield 'qos map traffic-class '
            yield str(l_1_tc_map)
            yield '\n'
        l_1_tc_map = missing
        for l_1_exp_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'exp')):
            _loop_vars = {}
            pass
            yield 'qos map exp '
            yield str(l_1_exp_map)
            yield '\n'
        l_1_exp_map = missing
        if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'random_detect'), 'ecn'), 'allow_non_ect'), 'enabled')):
            pass
            yield '!\n'
            l_0_ecn_command = 'qos random-detect ecn allow non-ect'
            context.vars['ecn_command'] = l_0_ecn_command
            context.exported_vars.add('ecn_command')
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'random_detect'), 'ecn'), 'allow_non_ect'), 'chip_based'), True):
                pass
                l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' chip-based', ))
                context.vars['ecn_command'] = l_0_ecn_command
                context.exported_vars.add('ecn_command')
            yield str((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command))
            yield '\n'

blocks = {}
debug_info = '7=25&9=28&12=31&13=35&15=38&16=42&18=45&19=49&21=52&22=56&24=59&26=62&27=65&28=67&30=70'