from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/dns-domain.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dns_domain = resolve('dns_domain')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='dns_domain') if l_0_dns_domain is missing else l_0_dns_domain)):
        pass
        yield '\n### DNS Domain\n\nDNS domain: '
        yield str((undefined(name='dns_domain') if l_0_dns_domain is missing else l_0_dns_domain))
        yield '\n\n#### DNS Domain Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/dns-domain.j2', 'documentation/dns-domain.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '!\n```\n'

blocks = {}
debug_info = '7=18&11=21&16=23'