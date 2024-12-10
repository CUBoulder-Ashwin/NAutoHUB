from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-community-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_community_lists = resolve('ip_community_lists')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='ip_community_lists') if l_0_ip_community_lists is missing else l_0_ip_community_lists)):
        pass
        yield '!\n'
        for l_1_community_list in (undefined(name='ip_community_lists') if l_0_ip_community_lists is missing else l_0_ip_community_lists):
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_community_list, 'name')):
                pass
                for l_2_entry in t_1(environment.getattr(l_1_community_list, 'entries'), []):
                    _loop_vars = {}
                    pass
                    if t_4(environment.getattr(l_2_entry, 'action')):
                        pass
                        if t_4(environment.getattr(l_2_entry, 'regexp')):
                            pass
                            yield 'ip community-list regexp '
                            yield str(environment.getattr(l_1_community_list, 'name'))
                            yield ' '
                            yield str(environment.getattr(l_2_entry, 'action'))
                            yield ' '
                            yield str(environment.getattr(l_2_entry, 'regexp'))
                            yield '\n'
                        elif t_4(environment.getattr(l_2_entry, 'communities')):
                            pass
                            if (t_3(environment.getattr(l_2_entry, 'communities')) > 0):
                                pass
                                yield 'ip community-list '
                                yield str(environment.getattr(l_1_community_list, 'name'))
                                yield ' '
                                yield str(environment.getattr(l_2_entry, 'action'))
                                yield ' '
                                yield str(t_2(context.eval_ctx, environment.getattr(l_2_entry, 'communities'), ' '))
                                yield '\n'
                l_2_entry = missing
        l_1_community_list = missing

blocks = {}
debug_info = '7=36&9=39&10=42&11=44&12=47&13=49&14=52&15=58&16=60&17=63'