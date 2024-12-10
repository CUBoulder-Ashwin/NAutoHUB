from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-domain-lookup.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_domain_lookup = resolve('ip_domain_lookup')
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
    if t_2((undefined(name='ip_domain_lookup') if l_0_ip_domain_lookup is missing else l_0_ip_domain_lookup)):
        pass
        for l_1_source in t_1(environment.getattr((undefined(name='ip_domain_lookup') if l_0_ip_domain_lookup is missing else l_0_ip_domain_lookup), 'source_interfaces'), 'name'):
            l_1_ip_domain_cli = missing
            _loop_vars = {}
            pass
            l_1_ip_domain_cli = 'ip domain lookup'
            _loop_vars['ip_domain_cli'] = l_1_ip_domain_cli
            if t_2(environment.getattr(l_1_source, 'vrf')):
                pass
                l_1_ip_domain_cli = str_join(((undefined(name='ip_domain_cli') if l_1_ip_domain_cli is missing else l_1_ip_domain_cli), ' vrf ', environment.getattr(l_1_source, 'vrf'), ))
                _loop_vars['ip_domain_cli'] = l_1_ip_domain_cli
            l_1_ip_domain_cli = str_join(((undefined(name='ip_domain_cli') if l_1_ip_domain_cli is missing else l_1_ip_domain_cli), ' source-interface ', environment.getattr(l_1_source, 'name'), ))
            _loop_vars['ip_domain_cli'] = l_1_ip_domain_cli
            yield str((undefined(name='ip_domain_cli') if l_1_ip_domain_cli is missing else l_1_ip_domain_cli))
            yield '\n'
        l_1_source = l_1_ip_domain_cli = missing

blocks = {}
debug_info = '7=24&8=26&9=30&10=32&11=34&13=36&14=38'