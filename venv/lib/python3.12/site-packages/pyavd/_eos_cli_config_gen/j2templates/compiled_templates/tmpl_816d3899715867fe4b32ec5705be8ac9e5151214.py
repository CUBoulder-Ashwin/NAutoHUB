from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vlan-internal-order.j2'

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
    if ((t_1(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'allocation')) and t_1(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'beginning'))) and t_1(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'ending'))):
        pass
        yield '!\nvlan internal order '
        yield str(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'allocation'))
        yield ' range '
        yield str(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'beginning'))
        yield ' '
        yield str(environment.getattr(environment.getattr((undefined(name='vlan_internal_order') if l_0_vlan_internal_order is missing else l_0_vlan_internal_order), 'range'), 'ending'))
        yield '\n'

blocks = {}
debug_info = '7=18&11=21'