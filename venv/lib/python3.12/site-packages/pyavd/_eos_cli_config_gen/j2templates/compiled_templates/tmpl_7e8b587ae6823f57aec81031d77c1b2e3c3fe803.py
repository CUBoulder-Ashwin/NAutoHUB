from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-extcommunity-lists-regexp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_extcommunity_lists_regexp = resolve('ip_extcommunity_lists_regexp')
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
    for l_1_ip_extcommunity_list in t_2((undefined(name='ip_extcommunity_lists_regexp') if l_0_ip_extcommunity_lists_regexp is missing else l_0_ip_extcommunity_lists_regexp), 'name'):
        _loop_vars = {}
        pass
        yield '!\n'
        for l_2_entry in t_1(environment.getattr(l_1_ip_extcommunity_list, 'entries'), []):
            _loop_vars = {}
            pass
            if (t_3(environment.getattr(l_2_entry, 'type')) and t_3(environment.getattr(l_2_entry, 'regexp'))):
                pass
                yield 'ip extcommunity-list regexp '
                yield str(environment.getattr(l_1_ip_extcommunity_list, 'name'))
                yield ' '
                yield str(environment.getattr(l_2_entry, 'type'))
                yield ' '
                yield str(environment.getattr(l_2_entry, 'regexp'))
                yield '\n'
        l_2_entry = missing
    l_1_ip_extcommunity_list = missing

blocks = {}
debug_info = '7=30&9=34&10=37&11=40'