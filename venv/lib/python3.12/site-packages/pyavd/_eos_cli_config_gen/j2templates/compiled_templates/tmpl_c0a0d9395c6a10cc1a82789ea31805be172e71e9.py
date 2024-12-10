from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/spanning-tree.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_spanning_tree = resolve('spanning_tree')
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
    if t_2((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree)):
        pass
        yield '!\n'
        if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode')):
            pass
            yield 'spanning-tree mode '
            yield str(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'no_spanning_tree_vlan')):
            pass
            yield 'no spanning-tree vlan-id '
            yield str(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'no_spanning_tree_vlan'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'pvst_border'), True):
            pass
            yield 'spanning-tree mst pvst border\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpduguard_default'), True):
            pass
            yield 'spanning-tree edge-port bpduguard default\n'
        elif t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpduguard_default'), False):
            pass
            yield 'no spanning-tree edge-port bpduguard default\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpdufilter_default'), True):
            pass
            yield 'spanning-tree edge-port bpdufilter default\n'
        elif t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpdufilter_default'), False):
            pass
            yield 'no spanning-tree edge-port bpdufilter default\n'
        if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'bpduguard_rate_limit')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'bpduguard_rate_limit'), 'default'), False):
                pass
                yield 'no spanning-tree bpduguard rate-limit default\n'
            elif t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'bpduguard_rate_limit'), 'default'), True):
                pass
                yield 'spanning-tree bpduguard rate-limit default\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'bpduguard_rate_limit'), 'count')):
                pass
                yield 'spanning-tree bpduguard rate-limit count '
                yield str(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'bpduguard_rate_limit'), 'count'))
                yield '\n'
        if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'root_super'), True):
            pass
            yield 'spanning-tree root super\n'
        if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'mstp'):
            pass
            for l_1_mst_instance in t_1(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst_instances'), 'id'):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_1_mst_instance, 'priority')):
                    pass
                    yield 'spanning-tree mst '
                    yield str(environment.getattr(l_1_mst_instance, 'id'))
                    yield ' priority '
                    yield str(environment.getattr(l_1_mst_instance, 'priority'))
                    yield '\n'
            l_1_mst_instance = missing
        elif t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'rapid-pvst'):
            pass
            for l_1_vlan_id in t_1(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rapid_pvst_instances'), 'id'):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_1_vlan_id, 'priority')):
                    pass
                    yield 'spanning-tree vlan-id '
                    yield str(environment.getattr(l_1_vlan_id, 'id'))
                    yield ' priority '
                    yield str(environment.getattr(l_1_vlan_id, 'priority'))
                    yield '\n'
            l_1_vlan_id = missing
        else:
            pass
            if t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rstp_priority')):
                pass
                yield 'spanning-tree priority '
                yield str(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rstp_priority'))
                yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration')):
            pass
            yield '!\nspanning-tree mst configuration\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'name')):
                pass
                yield '   name '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'name'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'revision')):
                pass
                yield '   revision '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'revision'))
                yield '\n'
            for l_1_instance in t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'instances'), 'id'):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_1_instance, 'vlans')):
                    pass
                    yield '   instance '
                    yield str(environment.getattr(l_1_instance, 'id'))
                    yield ' vlan '
                    yield str(environment.getattr(l_1_instance, 'vlans'))
                    yield '\n'
            l_1_instance = missing

blocks = {}
debug_info = '7=24&9=27&10=30&12=32&13=35&15=37&18=40&20=43&23=46&25=49&28=52&29=54&31=57&34=60&35=63&38=65&41=68&42=70&43=73&44=76&47=81&48=83&49=86&50=89&54=96&55=99&58=101&61=104&62=107&64=109&65=112&67=114&68=117&69=120'