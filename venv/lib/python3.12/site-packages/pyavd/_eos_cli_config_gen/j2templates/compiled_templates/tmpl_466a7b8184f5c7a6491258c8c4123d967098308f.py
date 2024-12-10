from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/interface-profiles.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_interface_profiles = resolve('interface_profiles')
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
    if t_2((undefined(name='interface_profiles') if l_0_interface_profiles is missing else l_0_interface_profiles)):
        pass
        yield '\n### Interface Profiles\n\n#### Interface Profiles Summary\n\n'
        for l_1_interface_profile in t_1((undefined(name='interface_profiles') if l_0_interface_profiles is missing else l_0_interface_profiles), 'name'):
            _loop_vars = {}
            pass
            yield '- '
            yield str(environment.getattr(l_1_interface_profile, 'name'))
            yield '\n'
        l_1_interface_profile = missing
        yield '\n#### Interface Profiles Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/interface-profiles.j2', 'documentation/interface-profiles.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=24&13=27&14=31&20=35'