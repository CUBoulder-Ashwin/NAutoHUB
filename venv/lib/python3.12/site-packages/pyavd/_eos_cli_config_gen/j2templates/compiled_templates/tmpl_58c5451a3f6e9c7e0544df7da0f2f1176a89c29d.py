from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/l2-protocol-forwarding.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_l2_protocol = resolve('l2_protocol')
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
    if t_2((undefined(name='l2_protocol') if l_0_l2_protocol is missing else l_0_l2_protocol)):
        pass
        yield '!\nl2-protocol\n'
        for l_1_profile in t_1(environment.getattr((undefined(name='l2_protocol') if l_0_l2_protocol is missing else l_0_l2_protocol), 'forwarding_profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '   forwarding profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            for l_2_protocol in environment.getattr(l_1_profile, 'protocols'):
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_2_protocol, 'forward'), True):
                    pass
                    yield '      '
                    yield str(environment.getattr(l_2_protocol, 'name'))
                    yield ' forward\n'
                if t_2(environment.getattr(l_2_protocol, 'tagged_forward'), True):
                    pass
                    yield '      '
                    yield str(environment.getattr(l_2_protocol, 'name'))
                    yield ' tagged forward\n'
                if t_2(environment.getattr(l_2_protocol, 'untagged_forward'), True):
                    pass
                    yield '      '
                    yield str(environment.getattr(l_2_protocol, 'name'))
                    yield ' untagged forward\n'
            l_2_protocol = missing
        l_1_profile = missing

blocks = {}
debug_info = '6=24&9=27&10=31&11=33&12=36&13=39&15=41&16=44&18=46&19=49'