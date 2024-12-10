from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-domain-lookup.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_domain_lookup = resolve('ip_domain_lookup')
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
    if t_3((undefined(name='ip_domain_lookup') if l_0_ip_domain_lookup is missing else l_0_ip_domain_lookup)):
        pass
        yield '\n### Domain Lookup\n\n#### DNS Domain Lookup Summary\n\n| Source interface | vrf |\n| ---------------- | --- |\n'
        for l_1_source in t_2(environment.getattr((undefined(name='ip_domain_lookup') if l_0_ip_domain_lookup is missing else l_0_ip_domain_lookup), 'source_interfaces'), 'name'):
            l_1_vrf = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_source, 'vrf'), '-')
            _loop_vars['vrf'] = l_1_vrf
            yield '| '
            yield str(environment.getattr(l_1_source, 'name'))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' |\n'
        l_1_source = l_1_vrf = missing
        yield '\n#### DNS Domain Lookup Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-domain-lookup.j2', 'documentation/ip-domain-lookup.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=30&15=33&16=37&17=40&23=46'