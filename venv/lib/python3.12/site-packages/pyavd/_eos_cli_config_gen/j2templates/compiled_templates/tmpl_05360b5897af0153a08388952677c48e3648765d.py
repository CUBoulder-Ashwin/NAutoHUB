from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mac-access-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_access_lists = resolve('mac_access_lists')
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
    for l_1_mac_access_list in t_1((undefined(name='mac_access_lists') if l_0_mac_access_lists is missing else l_0_mac_access_lists), 'name'):
        _loop_vars = {}
        pass
        if (t_2(environment.getattr(l_1_mac_access_list, 'name')) and t_2(environment.getattr(l_1_mac_access_list, 'entries'))):
            pass
            yield '!\nmac access-list '
            yield str(environment.getattr(l_1_mac_access_list, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_mac_access_list, 'counters_per_entry'), True):
                pass
                yield '   counters per-entry\n'
            for l_2_acl_entry in environment.getattr(l_1_mac_access_list, 'entries'):
                l_2_acl_string = missing
                _loop_vars = {}
                pass
                l_2_acl_string = ''
                _loop_vars['acl_string'] = l_2_acl_string
                if t_2(environment.getattr(l_2_acl_entry, 'sequence')):
                    pass
                    l_2_acl_string = str_join(((undefined(name='acl_string') if l_2_acl_string is missing else l_2_acl_string), environment.getattr(l_2_acl_entry, 'sequence'), ' ', ))
                    _loop_vars['acl_string'] = l_2_acl_string
                l_2_acl_string = str_join(((undefined(name='acl_string') if l_2_acl_string is missing else l_2_acl_string), environment.getattr(l_2_acl_entry, 'action'), ))
                _loop_vars['acl_string'] = l_2_acl_string
                yield '   '
                yield str((undefined(name='acl_string') if l_2_acl_string is missing else l_2_acl_string))
                yield '\n'
            l_2_acl_entry = l_2_acl_string = missing
    l_1_mac_access_list = missing

blocks = {}
debug_info = '7=24&8=27&10=30&11=32&14=35&15=39&16=41&17=43&19=45&20=48'