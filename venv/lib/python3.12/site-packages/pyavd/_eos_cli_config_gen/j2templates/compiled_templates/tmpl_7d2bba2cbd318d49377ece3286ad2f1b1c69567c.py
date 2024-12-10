from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-access-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_access_lists = resolve('ip_access_lists')
    l_0_ip_access_lists_max_entries = resolve('ip_access_lists_max_entries')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='ip_access_lists') if l_0_ip_access_lists is missing else l_0_ip_access_lists)):
        pass
        yield '\n### IP Access-lists\n'
        if t_1((undefined(name='ip_access_lists_max_entries') if l_0_ip_access_lists_max_entries is missing else l_0_ip_access_lists_max_entries)):
            pass
            yield '\n#### IP Access-lists Summary\n\n- The maximum number of ACL entries allowed to be provisioned per switch: '
            yield str((undefined(name='ip_access_lists_max_entries') if l_0_ip_access_lists_max_entries is missing else l_0_ip_access_lists_max_entries))
            yield '\n'
        yield '\n#### IP Access-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-access-lists.j2', 'documentation/ip-access-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=19&10=22&14=25&20=28'