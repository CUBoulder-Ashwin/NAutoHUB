from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/policy-maps-copp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_policy_maps = resolve('policy_maps')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy'), 'classes')):
        pass
        yield '!\npolicy-map type copp copp-system-policy\n'
        l_1_loop = missing
        for l_1_class, l_1_loop in LoopContext(environment.getattr(environment.getattr((undefined(name='policy_maps') if l_0_policy_maps is missing else l_0_policy_maps), 'copp_system_policy'), 'classes'), undefined):
            _loop_vars = {}
            pass
            yield '   class '
            yield str(environment.getattr(l_1_class, 'name'))
            yield '\n'
            if t_1(environment.getattr(l_1_class, 'rate_unit')):
                pass
                if t_1(environment.getattr(l_1_class, 'shape')):
                    pass
                    yield '      shape '
                    yield str(environment.getattr(l_1_class, 'rate_unit'))
                    yield ' '
                    yield str(environment.getattr(l_1_class, 'shape'))
                    yield '\n'
                if t_1(environment.getattr(l_1_class, 'bandwidth')):
                    pass
                    yield '      bandwidth '
                    yield str(environment.getattr(l_1_class, 'rate_unit'))
                    yield ' '
                    yield str(environment.getattr(l_1_class, 'bandwidth'))
                    yield '\n'
            if (not environment.getattr(l_1_loop, 'last')):
                pass
                yield '   !\n'
        l_1_loop = l_1_class = missing

blocks = {}
debug_info = '7=18&10=22&11=26&12=28&13=30&14=33&16=37&17=40&20=44'