from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/policy-maps-pbr.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_policy_maps = resolve('policy_maps')
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
    l_1_loop = missing
    for l_1_policy_map, l_1_loop in LoopContext(t_2(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'pbr'), 'name'), undefined):
        _loop_vars = {}
        pass
        yield '!\npolicy-map type pbr '
        yield str(environment.getattr(l_1_policy_map, 'name'))
        yield '\n'
        l_2_loop = missing
        for l_2_class, l_2_loop in LoopContext(t_1(environment.getattr(l_1_policy_map, 'classes'), []), undefined):
            l_2_nexthop_cli = resolve('nexthop_cli')
            l_2_class_cli = missing
            _loop_vars = {}
            pass
            l_2_class_cli = str_join(('class ', environment.getattr(l_2_class, 'name'), ))
            _loop_vars['class_cli'] = l_2_class_cli
            if t_3(environment.getattr(l_2_class, 'index')):
                pass
                l_2_class_cli = str_join((environment.getattr(l_2_class, 'index'), ' ', (undefined(name='class_cli') if l_2_class_cli is missing else l_2_class_cli), ))
                _loop_vars['class_cli'] = l_2_class_cli
            if (not environment.getattr(l_2_loop, 'first')):
                pass
                yield '   !\n'
            yield '   '
            yield str((undefined(name='class_cli') if l_2_class_cli is missing else l_2_class_cli))
            yield '\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr(l_2_class, 'set'), 'nexthop'), 'ip_address')):
                pass
                l_2_nexthop_cli = 'set nexthop'
                _loop_vars['nexthop_cli'] = l_2_nexthop_cli
                if t_3(environment.getattr(environment.getattr(environment.getattr(l_2_class, 'set'), 'nexthop'), 'recursive'), True):
                    pass
                    l_2_nexthop_cli = str_join(((undefined(name='nexthop_cli') if l_2_nexthop_cli is missing else l_2_nexthop_cli), ' recursive', ))
                    _loop_vars['nexthop_cli'] = l_2_nexthop_cli
                l_2_nexthop_cli = str_join(((undefined(name='nexthop_cli') if l_2_nexthop_cli is missing else l_2_nexthop_cli), ' ', environment.getattr(environment.getattr(environment.getattr(l_2_class, 'set'), 'nexthop'), 'ip_address'), ))
                _loop_vars['nexthop_cli'] = l_2_nexthop_cli
                yield '      '
                yield str((undefined(name='nexthop_cli') if l_2_nexthop_cli is missing else l_2_nexthop_cli))
                yield '\n'
            if t_3(environment.getattr(l_2_class, 'drop'), True):
                pass
                yield '      drop\n'
        l_2_loop = l_2_class = l_2_class_cli = l_2_nexthop_cli = missing
    l_1_loop = l_1_policy_map = missing

blocks = {}
debug_info = '7=31&9=35&10=38&11=43&12=45&13=47&15=49&18=53&19=55&20=57&21=59&22=61&24=63&25=66&27=68'