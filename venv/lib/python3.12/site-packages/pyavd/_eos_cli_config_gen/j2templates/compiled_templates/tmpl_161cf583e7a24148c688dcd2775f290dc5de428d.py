from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/qos.j2'

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
        t_2 = environment.filters['default']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'default' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='qos') if l_0_qos is missing else l_0_qos)):
        pass
        yield '\n### QOS\n\n#### QOS Summary\n'
        if t_3(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'rewrite_dscp'), True):
            pass
            yield '\nQOS rewrite DSCP: **enabled**\n'
        else:
            pass
            yield '\nQOS rewrite DSCP: **disabled**\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'random_detect'), 'ecn'), 'allow_non_ect'), 'enabled')):
            pass
            l_0_ecn_command = 'QOS random-detect ECN is set to allow **non-ect**'
            context.vars['ecn_command'] = l_0_ecn_command
            context.exported_vars.add('ecn_command')
            if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'random_detect'), 'ecn'), 'allow_non_ect'), 'chip_based'), True):
                pass
                l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' **chip-based**', ))
                context.vars['ecn_command'] = l_0_ecn_command
                context.exported_vars.add('ecn_command')
            yield '\n'
            yield str((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command))
            yield '\n'
        if t_3(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map')):
            pass
            yield '\n##### QOS Mappings\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'cos')):
                pass
                yield '\n| COS to Traffic Class mappings |\n| ----------------------------- |\n'
                for l_1_cos_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'cos')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(t_2(l_1_cos_map, '-'))
                    yield ' |\n'
                l_1_cos_map = missing
            if t_3(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'dscp')):
                pass
                yield '\n| DSCP to Traffic Class mappings |\n| ------------------------------ |\n'
                for l_1_dscp_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'dscp')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(t_2(l_1_dscp_map, '-'))
                    yield ' |\n'
                l_1_dscp_map = missing
            if t_3(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'exp')):
                pass
                yield '\n| EXP to Traffic Class mappings |\n| ----------------------------- |\n'
                for l_1_exp_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'exp')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(t_2(l_1_exp_map, '-'))
                    yield ' |\n'
                l_1_exp_map = missing
            if t_3(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'traffic_class')):
                pass
                yield '\n| Traffic Class to DSCP or COS mappings |\n| ------------------------------------- |\n'
                for l_1_tc_map in t_1(environment.getattr(environment.getattr((undefined(name='qos') if l_0_qos is missing else l_0_qos), 'map'), 'traffic_class')):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(t_2(l_1_tc_map, '-'))
                    yield ' |\n'
                l_1_tc_map = missing
        yield '\n#### QOS Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/qos.j2', 'documentation/qos.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ecn_command': l_0_ecn_command})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=31&12=34&19=40&20=42&21=45&22=47&25=51&27=53&30=56&34=59&35=63&38=66&42=69&43=73&46=76&50=79&51=83&54=86&58=89&59=93&67=97'