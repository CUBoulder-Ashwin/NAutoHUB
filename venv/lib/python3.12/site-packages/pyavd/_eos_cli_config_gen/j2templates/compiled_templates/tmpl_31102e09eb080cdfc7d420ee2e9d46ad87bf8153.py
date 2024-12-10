from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/mpls-and-ldp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mpls = resolve('mpls')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls)):
        pass
        yield '\n### MPLS and LDP\n\n#### MPLS and LDP Summary\n\n| Setting | Value |\n| -------- | ---- |\n| MPLS IP Enabled | '
        yield str(t_1(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ip'), '-'))
        yield ' |\n| LDP Enabled | '
        yield str((not t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'shutdown'), '-')))
        yield ' |\n| LDP Router ID | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'router_id'), '-'))
        yield ' |\n| LDP Interface Disabled Default | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'interface_disabled_default'), '-'))
        yield ' |\n| LDP Transport-Address Interface | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'ldp'), 'transport_address_interface'), '-'))
        yield ' |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'fragmentation_needed_tunneling')):
            pass
            yield '| ICMP Fragmentation-Needed Tunneling Enabled | '
            yield str(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'fragmentation_needed_tunneling'))
            yield ' |\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'ttl_exceeded_tunneling')):
            pass
            yield '| ICMP TTL-Exceeded Tunneling Enabled | '
            yield str(environment.getattr(environment.getattr((undefined(name='mpls') if l_0_mpls is missing else l_0_mpls), 'icmp'), 'ttl_exceeded_tunneling'))
            yield ' |\n'
        yield '\n#### MPLS and LDP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/mpls.j2', 'documentation/mpls-and-ldp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&15=27&16=29&17=31&18=33&19=35&20=37&21=40&23=42&24=45&30=48'