from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/queue-monitor-length.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_queue_monitor_length = resolve('queue_monitor_length')
    l_0_default_thresholds_cli = resolve('default_thresholds_cli')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'enabled'), True):
        pass
        yield '!\nqueue-monitor length\n'
        if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'notifying'), True):
            pass
            yield 'queue-monitor length notifying\n'
        elif t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'notifying'), False):
            pass
            yield 'no queue-monitor length notifying\n'
        if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'tx_latency'), True):
            pass
            yield 'queue-monitor length tx-latency\n'
        if t_1(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'default_thresholds'), 'high')):
            pass
            l_0_default_thresholds_cli = 'queue-monitor length default threshold'
            context.vars['default_thresholds_cli'] = l_0_default_thresholds_cli
            context.exported_vars.add('default_thresholds_cli')
            if t_1(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'default_thresholds'), 'low')):
                pass
                l_0_default_thresholds_cli = str_join(((undefined(name='default_thresholds_cli') if l_0_default_thresholds_cli is missing else l_0_default_thresholds_cli), 's ', environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'default_thresholds'), 'high'), ' ', environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'default_thresholds'), 'low'), ))
                context.vars['default_thresholds_cli'] = l_0_default_thresholds_cli
                context.exported_vars.add('default_thresholds_cli')
            else:
                pass
                l_0_default_thresholds_cli = str_join(((undefined(name='default_thresholds_cli') if l_0_default_thresholds_cli is missing else l_0_default_thresholds_cli), ' ', environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'default_thresholds'), 'high'), ))
                context.vars['default_thresholds_cli'] = l_0_default_thresholds_cli
                context.exported_vars.add('default_thresholds_cli')
            yield str((undefined(name='default_thresholds_cli') if l_0_default_thresholds_cli is missing else l_0_default_thresholds_cli))
            yield '\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high')):
            pass
            if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'low')):
                pass
                yield 'queue-monitor length cpu thresholds '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high'))
                yield ' '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'low'))
                yield '\n'
            else:
                pass
                yield 'queue-monitor length cpu threshold '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high'))
                yield '\n'
        if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'log')):
            pass
            yield '!\nqueue-monitor length log '
            yield str(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'log'))
            yield '\n'

blocks = {}
debug_info = '7=19&10=22&12=25&15=28&18=31&19=33&20=36&21=38&23=43&25=46&27=48&28=50&29=53&31=60&34=62&36=65'