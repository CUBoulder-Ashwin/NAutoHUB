from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vlans.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vlans = resolve('vlans')
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
    for l_1_vlan in t_1((undefined(name='vlans') if l_0_vlans is missing else l_0_vlans), 'id'):
        _loop_vars = {}
        pass
        yield '!\nvlan '
        yield str(environment.getattr(l_1_vlan, 'id'))
        yield '\n'
        if t_2(environment.getattr(l_1_vlan, 'name')):
            pass
            yield '   name '
            yield str(environment.getattr(l_1_vlan, 'name'))
            yield '\n'
        if t_2(environment.getattr(l_1_vlan, 'state')):
            pass
            yield '   state '
            yield str(environment.getattr(l_1_vlan, 'state'))
            yield '\n'
        for l_2_trunk_group in t_1(environment.getattr(l_1_vlan, 'trunk_groups')):
            _loop_vars = {}
            pass
            yield '   trunk group '
            yield str(l_2_trunk_group)
            yield '\n'
        l_2_trunk_group = missing
        if (t_2(environment.getattr(environment.getattr(l_1_vlan, 'private_vlan'), 'type')) and t_2(environment.getattr(environment.getattr(l_1_vlan, 'private_vlan'), 'primary_vlan'))):
            pass
            yield '   private-vlan '
            yield str(environment.getattr(environment.getattr(l_1_vlan, 'private_vlan'), 'type'))
            yield ' primary vlan '
            yield str(environment.getattr(environment.getattr(l_1_vlan, 'private_vlan'), 'primary_vlan'))
            yield '\n'
    l_1_vlan = missing

blocks = {}
debug_info = '7=24&9=28&10=30&11=33&13=35&14=38&16=40&17=44&19=47&21=50'