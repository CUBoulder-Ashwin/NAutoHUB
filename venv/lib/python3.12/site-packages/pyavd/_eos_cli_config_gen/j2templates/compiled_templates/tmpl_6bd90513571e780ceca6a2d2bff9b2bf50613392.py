from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/hardware-counters.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_hardware_counters = resolve('hardware_counters')
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
    if t_3((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters)):
        pass
        yield '\n### Hardware Counters\n\n#### Hardware Counters Summary\n'
        if t_3(environment.getattr((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters), 'features')):
            pass
            yield '\n##### Hardware Counter Features\n\n**NOTE:** Not all options (columns) in the table below are compatible with every available feature, it is the user responsibility to configure valid options for each feature.\n\n| Feature | Flow Direction | Address Type | Layer3 | VRF | Prefix | Units Packets |\n| ------- | -------------- | ------------ | ------ | --- | ------ | ------------- |\n'
            for l_1_feature in t_2(environment.getattr((undefined(name='hardware_counters') if l_0_hardware_counters is missing else l_0_hardware_counters), 'features'), 'name'):
                l_1_feature_direction = l_1_feature_address_type = l_1_feature_vrf = l_1_feature_layer3 = l_1_feature_prefix = l_1_feature_units_packets = missing
                _loop_vars = {}
                pass
                l_1_feature_direction = t_1(environment.getattr(l_1_feature, 'direction'), '-')
                _loop_vars['feature_direction'] = l_1_feature_direction
                l_1_feature_address_type = t_1(environment.getattr(l_1_feature, 'address_type'), '-')
                _loop_vars['feature_address_type'] = l_1_feature_address_type
                l_1_feature_vrf = t_1(environment.getattr(l_1_feature, 'vrf'), '-')
                _loop_vars['feature_vrf'] = l_1_feature_vrf
                l_1_feature_layer3 = t_1(environment.getattr(l_1_feature, 'layer3'), '-')
                _loop_vars['feature_layer3'] = l_1_feature_layer3
                l_1_feature_prefix = t_1(environment.getattr(l_1_feature, 'prefix'), '-')
                _loop_vars['feature_prefix'] = l_1_feature_prefix
                l_1_feature_units_packets = t_1(environment.getattr(l_1_feature, 'units_packets'), '-')
                _loop_vars['feature_units_packets'] = l_1_feature_units_packets
                yield '| '
                yield str(environment.getattr(l_1_feature, 'name'))
                yield ' | '
                yield str((undefined(name='feature_direction') if l_1_feature_direction is missing else l_1_feature_direction))
                yield ' | '
                yield str((undefined(name='feature_address_type') if l_1_feature_address_type is missing else l_1_feature_address_type))
                yield ' | '
                yield str((undefined(name='feature_vrf') if l_1_feature_vrf is missing else l_1_feature_vrf))
                yield ' | '
                yield str((undefined(name='feature_layer3') if l_1_feature_layer3 is missing else l_1_feature_layer3))
                yield ' | '
                yield str((undefined(name='feature_prefix') if l_1_feature_prefix is missing else l_1_feature_prefix))
                yield ' | '
                yield str((undefined(name='feature_units_packets') if l_1_feature_units_packets is missing else l_1_feature_units_packets))
                yield ' |\n'
            l_1_feature = l_1_feature_direction = l_1_feature_address_type = l_1_feature_vrf = l_1_feature_layer3 = l_1_feature_prefix = l_1_feature_units_packets = missing
        yield '\n#### Hardware Counters Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/hardware-counters.j2', 'documentation/hardware-counters.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&12=33&20=36&21=40&22=42&23=44&24=46&25=48&26=50&27=53&34=69'