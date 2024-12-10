from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/vlan-internal-order.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vlan_internal_order = resolve('vlan_internal_order')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order)):
        pass
        yield '\n## Internal VLAN Allocation Policy\n\n### Internal VLAN Allocation Policy Summary\n\n| Policy Allocation | Range Beginning | Range Ending |\n| ------------------| --------------- | ------------ |\n| '
        yield str(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'allocation'))
        yield ' | '
        yield str(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'beginning'))
        yield ' | '
        yield str(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'ending'))
        yield ' |\n\n### Internal VLAN Allocation Policy Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/vlan-internal-order.j2', 'documentation/vlan-internal-order.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=18&15=21&20=27'