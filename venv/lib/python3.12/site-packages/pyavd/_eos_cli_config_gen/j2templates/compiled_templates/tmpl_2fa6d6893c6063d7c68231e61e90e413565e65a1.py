from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/maintenance.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_maintenance = resolve('maintenance')
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
    if t_4((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance)):
        pass
        yield '\n### Maintenance\n\n#### Maintenance defaults\n\nDefault maintenance bgp profile: **'
        yield str(t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_bgp_profile'), 'Default'))
        yield '**\n\nDefault maintenance interface profile: **'
        yield str(t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_interface_profile'), 'Default'))
        yield '**\n\nDefault maintenance unit profile: **'
        yield str(t_1(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_unit_profile'), 'Default'))
        yield '**\n\n#### Maintenance profiles\n\n| BGP profile | Initiator route-map |\n| ----------- | ------------------- |\n'
        for l_1_bgp_profile in t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'bgp_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_bgp_profile, 'name'))
            yield ' | '
            yield str(t_1(environment.getattr(environment.getattr(l_1_bgp_profile, 'initiator'), 'route_map_inout'), 'SystemGenerated'))
            yield ' |\n'
        l_1_bgp_profile = missing
        yield '\n| Interface profile | Rate monitoring load interval (s) | Rate monitoring threshold in/out (kbps) | Shutdown Max Delay |\n|-------------------|-----------------------------------|-----------------------------------------|--------------------|\n'
        for l_1_interface_profile in t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'interface_profiles'), 'name'):
            l_1_row_load_interval = l_1_row_threshold = l_1_row_shutdown = missing
            _loop_vars = {}
            pass
            l_1_row_load_interval = t_1(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'load_interval'), 60)
            _loop_vars['row_load_interval'] = l_1_row_load_interval
            l_1_row_threshold = t_1(environment.getattr(environment.getattr(l_1_interface_profile, 'rate_monitoring'), 'threshold'), 100)
            _loop_vars['row_threshold'] = l_1_row_threshold
            l_1_row_shutdown = t_1(environment.getattr(environment.getattr(l_1_interface_profile, 'shutdown'), 'max_delay'), 'disabled')
            _loop_vars['row_shutdown'] = l_1_row_shutdown
            yield '| '
            yield str(environment.getattr(l_1_interface_profile, 'name'))
            yield ' | '
            yield str((undefined(name='row_load_interval') if l_1_row_load_interval is missing else l_1_row_load_interval))
            yield ' | '
            yield str((undefined(name='row_threshold') if l_1_row_threshold is missing else l_1_row_threshold))
            yield ' | '
            yield str((undefined(name='row_shutdown') if l_1_row_shutdown is missing else l_1_row_shutdown))
            yield ' |\n'
        l_1_interface_profile = l_1_row_load_interval = l_1_row_threshold = l_1_row_shutdown = missing
        yield '\n| Unit profile | on-boot duration (s) |\n| ------------ | -------------------- |\n'
        for l_1_unit_profile in t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'unit_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '| '
            yield str(environment.getattr(l_1_unit_profile, 'name'))
            yield ' | '
            yield str(t_1(environment.getattr(environment.getattr(l_1_unit_profile, 'on_boot'), 'duration'), 'disabled'))
            yield ' |\n'
        l_1_unit_profile = missing
        yield '\n#### Maintenance units\n\n| Unit | Interface groups | BGP groups | Unit profile | Quiesce |\n| ---- | ---------------- | ---------- | ------------ | ------- |\n'
        for l_1_unit in t_2(environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'units'), 'name'):
            l_1_row_interface_groups = l_1_row_bgp_groups = l_1_row_unit_profile = l_1_row_quiesce = missing
            _loop_vars = {}
            pass
            l_1_row_interface_groups = t_3(context.eval_ctx, t_2(t_1(environment.getattr(environment.getattr(l_1_unit, 'groups'), 'interface_groups'), ['-'])), '<br/>')
            _loop_vars['row_interface_groups'] = l_1_row_interface_groups
            l_1_row_bgp_groups = t_3(context.eval_ctx, t_2(t_1(environment.getattr(environment.getattr(l_1_unit, 'groups'), 'bgp_groups'), ['-'])), '<br/>')
            _loop_vars['row_bgp_groups'] = l_1_row_bgp_groups
            l_1_row_unit_profile = t_1(environment.getattr(l_1_unit, 'profile'), environment.getattr((undefined(name='maintenance') if l_0_maintenance is missing else l_0_maintenance), 'default_unit_profile'), 'Default')
            _loop_vars['row_unit_profile'] = l_1_row_unit_profile
            l_1_row_quiesce = ('Yes' if t_4(environment.getattr(l_1_unit, 'quiesce'), True) else 'No')
            _loop_vars['row_quiesce'] = l_1_row_quiesce
            yield '| '
            yield str(environment.getattr(l_1_unit, 'name'))
            yield ' | '
            yield str((undefined(name='row_interface_groups') if l_1_row_interface_groups is missing else l_1_row_interface_groups))
            yield ' | '
            yield str((undefined(name='row_bgp_groups') if l_1_row_bgp_groups is missing else l_1_row_bgp_groups))
            yield ' | '
            yield str((undefined(name='row_unit_profile') if l_1_row_unit_profile is missing else l_1_row_unit_profile))
            yield ' | '
            yield str((undefined(name='row_quiesce') if l_1_row_quiesce is missing else l_1_row_quiesce))
            yield ' |\n'
        l_1_unit = l_1_row_interface_groups = l_1_row_bgp_groups = l_1_row_unit_profile = l_1_row_quiesce = missing
        yield '\n#### Maintenance Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/maintenance.j2', 'documentation/maintenance.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=36&13=39&15=41&17=43&23=45&24=49&29=55&30=59&31=61&32=63&33=66&38=76&39=80&46=86&47=90&48=92&49=94&50=96&51=99&57=111'