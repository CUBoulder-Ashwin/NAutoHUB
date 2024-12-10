from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ethernet-interface-tx-queues.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tx_queue = resolve('tx_queue')
    l_0_units = resolve('units')
    l_0_ecn_command = resolve('ecn_command')
    l_0_drop_command = resolve('drop_command')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    yield '   !\n   tx-queue '
    yield str(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'id'))
    yield '\n'
    if t_2(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'comment')):
        pass
        for l_1_comment_line in t_1(context.call(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'comment'), 'splitlines')), []):
            _loop_vars = {}
            pass
            yield '      !! '
            yield str(l_1_comment_line)
            yield '\n'
        l_1_comment_line = missing
    if t_2(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'priority')):
        pass
        yield '      '
        yield str(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'priority'))
        yield '\n'
    if t_2(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'bandwidth_percent')):
        pass
        yield '      bandwidth percent '
        yield str(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'bandwidth_percent'))
        yield '\n'
    elif t_2(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'bandwidth_guaranteed_percent')):
        pass
        yield '      bandwidth guaranteed percent '
        yield str(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'bandwidth_guaranteed_percent'))
        yield '\n'
    if t_2(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'shape'), 'rate')):
        pass
        yield '      shape rate '
        yield str(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'shape'), 'rate'))
        yield '\n'
    if t_2(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect')):
        pass
        if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'count'), True):
            pass
            yield '      random-detect ecn count\n'
        if ((t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'min')) and t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'max'))) and t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'units'))):
            pass
            l_0_units = environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'units')
            context.vars['units'] = l_0_units
            context.exported_vars.add('units')
            l_0_ecn_command = 'random-detect ecn'
            context.vars['ecn_command'] = l_0_ecn_command
            context.exported_vars.add('ecn_command')
            l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' minimum-threshold ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'min'), ' ', (undefined(name='units') if l_0_units is missing else l_0_units), ))
            context.vars['ecn_command'] = l_0_ecn_command
            context.exported_vars.add('ecn_command')
            l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' maximum-threshold ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'max'), ' ', (undefined(name='units') if l_0_units is missing else l_0_units), ))
            context.vars['ecn_command'] = l_0_ecn_command
            context.exported_vars.add('ecn_command')
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'max_probability')):
                pass
                l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' max-mark-probability ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'max_probability'), ))
                context.vars['ecn_command'] = l_0_ecn_command
                context.exported_vars.add('ecn_command')
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'weight')):
                pass
                l_0_ecn_command = str_join(((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command), ' weight ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'ecn'), 'threshold'), 'weight'), ))
                context.vars['ecn_command'] = l_0_ecn_command
                context.exported_vars.add('ecn_command')
            yield '      '
            yield str((undefined(name='ecn_command') if l_0_ecn_command is missing else l_0_ecn_command))
            yield '\n'
        if ((t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'min')) and t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'max'))) and t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'units'))):
            pass
            l_0_units = environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'units')
            context.vars['units'] = l_0_units
            context.exported_vars.add('units')
            l_0_drop_command = 'random-detect drop'
            context.vars['drop_command'] = l_0_drop_command
            context.exported_vars.add('drop_command')
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'drop_precedence')):
                pass
                l_0_drop_command = str_join(((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command), ' drop-precedence ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'drop_precedence'), ))
                context.vars['drop_command'] = l_0_drop_command
                context.exported_vars.add('drop_command')
            l_0_drop_command = str_join(((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command), ' minimum-threshold ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'min'), ' ', (undefined(name='units') if l_0_units is missing else l_0_units), ))
            context.vars['drop_command'] = l_0_drop_command
            context.exported_vars.add('drop_command')
            l_0_drop_command = str_join(((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command), ' maximum-threshold ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'max'), ' ', (undefined(name='units') if l_0_units is missing else l_0_units), ))
            context.vars['drop_command'] = l_0_drop_command
            context.exported_vars.add('drop_command')
            l_0_drop_command = str_join(((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command), ' drop-probability ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'drop_probability'), ))
            context.vars['drop_command'] = l_0_drop_command
            context.exported_vars.add('drop_command')
            if t_2(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'weight')):
                pass
                l_0_drop_command = str_join(((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command), ' weight ', environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='tx_queue') if l_0_tx_queue is missing else l_0_tx_queue), 'random_detect'), 'drop'), 'threshold'), 'weight'), ))
                context.vars['drop_command'] = l_0_drop_command
                context.exported_vars.add('drop_command')
            yield '      '
            yield str((undefined(name='drop_command') if l_0_drop_command is missing else l_0_drop_command))
            yield '\n'

blocks = {}
debug_info = '8=28&9=30&10=32&11=36&14=39&15=42&17=44&18=47&19=49&20=52&22=54&23=57&25=59&26=61&29=64&30=66&31=69&32=72&33=75&34=78&35=80&37=83&38=85&40=89&42=91&43=93&44=96&45=99&46=101&48=104&49=107&50=110&51=113&52=115&54=119'