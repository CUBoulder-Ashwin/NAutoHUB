from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-bfd.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_bfd = resolve('router_bfd')
    l_0_interval = resolve('interval')
    l_0_min_rx = resolve('min_rx')
    l_0_multiplier = resolve('multiplier')
    l_0_init_interval = resolve('init_interval')
    l_0_init_multiplier = resolve('init_multiplier')
    l_0_init_round_trip = resolve('init_round_trip')
    l_0_ref_min_rx = resolve('ref_min_rx')
    l_0_ref_discriminator = resolve('ref_discriminator')
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
    if t_2((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd)):
        pass
        yield '\n### Router BFD\n'
        if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'slow_timer')):
            pass
            yield '\n| BFD Tuning |\n| ---------- |\n'
            if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'slow_timer')):
                pass
                yield '| Slow-Timer '
                yield str(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'slow_timer'))
                yield ' |\n'
        if ((t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'interval')) and t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'min_rx'))) and t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multiplier'))):
            pass
            yield '\n#### Router BFD Singlehop Summary\n\n| Interval | Minimum RX | Multiplier |\n| -------- | ---------- | ---------- |\n'
            l_0_interval = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'interval'), '-')
            context.vars['interval'] = l_0_interval
            context.exported_vars.add('interval')
            l_0_min_rx = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'min_rx'), '-')
            context.vars['min_rx'] = l_0_min_rx
            context.exported_vars.add('min_rx')
            l_0_multiplier = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multiplier'), '-')
            context.vars['multiplier'] = l_0_multiplier
            context.exported_vars.add('multiplier')
            yield '| '
            yield str((undefined(name='interval') if l_0_interval is missing else l_0_interval))
            yield ' | '
            yield str((undefined(name='min_rx') if l_0_min_rx is missing else l_0_min_rx))
            yield ' | '
            yield str((undefined(name='multiplier') if l_0_multiplier is missing else l_0_multiplier))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop')):
            pass
            yield '\n#### Router BFD Multihop Summary\n\n| Interval | Minimum RX | Multiplier |\n| -------- | ---------- | ---------- |\n'
            l_0_interval = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'interval'), '-')
            context.vars['interval'] = l_0_interval
            context.exported_vars.add('interval')
            l_0_min_rx = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'min_rx'), '-')
            context.vars['min_rx'] = l_0_min_rx
            context.exported_vars.add('min_rx')
            l_0_multiplier = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'multiplier'), '-')
            context.vars['multiplier'] = l_0_multiplier
            context.exported_vars.add('multiplier')
            yield '| '
            yield str((undefined(name='interval') if l_0_interval is missing else l_0_interval))
            yield ' | '
            yield str((undefined(name='min_rx') if l_0_min_rx is missing else l_0_min_rx))
            yield ' | '
            yield str((undefined(name='multiplier') if l_0_multiplier is missing else l_0_multiplier))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd')):
            pass
            yield '\n#### Router BFD SBFD Summary\n\n| Initiator Interval | Initiator Multiplier | Initiator Round-Trip | Reflector Minimum RX | Reflector Local-Discriminator |\n| ------------------ | -------------------- | -------------------- | ----------------------------- |\n'
            l_0_init_interval = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'initiator_interval'), '-')
            context.vars['init_interval'] = l_0_init_interval
            context.exported_vars.add('init_interval')
            l_0_init_multiplier = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'initiator_multiplier'), '-')
            context.vars['init_multiplier'] = l_0_init_multiplier
            context.exported_vars.add('init_multiplier')
            l_0_init_round_trip = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'initiator_measurement_round_trip'), '-')
            context.vars['init_round_trip'] = l_0_init_round_trip
            context.exported_vars.add('init_round_trip')
            l_0_ref_min_rx = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'reflector'), 'min_rx'), '-')
            context.vars['ref_min_rx'] = l_0_ref_min_rx
            context.exported_vars.add('ref_min_rx')
            l_0_ref_discriminator = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'reflector'), 'local_discriminator'), '-')
            context.vars['ref_discriminator'] = l_0_ref_discriminator
            context.exported_vars.add('ref_discriminator')
            yield '| '
            yield str((undefined(name='init_interval') if l_0_init_interval is missing else l_0_init_interval))
            yield ' | '
            yield str((undefined(name='init_multiplier') if l_0_init_multiplier is missing else l_0_init_multiplier))
            yield ' | '
            yield str((undefined(name='init_round_trip') if l_0_init_round_trip is missing else l_0_init_round_trip))
            yield ' | '
            yield str((undefined(name='ref_min_rx') if l_0_ref_min_rx is missing else l_0_ref_min_rx))
            yield ' | '
            yield str((undefined(name='ref_discriminator') if l_0_ref_discriminator is missing else l_0_ref_discriminator))
            yield ' |\n'
        yield '\n#### Router BFD Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-bfd.j2', 'documentation/router-bfd.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'init_interval': l_0_init_interval, 'init_multiplier': l_0_init_multiplier, 'init_round_trip': l_0_init_round_trip, 'interval': l_0_interval, 'min_rx': l_0_min_rx, 'multiplier': l_0_multiplier, 'ref_discriminator': l_0_ref_discriminator, 'ref_min_rx': l_0_ref_min_rx})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=32&10=35&14=38&15=41&18=43&24=46&25=49&26=52&27=56&29=62&35=65&36=68&37=71&38=75&40=81&46=84&47=87&48=90&49=93&50=96&51=100&57=111'