from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/boot.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_boot = resolve('boot')
    l_0_method = resolve('method')
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
    if t_2((undefined(name='boot') if l_0_boot is missing else l_0_boot)):
        pass
        yield '\n## System Boot Settings\n'
        if t_2(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret'), 'key')):
                pass
                yield '\n### Boot Secret Summary\n'
                l_0_method = str_join((t_1(environment.getattr(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret'), 'hash_algorithm'), 'sha512'), ' hashed', ))
                context.vars['method'] = l_0_method
                context.exported_vars.add('method')
                yield '\n- The '
                yield str((undefined(name='method') if l_0_method is missing else l_0_method))
                yield ' Aboot password is configured\n'
        yield '\n### System Boot Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/boot.j2', 'documentation/boot.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'method': l_0_method})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '7=25&10=28&11=30&14=33&16=37&23=40'